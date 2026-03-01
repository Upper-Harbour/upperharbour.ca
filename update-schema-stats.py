#!/usr/bin/env python3
"""
Upper Harbour — Schema Stats Updater

Run from your repo folder after editing saas-db.js:
    python3 update-schema-stats.py

Updates all hardcoded numbers inside JSON-LD schema blocks
and meta tags across every HTML file in the site.
"""

import os
import re
import json

# ── Parse saas-db.js ────────────────────────────────────────
def parse_database():
    db_path = 'saas-db.js'
    if not os.path.exists(db_path):
        print(f"ERROR: Can't find {db_path}")
        print("Make sure you're running this from your repo folder.")
        exit(1)

    content = open(db_path, 'r').read()

    # Count everything with regex — much more reliable than trying to parse JS as JSON
    total = len(re.findall(r'\{\s*name:', content))
    us_count = len(re.findall(r'jurisdiction:"United States"', content))
    ca_count = len(re.findall(r'jurisdiction:"Canada"', content))
    cloud_act = len(re.findall(r'cloudAct:true', content))
    canadian = len(re.findall(r'risk:"canadian"', content))
    review = len(re.findall(r'risk:"review"', content))
    non_exposed = len(re.findall(r'risk:"non_exposed"', content))
    exposed = len(re.findall(r'risk:"exposed"', content))
    categories = set(re.findall(r'category:"([^"]+)"', content))

    # Count CA-resident non-canadian tools that are CLOUD Act exposed
    # Extract each tool block and check
    ca_res_total = 0
    ca_res_exposed = 0
    tool_blocks = re.findall(r'\{[^{}]+\}', content)
    ca_keywords = ['canada', 'ca-central', 'montreal', 'montréal', 'toronto']
    for block in tool_blocks:
        if 'name:' not in block:
            continue
        risk_match = re.search(r'risk:"(\w+)"', block)
        if not risk_match or risk_match.group(1) == 'canadian':
            continue
        res_match = re.search(r'dataResidency:"([^"]*)"', block)
        if res_match:
            res = res_match.group(1).lower()
            if any(kw in res for kw in ca_keywords):
                ca_res_total += 1
                if 'cloudAct:true' in block:
                    ca_res_exposed += 1

    return {
        'total': total,
        'catCount': len(categories),
        'usCount': us_count,
        'cdnCount': ca_count,
        'cloudActCount': cloud_act,
        'canadianCount': canadian,
        'reviewCount': review,
        'nonExposedCount': non_exposed,
        'exposedCount': exposed,
        'caResTotal': ca_res_total,
        'caResExposed': ca_res_exposed,
    }


def compute_stats(db):
    total = db['total']
    foreign_count = total - db['cdnCount']

    stats = {
        'total': total,
        'catCount': db['catCount'],
        'usCount': db['usCount'],
        'usPct': round(db['usCount'] / total * 100),
        'foreignPct': round(foreign_count / total * 100),
        'cloudActPct': round(db['cloudActCount'] / total * 100),
        'canadianPct': round(db['canadianCount'] / total * 100),
        'reviewPct': round(db['reviewCount'] / total * 100),
        'nonExposedPct': round(db['nonExposedCount'] / total * 100),
        'exposedPct': round(db['exposedCount'] / total * 100),
        'nonCanadianPct': 100 - round(db['canadianCount'] / total * 100),
        'caResExposedPct': round(db['caResExposed'] / db['caResTotal'] * 100) if db['caResTotal'] > 0 else 0,
    }
    return stats


# ── Load previous values ────────────────────────────────────
def load_old_values():
    ref_path = os.path.join('assets', 'schema-stats-ref.json')
    if os.path.exists(ref_path):
        old = json.load(open(ref_path))
        print('Loaded previous values from schema-stats-ref.json')
        return old
    else:
        print('No reference file found — using initial values (first run)')
        return {
            'total': 693,
            'catCount': 30,
            'usCount': 453,
            'usPct': 65,
            'canadianPct': 18,
            'reviewPct': 11,
            'nonExposedPct': 15,
            'exposedPct': 54,
            'nonCanadianPct': 82,
            'caResExposedPct': 89,
        }


# ── Update HTML files ───────────────────────────────────────
def find_html_files():
    results = []
    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != '__MACOSX' and d != 'node_modules']
        for f in files:
            if f.endswith('.html'):
                results.append(os.path.join(root, f))
    return results


