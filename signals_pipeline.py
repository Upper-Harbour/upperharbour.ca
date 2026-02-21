#!/usr/bin/env python3
"""
Upper Harbour — Signals Pipeline
Runs every 6 hours via GitHub Actions.
Collects, filters, and processes Canadian data sovereignty intelligence.

Flow:
  1. Pull RSS feeds from known sources
  2. Run Claude API web searches for broader coverage
  3. Deduplicate and score for relevance
  4. Claude API rewrites summaries and classifies event type
  5. Detect database update candidates (acquisitions, vendor changes)
  6. Send approval email with approve/reject links
  7. Approved items → signals.json → site renders them

Requirements:
  pip install anthropic feedparser requests

Environment variables:
  ANTHROPIC_API_KEY  — Claude API key
  SMTP_HOST          — Email server (e.g., smtp.gmail.com)
  SMTP_PORT          — Email port (e.g., 587)
  SMTP_USER          — Email address to send from
  SMTP_PASS          — Email password / app password
  APPROVAL_EMAIL     — Your email (josh@upperharbour.ca)
  SIGNALS_JSON_PATH  — Path to signals.json in repo (default: signals.json)
  PENDING_JSON_PATH  — Path to pending.json in repo (default: pending.json)
"""

import os
import json
import hashlib
import logging
import time
from datetime import datetime, timedelta
from typing import Optional

import anthropic
import feedparser
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

# ── Configuration ────────────────────────────────────────────

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")
APPROVAL_EMAIL = os.environ.get("APPROVAL_EMAIL", "josh@upperharbour.ca")
SIGNALS_JSON_PATH = os.environ.get("SIGNALS_JSON_PATH", "signals.json")
PENDING_JSON_PATH = os.environ.get("PENDING_JSON_PATH", "pending.json")

# RSS feeds to monitor
RSS_FEEDS = [
    # Canadian regulators
    {"url": "https://www.cai.gouv.qc.ca/rss", "name": "CAI Quebec", "type_hint": "enforcement"},
    {"url": "https://www.priv.gc.ca/en/opc-news/news-and-announcements/rss/", "name": "OPC Canada", "type_hint": "enforcement"},
    {"url": "https://www.ipc.on.ca/feed/", "name": "IPC Ontario", "type_hint": "policy"},
    {"url": "https://www.oipc.bc.ca/feed/", "name": "OIPC BC", "type_hint": "enforcement"},
    {"url": "https://www.oipc.ab.ca/feed/", "name": "OIPC Alberta", "type_hint": "enforcement"},

    # Government
    {"url": "https://www.canada.ca/en/treasury-board-secretariat.atom", "name": "Treasury Board", "type_hint": "procurement"},
    {"url": "https://www.parl.ca/legisinfo/en/bills/rss", "name": "Parliament of Canada", "type_hint": "legislation"},

    # Tech / legal news
    {"url": "https://betakit.com/feed/", "name": "BetaKit", "type_hint": None},
    {"url": "https://www.itworldcanada.com/feed", "name": "IT World Canada", "type_hint": None},
    {"url": "https://www.lexology.com/feed", "name": "Lexology", "type_hint": None},
    {"url": "https://thelogic.co/feed/", "name": "The Logic", "type_hint": None},

    # Cloud vendor blogs
    {"url": "https://aws.amazon.com/blogs/publicsector/feed/", "name": "AWS Public Sector", "type_hint": "vendor"},
    {"url": "https://azure.microsoft.com/en-us/blog/feed/", "name": "Azure Blog", "type_hint": "vendor"},
    {"url": "https://cloud.google.com/blog/rss", "name": "Google Cloud Blog", "type_hint": "vendor"},
]

# Web search queries (run via Claude API with web search tool)
SEARCH_QUERIES = [
    "CLOUD Act Canada data sovereignty 2026",
    "Law 25 Quebec enforcement action",
    "PIPEDA CPPA privacy reform Canada",
    "Canadian SaaS company acquisition",
    "Canada data residency announcement",
    "government procurement data sovereignty Canada",
    "transfer impact assessment Canada",
    "Canadian privacy commissioner order",
    "data localization Canada policy",
    "SaaS vendor Canadian data centre",
]

# Relevance keywords for filtering
RELEVANCE_KEYWORDS = [
    "data sovereignty", "cloud act", "law 25", "pipeda", "cppa",
    "data residency", "data localization", "transfer impact assessment",
    "cross-border data", "privacy commissioner", "enforcement order",
    "saas", "cloud computing", "data protection", "procurement",
    "jurisdictional", "foreign jurisdiction", "acquisition",
    "data centre canada", "data center canada", "canadian privacy",
]

