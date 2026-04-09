#!/usr/bin/env python3
"""
Upper Harbour — Signals Pipeline
Runs every 6 hours via GitHub Actions.
Collects, filters, and auto-publishes Canadian data sovereignty intelligence.

Flow:
  1. Pull RSS feeds from known sources
  2. Run Claude API web searches for broader coverage
  3. Deduplicate and score for relevance
  4. Claude API rewrites summaries and classifies event type
  5. Auto-publish to signals.json (no approval step)
  6. Send daily digest email summarizing what was published

Requirements:
  pip install anthropic feedparser requests

Environment variables:
  ANTHROPIC_API_KEY  — Claude API key
  SMTP_HOST          — Email server (e.g., smtp.gmail.com)
  SMTP_PORT          — Email port (e.g., 587)
  SMTP_USER          — Email address to send from
  SMTP_PASS          — Email password / app password
  APPROVAL_EMAIL     — Your email (josh@upperharbour.ca)
  SIGNALS_JSON_PATH  — Path to signals.json in repo (default: assets/signals.json)
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
SIGNALS_JSON_PATH = os.environ.get("SIGNALS_JSON_PATH", "assets/signals.json")

# RSS feeds to monitor
RSS_FEEDS = [
    # Canadian regulators (skip keyword filtering — always relevant)
    {"url": "https://www.cai.gouv.qc.ca/rss", "name": "CAI Quebec", "type_hint": "enforcement", "always_relevant": True},
    {"url": "https://www.priv.gc.ca/en/opc-news/news-and-announcements/rss/", "name": "OPC Canada", "type_hint": "enforcement", "always_relevant": True},
    {"url": "https://www.priv.gc.ca/en/rss/blog", "name": "OPC Canada Blog", "type_hint": "policy", "always_relevant": True},
    {"url": "https://www.ipc.on.ca/feed/", "name": "IPC Ontario", "type_hint": "policy", "always_relevant": True},
    {"url": "https://www.oipc.bc.ca/feed/", "name": "OIPC BC", "type_hint": "enforcement", "always_relevant": True},
    {"url": "https://www.oipc.ab.ca/feed/", "name": "OIPC Alberta", "type_hint": "enforcement", "always_relevant": True},
    {"url": "https://www.oipc.sk.ca/feed/", "name": "OIPC Saskatchewan", "type_hint": "enforcement", "always_relevant": True},
    {"url": "https://www.ombudsman.mb.ca/info/access-and-privacy-feed.xml", "name": "Manitoba Ombudsman", "type_hint": "enforcement", "always_relevant": True},
    {"url": "https://www.gnb.ca/legis/bill/rss/index-e.asp", "name": "New Brunswick Legislature", "type_hint": "legislation", "always_relevant": False},

    # Government
    {"url": "https://www.canada.ca/en/treasury-board-secretariat.atom", "name": "Treasury Board", "type_hint": "procurement", "always_relevant": False},
    {"url": "https://www.parl.ca/legisinfo/en/bills/rss", "name": "Parliament of Canada", "type_hint": "legislation", "always_relevant": False},
    {"url": "https://www.gazette.gc.ca/rss/part2-en.xml", "name": "Canada Gazette", "type_hint": "legislation", "always_relevant": False},
    {"url": "https://buyandsell.gc.ca/procurement-data/rss", "name": "CanadaBuys", "type_hint": "procurement", "always_relevant": False},
    {"url": "https://www.canada.ca/en/shared-services.atom", "name": "Shared Services Canada", "type_hint": "procurement", "always_relevant": False},
    {"url": "https://ised-isde.canada.ca/site/ised/en/rss.xml", "name": "ISED", "type_hint": "policy", "always_relevant": False},
    {"url": "https://www.cyber.gc.ca/en/alerts-advisories/rss", "name": "Canadian Cyber Centre", "type_hint": "policy", "always_relevant": False},

    # Canadian law firms — privacy practices
    {"url": "https://www.blakes.com/insights/rss", "name": "Blakes", "type_hint": None, "always_relevant": False},
    {"url": "https://stikeman.com/en-ca/kh/canadian-communications-law/feed", "name": "Stikeman Elliott", "type_hint": None, "always_relevant": False},
    {"url": "https://www.mccarthy.ca/en/insights/rss", "name": "McCarthy Tétrault", "type_hint": None, "always_relevant": False},
    {"url": "https://www.osler.com/en/resources/rss", "name": "Osler", "type_hint": None, "always_relevant": False},
    {"url": "https://www.fasken.com/en/feeds/knowledge", "name": "Fasken", "type_hint": None, "always_relevant": False},
    {"url": "https://www.blg.com/en/insights/rss", "name": "BLG", "type_hint": None, "always_relevant": False},
    {"url": "https://www.nortonrosefulbright.com/en-ca/knowledge/rss", "name": "Norton Rose Fulbright", "type_hint": None, "always_relevant": False},
    {"url": "https://www.dentons.com/en/insights/rss", "name": "Dentons", "type_hint": None, "always_relevant": False},
    {"url": "https://www.torys.com/en/insights/rss", "name": "Torys", "type_hint": None, "always_relevant": False},
    {"url": "https://gowlingwlg.com/en/insights/rss", "name": "Gowling WLG", "type_hint": None, "always_relevant": False},

    # Tech / legal news
    {"url": "https://betakit.com/feed/", "name": "BetaKit", "type_hint": None, "always_relevant": False},
    {"url": "https://www.itworldcanada.com/feed", "name": "IT World Canada", "type_hint": None, "always_relevant": False},
    {"url": "https://www.lexology.com/feed", "name": "Lexology", "type_hint": None, "always_relevant": False},
    {"url": "https://thelogic.co/feed/", "name": "The Logic", "type_hint": None, "always_relevant": False},
    {"url": "https://iapp.org/rss/daily-dashboard/", "name": "IAPP", "type_hint": None, "always_relevant": False},
    {"url": "https://channelbuzz.ca/feed/", "name": "ChannelBuzz", "type_hint": None, "always_relevant": False},
    {"url": "https://www.cantechletter.com/feed/", "name": "Cantech Letter", "type_hint": None, "always_relevant": False},
    {"url": "https://www.cira.ca/en/blog/feed", "name": "CIRA", "type_hint": None, "always_relevant": False},

    # Policy media — shapes procurement narratives
    {"url": "https://ipolitics.ca/feed/", "name": "iPolitics", "type_hint": "policy", "always_relevant": False},
    {"url": "https://thehub.ca/feed/", "name": "The Hub", "type_hint": "policy", "always_relevant": False},
    {"url": "https://policyoptions.irpp.org/feed/", "name": "Policy Options", "type_hint": "policy", "always_relevant": False},
    {"url": "https://www.hilltimes.com/feed/", "name": "Hill Times", "type_hint": "policy", "always_relevant": False},
    {"url": "https://ppforum.ca/feed/", "name": "Public Policy Forum", "type_hint": "policy", "always_relevant": False},

    # The Conversation — Canada, politics + tech
    {"url": "https://theconversation.com/ca/articles.atom?tag=data-privacy", "name": "The Conversation CA", "type_hint": "policy", "always_relevant": False},

    # Industry research & reports
    {"url": "https://www.kiteworks.com/blog/feed/", "name": "Kiteworks", "type_hint": "policy", "always_relevant": False},
    {"url": "https://www.securityscorecard.com/blog/feed/", "name": "SecurityScorecard", "type_hint": "vendor", "always_relevant": False},
    {"url": "https://www.thalesgroup.com/en/feeds/blog/dis.rss", "name": "Thales", "type_hint": "vendor", "always_relevant": False},

    # Canadian news — sovereignty/tech coverage
    {"url": "https://www.canadianlawyermag.com/feed", "name": "Canadian Lawyer", "type_hint": None, "always_relevant": False},
    {"url": "https://www.thestar.com/search/?contenttype=articles&q=data+sovereignty&output=rss", "name": "Toronto Star", "type_hint": None, "always_relevant": False},
    {"url": "https://globalnews.ca/feed/", "name": "Global News", "type_hint": None, "always_relevant": False},
    {"url": "https://financialpost.com/feed/", "name": "Financial Post", "type_hint": None, "always_relevant": False},

    # Cloud vendor blogs
    {"url": "https://aws.amazon.com/blogs/publicsector/feed/", "name": "AWS Public Sector", "type_hint": "vendor", "always_relevant": False},
    {"url": "https://azure.microsoft.com/en-us/blog/feed/", "name": "Azure Blog", "type_hint": "vendor", "always_relevant": False},
    {"url": "https://cloud.google.com/blog/rss", "name": "Google Cloud Blog", "type_hint": "vendor", "always_relevant": False},
]

# Web search queries (run via Claude API with web search tool)
SEARCH_QUERIES = [
    # Core sovereignty (highest yield)
    "Canada data sovereignty news this week",
    "Law 25 Quebec enforcement PIPEDA",
    "CLOUD Act Canada data 2026",
    # M&A tracking (critical for DB accuracy)
    "Canadian SaaS company acquired 2026",
    # Enforcement
    "privacy commissioner order Canada 2026",
    # Infrastructure & procurement
    "sovereign cloud Canada data centre announcement",
    "government procurement data sovereignty Canada",
    # Research & reports
    "data sovereignty survey report Canada 2026",
    # Policy
    "digital sovereignty Canada federal policy 2026",
]

# Relevance keywords for filtering
RELEVANCE_KEYWORDS = [
    # Core sovereignty terms
    "data sovereignty", "digital sovereignty", "canadian sovereignty",
    "canadian data sovereignty", "cloud act", "law 25", "loi 25",
    "pipeda", "cppa", "fippa",
    # Data handling
    "data residency", "data localization", "transfer impact assessment",
    "cross-border data", "data transfer", "data protection",
    # Regulators and enforcement
    "privacy commissioner", "enforcement order", "enforcement action",
    "commission d'accès", "cai quebec",
    # Industry
    "saas", "cloud computing", "cloud infrastructure",
    "procurement", "government procurement", "public sector",
    # Corporate activity
    "jurisdictional", "foreign jurisdiction", "acquisition", "acquired",
    "private equity", "merger",
    # Infrastructure
    "data centre canada", "data center canada", "canadian data centre",
    "aws canada", "azure canada", "gcp canada",
    # Privacy and compliance
    "canadian privacy", "privacy law canada", "privacy reform",
    "compliance", "cybersecurity canada",
    # Procurement language shifts (early warning indicators)
    "canadian hosting", "data residency required", "protected b",
    "controlled access", "sovereign cloud", "domestic hosting",
    "data boundary", "sovereign key", "local control",
    # Vendor sovereignty marketing
    "canadian data centre", "canada region", "canadian customers",
    # Research and reports
    "sovereignty report", "sovereignty survey", "compliance survey",
    "data sovereignty report", "privacy survey", "compliance report",
    "kiteworks", "ponemon", "thales data threat",
]

# Event type classification
EVENT_TYPES = ["enforcement", "acquisition", "legislation", "vendor", "procurement", "policy"]


# ── RSS Collection ───────────────────────────────────────────

def collect_rss() -> list[dict]:
    """Pull items from all RSS feeds, filter by recency and relevance."""
    items = []
    cutoff = datetime.now() - timedelta(hours=168)  # Last 7 days

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

                # Basic relevance check (skip for regulator feeds — always relevant)
                if not feed_config.get("always_relevant", False):
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
            time.sleep(180)  # Wait 180s between searches to avoid rate limits
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = client.messages.create(
                    model="claude-haiku-4-5-20251001",
                    max_tokens=2000,
                    tools=[{"type": "web_search_20250305", "name": "web_search"}],
                    messages=[{
                        "role": "user",
                        "content": f"""Search for: {query}

