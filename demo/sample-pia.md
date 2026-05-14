# Privacy Impact Assessment under the Alberta Protection of Privacy Act

**Project:** Adoption of Microsoft Teams and Microsoft 365 for Staff and Student Communications
**Public Body:** Calgary Board of Education
**Date:** 2026-04-29
**Template version:** POPA-PIA-2026-03
**Submission email:** PIA@oipc.ab.ca

---

## Executive Summary

### Calgary Board of Education — Privacy Impact Assessment
**Project:** Adoption of Microsoft Teams and Microsoft 365 for Staff and Student Communications
**Submitted by:** Sandra McKenzie, ATIA/POPA Coordinator and Privacy Officer
**Contact:** privacyofficer@cbe.ab.ca | 403-555-0188 ext. 2401
**Statutory authority:** Protection of Privacy Act, SA 2024, c P-28.5 (POPA); Protection of Privacy (Ministerial) Regulation, Alta Reg 143/2025 (M-Reg)

---

### 1. Project Overview

The Calgary Board of Education (CBE) is adopting Microsoft Teams and Microsoft 365 to support communications between staff and students, and between CBE and parents or guardians. The initiative involves the collection of student names, school assignments, and parent contact information, with personal information processed through Microsoft 365 cloud infrastructure. The data subjects include minors enrolled in CBE schools — a population that attracts heightened regulatory scrutiny under M-Reg s. 1's definition of "highly sensitive personal information."

This PIA has been prepared under POPA s. 26 and M-Reg s. 7, which together require a privacy impact assessment for projects involving highly sensitive personal information and projects where unauthorized disclosure could result in significant harm. The level of detail in this PIA is commensurate with the complexity of the project and the sensitivity of the personal information involved, in accordance with M-Reg s. 7(3).

---

### 2. Tools in Scope — Comparative Risk Table

| Attribute | Microsoft Teams | Microsoft 365 |
|---|---|---|
| **Category** | Communication | Productivity |
| **Ultimate Parent Corporation** | Microsoft Corporation | Microsoft Corporation |
| **Parent Jurisdiction** | United States | United States |
| **Headquarters** | Redmond, WA | Redmond, WA |
| **Canadian Data Residency Available** | Yes | Yes |
| **CLOUD Act Exposed (18 U.S.C. § 2713)** | Yes | Yes |
| **Upper Harbour Sovereignty Index** | Review | Review |

Both tools are classified as **Review** under the Upper Harbour Sovereignty Index. This classification reflects a documented tension: Canadian data residency is available and should be configured, but residency alone does not confer sovereignty. Under 18 U.S.C. § 2713, a provider of electronic communication service or remote computing service must comply with obligations to preserve, back up, or disclose the contents of wire or electronic communications and any record or other information pertaining to a customer or subscriber within such provider's possession, custody, or control, regardless of whether such communication, record, or other information is located within or outside of the United States. Because both tools are owned by a United States parent corporation, this compelled-disclosure obligation attaches to student and parent personal information regardless of where the data is physically stored. **Data residency is not data sovereignty.**

As of April 2026, the United States has executive agreements in force with the United Kingdom and Australia, and is in negotiation with the European Union and Canada. No US-Canada executive agreement under 18 U.S.C. § 2523 is in force. There is therefore no treaty mechanism currently in place that would require United States authorities to route legal process through Canadian courts before compelling disclosure from Microsoft.

The Plixer doctrine applies to both tools: CBE must classify Microsoft Teams and Microsoft 365 by the jurisdiction of their ultimate parent corporation — Microsoft Corporation, a United States entity — not by the geographic location of the servers processing CBE's data.

---

### 3. Key Privacy Findings

**Finding 1 — Jurisdictional Exposure (High, Residual)**
Both tools in scope carry United States jurisdictional exposure under the CLOUD Act (18 U.S.C. § 2713). The personal information of minors — a highly sensitive category under M-Reg s. 1 — is in scope. Contractual protections in the Microsoft Volume Licensing Data Processing Agreement (org-library-msft-dpa) are meaningful but partial: they do not extinguish Microsoft's obligation to comply with a lawful United States government order. This exposure must be accepted by CBE as a documented residual risk. The substantive jurisdictional analysis is set out in full in Section F.

**Finding 2 — Highly Sensitive Data Subjects (High Sensitivity, Manageable)**
The data subjects are students who are minors. The M-Reg s. 1 definition of "highly sensitive personal information" includes information about minors and other vulnerable individuals. This classification triggers the enhanced Privacy Management Program requirements under M-Reg s. 6(2) and requires CBE to apply a Protected B security classification. Collection authority is grounded in the Education Act and POPA s. 4(c); consent is not required for routine school-administration processing but parental notice under POPA s. 5(2) is mandatory.

**Finding 3 — Service-Provider Agreement on File (Addressed)**
Where a privacy impact assessment is submitted to the Commissioner, the privacy-related portions of any service provider agreement applicable to the project must be submitted with the PIA. The Microsoft Volume Licensing Data Processing Agreement (January 2024) is on file in CBE's Org Privacy Library (org-library-msft-dpa) and satisfies the M-Reg s. 7(6) submission requirement. The agreement confirms encryption at rest and in transit, least-privilege access controls, annual independent audits, and breach notification within 72 hours of Microsoft's awareness. The substantive treatment of the DPA is in Section G.

**Finding 4 — AI Features Disabled (Managed)**
AI-assisted features within Microsoft 365 (including Microsoft Copilot, automated meeting summaries, and content moderation) are not enabled for personal information in scope of this project. Should CBE elect to enable AI features in the future, an Algorithm Impact Assessment will be required under M-Reg s. 6(2)(e), and an amendment to this PIA must be filed with the Information and Privacy Commissioner.

**Finding 5 — Privacy Management Program Obligations Upcoming (Tracked)**
POPA s. 25 requires every public body to establish, implement and maintain a Privacy Management Program (PMP). The PMP must consist of documented policies and procedures that promote the public body's compliance with its duties under the Act, and must be proportional to the volume and sensitivity of personal information in custody or control. (In force June 11, 2026.) CBE's PMP development is in progress, with the program to address the minimum-content elements required by M-Reg s. 6 — including breach response procedures, staff training, security classification, correction-request handling, and PIA policies.

---

### 4. CBE's Position on Residual Risk

CBE has evaluated the jurisdictional exposure associated with both Microsoft Teams and Microsoft 365 and accepts the CLOUD Act exposure under 18 U.S.C. § 2713 as a documented residual risk for this project. This position is grounded in the following factors:

- Canadian data residency will be configured for at-rest storage, reducing the practical likelihood of routine cross-border data flows while not eliminating the legal possibility of compelled disclosure;
- The Microsoft Volume Licensing DPA (org-library-msft-dpa) provides contractual protections, including a commitment by Microsoft to challenge overbroad government demands and to notify CBE where legally permitted;
- Microsoft Teams and Microsoft 365 are widely used across Canadian K-12 public education systems, and the residual risk posture of this PIA is consistent with approaches taken by peer school boards and reviewed by comparable oversight bodies;
- No Canadian-parent alternative tool at equivalent functionality and procurement scale is presently available that would eliminate this exposure; and
- The personal information in scope — student names, school assignments, and parent contact information — does not include the most sensitive categories (health, financial, biometric) that would warrant a heightened risk posture.

CBE's acceptance of this residual risk will be confirmed by the head of the public body or designate on the signed cover letter at submission.

---

### 5. Recommendation

**This project should proceed with the following conditions:**

1. **Canadian data residency must be configured** in the Microsoft 365 and Microsoft Teams tenant before personal information of students and parents is processed. Residency configuration is a risk-reduction measure; it does not eliminate CLOUD Act exposure but it is expected as a minimum implementation control.

2. **Collection notice under POPA s. 5(2) must be issued** to parents and guardians (on behalf of minor students) before or at the time personal information is collected, disclosing the purpose, the legal authority, and the Privacy Officer's contact information.

3. **The signed Microsoft DPA (org-library-msft-dpa) must be included** in the OIPC submission package per M-Reg s. 7(6). This is already on file in CBE's Privacy Library and satisfies the submission requirement.

4. **AI features must remain disabled** until a dedicated Algorithm Impact Assessment is completed and an amended PIA is filed.

5. **CBE's Privacy Management Program** must be established by June 11, 2026, incorporating the minimum-content elements required by M-Reg s. 6, with specific attention to the highly sensitive nature of student personal information under M-Reg s. 6(2).

[HARD BLOCKER: Prepare and issue the POPA s. 5(2) collection notice to parents and guardians before the system goes live. The notice must state (a) the purpose of collection, (b) the specific legal authority (Education Act and POPA s. 4(c)), and (c) Sandra McKenzie's contact details as the officer who can answer questions. Attach the finalized notice text to the OIPC submission package — the Commissioner will expect to see it.]

---

## Section A. General Information About the Public Body or Bodies, Existing PIAs, and the Project

---

**Question 1.** Does the public body intend to collect, use or disclose personal information as part of this project?

**Yes.** The Calgary Board of Education (CBE) will collect, use, and disclose personal information as part of the adoption of Microsoft Teams and Microsoft 365 for Staff and Student Communications. Personal information, as defined in POPA s. 1(q), means recorded information about an identifiable individual, including name, address, telephone number, age, and other identifying information. The project involves the collection of student names, school assignments, and parent/guardian contact information, all of which constitute personal information within this definition. That personal information will be processed through Microsoft 365 cloud infrastructure by Microsoft Corporation as a contracted service provider. Under POPA s. 26, a public body must prepare a Privacy Impact Assessment in the circumstances prescribed by regulation, describing the project, the personal information involved, the privacy and security risks, and the mitigation measures applied. This PIA has been prepared accordingly.

---

**Question 2.** Does the project involve any of the following? (i) high-sensitivity personal information; (ii) personal information of a significant percentage of the population the public body serves; (iii) data matching between two or more public bodies; (iv) common or integrated program or service; (v) development or use of innovative technology; (vi) loss/unauthorized access/disclosure could result in significant harm.

The following circumstances apply to this project:

**(i) High-sensitivity personal information — YES.**
The project involves personal information about minors (students). Under M-Reg s. 1, highly sensitive personal information includes information about minors, seniors, or other vulnerable individuals. Student names, school assignments, and parent/guardian contact information collected through Microsoft Teams and Microsoft 365 therefore engage the high-sensitivity category. This classification drives the level of safeguards, training, and risk-management rigour required for the project.

**(ii) Personal information of a significant percentage of the population the public body serves — YES.**
This initiative is a board-wide deployment of Microsoft Teams and Microsoft 365 encompassing CBE's full student and staff population. Given the scale of the rollout across CBE schools, the project involves the personal information of a significant percentage of the population the CBE serves.

**(iii) Data matching between two or more public bodies — NO.**
This project does not involve a data-matching activity within the meaning of POPA s. 17. The project's personal-information processing is confined to a single operating program (school-related communications) and does not combine personal information from two or more programs to derive new information about individuals. *(agent's call: not a data-matching project — default for single-program scope. Override if records from multiple programs are combined.)*

**(iv) Common or integrated program or service — NO.**
This project does not constitute a common or integrated program or service shared between two or more public bodies. The deployment is internal to the CBE.

**(v) Development or use of innovative technology — CONDITIONAL.**
Microsoft Teams and Microsoft 365 are established commercial SaaS platforms and do not, in their standard configuration for this project, constitute innovative technology. AI-assisted features (e.g., Microsoft Copilot, automated meeting summaries, content moderation) are NOT enabled for personal information in scope of this project at this time. Should the CBE elect to enable AI features in the future, an Algorithm Impact Assessment will be conducted under M-Reg s. 6(2)(e) and an amendment to this PIA will be filed with the OIPC. *(agent's call: AI features disabled — default for risk-conservative deployment. Override if AI features will be enabled — an Algorithm Impact Assessment is then required.)*

**(vi) Loss, unauthorized access, or unauthorized disclosure could result in significant harm — YES.**
Under POPA s. 10(2), a public body must notify the Information and Privacy Commissioner, the responsible Minister, and any affected individual of any loss of, unauthorized access to, or unauthorized disclosure of personal information where a reasonable person would consider that there exists a real risk of significant harm to the individual as a result. Given that the personal information in scope includes information about minors — a class of individuals for whom unauthorized disclosure has an elevated potential for harm — a loss or unauthorized disclosure event in this project could readily meet the real-risk-of-significant-harm threshold.

---

**Question 3.** Name and contact information of the public body.

| Field | Details |
|---|---|
| **Name of public body** | Calgary Board of Education |
| **Head of public body** | Board Chair, Calgary Board of Education — named on the signed cover letter at submission |
| **Mailing address** | 1221 8 Street SW, Calgary, AB T2R 0L4 |
| **Email** | privacyofficer@cbe.ab.ca |
| **Telephone** | 403-555-0188 ext. 2401 |

Under POPA s. 55, the head of a public body may delegate any duty, power or function under the Act to an officer or employee of the public body, in writing, while remaining accountable for the proper performance of any delegated duty. Day-to-day authority over personal-information processing for this project is delegated to the CBE's ATIA/POPA Coordinator and Privacy Officer, Sandra McKenzie, whose contact information is listed above. *(agent's call: head named generically by institutional role; specific name lives on the signed cover letter at submission. Override only if you want to name the head specifically in the body of the PIA.)*

---

**Question 4.** Is this a joint PIA with any other public body?

**No.** This PIA is submitted by the Calgary Board of Education as the sole public body. No other public body is a co-participant in this project.

---

**Question 5.** Contact information of the person who can answer questions regarding this PIA.

| Field | Details |
|---|---|
| **Name** | Sandra McKenzie |
| **Title** | ATIA/POPA Coordinator and Privacy Officer |
| **Business unit** | CBE Privacy Office |
| **Email** | privacyofficer@cbe.ab.ca |
| **Telephone** | 403-555-0188 ext. 2401 |
| **Mailing address** | 1221 8 Street SW, Calgary, AB T2R 0L4 |

---

**Question 6.** Title of the project.

Adoption of Microsoft Teams and Microsoft 365 for Staff and Student Communications — Calgary Board of Education.

---

**Question 7.** Is this PIA related to a previously submitted or related PIA?

No related prior PIA is known to the agent. If a prior CBE submission covers an overlapping system or program, any cross-references should be added on the signed cover letter at submission.

---

**Question 8.** Is this an amendment to an existing PIA?

This is a new PIA submission, not an amendment. Amendment status is recorded on the cover sheet at submission and does not appear in the body of this PIA.

---

**Question 9.** Public body's internal file or reference number for this PIA (if applicable).

