var regulatoryMap = {
  "AB": {
    province: "Alberta",
    laws: [
      { name: "PIPA", fullName: "Personal Information Protection Act", scope: "private", notes: "Substantially similar to PIPEDA. Covers private-sector organizations in Alberta." },
      { name: "HIA", fullName: "Health Information Act", scope: "health", notes: "Governs health information held by custodians (hospitals, pharmacies, physicians)." },
      { name: "FOIP", fullName: "Freedom of Information and Protection of Privacy Act", scope: "public", notes: "Applies to provincial government bodies." }
    ],
    authority: { name: "Office of the Information and Privacy Commissioner of Alberta", abbr: "OIPC AB", url: "https://www.oipc.ab.ca" },
    crossBorderRule: "Adequate protection required. Organizations must use contractual or other means to ensure comparable level of protection.",
    piaRequired: "Recommended but not explicitly mandatory for all transfers under PIPA. Mandatory for health information under HIA.",
    maxPenalty: "Up to $100,000 for individuals; $500,000 for organizations under PIPA."
  },
  "BC": {
    province: "British Columbia",
    laws: [
      { name: "PIPA BC", fullName: "Personal Information Protection Act", scope: "private", notes: "Substantially similar to PIPEDA. Covers private-sector organizations in BC." },
      { name: "FIPPA", fullName: "Freedom of Information and Protection of Privacy Act", scope: "public", notes: "Requires personal info held by public bodies to be stored and accessed only in Canada." }
    ],
    authority: { name: "Office of the Information and Privacy Commissioner for British Columbia", abbr: "OIPC BC", url: "https://www.oipc.bc.ca" },
    crossBorderRule: "FIPPA requires public body data to remain in Canada. PIPA requires comparable protection via contractual safeguards for private sector.",
    piaRequired: "Recommended. Mandatory for public bodies under FIPPA for new programs or systems.",
    maxPenalty: "Up to $100,000 for individuals; $500,000 for organizations under PIPA BC."
  },
  "MB": {
    province: "Manitoba",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies as Manitoba has no substantially similar private-sector law." },
      { name: "FIPPA MB", fullName: "Freedom of Information and Protection of Privacy Act", scope: "public", notes: "Applies to Manitoba government bodies." },
      { name: "PHIA", fullName: "Personal Health Information Act", scope: "health", notes: "Governs personal health information in Manitoba." }
    ],
    authority: { name: "Manitoba Ombudsman", abbr: "MB Ombudsman", url: "https://www.ombudsman.mb.ca" },
    crossBorderRule: "PIPEDA applies. Organizations must ensure comparable protection through contractual means.",
    piaRequired: "Recommended under PIPEDA. Required for health information under PHIA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation. PHIA: up to $50,000."
  },
  "NB": {
    province: "New Brunswick",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies as NB has no substantially similar private-sector law." },
      { name: "RTIPPA", fullName: "Right to Information and Protection of Privacy Act", scope: "public", notes: "Applies to NB government bodies." },
      { name: "PHIPAA", fullName: "Personal Health Information Privacy and Access Act", scope: "health", notes: "Governs personal health information in NB." }
    ],
    authority: { name: "Office of the Access to Information and Privacy Commissioner", abbr: "NB OAIPC", url: "https://www.gnb.ca/legis/business/currentsession/57/57-3/LegDoc/Eng/PrivComm.htm" },
    crossBorderRule: "PIPEDA applies. Contractual safeguards required.",
    piaRequired: "Recommended under PIPEDA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation."
  },
  "NL": {
    province: "Newfoundland and Labrador",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies." },
      { name: "ATIPPA", fullName: "Access to Information and Protection of Privacy Act", scope: "public", notes: "Applies to NL public bodies." },
      { name: "PHIA NL", fullName: "Personal Health Information Act", scope: "health", notes: "Governs personal health information in NL." }
    ],
    authority: { name: "Office of the Information and Privacy Commissioner of NL", abbr: "OIPC NL", url: "https://www.oipc.nl.ca" },
    crossBorderRule: "PIPEDA applies for private sector.",
    piaRequired: "Recommended under PIPEDA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation."
  },
  "NS": {
    province: "Nova Scotia",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies." },
      { name: "FOIPOP", fullName: "Freedom of Information and Protection of Privacy Act", scope: "public", notes: "Applies to NS public bodies." },
      { name: "PHIA NS", fullName: "Personal Health Information Act", scope: "health", notes: "Governs personal health information in NS. Strict rules on electronic health records." }
    ],
    authority: { name: "Office of the Information and Privacy Commissioner for Nova Scotia", abbr: "OIPC NS", url: "https://oipc.novascotia.ca" },
    crossBorderRule: "PIPEDA applies for private sector.",
    piaRequired: "Recommended under PIPEDA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation."
  },
  "NT": {
    province: "Northwest Territories",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies." },
      { name: "ATIPP", fullName: "Access to Information and Protection of Privacy Act", scope: "public", notes: "Applies to NWT public bodies." }
    ],
    authority: { name: "Information and Privacy Commissioner of the NWT", abbr: "IPC NWT", url: "https://www.assembly.gov.nt.ca" },
    crossBorderRule: "PIPEDA applies for private sector.",
    piaRequired: "Recommended under PIPEDA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation."
  },
  "NU": {
    province: "Nunavut",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies." },
      { name: "ATIPP NU", fullName: "Access to Information and Protection of Privacy Act", scope: "public", notes: "Applies to Nunavut public bodies." }
    ],
    authority: { name: "Information and Privacy Commissioner of Nunavut", abbr: "IPC NU", url: "https://www.assembly.nu.ca" },
    crossBorderRule: "PIPEDA applies for private sector.",
    piaRequired: "Recommended under PIPEDA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation."
  },
  "ON": {
    province: "Ontario",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies as Ontario has no substantially similar private-sector law." },
      { name: "FIPPA ON", fullName: "Freedom of Information and Protection of Privacy Act", scope: "public", notes: "Applies to Ontario provincial government bodies." },
      { name: "MFIPPA", fullName: "Municipal Freedom of Information and Protection of Privacy Act", scope: "municipal", notes: "Applies to Ontario municipalities." },
      { name: "PHIPA", fullName: "Personal Health Information Protection Act", scope: "health", notes: "Strict health privacy law. Governs health information custodians. Notable penalties." }
    ],
    authority: { name: "Information and Privacy Commissioner of Ontario", abbr: "IPC ON", url: "https://www.ipc.on.ca" },
    crossBorderRule: "PIPEDA applies for private sector. PHIPA has specific requirements for health information transfers.",
    piaRequired: "Recommended under PIPEDA. Effectively required for health information under PHIPA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation. PHIPA: up to $200,000 for individuals, $1,000,000 for organizations."
  },
  "PE": {
    province: "Prince Edward Island",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies." },
      { name: "FOIPP", fullName: "Freedom of Information and Protection of Privacy Act", scope: "public", notes: "Applies to PEI public bodies." }
    ],
    authority: { name: "Information and Privacy Commissioner of PEI", abbr: "IPC PEI", url: "https://www.assembly.pe.ca" },
    crossBorderRule: "PIPEDA applies for private sector.",
    piaRequired: "Recommended under PIPEDA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation."
  },
  "QC": {
    province: "Quebec",
    laws: [
      { name: "Law 25", fullName: "Act to modernize legislative provisions as regards the protection of personal information (Bill 64)", scope: "private", notes: "Canada's strictest provincial privacy law. GDPR-aligned. Fully in force since Sept 2024 including data portability." },
      { name: "Act respecting Access", fullName: "Act respecting Access to documents held by public bodies and the Protection of personal information", scope: "public", notes: "Applies to Quebec public bodies. Also modernized by Law 25." }
    ],
    authority: { name: "Commission d'accès à l'information du Québec", abbr: "CAI", url: "https://www.cai.gouv.qc.ca" },
    crossBorderRule: "PIA/TIA mandatory BEFORE any transfer outside Quebec. Must assess whether receiving jurisdiction provides adequate protection based on generally accepted privacy principles. Written agreement required with recipient. Must inform affected individuals.",
    piaRequired: "Mandatory for: (1) acquiring/developing/overhauling any information system handling PI, (2) any cross-border transfer, (3) communication for research without consent. CAI published official guide and template.",
    maxPenalty: "Administrative penalties up to $10M or 2% worldwide turnover. Penal fines up to $25M or 4% worldwide turnover. Private right of action with minimum $1,000 damages."
  },
  "SK": {
    province: "Saskatchewan",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies." },
      { name: "FOIP SK", fullName: "Freedom of Information and Protection of Privacy Act", scope: "public", notes: "Applies to SK government bodies." },
      { name: "HIPA", fullName: "Health Information Protection Act", scope: "health", notes: "Governs personal health information in SK." }
    ],
    authority: { name: "Office of the Saskatchewan Information and Privacy Commissioner", abbr: "OIPC SK", url: "https://oipc.sk.ca" },
    crossBorderRule: "PIPEDA applies for private sector. HIPA has specific cross-border provisions for health info.",
    piaRequired: "Recommended under PIPEDA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation. HIPA: up to $50,000 for individuals, $500,000 for organizations."
  },
  "YT": {
    province: "Yukon",
    laws: [
      { name: "PIPEDA", fullName: "Personal Information Protection and Electronic Documents Act", scope: "private", notes: "Federal law applies." },
      { name: "ATIPP YT", fullName: "Access to Information and Protection of Privacy Act", scope: "public", notes: "Applies to Yukon public bodies." }
    ],
    authority: { name: "Information and Privacy Commissioner of Yukon", abbr: "IPC YT", url: "https://www.yukonombudsman.ca" },
    crossBorderRule: "PIPEDA applies for private sector.",
    piaRequired: "Recommended under PIPEDA.",
    maxPenalty: "PIPEDA: up to $100,000 per violation."
  }
};

