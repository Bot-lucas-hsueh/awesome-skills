## § 3 · Risk Disclaimer

| Risk / 风险 | Severity / 严重程度 | Domain Consequence / 领域后果 | Mitigation
|------------|--------------------|-----------------------------|---------------------|
| **Unauthorized Privilege Escalation / 未授权提权** | CRITICAL | Admin account compromise → complete environment takeover, data exfiltration, ransomware deployment | Enforce MFA on all privileged accounts; use PAM (CyberArk/Delinea) with session recording; review standing admin accounts quarterly |
| **Misconfigured Firewall Rules
| **Unpatched Critical Vulnerabilities / 未修补的高危漏洞** | HIGH | CVSS ≥9.0 unpatched vulnerabilities are exploited within 15 days of public disclosure on average (Ponemon 2024) | 24-hour patch SLA for CVSS ≥9.0 internet-facing; 72h for internal; automated patching for OS via WSUS/SCCM |
| **Inadequate Backup & Recovery / 备份与恢复不足** | HIGH | Ransomware with no offline backup = forced ransom payment or permanent data loss | 3-2-1 backup rule (3 copies, 2 media, 1 offsite); quarterly restore test with RTO/RPO verification |
| **SIEM Alert Fatigue
| **Shadow IT
| **Compliance Documentation Gap

---
