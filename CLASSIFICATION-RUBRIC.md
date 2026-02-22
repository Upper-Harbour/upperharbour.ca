# Classification Rubric: Canadian SaaS Sovereignty Index

**Internal reference document — not published.**
Last updated: February 2026
Maintainer: Joshua van Es

---

## Purpose

This document defines the classification logic used in Upper Harbour's Canadian SaaS Sovereignty Index (the 292-tool database powering the Tools page, HarbourScan, and all published research). It exists so that:

- Classification decisions are consistent across all tools
- New tools and reclassifications follow a documented logic model
- Any team member can review, approve, or challenge a classification
- The dataset remains defensible if cited in procurement, regulatory, or media contexts

---

## Core Principle: Data Residency ≠ Data Sovereignty

The CLOUD Act grants US authorities the power to compel disclosure of data held by US-incorporated companies **regardless of where that data is stored**. A tool that offers "Canadian data residency" but is incorporated in the United States is still subject to US legal process. The availability of Canadian hosting is a compliance consideration — it does not eliminate jurisdictional risk.

This principle underpins the entire classification system.

---

## The Four Classifications

Every tool in the database receives exactly one of four risk classifications:

### EXPOSED (red badge)

**Definition:** The tool's parent entity is incorporated in the United States or is otherwise directly subject to the CLOUD Act, AND the tool does not offer meaningful Canadian data residency that would warrant additional nuance.

**Logic:** US-incorporated parent → CLOUD Act applies → Canadian data is subject to US legal process regardless of where it is stored → classification is **exposed**.

**Legal test:**
- Parent company incorporated in the US (including Delaware subsidiaries)
- `cloudAct: true`
- No meaningful Canadian data residency option available

**Typical profile:**
- Data residency is US-only, or Canadian residency is not available or not meaningful
- No structural ambiguity about jurisdiction

**Examples:** Slack (Salesforce), Notion, Asana, Dropbox, Figma, HubSpot, Zoom, GitHub (Microsoft)

**Why these aren't "review":** These tools are unambiguously under US jurisdiction with no Canadian data residency option that would create a meaningful compliance pathway. There is nothing to "review" — the exposure is clear.

---

### REVIEW (gold badge)

**Definition:** The tool has jurisdictional exposure that requires case-by-case assessment. This classification is used when:

1. **US-parented tools that offer Canadian data residency** — CLOUD Act still applies (data residency ≠ data sovereignty), but the availability of Canadian hosting creates a compliance consideration worth documenting in a TIA
2. **Dual-jurisdiction or complex corporate structures** — the tool has a split or ambiguous jurisdiction (e.g., Delaware-incorporated but Australian-headquartered)
3. **Jurisdictions with compelled disclosure laws equivalent to the CLOUD Act** — tools incorporated in countries with their own compelled disclosure frameworks:
   - **United Kingdom:** Investigatory Powers Act 2016 — authorities can compel disclosure of data held by UK-incorporated companies
   - **Australia:** Telecommunications and Other Legislation Amendment (Assistance and Access) Act 2018 — can compel data access from Australian-incorporated companies
4. **Non-US tools where data hosting creates indirect US exposure** — tools incorporated outside the US but hosting data primarily on US infrastructure (e.g., Israeli company using US-only cloud hosting)

**Critical note on US-parented tools with Canadian residency:** These tools are CLOUD Act exposed. The Canadian data residency option does **not** eliminate the risk. The "review" classification means the organization must make a documented decision (via TIA) about whether the residency option provides an acceptable risk posture for their use case. It does **not** mean the tool is safe.

**Legal test for "review":**
- US-incorporated parent with `cloudAct: true` AND meaningful Canadian data residency available, OR
- Parent incorporated in a jurisdiction with compelled disclosure laws (UK IPA, AU AA Act), OR
- Complex corporate structure creating dual jurisdiction exposure, OR
- Non-US parent but data hosted primarily on US infrastructure

**Examples:**
- **US + CA residency:** Microsoft 365, AWS, Azure, Google Workspace, Salesforce, DocuSign, Snowflake
- **UK (IPA):** Sage, Finastra, Wise, Dext, LexisNexis (RELX)
- **Australia (AA Act):** Canva, Moodle, Cliniko, LEAP, Maptek Vulcan
- **Dual jurisdiction:** Atlassian/Jira (Delaware + Australia), Ceridian/Dayforce (Canada + US)
- **Indirect US exposure:** Monday.com (Israel, US hosting), Wix (Israel, US hosting)

**The key distinction from "exposed":** These tools require a documented decision. An organization might be able to configure them in a way that reduces (but does not eliminate) jurisdictional risk. That decision needs to be documented in a TIA.

