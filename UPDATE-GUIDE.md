# What Auto-Updates vs What Doesn't
## When you add tools to saas-db.js

---

## ✅ FULLY AUTOMATIC (computed from saasDB at runtime)

| Page | What auto-updates |
|------|-------------------|
| `tools.html` | Stat boxes (total, exposed, review, canadian), search count, hero paragraph total |
| `research/canadian-saas-sovereignty-index.html` | All body text spans (introTotal, bodyTotal, bodyTotal2, statTools, bodyUSCount, bodyUSPct, bodyCaResPct, bodyCdnPct, sampleCount, sampleTotal, ownerTotal, etc.), stat boxes, category table, sample table |
| `research.html` (hub) | Hero subtitle, browse count, paper description, all interactive category data |
| `harbourscan.html` | Tool matching/lookups |

These pages load `saas-db.js` and compute everything from `saasDB.length` and filters.

---

## ❌ HARDCODED — Must manually update on each DB change

### index.html (homepage) — does NOT load saas-db.js
- Line 7: meta description ("324 tools")
- Line 12: og:description ("324 SaaS tools")  
- Line 19: twitter:description ("324 SaaS tools")
- Line 147: hero eyebrow ("324 SaaS Tools Mapped")
- Line 149: hero paragraph ("We mapped 324 SaaS tools...")
- Line 152: data-target="324" (animated counter)
- Line 182: "324-tool database"
- Line 197: "324 SaaS tools mapped"
- Line 376: JS string "all 324 tools"

### tools.html — meta tags & structured data only
- Line 6: `<title>` ("324 Tools Mapped")
- Line 7: meta description ("Search 324 SaaS tools")
- Line 11: og:title ("324 Tools Mapped")
- Line 12: og:description ("Search 324 SaaS tools")
- Line 138: JSON-LD description ("Search 324+ SaaS tools")

### harbourscan.html — prose text
- Line ~550: "324-tool Sovereignty Index database"
- Line ~576: "324-tool database"

### research/canadian-saas-sovereignty-index.html — meta tags, JSON-LD FAQ, body FAQ
- Lines 6-7, 11-12, 21-22, 32-33: meta/og/twitter/JSON-LD headline (all say "324")
- Lines 49, 64, 74, 84, 89, 94, 104, 109: JSON-LD FAQ answers (hardcoded stats + percentages)
- Lines 260, 272, 276, 280: Body FAQ text (hardcoded stats)

### Other pages with hardcoded count
- `engagements.html`: meta description, hero paragraph, diff item
- `founder.html`: JSON-LD description
- `research/sovereignty-acquisition-tracker.html`: body text
- `research/sovereignty-policy-scorecard.html`: JSON-LD FAQ, methodology text
- `research/government-saas-audit.html`: references to main DB count
- `resources/saas-inventory-compliance.html`: body text
- `resources/foreign-jurisdiction-saas-action-guide.html`: body text
- `llms.txt`: multiple references
- `SITE-BIBLE.md`: multiple references
- `CLASSIFICATION-RUBRIC.md`: breakdown table

---

## Fastest update method for future tool additions

```bash
# After updating saas-db.js, run this from repo root:
NEW_COUNT=$(grep -c 'name:"' assets/saas-db.js)
OLD_COUNT=324  # update this to current count

find . -type f \( -name "*.html" -o -name "*.md" -o -name "*.txt" \) \
  -not -path "./__MACOSX/*" \
  -exec sed -i "s/${OLD_COUNT} SaaS/${NEW_COUNT} SaaS/g; \
    s/${OLD_COUNT}-tool/${NEW_COUNT}-tool/g; \
    s/${OLD_COUNT} tools/${NEW_COUNT} tools/g; \
    s/${OLD_COUNT} Tools/${NEW_COUNT} Tools/g; \
    s/>${OLD_COUNT}</>${NEW_COUNT}</g; \
    s/target=\"${OLD_COUNT}\"/target=\"${NEW_COUNT}\"/g; \
    s/of ${OLD_COUNT}/of ${NEW_COUNT}/g; \
    s/${OLD_COUNT} commonly/${NEW_COUNT} commonly/g; \
    s/${OLD_COUNT}+/${NEW_COUNT}+/g; \
    s/all ${OLD_COUNT}/all ${NEW_COUNT}/g" {} +
```

Then review the diff — percentage stats (68%, 95%, 22%, etc.) need manual recalculation.

**CRITICAL: Run the validation checklist** from CLASSIFICATION-RUBRIC.md after every DB change. The quick validation command checks that `jurisdiction` and `risk` fields are consistent — a mismatch will cause visible stat discrepancies on the live site.