Today's date is {datetime.now().strftime('%Y-%m-%d')}. Return ONLY items published in the last 7 days (on or after {(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')}). Ignore anything older — even if it appears in search results.

Items must be directly relevant to Canadian data sovereignty, privacy law enforcement, SaaS vendor jurisdictional changes, or government procurement policy.

For each relevant result, return a JSON array with objects containing:
- "title": the headline
- "summary": 1-2 sentence summary of the development
- "source": publication name
- "source_url": URL
- "date": date in YYYY-MM-DD format (must be {(datetime.now() - timedelta(days=7)).strftime('%Y-%m-%d')} or later)

If nothing relevant was published in the last 48 hours, return an empty array: []

Return ONLY the JSON array, nothing else."""
                    }]
                )
                break  # Success — exit retry loop
            except anthropic.RateLimitError:
                wait = 60 * (attempt + 1)  # 60s, 120s, 180s
                log.warning(f"Rate limited on '{query}', retrying in {wait}s (attempt {attempt + 1}/{max_retries})")
                time.sleep(wait)
                if attempt == max_retries - 1:
                    log.warning(f"Search failed for '{query}': exhausted retries after rate limiting")
                    response = None
        if response is None:
            continue

        try:
            # Extract text from response
            text = ""
            for block in response.content:
                if hasattr(block, 'text'):
                    text += block.text

            # Parse JSON from response
            text = text.strip().strip('```json').strip('```').strip()
            if text.startswith('['):
                results = json.loads(text)
                cutoff_str = (datetime.now() - timedelta(days=7)).strftime("%Y-%m-%d")
                for r in results:
                    # Hard gate: reject anything with a date older than 72 hours
                    item_date = r.get("date", "")
                    if item_date < cutoff_str:
                        log.info(f"Search: rejected stale result '{r.get('title','')[:50]}' (date: {item_date})")
                        continue
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
                model="claude-haiku-4-5-20251001",
                max_tokens=4000,
                messages=[{
                    "role": "user",
                    "content": f"""You are the intelligence processor for Upper Harbour, a Canadian data sovereignty research organization.

