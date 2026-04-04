#!/usr/bin/env python3
"""
Upper Harbour — Lead Brief Generator
Researches prospects and generates pre-call sovereignty briefs.

Two modes:
  1. Manual: python lead_brief.py "Jane Smith" "jane@company.com"
  2. Webhook: receives Calendly/Stripe/Formspree webhooks (requires Flask server)

The brief tells you: who they are, what tools they likely use,
which ones are CLOUD Act exposed, what compliance regime applies,
and what to say on the call.

Requirements:
  pip install anthropic requests

Environment variables:
  ANTHROPIC_API_KEY  — Claude API key (required)
  SMTP_HOST          — Email server (optional, for emailing briefs)
  SMTP_PORT          — Email port
  SMTP_USER          — Email sender
  SMTP_PASS          — Email password
  BRIEF_EMAIL        — Where to send briefs (default: josh@upperharbour.ca)
"""

import os
import re
import json
import sys
import logging
import smtplib
from datetime import datetime
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import Optional

import anthropic
import requests

logging.basicConfig(level=logging.INFO, format='%(asctime)s [%(levelname)s] %(message)s')
log = logging.getLogger(__name__)

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
SMTP_HOST = os.environ.get("SMTP_HOST", "smtp.gmail.com")
SMTP_PORT = int(os.environ.get("SMTP_PORT", "587"))
SMTP_USER = os.environ.get("SMTP_USER")
SMTP_PASS = os.environ.get("SMTP_PASS")
BRIEF_EMAIL = os.environ.get("BRIEF_EMAIL", "josh@upperharbour.ca")
SAAS_DB_PATH = os.environ.get("SAAS_DB_PATH", "saas-db.js")


# ── Company Extraction from Email ────────────────────────────

# Common personal email domains (don't try to look these up as companies)
PERSONAL_DOMAINS = {
    "gmail.com", "yahoo.com", "hotmail.com", "outlook.com", "live.com",
    "icloud.com", "me.com", "mac.com", "protonmail.com", "proton.me",
    "aol.com", "mail.com", "zoho.com", "fastmail.com", "tutanota.com",
    "hey.com", "pm.me",
}

def extract_company_from_email(email: str) -> Optional[str]:
    """Extract company domain from email address."""
    if not email or "@" not in email:
        return None
    domain = email.split("@")[1].lower()
    if domain in PERSONAL_DOMAINS:
        return None
    # Strip common prefixes
    company = domain.replace("www.", "").split(".")[0]
    return domain


def domain_to_company_name(domain: str) -> str:
    """Convert a domain to a likely company name for search."""
    # Remove TLD
    name = domain.split(".")[0]
    # Capitalize
    return name.capitalize()


# ── Load SaaS Database ──────────────────────────────────────

def load_saas_db(db_path: str = SAAS_DB_PATH) -> list[dict]:
    """Load tools from saas-db.js for cross-referencing."""
    tools = []
    try:
        with open(db_path, 'r') as f:
            src = f.read()
        
        # Extract tool entries
        entries = re.findall(
            r'\{\s*name:"([^"]+)"[^}]*parent:"([^"]+)"[^}]*jurisdiction:"([^"]+)"[^}]*cloudAct:(true|false)[^}]*risk:"([^"]+)"',
            src
        )
        for name, parent, jurisdiction, cloud_act, risk in entries:
            tools.append({
                "name": name,
                "parent": parent,
                "jurisdiction": jurisdiction,
                "cloud_act": cloud_act == "true",
                "risk": risk,
            })
    except Exception as e:
        log.warning(f"Failed to load saas-db.js: {e}")
    
    return tools


# ── Web Research ─────────────────────────────────────────────

