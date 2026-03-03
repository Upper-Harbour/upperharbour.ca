# Upper Harbour — Site Bible

**Internal reference document. Not published.**
Last updated: February 2026
Founder: Joshua van Es

---

## What Upper Harbour Is

Upper Harbour is a Canadian compliance intelligence firm. It maps the jurisdictional exposure of SaaS tools used by Canadian organizations — specifically, which tools are subject to the US CLOUD Act because their parent companies are US-incorporated, even when they offer Canadian data residency.

The core insight: **data residency ≠ data sovereignty.** A tool can store data in Canada while the parent company remains subject to US legal process. Law 25 (Quebec) already requires organizations to document this. PIPEDA reform (the CPPA) would make it mandatory federally.

Upper Harbour's research is public and free. The revenue model is compliance documentation — sovereignty audits, TIA packages, and jurisdictional risk reports — sold via scoping calls after organizations use the free HarbourScan tool.

---

## Product Architecture

### Free tier (acquisition)
- **Tools page** (`/tools`) — lookup any of 324 SaaS tools for jurisdiction, CLOUD Act status, parent company. Branded as the "Canadian Technology Sovereignty Index."
- **HarbourScan** (`/harbourscan`) — free browser-based assessment. User enters their tools, gets a jurisdictional map with CLOUD Act exposure, missing TIAs, DPA gaps. Takes ~10 minutes. Runs entirely client-side.
- **Signals** (`/signals`) — automated feed of sovereignty-relevant events: enforcement actions, acquisitions, legislation, vendor updates.
- **Research** (`/research`) and **Guides** (`/resources`) — public articles, templates, and analysis.

### Paid tier (revenue)
- **Sovereignty audits** — full documentation of an organization's SaaS jurisdictional exposure
- **TIA packages** — Transfer Impact Assessment documentation required by Law 25
- **Ongoing monitoring** — continuous jurisdictional monitoring of the organization's stack

Paid work is accessed via Calendly scoping calls: `https://calendly.com/josh-upperharbour/30min`

### Pipeline (the funnel)
```
Research/Guides (SEO) → Tools page (lookup) → HarbourScan (free assessment) → Scoping call (paid documentation)
```

Every page should support this flow. CTAs point toward HarbourScan (primary) or scoping calls (secondary).

---

## Site Map

```
/ (root)
├── index.html                  Homepage
├── harbourscan.html            HarbourScan landing page
├── tools.html                  Sovereignty Index / tool lookup
├── signals.html                Signals feed
├── research.html               Research hub
├── resources.html              Guides hub
├── founder.html                Joshua van Es bio
├── law25.html                  Law 25 landing page (standalone, own nav)
├── sovereignty.html            Sovereignty landing page (standalone, own nav)
├── admin-alerts.html           Pipeline admin (auth-protected)
├── apply_db_updates.py         Pipeline: applies approved alerts to saas-db.js
├── saas-db.js                  The database — 715 tools (loaded by every page via <script src="/saas-db.js">)
├── CLASSIFICATION-RUBRIC.md    Internal: classification logic
├── SITE-BIBLE.md               Internal: this document
│
├── /assets/
│   ├── uh-stats.js             Client-side dynamic stats (computes from saas-db.js, populates uh-stat spans)
│   ├── schema-stats-ref.json   Tracks current schema values for update-schema-stats.py
│   └── site.css                Global stylesheet
│
├── /research/
│   ├── government-saas-audit.html
│   ├── model-tia-template.html
│   ├── modele-efvp-loi-25.html          (French)
│   ├── provincial-exposure-index.html
│   ├── sovereignty-acquisition-tracker.html
│   └── sovereignty-policy-scorecard.html
│
├── /resources/
│   ├── canadian-technology-sovereignty-index.html
│   ├── canadian-data-residency-saas.html
│   ├── cloud-act-canadian-data.html
│   ├── data-residency-vs-data-sovereignty-canada.html
│   ├── data-sovereignty-government-procurement.html
│   ├── law-25-saas-compliance.html
│   ├── pipeda-vs-law-25.html
│   └── transfer-impact-assessments-law-25.html
│
└── /.github/workflows/
    └── approve-db-update.yml    GitHub Actions: auto-apply approved DB updates
```

---

## Navigation

### Standard nav (all main pages)
```
Signals | Tools | Research | Guides | [Run HarbourScan] (teal button)
```

Logo links to `/`. All links use clean URLs (no `.html` extension).

### Standalone landing pages
`law25.html` and `sovereignty.html` have their own nav: logo + sub-label + single CTA ("Request Free Pilot Assessment"). These are isolated funnels — they don't link to the main site nav. They include pilot signup forms (Formspree).

