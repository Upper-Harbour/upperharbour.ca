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

## The Three Classifications

Every tool in the database receives exactly one of three risk classifications:

### EXPOSED (red)

**Definition:** The tool's parent entity is incorporated in the United States or is otherwise directly subject to the CLOUD Act, AND the tool does not offer meaningful Canadian data residency that would warrant additional nuance.

**Logic:** US-incorporated parent → CLOUD Act applies → Canadian data is subject to US legal process regardless of where it is stored → classification is **exposed**.

**Typical profile:**
- Parent company incorporated in the US
- `cloudAct: true`
- Data residency is US-only, or Canadian residency is not available or not meaningful
- No structural ambiguity about jurisdiction

**Examples:** Slack (Salesforce), Notion, Asana, Dropbox, Figma, HubSpot, Zoom (without CA residency option), GitHub (Microsoft)

**Why these aren't "review":** These tools are unambiguously under US jurisdiction with no Canadian data residency option that would create a meaningful compliance pathway. There is nothing to "review" — the exposure is clear.

---

### REVIEW (gold)

**Definition:** The tool has jurisdictional exposure that requires analysis, but the situation is not as straightforward as a simple US-incorporated/no-residency tool. This includes:

1. **US-parented tools that offer Canadian data residency** — CLOUD Act still applies, but the availability of Canadian hosting creates a compliance consideration worth documenting (e.g., Microsoft 365, AWS, Salesforce via Hyperforce)
2. **Dual-jurisdiction or complex corporate structures** — the tool has a split or ambiguous jurisdiction (e.g., Atlassian/Jira: incorporated in Delaware but headquartered in Australia; Ceridian/Dayforce: dual-headquartered Canada/US)
3. **Non-US, non-Canadian foreign jurisdiction** — tools incorporated in countries that are not subject to the CLOUD Act but are also not Canadian, where the regulatory environment may still create exposure (e.g., Canva in Australia, Monday.com in Israel)
4. **US-parented tools where the data type or processing model introduces nuance** — e.g., infrastructure providers like AWS/Azure where the customer has more architectural control over data placement

**Logic:** There is real jurisdictional exposure, but a blanket "exposed" label would be reductive. The tool requires case-by-case assessment depending on how the organization uses it, what data it processes, and whether available residency options are configured.

**Typical profile:**
- `cloudAct: true` (for US-parented with CA residency) OR `cloudAct: false` (for non-US/non-Canadian)
- Canadian data residency available or partially available
- Corporate structure is complex, split, or recently changed
- Data processing model gives the customer some control

**Examples:** Microsoft 365, Microsoft Teams, AWS, Azure, Google Workspace, Salesforce, DocuSign, Workday, Jira (Atlassian), Canva, Monday.com, QuickBooks, ADP, Ceridian/Dayforce

**The key distinction from "exposed":** These tools require a decision. An organization might be able to configure them in a way that reduces (but does not eliminate) jurisdictional risk. That decision needs to be documented — which is exactly what a TIA is for.

---

### CANADIAN (teal)

**Definition:** The tool's parent entity is headquartered in Canada with Canadian incorporation, OR the tool is headquartered in a jurisdiction that is not subject to the CLOUD Act and does not create comparable foreign legal process exposure for Canadian data.

**Logic:** The parent entity is not subject to US legal compulsion over Canadian data. This does not mean the tool is risk-free — ownership can change, VC backing can shift control, and non-Canadian jurisdictions have their own legal frameworks — but it means the tool is not currently CLOUD Act exposed.

**Typical profile:**
- `cloudAct: false`
- Parent company incorporated in Canada, or in a non-CLOUD Act jurisdiction (EU, NZ, AU without US nexus)
- No US parent company in the corporate chain that would create CLOUD Act exposure

**Examples:**
- **Canadian:** Clio, Shopify, FreshBooks, Hootsuite, Wealthsimple, Jane App, D2L Brightspace, Lightspeed, 1Password, Cohere
- **Non-Canadian, non-CLOUD Act:** SAP (Germany), Xero (New Zealand)

**Why SAP and Xero are "canadian" and not "review":** The "canadian" classification indicates the tool is not CLOUD Act exposed. SAP (German-incorporated) and Xero (NZ-incorporated) meet this test. The label could be more precisely called "not exposed" or "low jurisdictional risk," but "Canadian" was chosen because the primary audience is Canadian organizations looking for tools that don't create US legal process exposure. The label communicates the practical outcome: this tool does not expose your data to the CLOUD Act.