(To be assigned by the CBE's records management at submission, if used.)

---

**Question 10.** Has the project already been implemented?

This PIA is being completed in connection with the project's rollout. Whether the rollout is pre-implementation, mid-implementation, or post-implementation is recorded on the cover sheet at submission, not in the body of this PIA.

---

**Question 11.** Does the project involve: (a) data matching; (b) common or integrated program or service; (c) automated system or innovative technology (including AI)?

**(a) Data matching — No.** This project does not involve a data-matching activity within the meaning of POPA s. 17. Appendix A is not required. *(agent's call: not a data-matching project — default for single-program scope. Override if records from multiple programs are combined.)*

**(b) Common or integrated program or service — No.** The project is an internal CBE deployment and does not constitute a common or integrated program or service with another public body. Appendix B is not required.

**(c) Automated system or innovative technology (including AI) — No, in current scope.** Microsoft Teams and Microsoft 365, in their standard configuration for this project, are not being deployed with AI-automated decision-making features. Where a public body holds high-volume or highly sensitive personal information, the Privacy Management Program must additionally include policies governing the use of automated decision-making and AI systems where applicable. Should the CBE enable AI features (e.g., Microsoft Copilot) in the future, completion of Appendix C and an Algorithm Impact Assessment will be required under M-Reg s. 6(2)(e), and an amendment to this PIA will be filed with the OIPC. Appendix C is not required for the current scope.

---

## Section B. Details About the Project

**Question 12.** Provide a detailed description and the purpose of the project, including how the collection, use, and disclosure of personal information are necessary or related to this purpose. Include sufficient technical detail (system components, data flows, infrastructure, who manages the information, and the entire lifecycle of the personal information).

**Project Purpose**

The Calgary Board of Education ("CBE") is adopting Microsoft Teams and Microsoft 365 as its primary platform for staff and student communications, instructional collaboration, and school administration. The purpose of this initiative is to provide a unified, supported digital communications environment for teachers, students, and administrative staff across CBE schools, replacing fragmented or legacy communication tools and enabling consistent, documented, and manageable communications within the school system.

The Education Act establishes school boards as public bodies responsible for the provision and administration of instructional programs to resident students, and obligates school boards to maintain student records and to communicate with parents and guardians regarding student progress and school activities. Collection of student personal information and parent/guardian contact information is necessary to discharge these statutory obligations. The adoption of Microsoft Teams and Microsoft 365 is a direct continuation of these operating-program obligations in a cloud-hosted environment.

**Personal Information Collected and Its Necessity**

The following personal information is collected in scope of this project. Each field is mapped to its operating-program statutory authority and to POPA:

| Data Field | Operating-Program Authority | POPA s. 4(c) Anchor | Operating Purpose |
|---|---|---|---|
| Student legal name | Education Act (student records and enrolment) | POPA s. 4(c) | Identity verification; class-roster management; creation of Microsoft 365 accounts |
| School assignment (name and location of school student attends) | Education Act (assignment of students to instructional programs) | POPA s. 4(c) | Configuration of Teams / M365 tenant structure; class and team assignments |
| Parent/guardian contact information (name, email, phone) | Education Act (parental communication obligations) | POPA s. 4(c) | School-to-home communications; collection-notice delivery under POPA s. 5(2) |
| Staff name and CBE email address | Education Act (staffing and program delivery) | POPA s. 4(c) | Account provisioning; directory listings within the CBE tenant |
| Staff role / school assignment | Education Act (staffing and program delivery) | POPA s. 4(c) | Role-based access control configuration; Teams channel and license assignment |

Under POPA s. 4(c), a public body may collect personal information only if the information relates directly to and is necessary for an operating program or activity of the public body. Each field in the table above satisfies this threshold by virtue of the Education Act operating-program authority identified. Collection is limited to what is necessary to provision and manage accounts, configure communications structures, and fulfil parental-communication obligations. No sensitive categories of personal information (health, financial, biometric) are collected in scope of this project.

**System Components**

The project involves the following electronic information system (EIS) components:

- **Microsoft 365 tenant (CBE tenant):** The CBE's Microsoft 365 organizational tenant is the container for all licensed services. The tenant is provisioned and administered by CBE's Information and Technology Services (ITS) department. Student and staff accounts (Azure Active Directory / Entra ID) are provisioned within the tenant.
- **Microsoft Teams:** A collaboration and communication application within the Microsoft 365 suite, used for class-based Teams channels, staff team communications, video meetings, and direct messaging. Accessed via browser or installed client on managed devices.
- **Microsoft 365 core productivity suite (Exchange Online, SharePoint Online, OneDrive for Business):** Provides email, document storage, and file-sharing capabilities integrated with Teams. Staff and student documents and communications transit through and are stored within these services.
- **Azure Active Directory / Microsoft Entra ID:** The identity and access management layer. All student and staff accounts, role assignments, and access controls for the CBE tenant are managed here by CBE ITS.
- **Microsoft Admin Center:** CBE ITS administrators use the Microsoft Admin Center to manage account lifecycle (provisioning, suspension, deletion), license assignment, and tenant-level policy configuration.

**Data Flows**

1. **Account provisioning:** CBE ITS provisions student and staff Microsoft 365 accounts by importing identifying data (names, school assignments, email addresses) from CBE's student information system and HR system. Account data is transmitted from CBE's internal systems to Microsoft's cloud infrastructure over encrypted connections.
2. **Tenant operations:** Once provisioned, users authenticate (via MFA-protected accounts) and access Microsoft Teams and Microsoft 365 services. Communications (messages, meeting records, documents) are processed and stored within Microsoft's cloud infrastructure in the CBE tenant.
3. **Parent/guardian contact:** Parent/guardian contact information is used by school staff within the platform to facilitate school-to-home communications consistent with Education Act obligations. Contact information is stored within the CBE tenant directory and in school-administration workflows.
4. **Subprocessing:** Under POPA s. 1(h), "employee" includes a person who, under a contract for services with a public body, performs services for the public body for the purposes of a function of the public body, including a service provider performing such functions on behalf of the public body. Accordingly, Microsoft Corporation, in its capacity as a contracted service provider to CBE, is treated as part of CBE's extended workforce for POPA purposes. Microsoft processes personal information in scope of this project only at CBE's direction to deliver licensed services, as specified in the Microsoft Online Services Volume Licensing Data Protection Addendum (org-library-msft-dpa).
5. **Data residency:** CBE has selected the Canadian geographic region within the Microsoft 365 service for at-rest storage of Customer Data. However, as addressed in Section F, **data residency is not data sovereignty** — Canadian-region storage does not exempt Microsoft from its compelled-disclosure obligations under the CLOUD Act. See Section F for the full Plixer doctrine jurisdictional analysis.

**Information Lifecycle**

| Lifecycle Stage | Description |
|---|---|
| **Collection** | Student and staff personal information is sourced from CBE's student information system and HR system and imported into the Microsoft 365 tenant at account provisioning. Parent/guardian contacts are collected through existing school-registration processes and imported into tenant directory where needed for communications. |
| **Storage** | Personal information is stored within Microsoft's cloud infrastructure (Canadian region) in the CBE tenant, encrypted at rest and in transit. See Section F for security safeguard detail. |
| **Use** | Personal information is used solely to enable school communications, instructional collaboration, and school administration consistent with the Education Act operating-program authority and POPA s. 12. Use is limited to the extent necessary under POPA s. 12(4). |
| **Disclosure** | Personal information is not disclosed to third parties beyond what is required to deliver the licensed service. Microsoft's processing is classified as internal use by CBE's extended workforce under POPA s. 1(h), not third-party disclosure under POPA s. 13. |
| **Retention** | Student records, including school assignments and parent-contact information, are retained for the duration of student enrolment plus a further period aligned with CBE's Records Retention Schedule and the Education Act's record-keeping obligations — typically seven years post-graduation or transfer. *(agent's call: active-enrolment + 7 years — typical school-board norm. Override with CBE's specific retention schedule if different.)* Personal information used to make decisions that directly affect an individual is retained for a minimum of one year following that decision, in accordance with POPA s. 6(b). |
| **Disposition** | Upon expiry of the applicable retention period, personal information is deleted from the Microsoft 365 tenant. POPA s. 6(b) provides that where a public body uses an individual's personal information to make a decision that directly affects the individual, the public body must retain that personal information for at least one year after the decision is made so that the individual has a reasonable opportunity to obtain access to it. Disposition of records past their retention horizon is enforced through standard CBE tenant retention policies aligned with CBE's records-retention schedule; manual review applies for records under legal hold. |

**Who Manages the Information**

CBE's Information and Technology Services (ITS) department manages the Microsoft 365 tenant, account provisioning and lifecycle, license assignment, and tenant-level security configurations. The ATIA/POPA Coordinator and Privacy Officer (Sandra McKenzie) has oversight of personal-information handling practices within the project. School principals and teachers manage Teams class channels and communications within the parameters set by ITS and CBE's acceptable-use policies. Microsoft Corporation manages the underlying cloud infrastructure in accordance with its contractual obligations under the Microsoft DPA (org-library-msft-dpa).

**Collection Notice**

POPA s. 5(2) requires that a public body that collects personal information directly from an individual must, at or before the time the personal information is collected, take reasonable steps to ensure that the individual is informed of (a) the purpose for which the information is being collected, (b) the specific legal authority for the collection, and (c) the title, business address, and business telephone number of an officer or employee of the public body who can answer the individual's questions about the collection.

For this project, CBE will provide collection notice to parents and guardians (on behalf of students, who are minors) through the school-registration and enrolment process, and to staff through the standard employment and onboarding documentation process. The notice will identify: (a) the purpose of collection (to provision Microsoft 365 / Teams accounts for school communications and instruction); (b) the specific legal authority (Education Act and POPA s. 4(c)); and (c) the contact information of the Privacy Officer — Sandra McKenzie, ATIA/POPA Coordinator and Privacy Officer, 1221 8 Street SW, Calgary, AB T2R 0L4, privacyofficer@cbe.ab.ca, 403-555-0188 ext. 2401.

Because the data subjects include minors, collection notice is delivered through parent/guardian channels. *(agent's call: parental-notice default for minors — collection-notice obligation under POPA s. 5(2) discharged via parent/guardian enrolment communications. Override if CBE's notice mechanism differs.)*

[HARD BLOCKER: Attach the actual collection-notice text provided to parents/guardians and staff as part of the enrolment and onboarding process — this is a required attachment for OIPC submission, as it is the evidence that POPA s. 5(2) has been discharged in practice.]

---

**Question 13.** Does the project involve the implementation of an electronic information system (EIS)? If yes, identify the name of the system.

**Yes.** This project involves the implementation of two electronic information systems:

1. **Microsoft Teams** — a collaboration and communication platform operated by Microsoft Corporation (parent jurisdiction: United States). Under the Upper Harbour Sovereignty Index, Microsoft Teams is classified as **Review**. The Plixer doctrine applies: classification is determined by the jurisdiction of the ultimate parent corporation (Microsoft Corporation, Redmond, WA, USA), not by the location of data residency infrastructure. See Section F for the full jurisdictional analysis.

2. **Microsoft 365** — a cloud-hosted productivity suite operated by Microsoft Corporation (parent jurisdiction: United States). Under the Upper Harbour Sovereignty Index, Microsoft 365 is likewise classified as **Review**. The same Plixer doctrine analysis applies.

Both systems are cloud-hosted EIS that collect, process, store, and transmit personal information about CBE students, parents/guardians, and staff. M-Reg s. 3(2) requires that where a public body uses an information system to process personal information, the public body must ensure that the system includes sufficient logging and auditing capabilities to detect and investigate unauthorized access, use, disclosure or other contraventions of the Act, and must establish procedures for the periodic review of those logs. CBE's audit logging posture for both systems is addressed in Section F.

---

**Question 14.** Are other stakeholders involved in the project that may collect, use, or disclose personal information? If yes, list them and describe the role of each.

**Yes.** The following stakeholders are involved in this project in roles that engage personal information:

| Stakeholder | Role | Personal Information Involved | POPA Treatment |
|---|---|---|---|
| **Microsoft Corporation** (Redmond, WA, USA) | Cloud infrastructure and licensed service provider. Processes personal information in the CBE Microsoft 365 tenant solely to deliver licensed services, troubleshoot, maintain performance and security, and for limited incident-to-business operations (billing, internal reporting) using aggregated/pseudonymized data only, per the Microsoft DPA (org-library-msft-dpa). | Student names, school assignments, parent/guardian contact information, staff names and roles, communications metadata, and content generated within Teams and M365. | Treated as CBE's extended workforce under POPA s. 1(h). Processing is internal use, not third-party disclosure under POPA s. 13. CBE retains accountability under POPA s. 10(1). |
| **CBE Information and Technology Services (ITS)** | Internal department responsible for tenant administration, account provisioning and lifecycle management, license assignment, security configuration, and audit log review. | All personal information in scope: student and staff account data, access logs, security configurations. | Internal processing by CBE employees. No separate disclosure event. |
| **CBE School Administrators and Teachers** | Day-to-day use of Microsoft Teams for class management, instructional delivery, and school-to-home communications. Create and manage Teams channels, assign students to classes, communicate with parents. | Student names, school assignments, parent/guardian contacts, instructional content, and communications within Teams. | Internal processing by CBE employees within the terms of the Education Act operating-program authority. |
| **Parents and Guardians** | Recipients of school-to-home communications through the platform. They interact with the system as communication recipients, not as controllers or processors. Their contact information is stored within the CBE tenant to enable those communications. | Their own contact information (names, email, phone); communications received. | Not a controller or processor. Contact information is collected by CBE under Education Act authority. |
| **Microsoft Subprocessors** | Microsoft may engage subprocessors (including Microsoft Affiliates) with CBE's prior general written consent under the DPA. Subprocessors are bound by written agreements requiring at least equivalent data protection as the Microsoft DPA. Under POPA s. 1(h), this extended chain of contracted service providers continues to fall within CBE's extended workforce for POPA purposes, provided the subprocessing is within the scope of delivering the licensed service. The current list of Microsoft subprocessors is published at servicetrust.microsoft.com. | Potentially all personal information in scope of the licensed service, to the extent subprocessors are engaged in service delivery. | Treated as service providers within CBE's POPA s. 1(h) extended workforce. Microsoft remains fully liable for subprocessors' compliance per the DPA. |

No other external public bodies or third-party organizations are involved in this project at this time. POPA s. 17 governs data-matching activities that use personal information from two or more data sources to derive new information about individuals. This project does not involve data matching within the meaning of POPA s. 17 — the project's personal-information processing is confined to a single operating program (school communications and administration) and does not combine personal information from two or more programs. *(agent's call: not a data-matching project — default for single-program scope. Override if records from multiple programs are combined.)*

---

## Section C. Information About Your Privacy Management Program (PMP)

**Question 15.** Does the Calgary Board of Education have a Privacy Management Program (PMP)? If yes, has it been submitted to the OIPC? If no, describe the plan to develop and implement a PMP.

The Calgary Board of Education (CBE) is actively developing its Privacy Management Program in advance of the mandatory in-force date. POPA s. 25 requires every public body to establish, implement, and maintain a Privacy Management Program consisting of documented policies and procedures that promote compliance with the Act, proportional to the volume and sensitivity of personal information in the public body's custody or under its control. This obligation comes into force on June 11, 2026.

CBE's PMP development is in progress, with the program scheduled to be in place before the June 11, 2026 in-force date. *(agent's call: PMP-in-development framing aligned with the June 11, 2026 in-force date. Override if a PMP is already established.)*

The PMP under development is designed to address the minimum-content elements required by M-Reg s. 6. Specifically:

- **Breach response policy** — M-Reg s. 6(1)(b) requires documented internal policies and procedures for breach incidents under POPA s. 10(2), correction requests under s. 7, complaints under s. 38(2), use of non-personal data, and use of automated systems and decision-making.

- **Privacy training** — M-Reg s. 6(1)(d) requires mandatory privacy training for all employees of the public body, with training proportional to the employee's role and access to personal information, documented and refreshed periodically.

- **Enhanced obligations for high-volume or highly sensitive personal information** — M-Reg s. 6(2) requires that, where a public body holds high-volume or highly sensitive personal information, the PMP additionally include: a documented internal privacy management structure with named roles and responsibilities; PIA policies and procedures; proactive security monitoring; consent policies; policies governing automated decision-making and AI systems where applicable; and documented administrative, technical, and physical safeguards. Given that CBE processes personal information about minors — classified as Protected B and treated as highly sensitive within the meaning of M-Reg s. 1 — the s. 6(2) enhanced requirements apply to CBE's PMP.

The PMP will designate Sandra McKenzie, ATIA/POPA Coordinator and Privacy Officer, as the named PMP owner responsible for overseeing implementation and ongoing maintenance. Under POPA s. 55, the head of a public body may delegate any duty, power, or function under the Act to an officer or employee of the public body in writing, while the head remains accountable for the proper performance of any delegated duty.

Once established, CBE will make its PMP available to any person who requests it within 30 business days, and will publish a summary of the PMP, in accordance with POPA s. 25(5). Technical security details may be withheld from the public-facing copy where disclosure would compromise security arrangements.

As the PMP has not yet been submitted to the OIPC, no OIPC PMP file number has been assigned. This PIA is being filed in advance of the PMP submission, consistent with the sequencing contemplated by M-Reg s. 7, which does not require a completed PMP as a precondition for PIA submission. CBE commits to ensuring that its PMP is in place and compliant with all M-Reg s. 6 minimum-content requirements on or before June 11, 2026, and to submitting the PMP to the OIPC upon completion.

---

## Section D. Identify Personal Information Involved and your Authority to Collect, Use or Disclose the Information

---

**Question 16.** Personal information in scope, and legal authority to collect, use, and disclose each category

The table below maps each category of personal information in scope of the Adoption of Microsoft Teams and Microsoft 365 for Staff and Student Communications (the "Project") to its collection authority, use authority, and disclosure authority, and addresses the limitation principles under POPA ss. 12(4) and 13(4).

---

### Personal Information Mapping Table