### Footer (standard)
```
Research column:          Resources column:
- Sovereignty Index       - HarbourScan
- Policy Scorecard        - Tools
- Government SaaS Audit   - Guides
- Provincial Exposure     - Signals
```
Footer includes founder credit linking to `/founder`.

---

## Design System

### Status (February 2026)
The site is in transition between two design systems. New/rebuilt pages use the current system. Older article pages use the legacy system. Both are dark theme.

### Current design system (tools.html, harbourscan.html, admin-alerts.html, research hub pages)
```css
--bg: #06090E
--surface: #0C1219
--surface-2: #111A24
--surface-3: #162030
--teal: #3CB8B0        /* primary accent, CTAs, links */
--gold: #C9A84C        /* emphasis, italic headings */
--red: #E06050         /* danger, CLOUD Act exposure */
--ice: #EAF0F4         /* primary text */
--slate: #8A9DB0       /* secondary text */
--muted: #566778       /* tertiary text, labels */

Fonts:
--display: 'Newsreader', Georgia, serif      /* headings, editorial feel */
--body: 'DM Sans', sans-serif               /* body text */
--mono: 'JetBrains Mono', monospace         /* labels, data, eyebrows */
```

### Legacy design system (index.html, most article pages, signals.html)
```css
--midnight: #0A1018
--navy: #0F1C2E
--surface: #131E2D
(same teal, gold, red, ice, slate, muted values)

Fonts:
--serif: 'Playfair Display', Georgia, serif
--font: 'Inter', sans-serif
--mono: 'JetBrains Mono', monospace
```

### Migration plan
When touching any page, migrate it to the current system if practical. The homepage (`index.html`) still uses the legacy system — it was not migrated in the February 2026 update because the structural changes (nav, flow section, footer) were prioritized over the visual refresh. Migrating the homepage to Newsreader/DM Sans is a recommended future task.

### Component patterns
- **Eyebrows**: `font-family: var(--mono); font-size: 10px; font-weight: 600; letter-spacing: 0.2em; text-transform: uppercase; color: var(--teal)`
- **Section titles**: `font-family: var(--display); font-weight: 700; color: var(--ice)` with `em { font-style: italic; color: var(--gold) }`
- **Risk badges**: red for exposed, gold for review, teal for canadian. Consistent across tools page, harbourscan, homepage checker.
- **CTAs**: Primary = teal bg, dark text. Secondary = gold bg, dark text. Ghost = text-only with border-bottom.
- **Cards/surfaces**: Use `var(--surface)` bg with `var(--border-md)` borders. Subtle, no drop shadows.

### Responsive
- Breakpoint at 768px: collapse grid layouts, hide nav links (keep logo + CTA)
- Breakpoint at 480px: further simplification
- All pages use 52px horizontal padding on desktop, 20px on mobile

---

## The Database: saas-db.js

### Structure
`/saas-db.js` defines a global `saasDB` array. Each entry:
```javascript
{
  name: "Slack",
  parent: "Salesforce Inc.",
  hq: "San Francisco, CA",
  jurisdiction: "United States",
  cloudAct: true,
  dataResidency: "US/CA/EU/AU/JP",
  note: "Canadian-founded but US-incorporated since pre-IPO. Acquired by Salesforce (US) in 2021.",
  risk: "exposed"    // "exposed" | "review" | "canadian"
}
```

### Classification logic
See `CLASSIFICATION-RUBRIC.md` for the full decision tree, edge cases, and precedents. Summary:
- **exposed**: US-parented, CLOUD Act applies, no meaningful Canadian data residency
- **review**: jurisdictional exposure exists but requires case-by-case assessment (usually because Canadian data residency is available, or the corporate structure is complex)
- **canadian**: not CLOUD Act exposed (Canadian-incorporated, or non-US/non-Canadian jurisdiction without CLOUD Act equivalent)

### Current counts (as of March 2026)
- 715 tools total across 32 categories
- All numbers auto-computed from saas-db.js — do not hardcode

### Pages that load saas-db.js
Every page with dynamic stats loads `saas-db.js` (repo root) and `assets/uh-stats.js`. Currently 16 pages:
- `index.html` (homepage counters + inline 20-tool sample checker)
- `tools.html` (full search/filter — also has own inline JS reading saasDB)
- `research.html` (category breakdown — also has own inline JS reading saasDB)
- `research/canadian-technology-sovereignty-index.html` (charts/tables — also has own inline JS)
- `research/sovereignty-policy-scorecard.html`
- `research/government-saas-audit.html`
- `research/athena-collective-law-25-compliance.html`
- `research/sovereignty-acquisition-tracker.html`
- `harbourscan.html` (scan logic)
- `resources/canadian-data-residency-saas.html`
- `resources/law-25-saas-compliance.html`
- `resources/transfer-impact-assessments-law-25.html`
- `resources/data-sovereignty-compliance-2026.html`
- `resources/saas-inventory-compliance.html`
- `resources/foreign-jurisdiction-saas-action-guide.html`
- `terms.html`