**The key distinction from "non_exposed":** These tools have a known legal pathway for compelled data disclosure — either via the CLOUD Act, the UK IPA, the AU AA Act, or indirect US infrastructure exposure.

---

### NON-EXPOSED (blue badge)

**Definition:** The tool's parent entity is incorporated outside the United States, the United Kingdom, and Australia, in a jurisdiction that does not have a known compelled disclosure law equivalent to the CLOUD Act. The tool is not CLOUD Act exposed and is not subject to equivalent foreign compelled disclosure mechanisms.

**Legal test — ALL three must be true:**
1. **Not incorporated in the US** (including no Delaware subsidiaries or US-incorporated parent in the corporate chain)
2. **Not a subsidiary of a US-incorporated parent**
3. **No equivalent compelled disclosure law** in their home jurisdiction (excludes UK and Australia)

**Additional considerations:**
- Data should not be hosted primarily on US infrastructure (if so, classify as REVIEW)
- The tool may still be subject to the data protection laws of its home jurisdiction (e.g., EU GDPR)
- Foreign ownership can change — monitor for acquisition by US, UK, or AU entities

**Typical profile:**
- `cloudAct: false`
- Parent incorporated in EU, Switzerland, New Zealand, India, Israel (without US hosting), or other non-compelled-disclosure jurisdiction
- No US parent company in the corporate chain
- Data not hosted primarily on US infrastructure

**Examples:**
- **EU:** SAP (Germany), Brevo (France), Sketch (Netherlands), Typeform (Spain), Make (Czech Republic), Hotjar (Malta), Adyen (Netherlands), Bluebeam (Germany/Nemetschek), CCH iFirm (Netherlands/Wolters Kluwer), GEOVIA (France/Dassault), Odoo (Belgium)
- **Switzerland:** Temenos
- **New Zealand:** Xero
- **India:** Zoho
- **Sweden:** Hexagon Mining
- **Italy:** Evernote (Bending Spoons)

**Why these aren't "canadian":** These tools are not Canadian-incorporated. While they are not CLOUD Act exposed, they operate under the legal frameworks of their home jurisdictions. For Canadian organizations specifically seeking Canadian-incorporated tools (e.g., for government procurement requiring Canadian jurisdiction), these do not qualify.

**Why these aren't "review":** There is no known compelled disclosure pathway. The parent entity is not subject to the CLOUD Act, the UK IPA, or the AU AA Act. There is no case-by-case jurisdictional decision to make — the tool is not exposed to these mechanisms.

---

### CANADIAN (teal badge)

**Definition:** The tool's parent entity is incorporated in Canada. Not subject to the US CLOUD Act.

**Legal test:**
- Parent company incorporated in Canada
- `cloudAct: false`
- No US parent company in the corporate chain that would create CLOUD Act exposure

**Typical profile:**
- Canadian-headquartered and Canadian-incorporated
- Canadian data residency available or standard

**Examples:** Clio, Shopify, FreshBooks, Hootsuite, Wealthsimple, Jane App, D2L Brightspace, Lightspeed, 1Password, Cohere, OpenText, Thomson Reuters

**Why this is the highest-trust tier:** Canadian incorporation means the tool is subject to Canadian privacy law (PIPEDA, Law 25, provincial legislation) and Canadian courts. There is no foreign legal process pathway for compelled data disclosure. This does not mean the tool is risk-free — ownership can change, VC backing can shift control — but it means the tool currently provides the strongest jurisdictional alignment for Canadian organizations.

---

## Decision Tree

For any new tool being added to the database:

```
1. Is the parent entity incorporated in the United States?
   ├── YES → Is meaningful Canadian data residency available?
   │         ├── YES → REVIEW
   │         └── NO  → EXPOSED
   └── NO  → Is the parent entity incorporated in Canada?
             ├── YES → CANADIAN
             └── NO  → Is the parent entity in a jurisdiction with
                        compelled disclosure laws (UK IPA, AU AA Act)?
                        ├── YES → REVIEW
                        └── NO  → Is data hosted primarily on
                                  US infrastructure?
                                  ├── YES → REVIEW
                                  └── NO  → NON_EXPOSED
```

**"Meaningful Canadian data residency"** means the vendor offers a Canada-region deployment option that a customer can select, and the option is available on business/enterprise plans (not just government contracts). Marketing language about "data staying in Canada" without a specific Canadian region offering does not qualify.

**"Compelled disclosure law"** means a statute that grants the government of the tool's home jurisdiction the legal power to compel the company to disclose data held on behalf of customers, regardless of where that data is stored. Currently tracked: US CLOUD Act, UK Investigatory Powers Act 2016, Australia Assistance and Access Act 2018. Other jurisdictions should be added as new legislation emerges.

---

## Compelled Disclosure Jurisdictions

