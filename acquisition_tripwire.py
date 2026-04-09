#!/usr/bin/env python3
"""
Upper Harbour — Acquisition Tripwire Module
Monitors SEC EDGAR (US parents) and SEDAR+ (Canadian parents) for
corporate filings that signal ownership changes affecting tools in saas-db.js.

Designed to run daily via GitHub Actions alongside signals_pipeline.py.
Uses the FREE SEC EDGAR API (data.sec.gov) — no API key required.

Flow:
  1. Extract all parent companies from saas-db.js
  2. For US parents: check SEC EDGAR for recent 8-K, SC 13D, S-4 filings
  3. For Canadian parents: check SEDAR+ for material change reports
  4. Filter filings for acquisition/merger/ownership-change language
  5. Use Claude to assess sovereignty impact
  6. Output: signals for auto-publish + db_update alerts

Usage:
  python acquisition_tripwire.py              # Run full scan
  python acquisition_tripwire.py --us-only    # SEC EDGAR only
  python acquisition_tripwire.py --ca-only    # SEDAR+ only
  python acquisition_tripwire.py --test AAPL  # Test with single ticker

Requirements:
  pip install anthropic requests

Environment variables:
  ANTHROPIC_API_KEY  — Claude API key (required for impact assessment)
"""

import os
import re
import json
import time
import logging
import hashlib
from datetime import datetime, timedelta
from typing import Optional

import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
SAAS_DB_PATH = os.environ.get("SAAS_DB_PATH", "saas-db.js")
TRIPWIRE_CACHE_PATH = os.environ.get("TRIPWIRE_CACHE_PATH", "tripwire-cache.json")

# SEC EDGAR free API — no key required, 10 req/sec max
EDGAR_SUBMISSIONS_URL = "https://data.sec.gov/submissions/CIK{cik}.json"
EDGAR_FULLTEXT_URL = "https://efts.sec.gov/LATEST/search-index"

# User-Agent required by SEC (they block requests without it)
EDGAR_HEADERS = {
    "User-Agent": "Upper Harbour josh@upperharbour.ca",
    "Accept-Encoding": "gzip, deflate",
}

# Filing types that signal ownership changes
ACQUISITION_FORM_TYPES = {
    "8-K",       # Current report — material events including acquisitions
    "8-K/A",     # Amended 8-K
    "SC 13D",    # Beneficial ownership >5%
    "SC 13D/A",  # Amended SC 13D
    "SC 13G",    # Passive beneficial ownership >5%
    "SC 13G/A",  # Amended SC 13G
    "SC TO-T",   # Tender offer (third party)
    "S-4",       # Registration for securities in M&A
    "DEFM14A",   # Definitive merger proxy statement
    "425",       # Prospectus filed under Securities Act — often M&A related
}

# 8-K item codes that specifically relate to acquisitions
ACQUISITION_8K_ITEMS = [
    "1.01",  # Entry into a Material Definitive Agreement
    "2.01",  # Completion of Acquisition or Disposition of Assets
    "5.01",  # Changes in Control of Registrant
    "5.02",  # Departure/Election of Directors or Officers (often follows acquisition)
]

# Keywords in filing text that suggest acquisition/ownership change
ACQUISITION_KEYWORDS = [
    "acquisition", "acquired", "acquire",
    "merger", "merge", "merged",
    "purchase agreement", "asset purchase",
    "change of control", "change in control",
    "tender offer",
    "definitive agreement",
    "stock purchase agreement",
    "membership interest purchase",
    "business combination",
    "wholly-owned subsidiary",
]


# ── Extract Parent Companies from saas-db.js ─────────────────

def extract_parents(db_path: str = SAAS_DB_PATH) -> dict:
    """
    Parse saas-db.js and extract all unique parent companies
    with their jurisdiction and associated tools.
    
    Returns: {
        "Salesforce Inc.": {
            "jurisdiction": "United States",
            "tools": ["Slack", "Salesforce", "Tableau", ...],
            "ticker": "CRM",  # if extractable
        },
        ...
    }
    """
    with open(db_path, 'r') as f:
        src = f.read()

    parents = {}
    
    # Parse each tool entry
    # Pattern: { name:"...", parent:"...", hq:"...", jurisdiction:"...", ... }
    entries = re.findall(
        r'\{\s*name:"([^"]+)"[^}]*parent:"([^"]+)"[^}]*jurisdiction:"([^"]+)"',
        src
    )
    
    for tool_name, parent_name, jurisdiction in entries:
        if parent_name not in parents:
            parents[parent_name] = {
                "jurisdiction": jurisdiction,
                "tools": [],
            }
        parents[parent_name]["tools"].append(tool_name)
    
    log.info(f"Extracted {len(parents)} unique parent companies from {db_path}")
    return parents