# Event type classification
EVENT_TYPES = ["enforcement", "acquisition", "legislation", "vendor", "procurement", "policy"]


# ── RSS Collection ───────────────────────────────────────────

def collect_rss() -> list[dict]:
    """Pull items from all RSS feeds, filter by recency and relevance."""
    items = []
    cutoff = datetime.now() - timedelta(hours=72)  # Last 72 hours

    for feed_config in RSS_FEEDS:
        try:
            feed = feedparser.parse(feed_config["url"])
            for entry in feed.entries[:20]:  # Max 20 per feed
                # Parse date
                published = None
                if hasattr(entry, 'published_parsed') and entry.published_parsed:
                    published = datetime(*entry.published_parsed[:6])
                elif hasattr(entry, 'updated_parsed') and entry.updated_parsed:
                    published = datetime(*entry.updated_parsed[:6])

                # Skip old items
                if published and published < cutoff:
                    continue

                title = entry.get('title', '')
                summary = entry.get('summary', entry.get('description', ''))
                link = entry.get('link', '')

                # Basic relevance check
                text = (title + ' ' + summary).lower()
                if not any(kw in text for kw in RELEVANCE_KEYWORDS):
                    continue

                items.append({
                    "source": feed_config["name"],
                    "source_url": link,
                    "title": title,
                    "raw_summary": summary[:500],
                    "date": published.strftime("%Y-%m-%d") if published else datetime.now().strftime("%Y-%m-%d"),
                    "type_hint": feed_config["type_hint"],
                    "origin": "rss"
                })

            log.info(f"RSS: {feed_config['name']} — {len(feed.entries)} entries, {sum(1 for i in items if i['source'] == feed_config['name'])} relevant")

        except Exception as e:
            log.warning(f"RSS failed for {feed_config['name']}: {e}")

    return items


# ── Web Search Collection ────────────────────────────────────

def collect_web_search() -> list[dict]:
    """Run web searches via Claude API with web search tool."""
    if not ANTHROPIC_API_KEY:
        log.warning("No ANTHROPIC_API_KEY — skipping web search")
        return []

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    items = []

    for idx, query in enumerate(SEARCH_QUERIES):
        if idx > 0:
            time.sleep(60)  # Wait full minute to reset rate limit window
        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=2000,
                tools=[{"type": "web_search_20250305", "name": "web_search"}],
                messages=[{
                    "role": "user",
                    "content": f"""Search for: {query}

Return ONLY items from the last 48 hours that are directly relevant to Canadian data sovereignty, privacy law enforcement, SaaS vendor jurisdictional changes, or government procurement policy.

For each relevant result, return a JSON array with objects containing:
- "title": the headline
- "summary": 1-2 sentence summary of the development
- "source": publication name
- "source_url": URL
- "date": date in YYYY-MM-DD format

If nothing relevant is found, return an empty array: []

Return ONLY the JSON array, nothing else."""
                }]
            )

            # Extract text from response
            text = ""
            for block in response.content:
                if hasattr(block, 'text'):
                    text += block.text

            # Parse JSON from response
            text = text.strip().strip('```json').strip('```').strip()
            if text.startswith('['):
                results = json.loads(text)
                for r in results:
                    items.append({
                        "source": r.get("source", "Web"),
                        "source_url": r.get("source_url", ""),
                        "title": r.get("title", ""),
                        "raw_summary": r.get("summary", ""),
                        "date": r.get("date", datetime.now().strftime("%Y-%m-%d")),
                        "type_hint": None,
                        "origin": "search"
                    })

            log.info(f"Search: '{query}' — {len(results) if text.startswith('[') else 0} results")

        except Exception as e:
            log.warning(f"Search failed for '{query}': {e}")

    return items


# ── Deduplication ────────────────────────────────────────────

def deduplicate(items: list[dict]) -> list[dict]:
    """Remove duplicate items based on title similarity."""
    seen = set()
    unique = []

    for item in items:
        # Create a fingerprint from normalized title
        title_norm = item["title"].lower().strip()
        title_hash = hashlib.md5(title_norm[:60].encode()).hexdigest()

        if title_hash not in seen:
            seen.add(title_hash)
            unique.append(item)

    log.info(f"Dedup: {len(items)} → {len(unique)} unique items")
    return unique


# ── Claude Processing ────────────────────────────────────────