**Note on this naming decision:** If the index expands significantly beyond Canadian-headquartered tools in this tier, consider renaming the classification to "sovereign" or "low risk" to avoid confusion. For now, the label is accurate for the audience.

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
                        CLOUD Act-equivalent foreign legal process risk?
                        ├── YES or UNCLEAR → REVIEW
                        └── NO → CANADIAN
```

**"Meaningful Canadian data residency"** means the vendor offers a Canada-region deployment option that a customer can select, and the option is available on business/enterprise plans (not just government contracts). Marketing language about "data staying in Canada" without a specific Canadian region offering does not qualify.

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

### Dual-headquartered company (Canada/US)
**Classification:** REVIEW
**Reasoning:** If the entity has any US incorporation that could subject it to CLOUD Act jurisdiction, it cannot be classified as CANADIAN. But the Canadian presence and operations create nuance worth documenting.
**Example:** Ceridian/Dayforce (Toronto/Minneapolis, US incorporation creates CLOUD Act exposure).

### Australian or European company with no US nexus
**Classification:** CANADIAN
**Reasoning:** Not subject to CLOUD Act. May have its own regulatory framework, but for the purposes of Canadian jurisdictional compliance (the specific question this index answers), the tool does not expose Canadian data to US legal process.
**Examples:** Canva (Australia) is classified as REVIEW because its infrastructure runs on US cloud providers, creating indirect exposure. SAP (Germany) is classified as CANADIAN because it offers Canadian data residency on non-US infrastructure.

### Tool changes infrastructure but not corporate parent
**Classification:** Unchanged unless infrastructure change creates new jurisdictional exposure
**Reasoning:** The classification is primarily based on the parent entity's legal jurisdiction, not infrastructure. However, if a tool moves from self-hosted infrastructure to US cloud providers, the note should be updated. If the move creates a new CLOUD Act pathway (e.g., a Canadian company moves all processing to AWS US-East with no Canadian option), consider reclassification to REVIEW.

### Tool parent is acquired by another company in the same jurisdiction
**Classification:** Unchanged
**Reasoning:** Intra-jurisdictional acquisitions don't change CLOUD Act exposure. Update the parent company name and note, but keep the classification.
**Example:** If Salesforce acquires another US SaaS company, the acquired tool stays EXPOSED.

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
| `risk` | Classification: `exposed`, `review`, or `canadian` |

### cloudAct field logic

- `true` if the parent entity is incorporated in the United States, regardless of where data is stored
- `true` if the parent entity is a subsidiary of a US-incorporated company
- `false` if the parent entity is not incorporated in or controlled by a US entity
- For dual-jurisdiction entities, `true` if any entity in the corporate chain is US-incorporated

### note field standards

Every note should contain:
1. The jurisdictional fact (e.g., "US-incorporated" or "Canadian-headquartered")
2. The data residency situation (e.g., "Canadian data residency available" or "US only")
3. The CLOUD Act implication if applicable (e.g., "CLOUD Act applies regardless of data location")
4. Any structural nuance (e.g., "Dual-headquartered" or "Acquired by [parent] in [year]")

---

## Reclassification Triggers

A tool should be reviewed for potential reclassification when:

1. **Acquisition or merger** — new parent entity may change jurisdiction
2. **Reincorporation** — company moves legal domicile (rare but significant)
3. **New data residency offering** — US tool adds Canadian region (could move from EXPOSED to REVIEW)
4. **Data residency removal** — tool eliminates Canadian region option (could move from REVIEW to EXPOSED)
5. **Regulatory change** — new law creates CLOUD Act-equivalent exposure in another jurisdiction
6. **Infrastructure migration** — significant change in where data is processed

The signals pipeline monitors for triggers 1, 2, and 3 automatically. Triggers 4, 5, and 6 require manual review.

---

## Version History

| Date | Change | Reason |
|------|--------|--------|
| Feb 2026 | Initial rubric created | Codify classification logic used since database creation |

---

## Review Schedule

This rubric should be reviewed:
- When a classification decision is ambiguous or contested
- When a new jurisdiction category is considered (e.g., UK post-Brexit, India)
- Quarterly, as part of database maintenance
- When the database exceeds 350 tools (may need to add subcategories)
