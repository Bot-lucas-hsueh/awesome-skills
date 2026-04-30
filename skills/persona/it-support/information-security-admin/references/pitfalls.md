## § 10 · Common Pitfalls

### Pitfall 1: Shared Admin Accounts


❌ **BAD**
```
admin/P@ssw0rd123 — shared across 5 IT team members, no logging of who did what
```

✅ **GOOD**
```powershell
# Individual admin accounts + PAM for privileged access
# Each admin has their own named account: john.admin@company.com
# All privileged sessions recorded in CyberArk/BeyondTrust
# Zero shared credentials anywhere in the environment
Set-ADAccountPassword -Identity "john.admin" -Reset -NewPassword (Read-Host -AsSecureString)
```

**Why it matters:** Shared accounts make forensic attribution impossible during incidents; violates ISO 27001 A.9.2.3 and SOC 2 CC6.3.

---

### Pitfall 2: SIEM with No Tuning → Alert Fatigue


❌ **BAD:** Enable all default Splunk ES correlation rules → 10,000+ alerts/day → analysts stop looking

✅ **GOOD:**
```splunk
/* Start with 5 high-fidelity rules; tune before adding more */
/* Example: Brute force rule with tuning */
index=windows EventCode=4625
| stats count by src_ip, dest_host, user
| where count > 20  /* threshold: 20 failed logins */
/* After 2 weeks: adjust threshold based on legitimate patterns */
/* Whitelist known scanners, service accounts, and backup systems */
| where NOT src_ip IN ("10.1.5.10", "192.168.1.100")  /* known legit */
```

**Why it matters:** SIEM value comes from analysts trusting and acting on alerts; a noisy SIEM is worse than no SIEM because it creates false confidence.

---

### Pitfall 3: Firewall Rules Never Reviewed


❌ **BAD:** "Allow any-any" rule added for troubleshooting in 2019 → never removed → still open in 2026

✅ **GOOD:**
```
Quarterly firewall review process:
1. Export all rules: show running-config | section access-list
2. For each rule: identify owner, business justification, last-used date
3. Mark rules with no traffic in 90 days for removal
4. Remove or time-limit troubleshooting rules immediately after use
5. Document every change with ticket number and approver
```

**Why it matters:** Firewall rule bloat is one of the most common sources of security misconfigurations; average enterprise has 37% of firewall rules that serve no current business purpose (Gartner).

---

### Pitfall 4: Vulnerability Scan Without Authentication


❌ **BAD:** Running Nessus without credentials → sees only 15-30% of actual vulnerabilities

✅ **GOOD:**
```
Tenable.io authenticated scan setup:
1. Create dedicated scan account with local admin (Windows) or sudo (Linux)
2. Scan account: read-only registry access + WMI + SSH (no interactive login)
3. Verify: authenticated scan finds 3-5× more vulnerabilities than unauthenticated
4. Rotate scan account password quarterly via PAM
```

**Why it matters:** Unauthenticated scans miss 70-85% of vulnerabilities inside the OS (patching status, local config issues); your remediation SLA only applies to what you can see.

---

### Pitfall 5: Incident Response Without Documented Playbooks


❌ **BAD:** "Everyone knows what to do" → during a ransomware at 2am, nobody knows who to call, what to isolate, or where the backups are

✅ **GOOD:**
```markdown
IR Playbook — Ransomware (excerpt)
On-Call Contact: [Security Pager: +1-555-0100]
CISO Escalation: [Name, Mobile]
Backup Admin: [Name, Mobile]

Step 1: Isolate (0-15 min)
  → Block affected subnet at firewall [RUNBOOK LINK]
  → Disable affected AD accounts [SCRIPT: IR-Scripts\disable-accounts.ps1]

Step 2: Preserve Evidence (15-30 min)
  → Run memory capture [TOOL: \\ir-tools\procdump64.exe]
  → Export event logs [SCRIPT: IR-Scripts\collect-logs.ps1]
```

**Why it matters:** Average incident response time without playbooks is 3.5× longer than with documented procedures; minutes matter in ransomware containment.

---

### Pitfall 6: No Regular Backup Restore Tests


❌ **BAD:** "We have daily backups" → ransomware hits → attempt to restore → backup agent was broken for 3 months → no valid backups

✅ **GOOD:**
```
Quarterly backup restore test procedure:
1. Select random sample: 2 file servers, 1 database, 1 VM
2. Restore to isolated test environment (never production)
3. Verify: file integrity, database consistency, application startup
4. Measure: actual RTO achieved vs RTO target
5. Document: test date, result, any failures and remediation
6. Offsite/offline backup: verify air-gap backup is not reachable from main network
```

**Why it matters:** 58% of companies that have backups find them unrestorable during an actual ransomware event (Veeam Ransomware Trends 2024).

---

## § 11 · Integration with Other Skills

### Integration 1: Information Security Admin + DevOps Engineer


**Workflow:** Shift-left security — embed security controls into CI/CD pipeline.

- Security Admin defines: SAST policy, secrets scanning rules, container image signing requirements
- DevOps implements: Checkov for IaC scanning, Trivy for container scanning, git-secrets for pre-commit hooks
- Shared outcome: security findings caught at commit time vs. production deployment — 10× cheaper to fix

### Integration 2: Information Security Admin + IT Support Specialist


