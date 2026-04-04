# Upper Harbour — Canonical Decisions & Frameworks

Last updated: April 3, 2026

## Risk Classification Framework

### Three-Tier Risk Model
Canadian tools are classified into three tiers based on jurisdiction, not just hosting:

1. **Canadian** (`risk: "canadian"`) — Canadian-incorporated, no significant US operations, Canadian hosting available
   - Examples: Clio, 1Password, Sync.com, Edsby
   - These tools get a green badge in the Sovereignty Index

2. **Review Required** (`risk: "review"`) — One of two scenarios:
   - **US-incorporated but Canadian data residency available** — e.g., Microsoft 365, Salesforce (Hyperforce), Jira (Atlassian), DocuSign
   - **Canadian-incorporated but with US operations/hosting that create indirect CLOUD Act pathway** — e.g., Hootsuite (CDN company, AWS US hosting), FreshBooks (CDN company, GCP US hosting), Genius ERP (CDN company, US subsidiary)
   - These tools get an amber badge

3. **Exposed** (`risk: "exposed"`) — US-incorporated, CLOUD Act subject, no Canadian data residency
   - Examples: Slack, Zoom, Dropbox, Notion, Mailchimp
   - These tools get a red badge

### CLOUD Act Exposure Through US Subsidiaries

**Critical framework decision (March 30, 2026):**

A Canadian-incorporated company that has a US subsidiary is **not directly** CLOUD Act exposed — the Canadian parent's jurisdiction remains Canada. However, the US subsidiary **does** create an indirect CLOUD Act pathway:

- The CLOUD Act applies to any provider "subject to the jurisdiction of the US"
- A US subsidiary has general jurisdiction in the US
- US authorities can serve the US subsidiary with legal process for data in its "possession, custody, or control"
- If the US subsidiary has practical access to the Canadian parent's systems, that data may be reachable
- Per Osler: "US law enforcement can serve legal process on the US entity, compelling it to produce data, even if the data is held by a foreign parent or affiliate"
- Per Covington: "This can include data held by a foreign parent or other foreign affiliate, if that data is within the subsidiary's possession, custody, or control"

**Classification rule:**
- `jurisdiction: "Canada"` — correct, the parent is Canadian
- `cloudAct: false` — the Canadian parent is not directly subject
- `risk: "review"` — NOT "canadian", because the US operations create an indirect pathway
- Note field documents the US subsidiary as a risk factor

This is consistent with how Hootsuite and FreshBooks are handled — Canadian companies with US infrastructure exposure get "review", not "canadian" or "exposed".

### Data Residency vs Jurisdiction
These are two different compliance dimensions:
- **Data residency** = where data physically sits (servers in Canada)
- **Jurisdiction** = which government can legally compel access
- A US company hosting data in Canada is still CLOUD Act exposed
- A Canadian company hosting data in the US has an indirect exposure pathway
- Conflating these two is "the most common mistake in Canadian privacy compliance"

## Tool Page Standards

### Quality Standard
[DECISION] Josh wants each tool page individually researched to be genuinely authoritative — "the only source I really need on this topic for this vendor." No template-generated pages for high-use tools.

[DECISION] Every tool in the database gets the same quality treatment — no corners cut regardless of perceived importance.

[DECISION] Josh called out batch-built pages (OpenAI, Salesforce, DocuSign, AWS, TELUS Cloud) as cutting corners — these need to be redone properly with fresh research one by one.

### Research Requirements (per page)
1. Web search for corporate jurisdiction (SEC filings, incorporation records)
2. Web search for data hosting specifics (residency, regions, encryption)
3. Database cross-check and correction
4. Unique analytical angle (not generic)
5. Comparison table with verified competitor data
6. FAQ schema with researched answers

### Template (Gospel Format)
Base template: `tools/dropbox.html` — Josh's definitive version

Every tool page must include:
- Risk gauge animation (score out of 10)
- Bento cards (parent company, CLOUD Act status, CDN residency, encryption, TIA/PIA required)
- Jurisdiction flow diagram
- Expand/collapse sections (Regulatory Analysis, Alternatives, Technical, FAQ)
- Comparison table
- FAQ schema (structured data for Google)
- Mid-page CTA (HarbourScan)
- Contact box (Calendly + email)
- Cross-links to paid services (TIA $99, PIA Research Tool, HarbourScan)
- Inline author byline
- Methodology/verified box

### SEO Gospel
- Title: <60 chars, question format preferred ("Is X Safe for Canadian Data?")
- Description: <160 chars, include risk score
- H2s as questions where possible
- FAQ schema matching the FAQ section
- OG tags matching meta tags
- Canonical URL set

## Site Architecture