def research_company(name: str, domain: str, person_name: str) -> dict:
    """
    Use Claude with web search to research a company and person.
    Returns structured research data.
    """
    if not ANTHROPIC_API_KEY:
        return {"error": "No API key"}
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    # Research query
    search_query = f"{domain} OR \"{domain_to_company_name(domain)}\" Canada company"
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=2000,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=[{
                "role": "user",
                "content": f"""Research this company for a pre-call sovereignty brief.

Person: {person_name}
Email domain: {domain}
Company name (likely): {domain_to_company_name(domain)}

Find:
1. Company name, what they do, industry, size estimate, location (city/province)
2. Whether they are public or private sector (government, healthcare, education, etc.)
3. What province they operate in (critical for determining compliance regime)
4. Any public information about their technology stack (job postings mentioning tools, press releases about cloud migrations, etc.)
5. The person's role/title if findable on LinkedIn or company website

Return a JSON object:
{{
  "company_name": "Full legal/trading name",
  "domain": "{domain}",
  "industry": "e.g., healthcare, finance, government, education, legal, technology",
  "sector": "public" or "private",
  "size_estimate": "e.g., 50-200 employees",
  "province": "e.g., Ontario, Quebec, Alberta, BC",
  "city": "e.g., Toronto",
  "description": "One sentence description of what they do",
  "person_name": "{person_name}",
  "person_title": "Title if found, or 'Unknown'",
  "tech_signals": ["Any tools or platforms mentioned in job postings, press releases, etc."],
  "public_sector_signals": ["Any indicators they serve or are part of government/public sector"],
  "compliance_signals": ["Any mentions of privacy, compliance, data sovereignty in their materials"]
}}

Return ONLY the JSON object."""
            }]
        )
        
        text = ""
        for block in response.content:
            if hasattr(block, 'text'):
                text += block.text
        
        text = text.strip().strip('```json').strip('```').strip()
        return json.loads(text)
    
    except Exception as e:
        log.warning(f"Company research failed: {e}")
        return {
            "company_name": domain_to_company_name(domain),
            "domain": domain,
            "error": str(e),
        }


def research_tech_stack(company_name: str, domain: str) -> list[str]:
    """
    Try to identify what SaaS tools a company uses via public signals.
    Uses job postings, BuiltWith-style data, and press releases.
    """
    if not ANTHROPIC_API_KEY:
        return []
    
    client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)
    
    try:
        response = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1000,
            tools=[{"type": "web_search_20250305", "name": "web_search"}],
            messages=[{
                "role": "user",
                "content": f"""Find what SaaS tools and cloud services this company likely uses.

Company: {company_name}
Domain: {domain}

Search their job postings, career pages, press releases, and any public tech stack information.
Look for mentions of: Salesforce, Microsoft 365, Google Workspace, Slack, Zoom, AWS, Azure, 
ServiceNow, Workday, SAP, HubSpot, Jira, Confluence, GitHub, Notion, Dropbox, Box, 
DocuSign, Shopify, QuickBooks, FreshBooks, or any other SaaS tools.

Return ONLY a JSON array of tool names that you found evidence of them using.
If you can't find any evidence, return an empty array: []
Do NOT guess — only include tools you found actual evidence for.

Return ONLY the JSON array."""
            }]
        )
        
        text = ""
        for block in response.content:
            if hasattr(block, 'text'):
                text += block.text
        
        text = text.strip().strip('```json').strip('```').strip()
        if text.startswith('['):
            return json.loads(text)
    
    except Exception as e:
        log.warning(f"Tech stack research failed: {e}")
    
    return []


# ── Cross-Reference with Database ────────────────────────────

def cross_reference_stack(detected_tools: list[str], saas_db: list[dict]) -> list[dict]:
    """
    Match detected tools against the sovereignty database.
    Returns matched tools with their sovereignty data.
    """
    matches = []
    db_names_lower = {t["name"].lower(): t for t in saas_db}
    
    for tool_name in detected_tools:
        tool_lower = tool_name.lower().strip()
        
        # Exact match
        if tool_lower in db_names_lower:
            matches.append(db_names_lower[tool_lower])
            continue
        
        # Partial match (e.g., "Microsoft Teams" matches "Microsoft Teams")
        for db_name, db_tool in db_names_lower.items():
            if tool_lower in db_name or db_name in tool_lower:
                matches.append(db_tool)
                break
    
    return matches


# ── Compliance Regime Assessment ─────────────────────────────