def process_with_claude(items: list[dict]) -> list[dict]:
    """
    Send items to Claude for:
    1. Final relevance filtering
    2. Summary rewriting in Upper Harbour voice
    3. Event type classification
    4. Database update detection
    """
    if not ANTHROPIC_API_KEY or not items:
        return []

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # Process in batches of 10
    processed = []
    for i in range(0, len(items), 10):
        if i > 0:
            time.sleep(15)  # Avoid rate limiting
        batch = items[i:i+10]

        items_text = json.dumps([{
            "title": item["title"],
            "summary": item["raw_summary"],
            "source": item["source"],
            "source_url": item["source_url"],
            "date": item["date"],
        } for item in batch], indent=2)

        try:
            response = client.messages.create(
                model="claude-sonnet-4-20250514",
                max_tokens=4000,
                messages=[{
                    "role": "user",
                    "content": f"""You are the intelligence processor for Upper Harbour, a Canadian data sovereignty research organization.

Review these news items and process ONLY the ones that are directly relevant to Canadian data sovereignty. Discard anything that is:
- General tech news without sovereignty implications
- US or EU privacy news that doesn't affect Canada
- Product announcements without jurisdictional relevance
- Duplicate or trivial updates

For each relevant item, return a JSON array with objects containing:
- "headline": Rewritten headline — factual, concise, no clickbait. Written as Upper Harbour would write it.
- "summary": 2-3 sentence summary in Upper Harbour's voice — precise, analytical, focused on jurisdictional implications. Do not editorialize. State what happened and what it means for Canadian organizations.
- "type": One of: enforcement, acquisition, legislation, vendor, procurement, policy
- "source": Original source name
- "source_url": Original URL
- "date": YYYY-MM-DD
- "impact": Geographic scope — e.g., "QC", "ON", "Federal", "All provinces"
- "db_update": If this event should trigger a change in our SaaS database (e.g., a company was acquired, a vendor added Canadian data residency), include an object with:
  - "tool_name": Name of the SaaS tool affected
  - "change": What changed (e.g., "parent_company", "data_residency", "risk_status")
  - "old_value": Previous value (if known)
  - "new_value": New value
  - "reason": Brief explanation
  Otherwise set db_update to null.

Items to process:
{items_text}

Return ONLY the JSON array. If no items are relevant, return: []"""
                }]
            )

            text = ""
            for block in response.content:
                if hasattr(block, 'text'):
                    text += block.text

            text = text.strip().strip('```json').strip('```').strip()
            if text.startswith('['):
                results = json.loads(text)
                processed.extend(results)
                log.info(f"Claude processed batch: {len(batch)} in → {len(results)} relevant")

        except Exception as e:
            log.warning(f"Claude processing failed: {e}")

    return processed


# ── Approval Email ───────────────────────────────────────────