def extract_all_tool_names(db_path: str = SAAS_DB_PATH) -> set:
    """
    Return the flat set of all tool names in saas-db.js.

    Used by assess_sovereignty_impact to give Claude the "already tracked"
    list so it can reliably identify NEW tools mentioned in filings that
    Upper Harbour should probably be tracking.
    """
    with open(db_path, 'r') as f:
        src = f.read()
    names = re.findall(r'\{\s*name:"([^"]+)"', src)
    result = set(n.strip() for n in names if n.strip())
    log.info(f"Indexed {len(result)} tool names for new-tool suggestions")
    return result


# ── CIK Lookup (SEC EDGAR) ───────────────────────────────────

# Cache CIK lookups to avoid repeated API calls
_cik_cache = {}

def lookup_cik(company_name: str) -> Optional[str]:
    """
    Look up a company's CIK number from SEC EDGAR.
    Uses the company search endpoint.
    Returns padded 10-digit CIK string, or None if not found.
    """
    if company_name in _cik_cache:
        return _cik_cache[company_name]
    
    # Clean company name for search
    clean = company_name.replace(",", "").replace(".", "").replace("Inc", "").replace("Corp", "").replace("LLC", "").strip()
    
    try:
        url = f"https://efts.sec.gov/LATEST/search-index?q=%22{requests.utils.quote(clean)}%22&dateRange=custom&startdt=2020-01-01&forms=10-K&from=0&size=1"
        resp = requests.get(url, headers=EDGAR_HEADERS, timeout=10)
        if resp.status_code == 200:
            data = resp.json()
            hits = data.get("hits", {}).get("hits", [])
            if hits:
                cik = hits[0].get("_source", {}).get("file_num", "")
                # Try entity_id instead
                entity_id = hits[0].get("_source", {}).get("entity_id", "")
                if entity_id:
                    _cik_cache[company_name] = entity_id
                    return entity_id
    except Exception as e:
        log.warning(f"CIK lookup failed for '{company_name}': {e}")
    
    # Fallback: try the company tickers JSON
    try:
        resp = requests.get(
            "https://www.sec.gov/files/company_tickers.json",
            headers=EDGAR_HEADERS, timeout=10
        )
        if resp.status_code == 200:
            tickers = resp.json()
            name_lower = company_name.lower()
            for key, entry in tickers.items():
                if entry.get("title", "").lower() in name_lower or name_lower in entry.get("title", "").lower():
                    cik = str(entry["cik_str"]).zfill(10)
                    _cik_cache[company_name] = cik
                    return cik
    except Exception as e:
        log.warning(f"Ticker lookup failed for '{company_name}': {e}")
    
    _cik_cache[company_name] = None
    return None


# ── SEC EDGAR Filing Check ───────────────────────────────────