var dataCategories = [
  { id: "employee_pii", label: "Employee PII", description: "Names, addresses, SINs, payroll, benefits, performance reviews", sensitivity: "high", law25Consent: "express for SINs; implied for employment relationship" },
  { id: "client_pii", label: "Client / Customer PII", description: "Names, contact information, billing addresses, account details", sensitivity: "moderate", law25Consent: "express or implied depending on context" },
  { id: "health_info", label: "Health Information", description: "Medical records, diagnoses, prescriptions, health insurance, mental health notes", sensitivity: "very_high", law25Consent: "express consent required; subject to PHIPA/HIA where applicable" },
  { id: "financial_records", label: "Financial Records", description: "Banking details, tax returns, credit reports, transaction history, investment data", sensitivity: "high", law25Consent: "express consent required for sensitive financial data" },
  { id: "legal_privileged", label: "Legal / Privileged Communications", description: "Solicitor-client communications, litigation files, legal opinions, contracts", sensitivity: "very_high", law25Consent: "special protections; solicitor-client privilege applies" },
  { id: "student_records", label: "Student Records", description: "Academic records, enrollment data, disciplinary records, learning assessments", sensitivity: "high", law25Consent: "parental consent required for minors under 14 in Quebec" },
  { id: "government_ids", label: "Government Identifiers", description: "SINs, passport numbers, driver's licence numbers, immigration documents", sensitivity: "very_high", law25Consent: "express consent required; collection must be necessary" },
  { id: "biometric", label: "Biometric Data", description: "Fingerprints, facial recognition, voiceprints, retinal scans", sensitivity: "very_high", law25Consent: "express consent required; must notify CAI 60 days before creating biometric database in Quebec" },
  { id: "location_data", label: "Location / Tracking Data", description: "GPS coordinates, IP-based geolocation, movement patterns, check-in data", sensitivity: "moderate", law25Consent: "must disclose use of tracking/profiling technology under Law 25" },
  { id: "minor_data", label: "Minor's Personal Information", description: "Any PI relating to individuals under 18 (under 14 in Quebec requires parental consent)", sensitivity: "very_high", law25Consent: "parental/guardian consent required for under-14 in Quebec; heightened protections for all minors" },
  { id: "operational_only", label: "Operational / Non-Personal", description: "System logs, anonymized analytics, configuration data with no personal information", sensitivity: "none", law25Consent: "not applicable if truly anonymized" }
];