def send_approval_email(signals: list[dict]):
    """Send an HTML email with approve/reject for each signal."""
    if not SMTP_USER or not SMTP_PASS:
        log.warning("No SMTP credentials — skipping email")
        # Write to pending.json instead
        save_pending(signals)
        return

    if not signals:
        log.info("No new signals to approve")
        return

    # Build HTML email
    now = datetime.now().strftime("%B %d, %Y — %H:%M ET")
    db_updates = [s for s in signals if s.get("db_update")]

    html = f"""
    <html>
    <head>
      <style>
        body {{ font-family: -apple-system, 'Segoe UI', Helvetica, Arial, sans-serif; background: #0A1018; color: #EAF0F4; padding: 32px; }}
        .container {{ max-width: 640px; margin: 0 auto; }}
        h1 {{ font-size: 22px; font-weight: 700; margin-bottom: 4px; }}
        .subtitle {{ font-size: 13px; color: #7A92A8; margin-bottom: 32px; }}
        .signal {{ background: #0F1C2E; border: 1px solid rgba(234,240,244,0.1); border-radius: 8px; padding: 20px; margin-bottom: 16px; }}
        .signal h3 {{ font-size: 16px; margin: 0 0 8px 0; color: #EAF0F4; }}
        .signal p {{ font-size: 14px; color: #7A92A8; line-height: 1.6; margin: 0 0 12px 0; }}
        .meta {{ font-size: 11px; color: #6B7B8D; }}
        .badge {{ display: inline-block; font-size: 10px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.08em; padding: 3px 8px; border-radius: 3px; margin-right: 8px; }}
        .badge-enforcement {{ background: rgba(224,96,80,0.15); color: #E06050; }}
        .badge-acquisition {{ background: rgba(201,168,76,0.15); color: #C9A84C; }}
        .badge-legislation {{ background: rgba(60,184,176,0.15); color: #3CB8B0; }}
        .badge-vendor {{ background: rgba(139,159,232,0.15); color: #8B9FE8; }}
        .badge-procurement {{ background: rgba(196,144,209,0.15); color: #C490D1; }}
        .badge-policy {{ background: rgba(234,240,244,0.08); color: #EAF0F4; }}
        .db-alert {{ background: rgba(60,184,176,0.08); border: 1px solid rgba(60,184,176,0.2); border-radius: 4px; padding: 10px 14px; margin-top: 10px; font-size: 12px; color: #3CB8B0; }}
        .actions {{ margin-top: 12px; }}
        .btn {{ display: inline-block; font-size: 12px; font-weight: 700; text-decoration: none; padding: 8px 20px; border-radius: 4px; margin-right: 8px; }}
        .btn-approve {{ background: #3CB8B0; color: #0A1018; }}
        .btn-reject {{ background: transparent; border: 1px solid rgba(234,240,244,0.15); color: #7A92A8; }}
        .summary {{ background: #131E2D; border-radius: 8px; padding: 16px 20px; margin-bottom: 24px; }}
        .summary h2 {{ font-size: 14px; color: #3CB8B0; margin: 0 0 8px 0; }}
        .summary p {{ font-size: 13px; color: #7A92A8; margin: 0; }}
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Signals — Approval Queue</h1>
        <p class="subtitle">{now} &middot; {len(signals)} items pending &middot; {len(db_updates)} database updates</p>

        <div class="summary">
          <h2>Quick Summary</h2>
          <p>{len(signals)} new signals detected. Review each below and reply with the numbers you want to approve. Items not approved within 24 hours are discarded.</p>
        </div>
    """

    for idx, signal in enumerate(signals):
        badge_cls = f"badge-{signal.get('type', 'policy')}"
        html += f"""
        <div class="signal">
          <span class="badge {badge_cls}">{signal.get('type', 'policy')}</span>
          <span class="meta">{signal.get('date', '')} &middot; {signal.get('source', '')}</span>
          <h3>{signal.get('headline', '')}</h3>
          <p>{signal.get('summary', '')}</p>
          <div class="meta">Impact: {signal.get('impact', 'TBD')} &middot; <a href="{signal.get('source_url', '#')}" style="color:#3CB8B0;">View source</a></div>
        """

        if signal.get("db_update"):
            db = signal["db_update"]
            html += f"""
          <div class="db-alert">
            ⟳ Database update: <strong>{db.get('tool_name', '?')}</strong> — {db.get('change', '?')}: {db.get('old_value', '?')} → {db.get('new_value', '?')}
            <br/>{db.get('reason', '')}
          </div>
            """

        html += f"""
          <div class="actions">
            <span style="font-size:13px;font-weight:700;color:#EAF0F4;">#{idx + 1}</span>
          </div>
        </div>
        """

    html += """
        <div class="summary" style="margin-top:32px;">
          <h2>How to Approve</h2>
          <p>Reply to this email with the numbers of the signals you want to publish. Example: "Approve 1, 2, 4" or "Approve all" or "Reject all".</p>
        </div>
      </div>
    </body>
    </html>
    """

    # Send email
    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Signals: {len(signals)} items pending — {now}"
    msg['From'] = SMTP_USER
    msg['To'] = APPROVAL_EMAIL
    msg.attach(MIMEText(html, 'html'))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        log.info(f"Approval email sent to {APPROVAL_EMAIL}")
    except Exception as e:
        log.error(f"Email failed: {e}")
        save_pending(signals)


# ── File I/O ─────────────────────────────────────────────────

def load_existing_signals() -> dict:
    """Load the current signals.json."""
    if os.path.exists(SIGNALS_JSON_PATH):
        with open(SIGNALS_JSON_PATH) as f:
            return json.load(f)
    return {"meta": {}, "signals": []}


