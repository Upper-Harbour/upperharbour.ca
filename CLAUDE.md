This is a static HTML site for upperharbour.ca hosted on GitHub Pages. The main database is assets/saas-db.js containing SaaS tools mapped to parent jurisdictions, CLOUD Act exposure, and sovereignty risk tiers.

## Database updates

When adding a tool to assets/saas-db.js, run these commands afterward:

```
python3 update-schema-stats.py
git add -A
git commit -m "Add [tool name]"
git push
```

The script updates hardcoded numbers in JSON-LD schema blocks and meta tags across all HTML files. Visible page text updates automatically via assets/uh-stats.js (client-side).

See UPDATE-GUIDE.md for full details on the tool entry format, risk tier rules, and how the system works.

## Dynamic stats system

- `assets/uh-stats.js` — loaded by every page, computes stats from saas-db.js at runtime, populates any `<span class="uh-stat" data-stat="statName">fallback</span>` element
- `update-schema-stats.py` — run manually after DB changes, updates JSON-LD schema and meta tags, saves reference values to `assets/schema-stats-ref.json`
- Hardcoded numbers in HTML are fallbacks only — real visitors see live computed values

## Site structure

Navigation: Research | Sovereignty Index | Methodology | Signals | Compliance | [Run HarbourScan]
Footer columns: Platform (HarbourScan, Sovereignty Index, Signals, Research, Methodology, Compliance Guides, Pricing) | About (Founder, LinkedIn, Contact)
Footer tagline: "Technology sovereignty intelligence for Canadian organizations."

Pages added February 2026: methodology.html, pricing.html, resources/data-sovereignty-compliance-2026.html
Standalone pages with own nav (do not update): law25.html, sovereignty.html
Deleted: engagements.html

## Key files

- `assets/saas-db.js` — the database (all tools)
- `assets/uh-stats.js` — client-side dynamic stats
- `assets/schema-stats-ref.json` — tracks current schema values for the updater
- `update-schema-stats.py` — schema/meta tag updater script
- `signals_pipeline.py` — automated signals collection (runs via GitHub Actions)
- `UPDATE-GUIDE.md` — full database update documentation
- `CLASSIFICATION-RUBRIC.md` — risk tier classification rules
- `SITE-BIBLE.md` — site strategy and content reference

No frameworks. Vanilla HTML, CSS, and JS.