def check_edgar_filings(cik: str, company_name: str, lookback_days: int = 7) -> list[dict]:
    """
    Check a company's recent SEC filings for acquisition-related events.
    Uses the free data.sec.gov submissions API.
    
    Returns list of relevant filings with metadata.
    """
    filings = []
    cutoff = datetime.now() - timedelta(days=lookback_days)
    cutoff_str = cutoff.strftime("%Y-%m-%d")
    
    try:
        url = EDGAR_SUBMISSIONS_URL.format(cik=cik.zfill(10))
        resp = requests.get(url, headers=EDGAR_HEADERS, timeout=15)
        
        if resp.status_code != 200:
            log.warning(f"EDGAR API returned {resp.status_code} for {company_name} (CIK: {cik})")
            return []
        
        data = resp.json()
        recent = data.get("filings", {}).get("recent", {})
        
        forms = recent.get("form", [])
        dates = recent.get("filingDate", [])
        accessions = recent.get("accessionNumber", [])
        primary_docs = recent.get("primaryDocument", [])
        descriptions = recent.get("primaryDocDescription", [])
        items_list = recent.get("items", [])  # 8-K item codes
        
        for i in range(len(forms)):
            form_type = forms[i] if i < len(forms) else ""
            filing_date = dates[i] if i < len(dates) else ""
            accession = accessions[i] if i < len(accessions) else ""
            primary_doc = primary_docs[i] if i < len(primary_docs) else ""
            description = descriptions[i] if i < len(descriptions) else ""
            items = items_list[i] if i < len(items_list) else ""
            
            # Skip old filings
            if filing_date < cutoff_str:
                break  # Filings are in reverse chronological order
            
            # Check if this is an acquisition-relevant form type
            if form_type not in ACQUISITION_FORM_TYPES:
                continue
            
            # For 8-K filings, check if the item codes are acquisition-related
            is_relevant = False
            if form_type.startswith("8-K"):
                if items:
                    for item_code in ACQUISITION_8K_ITEMS:
                        if item_code in items:
                            is_relevant = True
                            break
                # If no items field, we'll check the filing text later
                if not items:
                    is_relevant = True
            else:
                # SC 13D, S-4, etc. are always relevant
                is_relevant = True
            
            if is_relevant:
                # Build filing URL
                accession_clean = accession.replace("-", "")
                filing_url = f"https://www.sec.gov/Archives/edgar/data/{cik.lstrip('0')}/{accession_clean}/{primary_doc}"
                
                filings.append({
                    "company": company_name,
                    "cik": cik,
                    "form_type": form_type,
                    "filing_date": filing_date,
                    "accession": accession,
                    "items": items,
                    "description": description,
                    "filing_url": filing_url,
                    "source": "SEC EDGAR",
                })
                
                log.info(f"EDGAR: Found {form_type} for {company_name} filed {filing_date} (items: {items})")
        
    except Exception as e:
        log.warning(f"EDGAR check failed for {company_name}: {e}")
    
    return filings


# ── SEDAR+ Check (Canadian Parents) ──────────────────────────

def check_sedar_filings(company_name: str, lookback_days: int = 7) -> list[dict]:
    """
    Check SEDAR+ for recent material change reports from Canadian companies.
    
    Note: SEDAR+ doesn't have a clean public API, so we use the EDGAR
    full-text search as a proxy (many Canadian companies dual-list on US exchanges)
    and supplement with web search via Claude.
    """
    filings = []
    
    # Many large Canadian companies are dual-listed (TSX + NYSE/NASDAQ)
    # Check EDGAR first for dual-listed companies
    cik = lookup_cik(company_name)
    if cik:
        filings = check_edgar_filings(cik, company_name, lookback_days)
        if filings:
            return filings
    
    # For non-dual-listed Canadian companies, we rely on the signals pipeline's
    # web search to catch news coverage of material changes.
    # This is a known gap — SEDAR+ scraping could be added later with Playwright.
    
    return filings


# ── Filing Text Analysis ─────────────────────────────────────

def fetch_filing_text(filing_url: str, max_chars: int = 5000) -> Optional[str]:
    """Fetch the first N chars of a filing to check for acquisition keywords."""
    try:
        resp = requests.get(filing_url, headers=EDGAR_HEADERS, timeout=15)
        if resp.status_code == 200:
            # Strip HTML tags
            text = re.sub(r'<[^>]+>', ' ', resp.text)
            text = re.sub(r'\s+', ' ', text)
            return text[:max_chars]
    except Exception as e:
        log.warning(f"Failed to fetch filing text: {e}")
    return None


def has_acquisition_language(text: str) -> bool:
    """Check if filing text contains acquisition-related keywords."""
    text_lower = text.lower()
    return any(kw in text_lower for kw in ACQUISITION_KEYWORDS)


# ── Claude Impact Assessment ─────────────────────────────────