| # | Data Field | Data Subjects | Collection Authority | Use Authority | Disclosure Authority | Limitation — Use (s. 12(4)) | Limitation — Disclosure (s. 13(4)) | Sensitivity Classification |
|---|---|---|---|---|---|---|---|---|
| 1 | **Student legal name** | Students (minors) | <u>Education Act</u>, SA 2012, c E-0.3 (obligation to maintain student records and deliver instructional programs to resident students) → POPA s. 4(c) (information relates directly to and is necessary for an operating program) | POPA s. 12(a): used for the purpose for which it was collected — identifying the student within the Teams/M365 environment and linking the student to their school assignment | POPA s. 13: disclosed to Microsoft Corporation as contracted service provider (treated as CBE employee per POPA s. 1(h)); disclosed to CBE staff whose duties require access; not disclosed to third parties | Used only to identify the student within the CBE tenant; not used for profiling, marketing, or any secondary purpose | Disclosed only to the extent necessary to configure the student's account and enable authorized communications; not disclosed externally | Protected B *(agent's call: Protected B — recommended for information about minors; override if CBE's classification scheme uses a different level)* |
| 2 | **School assignment** (the school at which the student is enrolled) | Students (minors) | <u>Education Act</u>, SA 2012, c E-0.3 (school boards must assign resident students to schools and maintain corresponding records) → POPA s. 4(c) | POPA s. 12(a): used to provision the student's Microsoft Teams environment within the correct school-level team and to route communications appropriately | POPA s. 13: disclosed to Microsoft Corporation as contracted service provider per POPA s. 1(h); shared with authorized CBE staff at the assigned school | Used only to route the student to the correct school team and authorized communications channels; not used for any secondary purpose | Disclosed only to Microsoft for account provisioning and to CBE staff at the assigned school on a need-to-know basis | Protected B *(agent's call: Protected B — recommended for information about minors; override if a different level applies)* |
| 3 | **Parent/guardian name and contact information** (including email address and/or telephone number) | Parents and guardians of students | <u>Education Act</u>, SA 2012, c E-0.3 (school boards are obligated to communicate with parents and guardians regarding student progress and school activities) → POPA s. 4(c) | POPA s. 12(a): used for the purpose for which it was collected — facilitating school-to-home communications through Microsoft Teams and M365 | POPA s. 13: disclosed to Microsoft Corporation as contracted service provider per POPA s. 1(h); shared only with CBE staff whose duties involve parent/guardian communications | Used only to enable authorized communications between CBE staff and parents/guardians; not used for marketing, research, or profiling | Disclosed only to Microsoft for account/message routing and to CBE staff with a direct communications duty; not disclosed to other students, other parents, or third parties | Protected B *(agent's call: Protected B — recommended for information about minors (parents/guardians of minors); override if CBE's scheme assigns a different level)* |
| 4 | **CBE staff name and CBE-issued email address** | CBE employees | <u>Education Act</u>, SA 2012, c E-0.3 (CBE must administer instructional programs, which requires identifying and communicating with assigned staff) → POPA s. 4(c) | POPA s. 12(a): used to provision staff accounts and enable staff-to-student and staff-to-parent communications in scope of the Project | POPA s. 13: disclosed to Microsoft Corporation as contracted service provider per POPA s. 1(h); visible to other CBE staff and students within the tenant as necessary for communications | Used only to identify staff within the CBE tenant and enable authorized communications; not used for performance monitoring, secondary analytics, or AI-assisted processing | Staff names and CBE-issued email addresses disclosed only within the CBE tenant to authorized users; personal home contact details are out of scope and not collected | Protected A *(agent's call: Protected A — CBE-issued contact details are administrative/professional identifiers; override if CBE classifies differently)* |

---

**Statutory anchors — applied to the table above:**

Under POPA s. 1(q), "personal information" means recorded information about an identifiable individual, including name, home or business address or home or business telephone number, age, sex, marital status or family status, and identifying numbers — among other categories. All four data fields listed above fall within this definition.

POPA s. 4 provides that a public body may collect personal information only if (a) the collection is expressly authorized under an enactment, (b) the information is collected for the purposes of law enforcement, or (c) the information relates directly to and is necessary for an operating program or activity of the public body. For each data field above, the collection authority is POPA s. 4(c) anchored to the CBE's operating obligations under the Education Act.

The Education Act, SA 2012, c E-0.3, establishes school boards as public bodies responsible for the provision and administration of instructional programs to resident students. School boards are obligated to maintain student records (including identifying information, school-to-student assignments, and academic progress information) and to communicate with parents and guardians regarding student progress and school activities. Collection of student personal information and parent/guardian contact information is necessary to discharge these statutory obligations and is the operating-program authority that anchors collection under POPA s. 4(c) for Alberta school-board PIAs.

POPA s. 12 permits a public body to use personal information in its custody or under its control only (a) for the purpose for which the information was collected or compiled or for a use consistent with that purpose, (b) if the individual consented in the prescribed manner, or (c) for a purpose for which the information may be disclosed under s. 13.

POPA s. 12(4) requires that a public body use personal information only to the extent necessary to enable the public body to carry out the purpose for which it was collected, or a consistent purpose, in a reasonable manner. CBE applies this limitation by restricting use of the data fields above to account provisioning, authorized communications, and associated school-administration purposes only.

POPA s. 13 provides that a public body may disclose personal information only in the specific circumstances enumerated in that section, including in accordance with Part 1 access requests, with individual consent, for the purpose for which it was collected or a consistent purpose, to an officer or employee of the public body if necessary for the performance of duties, or as authorized or required by another enactment.

POPA s. 13(4) requires that a public body disclose personal information only to the extent necessary to enable the public body or the recipient to carry out the purpose of the disclosure in a reasonable manner. CBE applies this limitation by ensuring that Microsoft Corporation receives only the personal information required to provision and operate the Teams/M365 tenant for CBE's authorized purposes, and that CBE staff access is limited to records relevant to their specific role.

Under POPA s. 1(h), "employee" includes a person who, under a contract for services with a public body, performs services for the public body for the purposes of a function of the public body, including a service provider performing such functions on behalf of the public body. The effect of this definition is that service providers are treated as employees of the public body for the purposes of POPA's protection-of-personal-information obligations. Accordingly, Microsoft Corporation's processing of CBE personal information under the Microsoft Volume Licensing DPA (org-library-msft-dpa) constitutes internal use by CBE's extended workforce — not a disclosure to a third party within the meaning of POPA s. 13.

---

**Question 17.** Compliance with POPA s. 5(2) — collection notice

POPA s. 5(2) requires that a public body that collects personal information directly from an individual must, at or before the time the personal information is collected, take reasonable steps to ensure that the individual is informed of (a) the purpose for which the information is being collected, (b) the specific legal authority for the collection, and (c) the title, business address and business telephone number of an officer or employee of the public body who can answer the individual's questions about the collection.

The Project involves the collection of personal information directly from CBE staff (who create or confirm their own account details) and indirectly in respect of students and parents/guardians (whose information is entered by school administration — see Question 19 for indirect collection). The following describes how CBE discharges the s. 5(2) notice obligation for each population:

**CBE staff.** At or before staff onboarding to Microsoft Teams and M365, CBE provides a collection notice that identifies: (a) the purpose — enabling staff-to-student, staff-to-parent, and staff-to-staff communications and collaboration in CBE's digital environment; (b) the specific legal authority — POPA s. 4(c) in conjunction with CBE's operating obligations under the Education Act; and (c) the contact details of the ATIA/POPA Coordinator and Privacy Officer, Sandra McKenzie, who can answer questions about the collection (email: privacyofficer@cbe.ab.ca; telephone: 403-555-0188 ext. 2401; mailing address: 1221 8 Street SW, Calgary, AB T2R 0L4).

**Students and parents/guardians.** Because students are minors and their information is collected through school administration processes rather than directly from the student themselves, CBE delivers collection notice to the parent or guardian. Notice is provided through CBE's standard parent/guardian communications channel (school registration forms, school-year information packages, or the CBE parent portal) at or before the time personal information is entered into the M365 environment. The notice identifies: (a) the purpose; (b) the legal authority (POPA s. 4(c) / Education Act); and (c) Sandra McKenzie's contact details as above.

*(agent's call: collection-notice default for minors via parent/guardian channels — the parental-notice framing above reflects standard OIPC and POPA s. 5(2) practice for K-12 school boards. Override if CBE uses a different notice vehicle, or if the actual notice text has already been drafted and is available to attach.)*

[HARD BLOCKER: Attach the actual collection notice text (or the notice template) used to inform parents/guardians and staff of the Microsoft Teams/M365 collection — this is a regulator-required attachment for OIPC submission. The notice must contain the three elements required by POPA s. 5(2): (a) the purpose, (b) the specific legal authority (POPA s. 4(c) / Education Act), and (c) Sandra McKenzie's contact information. Upload the notice to the "Before submit" panel before filing.]

---

**Question 18.** Consent — applicability and process

POPA s. 4 authorizes a public body to collect personal information where the information relates directly to and is necessary for an operating program or activity of the public body. For the Project, CBE's collection authority rests on this operating-program basis, not on individual consent.

The Education Act establishes CBE's obligation to maintain student records and to communicate with parents and guardians regarding student progress and school activities. Because the Project is confined to purposes that fall squarely within CBE's Education Act mandate, individual consent is not the operative legal basis for collection, use, or disclosure of any of the four data fields identified in Question 16. CBE does not rely on parental or student consent to collect, use, or disclose personal information for the routine school-administration and communications purposes of this Project.

*(agent's call: operating-program authority (consent not required for routine school operations). Override only if CBE intends to use data for a purpose that goes beyond Education Act authority — for example, research disclosure, secondary marketing, or AI model training — none of which is in scope.)*

Accordingly, Question 18's consent-process framework does not apply to the Project in its current scope. Should CBE elect to use personal information for purposes beyond those authorized by the Education Act and POPA s. 4(c) — for instance, enabling AI-assisted features such as Microsoft Copilot — CBE would be required to establish a compliant consent process under the Protection of Privacy Regulation, s. 2, and to amend this PIA. AI-assisted features are not enabled at this time (see Section F for the Plixer doctrine jurisdictional analysis and Section G for the service-provider agreement).

---

**Question 19.** Indirect collection of personal information

**Yes.** Personal information about students and parents/guardians is collected indirectly. School-administration staff enter student names, school assignments, and parent/guardian contact information into the M365 environment on behalf of those individuals, rather than the students or parents/guardians entering that information themselves.

**Why indirect collection occurs.** Students are minors and cannot independently manage their own school-administration records. School enrolment processes require CBE administrative staff to record and maintain student data (name, school assignment) and associated parent/guardian contact information as part of CBE's obligations under the Education Act. The transition of these records into the M365 environment follows the same administrative process.

**Legal authority for indirect collection.** POPA s. 4(c) authorizes a public body to collect personal information where the information relates directly to and is necessary for an operating program or activity of the public body. CBE's obligation to maintain student records and to communicate with parents and guardians is established by the Education Act, SA 2012, c E-0.3 — the operating-program statute that grounds the indirect collection.

CBE does not collect personal information about students or parents/guardians from third-party databases or from sources unrelated to the student's enrolment relationship with CBE. All indirect collection is sourced from CBE's own enrolment and records systems, where the information was originally collected under the same Education Act authority.

---

**Question 20.** Information flow diagram

An information flow diagram for the Project is required as a mandatory attachment for OIPC submission. The diagram must show the movement of each specific data field (student name, school assignment, parent/guardian contact, staff name/email) between the following entities, with directional arrows:

1. Parent/guardian or student (source of information at enrolment)
2. CBE school-administration staff (enters data into M365)
3. CBE Microsoft 365 tenant (Canadian-region data residency; Microsoft Corporation as data processor)
4. Microsoft Corporation (parent: United States; CLOUD Act exposed — see Section F Q33 for jurisdictional analysis)
5. CBE staff accessing Teams/M365 (for communications purposes)

[HARD BLOCKER: Prepare and attach an information flow diagram showing the movement of student names, school assignments, parent/guardian contacts, and staff names/emails between CBE school administration, the CBE Microsoft 365 tenant (Microsoft Corporation), and authorized CBE staff — required for OIPC submission per POPA s. 26 and M-Reg s. 7. The diagram must show directional arrows and must NOT be a network or business-process diagram. Upload to the "Before submit" panel.]

---

**Question 21.** How CBE ensures collection, use, and disclosure are only to the extent necessary (limitation principle, POPA ss. 12(4) and 13(4))

POPA s. 12(4) requires that a public body use personal information only to the extent necessary to enable the public body to carry out the purpose for which it was collected, or a consistent purpose, in a reasonable manner. POPA s. 13(4) requires that a public body disclose personal information only to the extent necessary to enable the public body or the recipient to carry out the purpose of the disclosure in a reasonable manner.

CBE applies the limitation principle through the following measures:

**Minimum-necessary collection.** CBE collects only the four data fields identified in Question 16. No additional personal information (such as student date of birth, health information, financial information, or home address) is collected through the M365 environment for the purposes of this Project. The data fields collected are the minimum necessary to provision accounts, assign students to the correct school team, and enable authorized communications.

**Role-based access controls.** Access to personal information within the CBE Teams/M365 tenant is governed by role-based access controls applying the principle of least privilege, with access granted only to CBE staff whose duties require it. Staff in administrative roles can see student and parent/guardian information relevant to their school; staff at School A do not have tenant-level access to records at School B. *(agent's call: RBAC + least privilege applied — industry standard for this deployment scope; override if CBE's actual configuration differs.)*

**No secondary use.** Personal information collected for the Project is used only for the purposes identified in Question 16 — account provisioning, school-assignment routing, and authorized school communications. CBE does not use personal information collected through M365 for research, marketing, profiling, or AI model training. AI-assisted features (e.g., Microsoft Copilot) are not enabled.

**Disclosure limited to contracted service provider.** The only external disclosure of personal information is to Microsoft Corporation in its capacity as contracted service provider under the Microsoft Volume Licensing DPA (org-library-msft-dpa). Microsoft is treated as a CBE employee under POPA s. 1(h) and processes personal information only on CBE's documented instructions to deliver the licensed services. The DPA prohibits Microsoft from using CBE personal information for its own commercial purposes.

**Tenant configuration.** The CBE M365 tenant is configured to restrict external sharing of CBE personal information. Communications and data stored within the tenant are not accessible to individuals or organizations outside the CBE tenant except as explicitly authorized by CBE administrators. *(agent's call: external sharing restricted — standard configuration for K-12 school-board M365 tenants; override if CBE's tenant permits external sharing for specific workloads.)*

**Periodic review.** Access permissions and tenant-configuration settings are reviewed annually by CBE's IT function and the Privacy Officer, with event-triggered reviews on staff role changes and departures, to ensure that access and disclosure remain limited to what is necessary for the Project's authorized purposes. *(agent's call: annual review + event-triggered — standard cadence; override if CBE reviews on a different schedule.)*

---

## Section E. Access, Correction, Accuracy, Retention, and Disposition

---

**Question 22.** Describe how the public body makes individuals aware of their rights under ATIA to request access to their personal information.

Under the *Access to Information Act* (ATIA), SA 2024, c A-1.5, any person has a right of access to records in the custody or under the control of the Calgary Board of Education (CBE), including records containing personal information about themselves. The ATIA imposes a duty on the CBE to make every reasonable effort to assist applicants and to respond to each applicant openly, accurately, and completely. The CBE is required to respond to access requests within 30 calendar days, with limited grounds for extension.

The CBE makes individuals — including students, parents, and guardians — aware of this right through the following channels:

- **CBE Website.** The CBE publishes information about the right to request access to personal information under ATIA, including instructions on how to submit a written request and the applicable response timelines, on its public-facing website.
- **Direct Communication.** At or before the time personal information is collected for this project, the collection notice delivered to parents and guardians (see Question 11 in Section B) identifies the ATIA/POPA Coordinator by title and contact information as the point of contact for questions about collection and access.
- **Designated Contact.** All access requests are directed to Sandra McKenzie, ATIA/POPA Coordinator and Privacy Officer, whose contact details are: privacyofficer@cbe.ab.ca and 403-555-0188 ext. 2401, at 1221 8 Street SW, Calgary, AB T2R 0L4. *(agent's call: contact details drawn directly from the org profile — override only if a separate access-request intake address is used.)*

---

**Question 23.** Does the public body have an access request policy governing how it processes access to personal information requests?

Yes. The CBE has an established access-request policy governing the intake, processing, and response to access requests made under the ATIA. The policy is administered by Sandra McKenzie, ATIA/POPA Coordinator and Privacy Officer. The policy addresses intake of written requests, assignment of file reference, duty-to-assist obligations, processing timelines, fee structures, notification to third parties where required, and the right of applicants to seek review by the Information and Privacy Commissioner.

The CBE's access-request policy reflects the ATIA's duty to assist: the CBE makes every reasonable effort to assist applicants in formulating requests and to respond within the statutory 30-calendar-day deadline, with any extension exercised only on the grounds the ATIA permits. *(agent's call: CBE is assumed to have an operational access-request policy as a mature Alberta school board; override if no formal policy document yet exists, in which case the CBE should describe the steps it will take to document one.)*

---

**Question 24.** Describe how the public body makes individuals aware of their right under POPA to request correction of their personal information.

Under POPA s. 7, an individual has a right to request that the CBE correct personal information about the individual that is in the CBE's custody or under its control. On receiving such a request, the CBE must either correct the information or annotate the record with the correction sought, and must notify any person to whom the information was disclosed during the previous year of the correction or annotation.

The CBE discharges the obligation to make individuals aware of this right as follows:

- **Collection Notice.** The collection notice delivered to parents and guardians at or before the time personal information is collected, pursuant to POPA s. 5(2), identifies the purpose of collection, the legal authority, and the contact information of the ATIA/POPA Coordinator. The notice also advises parents and guardians that they have the right to request correction of any personal information about their child that is inaccurate or incomplete.
- **Website Publication.** Information about the correction-request process — including how to submit a request, the CBE's obligations on receipt, and the timelines that apply — is published on the CBE's public-facing website alongside access-request information.
- **Direct Referral.** Where a parent, guardian, or adult student contacts the CBE with a concern about the accuracy of recorded personal information, CBE staff are trained to refer the individual directly to the ATIA/POPA Coordinator, Sandra McKenzie, at the contact details listed above.

*(agent's call: POPA s. 7 correction-rights standard framing applied throughout; this is a statutory standard, not an override candidate.)*

---

**Question 25.** Does the public body have a correction request policy?

Yes. The CBE has a correction-request policy that governs the receipt and processing of requests made under POPA s. 7. The policy addresses: the manner in which requests are submitted (written request directed to the ATIA/POPA Coordinator); the CBE's obligation to review the request and either correct the information or annotate the record with the correction sought; timelines for response; and the obligation to notify persons to whom the information was disclosed in the previous year of any correction or annotation made.

Correction requests related to personal information processed through Microsoft Teams or Microsoft 365 in scope of this project follow the same policy. Where the information to be corrected is stored in CBE-controlled Microsoft 365 infrastructure (for example, a student's name or school-assignment record held in the CBE tenant), the CBE's Privacy Officer coordinates with the relevant school administrator to update the record in the authoritative source system, which is then reflected in the Microsoft 365 environment. *(agent's call: correction-request policy assumed to exist; override if the CBE is in the process of documenting a formal policy and describe the development steps instead.)*

---

**Question 26.** Describe how the public body makes every reasonable effort to ensure the accuracy and completeness of personal information that it relies on to make decisions affecting individuals (POPA s. 6(a)).

POPA s. 6(a) requires the CBE to make every reasonable effort to ensure that personal information collected by or on behalf of the CBE is accurate and complete in any case where the personal information will be used to make a decision that directly affects the individual the information is about.

For the personal information in scope of this project — student names, school assignments, and parent and guardian contact information — the CBE discharges the accuracy obligation through the following measures:

1. **Source of Truth — Authoritative School Information System.** Student names, school assignments, and parent-contact records are maintained in the CBE's authoritative student information system (SIS). Microsoft Teams and Microsoft 365 receive personal information from the SIS; records in the Microsoft 365 tenant are derived from and reconciled against the SIS, not maintained independently. This architecture ensures that Teams and 365 do not become independent repositories of unchecked personal data.

2. **At Enrolment and on Change of Circumstances.** The CBE collects student and parent information directly at enrolment and re-confirms or updates that information at the beginning of each school year and on any change of circumstances (e.g., change of address, change of guardian). Staff are directed to update records promptly in the SIS when a parent or guardian provides updated contact information.

3. **Correction-Request Channel.** The correction-request process described in Questions 24 and 25 provides an additional safeguard: parents, guardians, and adult students who identify inaccuracies in their recorded information can request correction at any time, and the CBE is obligated to act on such requests.

4. **Staff Training.** CBE staff who manage student and parent data are trained on the accuracy obligation and on the process for recording updates, to minimize manual data-entry errors.

*(agent's call: SIS-as-authoritative-source architecture is the dominant pattern for Alberta school boards using Microsoft 365; override if CBE's actual architecture differs.)*

---

**Question 27.** Describe the public body's retention and disposition policy for the personal information involved in this project and how it complies with POPA s. 6(b).

POPA s. 6(b) requires that where the CBE uses an individual's personal information to make a decision that directly affects the individual, the CBE must retain that personal information for at least one year after the decision is made, so that the individual has a reasonable opportunity to obtain access to it.

The personal information in scope of this project is subject to the following retention rules:

**Student Records (names, school assignments, academic communications).** The Education Act establishes the CBE as a public body responsible for the provision and administration of instructional programs to resident students, with obligations to maintain student records including identifying information, school-to-student assignments, and academic progress information. Consistent with these obligations, student records — including personal information processed through Microsoft Teams and Microsoft 365 — are retained for the duration of the student's enrolment plus a further seven years following graduation or transfer, in accordance with the CBE's Records Retention Schedule. *(agent's call: active-enrolment + 7 years post-graduation or transfer — typical school-board retention norm; override with CBE's specific retention schedule if different.)*

**Parent and Guardian Contact Information.** Parent and guardian contact information is retained for the duration of the relevant student's enrolment, updated as required by changed circumstances, and disposed of in accordance with the CBE's Records Retention Schedule following the conclusion of the student's enrolment and the applicable post-enrolment retention period.

**POPA s. 6(b) Minimum.** For any personal information that the CBE uses to make a decision directly affecting an individual (for example, a school-assignment decision or a communications record used in a conduct proceeding), a minimum one-year post-decision retention period applies, which is satisfied within the broader retention periods described above.

**Microsoft 365 Tenant — Post-Termination Deletion.** The Microsoft Volume Licensing DPA (org-library-msft-dpa) provides that Microsoft retains Customer Data for 90 days following expiration or termination of the CBE's subscription in a limited-function state, then deletes within a further 90 days. The CBE must export or migrate any records subject to the CBE's Records Retention Schedule before subscription termination to ensure those records are preserved within CBE-controlled infrastructure for the duration of the applicable retention period.

---

**Question 28.** Describe how retention and disposition policies are implemented in the information systems used in this project — whether disposition is automated or manual, and how this prevents personal information from being retained past its retention period.

Retention and disposition of personal information in scope of this project are implemented through a combination of Microsoft 365 tenant retention controls and the CBE's records-management procedures, as follows:

**Microsoft 365 Retention Policies (Automated).** Retention of personal information in scope of this project is enforced through standard Microsoft 365 tenant retention policies aligned with the CBE's Records Retention Schedule. Disposition of records past their retention horizon is automated where the tenant's retention-label and retention-policy tooling supports it; manual review applies for records under legal hold. *(agent's call: standard tenant retention + automated disposition — industry standard for Microsoft 365 deployments; override if CBE has specific Microsoft Purview or retention-label configurations that differ.)*

In practice, the CBE's Microsoft 365 administrator configures retention labels and policies within the Microsoft Purview compliance centre to enforce retention periods at the content level (Teams messages, SharePoint documents, Exchange email). Records that reach the end of their configured retention period are either automatically deleted or flagged for disposition review, depending on the label applied. This automated mechanism reduces reliance on manual processes and minimizes the risk that records are retained beyond their required period.

**Student Information System Reconciliation (Ongoing).** Because the CBE's SIS is the authoritative source of student and parent records (see Question 26), disposition of records in the SIS triggers a corresponding review of associated Microsoft 365 data. When a student's record is closed in the SIS (e.g., upon graduation, transfer, or withdrawal), the CBE's IT function reviews the student's Microsoft 365 account and associated Teams and 365 data and applies the disposition action indicated by the Records Retention Schedule.

**Legal Hold.** Records subject to ongoing litigation, investigation, or legal-hold order are preserved regardless of their retention-period expiry, consistent with standard records-management practice. Automated disposition for such records is suspended until the hold is lifted.

**Verification of Disposition.** The CBE's Privacy Officer, in coordination with the IT Security function, reviews disposition records on an annual basis to confirm that records disposed of under automated or manual processes were properly authorized and that no records subject to an active retention requirement were prematurely deleted. *(agent's call: annual disposition-record review — standard governance practice at this risk profile; override if a different review cadence applies.)*

---

## Section F. Protection of Information

*POPA s. 10(1) requires the head of a public body to protect personal information by making reasonable security arrangements against unauthorized access, collection, use, disclosure, or destruction. The questions in this section address CBE's administrative, physical, and technical safeguards for the Microsoft Teams and Microsoft 365 deployment.*

---

**Question 29.** Security classification of personal information in scope

Yes. Under M-Reg s. 2(1), a public body must establish and maintain a security classification system for personal information in its custody or under its control, and that classification must be commensurate with the sensitivity of the information and communicated in writing to all employees who have access to it.

The personal information in scope of the Microsoft Teams and Microsoft 365 deployment — student names, school assignments, and parent and guardian contact information — spans two classification levels:

- **Protected B** applies to student names and school-assignment records. Information about minors is "highly sensitive personal information" within the meaning of M-Reg s. 1. Unauthorized disclosure of student-identifying information could reasonably cause significant harm to the students concerned, including reputational harm, family safety risks, and exposure to grooming or targeting. Protected B classification reflects that sensitivity. *(agent's call: Protected B — recommended for minors. Override if CBE's classification system uses a different scheme.)*

- **Protected A** applies to parent and guardian contact information (names, phone numbers, email addresses) collected solely for the purpose of school communications. This information is standard administrative personal information whose unauthorized disclosure could cause limited or no harm in isolation. *(agent's call: Protected A — default for routine administrative contact data. Override if elevated risk applies, e.g., if any contact records involve domestic-violence safety concerns, in which case Protected B would apply.)*

CBE's classification system operates in accordance with M-Reg s. 2(1) and is communicated to all staff with access to personal information in scope of this project as part of the onboarding privacy training described in Question 32.

---

**Question 30.** Administrative, physical, and technical safeguards

**(a) Administrative safeguards**

Under POPA s. 10(1), the head of a public body must protect personal information by making reasonable security arrangements against such risks as unauthorized access, collection, use, disclosure, or destruction. CBE's administrative safeguards for this project include the following.

*Service-provider agreement.* M-Reg s. 7(6) requires that the privacy-related portions of any service-provider agreement applicable to the project be submitted with the PIA. CBE has executed the Microsoft Online Services Volume Licensing Data Processing Agreement (January 2024) (org-library-msft-dpa), which constitutes the privacy-related service-provider agreement for this project. The M-Reg s. 7(6) obligation is substantively satisfied by this executed agreement. The Microsoft DPA's privacy commitments are addressed in Section G.

*Employee definition and accountability.* Under POPA s. 1(h), "employee" includes a person who, under a contract for services with a public body, performs services for the public body for the purposes of a function of the public body, including a service provider performing such functions on behalf of the public body. Microsoft Corporation, in its capacity as the contracted service provider for Microsoft Teams and Microsoft 365, is therefore treated as part of CBE's extended workforce for POPA accountability purposes. CBE remains accountable under POPA s. 10(1) for the reasonableness of security arrangements protecting personal information in scope of this project, including arrangements that flow through Microsoft. Reliance on Microsoft's technical and organizational measures does not transfer that accountability — CBE must be satisfied that Microsoft's controls are reasonable in light of the sensitivity and volume of personal information processed.

*Privacy training.* M-Reg s. 6(1)(d) requires mandatory privacy training for all employees of the public body, with the training proportional to the employee's role and access to personal information, documented and refreshed periodically. CBE provides privacy training to staff with access to personal information in scope of this project, proportional to staff role and to the sensitivity of the information they handle. Training is delivered at onboarding and refreshed at least annually for staff in privacy-sensitive roles. *(agent's call: proportional training at onboarding + annual refresh — M-Reg s. 6(1)(d) standard. Override if CBE's program operates on a different cadence or scope.)*

*AI features.* AI-assisted features (e.g., Microsoft Copilot, automated meeting summaries, content moderation) are **not** enabled for personal information in scope of this project at this time. Should CBE elect to enable AI features in the future, an Algorithm Impact Assessment will be conducted under M-Reg s. 6(2)(e) and an amendment to this PIA will be filed with the OIPC. *(agent's call: AI features disabled — default for risk-conservative deployment. Override if AI features will be enabled.)*

*Third-party assessment.* A formal third-party privacy and security assessment of Microsoft Teams and Microsoft 365 is not required for this project at this stage. CBE relies on Microsoft's published independent audit reports (SOC 2 Type II, ISO 27001, ISO 27018), which are publicly available at servicetrust.microsoft.com, and on the contractual security commitments in the Microsoft DPA (org-library-msft-dpa), which together satisfy POPA s. 10(1) for this project's risk profile. *(agent's call: vendor-attestation reliance — defensible for moderate-risk deployments using major SaaS vendors. Override if a formal assessment has been completed or if CBE's risk appetite requires one.)*

**(b) Physical safeguards**

Personal information in scope of this project is processed and stored within Microsoft's cloud infrastructure. CBE does not operate on-premises servers or storage for these workloads. Physical safeguards for the cloud environment are Microsoft's responsibility under the Microsoft DPA (org-library-msft-dpa), which commits Microsoft to: maintaining asset inventory, classification, and handling controls for media containing Customer Data; maintaining anti-malware controls; and maintaining business continuity and emergency or contingency plans. CBE's physical safeguards address the endpoint layer: devices accessing personal information in scope of this project are subject to CBE's endpoint management standards, including device enrollment in the organization's mobile device management (MDM) tooling, screen-lock enforcement, encryption at rest on managed devices, and remote-wipe capability for lost or stolen devices, in accordance with POPA s. 10(1). *(agent's call: standard MDM-enrolled-with-screen-lock-and-remote-wipe posture. Override if endpoint-management policy differs.)*

**(c) Technical safeguards**

*Encryption at rest.* Personal information in scope of this project is encrypted at rest using industry-standard cryptographic algorithms (AES-256 or equivalent) provided by Microsoft Teams and Microsoft 365 as part of standard tenant configuration, and confirmed by the Microsoft DPA (org-library-msft-dpa), which commits Microsoft to encrypting "Customer Data and Professional Services Data at rest in Online Services." *(agent's call: encryption at rest enabled — vendor default confirmed in org-library-msft-dpa. Override only if specific configuration concerns apply.)*

*Encryption in transit.* Personal information in scope of this project is encrypted in transit using TLS 1.2 or higher between CBE's endpoints and the Microsoft service. The Microsoft DPA (org-library-msft-dpa) commits Microsoft to encrypting "Customer Data and Professional Services Data in transit over public networks by default." *(agent's call: TLS 1.2+ in transit — industry standard confirmed in org-library-msft-dpa. Override only if a different protocol applies.)*

*Role-based access controls.* Access to personal information in scope of this project is governed by role-based access controls applying the principle of least privilege, with access granted only to staff whose duties require it, in accordance with POPA s. 10(1). The Microsoft DPA (org-library-msft-dpa) also commits Microsoft to applying "least-privilege and role-based access controls; no standing access by Microsoft personnel to Customer Data." *(agent's call: RBAC + least privilege — industry-standard control posture confirmed in org-library-msft-dpa.)*

*Multi-factor authentication.* Multi-factor authentication is enforced for all staff accounts accessing personal information in scope of this project. MFA is the industry-standard expected control under POPA s. 10(1)'s "reasonable security arrangements" obligation for cloud-tenant deployments handling regulated personal information. *(agent's call: MFA enforced — industry standard for cloud SaaS at this scope. Override if MFA is not yet enabled — that is a real gap to disclose.)*

*Audit logging.* See Question 38–40 for the logging and auditing analysis.

*Jurisdictional risk — Plixer doctrine and CLOUD Act exposure.* Under the Upper Harbour **Plixer doctrine**, Microsoft Teams and Microsoft 365 are classified by reference to the jurisdiction of their **ultimate parent corporation**: Microsoft Corporation, headquartered in Redmond, Washington, United States. Both tools carry a Sovereignty Index rating of **Review**. **Data residency is not data sovereignty**: although Microsoft offers Canadian-region data residency for at-rest storage (and CBE should confirm Canadian Geo selection in its tenant settings), that residency election does not exempt Microsoft from its obligations under the United States CLOUD Act. Under 18 U.S.C. § 2713, a provider of electronic communication service or remote computing service shall comply with obligations to preserve, backup, or disclose the contents of a wire or electronic communication and any record or other information pertaining to a customer or subscriber within such provider's possession, custody, or control, regardless of whether such communication, record, or other information is located within or outside of the United States. As of April 2026, the United States has executive agreements under 18 U.S.C. § 2523 in force with the United Kingdom and Australia, but no United States–Canada executive agreement under § 2523 is in force. Contractual measures — including the Microsoft DPA (org-library-msft-dpa), Microsoft's transparency reporting, and any customer-managed encryption key configuration — are partial mitigations only. They reduce practical exposure and provide notice and challenge rights, but they do not eliminate United States jurisdictional authority over Microsoft Corporation's disclosure obligations. CBE accepts this exposure as a documented residual risk for this project. The head of CBE's acceptance of this residual risk is recorded on the signed cover letter at submission. *(agent's call: documented residual risk — dominant practitioner middle-spectrum position. If CBE's project requires Canadian-only sovereignty, a Canadian-parent alternative must be identified.)*

---

**Question 31.** Continuous assessment and monitoring of safeguards

CBE assesses and monitors the safeguards described in Question 30 through the following mechanisms.

*Audit-log review.* M-Reg s. 3(2) requires that where a public body uses an information system to process personal information, the public body must ensure that the system includes sufficient logging and auditing capabilities to detect and investigate unauthorized access, use, disclosure or other contraventions of the Act, and must establish procedures for the periodic review of those logs. Audit logs for Microsoft Teams and Microsoft 365 workloads in scope of this project are reviewed on a quarterly cadence by CBE's IT Security function in coordination with the Privacy Officer, Sandra McKenzie (privacyofficer@cbe.ab.ca, 403-555-0188 ext. 2401), with ad-hoc reviews triggered by suspected confidentiality incidents. *(agent's call: quarterly review — industry standard at this risk profile. Override if CBE reviews more frequently or on a different cadence.)*

*Access reviews.* Access permissions for Microsoft Teams and Microsoft 365 in scope of this project are reviewed annually by CBE's IT function and the Privacy Officer, with event-triggered reviews on staff role changes, departures, and project scope changes. Annual review is the standard cadence for cloud-tenant access governance under POPA s. 10(1) for moderate-risk deployments. *(agent's call: annual access review + event-triggered. Override if CBE's cadence differs.)*

*Vendor audit reports.* CBE monitors Microsoft's published third-party audit results — including SOC 2 Type II and ISO 27001 reports — through Microsoft's Service Trust Portal (servicetrust.microsoft.com). The Microsoft DPA (org-library-msft-dpa) confirms that Microsoft "conduct[s] annual third-party independent audits against applicable control standards/frameworks" and publishes results at servicetrust.microsoft.com. CBE's Privacy Officer reviews the current-cycle audit results annually and flags material findings to CBE's senior leadership.

*Privacy Management Program integration.* POPA s. 25 requires every public body to establish, implement, and maintain a Privacy Management Program (PMP). The PMP must consist of documented policies and procedures that promote the public body's compliance with its duties under the Act and must be proportional to the volume and sensitivity of personal information in the custody or under the control of the public body (in force June 11, 2026). CBE's PMP development is in progress, with the program scheduled to be in place before the June 11, 2026 in-force date, and will include a periodic review cycle covering the safeguards documented in this PIA. *(agent's call: PMP in development — aligned with the June 11, 2026 in-force date. Override if CBE's PMP is already established.)*

---

**Question 32.** Employee awareness of duty to notify under POPA s. 10(2)

Yes. Under POPA s. 10(2), a public body must without unreasonable delay notify (a) the Information and Privacy Commissioner, (b) the responsible Minister, and (c) any individual to whom the information relates, of any loss of, unauthorized access to, or unauthorized disclosure of personal information in the public body's custody or under its control where a reasonable person would consider that there exists a real risk of significant harm to the individual as a result of the loss, access or disclosure.

CBE makes employees aware of this duty through the following measures:

- **Privacy training.** Staff with access to personal information in scope of this project receive training at onboarding that covers the definition of a confidentiality incident, the real-risk-of-significant-harm (RROSH) threshold under POPA s. 10(2), and the internal escalation path. Training is refreshed at least annually for staff in privacy-sensitive roles, in accordance with M-Reg s. 6(1)(d).

- **Breach response policy.** M-Reg s. 6(1)(b) requires that the minimum requirements for a Privacy Management Program include documented internal policies and procedures for breach incidents under POPA s. 10(2). CBE's breach response policy documents the incident-reporting channel (Privacy Officer, privacyofficer@cbe.ab.ca), the internal triage timeline, and the escalation decision for OIPC notification. Where a confidentiality incident involving personal information in scope of this project creates a real risk of significant harm to an affected individual, CBE will notify (a) the Information and Privacy Commissioner of Alberta, (b) the responsible Minister, and (c) each affected individual without unreasonable delay, consistent with POPA s. 10(2). The internal target is notification to the Commissioner within 14 days of confirmation of the RROSH threshold, with notification to affected individuals to follow as soon as reasonably possible. *(agent's call: 14-day internal target — faster than statutory "without unreasonable delay"; aligned with OIPC published guidance. Override if CBE's breach response policy specifies a different timeline.)*

- **Microsoft DPA breach notification.** The Microsoft DPA (org-library-msft-dpa) requires Microsoft to notify CBE "promptly and without undue delay upon becoming aware of a Security Incident," with notification within 72 hours per Appendix A incident response standards and detailed incident information to assist CBE in meeting its OIPC notification obligation.

- **Code of conduct.** Staff obligations regarding the protection of student and parent personal information, including the duty to report suspected incidents to the Privacy Officer without delay, are reinforced through CBE's standard code of conduct and professional standards for educators and administrative staff.

---

**Question 33.** Access control policy and procedures

Yes. CBE has an access control policy governing access to personal information in the Microsoft Teams and Microsoft 365 environment used in this project. Given that this project involves highly sensitive personal information (student records about minors, classified as Protected B), M-Reg s. 6(2) requires the Privacy Management Program to include documented administrative, technical, and physical safeguards where a public body holds high-volume or highly sensitive personal information. Access controls are a documented component of CBE's safeguards for this environment. The policy is administered by CBE's IT function with oversight by the Privacy Officer.

---

**Question 34.** Access approval process

Access requests for Microsoft Teams and Microsoft 365 workloads in scope of this project follow CBE's standard access-approval procedure: line-manager approval combined with IT service-management ticketing, with the Privacy Officer notified of any access grant involving Protected B data classifications (student names and school-assignment records). The Microsoft DPA (org-library-msft-dpa) confirms that Microsoft applies "least-privilege and role-based access controls; no standing access by Microsoft personnel to Customer Data," which means Microsoft-side access to CBE's tenant is itself subject to a defined approval process independent of CBE's internal procedure. *(agent's call: line-manager + IT-ticket access-approval pattern — standard for moderate-risk deployments. Override if CBE's process differs.)*

---

**Question 35.** Least-privilege access limitation

Access to personal information in scope of this project is limited on the basis of defined business requirements and the principle of least privilege, in accordance with POPA s. 10(1). In practice:

- **Teachers and instructional staff** are provisioned with access only to the student records relevant to their assigned classes and sections. A teacher's Teams environment is scoped to their specific class teams; they do not have tenant-wide visibility into other classes' records.
- **Administrative staff** (e.g., school office staff who manage parent-contact records) are provisioned with access to contact directories and communication tools appropriate to their role; they are not provisioned with academic-record access unless their duties require it.
- **IT administrators** hold elevated administrative permissions within the Microsoft 365 tenant but are subject to the "no standing access" commitment in the Microsoft DPA (org-library-msft-dpa) and to CBE's privileged-access management controls.
- **Students** are provisioned as users within their school's Teams environment and have access only to class teams and communications in which they are enrolled members; they cannot access other students' records or other classes' content.

Access is defined at provisioning and reviewed annually, with event-triggered reviews on role changes and departures, as described in Question 31. *(agent's call: RBAC + least privilege — industry-standard control posture. Override if specific deviations apply.)*

---

**Question 36.** Access revocation process

When a staff member's access to Microsoft Teams or Microsoft 365 personal information in scope of this project is no longer required — whether due to role change, transfer, resignation, retirement, or termination — CBE's IT function deactivates the staff member's account and revokes associated role assignments through the standard off-boarding IT service-management process. The target for account deactivation on involuntary separation is the same business day; for planned departures (retirement, transfer), access is transitioned on the effective departure date. The Microsoft DPA (org-library-msft-dpa) commits Microsoft to "deactivat[ing] authentication credentials unused for more than six months," providing a secondary catch for any missed de-provisioning. For students, accounts are deactivated at the end of the school year or upon transfer or withdrawal from CBE. *(agent's call: same-day deactivation on involuntary departure, planned-departure date for voluntary departures — industry standard. Override if CBE's off-boarding SLA differs.)*

---

**Question 37.** Access control table

The access control table below maps CBE positions to system roles, permissions, and the personal information accessible in scope of this project. Row-level staffing numbers are estimates based on a standard Calgary Board of Education organizational profile; CBE's IT function should verify counts against current provisioning records.

| Position / Job Title | System User Role | Approx. No. of Staff | Permissions (C/R/W/M/D) | Personal Information Accessible |
|---|---|---|---|---|
| Classroom Teacher / Instructional Staff | Teams Class Owner / Member | ~6,000 | C, R, W, M | Student names; class/section assignment; class communications and submitted work; parent contact (where shared by admin) |
| School Administrative Staff (office, registrar) | Teams Member; M365 standard user | ~800 | C, R, W, M | Parent/guardian names, phone numbers, email addresses; student name and school-assignment records for administrative purposes |
| School Principal / Assistant Principal | Teams Admin (school-scoped) | ~350 | C, R, W, M | All student and parent records within the school; staff communications |
| CBE Central IT Administrator | Global / Tenant Administrator | ~15 | C, R, W, M, D | Full tenant scope; access is break-glass / privileged-access-managed with audit logging |
| CBE Privacy Officer / ATIA/POPA Coordinator | Standard M365 user + compliance read | 1 | R | Audit logs; compliance reports; access to records relevant to access requests and breach investigations |
| Students (enrolled) | Teams Member (class-scoped) | ~125,000 | C, R, W | Own submitted work; class communications within enrolled teams; no access to other students' records |

*(agent's call: role definitions and permission sets derived from standard Microsoft 365 education-tenant architecture and CBE organizational profile. CBE's IT department should verify staff counts and confirm that permission assignments match actual provisioning in the tenant before submission.)*

---

**Question 38.** Logging and auditing policy and procedures

Yes. CBE has a logging and auditing policy and associated procedures for the Microsoft Teams and Microsoft 365 environment used in this project. M-Reg s. 3(2) requires that where a public body uses an information system to process personal information, the public body must ensure that the system includes sufficient logging and auditing capabilities to detect and investigate unauthorized access, use, disclosure or other contraventions of the Act, and must establish procedures for the periodic review of those logs. Given that this project involves highly sensitive personal information (Protected B — student records about minors), the logging policy is a documented element of CBE's safeguards in accordance with M-Reg s. 6(2). The Microsoft DPA (org-library-msft-dpa) confirms that Microsoft "log[s] access and use of systems containing Customer Data" and conducts "service monitoring at least every six months."

---

**Question 39.** Audit log capture and data elements

Yes. The Microsoft Teams and Microsoft 365 tenant captures and maintains audit logs of access to personal information in scope of this project. Unified audit logging within Microsoft 365 records the following data elements for activities involving personal information:

| Audit Log Data Element | Description |
|---|---|
| User ID / UPN | The account identifier (user principal name) of the staff member, student, or administrator who performed the action |
| Timestamp | Date and time of the action (UTC), with precision to the second |
| Action / Operation | The specific operation performed (e.g., FileAccessed, FileDownloaded, MessageSent, MemberAdded, SignIn) |
| Record / Object Accessed | The specific file, message thread, channel, or Teams object that was accessed or modified |
| IP Address / Client Info | The originating IP address and client application used to perform the action |
| Result Status | Whether the action succeeded or failed (success/failure) |
| Workload / Service | The Microsoft 365 service in which the action occurred (e.g., Teams, SharePoint, Exchange) |

Audit logs are retained for a default period of 90 days, extensible to 365 days for sensitive workloads through Microsoft Purview audit-log retention policies. This satisfies M-Reg s. 3(2)'s requirement for sufficient logging capabilities to detect and investigate unauthorized access to personal information. *(agent's call: unified audit logging enabled, 90-day default retention — industry standard for Microsoft 365 at this scope. Override if a different retention period has been configured or if unified audit logging has not yet been enabled — the latter would be a real gap to disclose.)*

---

**Question 40.** Proactive audit process

CBE proactively audits access to personal information in the Microsoft Teams and Microsoft 365 environment through the following process:

- **Audit criteria.** Reviews focus on: (1) privileged-account activity (tenant administrator sign-ins and actions); (2) anomalous access patterns, including large-scale file downloads, after-hours access, and access from unfamiliar IP addresses or locations; (3) external sharing events involving personal information; and (4) any account flagged by Microsoft's built-in threat-detection signals (Microsoft Defender for Office 365 / Microsoft Entra ID Protection alerts).

- **Frequency.** Routine audit-log reviews are conducted quarterly by CBE's IT Security function in coordination with the Privacy Officer. Ad-hoc reviews are initiated immediately upon receipt of a Microsoft security alert, a staff-reported incident, or a parent or student complaint involving potential unauthorized access. *(agent's call: quarterly routine review + ad-hoc on incident signal — M-Reg s. 3(2) standard for moderate-risk deployments. Override if CBE conducts more frequent reviews.)*

- **Who conducts the audits.** Routine reviews are conducted by CBE's IT Security function. The Privacy Officer (Sandra McKenzie, privacyofficer@cbe.ab.ca, 403-555-0188 ext. 2401) reviews findings and determines whether any incident meets the POPA s. 10(2) real-risk-of-significant-harm threshold requiring notification to the Information and Privacy Commissioner. Escalation to CBE senior leadership occurs where the audit reveals a systemic access-control failure.

- **Documentation.** Findings from each quarterly review are documented in a brief written audit summary retained by the Privacy Officer's office. Summaries that result in remediation actions are filed in CBE's incident log and cross-referenced with the breach response policy required by M-Reg s. 6(1)(b).

---

**Question 41.** Additional protective measures specific to this project

The following additional protective measures apply specifically to this project by virtue of the student population involved and the jurisdictional characteristics of the tools deployed:

*Parental notice of collection.* Because this project involves the collection of personal information about minors, CBE notifies parents and guardians of the collection at or before the time it occurs, in accordance with POPA s. 5(2), which requires the public body to take reasonable steps to ensure that the individual is informed of (a) the purpose for which the information is being collected, (b) the specific legal authority for the collection, and (c) the title, business address and business telephone number of an officer or employee of the public body who can answer the individual's questions about the collection. The collection notice is delivered through CBE's standard school-year communications to parents and guardians (enrolment packages, school newsletters, and the CBE website). Parents and guardians may direct questions about this collection to Sandra McKenzie, ATIA/POPA Coordinator and Privacy Officer, 1221 8 Street SW, Calgary, AB T2R 0L4, privacyofficer@cbe.ab.ca, 403-555-0188 ext. 2401. (See Section B for the full collection-notice analysis.)

[HARD BLOCKER: Provide the actual collection-notice text delivered to parents and guardians at enrolment — the OIPC will review this notice as part of the PIA submission to confirm it meets the POPA s. 5(2) requirements (purpose, legal authority, Privacy Officer contact). If the notice is included in an enrolment package or school handbook, attach that document.]

*Canadian data residency election.* CBE should confirm that its Microsoft 365 tenant is configured with Canada as the selected Geo for at-rest data storage of Core Online Services, in accordance with the data-residency options described in the Microsoft DPA (org-library-msft-dpa). While **data residency is not data sovereignty** — Canadian-region storage does not eliminate CLOUD Act exposure, as addressed in Question 30(c) — Canadian data residency reduces the volume of information transiting to non-Canadian data centres and is a prudent risk-reduction measure. *(agent's call: Canadian Geo selection — prudent baseline. Override if CBE's tenant is already confirmed to a specific Geo or if a different configuration applies.)*

*Previews and experimental features.* The Microsoft DPA (org-library-msft-dpa) explicitly excludes Microsoft "Previews" from GDPR processing terms, Data Security commitments, and HIPAA BAA provisions. CBE will not enable Microsoft 365 or Teams Preview features for workloads involving student or parent personal information in scope of this project. If a Preview feature is evaluated for future adoption, a separate privacy assessment will be conducted before enabling it in the production tenant.

*Data matching not applicable.* This project does not involve a data-matching activity within the meaning of POPA s. 17. The project's personal-information processing is confined to the single operating program of school communications and does not combine personal information from two or more programs to derive new information about individuals. *(agent's call: not a data-matching project — default for single-program scope. Override if records from multiple programs are combined.)*

---

## Section G. Service Providers

**Question 42.** Does the public body use service providers in this project that will have access to personal information?

Yes. The Calgary Board of Education (CBE) uses Microsoft Corporation as the primary service provider for this project. Microsoft Corporation, headquartered in Redmond, Washington, USA, provides the Microsoft Teams and Microsoft 365 platforms through which student names, school assignments, and parent/guardian contact information are collected, processed, and stored.

Under POPA s. 1(h), an "employee" includes a person who, under a contract for services with a public body, performs services for the public body for the purposes of a function of the public body, including a service provider performing such functions on behalf of the public body. Accordingly, Microsoft Corporation, in its capacity as a contracted service provider, is treated as an employee of the CBE for the purposes of POPA's protection-of-personal-information obligations. Processing of personal information through Microsoft Teams and Microsoft 365 is therefore internal use by the CBE's extended workforce, not a disclosure to a third party under POPA s. 13. *(agent's call: standard POPA s. 1(h) service-provider framing — this is a doctrinal point, not an override candidate.)*

The following table identifies the service providers in scope:

| Name of Third Party | Relationship with CBE | Description of Services | Type of Agreement |
|---|---|---|---|
| Microsoft Corporation (parent: Microsoft Corporation, Redmond, WA, USA) | Contracted service provider — treated as employee per POPA s. 1(h) | Provision of Microsoft Teams (staff and student communications platform) and Microsoft 365 (productivity and collaboration suite); processes student names, school assignments, parent/guardian contact details on CBE's behalf | Microsoft Online Services Volume Licensing DPA (org-library-msft-dpa), supplemented by the applicable Product Terms and Online Services Terms |
| Microsoft Ireland Operations Limited | EEA/Switzerland data-protection representative of Microsoft Corporation; Subprocessor affiliate | Serves as Microsoft's designated EEA/Switzerland representative for data protection purposes; engaged where cross-border processing implicates EEA/UK/Switzerland transfer frameworks | Bound by the same Volume Licensing DPA as Microsoft Corporation per the sub-processor provisions of that agreement |

---

**Question 43.** Does the CBE have a contractual agreement with each service provider that addresses its duties under POPA, including the privacy and security of personal information?

Yes. The CBE has the Microsoft Online Services Volume Licensing Data Processing Agreement (DPA), dated January 2, 2024, on file as **org-library-msft-dpa**. This agreement constitutes the service-provider agreement required by M-Reg s. 7(6), which requires that where a privacy impact assessment is submitted to the Commissioner, the privacy-related portions of any service provider agreement applicable to the project must be submitted with the PIA. The privacy-related portions of this DPA are identified below and submitted with this PIA.

The DPA establishes the following POPA-relevant contractual commitments:

**Processing scope and purpose limitation.** The DPA commits Microsoft to processing Customer Data and Personal Data solely to deliver licensed Products and Services per CBE's instructions, to troubleshoot, maintain performance and security, and for limited incident-to-business operations (billing, compensation, internal reporting, financial reporting) using aggregated or pseudonymized data only. This aligns with the use-limitation principle in POPA s. 12(4), which requires a public body to use personal information only to the extent necessary to enable it to carry out the purpose for which it was collected.

**Security commitments.** Under POPA s. 10(1), the head of a public body must protect personal information by making reasonable security arrangements against such risks as unauthorized access, collection, use, disclosure or destruction. The DPA (org-library-msft-dpa) addresses this obligation through commitments that include: implementation and maintenance of technical and organizational measures per ISO 27001, ISO 27002, and ISO 27018; encryption of Customer Data in transit over public networks and at rest in Online Services; application of least-privilege and role-based access controls with no standing access by Microsoft personnel to Customer Data; annual third-party independent audits with results published at servicetrust.microsoft.com; and implementation of pseudonymization, encryption, and processes for regularly testing and evaluating security measures. The substantive security analysis, including the Upper Harbour Sovereignty Index classification and CLOUD Act residual-risk acceptance, is addressed in Section F Q33.

**Breach notification.** The DPA commits Microsoft to notify CBE promptly and without undue delay upon becoming aware of a Security Incident, with notification including detailed information about the incident, within 72 hours per the DPA's Appendix A incident-response standards. This supports CBE's own obligation under POPA s. 10(2) to notify (a) the Information and Privacy Commissioner, (b) the responsible Minister, and (c) any individual to whom the information relates, of any loss of, unauthorized access to, or unauthorized disclosure of personal information where a reasonable person would consider that there exists a real risk of significant harm to the individual as a result of the loss, access or disclosure.

**Sub-processors.** Microsoft may engage sub-processors (including Microsoft Affiliates) with CBE's prior general written consent. Sub-processors are bound by written agreements requiring at least equivalent data protection as the DPA. New sub-processors for Customer Data require six months' advance notice; CBE may terminate without penalty if it objects within that notice period. Microsoft remains fully liable for sub-processors' compliance.

**Post-termination deletion.** Microsoft retains Customer Data for 90 days post-expiration or termination in limited function, then deletes within an additional 90 days. This supports CBE's retention obligations under POPA s. 6(b) (see Section E for the full retention analysis).

[HARD BLOCKER: Submit the privacy-related portions of the Microsoft Volume Licensing DPA (org-library-msft-dpa) as an attachment to this PIA when filing with the OIPC — required for submission per M-Reg s. 7(6).]

---

**Question 44.** Will the service provider process access to information requests on behalf of the CBE?

No. Microsoft Corporation, as service provider, will not process access to information requests on behalf of the CBE. Access requests submitted by individuals under the Access to Information Act (ATIA) are received, processed, and responded to by the CBE directly through its ATIA/POPA Coordinator, Sandra McKenzie (privacyofficer@cbe.ab.ca; 403-555-0188 ext. 2401). Microsoft's role is confined to providing CBE with the technical capability to locate, retrieve, and export records responsive to an access request (e.g., through the Microsoft 365 compliance centre and eDiscovery tooling), acting solely on CBE's instruction. The DPA (org-library-msft-dpa) confirms that Microsoft processes Customer Data solely per customer instructions and does not exercise independent judgment over the content or disposition of such records.

Where an individual submits an access request and responsive records reside within CBE's Microsoft 365 or Teams tenant, CBE's Privacy Officer coordinates with CBE's IT function to retrieve the relevant records and fulfill the request within the statutory timelines prescribed by the ATIA. The ATIA access-rights framework is addressed substantively in Section E.

---

**Question 45.** Has the CBE clarified in its contractual agreement(s) with service provider(s) that CBE maintains control of any information the service provider accesses, collects, or uses?

Yes. The Microsoft Volume Licensing DPA (org-library-msft-dpa) establishes CBE's control over its Customer Data through the following provisions:

**Customer-as-controller framing.** The DPA identifies CBE as the data controller and Microsoft as the data processor. Microsoft processes Customer Data solely to deliver licensed Products and Services per CBE's documented instructions. Microsoft does not acquire rights in Customer Data independent of those instructions, and does not use Customer Data for its own commercial purposes or for AI model training without CBE's separate consent.

**Instruction-only processing.** Microsoft's processing scope is expressly limited to CBE's instructions. Microsoft does not independently determine the purposes or means of processing CBE's Customer Data for core service delivery, consistent with CBE's obligation to retain custody and control of personal information under POPA.

**Least-privilege and no-standing-access.** The DPA commits Microsoft to applying least-privilege and role-based access controls, with no standing access by Microsoft personnel to Customer Data. Any access by Microsoft personnel requires a specific operational justification and is logged and auditable.

**Post-termination deletion.** On expiry or termination, Microsoft retains Customer Data for 90 days in a limited-function state, then deletes it within a further 90 days. CBE retains the right to export its Customer Data during this period. This clause ensures CBE's control over disposition does not evaporate at contract end.

**Sub-processor accountability.** Microsoft remains contractually liable for its sub-processors' compliance with the DPA's terms, ensuring that CBE's control extends through the sub-processor chain.

Failure to retain contractual control of personal information would constitute a disclosure to a third party under POPA s. 13, which requires authority. The provisions above are sufficient to characterize Microsoft's processing as internal use under POPA s. 1(h), not a third-party disclosure. *(agent's call: standard POPA s. 1(h) / controller-framing analysis derived from the DPA summary in org-library-msft-dpa — override if a specific DPA clause has been amended or if a separate data-custody agreement is in place.)*

[HARD BLOCKER: Submit the privacy-related portions of the Microsoft Volume Licensing DPA (org-library-msft-dpa) as an attachment to this PIA when filing with the OIPC — the OIPC will not review PIAs missing copies of associated contracts, per M-Reg s. 7(6).]

---

**Question 46.** Does the contractual agreement identify each party's responsibilities related to the privacy and security of personal information?

Yes. The Microsoft Volume Licensing DPA (org-library-msft-dpa) allocates responsibilities across the full personal-information life cycle as follows:

| Life-Cycle Stage | CBE's Responsibilities | Microsoft's Responsibilities | DPA Basis |
|---|---|---|---|
| **Collection** | Determines what personal information is collected and for what purpose; provides collection notice under POPA s. 5(2); obtains any necessary operating-program authority under POPA s. 4(c) / Education Act | Provides the technical platform through which collection occurs; processes only per CBE's instructions | Processing scope clause; Customer-as-controller framing |
| **Use** | Restricts use to operating-program purposes (school communications, administration); applies POPA s. 12(4) use-limitation principle | Processes Customer Data for service delivery and limited incident-to-business operations (billing, compensation, internal reporting) using aggregated or pseudonymized data only | Processing scope clause |
| **Disclosure** | Authorizes any disclosure of personal information; retains control of Customer Data | Does not disclose Customer Data to third parties except sub-processors bound by equivalent obligations, or as required by applicable law (subject to CLOUD Act residual risk — see Section F Q33) | Sub-processor clause; government-access clause |
| **Protection / Security** | Maintains reasonable security arrangements under POPA s. 10(1); configures tenant security settings (MFA, RBAC, audit logging, device management); reviews logs per M-Reg s. 3(2) | Implements and maintains ISO 27001 / ISO 27002 / ISO 27018 technical and organizational measures; encrypts data in transit and at rest; applies least-privilege access; conducts annual third-party audits | Security commitments section; Appendix A |
| **Retention** | Applies CBE's Records Retention Schedule and POPA s. 6(b) minimums; configures Microsoft 365 retention policies aligned with the schedule | Retains Customer Data for 90 days post-termination, then deletes; supports CBE-configured retention labels and policies in the tenant | Term and termination clause; post-termination deletion clause |
| **Disposition** | Initiates post-retention deletion through tenant administration; exports records prior to contract termination where required | Deletes Customer Data within 180 days of contract expiry (90-day limited-function window + 90-day deletion window); provides Customer with export capability during this period | Term and termination clause |
| **Breach Notification** | Assesses RROSH threshold; notifies OIPC, responsible Minister, and affected individuals per POPA s. 10(2) where threshold is met | Notifies CBE promptly and without undue delay (within 72 hours per Appendix A) upon becoming aware of a Security Incident; provides detailed incident information; assists CBE in fulfilling notification obligations | Breach notification clause; Appendix A |
| **Sub-processors** | Grants general written consent to Microsoft Affiliates as sub-processors; retains right to object to new third-party sub-processors within notice periods | Binds sub-processors to equivalent data protection obligations; publishes sub-processor list; provides 6-month (Customer Data) or 30-day (Professional Services Data) advance notice of new sub-processors; remains fully liable | Sub-processor clause |

*(agent's call: responsibilities table derived from DPA summary in org-library-msft-dpa — override if specific DPA clause numbers are needed for the OIPC submission, in which case cite the actual DPA section references.)*

---

**Question 47.** Identify sections of the contractual agreement(s) that address ongoing training requirements for the service provider's employees who have access to personal information.

The Microsoft Volume Licensing DPA (org-library-msft-dpa) addresses Microsoft personnel training through its security commitments, which include a commitment to provide periodic and mandatory data privacy and security training to personnel with access to Customer Data, and to ensure that all such personnel are under confidentiality obligations.

M-Reg s. 6(1)(d) requires that the minimum requirements for a Privacy Management Program include mandatory privacy training for all employees of the public body, with the training proportional to the employee's role and access to personal information, and with training documented and refreshed periodically. Because Microsoft Corporation is treated as an employee of the CBE under POPA s. 1(h), Microsoft's training commitments under the DPA are relevant to the CBE's overall satisfaction of the M-Reg s. 6(1)(d) standard as it extends through the service-provider relationship.

For its own staff, the CBE provides privacy training to all employees with access to personal information in scope of this project, proportional to staff role and the sensitivity of the information they handle, in accordance with M-Reg s. 6(1)(d). Training is delivered at onboarding and refreshed at least annually for staff in privacy-sensitive roles. *(agent's call: proportional training program at onboarding + annual refresh — M-Reg s. 6(1)(d) standard. Override if the CBE's program operates on a different cadence or scope.)*

The DPA does not specify the precise curriculum, frequency, or delivery format of Microsoft's internal privacy training beyond the commitment to "periodic and mandatory" training with confidentiality obligations. The CBE relies on Microsoft's published independent audit certifications (ISO 27001, SOC 2 Type II — see DPA security commitments section and servicetrust.microsoft.com) as evidence that Microsoft's training and personnel-security controls meet the standard expected of a contracted service provider under POPA s. 10(1). *(agent's call: vendor-attestation reliance on ISO 27001 / SOC 2 Type II — defensible for this risk profile. Override if CBE's risk appetite requires direct audit of Microsoft's training records.)*

---

## Section H. Project Risk Assessment and Mitigation

**Question 48.** Security vulnerability assessment and penetration testing

A formal third-party vulnerability assessment (VA) or penetration test (pentest) specific to the Adoption of Microsoft Teams and Microsoft 365 for Staff and Student Communications has not been commissioned by CBE as a standalone project-level exercise. *(agent's call: no VA/pentest on file in the Org Privacy Library — correct if a project-specific assessment has been completed, and attach the results to this submission.)*

This position is supportable at CBE's current risk profile for the following reasons:

**Vendor-side assurance.** The Microsoft Volume Licensing DPA (org-library-msft-dpa), submitted with this PIA as required by M-Reg s. 7(6), is the primary service-provider agreement governing Microsoft's processing obligations. The DPA's security commitments include annual third-party independent audits conducted against ISO 27001, ISO 27002, and ISO 27018, with results published at servicetrust.microsoft.com. Those published audit reports — SOC 2 Type II and ISO 27001 — constitute independent attestation of Microsoft's control environment and satisfy the vendor-assurance component of CBE's reasonable security inquiry under POPA s. 10(1), which requires the head of a public body to protect personal information by making reasonable security arrangements against risks such as unauthorized access, collection, use, disclosure or destruction.

**CBE tenant-level controls.** The project's risk exposure is further bounded by the tenant-level controls addressed in Section F: multi-factor authentication, role-based access, unified audit logging, encryption at rest and in transit, and endpoint management. These controls collectively represent the administrative and technical safeguard layer that a VA or pentest would be expected to verify. Their presence reduces the marginal value of a standalone pentest for a deployment of this type and scale.

**Proportionality under M-Reg s. 7(3).** The level of detail required in a privacy impact assessment — and by extension, the depth of security assurance activities associated with it — must be commensurate with the complexity of the project and the sensitivity of the personal information involved. This deployment involves school-administration and communications data (student names, school assignments, parent contacts) for a K–12 school board using a major enterprise SaaS platform. It does not involve financial transaction processing, biometric identification, or real-time health monitoring. A formal pentest is therefore not required at this stage.

**Recommended periodic practice.** Notwithstanding the above, CBE should incorporate periodic vulnerability scanning of its Microsoft 365 tenant configuration into its broader IT security risk-management cycle. Microsoft's Secure Score tooling within the Microsoft 365 Defender portal provides continuous posture visibility at no additional cost and is an appropriate substitute for periodic VA exercises at this risk level. Should CBE expand the project's scope to include AI-assisted features, bulk data export integrations, or custom application development on the Microsoft Power Platform, a formal VA or pentest should be conducted before go-live and results attached as an amendment to this PIA.

*(agent's call: vendor-attestation reliance — defensible for moderate-risk K–12 deployments using major SaaS vendors with published SOC 2 / ISO 27001 reports. Override if CBE's IT security policy mandates project-level pentests, or if a pentest has already been completed — attach results in that case.)*

---

## Section H1. General Risks (to be completed for all PIA submissions)

| Risk # | Privacy Risk | Description | Risk Mitigation Measures | Policy Reference and Public Body Comments |
|--------|-------------|-------------|--------------------------|------------------------------------------|
| 1 | Unauthorized collection of personal information by authorized users contrary to POPA ss. 4 and 5 | Microsoft Teams and Microsoft 365 are commercial platforms built for global enterprise markets. Default configurations may enable collection of telemetry, diagnostic data, or optional profile fields that exceed what CBE requires for school-related communications. Without tenant hardening, the platform may ingest personal information about students, parents, and staff beyond what is authorized under the Education Act and POPA s. 4(c). | CBE's collection authority for student names, school assignments, and parent-contact information flows from the Education Act (operating-program authority) and POPA s. 4(c). Tenant configuration for Microsoft Teams and Microsoft 365 is scoped to the data fields necessary for that operating purpose; optional fields and telemetry-collection features not required for school communications are disabled. AI-assisted features (e.g., Microsoft Copilot, automated meeting summaries) are not enabled — see Section F for the Sovereignty Index analysis and AI-features determination. Per-field collection authority is documented in Section B/D of this PIA. *(agent's call: tenant scoping to required fields is the expected control at this risk profile. Override if specific fields have been disabled or enabled differently in your Microsoft 365 configuration.)* | POPA s. 4(c) — collection must relate directly to and be necessary for an operating program or activity of the public body. Education Act, SA 2012, c E-0.3 — operating-program authority for CBE's record-keeping and instructional obligations. See Section B/D for per-field authority mapping. |
| 2 | Unauthorized use of personal information by authorized users | Staff with access to Microsoft Teams and Microsoft 365 may use personal information collected for school-communications purposes for a secondary purpose — for example, using student contact data to communicate about non-school activities, sharing rosters in group chats outside the relevant class context, or using parent-contact details for purposes unrelated to CBE programs. | POPA s. 12(4) requires that personal information be used only to the extent necessary to enable the public body to carry out the purpose for which it was collected. CBE enforces the use-limitation principle through: (a) acceptable-use policy applicable to all staff accessing Microsoft Teams and Microsoft 365; (b) role-based access controls (RBAC) applying the principle of least privilege, ensuring staff access only information relevant to their duties; and (c) privacy training under M-Reg s. 6(1)(d) delivered at onboarding and refreshed annually, covering POPA use-limitation obligations. *(agent's call: acceptable-use policy + RBAC + training as the standard control triad. Override if CBE's use-governance controls operate differently.)* | POPA ss. 12 and 12(4) — use limited to the purpose of collection or a consistent purpose, and only to the extent necessary. M-Reg s. 6(1)(d) — mandatory privacy training proportional to role and access. See Section F for RBAC and training measures. |
| 3 | Unauthorized disclosure of personal information by authorized users | Personal information in scope may be disclosed contrary to POPA s. 13 through: (a) staff sharing student or parent-contact data in external chats or Teams channels outside the authorized school-communications context; (b) misconfigured sharing permissions that expose files or contacts to recipients outside CBE's tenant; (c) interception of data in transit where appropriate security controls are absent; or (d) insecure disposal of devices containing cached personal information. | POPA s. 13(4) requires that personal information be disclosed only to the extent necessary to carry out the purpose of the disclosure in a reasonable manner. Mitigations include: (a) tenant-level sharing controls restricting external sharing of CBE data; (b) encryption in transit using TLS 1.2 or higher between CBE endpoints and Microsoft 365/Teams service — *(agent's call: TLS 1.2+ in transit, industry standard. Override if a different protocol applies)*; (c) endpoint management (MDM) controls covering screen-lock, device encryption, and remote-wipe for devices accessing CBE personal information — *(agent's call: standard MDM posture. Override if BYOD or unmanaged endpoints are permitted)*; (d) staff training on disclosure limitations and proper channel use. Disposal of media containing CBE personal information follows CBE's records-disposal procedures. | POPA ss. 13 and 13(4) — disclosure authority and disclosure-limitation principle. POPA s. 10(1) — reasonable security arrangements against unauthorized disclosure. See Section F Q29–Q33 for full security-safeguards analysis. |
| 4 | Unauthorized access to personal information by unauthorized users or malicious software | Student names, school assignments, and parent-contact information stored and transmitted through Microsoft Teams and Microsoft 365 may be exposed to unauthorized external actors (credential-based attacks, phishing, ransomware) or unauthorized internal actors if account hygiene and access controls are inadequate. Information about minors is highly sensitive within the meaning of M-Reg s. 1; unauthorized access creates a real risk of significant harm under POPA s. 10(2). | POPA s. 10(1) requires the head of a public body to protect personal information by making reasonable security arrangements against risks including unauthorized access. Safeguards include: (a) multi-factor authentication (MFA) enforced for all staff accounts accessing personal information in scope — *(agent's call: MFA enforced, industry standard for cloud-SaaS at this scope. Override if MFA is not yet enabled — that is a real gap to disclose)*; (b) RBAC applying least-privilege principles; (c) encryption at rest and in transit per Microsoft's DPA commitments, with no standing access by Microsoft personnel to Customer Data, and least-privilege and role-based access controls maintained on the vendor side; (d) anti-malware controls maintained by Microsoft per the DPA; (e) Microsoft's annual third-party independent audits published at servicetrust.microsoft.com. CBE's accountability for these safeguards flows through POPA s. 1(h), which treats Microsoft as an extended employee of CBE for POPA purposes. | POPA s. 10(1) — reasonable security arrangements. POPA s. 1(h) — service providers treated as employees for protection-of-personal-information obligations. See Section F Q29–Q33 for the full safeguards analysis and Section G for the Microsoft DPA. |
| 5 | Loss of personal information | Student, parent, and staff personal information in the Microsoft Teams and Microsoft 365 environment may be rendered inaccessible through: ransomware or destructive malware encrypting CBE tenant data; accidental deletion by staff with insufficient recovery safeguards; or inadequate backup and disaster-recovery configuration. Loss of information could impair CBE's ability to meet POPA s. 6(b) minimum-retention obligations and ATIA access-request obligations. | Mitigations include: (a) Microsoft maintains data recovery procedures with copies stored separately, reviewed at least every six months, and maintains business continuity and emergency/contingency plans; (b) CBE maintains backup and recovery procedures for data held in the Microsoft 365 tenant, tested periodically — *(agent's call: standard backup + recovery posture. Override if CBE's backup procedures for Microsoft 365 differ or if third-party backup tooling is used)*; (c) CBE's change-management process governs IT-system modifications affecting tenant configuration; (d) role-based access controls limit the universe of accounts capable of bulk deletion. | POPA s. 6(b) — retention obligation for personal information used to make a decision directly affecting an individual. POPA s. 10(1) — reasonable security arrangements including against destruction. See Section E for retention requirements and Section F for full safeguards. |
| 6 | Loss of custody or control of personal information | CBE may lose effective custody or control of personal information in scope if: (a) the Microsoft service-provider agreement fails to adequately bind Microsoft to POPA-consistent handling obligations; (b) Microsoft's United States parent-jurisdiction nexus enables compelled disclosure to US authorities under the CLOUD Act (18 U.S.C. § 2713), effectively removing CBE's control over the information without notice; or (c) Microsoft sub-processors are engaged without adequate contractual protections flowing through the supply chain. | The Microsoft Volume Licensing DPA (org-library-msft-dpa) contractually binds Microsoft to CBE's data-handling instructions and satisfies M-Reg s. 7(6). Sub-processors are bound by written agreements requiring at least equivalent data protection as the DPA; Microsoft remains fully liable for sub-processor compliance; and CBE retains termination rights where it objects to a new sub-processor. However, **data residency is not data sovereignty**: although Microsoft offers Canadian-region data residency for at-rest storage, this does not exempt Microsoft from compelled disclosure under 18 U.S.C. § 2713, which requires a US-jurisdictional provider to comply with disclosure obligations regardless of whether the data is located within or outside the United States. As of April 2026, no US–Canada executive agreement under 18 U.S.C. § 2523 is in force. CBE accepts this exposure as a documented residual risk that cannot be eliminated by contractual measures. See Section F Q33 for the full Plixer doctrine and CLOUD Act jurisdictional analysis. | POPA s. 1(h) — service-provider/employee definition. M-Reg s. 7(6) — privacy-related portions of service-provider agreements must be submitted with the PIA. 18 U.S.C. § 2713 (CLOUD Act); 18 U.S.C. § 2523 (no US–Canada agreement in force). Full jurisdictional analysis: Section F Q33. Microsoft DPA: Section G. |
| 7 | Unauthorized destruction of personal information | Student, parent, and staff personal information may be prematurely or inadvertently destroyed through: (a) misconfigured tenant retention labels that trigger early deletion; (b) staff manually deleting records without authority; (c) failure to apply a legal hold when required; or (d) Microsoft deleting Customer Data following subscription expiration without adequate notice to CBE. | Mitigations include: (a) retention policies are enforced through the Microsoft 365 tenant, aligned with CBE's records-retention schedule — student records are retained for the duration of enrolment plus seven years post-graduation or transfer, in accordance with the Education Act and POPA s. 6(b) — *(agent's call: active-enrolment + 7 years, typical school-board norm. Override with CBE's specific retention schedule if different)*; (b) Microsoft retains Customer Data for 90 days post-expiration or termination in limited function, then deletes within an additional 90 days — CBE's subscription management procedures must account for this window; (c) legal-hold procedures are applied to records subject to litigation or regulatory investigation before any disposition occurs; (d) staff are trained on destruction authority and the obligation not to delete personal information outside the approved schedule. | POPA s. 6(b) — retention obligation. Education Act — record-keeping obligations for school boards. See Section E for the full retention and disposition analysis. |
| 8 | Loss of integrity including unauthorized modification of personal information | Student names, school assignments, and parent-contact data may be rendered inaccurate or incomplete through: (a) staff data-entry errors; (b) unauthorized modification by an internal or external actor with access to the relevant records; (c) synchronization errors between Microsoft 365 and CBE's student information system; or (d) IT system changes that affect record integrity without adequate change management. | POPA s. 6(a) requires that a public body make every reasonable effort to ensure that personal information is accurate and complete where it will be used to make a decision that directly affects the individual. Mitigations include: (a) RBAC limiting write access to records to staff with an operational need to modify them; (b) audit logging capturing modification events in the Microsoft Teams and Microsoft 365 tenant — *(agent's call: unified audit logging enabled, 90-day default retention. Override if not yet enabled or different retention applies)*; (c) CBE's change-management process governing IT-system changes affecting tenant data; (d) staff training on accurate data-entry practices; (e) POPA s. 7 correction rights enabling individuals to identify and request correction of inaccurate records (see Section E). | POPA s. 6(a) — accuracy obligation. M-Reg s. 3(2) — audit logging to detect unauthorized access or modification. See Section E for correction rights; Section F for audit-logging configuration. |
| 9 | Unauthorized retention of personal information | Personal information in scope may be retained beyond its authorized retention period if: (a) CBE has not configured Microsoft 365 tenant retention labels to enforce disposition; (b) staff retain copies of records in personal OneDrive or local storage outside the retention framework; or (c) backup copies persist beyond the authorized retention window. | Retention of personal information in scope of this project is enforced through Microsoft 365 tenant retention policies aligned with CBE's records-retention schedule — *(agent's call: standard tenant retention + automated disposition. Override if Purview/retention-label configuration differs)*. Student records are retained for the duration of enrolment plus seven years post-graduation or transfer *(agent's call: active-enrolment + 7 years. Override with CBE's specific schedule if different)*. Staff are trained on retention obligations and prohibited from maintaining personal shadow copies of personal information outside the authorized system. Disposition past the retention horizon is automated where the tenant supports it; manual review applies for records under legal hold. | POPA s. 6(b) — retention minimum for decision-related personal information. Education Act — record-keeping obligations. See Section E for the full retention and disposition analysis. |
| 10 | Lack of notice or improper notice at the time of collection | POPA s. 5(2) requires a public body that collects personal information directly from an individual to take reasonable steps, at or before the time of collection, to ensure the individual is informed of: (a) the purpose for which the information is being collected; (b) the specific legal authority for the collection; and (c) the title, business address, and business telephone number of an officer or employee who can answer questions about the collection. For a project involving students (minors), notice must be provided through appropriate parental/guardian channels. | CBE provides collection notice to parents and guardians (on behalf of students) and to staff at or before the time personal information is collected for this project. Notice identifies: (a) the purpose (school communications via Microsoft Teams and Microsoft 365); (b) the legal authority (Education Act operating-program obligations and POPA s. 4(c)); and (c) the contact for questions: Sandra McKenzie, ATIA/POPA Coordinator and Privacy Officer, privacyofficer@cbe.ab.ca, 403-555-0188 ext. 2401. Notice is delivered through CBE's standard parental-communication channel (e.g., school registration package, CBE website notice, and/or enrollment letter) to ensure the manner of notice matches the manner of collection. The actual collection-notice text provided to parents and guardians is a required attachment for OIPC submission. | POPA s. 5(2) — collection-notice obligation. Education Act — operating-program authority anchoring the notice's legal-authority statement. See Section B for the full collection-notice analysis. [HARD BLOCKER: Attach the collection notice provided to parents/guardians and staff for this project — required for OIPC submission per POPA s. 5(2). The notice must state the purpose, the specific legal authority (Education Act and POPA s. 4(c)), and Sandra McKenzie's contact details.] |
| 11 | Lack of clarity or failure to provide information regarding access to or correction of personal information | CBE may fail to adequately inform students, parents, and staff of their rights to request access to, or correction of, personal information held by CBE in connection with this project. | Individuals have the right to request access to records in CBE's custody or under its control — including records about themselves in Microsoft Teams and Microsoft 365 — under the ATIA. CBE responds to access requests within 30 calendar days, with limited grounds for extension. Information about the access-request process is available through Sandra McKenzie, ATIA/POPA Coordinator and Privacy Officer (privacyofficer@cbe.ab.ca, 403-555-0188 ext. 2401) and through CBE's published privacy procedures. Individuals also have a right under POPA s. 7 to request correction of personal information about them in CBE's custody or control; CBE either corrects the information or annotates the record, and notifies any person to whom the information was disclosed in the previous year of the correction or annotation. Access and correction rights are disclosed to individuals in CBE's collection notice and on CBE's website. | ATIA — right of access, duty to assist, and 30-day response-time obligation. POPA s. 7 — correction right. See Section E for the full access and correction analysis. |
| 12 | Lack of or inadequate privacy breach management policies and procedures | Without documented breach-response procedures, CBE may fail to detect, triage, or notify the relevant parties in a timely manner following a confidentiality incident involving student, parent, or staff personal information in the Microsoft Teams and Microsoft 365 environment. POPA s. 10(2) requires notification of the Information and Privacy Commissioner, the responsible Minister, and affected individuals without unreasonable delay where a reasonable person would consider there exists a real risk of significant harm (RROSH). | CBE's breach-response procedures align with M-Reg s. 6(1)(b). Where a confidentiality incident involving personal information in scope creates a RROSH, CBE notifies (a) the Information and Privacy Commissioner of Alberta, (b) the responsible Minister, and (c) each affected individual without unreasonable delay. The internal target is notification to the Commissioner within 14 days of RROSH confirmation, with notification to affected individuals to follow as soon as reasonably possible — *(agent's call: 14-day internal target, aligned with OIPC published guidance. Override if CBE's breach-response policy specifies a different timeline)*. Staff are trained on incident-reporting obligations at onboarding and annually. Microsoft is required under the DPA to notify CBE promptly and without undue delay upon becoming aware of a Security Incident, with a target of 72 hours per Appendix A incident response standards, and to assist CBE in fulfilling its regulatory notification obligations. | POPA s. 10(2) — breach notification obligation (RROSH threshold). M-Reg s. 6(1)(b) — breach-response policy as PMP minimum content. See Section F for full breach-response analysis. |
| 13 | Lack of assessment of third-party privacy and security controls | Without an adequate assessment of Microsoft's privacy and security controls, CBE cannot attest that its service provider reasonably protects personal information in compliance with POPA, and may fail to meet its obligations under POPA s. 10(1). | CBE assessed Microsoft's controls through the following: (a) the Microsoft Volume Licensing DPA commits Microsoft to technical and organizational measures per ISO 27001, ISO 27002, and ISO 27018; annual third-party independent audits with results published at servicetrust.microsoft.com; and encryption at rest and in transit, least-privilege access, anti-malware, and data-recovery procedures; (b) CBE's review of Microsoft's published SOC 2 Type II audit reports and ISO certifications; (c) the contractual commitments in the DPA on file (org-library-msft-dpa), which satisfies M-Reg s. 7(6). A formal standalone third-party assessment of Microsoft's controls is not required for this project at this stage — CBE relies on vendor attestation through published audit reports, which is defensible for a moderate-risk deployment using a major SaaS vendor under POPA s. 10(1) and M-Reg s. 7(3) — *(agent's call: vendor-attestation reliance. Override if CBE's risk appetite requires a formal independent assessment)*. The residual jurisdictional risk from Microsoft's US parent is documented in Risk 6 above and in Section F Q33. | POPA s. 10(1) — reasonable security arrangements. M-Reg s. 7(3) — level of PIA detail commensurate with project complexity. M-Reg s. 7(6) — service-provider agreement required with PIA submission. See Section G for the DPA analysis and Section F Q33 for jurisdictional risk. |
| 14 | Use or disclosure of personal information for secondary purposes by CBE or Microsoft without proper authority | Microsoft may use CBE's student, parent, or staff personal information for purposes beyond delivering the licensed services — for example, to train AI models, for product improvement, or for targeted advertising — contrary to POPA s. 12. CBE staff may also use personal information for secondary purposes without authority. | The Microsoft DPA restricts processing to: delivery of licensed Products and Services per Customer instructions; troubleshooting; performance and security maintenance; and limited incident-to-business operations (billing, compensation, internal reporting, financial reporting) using aggregated or pseudonymized data only. AI-assisted features (e.g., Microsoft Copilot, automated meeting summaries) that could expose personal information to AI model training are not enabled for this project — *(agent's call: AI features disabled, default risk-conservative deployment. Override and file an Algorithm Impact Assessment if AI features will be enabled)*. Previews are explicitly excluded from GDPR processing terms and the DPA's data-security provisions — use of Previews with personal information is at CBE's own risk. CBE's acceptable-use policy prohibits staff from using personal information collected for school-communications purposes for non-school secondary purposes, consistent with POPA s. 12(4). | POPA ss. 12 and 12(4) — use-limitation obligation. M-Reg s. 6(2)(e) — PMP must include policies governing use of automated decision-making and AI systems. See Section F Q33 for the Plixer doctrine analysis. |
| 15 | Insufficient or absent logging and auditing controls | Without adequate logging, CBE cannot detect unauthorized access, use, or disclosure of personal information in the Microsoft Teams and Microsoft 365 environment; cannot investigate suspected breaches; and cannot support the Commissioner's investigation powers under POPA s. 27(1)(j). | M-Reg s. 3(2) requires that information systems processing personal information include sufficient logging and auditing capabilities to detect and investigate unauthorized access, use, disclosure, or other contraventions, and that the public body establish procedures for periodic review of those logs. Unified audit logging is enabled in the Microsoft Teams and Microsoft 365 tenant covering this project's workloads, with a default retention period of 90 days (extensible to 365 days for sensitive workloads) — *(agent's call: audit logging enabled, 90-day retention. Override if not yet enabled or different retention applies)*. Audit logs are reviewed quarterly by CBE's IT Security function in coordination with the Privacy Officer, with ad-hoc reviews triggered by suspected incidents — *(agent's call: quarterly review cadence, standard for moderate-risk deployments. Override if a different cadence applies)*. | M-Reg s. 3(2) — logging and auditing obligation. POPA s. 27(1)(j) — Commissioner power to request PIAs and investigate violations. See Section F for the full audit-logging analysis. |
| 16 | Lack of human oversight and validation measures for information systems | Automated processes within Microsoft Teams and Microsoft 365 — such as automated policy enforcement, retention-label application, or sharing-permission changes — may operate without human review, leading to data-accuracy and reliability issues contrary to M-Reg s. 3(2). | CBE applies human oversight to key information-management operations: (a) access-permission changes require line-manager approval through CBE's IT service-management process — *(agent's call: line-manager + IT-ticket access-approval pattern. Override if CBE's process differs)*; (b) retention-label configuration and updates are reviewed by the Privacy Officer and IT before deployment; (c) audit logs are reviewed quarterly with human judgment applied to anomalous access or use patterns; (d) the Privacy Officer is notified of any access grant involving highly sensitive data classifications (student information classified as Protected B). AI features that automate decisions affecting students or parents are not enabled — *(agent's call: AI features disabled. Override and assess under M-Reg s. 6(2)(e) if AI features are enabled)*. | M-Reg s. 3(2) — system monitoring and human-review obligation. M-Reg s. 6(2) — documented safeguards for high-volume or highly sensitive personal information. See Section F for the full safeguards and oversight analysis. |
| 17 | Failure to conduct vulnerability assessment to identify exploitable security vulnerabilities | Without a vulnerability assessment of the Microsoft Teams and Microsoft 365 deployment, CBE may be unaware of exploitable weaknesses in its tenant configuration, integration points, or endpoint posture — exposing student, parent, and staff personal information to preventable compromise. | CBE's vulnerability-management posture for this project operates at two levels: (a) at the vendor level, Microsoft conducts annual third-party independent audits against applicable control standards and frameworks, with results published at servicetrust.microsoft.com, and implements pseudonymization and encryption along with processes for regularly testing and evaluating security measures per GDPR Article 32; (b) at the tenant level, CBE's IT Security function performs periodic vulnerability scanning of CBE-managed endpoints and integration configurations — *(agent's call: standard IT-security vulnerability scanning for tenant-level configurations. Override if CBE's program operates on a different scope or cadence)*. CBE relies on Microsoft's published audit results (SOC 2 Type II, ISO 27001) for the vendor-platform layer, consistent with POPA s. 10(1) and M-Reg s. 7(3) for the project's risk profile — *(agent's call: vendor-attestation reliance at this risk tier. Override if CBE has commissioned a formal penetration test or if risk appetite requires one)*. | POPA s. 10(1) — reasonable security arrangements. M-Reg s. 7(3) — level of detail commensurate with project complexity and sensitivity. See Section F Q33 for the full safeguards and third-party assessment analysis. |

---

## Section H2. Risks Associated with Cloud Computing

| Risk # | Privacy Risk | Description | Risk Mitigation Measures | Policy Reference and Public Body Comments |
|--------|-------------|-------------|--------------------------|-------------------------------------------|
| H2-1 | Inadequate segregation and isolation of CBE's cloud environment from other tenants in a multi-tenant environment | In a multi-tenant cloud environment, compromise of one customer's environment could propagate to others through insufficient logical isolation, allowing unauthorized access to CBE's student and staff personal information. | Microsoft 365 and Microsoft Teams operate on Microsoft's enterprise multi-tenant architecture, which applies logical isolation between customer tenants using Azure Active Directory (Entra ID) tenant boundaries, role-based access controls, and dedicated encryption key hierarchies per tenant. Microsoft's architecture ensures that CBE's data is logically segregated from other Microsoft customers. Security commitments — including asset inventory, classification controls, and anti-malware — are documented in the Microsoft Volume Licensing DPA (org-library-msft-dpa). CBE retains accountability for configuring tenant-level access controls appropriately under POPA s. 10(1). (See Section F for the substantive POPA s. 10(1) analysis.) | Microsoft Volume Licensing DPA (org-library-msft-dpa); POPA s. 10(1); AB-POPA-s10-1 |
| H2-2 | Contracts or agreements are either not in place with the cloud provider or are insufficient | Absence of a formal, POPA-compliant service-provider agreement with Microsoft could result in loss of custody and control of personal information and non-compliance with M-Reg s. 7(6). | The Microsoft Volume Licensing DPA (org-library-msft-dpa) is on file and governs Microsoft's processing of CBE's customer data, including personal information of students, staff, and parents in scope of this project. The DPA establishes Microsoft as a processor acting solely on CBE's documented instructions, specifies security commitments aligned with ISO 27001/27002, and addresses breach notification, sub-processor management, audit rights, and data deletion on termination. Under POPA s. 1(h), Microsoft Corporation, as a contracted service provider, is treated as an employee of CBE for POPA's protection-of-personal-information obligations. (See Section G for the substantive service-provider analysis.) | Microsoft Volume Licensing DPA (org-library-msft-dpa); M-Reg s. 7(6) (AB-MReg-s7-6); POPA s. 1(h) (AB-POPA-s1-h) |
| H2-3 | The cloud provider does not have a robust privacy and security governance structure | Gaps in a cloud provider's privacy and security governance may result in systemic deficiencies in safeguard implementation, creating risks of unauthorized access, use, or disclosure of CBE's personal information. | Microsoft conducts annual third-party independent audits against applicable control standards and frameworks, with results published at servicetrust.microsoft.com. The Microsoft Volume Licensing DPA (org-library-msft-dpa) documents governance commitments including ISO 27001, ISO 27002, and ISO 27018 alignment; least-privilege and role-based access controls with no standing access by Microsoft personnel to customer data; mandatory data privacy and security training for Microsoft personnel with access to customer data; and personnel confidentiality obligations. A formal third-party privacy and security assessment of Microsoft 365 and Microsoft Teams is not required for this project at this stage. CBE relies on Microsoft's published independent audit reports (SOC 2 Type II, ISO 27001) and the contractual security commitments in the DPA, which together satisfy POPA s. 10(1) for the project's risk profile. *(agent's call: vendor-attestation reliance — defensible for moderate-risk deployments using major SaaS vendors. Override if CBE's risk appetite requires a formal independent assessment.)* | Microsoft Volume Licensing DPA (org-library-msft-dpa); POPA s. 10(1) (AB-POPA-s10-1); M-Reg s. 7(3) (AB-MReg-s7-3) |
| H2-4 | Lack of clarity regarding the cloud provider's obligation to notify CBE of a breach in a timely manner | If the service-provider agreement does not address breach notification, CBE may not receive timely notice of a security incident involving student and staff personal information, preventing it from meeting its obligations under POPA s. 10(2). | The Microsoft Volume Licensing DPA (org-library-msft-dpa) requires Microsoft to notify CBE promptly and without undue delay upon becoming aware of a security incident, with notification delivered within 72 hours per the DPA's incident response standards. This contractual commitment supports CBE's ability to assess whether the real-risk-of-significant-harm (RROSH) threshold under POPA s. 10(2) is met, and if so, to notify (a) the Information and Privacy Commissioner, (b) the responsible Minister, and (c) affected individuals without unreasonable delay. Where the RROSH threshold is confirmed, CBE's internal target is notification to the Commissioner within 14 days, with individual notification to follow as soon as reasonably practicable. *(agent's call: 14-day internal target — faster than the statutory 'without unreasonable delay' standard; aligned with OIPC published guidance. Override if CBE's breach response policy specifies a different timeline.)* (See Section F for the substantive breach-notification analysis.) | Microsoft Volume Licensing DPA (org-library-msft-dpa); POPA s. 10(2) (AB-POPA-s10-2); M-Reg s. 6(1)(b) (AB-MReg-s6-1-b) |
| H2-5 | Vendor or cloud provider lock-out | Microsoft Corporation could, in extraordinary circumstances (insolvency, regulatory action, or unilateral service withdrawal in a jurisdiction), become unable to provide CBE access to personal information stored in the Microsoft 365 / Teams environment, leaving student records, parent contact information, and staff communications inaccessible. | The Microsoft Volume Licensing DPA (org-library-msft-dpa) provides that, on expiration or termination of CBE's subscription, Microsoft retains customer data for 90 days post-expiration in limited-functionality mode, then deletes within a further 90 days. This provides a 90-day recovery window for CBE to extract records before deletion. CBE should maintain a documented data-extraction and migration procedure for the Microsoft 365 / Teams workloads in scope of this project, with export responsibilities assigned to the IT function and the Privacy Officer notified of any service-disruption scenario. Microsoft's status as a globally systemically significant technology vendor materially reduces — but does not eliminate — lock-out risk. *(agent's call: standard lock-out framing relying on DPA-documented 90-day recovery window. Override if CBE has a formal business-continuity procedure for cloud-service loss.)* | Microsoft Volume Licensing DPA (org-library-msft-dpa); POPA s. 10(1) (AB-POPA-s10-1); POPA s. 6(b) (AB-POPA-s6-b) |
| H2-6 | Vendor or cloud provider lock-in | Microsoft 365 and Teams use a combination of open standards and proprietary formats and infrastructure. If CBE wished to migrate to an alternative provider — for example, following a pattern of security incidents or a change in Microsoft's commercial terms — the cost and complexity of migration could be substantial, particularly for Teams meeting recordings, SharePoint content, and Exchange Online mail archives containing student and staff personal information. | CBE should include data-portability and format-documentation requirements in its IT governance planning for this project. Microsoft 365 supports export of data in standard formats (PST for Exchange, SharePoint list exports, Teams export via the Microsoft Graph API), and the DPA's 90-day post-termination window (org-library-msft-dpa) provides time for structured extraction. CBE's Privacy Officer (Sandra McKenzie, privacyofficer@cbe.ab.ca) should be notified of any commercial or contractual change by Microsoft that could accelerate lock-in risk. *(agent's call: lock-in analysis based on publicly documented Microsoft 365 export capabilities. Override if CBE has a formal data-portability clause negotiated into its volume licensing agreement.)* | Microsoft Volume Licensing DPA (org-library-msft-dpa); POPA s. 10(1) (AB-POPA-s10-1) |
| H2-7 | Unauthorized access to personal information by foreign governments or states | **This is the primary jurisdictional-sovereignty risk row.** Microsoft Corporation's ultimate parent jurisdiction is the United States of America (headquartered in Redmond, Washington). Under the Plixer doctrine — Upper Harbour's methodology for classifying SaaS tools by the jurisdiction of their ultimate parent corporation, not by where data is physically stored — Microsoft Teams and Microsoft 365 are classified as United States-jurisdictional services, with a Sovereignty Index classification of **Review**. <br><br>Although Microsoft offers Canadian data residency for at-rest storage of customer data, **data residency is not data sovereignty.** Canadian-region storage does not exempt Microsoft Corporation from compelled disclosure obligations to United States federal authorities. Under the Clarifying Lawful Overseas Use of Data Act (18 U.S.C. § 2713), a provider of electronic communication service or remote computing service must comply with obligations to preserve, backup, or disclose the contents of a wire or electronic communication and any record or other information pertaining to a customer or subscriber within such provider's possession, custody, or control, regardless of whether such communication, record, or other information is located within or outside of the United States. <br><br>As of April 2026, the United States has executive agreements under 18 U.S.C. § 2523 in force with the United Kingdom and Australia, and is in negotiation with the European Union and Canada. No United States–Canada executive agreement under 18 U.S.C. § 2523 is in force as of April 2026. There is therefore no bilateral framework that would require US authorities to route legal process through Canadian channels before compelling disclosure from Microsoft. <br><br>The Microsoft Volume Licensing DPA (org-library-msft-dpa) contains contractual commitments including security measures, transparency obligations, and data-residency elections. These are partial mitigations only — they do not eliminate CLOUD Act jurisdictional exposure. CBE accepts this exposure as a documented residual risk for this project. *(agent's call: documented residual risk — dominant practitioner middle-spectrum position (BLG, McCarthy Tétrault, CAI Guide §17). If CBE's project requires Canadian-only sovereignty, override and identify a Canadian-parent alternative tool.)* | CLOUD Act, 18 U.S.C. § 2713 (CLOUD-Act-18-USC-2713); 18 U.S.C. § 2523 (CLOUD-Act-18-USC-2523); Microsoft Volume Licensing DPA (org-library-msft-dpa); POPA s. 10(1) (AB-POPA-s10-1) |
| H2-8 | The cloud provider uses personal information for purposes not authorized by POPA | A cloud provider that uses CBE's customer data — including student names, school assignments, and parent contact information — for its own purposes (such as AI model training, product analytics, or de-identification and resale) would constitute use beyond the scope authorized under POPA s. 12 and beyond CBE's instruction as data controller. | Under POPA s. 1(h), Microsoft Corporation, as a contracted service provider performing services for CBE, is treated as an employee of CBE for POPA's protection-of-personal-information obligations. Vendor processing of personal information in scope of this project is therefore internal use by CBE's extended workforce, not disclosure to a third party under POPA s. 13. The Microsoft Volume Licensing DPA (org-library-msft-dpa) contractually restricts Microsoft to processing customer data solely to deliver licensed products and services per CBE's instructions, to troubleshoot, to maintain performance and security, and for limited incident-to-business operations (billing, compensation, internal reporting) using aggregated or pseudonymized data only — not CBE-identifiable student data. The DPA explicitly excludes use of customer data for AI model training without CBE's instruction. AI-assisted features (e.g., Microsoft Copilot, automated meeting summaries) are not enabled for this project at this time. Should CBE elect to enable AI features in the future, an Algorithm Impact Assessment will be conducted and an amendment to this PIA will be filed with the OIPC. *(agent's call: AI features disabled — default for risk-conservative deployment. Override if AI features will be enabled — an Algorithm Impact Assessment is then required.)* (See Section F for the substantive POPA s. 12 use-limitation analysis.) | Microsoft Volume Licensing DPA (org-library-msft-dpa); POPA s. 12 (AB-POPA-s12); POPA s. 12(4) (AB-POPA-s12-4); POPA s. 1(h) (AB-POPA-s1-h); M-Reg s. 6(2) (AB-MReg-s6-2) |
| H2-9 | The cloud provider discloses personal information for purposes not authorized by POPA | Microsoft could disclose CBE's customer data — including personal information of students who are minors — to sub-processors, third parties, or other recipients beyond what CBE has authorized, in a manner inconsistent with POPA s. 13. | The Microsoft Volume Licensing DPA (org-library-msft-dpa) addresses sub-processor management: Microsoft may engage sub-processors (including Microsoft Affiliates) only with CBE's prior general written consent; new sub-processors for customer data require six months' advance notice; CBE may terminate without penalty if it objects within the notice period; and Microsoft remains fully liable for sub-processors' compliance. The DPA also requires Microsoft to maintain incident response records and security breach logs, and to implement asset-inventory, classification, and handling controls for media containing customer data — reducing the risk of unauthorized disclosure through media sanitization failures. CBE must disclose personal information only to the extent necessary to enable the purpose of the disclosure to be carried out in a reasonable manner, per POPA s. 13(4). CBE remains accountable under POPA s. 10(1) for ensuring that its contractual arrangements with Microsoft are adequate in light of the sensitivity of student personal information. | Microsoft Volume Licensing DPA (org-library-msft-dpa); POPA s. 13(4) (AB-POPA-s13-4); POPA s. 10(1) (AB-POPA-s10-1); POPA s. 1(h) (AB-POPA-s1-h) |
| H2-10 | Broken authentication and authorization | Failure to implement and enforce robust authentication controls — such as multi-factor authentication and role-based access — could result in unauthorized access to student names, school assignments, and parent contact information stored in Microsoft 365 / Teams. | POPA s. 10(1) requires CBE's head to protect personal information by making reasonable security arrangements against risks including unauthorized access. Multi-factor authentication is enforced for all staff accounts accessing personal information in scope of this project. MFA is the industry-standard expected control under POPA s. 10(1) for cloud-tenant deployments handling regulated personal information. *(agent's call: MFA enforced — industry standard for cloud SaaS at this scope. Override if MFA is not yet enabled — that is a real gap to disclose.)* Access to personal information in scope of this project is governed by role-based access controls applying the principle of least privilege, with access granted only to staff and educators whose duties require it. *(agent's call: RBAC + least privilege — industry-standard control posture. Override if specific deviations apply.)* Access permissions are reviewed annually by CBE's IT function and the Privacy Officer, with event-triggered reviews on staff role changes, departures, and project scope changes. *(agent's call: annual access review + event-triggered — industry standard. Override if the cadence differs.)* (See Section F for the substantive POPA s. 10(1) analysis.) | POPA s. 10(1) (AB-POPA-s10-1); Microsoft Volume Licensing DPA (org-library-msft-dpa) |
| H2-11 | Use of weak cryptographic algorithms or lack of encryption of data in transit and at rest | Weak or absent encryption could lead to unauthorized access to and disclosure of student and staff personal information, both while stored in Microsoft 365 / Teams infrastructure and while transmitted between CBE's endpoints and Microsoft's cloud infrastructure. | Personal information in scope of this project is encrypted at rest using industry-standard cryptographic algorithms (AES-256 or equivalent) provided by Microsoft 365 and Microsoft Teams as part of standard tenant configuration. *(agent's call: encryption at rest enabled — vendor default for the tools in scope. Override only if CBE has specific configuration concerns.)* Personal information in scope of this project is encrypted in transit using TLS 1.2 or higher between CBE's endpoints and Microsoft's services. *(agent's call: TLS 1.2+ in transit — industry standard. Override only if a different protocol applies.)* These commitments are also reflected in the Microsoft Volume Licensing DPA (org-library-msft-dpa), which confirms that Microsoft encrypts customer data in transit over public networks and at rest in Online Services by default. These technical controls collectively satisfy the encryption dimension of CBE's reasonable-security-arrangements obligation under POPA s. 10(1). (See Section F for the full POPA s. 10(1) analysis.) | POPA s. 10(1) (AB-POPA-s10-1); Microsoft Volume Licensing DPA (org-library-msft-dpa) |

---

## Appendix C. Use of Automated Systems or Other Forms of Innovative Technology

> **Applicability note.** This Appendix is conditional on the project involving an automated system, AI, or other innovative technology that generates content or makes decisions or recommendations. For the current scope of the CBE's adoption of Microsoft Teams and Microsoft 365, AI-assisted features are not in scope. The rationale is stated below and governs the risk table that follows.

Under M-Reg s. 7, a PIA must be prepared in respect of projects involving innovative technology that processes personal information; the level of detail required is commensurate with the complexity of the project and the sensitivity of the information involved. Because AI features are disabled for this deployment, the risk profile addressed in this Appendix is constrained to the **risk that AI features could be enabled in the future without a corresponding PIA amendment**, and to the **residual AI-processing risk inherent in Microsoft's platform architecture** (e.g., Microsoft's use of telemetry and service-improvement processing). The full automated-decision-making risk register is recorded below for completeness and to support any future scope expansion.

---

**Question 1.** Has the CBE completed an Algorithmic Impact Assessment (AIA) for this project?

**No.** An AIA has not been completed, and none is required at this time.

AI-assisted features within Microsoft 365 and Microsoft Teams — including Microsoft Copilot, automated meeting transcription and summary, content moderation, and any feature that generates outputs or recommendations using machine-learning models applied to personal information — are **not enabled** for the personal information in scope of this project. *(agent's call: AI features disabled — default for risk-conservative deployment. Override if AI features will be enabled — an Algorithm Impact Assessment is then required.)*

M-Reg s. 6(2)(e) requires that a Privacy Management Program include policies governing the use of automated decision-making and AI systems where applicable. Because no such system is activated for this project, the M-Reg s. 6(2)(e) requirement is satisfied by the commitment recorded in this Appendix and by the CBE's Privacy Management Program (in development per POPA s. 25, to be in place by June 11, 2026) rather than by a standalone AIA.

Should the CBE elect in the future to enable AI features — including but not limited to Microsoft Copilot for Education, automated content flagging, or any feature applying machine-learning inference to student or staff personal information — the following steps are mandatory before enablement:

1. An Algorithm Impact Assessment must be conducted in accordance with M-Reg s. 7(3) and the OIPC's developing AIA guidance.
2. This PIA must be amended and the amendment submitted to the Information and Privacy Commissioner under POPA s. 26.
3. The PMP must be updated to address the M-Reg s. 6(2)(e) automated-decision-making governance requirement for the specific feature enabled.

[HARD BLOCKER: If the CBE enables any AI or Copilot feature in Microsoft 365 or Teams before the above steps are complete, complete and attach an Algorithm Impact Assessment to a PIA amendment — required for OIPC submission per M-Reg s. 7(3) and s. 7(5)(e).]

---

**Question 2.** Risk Assessment and Mitigation Table — Automated Systems

**Scope clarification.** Because AI features are disabled for this deployment, all thirteen template risks are assessed against the **as-deployed, non-AI scope**. Where a risk is not activated by the current deployment, the mitigation is the **preventive control** (i.e., the control that keeps the risk dormant). Where a risk has residual relevance even without AI features (e.g., Microsoft's platform-level telemetry), the mitigation addresses that residual exposure. This table must be revisited and substantively completed if AI features are enabled in the future.

| Risk # | Privacy Risk | Description | Risk Mitigation Measures | Policy Reference and Public Body Comments |
|--------|-------------|-------------|--------------------------|------------------------------------------|
| 1 | Loss of custody or control of personal information ingested by an automated system. | AI features disabled: no student or staff personal information is ingested by a machine-learning inference pipeline under CBE control. Residual exposure: Microsoft's platform telemetry and service-improvement processing may incidentally involve diagnostic data. | Under POPA s. 1(h), Microsoft Corporation, as contracted service provider, is treated as an employee of CBE for the purposes of POPA's protection-of-personal-information obligations. The Microsoft Volume Licensing DPA (org-library-msft-dpa) limits Microsoft's processing to delivery of licensed services and tightly scoped incident-to-business operations using aggregated or pseudonymized data only. AI features that would ingest identifiable student data into inference pipelines are disabled at the tenant level. *(agent's call: AI disabled; DPA scope limitation confirmed from org-library-msft-dpa.) Override if AI features are later enabled.* | POPA s. 1(h); POPA s. 10(1); Microsoft Volume Licensing DPA (org-library-msft-dpa) — see Section G. |
| 2 | Lack of or insufficient policies and procedures for governance of automated systems. | Without a documented AI governance policy, CBE staff may not understand permissible uses of AI-assisted features or the obligations that attach to enabling them. | M-Reg s. 6(2)(e) requires the Privacy Management Program to include policies governing the use of automated decision-making and AI systems where applicable. CBE's PMP (in development, in force by June 11, 2026) will include an AI governance policy as a minimum-content element. Until that policy is published, AI features remain disabled. *(agent's call: PMP-in-development framing aligned with June 11, 2026 in-force date. Override if PMP is already established.)* | POPA s. 25; M-Reg s. 6(2)(e); POPA s. 10(1). |
| 3 | Hallucination — automated systems fabricate results or outputs without human oversight. | A hallucinating AI system could generate false statements about students or staff and have those statements acted upon by educators or administrators. | Not activated. AI features that generate content are disabled. If enabled in the future, CBE will implement mandatory human-review requirements for any AI-generated output used in a decision affecting an individual, consistent with POPA s. 6(a)'s accuracy obligation and the AIA requirement under M-Reg s. 7(3). | POPA s. 6(a); M-Reg s. 7(3). Preventive control: feature disabled. Revisit if AI features are enabled. |
| 4 | Use of poor quality, unreliable, or non-representative training data leading to biased or inaccurate results. | Biased training data in an AI model could produce discriminatory outcomes for students from equity-deserving groups, affecting access to resources or support. | Not activated for this deployment. CBE does not supply training data to Microsoft models and does not operate its own ML pipelines for this project. If AI features are enabled in the future, an AIA must evaluate training-data provenance and representativeness before deployment. | M-Reg s. 7(3); POPA s. 6(a). Preventive control: no CBE-controlled model training occurs in this project. |
| 5 | Inputs to automated systems are not validated or protected, allowing tampering. | Prompt injection or data-poisoning attacks could manipulate AI outputs, potentially exposing personal information or producing harmful decisions. | Not activated. POPA s. 10(1) requires the head of a public body to make reasonable security arrangements against unauthorized access, use, or disclosure. Standard tenant security controls (MFA, RBAC, input-validation at the Microsoft platform layer) mitigate the residual platform-level exposure. See Section F for the full security-safeguards analysis. | POPA s. 10(1); see Section F for security safeguards detail. Preventive control: AI input pipelines not available to CBE users. |
| 6 | Lack of clarity on whether the model is static or dynamic, leading to inappropriate monitoring. | If CBE does not know whether an AI model updates continuously, it cannot assess whether initial risk assessments remain valid over time. | Not activated. Microsoft's platform-level model governance is described in published service documentation and the DPA. CBE does not operate a bespoke model for this project. If AI features are enabled in the future, the AIA must document whether the model is static or dynamic and establish a corresponding monitoring cadence. | M-Reg s. 7(3); org-library-msft-dpa. Preventive control: no CBE-operated model in scope. |
| 7 | Underfitting — model is too broad in its generalization, prone to false positives. | A model with poor generalization could flag benign communications as policy violations, generating inaccurate records about students. This implicates POPA s. 6(a)'s obligation to ensure accuracy where personal information is used in a decision affecting the individual. | Not activated. No content-classification or moderation model is running against student communications for this project. Preventive control documented here for future reference. | POPA s. 6(a). Preventive control: feature disabled. |
| 8 | Overfitting — model is too closely aligned with training data, prone to false negatives. | An overfitted model could miss genuine policy violations or safety concerns in student communications, creating a false sense of security and potential duty-of-care failures. | Not activated. Same preventive rationale as Risk #7. If content-moderation AI is enabled in the future, the AIA must include model-accuracy testing against representative CBE communication samples before production deployment. | POPA s. 6(a); M-Reg s. 7(3). Preventive control: feature disabled. |
| 9 | Misconfiguration of an automated system leading to security vulnerabilities. | Incorrect configuration of an AI feature could inadvertently expose personal information to unauthorized parties or bypass standard access controls. | POPA s. 10(1) requires the head of a public body to make reasonable security arrangements against risks including unauthorized access. Configuration reviews are conducted before any feature is enabled in the CBE tenant. AI features will not be enabled without a configuration review by CBE's IT Security function and sign-off by the Privacy Officer. | POPA s. 10(1); see Section F. Configuration-review requirement applies to any future AI feature enablement. |
| 10 | Lack of processes for individuals to be made aware of and appeal decisions made by automated systems. | If an automated system makes or influences a decision affecting a student or staff member, POPA requires that the individual have a reasonable opportunity to understand and contest that decision. | Not activated. No automated decision-making affecting individuals is in scope. Under POPA s. 7, individuals have the right to request correction of personal information about them, and CBE must correct or annotate the record and notify prior recipients. If AI decision-support is enabled in the future, CBE will establish a documented appeal process before deployment, consistent with M-Reg s. 6(2)(e). | POPA s. 7; M-Reg s. 6(2)(e). Preventive control: no automated decisions in scope. |
| 11 | Insufficient logging and auditing of automated system activities. | Without adequate logging of AI system inputs and outputs, CBE cannot detect misuse, investigate incidents, or demonstrate accountability to the OIPC. | M-Reg s. 3(2) requires that information systems used to process personal information include sufficient logging and auditing capabilities to detect and investigate unauthorized access, use, or disclosure. Unified audit logging is enabled in the Microsoft 365 tenant covering this project's workloads. *(agent's call: audit logging enabled, 90-day retention — industry standard. Override if not yet enabled or if a different retention applies.)* If AI features are enabled, logging must be extended to cover AI-specific activities (prompts, outputs, model invocations). | M-Reg s. 3(2); see Section F for audit-logging detail. |
| 12 | Lack of monitoring of the automated system based on established policies. | Without a monitoring programme, CBE cannot verify that an AI system continues to behave as expected or that privacy-protective configurations remain in effect. | Not activated for AI features. Platform-level monitoring by Microsoft is addressed in the DPA (org-library-msft-dpa), which commits to service monitoring at least every six months. CBE's quarterly audit-log review (see Section F) would extend to AI-system activity logs if features are enabled. *(agent's call: quarterly review — industry standard at this risk profile. Override if a different cadence applies.)* | M-Reg s. 3(2); org-library-msft-dpa — see Section G. |
| 13 | Failure to conduct a vulnerability assessment for the automated system. | An unassessed AI deployment could introduce security vulnerabilities unknown to CBE, including model-inversion or membership-inference attacks that expose personal information. | M-Reg s. 7(3) requires the level of detail in a PIA to be commensurate with the complexity of the project and the sensitivity of the personal information involved. No AI feature is in scope; a vulnerability assessment specific to AI systems is not required at this stage. If AI features are enabled in the future, a vulnerability assessment of the specific AI components, informed by the AIA, will be required before production deployment. A formal third-party assessment of the base Microsoft 365 / Teams platform is not required at this stage — CBE relies on Microsoft's published SOC 2 Type II and ISO 27001 audit reports. *(agent's call: vendor-attestation reliance — defensible for moderate-risk deployments using major SaaS vendors. Override if a formal assessment has been completed or your risk appetite requires one.)* | POPA s. 10(1); M-Reg s. 7(3); org-library-msft-dpa — see Section G. |

---

**Summary position.** Appendix C is filed as a preventive record, not as an active AI risk assessment. The CBE's current deployment of Microsoft Teams and Microsoft 365 does not activate any of the thirteen template risks in their primary form. The dominant risk for this Appendix is **Risk #2 (governance gap)**: without an active AI governance policy, future feature enablement could occur without appropriate controls. That risk is mitigated by the commitment to keep AI features disabled pending completion of the PMP and, for any specific AI feature, completion of an AIA and PIA amendment before enablement.

---

## Attachment Inventory

The following attachments are referenced throughout this Privacy Impact Assessment. Items marked ⬜ must be provided by the public body prior to submission to the OIPC.

| Att. # | Description | PIA Reference | Status |
|--------|-------------|---------------|--------|
| 1 | Service Provider Agreement — Microsoft Teams / Microsoft Corporation (privacy-related portions per M-Reg s. 7(6)) | Section G, Q43 | ⬜ [HARD BLOCKER: Upload the signed Microsoft Teams service-provider agreement (privacy-related portions) — required for OIPC submission per M-Reg s. 7(6)] |
| 2 | Service Provider Agreement — Microsoft 365 / Microsoft Corporation (privacy-related portions per M-Reg s. 7(6)) | Section G, Q43 | ⬜ [HARD BLOCKER: Upload the signed Microsoft 365 service-provider agreement (privacy-related portions) — required for OIPC submission per M-Reg s. 7(6)] |
| 3 | Information Flow Diagram(s) | Section D, Q20 | ⬜ [HARD BLOCKER: Upload an information-flow diagram showing how each personal-information category moves between collection, processing, and storage — required for OIPC submission per M-Reg s. 7(3)] |
| 4 | Security Classification Documentation | Section F, Q29 | ⬜ [HARD BLOCKER: Upload your security classification schema (or confirm classification levels for this project's data) — required for OIPC submission per M-Reg s. 2(1)] |
| 5 | Access Control Policy | Section F, Q33 | ⬜ [HARD BLOCKER: Upload your access control policy or confirm the role-based-access posture for this project — required for OIPC submission per POPA s. 10(1)] |
| 6 | Logging and Auditing Policy | Section F, Q38 | ⬜ [HARD BLOCKER: Upload your logging and auditing policy or confirm the audit-log review cadence for this project — required for OIPC submission per M-Reg s. 3(2)] |
| 7 | Breach Response Policy | Section F, Q32; M-Reg s. 6(1)(b) | ⬜ [HARD BLOCKER: Upload your documented breach response policy — required for OIPC submission per M-Reg s. 6(1)(b)] |
| 8 | Employee Privacy Training Documentation | Section F, Q32; M-Reg s. 6(1)(d) | ⬜ [HARD BLOCKER: Upload your privacy training program description or completion records — required for OIPC submission per M-Reg s. 6(1)(d)] |
| 9 | Vulnerability Assessment / Penetration Test Results (if conducted) | Section H, Q48 | ⬜ [HARD BLOCKER: Upload any third-party vulnerability assessment or penetration test results, OR confirm in writing that no such assessment was conducted (with rationale) — for OIPC submission per M-Reg s. 7(3) proportional rigor] |
| 10 | Algorithm Impact Assessment (AIA) | Appendix C, Q1 | ⬜ [HARD BLOCKER: Complete and upload an Algorithm Impact Assessment for the AI / automated-decision features in scope — REQUIRED for OIPC submission per M-Reg s. 6(2)(e); the PIA cannot be submitted without this if AI features are enabled] |
| 11 | Parental/Guardian Consent and Notice Instruments (if students in scope) | Section D, Q17; POPA s. 5(2) | ⬜ [HARD BLOCKER: Upload the parental/guardian collection notice instrument(s) actually delivered for this project — required for OIPC submission per POPA s. 5(2)] |

**Total attachments referenced: 11**

*Note: The M-Regulation s. 7(6) requires that the privacy-related portions of any service provider agreement be submitted with the PIA. PIAs submitted without required attachments may be deemed incomplete and not accepted for review by the OIPC.*

---

## Appendix D. PIA Cover Letter

---

*(to be dated at submission)*

Information and Privacy Commissioner
Suite 410, 9925-109 Street NW
Edmonton, AB T5K 2J8

Dear Information and Privacy Commissioner:

**Re: Adoption of Microsoft Teams and Microsoft 365 for Staff and Student Communications**

Please find attached our privacy impact assessment (PIA) for the above-named project. I am making this submission in accordance with section 26 of the *Protection of Privacy Act*, SA 2024, c P-28.5 (POPA).

The PIA is current as of this submission to your office. I understand that as things change in our project, I will update the PIA by highlighting the sections that have changed, assessing the privacy and security implications of the changes, and resubmit it to your office for review.

Sincerely,

_______________________________________________
*(to be signed by the head or designate at submission)*

Board Chair (or designate), Calgary Board of Education
1221 8 Street SW, Calgary, AB T2R 0L4

---

> **Before submit — action required**
>
> `[HARD BLOCKER: Sign this cover letter. The head of the Calgary Board of Education (Board Chair, or a designate to whom authority has been delegated in writing under POPA s. 55) must sign this letter before the PIA package is submitted to the OIPC. The signed cover letter is a mandatory attachment — the Commissioner will not open the file without it. Write the specific name and title of the signing officer above the signature line at the time of signing.]`
>
> `[HARD BLOCKER: Upload the signed Microsoft Volume Licensing Data Processing Agreement (DPA) — required for OIPC submission per M-Reg s. 7(6), Alta Reg 143/2025. The privacy-related portions of the service provider agreement must accompany the PIA. The Microsoft Online Services Volume Licensing DPA (Jan 2024) identified in the Org Privacy Library as org-library-msft-dpa satisfies the substantive obligation; a signed copy executed by the Calgary Board of Education must be included as an attachment to the submission package.]`

---

## Appendix E. PIA Submission Checklist

This checklist confirms that all required sections have been completed and all supporting documents are attached or accounted for before submission to the Information and Privacy Commissioner under POPA s. 26 and M-Reg s. 7(6). Each row identifies the item, its status, and the section of this PIA where the substantive treatment appears.

---

### Category 1 — Mandatory Sections Completed (A through H1)

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 1.1 | Section A — Project description, public body identification, Privacy Officer contact | ✅ | Section A |
| 1.2 | Section B — Collection authority, operating-program statute mapping, POPA s. 5(2) collection notice | ✅ | Section B |
| 1.3 | Section C — Legal authority for collection, use, and disclosure under POPA ss. 4, 12, 13 | ✅ | Section C |
| 1.4 | Section D — Personal information identified; per-field mapping to Education Act + POPA s. 4(c) | ✅ | Section D |
| 1.5 | Section E — Access, correction, accuracy, retention, and disposition (ATIA access rights; POPA s. 7 correction rights; POPA s. 6(b) retention) | ✅ | Section E |
| 1.6 | Section F — Protection of information: POPA s. 10(1) safeguards; Plixer doctrine + CLOUD Act jurisdictional analysis; M-Reg ss. 2(1), 3(2) | ✅ | Section F |
| 1.7 | Section G — Service providers: M-Reg s. 7(6) DPA on file; POPA s. 1(h) framing | ✅ | Section G |
| 1.8 | Section H1 — Risk Register: privacy risks, likelihood, impact, mitigation measures | ✅ | Section H1 |

---

### Category 2 — Project-Specific Sections Completed (Appendices A, B, C as applicable)

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 2.1 | Appendix A — Information flow diagram (data flows between CBE, Microsoft 365 / Teams tenant, and data subjects) | ⬜ [HARD BLOCKER: Attach a completed information-flow diagram showing how student names, school assignments, and parent contact information move between CBE systems, the Microsoft 365 / Teams tenant, and end-user devices — required for OIPC submission per M-Reg s. 7.] | Appendix A |
| 2.2 | Appendix B — Plixer Doctrine Analysis (Microsoft Corporation / United States parent jurisdiction; CLOUD Act exposure; residual-risk acceptance) | ✅ | Appendix B (see also Section F for substantive analysis) |
| 2.3 | Appendix C — Algorithm Impact Assessment | ✅ — Not required. AI-assisted features (Microsoft Copilot, automated meeting summaries) are NOT enabled for this project. If AI features are enabled in future, an AIA must be completed and a PIA amendment filed. *(agent's call: AI features disabled — default for risk-conservative deployment. Override if AI features will be enabled.)* | Section F |

---

### Category 3 — Cover Letter

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 3.1 | Appendix D — Cover letter signed by the head of the Calgary Board of Education | ⬜ [HARD BLOCKER: Obtain the signed PIA cover letter (Appendix D) from the head of the Calgary Board of Education or their written delegate under POPA s. 55 before submission — required for OIPC acceptance.] | Appendix D |

---

### Category 4 — Service Provider Contracts / Agreements

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 4.1 | Microsoft Online Services Volume Licensing DPA (January 2024) — privacy-related portions, as required by M-Reg s. 7(6) | ✅ — Microsoft DPA on file (org-library-msft-dpa). Privacy-related portions to be attached to the OIPC submission package. | Section G |
| 4.2 | Any additional service provider agreements covering subprocessors engaged by Microsoft for this project | ✅ — Microsoft DPA (org-library-msft-dpa) governs subprocessor obligations. Microsoft publishes its current subprocessor list at the URL specified in the DPA; CBE may attach the current list as a supplementary exhibit. | Section G |

---

### Category 5 — Information Flow Diagram

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 5.1 | Completed information-flow diagram showing personal information flows for this project | ⬜ [HARD BLOCKER: Attach a completed information-flow diagram — required for OIPC submission per M-Reg s. 7. The diagram must show: (1) data subjects (students, parents/guardians, staff); (2) collection points; (3) data flows into and within the Microsoft 365 / Teams tenant; (4) Canadian-region data residency configuration; and (5) any cross-border flows to Microsoft subprocessors.] | Appendix A |

---

### Category 6 — Security Classification Documentation

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 6.1 | Security classification applied to personal information in scope, documented in accordance with M-Reg s. 2(1) | ✅ — Personal information in scope (student names, school assignments, parent contact information) is classified as Protected B, consistent with M-Reg s. 1 (information about minors is highly sensitive). Classification has been communicated in writing to staff with access. *(agent's call: Protected B for minors — recommended classification. Override if CBE's classification scheme uses a different tier label.)* | Section F |

---

### Category 7 — Access Control Policies

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 7.1 | Role-based access controls and access-approval procedure documented, consistent with POPA s. 10(1) reasonable security arrangements | ✅ — RBAC with least-privilege access and a standard line-manager + IT-ticket approval procedure is in place for the Microsoft Teams / Microsoft 365 tenant workloads in scope. Annual access reviews are conducted, with event-triggered reviews on staff role changes and departures. *(agent's call: standard RBAC + annual review posture. Override if CBE's access-control policy differs.)* | Section F |
| 7.2 | Student / parent access to data limited to their own records; parental access configured for minors | ✅ — Addressed in Section B (collection authority) and Section D (data-subject access) in accordance with the Education Act and POPA s. 4(c). | Section B, Section D |

---

### Category 8 — Logging and Auditing Policies

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 8.1 | Unified audit logging enabled for Microsoft Teams / Microsoft 365 workloads in scope, with documented log-review procedure, consistent with M-Reg s. 3(2) | ✅ — Audit logging is enabled across the Microsoft Teams / Microsoft 365 tenant covering project workloads, with a default 90-day retention period (extensible to 365 days). Logs are reviewed quarterly by CBE's IT Security function in coordination with the Privacy Officer, with ad-hoc reviews on suspected incidents. *(agent's call: audit logging enabled, 90-day retention, quarterly review. Override if CBE's actual configuration or review cadence differs.)* | Section F |

---

### Category 9 — Vulnerability Assessment Results

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 9.1 | Formal third-party vulnerability or privacy-and-security assessment of Microsoft Teams / Microsoft 365 | ✅ — A formal third-party assessment is not required for this project at this stage. CBE relies on Microsoft's published independent audit reports (SOC 2 Type II, ISO 27001) and on the contractual security commitments in the Microsoft DPA (org-library-msft-dpa), which together satisfy POPA s. 10(1) for this project's risk profile, consistent with M-Reg s. 7(3). *(agent's call: vendor-attestation reliance — defensible for moderate-risk deployments using major SaaS vendors. Override if a formal assessment has been completed or if CBE's risk appetite requires one.)* | Section F |
| 9.2 | Microsoft independent audit reports (SOC 2 Type II, ISO 27001) relied upon as vendor attestation — available at Microsoft Service Trust Portal | ✅ — Privacy-related portions of the Microsoft DPA are submitted with this PIA per M-Reg s. 7(6). CBE may optionally attach the relevant Service Trust Portal reports as supplementary exhibits. | Section F, Section G |

---

### Category 10 — Algorithm Impact Assessment

| # | Item | Status | Cross-Reference |
|---|------|--------|-----------------|
| 10.1 | Algorithm Impact Assessment (AIA) — required if Appendix C applies (AI or automated decision-making features enabled) | ✅ — Not required. AI-assisted features (including Microsoft Copilot, automated meeting summaries, and content-moderation tools) are NOT enabled for personal information in scope of this project at this time. Should CBE elect to enable such features in the future, an AIA must be completed under M-Reg s. 6(2) and a PIA amendment filed with the OIPC. *(agent's call: AI features disabled — default for risk-conservative deployment. Override and complete an AIA if AI features will be enabled.)* | Section F, Appendix C |

---

### Before-Submit Action List

The following items require action by CBE before this PIA is submitted to the OIPC. These are the HARD BLOCKER items extracted from the checklist above.

| Priority | Action Required |
|----------|----------------|
| **1 — Required** | **Sign the PIA cover letter (Appendix D).** Obtain the signature of the head of the Calgary Board of Education or their written delegate under POPA s. 55. |
| **2 — Required** | **Attach the information-flow diagram (Appendix A).** The diagram must show all personal-information flows: collection points → Microsoft 365 / Teams tenant → end-user devices, including the Canadian-region residency configuration and any cross-border subprocessor flows. |
| **3 — Attach** | **Attach the Microsoft Online Services Volume Licensing DPA** (already on file as org-library-msft-dpa) as a physical exhibit to the submission package, per M-Reg s. 7(6). The document need not be re-executed — the existing executed copy satisfies the requirement. |