### Dynamic stats system
1. **Client-side (automatic):** `assets/uh-stats.js` computes stats from `saasDB` and populates any `<span class="uh-stat" data-stat="statName">` element. Hardcoded values in HTML are fallbacks for crawlers only.
2. **Build-time (run manually):** `python3 update-schema-stats.py` updates JSON-LD schema blocks and meta tags for SEO. Uses `assets/schema-stats-ref.json` to track what numbers to find/replace.

---

## The Pipeline

### Overview
The signals pipeline monitors for sovereignty-relevant events and can trigger database updates.

### Data flow
```
External monitoring (manual or automated)
    ↓
signals.json ← new signals added (enforcement, acquisition, legislation, vendor, procurement, policy)
    ↓
signals.html ← renders signals feed automatically
    ↓
db-alerts.json ← when a signal implies a database change, an alert is created
    ↓
admin-alerts.html ← Joshua reviews and approves/dismisses alerts (auth-protected)
    ↓
apply_db_updates.py ← processes approved alerts, modifies saas-db.js
    ↓
approve-db-update.yml ← GitHub Actions workflow commits and pushes changes
```

### Key files
- **signals.json** (`/assets/signals.json`): array of signal objects with `id`, `date`, `type`, `title`, `summary`, `source`, `sourceUrl`, `impact`, `tools` (affected tool names)
- **db-alerts.json** (root): array of alert objects with `id`, `signalId`, `tool`, `field`, `oldValue`, `newValue`, `status` ("pending"/"approved"/"dismissed"), `reason`
- **apply_db_updates.py** (root): Python script that reads db-alerts.json, parses saas-db.js with Node.js, applies approved changes, writes back. Run with `--apply --commit`.
- **approve-db-update.yml** (`.github/workflows/`): triggers on db-alerts.json changes, runs apply_db_updates.py, commits results.

### admin-alerts.html
Auth-protected page at `/admin-alerts`. Uses a simple password check (hardcoded, not production-grade). Shows pending alerts with approve/dismiss buttons. Writes changes back to db-alerts.json via GitHub API (requires PAT token).

---

## Key Decisions and Rationale

### "Engagements" is dead
The original site had an `/engagements` page and "Engagements" in the nav. This was replaced in February 2026. All references to "engagements" have been removed. The concept is now expressed as "documentation" or "compliance deliverables" — accessed via scoping calls, not a dedicated page. The homepage flow section step 03 is labeled "Documentation" with title "We produce the deliverables."

**If you see any remaining reference to "engagements" or `/engagements` anywhere on the site, it's a bug. Remove it.**

### Tools page UX: empty state on load
The tools page does NOT show all 324 rows on load. It shows: the hero stat (173 of 324 exposed), a risk meter, a search bar, and clickable chips for common tools. The full list only appears when the user searches or filters. This was a deliberate decision — 324 rows on load is overwhelming and kills conversion.

### Tools page: "Canadian Technology Sovereignty Index" branding
The eyebrow on the tools page says "Canadian Technology Sovereignty Index." This brands the dataset as a named, citable reference. The nav still says "Tools" because that's what people search for. The page teaches them it's an index once they arrive.

### Risk sorting: exposed first
When the tools list renders, it sorts by risk priority: exposed first, then review, then canadian. Within each tier, alphabetical. This is deliberate — the most alarming results appear first.

### Contextual CTAs on tool expansion
When you expand a tool's detail card, the CTA nudge is risk-specific:
- Exposed: "[Tool] is CLOUD Act exposed. US law enforcement can compel disclosure..."
- Review: "[Tool] requires jurisdictional review..."
- Canadian: "[Tool] is Canadian-headquartered. Jurisdiction today doesn't guarantee jurisdiction tomorrow."

All nudges link to HarbourScan with "Assess your stack →".

### Bottom CTA on tools page
"This page tells you the risk. HarbourScan produces the documentation." Followed by: "HarbourScan maps your entire SaaS environment using the same sovereignty dataset shown here — jurisdictions, CLOUD Act exposure, and data residency for every tool at once. Then it produces the documentation: sovereignty audit, TIA package, and jurisdictional risk report."

### Homepage primary CTA
HarbourScan is the primary CTA ("Run HarbourScan — free →"). Research is secondary. This was changed in February 2026 — previously "Explore the research" was primary.

### Homepage quick checker
The homepage embeds a 20-tool sample for instant lookups. "No match" results link to the full tools page (Sovereignty Index). This is intentional — the homepage checker is a teaser that drives traffic to the tools page.