def assess_sovereignty_impact(filing: dict, tools: list[str], filing_text: str,
                              known_tool_names: set = None) -> Optional[dict]:
    """
    Use Claude to assess whether a filing has sovereignty implications
    for Canadian organizations using the affected tools.

    Also asks Claude to identify any OTHER tools mentioned in the filing
    that Upper Harbour should probably be tracking but isn't yet. Those
    come back as a suggested_new_tools array and downstream become
    db-alerts entries with change="suggest_new_tool".

    Returns a signal dict ready for publish, or None if not relevant.
    """
    if not ANTHROPIC_API_KEY:
        log.warning("No ANTHROPIC_API_KEY — skipping impact assessment")
        return None

    import anthropic
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

    # Lazy-load the known-tool index if the caller didn't pass one
    if known_tool_names is None:
        try:
            known_tool_names = extract_all_tool_names()
        except Exception as e:
            log.warning(f"Could not load known tool names: {e}")
            known_tool_names = set()

    # Give Claude a compact but useful slice of the known-tool list so it
    # can recognize what's already tracked. The full list is ~755 tools
    # (~10-12KB of text) which fits easily in the prompt.
    known_sample = sorted(known_tool_names)

    try:
        response = client.messages.create(
            model="claude-haiku-4-5-20251001",
            max_tokens=2500,
            messages=[{
                "role": "user",
                "content": f"""You are an analyst for Upper Harbour, a Canadian data sovereignty research organization.

A SEC filing has been detected for a company whose tools are used by Canadian organizations.

Filing details:
- Company: {filing['company']}
- Form type: {filing['form_type']}
- Filed: {filing['filing_date']}
- 8-K items: {filing.get('items', 'N/A')}
- Tools already tracked for this parent: {', '.join(tools)}

Filing text excerpt (first 5000 chars):
---
{filing_text[:5000]}
---

Upper Harbour already tracks the following tool names in its Sovereignty Index (this is the complete list — anything NOT on this list is a candidate for a new tool suggestion):
{', '.join(known_sample)}

Analyze this filing and determine:

PART A — Primary event:
1. Does this filing indicate an acquisition, merger, ownership change, or change of control?
2. If yes, what specifically changed? (new parent company, new PE owner, etc.)
3. Does this change affect the CLOUD Act exposure or jurisdictional status of the tools listed above?
4. What should Canadian organizations using these tools know?

PART B — New tool suggestions:
5. Does the filing mention any OTHER software products, SaaS tools, cloud services, or technology offerings that are NOT in the "already tracked" list above and that Canadian organizations could plausibly be using? This could include:
   - A target company being acquired whose products are a SaaS/cloud/enterprise tool
   - A newly-announced product or service line with sovereignty relevance
   - A subsidiary or brand mentioned that has its own distinct tool offering
   - A partnership or integration that creates a new tool-like offering
   Do NOT suggest: generic terms (like "cloud services"), consulting services, physical hardware, financial products, media products, or things clearly out of scope for Canadian data sovereignty research.
6. For each suggested new tool, provide a short factual rationale grounded in the filing text.

Return a JSON object in this exact shape:

If the filing IS sovereignty-relevant OR contains new-tool suggestions:
{{
  "is_relevant": true,
  "headline": "Short factual headline for Signals page (required even if the only finding is new tools — in that case frame it around the filing itself)",
  "summary": "2-3 sentence summary of what happened and what it means for Canadian organizations",
  "type": "acquisition",
  "impact": "Who is affected and what they should do (one sentence)",
  "db_update": {{
    "tool_name": "Name of the primary tool affected",
    "change": "What changed (e.g., parent_company, jurisdiction, risk_status)",
    "old_value": "Previous value",
    "new_value": "New value",
    "reason": "Brief explanation"
  }} OR null if there's no primary-tool update (only new-tool suggestions),
  "suggested_new_tools": [
    {{
      "tool_name": "Exact name of the tool (as it would appear in the Sovereignty Index)",
      "parent": "Parent company name after this filing's effect",
      "jurisdiction": "Best-guess jurisdiction of the parent (Canada, United States, United Kingdom, Germany, etc.)",
      "category": "Best-guess category (communication, crm, storage, ai, analytics, devtools, etc.) or 'unknown'",
      "rationale": "1-2 sentence explanation of why Upper Harbour should track this tool, grounded in the filing"
    }}
  ]
}}

If this is NOT sovereignty-relevant AND there are no new-tool candidates, return:
{{"is_relevant": false}}

IMPORTANT:
- Only return suggested_new_tools for products that plausibly fit the Sovereignty Index — real SaaS/cloud/enterprise software Canadian organizations would actually use. Be conservative; if in doubt, don't suggest.
- Each suggested tool's name must NOT already appear in the "already tracked" list above. Check carefully.
- If there are no new-tool candidates, omit the suggested_new_tools field or return an empty array.
- Return ONLY the JSON object, nothing else."""
            }]
        )

        text = ""
        for block in response.content:
            if hasattr(block, 'text'):
                text += block.text

        text = text.strip().strip('```json').strip('```').strip()
        result = json.loads(text)

        if result.get("is_relevant"):
            # Filter suggested_new_tools to drop anything that's actually a dup
            # against our known list (Claude occasionally hallucinates that
            # something is new when it isn't — belt-and-suspenders check).
            raw_suggestions = result.get("suggested_new_tools") or []
            cleaned_suggestions = []
            known_lower = {n.lower() for n in known_tool_names}
            for s in raw_suggestions:
                if not isinstance(s, dict):
                    continue
                name = (s.get("tool_name") or "").strip()
                if not name:
                    continue
                if name.lower() in known_lower:
                    log.info(f"Dropping suggested new tool '{name}' — already tracked")
                    continue
                cleaned_suggestions.append({
                    "tool_name": name,
                    "parent": (s.get("parent") or "").strip(),
                    "jurisdiction": (s.get("jurisdiction") or "").strip(),
                    "category": (s.get("category") or "unknown").strip(),
                    "rationale": (s.get("rationale") or "").strip(),
                })

            return {
                "headline": result["headline"],
                "summary": result["summary"],
                "type": result.get("type", "acquisition"),
                "source": f"SEC EDGAR ({filing['form_type']})",
                "source_url": filing["filing_url"],
                "date": filing["filing_date"],
                "impact": result.get("impact", ""),
                "db_update": result.get("db_update"),
                "suggested_new_tools": cleaned_suggestions,
            }
        else:
            log.info(f"Filing for {filing['company']} assessed as not sovereignty-relevant")
            return None

    except Exception as e:
        log.warning(f"Claude assessment failed for {filing['company']}: {e}")
        return None


