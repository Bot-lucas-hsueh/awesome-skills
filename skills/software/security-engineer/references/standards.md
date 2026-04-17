## 7. Standards & Reference

### 7.1 OWASP Top 10 (2021) Quick Reference

| # | Vulnerability / 漏洞 | Root Cause / 根因 | Detection / 检测 | Mitigation
|---|---------------------|------------------|-----------------|-----------------|
| A01 | Broken Access Control | Missing authz checks | DAST, code review | RBAC, deny by default, audit logs |
| A02 | Cryptographic Failures | Weak/missing encryption | Manual review, Semgrep | TLS 1.3, AES-256, PBKDF2/Argon2 |
| A03 | Injection (SQLi, XXE) | Unsanitized input | SAST, SQLMap | Parameterized queries, allowlists |
| A04 | Insecure Design | Missing threat model | Architecture review | STRIDE, secure design patterns |
| A05 | Security Misconfiguration | Default settings | Trivy, ScoutSuite | CIS benchmarks, hardening guides |
| A06 | Vulnerable Components | Outdated dependencies | Dependabot, Snyk, SBOM | Patch SLA, SCA in CI/CD |
| A07 | Auth & Session Failures | Weak passwords, no MFA | DAST, pentest | MFA, FIDO2, secure session management |
| A08 | Software Integrity Failures | No code signing | SLSA, Sigstore | Code signing, verified builds, SBOM |
| A09 | Logging & Monitoring Failures | Insufficient audit trails | Gap analysis | Centralized SIEM, anomaly detection |
| A10 | SSRF | Unvalidated server-side URLs | DAST, code review | Allowlists, block metadata endpoints (169.254.x) |

### 7.2 Compliance Mapping Matrix

| Control Domain
|------------------------|---------|-------------|---------|------------|
| Access Control | CC6.1 | Art. 32 | 164.312(a) | Req. 7 |
| Encryption in Transit | CC6.7 | Art. 32 | 164.312(e) | Req. 4 |
| Audit Logging | CC7.2 | Art. 30 | 164.312(b) | Req. 10 |
| Vulnerability Management | CC7.1 | Art. 32 | 164.308(a)(8) | Req. 6 |
| Incident Response | CC7.3 | Art. 33/34 | 164.308(a)(6) | Req. 12 |
| Risk Assessment | CC3.1 | Art. 35 (DPIA) | 164.308(a)(1) | Req. 12 |
| Patch Management | CC7.1 | Art. 32 | 164.308(a)(5) | Req. 6 |
| Network Segmentation | CC6.6 | Art. 32 | 164.312(a)(2) | Req. 1 |

### 7.3 STRIDE Threat Framework

| Threat / 威胁 | Category | Example Attack | Control
|--------------|----------|---------------|------------------|
| **Spoofing** | Identity | Forged JWT, credential theft | MFA, strong auth, certificate pinning |
| **Tampering** | Integrity | SQL injection, parameter manipulation | Input validation, parameterized queries, signing |
| **Repudiation** | Audit | Deleting logs, denying actions | Immutable audit logs, WORM storage |
| **Information Disclosure** | Confidentiality | Data leakage, verbose errors | Encryption, need-to-know access, sanitized errors |
| **Denial of Service** | Availability | DDoS, resource exhaustion | Rate limiting, WAF, auto-scaling, CDN |
| **Elevation of Privilege** | Authorization | Privilege escalation, IDOR | Authz checks, RBAC, least privilege |

---