def assess_compliance(company_info: dict) -> dict:
    """
    Determine which compliance frameworks apply based on
    province, industry, and sector.
    """
    province = company_info.get("province", "").lower()
    industry = company_info.get("industry", "").lower()
    sector = company_info.get("sector", "").lower()
    
    regimes = []
    
    # Federal
    regimes.append({
        "framework": "PIPEDA",
        "applies": True,
        "reason": "Federal private-sector privacy law applies to all commercial activity",
    })
    
    # Provincial
    if "quebec" in province or "qc" in province:
        regimes.append({
            "framework": "Law 25 (Quebec)",
            "applies": True,
            "reason": "Quebec residents' data — TIAs required for cross-border transfers",
            "urgency": "high",
        })
    
    if "alberta" in province or "ab" in province:
        regimes.append({
            "framework": "PIPA / POPA (Alberta)",
            "applies": True,
            "reason": "Alberta private-sector (PIPA) or public-sector (POPA) privacy law",
        })
        if "public" in sector or "government" in sector or "health" in industry or "education" in industry:
            regimes.append({
                "framework": "POPA PIA requirement",
                "applies": True,
                "reason": "Alberta public bodies must complete PIAs for all SaaS tools — OIPC template mandatory",
                "urgency": "high",
            })
    
    if "british columbia" in province or "bc" in province:
        regimes.append({
            "framework": "FIPPA (BC)",
            "applies": "public" in sector,
            "reason": "BC public bodies — data residency requirements for personal information",
        })
        regimes.append({
            "framework": "PIPA (BC)",
            "applies": "private" in sector,
            "reason": "BC private-sector privacy law",
        })
    
    if "ontario" in province or "on" in province:
        if "health" in industry:
            regimes.append({
                "framework": "PHIPA (Ontario)",
                "applies": True,
                "reason": "Ontario health information privacy — strict requirements for health data",
                "urgency": "high",
            })
    
    # Sector-specific
    if "government" in sector or "public" in sector:
        regimes.append({
            "framework": "GC Cloud Framework",
            "applies": True,
            "reason": "Federal government cloud security requirements — Protected-B standard",
        })
    
    if "health" in industry:
        regimes.append({
            "framework": "Health data requirements",
            "applies": True,
            "reason": "Patient data has heightened sovereignty requirements across all provinces",
            "urgency": "high",
        })
    
    if "finance" in industry or "banking" in industry or "insurance" in industry:
        regimes.append({
            "framework": "OSFI guidelines",
            "applies": True,
            "reason": "Financial institutions — OSFI B-13 (technology and cyber risk) and outsourcing guidelines",
        })
    
    return {
        "primary": next((r["framework"] for r in regimes if r.get("urgency") == "high"), regimes[0]["framework"] if regimes else "PIPEDA"),
        "all_regimes": [r for r in regimes if r.get("applies", True)],
    }


# ── Generate Brief ───────────────────────────────────────────