Review these news items and process ONLY the ones that are directly relevant to Canadian data sovereignty. Discard anything that is:
- General tech news without sovereignty implications
- US or EU privacy news that doesn't affect Canada
- Product announcements without jurisdictional relevance
- Duplicate or trivial updates

IMPORTANT: Only process items about real, verifiable events. Do not infer, speculate, or embellish. If an item is ambiguous about whether it relates to Canadian data sovereignty, discard it.

For each relevant item, return a JSON array with objects containing:
- "headline": Rewritten headline — factual, concise, no clickbait. Written as Upper Harbour would write it.
- "summary": 2-3 sentence summary in Upper Harbour's voice — precise, analytical, focused on jurisdictional implications. Do not editorialize. State what happened and what it means for Canadian organizations.
- "type": One of: enforcement, acquisition, legislation, vendor, procurement, policy
- "source": Original source name
- "source_url": Original URL
- "date": YYYY-MM-DD
- "impact": A short actionable sentence describing who is affected and what they should do. Examples: "Quebec public-sector organizations using this vendor should reassess compliance." or "Federal departments may need to update procurement documentation." or "Organizations using this tool should review their TIA." Do NOT just write a province code — write a sentence.
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


# ── Source Verification ──────────────────────────────────────

def verify_signals(signals: list[dict]) -> list[dict]:
    """
    Fetch each signal's source URL and verify:
    1. The URL is reachable and returns content
    2. The page content actually relates to the signal headline
    3. The publish date on the page is recent (not months old)
    
    Rejects signals where the source doesn't match the claim.
    """
    if not ANTHROPIC_API_KEY or not signals:
        return signals

    import requests

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    verified = []

    for signal in signals:
        url = signal.get("source_url", "")
        headline = signal.get("headline", "")

        if not url:
            log.warning(f"Verify: no URL for '{headline[:50]}' — skipping")
            continue

        # Fetch the page
        try:
            resp = requests.get(url, timeout=10, headers={
                "User-Agent": "Mozilla/5.0 (Upper Harbour Signals Pipeline)"
            })
            if resp.status_code != 200:
                log.warning(f"Verify: HTTP {resp.status_code} for '{headline[:50]}' — rejecting")
                continue

            # Get first 3000 chars of page text (enough to verify topic + find date)
            page_text = resp.text[:8000]
            # Strip HTML tags crudely for comparison
            import re
            page_text_clean = re.sub(r'<[^>]+>', ' ', page_text)
            page_text_clean = re.sub(r'\s+', ' ', page_text_clean)[:3000]

        except Exception as e:
            log.warning(f"Verify: fetch failed for '{headline[:50]}': {e} — rejecting")
            continue

        # Ask Claude to verify: does this page content match the signal?
        try:
            time.sleep(2)  # Light rate limiting
            verify_response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=200,
                messages=[{
                    "role": "user",
                    "content": f"""You are a fact-checker. A signals pipeline generated this signal:

Headline: {headline}
Date claimed: {signal.get('date', 'unknown')}
Source URL: {url}

Here is the actual text from that URL (first 3000 chars):
---
{page_text_clean}
---

Answer these questions:
1. Does the page content actually discuss the topic described in the headline? (yes/no)
2. What is the actual publish date on the page? (YYYY-MM-DD or "unknown")
3. Is this from the last 7 days? (yes/no/unknown)

Return ONLY a JSON object: {{"topic_match": true/false, "actual_date": "YYYY-MM-DD", "recent": true/false}}
If you can't determine the date, use "unknown" and set recent to false."""
                }]
            )

            vtext = ""
            for block in verify_response.content:
                if hasattr(block, 'text'):
                    vtext += block.text

            vtext = vtext.strip().strip('```json').strip('```').strip()
            verdict = json.loads(vtext)

            if not verdict.get("topic_match", False):
                log.info(f"Verify REJECTED (topic mismatch): '{headline[:60]}'")
                continue

            # Only reject if we have a confirmed date that's older than 14 days
            if verdict.get("actual_date", "unknown") != "unknown":
                actual = verdict["actual_date"]
                cutoff_date = (datetime.now() - timedelta(days=14)).strftime("%Y-%m-%d")
                if actual < cutoff_date:
                    log.info(f"Verify REJECTED (stale — actual date {actual}): '{headline[:60]}'")
                    continue

            # If actual_date is known and different from claimed, correct it
            if verdict.get("actual_date", "unknown") != "unknown":
                signal["date"] = verdict["actual_date"]

            verified.append(signal)
            log.info(f"Verify PASSED: '{headline[:60]}' (date: {signal['date']})")

        except Exception as e:
            log.warning(f"Verify: Claude check failed for '{headline[:50]}': {e} — keeping signal")
            verified.append(signal)  # Fail open — keep if we can't verify

    log.info(f"Verification: {len(signals)} in → {len(verified)} verified")
    return verified