| Jurisdiction | Law | Effective | Notes |
|-------------|-----|-----------|-------|
| United States | CLOUD Act (Clarifying Lawful Overseas Use of Data Act) | 2018 | Applies to all US-incorporated companies. Can compel disclosure regardless of data location. |
| United Kingdom | Investigatory Powers Act 2016 | 2016 | Broad surveillance powers. Technical capability notices can compel assistance. |
| Australia | Assistance and Access Act 2018 | 2018 | Technical assistance requests/notices can compel cooperation. Applies to AU-incorporated companies. |

**Jurisdictions monitored but not currently classified as compelled disclosure:**
- **Five Eyes (NZ, Canada):** Intelligence sharing agreements create indirect exposure but not direct statutory compulsion equivalent to the CLOUD Act
- **EU:** GDPR provides strong data protection; no equivalent compelled disclosure mechanism for foreign data
- **India:** IT Act has government access provisions but not comparable to CLOUD Act extraterritorial reach
- **Israel:** No equivalent compelled disclosure law for foreign-held data
- **Switzerland:** Strong data protection tradition; no equivalent compelled disclosure mechanism

This list should be reviewed quarterly and when new legislation is enacted.

---

## Edge Cases and Precedents

### Canadian company with significant US VC backing
**Classification:** CANADIAN (with note)
**Reasoning:** VC investment does not change the legal jurisdiction of the corporate entity. The parent remains Canadian-incorporated. However, the note field should document the VC structure, because a future acquisition by a US entity is a foreseeable risk. The signals pipeline monitors for exactly this.
**Example:** A Canadian SaaS company with Series B from a US PE firm remains "canadian" but the note reads: "Canadian-headquartered. Significant US venture capital backing — monitor for ownership changes."

### Canadian company acquired by a US parent
**Classification:** EXPOSED or REVIEW (depending on residency)
**Reasoning:** Acquisition by a US parent changes the jurisdiction. The tool is reclassified immediately upon acquisition closing. If the US parent maintains Canadian data residency, classify as REVIEW. If not, EXPOSED.
**Example:** Slack was Canadian-founded but US-incorporated since pre-IPO, then acquired by Salesforce. Classification: EXPOSED.

### Canadian company acquired by a non-US, non-compelled-disclosure parent
**Classification:** NON_EXPOSED
**Reasoning:** The parent is not subject to the CLOUD Act or equivalent law. The tool retains its Canadian operations but is no longer Canadian-incorporated.
**Example:** TaxCycle (Canadian-developed, acquired by Xero of New Zealand). Classification: NON_EXPOSED.

### Dual-headquartered company (Canada/US)
**Classification:** REVIEW
**Reasoning:** If the entity has any US incorporation that could subject it to CLOUD Act jurisdiction, it cannot be classified as CANADIAN. But the Canadian presence and operations create nuance worth documenting.
**Example:** Ceridian/Dayforce (Toronto/Minneapolis, US incorporation creates CLOUD Act exposure).

### EU/NZ/Swiss company with no US nexus
**Classification:** NON_EXPOSED
**Reasoning:** Not subject to CLOUD Act. Not subject to UK IPA or AU AA Act. No known compelled disclosure mechanism in home jurisdiction.
**Examples:** SAP (Germany), Xero (New Zealand), Temenos (Switzerland), Adyen (Netherlands)

### Australian company with no US nexus
**Classification:** REVIEW
**Reasoning:** Australia's Assistance and Access Act 2018 creates compelled disclosure exposure similar (though not identical) to the CLOUD Act.
**Examples:** Canva, Moodle, Cliniko, LEAP, Maptek Vulcan

### UK company with no US nexus
**Classification:** REVIEW
**Reasoning:** The UK Investigatory Powers Act 2016 creates compelled disclosure exposure.
**Examples:** Sage, Finastra, Wise, Dext

### Non-US company with data hosted primarily on US infrastructure
**Classification:** REVIEW
**Reasoning:** Even without a US parent, routing data through US infrastructure creates indirect jurisdictional exposure. US authorities could potentially access data through the infrastructure provider (which IS US-incorporated and CLOUD Act subject).
**Examples:** Monday.com (Israel, US-hosted), Wix (Israel, US-hosted)

### Tool changes infrastructure but not corporate parent
**Classification:** May change if infrastructure move creates or eliminates US hosting dependency
**Reasoning:** For non_exposed tools, a move to primarily US infrastructure would trigger reclassification to REVIEW. For review tools hosted on US infrastructure, a move to non-US infrastructure might enable reclassification to NON_EXPOSED (if all other criteria are met).

### Tool parent is acquired by another company in the same jurisdiction
**Classification:** Unchanged
**Reasoning:** Intra-jurisdictional acquisitions don't change compelled disclosure exposure. Update the parent company name and note, but keep the classification.

