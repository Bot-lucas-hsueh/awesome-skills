## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Missing Data Retention and Deletion Controls

```markdown
❌ BAD: Storing all data indefinitely "just in case"
  - Log files retained forever in S3 with PII
  - Test databases with production data from 5 years ago never deleted
  - GDPR purpose limitation violated: data kept beyond original purpose
  → GDPR Art. 5(1)(e): storage limitation; up to 4% fine

✅ GOOD: Policy-driven automated deletion with audit trail
  aws s3api put-bucket-lifecycle-configuration --bucket logs-bucket \
    --lifecycle-configuration '{"Rules":[{"Status":"Enabled",
      "Expiration":{"Days":90},"Id":"pii-log-expiration",
      "Filter":{"Prefix":""}}]}'
  # Application-level: soft delete → hard delete after retention period
  # Quarterly: delete all test environments containing production PII

Why it matters: Schrems II and GDPR enforcement specifically target data
minimization violations; they're easy to detect and fine.
```

**Anti-Pattern 2: Over-broad Database Access

```markdown
❌ BAD: All engineers have read access to production database with PII
  GRANT SELECT ON *.* TO 'engineers'@'%';
  # 50 engineers can read all customer PII; 1 breach = all PII exposed

✅ GOOD: Role-based access with DAM audit trail
  # Production: only on-call DBA + automated app services
  GRANT SELECT ON orders(order_id, status, amount) TO 'app_service'@'app-host';
  # Engineers: read anonymized copy only (tokenized PII in dev environment)
  # Privileged access: CyberArk PAM with session recording + just-in-time approval

Why it matters: 34% of data breaches involve insider access (Verizon DBIR 2025);
over-permissive access turns every compromised credential into a full data breach.
```

### 🟡 Medium Severity

**Anti-Pattern 3: Regex-Only DLP Rules

```markdown
❌ BAD: DLP policy built entirely on regex patterns
  rule: regex="\d{3}-\d{2}-\d{4}"  # SSN pattern
  # Matches product serial numbers, timestamps → 80%+ false positive rate
  # Analysts stop reviewing alerts → DLP program effectively disabled

✅ GOOD: Exact Data Match (EDM) + regex + context analysis
  # EDM: fingerprint actual data (hash of real SSNs from HR system)
  # Context: PII + nearby keywords (name, SSN, employee, salary)
  # Confidence threshold: HIGH only
  # Result: false positive rate drops from 80% to < 5%

Why it matters: DLP programs fail when alert fatigue causes analysts to ignore
all alerts; precision matters more than recall for operationally sustainable DLP.
```

**Anti-Pattern 4: Ignoring SaaS Data

```markdown
❌ BAD: Robust on-prem DLP, but no visibility into Salesforce, Slack, Google Drive
  - Customer PII in Salesforce without DPA with Salesforce
  - Engineering credentials in Slack messages
  → GDPR: controller remains responsible for processor data handling

✅ GOOD: SaaS-native DLP integration + CASB
  - Nightfall AI: GitHub, Slack, Jira, Confluence real-time scanning
  - Microsoft Purview: M365, SharePoint, Teams, Exchange
  - CASB (Netskope): visibility + policy enforcement for any SaaS
  - DPA signed with every SaaS vendor processing personal data

Why it matters: SaaS data > 60% of enterprise data in 2026; most data
breaches now originate from SaaS misconfigurations.
```

**Anti-Pattern 5: Using Consent as Universal Legal Basis

```markdown
❌ BAD: Requesting consent for all processing "to be safe"
  - Consent for employment data (invalid; contract/legal obligation applies)
  - Consent for fraud prevention (invalid; legitimate interest applies)
  - Bundled consent for 20 different purposes in one click
  → GDPR: bundled consent is invalid; cannot condition service on unnecessary consent

✅ GOOD: Select appropriate legal basis per processing purpose
  Purpose              → Legal Basis (GDPR Art. 6)
  Employment contract  → Art. 6(1)(b): performance of contract
  Fraud prevention     → Art. 6(1)(f): legitimate interests
  Marketing (opted-in) → Art. 6(1)(a): consent (granular, easy withdrawal)
  Legal obligation     → Art. 6(1)(c): compliance with law
  # Document each legal basis in processing record (Art. 30)

Why it matters: Employer-employee consent is not freely given (power imbalance);
regulatory guidance consistently rejects "consent-washing".
```

---

