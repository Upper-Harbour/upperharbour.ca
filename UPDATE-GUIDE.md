# Updating the Database

When Claude (or anyone) adds, removes, or edits a tool in `saas-db.js`, here's what happens and what to do.

---

## What updates automatically (you do nothing)

**Every visible number on every page** updates itself. This includes:

- The animated counters on the homepage (tool count, foreign %, CLOUD Act %, Canadian %)
- All body text that says "715 tools" or "89% of tools offering Canadian residency" etc.
- The Sovereignty Index page charts, tables, stats, and category breakdowns
- The research hub page stats
- HarbourScan's scan logic and tool matching
- The tools page search, filters, and stat boxes

This works because `uh-stats.js` (loaded on every page) reads `saas-db.js` at runtime and computes fresh numbers. The hardcoded values in the HTML (like "715") are just fallbacks for search engine crawlers — real visitors always see live computed numbers.

---

## What needs the update script

**JSON-LD schema markup and meta tags** contain hardcoded numbers that Google reads directly from the HTML source. These are invisible to users but matter for SEO. The script `update-schema-stats.py` updates these automatically.

Pages with schema markup that gets updated:
- index.html (meta tags)
- founder.html (Person schema)
- methodology.html (schema description)
- tools.html (schema description)
- research/canadian-technology-sovereignty-index.html (6 FAQ answers with stats)
- research/cloud-infrastructure-sovereignty.html (FAQ answers with provider counts)
- research/athena-collective-law-25-compliance.html (FAQ answer)
- research/sovereignty-policy-scorecard.html (FAQ answer)
- resources/canadian-data-residency-saas.html (2 FAQ answers)
- resources/law-25-saas-compliance.html (FAQ answer)
- resources/transfer-impact-assessments-law-25.html (FAQ answer)

---

## The workflow

After editing `saas-db.js`:

```
python3 update-schema-stats.py
git add -A
git commit -m "Add [tool name]"
git push
```

That's it. The script reads saas-db.js, computes fresh stats, and updates every schema block and meta tag across the site. It also saves a reference file (`assets/schema-stats-ref.json`) so it knows what numbers to look for next time.

---

## Adding a tool to saas-db.js

Each tool entry looks like this:

```javascript
{ name:"Tool Name", parent:"Parent Company Inc.", hq:"City, Country", jurisdiction:"United States", cloudAct:true, dataResidency:"US/CA", note:"Brief description of the tool, its ownership, and sovereignty implications.", risk:"exposed", category:"category-name", industries:["industry1","industry2"] },
```

**Required fields:**
- `name` — the product name users know
- `parent` — the legal parent entity (check SEC filings, corporate registries)
- `hq` — headquarters city and country
- `jurisdiction` — country of incorporation of the ultimate parent
- `cloudAct` — `true` if subject to US CLOUD Act (any US-incorporated entity in the ownership chain)
- `dataResidency` — where data can be stored (e.g. "US", "US/CA/EU", "Canada")
- `note` — 1-2 sentences explaining ownership structure and sovereignty implications
- `risk` — one of: `"canadian"`, `"review"`, `"non_exposed"`, `"exposed"`
- `category` — must match an existing category in the database
- `industries` — array of relevant industry tags

**Risk tier rules:**
- `"canadian"` — Canadian-headquartered, majority Canadian-owned, no foreign parent
- `"review"` — Canadian HQ with foreign backing, or foreign parent with Canadian residency available
- `"non_exposed"` — Non-US foreign jurisdiction, not subject to CLOUD Act
- `"exposed"` — US-parented or US-incorporated, subject to CLOUD Act

**Also update the metadata timestamp:**

```javascript
var saasDBMeta = {
  lastUpdated: "2026-03-01T10:00:00-05:00",  // ← update this date
  version: "2026-Q1",
  totalTools: saasDB.length
};
```

---

## Other files that may need manual updates (infrequently)

These files reference tool counts but aren't covered by the automated system:

- `llms.txt` — plain text, update when count changes significantly
- `SITE-BIBLE.md` — internal reference doc
- `CLASSIFICATION-RUBRIC.md` — breakdown table

These only matter for internal reference and AI context. Update them periodically, not on every tool addition.

---

## How the system works (technical reference)

**Database: `saas-db.js` (repo root)**
The single canonical database. Every page loads it via `<script src="/saas-db.js">`. There is no copy elsewhere — do not create one in assets/ or anywhere else.

**Client-side: `assets/uh-stats.js`**
Loaded by every page alongside `saas-db.js`. Computes stats from the database and populates any HTML element with `class="uh-stat"` and a `data-stat` attribute. Example: `<span class="uh-stat" data-stat="totalTools">715</span>` gets its text replaced with the live count.

Three pages (tools.html, research.html, research/canadian-technology-sovereignty-index.html) also have their own inline JS that reads `saasDB` directly for charts, tables, and search — these update automatically too.

Available data-stat values: `totalTools`, `foreignPct`, `cloudActPct`, `canadianPct`, `reviewPct`, `nonExposedPct`, `exposedPct`, `caResExposedPct`, `nonCanadianPct`, `categoryCount`, `lastUpdated`

**Build-time: `update-schema-stats.py`**
Run manually after DB changes. Reads saas-db.js (repo root) with regex, computes the same stats, finds old values in JSON-LD schema blocks and meta tags, replaces with new values. Uses `assets/schema-stats-ref.json` to track what values are currently in the files.