def generate_brief(
    person_name: str,
    email: str,
    company_info: dict,
    matched_tools: list[dict],
    compliance: dict,
    source: str = "manual",
) -> str:
    """Generate the pre-call brief text."""
    
    company_name = company_info.get("company_name", "Unknown")
    province = company_info.get("province", "Unknown")
    industry = company_info.get("industry", "Unknown")
    sector = company_info.get("sector", "Unknown")
    person_title = company_info.get("person_title", "Unknown")
    
    # Count exposure
    exposed = [t for t in matched_tools if t.get("cloud_act")]
    canadian = [t for t in matched_tools if t.get("risk") == "canadian"]
    
    brief = f"""PRE-CALL BRIEF — {company_name}
{'='*60}
Generated: {datetime.now().strftime('%B %d, %Y at %I:%M %p ET')}
Source: {source}

CONTACT
  {person_name}
  {person_title}
  {email}

COMPANY
  {company_name}
  {company_info.get('city', '?')}, {province}
  Industry: {industry} | Sector: {sector}
  Size: {company_info.get('size_estimate', 'Unknown')}
  {company_info.get('description', '')}

COMPLIANCE REGIME
  Primary: {compliance['primary']}
"""
    
    for regime in compliance.get("all_regimes", []):
        urgency = " ⚠️ HIGH PRIORITY" if regime.get("urgency") == "high" else ""
        brief += f"  → {regime['framework']}{urgency}\n    {regime['reason']}\n"
    
    brief += f"""
THEIR STACK (from our database)
"""
    
    if matched_tools:
        for tool in matched_tools:
            status = "✗" if tool.get("cloud_act") else "✓"
            exposure = "CLOUD Act EXPOSED" if tool.get("cloud_act") else "Not exposed"
            brief += f"  {status} {tool['name']} — {tool['jurisdiction']} ({tool['parent']}) — {exposure}\n"
        
        if exposed:
            brief += f"\n  EXPOSURE: {len(exposed)} of {len(matched_tools)} confirmed tools are CLOUD Act exposed\n"
        else:
            brief += f"\n  All {len(matched_tools)} confirmed tools are Canadian-jurisdiction ✓\n"
    else:
        brief += "  No tools confirmed through public sources.\n"
        brief += "  Ask on the call: What's your core SaaS stack? (M365, Google, Salesforce, etc.)\n"
    
    # Determine likely needs and talking points
    brief += f"""
LIKELY NEEDS
"""
    
    if compliance["primary"] in ["Law 25 (Quebec)", "POPA PIA requirement"]:
        brief += "  → TIA/PIA documentation (they probably need this urgently)\n"
    if exposed:
        brief += "  → CLOUD Act exposure assessment for their stack\n"
        brief += "  → Sovereign alternative evaluation\n"
    if len(matched_tools) >= 3:
        brief += "  → Full sovereignty assessment ($5K+ consulting)\n"
    else:
        brief += "  → Start with a $500 custom assessment to map their full stack\n"
    
    brief += f"""
TALKING POINTS
"""
    
    # Generate contextual talking points
    if any("Microsoft" in t["name"] for t in exposed):
        brief += "  1. Their Microsoft deployment is the biggest exposure — mention the\n"
        brief += "     Anton Carniaux French Senate testimony (\"obligated to comply\n"
        brief += "     regardless of where the data is stored\")\n"
    elif exposed:
        top_exposed = exposed[0]
        brief += f"  1. {top_exposed['name']} is their highest-profile exposed tool —\n"
        brief += f"     parent is {top_exposed['parent']} ({top_exposed['jurisdiction']})\n"
    else:
        brief += "  1. Ask about their core stack — most orgs don't know their\n"
        brief += "     exposure until someone maps it\n"
    
    if "quebec" in province.lower():
        brief += "  2. Law 25 TIA deadline has passed — they may already be non-compliant\n"
        brief += "     on cross-border data transfers\n"
    elif "alberta" in province.lower():
        brief += "  2. Alberta PMP deadline is June 2026 — PIAs are a prerequisite\n"
        brief += "     and the OIPC template is now mandatory\n"
    else:
        brief += "  2. PIPEDA reform is coming — organizations that document their\n"
        brief += "     sovereignty posture now will be ahead when enforcement tightens\n"
    
    brief += "  3. Offer: \"Let me run a quick HarbourScan on your stack right now\"\n"
    brief += "     — this is the fastest way to demonstrate value on the call\n"
    
    # Recommended product path
    brief += f"""
RECOMMENDED PATH
"""
    if len(matched_tools) == 0:
        brief += "  Start: Free HarbourScan on the call → $99 industry report\n"
        brief += "  Upgrade: $500 custom assessment once stack is known\n"
    elif len(exposed) >= 3:
        brief += "  Start: $500 custom assessment (they have enough exposure to justify it)\n"
        brief += "  Upgrade: $5K sovereignty assessment if stack is complex\n"
    else:
        brief += "  Start: $99 industry report → $500 custom assessment\n"
        brief += "  Upgrade: Consulting if they need migration support\n"
    
    brief += f"""
{'='*60}
"""
    
    return brief


# ── Email the Brief ──────────────────────────────────────────

def email_brief(brief: str, subject: str):
    """Send the brief to Josh via email."""
    if not SMTP_USER or not SMTP_PASS:
        log.warning("No SMTP credentials — printing brief to stdout instead")
        print(brief)
        return
    
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = SMTP_USER
    msg['To'] = BRIEF_EMAIL
    
    # Plain text version
    msg.attach(MIMEText(brief, 'plain'))
    
    # HTML version (monospace for formatting)
    html_brief = f"""
    <html>
    <body style="background:#0A1018;color:#EAF0F4;font-family:monospace;padding:32px;">
    <pre style="font-size:13px;line-height:1.6;white-space:pre-wrap;">{brief}</pre>
    </body>
    </html>
    """
    msg.attach(MIMEText(html_brief, 'html'))
    
    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as server:
            server.starttls()
            server.login(SMTP_USER, SMTP_PASS)
            server.send_message(msg)
        log.info(f"Brief emailed to {BRIEF_EMAIL}")
    except Exception as e:
        log.error(f"Email failed: {e}")
        print(brief)


