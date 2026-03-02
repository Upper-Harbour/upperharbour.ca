#!/usr/bin/env python3
"""
apply_db_updates.py — Close the saas-db.js auto-update loop.

Reads approved alerts from db-alerts.json, applies matching updates
to saas-db.js, marks alerts as "applied", and optionally commits
the changes to the repo.

Uses Node.js to parse saas-db.js (since it's a JavaScript file with
JS-native syntax — unquoted keys, comments, apostrophes in values —
that can't be reliably regex-converted to JSON).

Designed to run inside the approve-db-update.yml GitHub Actions workflow
or locally for testing.

Usage:
    python apply_db_updates.py                    # dry-run by default
    python apply_db_updates.py --apply            # write changes
    python apply_db_updates.py --apply --commit   # write + git commit/push
"""

import json
import sys
import subprocess
import argparse
from datetime import datetime, timezone
from pathlib import Path


# ── Paths (relative to repo root) ────────────────────────────────────────────

REPO_ROOT = Path(__file__).resolve().parent
SAAS_DB_PATH = REPO_ROOT / "saas-db.js"
DB_ALERTS_PATH = REPO_ROOT / "db-alerts.json"

# Fields in saas-db.js entries that alerts are allowed to update
UPDATABLE_FIELDS = {
    "parent",
    "hq",
    "jurisdiction",
    "cloudAct",
    "dataResidency",
    "risk",
    "note",
    "category",
    "name",  # rare — renames
}

# Map snake_case and alternate names from pipeline to saas-db.js camelCase field names
FIELD_ALIASES = {
    "data_residency": "dataResidency",
    "cloud_act": "cloudAct",
    "data_residency_option": "dataResidency",
    "dataresidency": "dataResidency",
    "cloudact": "cloudAct",
}

def normalize_field(field: str) -> str:
    """Normalize a field name from pipeline format to saas-db.js format."""
    return FIELD_ALIASES.get(field, field)


# ── Parse saas-db.js via Node.js ──────────────────────────────────────────────

def read_saas_db(path: Path) -> list[dict]:
    """Parse the saasDB variable from a .js file using Node.js."""
    node_script = f"""
    const fs = require('fs');
    const raw = fs.readFileSync({json.dumps(str(path))}, 'utf8');
    eval(raw);
    if (!Array.isArray(saasDB)) {{
        process.stderr.write('saasDB is not an array');
        process.exit(1);
    }}
    process.stdout.write(JSON.stringify(saasDB));
    """

    result = subprocess.run(
        ["node", "-e", node_script],
        capture_output=True, text=True,
    )

    if result.returncode != 0:
        raise ValueError(
            f"Node.js failed to parse {path}:\n"
            f"  stderr: {result.stderr.strip()}"
        )

    data = json.loads(result.stdout)
    if not isinstance(data, list):
        raise ValueError(f"saasDB is not an array, got {type(data).__name__}")

    return data


def write_saas_db(path: Path, data: list[dict]) -> None:
    """Write the saasDB array back to the .js file.

    Produces compact single-line-per-entry format matching the original style:
        var saasDB = [
          { name:"Slack", parent:"Salesforce Inc.", ... },
          ...
        ];

    Data is passed via stdin to avoid OS argument length limits.
    """
    node_script = """
    let chunks = [];
    process.stdin.on('data', c => chunks.push(c));
    process.stdin.on('end', () => {
        const data = JSON.parse(chunks.join(''));
        const lines = data.map(entry => {
            const pairs = Object.entries(entry).map(([k, v]) => {
                return k + ':' + JSON.stringify(v);
            });
            return '      { ' + pairs.join(', ') + ' }';
        });
        const output = '    var saasDB = [\\n' + lines.join(',\\n') + '\\n    ];\\n';
        process.stdout.write(output);
    });
    """

    result = subprocess.run(
        ["node", "-e", node_script],
        input=json.dumps(data),
        capture_output=True, text=True,
    )

    if result.returncode != 0:
        raise ValueError(f"Node.js failed to serialize saasDB:\n  {result.stderr.strip()}")

    path.write_text(result.stdout, encoding="utf-8")


# ── Read / write db-alerts.json ───────────────────────────────────────────────

def read_alerts(path: Path) -> list[dict]:
    """Read the alerts array from db-alerts.json."""
    if not path.exists():
        print(f"[warn] {path} does not exist — nothing to apply.")
        return []

    raw = path.read_text(encoding="utf-8")
    if not raw.strip():
        return []

    data = json.loads(raw)
    if isinstance(data, dict) and "alerts" in data:
        return data["alerts"]
    if isinstance(data, list):
        return data

    raise ValueError(f"Unexpected db-alerts.json structure: {type(data)}")