# ── Semantic Dedup ───────────────────────────────────────────

def semantic_dedup(new_signals: list[dict], existing_signals: list[dict]) -> list[dict]:
    """
    Use Claude to detect when a new signal covers the same event as an
    existing signal (different source, same story). Returns only truly new signals.
    Also deduplicates within the new batch itself (same story from multiple sources).
    """
    if not ANTHROPIC_API_KEY or not new_signals:
        return new_signals

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # ── Phase 1: Intra-batch dedup (new signals against each other) ──
    if len(new_signals) > 1:
        try:
            batch_list = [{"idx": i, "headline": s.get("headline", ""), "type": s.get("type", ""), "date": s.get("date", ""), "source": s.get("source", "")}
                          for i, s in enumerate(new_signals)]

            response = client.messages.create(
                model="claude-haiku-4-5-20251001",
                max_tokens=1000,
                messages=[{
                    "role": "user",
                    "content": f"""You are a deduplication filter. Look at these signals and identify groups that cover the SAME underlying event, report, or announcement — even if they have different sources, angles, types, or wording.

Signals:
{json.dumps(batch_list, indent=2)}

For each group of duplicates, keep the LOWEST idx (first one) and mark the rest as duplicates.

Return a JSON array of the idx values that should be REMOVED as duplicates. If none are duplicates, return an empty array: []

Return ONLY the JSON array, nothing else."""
                }]
            )

            text = ""
            for block in response.content:
                if hasattr(block, 'text'):
                    text += block.text

            text = text.strip().strip('```json').strip('```').strip()
            if text.startswith('['):
                intra_dupes = set(json.loads(text))
                if intra_dupes:
                    new_signals = [s for i, s in enumerate(new_signals) if i not in intra_dupes]
                    log.info(f"Intra-batch dedup removed {len(intra_dupes)} duplicate(s)")

        except Exception as e:
            log.warning(f"Intra-batch dedup failed (keeping all): {e}")

    # ── Phase 2: Compare against existing published signals ──
    # Build compact representations — include URLs and summaries for better matching
    new_list = [{"idx": i, "headline": s.get("headline", ""), "date": s.get("date", ""), "source": s.get("source", ""), "summary": s.get("summary", "")[:150]}
                for i, s in enumerate(new_signals)]
    existing_list = [{"headline": s.get("headline", ""), "date": s.get("date", ""), "source": s.get("source", ""), "summary": s.get("summary", "")[:150]}
                     for s in existing_signals[:50]]

    if not existing_list:
        return new_signals

    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=1000,
            messages=[{
                "role": "user",
                "content": f"""You are a deduplication filter. Compare these NEW signals against EXISTING published signals.

A signal is a DUPLICATE if it covers the same underlying event, announcement, report, study, or development as an existing signal — even if:
- The source is different (e.g. vendor blog vs news outlet covering the same report)
- The wording, angle, or type classification is different
- One focuses on a specific finding while the other covers the broader report
- They reference the same company, study, or dataset

Be AGGRESSIVE about catching duplicates. If two signals are about the same report, product launch, policy announcement, or study — even from different sources — mark the new one as duplicate.

NEW signals (candidates for publishing):
{json.dumps(new_list, indent=2)}

EXISTING signals (already published):
{json.dumps(existing_list, indent=2)}

Return a JSON array of the idx values of NEW signals that are DUPLICATES of existing signals. If none are duplicates, return an empty array: []

Return ONLY the JSON array of duplicate idx numbers, nothing else."""
            }]
        )

        text = ""
        for block in response.content:
            if hasattr(block, 'text'):
                text += block.text

        text = text.strip().strip('```json').strip('```').strip()
        if text.startswith('['):
            duplicate_idxs = set(json.loads(text))
            kept = [s for i, s in enumerate(new_signals) if i not in duplicate_idxs]
            removed = len(new_signals) - len(kept)
            if removed:
                log.info(f"Semantic dedup removed {removed} duplicate(s)")
            return kept

    except Exception as e:
        log.warning(f"Semantic dedup failed (keeping all signals): {e}")

    return new_signals