### law25.html and sovereignty.html are standalone
These are isolated landing pages with their own navs and pilot signup forms. They were created before the main site architecture and operate as separate funnels. They do NOT use the standard nav. They reference a "Free Pilot Program" with Formspree forms. Whether these are still active is a business decision — check with Joshua.

### The Microsoft quote
The homepage and several articles cite Anton Carniaux (Microsoft France) from French Senate testimony, June 2025: "If a legally valid US CLOUD Act order is issued, Microsoft is obligated to comply — regardless of where the data is stored." This is the single most compelling proof point for the data residency ≠ data sovereignty argument. It should remain prominent.

---

## External Services

| Service | Purpose | URL/ID |
|---------|---------|--------|
| Formspree | Form submissions (CTA forms, pilot signups) | `https://formspree.io/f/mgolzdwe` |
| Calendly | Scoping calls | `https://calendly.com/josh-upperharbour/30min` |
| Cloudflare | Hosting, email protection, CDN | `upperharbour.ca` |
| GitHub | Repo, Actions pipeline | GitHub Pages or Cloudflare Pages deployment |
| LinkedIn | Joshua's profile | `https://www.linkedin.com/in/joshuavanes` |

---

## Content Tone

- **Authoritative but not academic.** The site presents compliance intelligence, not consulting jargon. Short sentences. Active voice.
- **The data speaks.** Lead with numbers (71%, 324, 95%, 22%). Let the statistics create urgency.
- **Never say "engagement."** Say "documentation," "deliverables," "compliance work," or "scoping call."
- **"Jurisdictional" is the differentiator.** Not just "compliance" — "jurisdictional compliance." This is what makes Upper Harbour different from generic privacy consultants.
- **CTAs are direct.** "Run HarbourScan — free →" not "Learn more about our assessment tool." "Request a scoping call" not "Contact us to discuss your needs."
- **French content exists.** `modele-efvp-loi-25.html` is a French-language TIA template. CTAs on French pages use "Demander un appel →" (not "Voir nos services").

---

## Press / Credibility

Joshua van Es and Upper Harbour research have been cited in:
- **Maclean's** (national newsmagazine)
- **BetaKit** (Canadian tech media)
- **OpenCanada** (foreign policy / international affairs)

Joshua's background includes: corporate law, policy research, SSHRC-funded Landscapes of Injustice project, chapter published by McGill-Queen's University Press.

---

## Known Issues and Technical Debt

1. **Design system split**: ~half the pages use Newsreader/DM Sans, ~half use Playfair/Inter. No functional impact but visual inconsistency. Migrate pages to the current system when touching them.

2. **Homepage still uses legacy design system**: The February 2026 update fixed content (nav, flow section, footer, CTAs) but kept the Playfair/Inter fonts. A full visual refresh of the homepage to match the tools/harbourscan pages would be a clean improvement.

3. **law25.html and sovereignty.html have isolated navs**: These don't link to Signals or Tools. They reference a "Free Pilot Program" that may or may not still be active. These pages also use `/founder.html` (with extension) instead of `/founder` (clean URL).

4. **www.upperharbour.ca vs upperharbour.ca**: Footer contact links use `www.`, canonical URLs don't. Should be normalized.

5. **admin-alerts.html auth**: Currently a simple password prompt. Not production-grade. Fine for a solo founder, not for a team.

6. **Pipeline not yet producing live signals**: The pipeline infrastructure (signals.json → db-alerts.json → admin approval → saas-db.js update) is built but needs external monitoring to feed it. First priority: connect a real monitoring source (Google Alerts, regulatory feeds, RSS).

7. **"Last reviewed" field not yet in saas-db.js**: Worth adding once the pipeline has produced real updates with varied dates. Not useful while all entries would show the same date.

---

## How to Continue This Site

If you're a future version of Claude (or a human developer) picking this up:

1. **Read this document first.** It tells you what exists, how it connects, and what decisions were made.
2. **Read CLASSIFICATION-RUBRIC.md** before touching the database. It defines the logic model.
3. **Use the current design system** (Newsreader/DM Sans/JetBrains Mono, `--bg: #06090E` color scheme) for any new pages or major rebuilds.
4. **Maintain the nav**: Signals | Tools | Research | Guides | [Run HarbourScan]. No exceptions for main pages.
5. **No "engagements."** Ever. Documentation, deliverables, scoping calls.
6. **Every page should drive toward HarbourScan** (free assessment) or a scoping call (paid work). That's the funnel.
7. **The tools page is the Sovereignty Index.** Treat it as the reference dataset, not just a lookup.
8. **Test the pipeline** if you're making changes to saas-db.js format — apply_db_updates.py parses the JS file with Node.js and needs the array structure to be consistent.