def write_alerts(path: Path, alerts: list[dict]) -> None:
    """Write the alerts back. Preserves wrapper object if one existed."""
    raw = path.read_text(encoding="utf-8") if path.exists() else "[]"
    original = json.loads(raw) if raw.strip() else []

    if isinstance(original, dict) and "alerts" in original:
        original["alerts"] = alerts
        out = original
    else:
        out = alerts

    path.write_text(
        json.dumps(out, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )


# ── Apply updates ─────────────────────────────────────────────────────────────

def find_tool_index(db: list[dict], tool_name: str) -> int | None:
    """Find a tool by name (case-insensitive)."""
    target = tool_name.strip().lower()
    for i, entry in enumerate(db):
        if entry.get("name", "").strip().lower() == target:
            return i
    return None


def apply_alert(db: list[dict], alert: dict) -> tuple[bool, str]:
    """Apply a single approved alert to the database."""
    tool_name = alert.get("tool") or alert.get("tool_name") or alert.get("name") or alert.get("toolName")
    if not tool_name:
        return False, "Alert has no tool/name field — skipping"

    idx = find_tool_index(db, tool_name)
    if idx is None:
        return False, f"Tool '{tool_name}' not found in saas-db.js — skipping"

    updates = alert.get("updates") or alert.get("changes") or {}
    if not updates:
        updates = {
            k: v for k, v in alert.items()
            if k in UPDATABLE_FIELDS
        }

    if not updates:
        return False, f"Alert for '{tool_name}' has no updatable fields — skipping"

    applied_fields = []
    for field, new_value in updates.items():
        norm_field = normalize_field(field)

        # Skip fields that aren't actual saas-db.js fields (e.g. vendor_entry, canadian_sovereign_option)
        if norm_field not in UPDATABLE_FIELDS:
            print(f"  [skip] Field '{field}' (normalized: '{norm_field}') is not updatable")
            continue

        old_value = db[idx].get(norm_field)
        db[idx][norm_field] = new_value
        applied_fields.append(f"{norm_field}: {old_value!r} → {new_value!r}")

    if not applied_fields:
        return False, f"No valid fields to update for '{tool_name}'"

    detail = "; ".join(applied_fields)
    return True, f"Updated '{tool_name}': {detail}"


def run(apply: bool = False, commit: bool = False) -> None:
    """Main execution."""
    print("=" * 60)
    print("apply_db_updates.py")
    print(f"  Mode: {'APPLY' if apply else 'DRY RUN'}")
    print(f"  saas-db.js:    {SAAS_DB_PATH}")
    print(f"  db-alerts.json: {DB_ALERTS_PATH}")
    print("=" * 60)

    # 1. Load
    db = read_saas_db(SAAS_DB_PATH)
    print(f"\nLoaded {len(db)} tools from saas-db.js")

    alerts = read_alerts(DB_ALERTS_PATH)
    approved = [a for a in alerts if a.get("status") == "approved"]
    print(f"Found {len(approved)} approved alert(s) out of {len(alerts)} total\n")

    if not approved:
        print("Nothing to apply. Exiting.")
        return

    # 2. Apply each approved alert
    applied_count = 0
    now = datetime.now(timezone.utc).isoformat()

    for alert in approved:
        tool_label = alert.get("tool") or alert.get("tool_name") or alert.get("name") or "unknown"
        print(f"Processing: {tool_label}")

        success, message = apply_alert(db, alert)
        print(f"  → {message}")

        if success:
            alert["status"] = "applied"
            alert["appliedAt"] = now
            applied_count += 1
        else:
            alert["status"] = "failed"
            alert["failedAt"] = now
            alert["failureReason"] = message

    print(f"\nApplied {applied_count} / {len(approved)} alerts")

    # 3. Write if not dry-run
    if not apply:
        print("\n[DRY RUN] No files written. Use --apply to write changes.")
        return

    write_saas_db(SAAS_DB_PATH, db)
    print(f"Wrote updated saas-db.js ({len(db)} tools)")

    write_alerts(DB_ALERTS_PATH, alerts)
    print(f"Wrote updated db-alerts.json")

    # 4. Git commit + push if requested
    if commit and applied_count > 0:
        _git_commit_and_push(applied_count)


def _git_commit_and_push(count: int) -> None:
    """Commit the updated files and push to origin."""
    try:
        subprocess.run(
            ["git", "config", "user.name", "HarbourScan Pipeline"],
            cwd=REPO_ROOT, check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "config", "user.email", "pipeline@upperharbour.com"],
            cwd=REPO_ROOT, check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "add",
             str(SAAS_DB_PATH.relative_to(REPO_ROOT)),
             str(DB_ALERTS_PATH.relative_to(REPO_ROOT))],
            cwd=REPO_ROOT, check=True, capture_output=True,
        )

        msg = (
            f"chore(saas-db): apply {count} approved alert(s)\n\n"
            f"Auto-applied by apply_db_updates.py at "
            f"{datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}"
        )
        subprocess.run(
            ["git", "commit", "-m", msg],
            cwd=REPO_ROOT, check=True, capture_output=True,
        )
        subprocess.run(
            ["git", "push"],
            cwd=REPO_ROOT, check=True, capture_output=True,
        )
        print(f"Committed and pushed to origin.")
    except subprocess.CalledProcessError as e:
        print(f"[error] Git operation failed: {e}")
        print(f"  stdout: {e.stdout.decode() if e.stdout else ''}")
        print(f"  stderr: {e.stderr.decode() if e.stderr else ''}")
        sys.exit(1)


# ── CLI ───────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Apply approved db-alerts to saas-db.js"
    )
    parser.add_argument(
        "--apply", action="store_true",
        help="Actually write changes (default is dry-run)"
    )
    parser.add_argument(
        "--commit", action="store_true",
        help="Git commit and push after applying (requires --apply)"
    )
    parser.add_argument(
        "--db-path", type=Path, default=None,
        help="Override path to saas-db.js"
    )
    parser.add_argument(
        "--alerts-path", type=Path, default=None,
        help="Override path to db-alerts.json"
    )
    args = parser.parse_args()

    if args.db_path:
        SAAS_DB_PATH = args.db_path.resolve()
    if args.alerts_path:
        DB_ALERTS_PATH = args.alerts_path.resolve()

    run(apply=args.apply, commit=args.commit)