var industryProfiles = [
  { id: "legal", label: "Legal Services", typicalData: ["client_pii", "legal_privileged", "financial_records", "government_ids"], regulatoryNotes: "Law society obligations overlay privacy law. Solicitor-client privilege adds additional protection requirements. Conflicts checks involve cross-referencing client PI." },
  { id: "healthcare", label: "Healthcare", typicalData: ["health_info", "client_pii", "government_ids", "biometric"], regulatoryNotes: "Provincial health privacy laws (PHIPA, HIA, HIPA) add sector-specific obligations on top of PIPEDA/Law 25. Electronic health records have strict residency requirements in some provinces." },
  { id: "accounting", label: "Accounting & Tax", typicalData: ["financial_records", "client_pii", "employee_pii", "government_ids"], regulatoryNotes: "CPA professional standards require confidentiality. Tax data includes SINs and detailed financial information. CRA reporting obligations interact with privacy requirements." },
  { id: "real_estate", label: "Real Estate & Construction", typicalData: ["client_pii", "financial_records", "employee_pii", "government_ids"], regulatoryNotes: "FINTRAC anti-money laundering requirements overlap. Mortgage and tenant data highly sensitive. Construction project data may involve multiple subcontractor relationships." },
  { id: "finance", label: "Financial Services & Fintech", typicalData: ["financial_records", "client_pii", "government_ids", "biometric"], regulatoryNotes: "OSFI guidelines for federally regulated institutions. Provincial securities regulations. KYC/AML requirements under PCMLTFA. Payment card industry (PCI-DSS) standards." },
  { id: "education", label: "Education", typicalData: ["student_records", "client_pii", "employee_pii", "minor_data"], regulatoryNotes: "Student privacy protections vary by province. Parental consent required for minors. EdTech vendor agreements require careful review of data handling practices." },
  { id: "government", label: "Government & Public Sector", typicalData: ["client_pii", "government_ids", "employee_pii", "health_info"], regulatoryNotes: "Provincial FOIP/FIPPA legislation applies. Many provinces require data to remain in Canada. Security classification requirements. Treasury Board directives (federal)." },
  { id: "technology", label: "Technology & SaaS", typicalData: ["client_pii", "employee_pii", "location_data"], regulatoryNotes: "If processing PI on behalf of clients, service provider obligations under Law 25 apply. DPA requirements with enterprise customers. SOC 2 / ISO 27001 expectations." },
  { id: "mining", label: "Mining & Resources", typicalData: ["employee_pii", "health_info", "location_data", "biometric"], regulatoryNotes: "Occupational health and safety records contain health PI. Remote site monitoring may involve location/biometric tracking. Environmental assessment data may reference individuals." },
  { id: "hospitality", label: "Hospitality & Restaurant", typicalData: ["client_pii", "employee_pii", "financial_records", "location_data"], regulatoryNotes: "POS systems handle payment card data (PCI-DSS). Reservation systems collect guest PI. Loyalty programs involve profiling. Delivery platforms share data with third parties." },
  { id: "nonprofit", label: "Non-Profit & Charitable", typicalData: ["client_pii", "financial_records", "health_info"], regulatoryNotes: "Law 25 applies to all organizations including non-profits. Donor data is personal information. Beneficiary data may include sensitive categories." },
  { id: "other", label: "Other", typicalData: ["client_pii", "employee_pii"], regulatoryNotes: "Standard PIPEDA / Law 25 obligations apply. Specific requirements depend on the types of personal information collected and processed." }
];
