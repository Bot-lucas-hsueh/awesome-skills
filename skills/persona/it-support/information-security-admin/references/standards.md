## § 7 · Standards & Reference

### Key Frameworks

| Framework / 框架 | Scope / 范围 | Key Metric
|-----------------|-------------|----------------------|
| **ISO 27001:2022** | ISMS certification standard; 93 controls in 4 themes | Zero major nonconformities on surveillance audit |
| **NIST CSF 2.0** | Govern, Identify, Protect, Detect, Respond, Recover | Maturity tier ≥3 (Repeatable) for critical functions |
| **SOC 2 Type II** | Trust Service Criteria: Security, Availability, Confidentiality | Zero exceptions on annual Type II audit |
| **GDPR** | EU data protection — consent, rights, breach notification | Breach notification within 72 hours of detection |
| **CIS Controls v8** | Prioritized 18 controls for cyber defense | IG1 (basic hygiene) → IG2 → IG3 implementation |
| **MITRE ATT&CK** | Adversary TTP taxonomy for detection engineering | Map SIEM rules to ATT&CK techniques; coverage ≥70% |

### Security Metrics

| Metric / 指标 | Formula / 公式 | Target
|--------------|---------------|--------------|
| Mean Time to Detect (MTTD) | avg(incident_detection_time - attack_start_time) | <4 hours for critical incidents |
| Mean Time to Respond (MTTR) | avg(incident_containment_time - detection_time) | <1 hour for P1; <4 hours for P2 |
| Patch SLA Compliance | patched_in_SLA
| Privileged Account Count | count(accounts_with_admin_rights) | <0.5% of total user accounts |
| Phishing Click Rate | users_clicked
| SIEM False Positive Rate | false_alerts
| MFA Adoption Rate | mfa_enrolled

### Access Review SLAs

| Review Type / 审查类型 | Frequency / 频率 | Owner
|-----------------------|----------------|---------------|
| Privileged accounts (Domain Admin, etc.) | Monthly | Security Admin |
| All user accounts + access rights | Quarterly | Department Managers + Security |
| Service accounts and API keys | Quarterly | System Owners |
| Third-party
| Firewall rules | Quarterly | Network + Security |

---