def save_signals(data: dict):
    """Write signals.json."""
    with open(SIGNALS_JSON_PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    log.info(f"Saved {len(data.get('signals', []))} signals to {SIGNALS_JSON_PATH}")


def save_pending(signals: list[dict]):
    """Save pending signals for manual approval."""
    with open(PENDING_JSON_PATH, 'w') as f:
        json.dump({"pending": signals, "created": datetime.now().isoformat()}, f, indent=2, ensure_ascii=False)
    log.info(f"Saved {len(signals)} pending signals to {PENDING_JSON_PATH}")


def load_pending() -> list[dict]:
    """Load pending signals."""
    if os.path.exists(PENDING_JSON_PATH):
        with open(PENDING_JSON_PATH) as f:
            data = json.load(f)
        return data.get("pending", [])
    return []


# ── Approval Handler ─────────────────────────────────────────

def approve_signals(approved_indices: list[int]):
    """
    Move approved signals from pending to published.
    Called by the approval webhook or manual script.
    """
    pending = load_pending()
    existing = load_existing_signals()

    approved = []
    for idx in approved_indices:
        if 0 <= idx < len(pending):
            signal = pending[idx]
            # Convert to published format
            published = {
                "headline": signal.get("headline", ""),
                "summary": signal.get("summary", ""),
                "type": signal.get("type", "policy"),
                "source": signal.get("source", ""),
                "sourceUrl": signal.get("source_url", ""),
                "date": signal.get("date", ""),
                "impact": signal.get("impact", ""),
                "dbUpdate": signal.get("db_update") is not None,
            }
            approved.append(published)

    # Add to existing signals (newest first)
    existing["signals"] = approved + existing.get("signals", [])

    # Keep max 200 signals
    existing["signals"] = existing["signals"][:200]

    # Update meta
    existing["meta"] = {
        "lastUpdated": datetime.now().strftime("%b %d, %Y — %H:%M ET"),
        "sourceCount": f"{len(RSS_FEEDS) + len(SEARCH_QUERIES)}+",
    }

    save_signals(existing)

    # Clear pending
    if os.path.exists(PENDING_JSON_PATH):
        os.remove(PENDING_JSON_PATH)

    log.info(f"Published {len(approved)} signals")
    return approved


# ── Main Pipeline ────────────────────────────────────────────

def run_pipeline():
    """Main entry point — runs the full collection and processing pipeline."""
    log.info("=" * 60)
    log.info("SIGNALS PIPELINE — Starting")
    log.info("=" * 60)

    # 1. Collect from RSS
    log.info("Step 1: Collecting RSS feeds...")
    rss_items = collect_rss()

    # 2. Collect from web search
    log.info("Step 2: Running web searches...")
    search_items = collect_web_search()

    # 3. Combine and deduplicate
    all_items = rss_items + search_items
    log.info(f"Total raw items: {len(all_items)} (RSS: {len(rss_items)}, Search: {len(search_items)})")
    unique_items = deduplicate(all_items)

    if not unique_items:
        log.info("No new relevant items found. Done.")
        return

    # 4. Process with Claude
    log.info("Step 3: Processing with Claude...")
    processed = process_with_claude(unique_items)
    log.info(f"Processed: {len(processed)} relevant signals")

    if not processed:
        log.info("No items passed relevance filter. Done.")
        return

    # 5. Check against existing signals (avoid re-publishing)
    existing = load_existing_signals()
    existing_headlines = {s.get("headline", "").lower() for s in existing.get("signals", [])}
    new_signals = [s for s in processed if s.get("headline", "").lower() not in existing_headlines]
    log.info(f"After dedup against existing: {len(new_signals)} new signals")

    if not new_signals:
        log.info("All items already published. Done.")
        return

    # 6. Send approval email
    log.info("Step 4: Sending approval email...")
    send_approval_email(new_signals)

    log.info("=" * 60)
    log.info(f"PIPELINE COMPLETE — {len(new_signals)} items pending approval")
    log.info("=" * 60)


# ── CLI ──────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "collect":
            # Run the full pipeline
            run_pipeline()

        elif command == "approve":
            # Approve specific signals: python signals.py approve 1 2 4
            indices = [int(x) - 1 for x in sys.argv[2:]]  # Convert to 0-indexed
            approved = approve_signals(indices)
            print(f"Approved {len(approved)} signals")

        elif command == "approve-all":
            pending = load_pending()
            indices = list(range(len(pending)))
            approved = approve_signals(indices)
            print(f"Approved all {len(approved)} signals")

        elif command == "reject-all":
            if os.path.exists(PENDING_JSON_PATH):
                os.remove(PENDING_JSON_PATH)
            print("All pending signals rejected")

        elif command == "status":
            pending = load_pending()
            existing = load_existing_signals()
            print(f"Published signals: {len(existing.get('signals', []))}")
            print(f"Pending approval: {len(pending)}")

        else:
            print(f"Unknown command: {command}")
            print("Usage: python signals_pipeline.py [collect|approve N N N|approve-all|reject-all|status]")
    else:
        run_pipeline()
