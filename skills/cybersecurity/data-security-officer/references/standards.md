## 7. Standards & Reference

### 7.1 Regulatory Comparison Matrix

| Requirement / 要求 | GDPR (EU) | CCPA/CPRA (CA) | PIPL (CN) | HIPAA (US) |
|-------------------|-----------|---------------|-----------|-----------|
| **Breach Notification** | 72h to authority; ASAP to subjects (Art. 33/34) | 72h to AG if > 500 residents | Immediate to authority | 60 days to HHS; media if > 500 |
| **Data Subject Rights** | Access, erasure, portability, rectification | Know, delete, opt-out, correct | Access, correction, deletion, portability | Access, amendment (limited) |
| **Legal Basis Required** | Yes (Art. 6): consent, contract, legitimate interest | No (opt-out model) | Yes: consent or lawful basis | Yes: TPO, healthcare operations |
| **Cross-Border Transfer** | Adequacy/SCC/BCR required | Contracts with foreign processors | Data localization for sensitive data | BAA required for US processors |
| **Max Penalty** | 4% global turnover or €20M | $7,500/intentional violation | RMB 50M or 5% annual revenue | $1.9M/category/year |
| **DPO Required** | Yes (large-scale processing) | No | Yes (processors above threshold) | Privacy Officer required |

### 7.2 Data Classification Framework

| Tier / 级别 | Data Types / 数据类型 | Encryption / 加密 | Access / 访问 | Retention
|------------|---------------------|------------------|--------------|----------------|
| **Restricted** | SSN, biometrics, health records, card PAN, credentials | AES-256-GCM at rest; TLS 1.3 in transit; HSM key management | Need-to-know; MFA; PAM-controlled | As short as legally required; audit every 6 months |
| **Confidential** | Employee data, financials, trade secrets, M&A data | AES-256 at rest; TLS 1.3; managed key rotation | Role-based; approval required; logged | Business necessity; annual review |
| **Internal** | Internal policies, business processes, non-PII analytics | TLS 1.3; encryption recommended | All employees; contractor with NDA | 3-7 years per retention schedule |
| **Public** | Marketing materials, press releases, open datasets | TLS 1.3 for integrity | Anyone | No automatic deletion |

### 7.3 Key Management Lifecycle

| Phase / 阶段 | Requirement / 要求 | Control
|-------------|------------------|----------------|
| **Generation** | FIPS 140-3 validated RNG; HSM-generated for Restricted data | AWS CloudHSM, Azure Dedicated HSM, Thales Luna |
| **Distribution** | Never in plaintext; key-wrapping (KEK encrypts DEK) | Envelope encryption via KMS |
| **Storage** | HSM or KMS; no plaintext key in application config | Vault, AWS KMS, Azure Key Vault |
| **Rotation** | Restricted: 1 year; Confidential: 2 years; automatic rotation | KMS automatic rotation; Vault key rotation policies |
| **Revocation** | Immediate on compromise; document justification | Key revocation list; KMS key deletion with grace period |
| **Destruction** | NIST SP 800-88 media sanitization; key ceremony for master keys | Cryptographic erasure + physical destruction |

---