# ── Cache Management ─────────────────────────────────────────

def load_cache() -> dict:
    """Load the tripwire cache (tracks which filings we've already processed)."""
    if os.path.exists(TRIPWIRE_CACHE_PATH):
        with open(TRIPWIRE_CACHE_PATH) as f:
            return json.load(f)
    return {"processed_filings": [], "last_run": None, "cik_map": {}}


def save_cache(cache: dict):
    """Save the tripwire cache."""
    cache["last_run"] = datetime.now().isoformat()
    # Keep only last 500 processed filing IDs
    cache["processed_filings"] = cache["processed_filings"][-500:]
    with open(TRIPWIRE_CACHE_PATH, 'w') as f:
        json.dump(cache, f, indent=2)


# ── Main Pipeline ────────────────────────────────────────────

def run_tripwire(us_only: bool = False, ca_only: bool = False, 
                 test_ticker: str = None, lookback_days: int = 7) -> list[dict]:
    """
    Main entry point. Scans SEC EDGAR and SEDAR+ for acquisition signals.
    
    Returns list of sovereignty-relevant signals ready for publish.
    """
    log.info("=" * 60)
    log.info("ACQUISITION TRIPWIRE — Starting")
    log.info("=" * 60)
    
    cache = load_cache()
    processed = set(cache.get("processed_filings", []))
    cik_map = cache.get("cik_map", {})

    # Extract parent companies from database
    parents = extract_parents()

    # Build a one-shot index of every tool name in the database so Claude
    # can recognize new tools vs already-tracked ones without us reparsing
    # saas-db.js for every filing.
    try:
        known_tool_names = extract_all_tool_names()
    except Exception as e:
        log.warning(f"Could not build known-tool index: {e}")
        known_tool_names = set()
    
    # Filter by jurisdiction
    if test_ticker:
        # Test mode — look up a single company
        parents = {test_ticker: {"jurisdiction": "United States", "tools": [test_ticker]}}
    
    us_parents = {k: v for k, v in parents.items() if v["jurisdiction"] == "United States"} if not ca_only else {}
    ca_parents = {k: v for k, v in parents.items() if v["jurisdiction"] == "Canada"} if not us_only else {}
    
    log.info(f"Monitoring: {len(us_parents)} US parents (EDGAR), {len(ca_parents)} Canadian parents (SEDAR+)")
    
    all_signals = []
    
    # ── Phase 1: SEC EDGAR (US parents) ──
    if us_parents:
        log.info(f"Phase 1: Checking SEC EDGAR for {len(us_parents)} US parent companies...")
        
        checked = 0
        for company_name, info in us_parents.items():
            # Rate limiting: 10 req/sec max, but we'll be conservative
            if checked > 0 and checked % 8 == 0:
                time.sleep(1.5)
            
            # Look up CIK (use cache first)
            cik = cik_map.get(company_name)
            if not cik:
                cik = lookup_cik(company_name)
                if cik:
                    cik_map[company_name] = cik
                else:
                    checked += 1
                    continue
            
            # Check for recent filings
            filings = check_edgar_filings(cik, company_name, lookback_days)
            
            for filing in filings:
                # Skip already-processed filings
                filing_id = filing["accession"]
                if filing_id in processed:
                    continue
                
                # Fetch filing text and check for acquisition language
                filing_text = fetch_filing_text(filing["filing_url"])
                if filing_text and has_acquisition_language(filing_text):
                    # Assess sovereignty impact with Claude
                    signal = assess_sovereignty_impact(
                        filing, info["tools"], filing_text,
                        known_tool_names=known_tool_names,
                    )
                    if signal:
                        all_signals.append(signal)
                        log.info(f"ALERT: {signal['headline']}")
                        if signal.get("suggested_new_tools"):
                            log.info(
                                f"  + {len(signal['suggested_new_tools'])} new-tool suggestion(s)"
                            )
                
                processed.add(filing_id)
            
            checked += 1
            
            # Progress logging
            if checked % 50 == 0:
                log.info(f"  ... checked {checked}/{len(us_parents)} US parents")
    
    # ── Phase 2: SEDAR+ (Canadian parents) ──
    if ca_parents:
        log.info(f"Phase 2: Checking SEDAR+ for {len(ca_parents)} Canadian parent companies...")
        
        for company_name, info in ca_parents.items():
            filings = check_sedar_filings(company_name, lookback_days)
            
            for filing in filings:
                filing_id = filing["accession"]
                if filing_id in processed:
                    continue
                
                filing_text = fetch_filing_text(filing["filing_url"])
                if filing_text and has_acquisition_language(filing_text):
                    signal = assess_sovereignty_impact(
                        filing, info["tools"], filing_text,
                        known_tool_names=known_tool_names,
                    )
                    if signal:
                        all_signals.append(signal)
                
                processed.add(filing_id)
    
    # ── Save cache ──
    cache["processed_filings"] = list(processed)
    cache["cik_map"] = cik_map
    save_cache(cache)
    
    log.info("=" * 60)
    log.info(f"TRIPWIRE COMPLETE — {len(all_signals)} acquisition signals detected")
    log.info("=" * 60)
    
    return all_signals


