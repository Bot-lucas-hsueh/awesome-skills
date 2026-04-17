# Standards & Reference

## 7.1 Security Frameworks

### NIST Cybersecurity Framework
| Function | Description |
|----------|-------------|
| Identify | Asset management, risk assessment |
| Protect | Access control, training |
| Detect | Anomaly detection, monitoring |
| Respond | Incident response |
| Recover | Recovery planning |

### OWASP Top 10 (2021)
1. A01 Broken Access Control
2. A02 Cryptographic Failures
3. A03 Injection
4. A04 Insecure Design
5. A05 Security Misconfiguration
6. A06 Vulnerable Components
7. A07 Auth Failures
8. A08 Data Integrity Failures
9. A09 Logging Failures
10. A10 SSRF

## 7.2 Common Vulnerabilities

| Vulnerability | Severity | Exploitability |
|---------------|----------|----------------|
| SQL Injection | 🔴 Critical | Easy |
| XSS | 🟡 High | Easy |
| CSRF | 🟡 Medium | Medium |
| SSRF | 🟡 High | Medium |
| IDOR | 🟡 High | Easy |

## 7.3 Encryption Standards

| Standard | Use Case | Key Size |
|----------|----------|----------|
| AES-256 | Data at rest | 256 bit |
| TLS 1.3 | Data in transit | Ephemeral |
| SHA-256 | Hashing | 256 bit |
| Argon2id | Password hashing | Memory-hard |