# ── Main Pipeline ────────────────────────────────────────────

def generate_lead_brief(person_name: str, email: str, source: str = "manual") -> str:
    """
    Full pipeline: research → cross-reference → assess → generate → deliver.
    """
    log.info(f"Generating brief for {person_name} ({email})")
    
    # 1. Extract company from email
    domain = extract_company_from_email(email)
    if not domain:
        log.info(f"Personal email domain — limited research possible")
        domain = email.split("@")[1] if "@" in email else "unknown"
    
    # 2. Research the company
    log.info(f"Researching company: {domain}")
    company_info = research_company(person_name, domain, person_name)
    
    # 3. Research their tech stack
    log.info(f"Researching tech stack...")
    company_name = company_info.get("company_name", domain_to_company_name(domain))
    detected_tools = research_tech_stack(company_name, domain)
    
    # Also add any tools from the company research
    tech_signals = company_info.get("tech_signals", [])
    for signal in tech_signals:
        if signal not in detected_tools:
            detected_tools.append(signal)
    
    log.info(f"Detected tools: {detected_tools}")
    
    # 4. Cross-reference with sovereignty database
    saas_db = load_saas_db()
    matched_tools = cross_reference_stack(detected_tools, saas_db)
    log.info(f"Matched {len(matched_tools)} tools in database")
    
    # 5. Assess compliance regime
    compliance = assess_compliance(company_info)
    
    # 6. Generate the brief
    brief = generate_brief(
        person_name=person_name,
        email=email,
        company_info=company_info,
        matched_tools=matched_tools,
        compliance=compliance,
        source=source,
    )
    
    # 7. Deliver
    subject = f"Pre-Call Brief: {person_name} — {company_info.get('company_name', domain)}"
    email_brief(brief, subject)
    
    return brief


# ── Webhook Handlers (for future Flask/FastAPI server) ────────

def handle_calendly_webhook(data: dict) -> str:
    """Process a Calendly booking webhook."""
    invitee = data.get("payload", {}).get("invitee", {})
    name = invitee.get("name", "Unknown")
    email = invitee.get("email", "")
    
    if not email:
        log.warning("Calendly webhook missing email")
        return ""
    
    return generate_lead_brief(name, email, source="Calendly booking")


def handle_stripe_webhook(data: dict) -> str:
    """Process a Stripe purchase webhook."""
    customer = data.get("data", {}).get("object", {}).get("customer_details", {})
    name = customer.get("name", "Unknown")
    email = customer.get("email", "")
    amount = data.get("data", {}).get("object", {}).get("amount_total", 0)
    
    if not email:
        log.warning("Stripe webhook missing email")
        return ""
    
    product = "$99 report" if amount <= 10000 else "$500 custom" if amount <= 55000 else "$2,500 package"
    return generate_lead_brief(name, email, source=f"Stripe purchase ({product})")


def handle_formspree_webhook(data: dict) -> str:
    """Process a Formspree vendor form submission."""
    name = data.get("name", data.get("_replyto", "Unknown"))
    email = data.get("email", data.get("_replyto", ""))
    
    if not email:
        log.warning("Formspree webhook missing email")
        return ""
    
    return generate_lead_brief(name, email, source="Vendor form submission")


# ── CLI ──────────────────────────────────────────────────────

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python lead_brief.py \"Name\" \"email@company.com\"")
        print()
        print("Examples:")
        print('  python lead_brief.py "Sarah Chen" "sarah@telus.com"')
        print('  python lead_brief.py "Marc Dubois" "marc@ville.montreal.qc.ca"')
        print('  python lead_brief.py "John Smith" "john@gmail.com"')
        sys.exit(1)
    
    name = sys.argv[1]
    email = sys.argv[2]
    source = sys.argv[3] if len(sys.argv) > 3 else "manual"
    
    brief = generate_lead_brief(name, email, source)
    
    # Also save to file
    safe_name = re.sub(r'[^a-zA-Z0-9]', '-', name.lower())
    output_path = f"briefs/brief-{safe_name}-{datetime.now().strftime('%Y%m%d')}.txt"
    os.makedirs("briefs", exist_ok=True)
    with open(output_path, 'w') as f:
        f.write(brief)
    log.info(f"Brief saved to {output_path}")