# ── Integration with signals_pipeline.py ─────────────────────

def integrate_with_pipeline(signals: list[dict]):
    """
    Feed tripwire signals into the existing signals pipeline for
    auto-publishing and digest email.
    """
    if not signals:
        return
    
    # Import from signals pipeline
    try:
        from signals_pipeline import publish_signals, send_digest_email
        
        published = publish_signals(signals)
        if published:
            send_digest_email(published)
            log.info(f"Integrated {len(published)} acquisition signals into pipeline")
    except ImportError:
        # If signals_pipeline isn't available, write signals to a JSON file
        output_path = "tripwire-signals.json"
        with open(output_path, 'w') as f:
            json.dump(signals, f, indent=2, ensure_ascii=False)
        log.info(f"Wrote {len(signals)} signals to {output_path} (pipeline not available)")


# ── CLI ──────────────────────────────────────────────────────

if __name__ == "__main__":
    import sys
    
    us_only = "--us-only" in sys.argv
    ca_only = "--ca-only" in sys.argv
    test_ticker = None
    
    for i, arg in enumerate(sys.argv):
        if arg == "--test" and i + 1 < len(sys.argv):
            test_ticker = sys.argv[i + 1]
    
    lookback = 7  # Default 7 days
    for i, arg in enumerate(sys.argv):
        if arg == "--lookback" and i + 1 < len(sys.argv):
            lookback = int(sys.argv[i + 1])
    
    signals = run_tripwire(
        us_only=us_only,
        ca_only=ca_only,
        test_ticker=test_ticker,
        lookback_days=lookback,
    )
    
    if signals:
        print(f"\n{'='*60}")
        print(f"ACQUISITION ALERTS ({len(signals)})")
        print(f"{'='*60}\n")
        for s in signals:
            print(f"  [{s['type'].upper()}] {s['headline']}")
            print(f"  {s['summary']}")
            print(f"  Source: {s['source']} — {s['source_url']}")
            if s.get('db_update'):
                db = s['db_update']
                print(f"  DB Update: {db['tool_name']} — {db['change']}: {db.get('old_value','?')} → {db['new_value']}")
            if s.get('suggested_new_tools'):
                for sugg in s['suggested_new_tools']:
                    print(f"  New tool suggestion: {sugg['tool_name']} ({sugg.get('parent','?')}, {sugg.get('jurisdiction','?')})")
                    if sugg.get('rationale'):
                        print(f"    → {sugg['rationale']}")
            print()
        
        # Auto-integrate with pipeline if running in CI
        if os.environ.get("CI") or os.environ.get("GITHUB_ACTIONS"):
            integrate_with_pipeline(signals)
    else:
        print("No acquisition signals detected.")