**Workflow:** Security-aware endpoint support and incident escalation path.

- IT Support handles Tier 1: reset passwords, unlock accounts, malware removal on single endpoint
- Security Admin handles Tier 2+: suspicious activity patterns, policy violations, multi-endpoint incidents
- Shared process: IT Support runbook includes security escalation triggers (IOCs, bulk account lockouts, unusual login times)
- Outcome: Faster MTTD because IT Support triages and escalates with full context vs. raw ticket

### Integration 3: Information Security Admin + Legal Counsel


**Workflow:** Breach notification and regulatory compliance.

- Security Admin provides: incident timeline, data involved (PII/PHI/PCI), affected records count, containment evidence
- Legal Counsel determines: notification obligations (GDPR 72h, HIPAA 60 days, SEC 4 days for material events)
- Shared output: regulator notification letter, customer communication, law enforcement referral if criminal
- Outcome: Correct and timely notifications avoid regulatory penalties on top of breach costs

---

## § 12 · Scope & Limitations

### Use When

- Managing security policies, access controls, and compliance programs for an organization
- Responding to security incidents including malware, phishing, unauthorized access, and data breaches
- Operating and tuning SIEM platforms (Splunk, Microsoft Sentinel) for threat detection
- Conducting vulnerability assessments and managing remediation workflows
- Preparing for and maintaining compliance with ISO 27001, SOC 2, NIST CSF, GDPR, HIPAA

### Do NOT Use When

- Offensive security
- Network infrastructure design (routing, switching, SD-WAN) — use Network Engineer skill
- Application security code review (SAST, DAST in development) — use Security Engineer skill
- Physical security (access badges, CCTV) — requires physical security specialist
- Legal interpretation of regulatory requirements — Security Admin informs; Legal Counsel decides

### Alternatives

- **Penetration testing needs**: AI Security Engineer skill (offensive techniques, red teaming)
- **Application security**: Security Engineer skill (OWASP, SAST, code review)
- **Network security architecture**: System/Network Architect skills

---

## § 13 · How to Use This Skill

### Quick Install

```
Read https://theneoai.github.io/awesome-skills/skills/it-support/information-security-admin/SKILL.md and install
```

### Trigger Words

| English | 中文 |
|---------|------|
| "information security admin" | "信息安全管理员" |
| "access control" / "IAM" / "privileged access" | "访问控制" / "身份管理"
| "SIEM alert" / "threat monitoring" | "SIEM告警"
| "vulnerability scan" / "patch management" | "漏洞扫描"
| "incident response" / "ransomware" | "事件响应"
| "ISO 27001" / "SOC 2" / "NIST CSF" | "ISO 27001合规"
| "security policy" / "compliance audit" | "安全策略"

---

## § 14 · Quality Verification

### Self-Checklist

```
[✓] Classified data/system sensitivity before recommending controls
[✓] Cited specific framework control IDs (ISO 27001 A.x.x, NIST CSF function)
[✓] Distinguished active incident response from proactive hardening
[✓] Applied least privilege principle to every access recommendation
[✓] Provided specific CLI commands, query syntax, or policy config — not general advice
[✓] Included regulatory notification requirement if PII/PHI involved
[✓] Risk-ranked recommendations by likelihood × impact
[✓] MTTD and MTTR targets cited for SIEM/incident response guidance
```

### Test Cases

**Test 1:** "How do I implement MFA for all users in Microsoft 365?"
- Expected: Entra ID Conditional Access policy configuration, authentication methods setup, exclusion groups for break-glass accounts, monitoring for MFA bypass attempts

**Test 2:** "We had a phishing attack and 3 users clicked the link. What do I do?"
- Expected: Immediate account password reset + session revocation, email header analysis, IOC extraction, email gateway block of phishing domain, user notification, check for OAuth app consent grants, document timeline

**Test 3:** "How do I prepare for our first ISO 27001 audit?"
- Expected: Gap assessment methodology, ISMS documentation requirements (Scope, Policy, Risk Register, SoA), evidence collection for key controls, internal audit process, management review, corrective action tracking

---

## § 15 · Version History

| Version / 版本 | Date / 日期 | Changes
|----------------|-------------|-------------------|
| 3.0.0 | 2026-03-04 | Full 16-section rewrite to 9.5/10 Exemplary standard; added IAM, SIEM, vulnerability management, incident response playbooks, 3 scenario examples, 6 pitfalls, compliance metrics |
| 1.1.0 | 2026-02-20 | Added basic access control and threat monitoring sections |
| 1.0.0 | 2026-02-16 | Initial release with basic security policy overview |

---

## § 16 · License & Author

| Field / 字段 | Value
|-------------|-----------|
| **License** | MIT with Attribution |
| **Author** | neo.ai |
| **Repository** | [theneoai/awesome-skills](https://github.com/theneoai/awesome-skills) |
| **Skill URL** | `https://theneoai.github.io/awesome-skills/skills/it-support/information-security-admin/SKILL.md` |
| **Category** | it-support |
| **Verified By** | Expert Review — 2026-03-04 |

```
MIT License — Copyright (c) 2026 neo.ai
Permission is hereby granted, free of charge, to any person obtaining a copy of this skill
to use, copy, modify, and distribute, subject to the condition that attribution is preserved.
```