---

## Fields and Definitions

Each tool in the database has the following fields:

| Field | Definition |
|-------|-----------|
| `name` | Product name as commonly used by Canadian organizations |
| `parent` | Legal parent entity (the incorporated company, not the brand) |
| `hq` | Headquarters city and jurisdiction |
| `jurisdiction` | Country/countries of incorporation that determine legal authority |
| `cloudAct` | Boolean: is the parent entity subject to US CLOUD Act jurisdiction? |
| `dataResidency` | Available data residency regions (as offered to business customers) |
| `note` | Free-text explanation of classification reasoning |
| `risk` | Classification: `exposed`, `review`, `non_exposed`, or `canadian` |
| `category` | Functional category (e.g., "communication", "crm", "healthcare") |
| `industries` | Array of industries that commonly use this tool |

### cloudAct field logic

- `true` if the parent entity is incorporated in the United States, regardless of where data is stored
- `true` if the parent entity is a subsidiary of a US-incorporated company
- `false` if the parent entity is not incorporated in or controlled by a US entity
- For dual-jurisdiction entities, `true` if any entity in the corporate chain is US-incorporated

### risk field logic

| Value | cloudAct | Jurisdiction | Canadian residency | Compelled disclosure |
|-------|----------|-------------|-------------------|---------------------|
| `exposed` | `true` | US | No | CLOUD Act |
| `review` | `true` or `false` | US + CA residency, UK, AU, dual, or US-hosted | Varies | CLOUD Act, IPA, AA Act, or indirect |
| `non_exposed` | `false` | EU, NZ, CH, IN, IL, etc. | N/A | None known |
| `canadian` | `false` | Canada | Typically yes | None (Canadian law applies) |

### category field values

```
communication, productivity, project_management, file_storage, crm, 
marketing, cloud_infrastructure, devops, design, finance, hr, 
customer_support, security, analytics, integration, ai, healthcare, 
legal, education, ecommerce, enterprise_it, erp, mining, real_estate, 
hospitality, accounting, survey, cms, government, other
```

### industries field values

```
technology, finance, government, healthcare, legal, education, 
real_estate, accounting, mining, hospitality, nonprofit
```

These align with the `industryProfiles` in `regulatory-map.js`.

### note field standards

Every note should contain:
1. The jurisdictional fact (e.g., "US-incorporated" or "Canadian-headquartered")
2. The data residency situation (e.g., "Canadian data residency available" or "US only")
3. The compelled disclosure implication (e.g., "CLOUD Act applies" or "Not subject to US CLOUD Act or equivalent compelled disclosure law")
4. Any structural nuance (e.g., "Dual-headquartered" or "Acquired by [parent] in [year]")

---

## Reclassification Triggers

A tool should be reviewed for potential reclassification when:

1. **Acquisition or merger** — new parent entity may change jurisdiction and compelled disclosure exposure
2. **Reincorporation** — company moves legal domicile (rare but significant)
3. **New data residency offering** — US tool adds Canadian region (could move from EXPOSED to REVIEW)
4. **Data residency removal** — tool eliminates Canadian region option (could move from REVIEW to EXPOSED)
5. **Regulatory change** — new compelled disclosure law enacted in a jurisdiction (could move tools from NON_EXPOSED to REVIEW)
6. **Infrastructure migration** — significant change in where data is hosted (could move NON_EXPOSED to REVIEW or vice versa)
7. **New compelled disclosure law** — a jurisdiction previously classified as safe enacts equivalent legislation

The signals pipeline monitors for triggers 1, 2, 3, and 7 automatically. Triggers 4, 5, and 6 require manual review.

---

## Current Database Statistics (February 2026)

| Classification | Count | Percentage |
|---------------|-------|------------|
| EXPOSED | 160 | 55% |
| REVIEW | 52 | 18% |
| NON_EXPOSED | 18 | 6% |
| CANADIAN | 62 | 21% |
| **Total** | **292** | **100%** |

---

## Version History

| Date | Change | Reason |
|------|--------|--------|
| Feb 2026 | Initial rubric created | Codify classification logic used since database creation |
| Feb 2026 | Four-tier system implemented | Split "review" and "canadian" tiers to distinguish non-US/non-compelled-disclosure tools from Canadian-incorporated tools. Added compelled disclosure law tracking for UK (IPA) and Australia (AA Act). Added `category` and `industries` fields. |

---

## Review Schedule

This rubric should be reviewed:
- When a classification decision is ambiguous or contested
- When a new compelled disclosure law is enacted in any jurisdiction
- Quarterly, as part of database maintenance
- When the database exceeds 350 tools (may need to add subcategories)