### Hosting
- **GitHub Pages** with **Cloudflare DNS/CDN** (NOT Cloudflare Pages)
- Static only — no server-side functions
- Cloudflare caches aggressively — append `?v=N` to bust cache

### Database
- `saas-db.js` at root — global `saasDB` array
- Currently 755 tools
- Cross-check database after every tool page research

### Key Files — DO NOT OVERWRITE
- `harbourscan.html` — contains ~1000 lines of wizard JS
- `alberta-pia.html` — Josh built the definitive version

### Stripe
- Publishable key: `pk_live_51T7jm1HacAqcnAkVNz7quTDA5wMMmlzdS0GtumcVDy2XNAbone5VCl7eqklWgfhVlgA9PRa7T4F3G7aj3nLbJ2Vz004QLuyxlP`
- Alberta PIA Buy Button: `buy_btn_1TGB6eHacAqcnAkVEOryP5ce`

### Git
```
cd /home/claude/upperharbour.ca
git config user.email "josh@upperharbour.ca"
git config user.name "Upper Harbour"
```

## Products & Pricing
- **TIA Reports:** $99 (via /comply)
- **PIA Research Tool:** $199 (via /alberta-pia)
- **HarbourScan:** Free tier + paid (via /harbourscan)
- **Consulting:** Via Calendly (https://calendly.com/josh-upperharbour/30min)

## Content Tone
- Authoritative but not alarmist
- Nuanced — acknowledge genuine safeguards (Canadian residency, BYOK) while documenting jurisdictional exposure
- "Acceptable risk with documented safeguards" is a valid conclusion
- The organizations that get into trouble are the ones without documentation, not the ones using US tools

## Consulting Page (April 2026)

[DECISION] Consulting page is landing page format, not article — no byline, `landing-hero` format matching HarbourScan page. First price visitor sees is $5,000+.

[DECISION] Self-serve products ($99 reports) removed from consulting page. Soft catch at bottom only: "Not sure you need consulting? Start with a $99 compliance report or a free HarbourScan." Avoids undercutting consulting tiers with a $99 anchor.

[DECISION] "Consulting" appears in footer only, not navigation header. Wait until site-driven consulting leads prove demand before promoting in header nav.

## Footer & Navigation (April 2026)

[DECISION] "For Vendors" renamed to "Vendors" across all pages — cleaner, less wordy.

[DECISION] Footer link order: HarbourScan, Sovereignty Index, Signals, Research, Methodology, Compliance Guides, Consulting, Vendors, Compliance Reports.

## CTA Strategy (April 2026)

[DECISION] Compliance-oriented pages (TIA templates, PIA guides, compliance checklists) → CTA points to `/comply` (paid reports).

[DECISION] Research-oriented pages (cloud infrastructure sovereignty, data pages) → CTA stays on HarbourScan (free tool).

[DECISION] Alberta PIA pages → CTA points to `/alberta-pia` (specialized product).

## GTM Agent Architecture (April 2026)

[DECISION] Single-agent system with human-in-the-loop beats 4 autonomous agents at current stage. The signals pipeline already handles content collection. Identified 6 gaps, building incrementally.

[DECISION] Acquisition tripwire runs as its own daily GitHub Actions workflow (7am ET), separate from signals pipeline. SEC EDGAR free API, no key required.

[DECISION] Lead brief generator deployed on Railway server. Triggered by webhooks (Calendly bookings, Stripe purchases), not running on a schedule.

[DECISION] Signals pipeline frequency changed from every 6 hours to once daily at 7am ET to reduce API costs. SEC filings and news don't change fast enough to justify 4x daily runs.

## Infrastructure (April 2026)

[DECISION] Railway.app chosen for server hosting — $5/month, auto-deploys from GitHub, simplest option for a non-technical founder. Server repo is `upperharbour-server` (private, separate from the static site repo).

[DECISION] Server handles: Calendly webhooks (lead briefs), Stripe webhooks (purchase notifications), manual brief endpoint. Static site stays on GitHub Pages + Cloudflare.

[DECISION] Calendly upgraded to Standard plan ($10/month) to enable webhook API for automated lead brief generation. This is the highest-ROI spend in the GTM stack — walking into calls with prospect research is the difference between discovery and closing.

## Canadian Provider Tool Pages (April 2026)

[DECISION] Canadian-owned providers (Bell, eStruxture, Hypertec, Micrologic, OpenText, ThinkOn) get the same gospel template as US-exposed tools but with risk score 1.0/10, all-green bento cards, and all-green jurisdiction flow diagrams. These pages serve as "safe alternative" destinations from the high-risk tool pages.

[DECISION] Comparison tables on Canadian provider pages include both Canadian alternatives and US competitors (Equinix, Cologix, AWS, Azure, etc.) to show the sovereignty contrast. This makes the pages useful for procurement officers doing vendor comparisons.
