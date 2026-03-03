This is a static HTML site for upperharbour.ca hosted on GitHub Pages.

## The database

There is ONE database file: `saas-db.js` in the repo root. Every page loads it via `<script src="/saas-db.js">`. There is no copy in assets/ — do not create one. All tools, all stats, all automation flows from this single file. Currently 715 tools across 32 categories including SaaS and cloud infrastructure.

## Adding a tool

1. Add the entry to `saas-db.js` (see UPDATE-GUIDE.md for format and risk tier rules)
2. Update the `lastUpdated` timestamp in `saasDBMeta` at the bottom of the file
3. Run: `python3 update-schema-stats.py` (updates JSON-LD schema and meta tags for SEO)
4. Commit and push

All visible numbers on the site update automatically — `assets/uh-stats.js` computes stats from `saas-db.js` at runtime and populates every `<span class="uh-stat">` element. The hardcoded values in HTML are fallbacks for crawlers only.

## How stats flow

- `saas-db.js` — the single canonical database (root of repo, loaded by every page)
- `assets/uh-stats.js` — client-side script, computes stats from saas-db.js, populates `<span class="uh-stat" data-stat="statName">fallback</span>` elements across all pages
- `update-schema-stats.py` — run manually after DB changes, updates JSON-LD schema blocks and meta tags, saves reference to `assets/schema-stats-ref.json`
- Three pages (tools.html, research.html, research/canadian-technology-sovereignty-index.html) have additional inline JS that reads `saasDB` directly for charts, tables, and search — these also update automatically

## Site structure

Navigation: Signals | Tools | Research | Guides | [Run HarbourScan]
Footer columns: Platform (HarbourScan, Sovereignty Index, Signals, Research, Methodology, Compliance Guides, Pricing) | About (Founder, LinkedIn, Contact)
Footer tagline: "Technology sovereignty intelligence for Canadian organizations."

Google Analytics: G-3KSW0FVBL1 (GA tag in all HTML files, added March 2026)

Standalone pages with own nav (do not update): law25.html, sovereignty.html

## Key pages

- `index.html` — Homepage (severity classification framing, "How exposed are you?" CTA)
- `harbourscan.html` — HarbourScan tool (severity rating: Low/Moderate/High/Critical, free export, four-tier pricing)
- `tools.html` — Sovereignty Index (715 tools, search/filter)
- `research.html` — Research hub (6 research cards including cloud infrastructure)
- `methodology.html` — Classification framework
- `pricing.html` — Four-tier pricing
- `research/canadian-technology-sovereignty-index.html` — Flagship research (renamed from SaaS Sovereignty Index, March 2026)
- `research/cloud-infrastructure-sovereignty.html` — Cloud infrastructure analysis (25 providers, 7 Canadian sovereign)
- `research/government-saas-audit.html` — Government SaaS audit
- `research/provincial-exposure-index.html` — Provincial analysis
- `research/sovereignty-policy-scorecard.html` — Policy scorecard
- `research/sovereignty-acquisition-tracker.html` — Acquisition tracker
- `tools/thinkon.html` — ThinkOn sovereignty analysis
- `tools/micrologic.html` — Micrologic sovereignty analysis
- `tools/estruxture.html` — eStruxture sovereignty analysis
- `tools/hypertec-cloud.html` — Hypertec Cloud sovereignty analysis
- `tools/bell-cloud.html` — Bell Cloud / AI Fabric sovereignty analysis
- `tools/telus-cloud.html` — TELUS Cloud sovereignty analysis
- `tools/opentext-sovereign-cloud.html` — OpenText Sovereign Cloud sovereignty analysis
- `tools/aws.html`, `tools/slack.html`, etc. — Foreign provider analyses

## Key files

- `saas-db.js` — the database (all tools, repo root, the ONLY copy)
- `assets/uh-stats.js` — client-side dynamic stats
- `assets/schema-stats-ref.json` — tracks current schema values for the updater
- `update-schema-stats.py` — schema/meta tag updater script
- `signals_pipeline.py` — automated signals collection (runs via GitHub Actions)
- `UPDATE-GUIDE.md` — full database update documentation
- `CLASSIFICATION-RUBRIC.md` — risk tier classification rules
- `SITE-BIBLE.md` — site strategy and content reference
- `business-sherpa.md` — master strategy document (share at start of AI conversations)

No frameworks. Vanilla HTML, CSS, and JS.

## Recent changes (March 2026)

- Renamed "Canadian SaaS Sovereignty Index" → "Canadian Technology Sovereignty Index" (file renamed, redirect at old URL)
- Added 25 cloud infrastructure entries (7 Canadian, 9 Review, 4 Non-exposed, 5 Exposed) — total now 715
- Built cloud infrastructure research page (`/research/cloud-infrastructure-sovereignty`)
- Built 7 Canadian provider tool detail pages (`/tools/thinkon`, `/tools/micrologic`, etc.)
- Added severity rating system to HarbourScan (Low/Moderate/High/Critical Exposure)
- Added free export (downloadable summary) to HarbourScan
- Added Google Analytics (G-3KSW0FVBL1) to all 45+ HTML files
- Updated all hardcoded counts from 707→715 and corrected percentages site-wide
- Updated homepage and HarbourScan copy to lead with severity classification framing