# ── Digest Email ─────────────────────────────────────────────

def send_digest_email(signals: list[dict]):
    """Send a daily digest email summarizing what was auto-published."""
    if not SMTP_USER or not SMTP_PASS:
        log.warning("No SMTP credentials — skipping digest email")
        return

    if not signals:
        return

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
        .impact {{ font-size: 12px; color: #C9A84C; font-style: italic; margin-top: 8px; }}
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Signals — Published</h1>
        <p class="subtitle">{now} &middot; {len(signals)} signals auto-published &middot; <a href="https://upperharbour.ca/signals" style="color:#3CB8B0;">View live page</a></p>
    """

    for signal in signals:
        badge_cls = f"badge-{signal.get('type', 'policy')}"
        html += f"""
        <div class="signal">
          <span class="badge {badge_cls}">{signal.get('type', 'policy')}</span>
          <span class="meta">{signal.get('date', '')} &middot; {signal.get('source', '')}</span>
          <h3>{signal.get('headline', '')}</h3>
          <p>{signal.get('summary', '')}</p>
          <div class="impact">Impact: {signal.get('impact', 'TBD')}</div>
          <div class="meta"><a href="{signal.get('sourceUrl', signal.get('source_url', '#'))}" style="color:#3CB8B0;">View source</a></div>
        """

        if signal.get("db_update"):
            db = signal["db_update"]
            html += f"""
          <div class="db-alert">
            ⟳ Database update recommended: <strong>{db.get('tool_name', '?')}</strong> — {db.get('change', '?')}: {db.get('old_value', '?')} → {db.get('new_value', '?')}
          </div>
            """

        html += "</div>"

    html += """
      </div>
    </body>
    </html>
    """

    msg = MIMEMultipart('alternative')
    msg['Subject'] = f"Signals: {len(signals)} published — {now}"
    msg['From'] = SMTP_USER
    msg['To'] = APPROVAL_EMAIL
    msg.attach(MIMEText(html, 'html'))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        log.info(f"Digest email sent to {APPROVAL_EMAIL}")
    except Exception as e:
        log.error(f"Email failed: {e}")


# ── File I/O ─────────────────────────────────────────────────

def load_existing_signals() -> dict:
    """Load the current signals.json."""
    if os.path.exists(SIGNALS_JSON_PATH):
        with open(SIGNALS_JSON_PATH) as f:
            return json.load(f)
    return {"meta": {}, "signals": []}


def save_signals(data: dict):
    """Write signals.json."""
    os.makedirs(os.path.dirname(SIGNALS_JSON_PATH) or '.', exist_ok=True)
    with open(SIGNALS_JSON_PATH, 'w') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    log.info(f"Saved {len(data.get('signals', []))} signals to {SIGNALS_JSON_PATH}")


DB_ALERTS_PATH = os.environ.get("DB_ALERTS_PATH", "db-alerts.json")

def load_db_alerts() -> list[dict]:
    """Load existing database update alerts."""
    if os.path.exists(DB_ALERTS_PATH):
        with open(DB_ALERTS_PATH) as f:
            data = json.load(f)
        if isinstance(data, list):
            return data
        return data.get("alerts", [])
    return []

def save_db_alerts(new_alerts: list[dict]):
    """Append new database alerts to db-alerts.json."""
    existing = load_db_alerts()
    # Avoid duplicate alerts for the same tool + change
    existing_keys = {(a["tool_name"], a["change"], a.get("new_value", "")) for a in existing}
    for alert in new_alerts:
        key = (alert["tool_name"], alert["change"], alert.get("new_value", ""))
        if key not in existing_keys:
            existing.append(alert)
    # Keep only pending alerts (max 50)
    existing = [a for a in existing if a.get("status") == "pending_review"][:50]
    with open(DB_ALERTS_PATH, 'w') as f:
        json.dump({"alerts": existing, "updated": datetime.now().isoformat()}, f, indent=2, ensure_ascii=False)
    log.info(f"Saved {len(existing)} db alerts to {DB_ALERTS_PATH}")


# ── Auto-Publish ─────────────────────────────────────────────

def publish_signals(new_signals: list[dict]):
    """Auto-publish signals directly to signals.json and flag db updates."""
    existing = load_existing_signals()

    # Build sets of existing source URLs and headline fingerprints for dedup
    existing_urls = set()
    existing_headlines = set()
    for s in existing.get("signals", []):
        url = s.get("sourceUrl", "").strip().rstrip("/").lower()
        if url:
            existing_urls.add(url)
        headline = s.get("headline", "").lower().strip()
        if headline:
            # Extract key terms for fuzzy matching (strips filler words)
            words = set(w for w in headline.split() if len(w) > 3 and w not in {'this', 'that', 'with', 'from', 'their', 'about', 'into', 'have', 'been', 'will', 'more', 'than', 'also', 'over', 'under', 'after', 'before', 'between', 'through', 'across', 'along', 'other', 'each', 'which', 'would', 'could', 'should', 'there', 'these', 'those', 'where', 'when', 'what', 'just', 'some', 'most', 'very', 'only', 'first', 'international', 'global', 'world', 'worldwide', 'announces', 'announced', 'launches', 'launched', 'joins', 'joined', 'says', 'said', 'new', 'based'})
            key_terms = sorted(words)[:6]  # Top 6 keywords alphabetically
            existing_headlines.add(hashlib.md5(' '.join(key_terms).encode()).hexdigest())

    published = []
    db_alerts = []
    for signal in new_signals:
        # Check if this signal's source URL already exists
        src_url = signal.get("source_url", "").strip().rstrip("/").lower()
        if src_url and src_url in existing_urls:
            log.info(f"Skipping duplicate (URL match): {signal.get('headline', '?')[:60]}")
            continue

        # Check headline similarity against existing (keyword-based)
        headline = signal.get("headline", "").lower().strip()
        words = set(w for w in headline.split() if len(w) > 3 and w not in {'this', 'that', 'with', 'from', 'their', 'about', 'into', 'have', 'been', 'will', 'more', 'than', 'also', 'over', 'under', 'after', 'before', 'between', 'through', 'across', 'along', 'other', 'each', 'which', 'would', 'could', 'should', 'there', 'these', 'those', 'where', 'when', 'what', 'just', 'some', 'most', 'very', 'only', 'first', 'international', 'global', 'world', 'worldwide', 'announces', 'announced', 'launches', 'launched', 'joins', 'joined', 'says', 'said', 'new', 'based'})
        key_terms = sorted(words)[:6]
        headline_hash = hashlib.md5(' '.join(key_terms).encode()).hexdigest()
        if headline_hash in existing_headlines:
            log.info(f"Skipping duplicate (headline match): {signal.get('headline', '?')[:60]}")
            continue

        item = {
            "headline": signal.get("headline", ""),
            "summary": signal.get("summary", ""),
            "type": signal.get("type", "policy"),
            "source": signal.get("source", ""),
            "sourceUrl": signal.get("source_url", ""),
            "date": signal.get("date", ""),
            "impact": signal.get("impact", ""),
            "dbUpdate": signal.get("db_update") is not None,
        }
        published.append(item)
        existing_urls.add(src_url)
        existing_headlines.add(headline_hash)

        # Collect database update alerts
        if signal.get("db_update"):
            db = signal["db_update"]
            db_alerts.append({
                "tool_name": db.get("tool_name", ""),
                "change": db.get("change", ""),
                "old_value": db.get("old_value", ""),
                "new_value": db.get("new_value", ""),
                "reason": db.get("reason", ""),
                "signal_headline": signal.get("headline", ""),
                "signal_date": signal.get("date", ""),
                "source_url": signal.get("source_url", ""),
                "flagged_at": datetime.now().isoformat(),
                "status": "pending_review",
            })

        # Collect new-tool suggestions as a distinct alert type. These come
        # from the tripwire's assess_sovereignty_impact pass, which asks
        # Claude to identify tools mentioned in a filing that Upper Harbour
        # isn't tracking yet. Each suggestion becomes its own db-alerts entry
        # with change="suggest_new_tool" so the admin UI can render it and
        # Josh can accept or dismiss it.
        for sugg in (signal.get("suggested_new_tools") or []):
            if not isinstance(sugg, dict):
                continue
            tool_name = (sugg.get("tool_name") or "").strip()
            if not tool_name:
                continue
            # Pack the suggestion details into new_value as a JSON string so
            # the applier (future session) can reconstruct a full tool entry
            # on approval without losing any of the fields. old_value is null
            # because there's nothing there yet.
            sugg_payload = {
                "parent": sugg.get("parent", ""),
                "jurisdiction": sugg.get("jurisdiction", ""),
                "category": sugg.get("category", "unknown"),
                "rationale": sugg.get("rationale", ""),
            }
            db_alerts.append({
                "tool_name": tool_name,
                "change": "suggest_new_tool",
                "old_value": None,
                "new_value": json.dumps(sugg_payload, ensure_ascii=False),
                "reason": sugg.get("rationale", "") or f"Mentioned in filing linked to {signal.get('headline', 'a tracked parent')}",
                "signal_headline": signal.get("headline", ""),
                "signal_date": signal.get("date", ""),
                "source_url": signal.get("source_url", ""),
                "flagged_at": datetime.now().isoformat(),
                "status": "pending_review",
            })

    # Add to existing signals (newest first)
    existing["signals"] = published + existing.get("signals", [])

    # Keep max 200 signals (oldest drop off naturally as new ones are added)
    existing["signals"] = existing["signals"][:200]

    # Update meta
    existing["meta"] = {
        "lastUpdated": datetime.now().strftime("%b %d, %Y — %H:%M ET"),
        "sourceCount": f"{len(RSS_FEEDS) + len(SEARCH_QUERIES)}+",
    }

    save_signals(existing)

    # Write database alerts file (append to existing)
    if db_alerts:
        save_db_alerts(db_alerts)

    log.info(f"Auto-published {len(published)} signals, {len(db_alerts)} db alerts flagged")
    return published


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
    time.sleep(90)  # Wait for rate limit window to reset after searches
    processed = process_with_claude(unique_items)
    log.info(f"Processed: {len(processed)} relevant signals")

    if not processed:
        log.info("No items passed relevance filter. Done.")
        return

    # 4b. Verify signals against their actual source URLs
    log.info("Step 3b: Verifying signals against source URLs...")
    processed = verify_signals(processed)

    if not processed:
        log.info("No items passed source verification. Done.")
        return

    # 5. Check against existing signals (avoid re-publishing)
    existing = load_existing_signals()
    existing_headlines = {s.get("headline", "").lower() for s in existing.get("signals", [])}
    new_signals = [s for s in processed if s.get("headline", "").lower() not in existing_headlines]
    log.info(f"After dedup against existing: {len(new_signals)} new signals")

    if not new_signals:
        log.info("All items already published. Done.")
        return

    # 5b. Semantic dedup — catch same story from different sources
    log.info("Step 3b: Semantic dedup...")
    new_signals = semantic_dedup(new_signals, existing.get("signals", [])[:30])
    log.info(f"After semantic dedup: {len(new_signals)} signals")

    if not new_signals:
        log.info("All items were duplicates of existing signals. Done.")
        return

    # 6. Auto-publish
    log.info("Step 4: Auto-publishing signals...")
    published = publish_signals(new_signals)

    # 7. Send digest email
    log.info("Step 5: Sending digest email...")
    send_digest_email(published)

    log.info("=" * 60)
    log.info(f"PIPELINE COMPLETE — {len(published)} signals published")
    log.info("=" * 60)


# ── CLI ──────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys

    if len(sys.argv) > 1:
        command = sys.argv[1]

        if command == "collect":
            run_pipeline()

        elif command == "status":
            existing = load_existing_signals()
            print(f"Published signals: {len(existing.get('signals', []))}")

        else:
            print(f"Unknown command: {command}")
            print("Usage: python signals_pipeline.py [collect|status]")
    else:
        run_pipeline()