def update_file(filepath, old, stats):
    content = open(filepath, 'r').read()
    original = content
    changes = 0

    # Find all JSON-LD blocks and update numbers inside them
    def replace_schema(match):
        nonlocal changes
        schema_content = match.group(1)
        updated = schema_content

        # Replace tool count — any instance of old total followed by a space or hyphen
        if old['total'] != stats['total']:
            pattern = re.compile(r'\b' + str(old['total']) + r'\b(?=\+?\s|\+-)')
            count_before = len(pattern.findall(updated))
            updated = pattern.sub(str(stats['total']), updated)
            changes += count_before

        # Replace category count
        if old['catCount'] != stats['catCount']:
            old_pat = f"{old['catCount']} categories"
            new_pat = f"{stats['catCount']} categories"
            count_before = updated.count(old_pat)
            updated = updated.replace(old_pat, new_pat)
            changes += count_before

        # Replace "approximately N tools"
        if old['usCount'] != stats.get('usCount', old['usCount']):
            old_pat = f"approximately {old['usCount']} tools"
            new_pat = f"approximately {stats['usCount']} tools"
            count_before = updated.count(old_pat)
            updated = updated.replace(old_pat, new_pat)
            changes += count_before

        # Percentage replacements with context matching
        pct_replacements = [
            (old['usPct'], stats['usPct'], r'(\b)' + str(old['usPct']) + r'(%[^"]*?(?:parented|subject|tools))'),
            (old['canadianPct'], stats['canadianPct'], r'(\b)' + str(old['canadianPct']) + r'(%[^"]*?(?:Canadian|are Canadian))'),
            (old['reviewPct'], stats['reviewPct'], r'(\b)' + str(old['reviewPct']) + r'(%[^"]*?(?:review|require|caution))'),
            (old['nonExposedPct'], stats['nonExposedPct'], r'(\b)' + str(old['nonExposedPct']) + r'(%[^"]*?(?:non-US|foreign vendor))'),
            (old['exposedPct'], stats['exposedPct'], r'(\b)' + str(old['exposedPct']) + r'(%[^"]*?(?:CLOUD Act|exposed))'),
            (old['nonCanadianPct'], stats['nonCanadianPct'], r'(\b)' + str(old['nonCanadianPct']) + r'(%[^"]*?(?:disqualify|tools Canadian))'),
            (old['caResExposedPct'], stats['caResExposedPct'], r'(\b)' + str(old['caResExposedPct']) + r'(%[^"]*?(?:tools offering|tools with|residency))'),
        ]

        for old_val, new_val, pattern in pct_replacements:
            if old_val != new_val:
                def do_replace(m):
                    nonlocal changes
                    changes += 1
                    return m.group(1) + str(new_val) + m.group(2)
                updated = re.sub(pattern, do_replace, updated)

        return f'<script type="application/ld+json">{updated}</script>'

    content = re.sub(
        r'<script\s+type="application/ld\+json">([\s\S]*?)</script>',
        replace_schema,
        content
    )

    # Also update meta tags with exact old total
    if old['total'] != stats['total']:
        def replace_meta(m):
            nonlocal changes
            if 'Nearly' in m.group(0):
                return m.group(0)  # Skip approximate ones
            changes += 1
            return m.group(1) + str(stats['total']) + m.group(2)
        content = re.sub(
            r'(content="[^"]*?)\b' + str(old['total']) + r'\b([^"]*?")',
            replace_meta,
            content
        )

    if content != original:
        open(filepath, 'w').write(content)
        rel = filepath.replace('./', '')
        print(f'  UPDATED: {rel} ({changes} replacements)')
        return changes
    return 0


# ── Save reference file ─────────────────────────────────────
def save_reference(stats):
    ref_path = os.path.join('assets', 'schema-stats-ref.json')
    ref = {
        '_note': 'Auto-generated by update-schema-stats.py. Do not edit.',
        'total': stats['total'],
        'catCount': stats['catCount'],
        'usCount': stats.get('usCount', 0),
        'usPct': stats['usPct'],
        'canadianPct': stats['canadianPct'],
        'reviewPct': stats['reviewPct'],
        'nonExposedPct': stats['nonExposedPct'],
        'exposedPct': stats['exposedPct'],
        'nonCanadianPct': stats['nonCanadianPct'],
        'caResExposedPct': stats['caResExposedPct'],
    }
    open(ref_path, 'w').write(json.dumps(ref, indent=2))
    print(f'\nReference file saved to {ref_path}')


# ── Main ────────────────────────────────────────────────────
if __name__ == '__main__':
    print('Reading saas-db.js...\n')
    db = parse_database()
    stats = compute_stats(db)

    print(f'  Total tools: {stats["total"]}')
    print(f'  Categories: {stats["catCount"]}')
    print(f'  US-parented: {stats["usPct"]}%')
    print(f'  CLOUD Act exposed: {stats["cloudActPct"]}%')
    print(f'  Canadian-owned: {stats["canadianPct"]}%')
    print(f'  Review: {stats["reviewPct"]}%')
    print(f'  Non-exposed foreign: {stats["nonExposedPct"]}%')
    print(f'  CA-resident + CLOUD Act: {stats["caResExposedPct"]}%')
    print()

    old = load_old_values()
    print('\nUpdating JSON-LD schema blocks...\n')

    files = find_html_files()
    total_changes = 0
    files_changed = 0

    for f in files:
        c = update_file(f, old, stats)
        if c > 0:
            total_changes += c
            files_changed += 1

    print(f'\nDone. {total_changes} replacements across {files_changed} files.')
    save_reference(stats)
