## § 6 · Domain Knowledge

### 6.1 OWASP Top 10 2021

| Rank | Risk | Mitigation |
|------|------|------------|
| 1 | Broken Access Control | RBAC, authorization checks |
| 2 | Cryptographic Failures | TLS 1.3, strong ciphers |
| 3 | Injection | Parameterized queries |
| 4 | Insecure Design | Threat modeling, secure patterns |
| 5 | Security Misconfiguration | Hardening guides, scanning |
| 6 | Vulnerable Components | Dependency scanning |
| 7 | Auth Failures | MFA, secure session management |
| 8 | Software Integrity | Code signing, verification |
| 9 | Logging Failures | Comprehensive audit logging |
| 10 | SSRF | Input validation, deny lists |

### 6.2 Cloud Security Controls

| Layer | AWS | GCP | Azure |
|-------|-----|-----|-------|
| **IAM** | IAM, SSO | Cloud IAM | Azure AD |
| **Network** | Security Groups | Firewall Rules | NSG |
| **Encryption** | KMS | Cloud KMS | Key Vault |
| **Monitoring** | GuardDuty | Security Command Center | Sentinel |
| **WAF** | AWS WAF | Cloud Armor | WAF |

### 6.3 Compliance Mapping

| Framework | Key Controls | Technical Implementation |
|-----------|--------------|-------------------------|
| **SOC2** | Access control, monitoring | IAM, CloudTrail, SIEM |
| **GDPR** | Data protection, breach notification | Encryption, DLP, logging |
| **HIPAA** | PHI protection, audit controls | Encryption, access logs |
| **PCI-DSS** | Cardholder data protection | Network segmentation, encryption |

---
