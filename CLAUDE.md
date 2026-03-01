This is a static HTML site for upperharbour.ca hosted on GitHub Pages.

## The database

There is ONE database file: `saas-db.js` in the repo root. Every page loads it via `<script src="/saas-db.js">`. There is no copy in assets/ — do not create one. All tools, all stats, all automation flows from this single file.

## Adding a tool

1. Add the entry to `saas-db.js` (see UPDATE-GUIDE.md for format and risk tier rules)
2. Update the `lastUpdated` timestamp in `saasDBMeta` at the bottom of the file
3. Run: `python3 update-schema-stats.py` (updates JSON-LD schema and meta tags for SEO)
4. Commit and push

All visible numbers on the site update automatically — `assets/uh-stats.js` computes stats from `saas-db.js` at runtime and populates every `<span class="uh-stat">` element. The hardcoded values in HTML are fallbacks for crawlers only.

## How stats flow

- `saas-db.js` — the single canonical database (root of repo, loaded by every page)
- `assets/uh-stats.js` — client-side script, computes stats from saas-db.js, populates `<span class="uh-stat" data-stat="statName">fallback</span>` elements across 16 pages
- `update-schema-stats.py` — run manually after DB changes, updates JSON-LD schema blocks and meta tags, saves reference to `assets/schema-stats-ref.json`
- Three pages (tools.html, research.html, research/canadian-saas-sovereignty-index.html) have additional inline JS that reads `saasDB` directly for charts, tables, and search — these also update automatically

## Site structure

Navigation: Research | Sovereignty Index | Methodology | Signals | Compliance | [Run HarbourScan]
Footer columns: Platform (HarbourScan, Sovereignty Index, Signals, Research, Methodology, Compliance Guides, Pricing) | About (Founder, LinkedIn, Contact)
Footer tagline: "Technology sovereignty intelligence for Canadian organizations."

Pages added February 2026: methodology.html, pricing.html, resources/data-sovereignty-compliance-2026.html
Standalone pages with own nav (do not update): law25.html, sovereignty.html
Deleted: engagements.html

## Key files

- `saas-db.js` — the database (all tools, repo root, the ONLY copy)
- `assets/uh-stats.js` — client-side dynamic stats
- `assets/schema-stats-ref.json` — tracks current schema values for the updater
- `update-schema-stats.py` — schema/meta tag updater script
- `signals_pipeline.py` — automated signals collection (runs via GitHub Actions)
- `UPDATE-GUIDE.md` — full database update documentation
- `CLASSIFICATION-RUBRIC.md` — risk tier classification rules
- `SITE-BIBLE.md` — site strategy and content reference

No frameworks. Vanilla HTML, CSS, and JS.
