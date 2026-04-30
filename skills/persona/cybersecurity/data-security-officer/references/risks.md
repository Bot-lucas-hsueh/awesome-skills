## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重度 | Description / 描述 | Mitigation
|------------|-----------------|-------------------|---------------------|
| **Inadequate breach notification timing** | 🔴 Critical | GDPR requires 72h to supervisory authority (Art. 33); HIPAA requires 60 days; PIPL requires immediate; missing deadlines carries penalties up to 4% global turnover | Implement automated breach detection with clock-triggered notification workflow; test annually |
| **Cross-border data transfer violations** | 🔴 High | Transferring EU personal data to non-adequate countries without SCC, BCR, or adequacy decision violates GDPR Art. 46; Schrems II invalidated Privacy Shield | Map all data flows; use SCC for US transfers; implement supplemental technical measures |
| **Encryption key loss** | 🔴 High | Losing encryption keys makes encrypted data permanently inaccessible; 20% of encrypted databases are lost to key mismanagement annually | Use cloud HSM (AWS CloudHSM, Azure Dedicated HSM); key backup with M-of-N ceremony; quarterly testing |
| **Shadow data exposure** | 🟡 Medium | Dev copies of production databases, forgotten S3 buckets, and test data with real PII are the most common GDPR violation source | Run monthly automated discovery (AWS Macie, Varonis); mandate data minimization in SDLC |
| **Tokenization scope gaps** | 🟡 Medium | Tokenizing primary key (SSN) while leaving correlated fields (name, DOB, address) un-tokenized allows re-identification | Apply tokenization to full re-identification set; validate with k-anonymity ≥ 5 |
| **DLP false positive alert fatigue** | 🟡 Medium | DLP rules generating > 500 alerts/day go unreviewed; teams disable overly aggressive policies | Tune DLP with Exact Data Match over regex; target < 50 true-positive alerts/day |
| **Missing vendor DPA agreements** | 🟢 Low | Third-party vendors processing personal data without Data Processing Agreements creates joint controller liability under GDPR Art. 28 | Maintain vendor inventory; require DPA before any data sharing; annual vendor risk reviews |

---
