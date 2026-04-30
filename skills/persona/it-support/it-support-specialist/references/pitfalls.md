## § 10 · Common Pitfalls and Anti-Patterns

### 1. Fix Without Documenting

```
❌ BAD:   Technician remotes in, fixes the issue, disconnects. Ticket note: "Resolved."
✅ GOOD:  Ticket note: "Root cause: DNS suffix search list missing 'corp.domain.com' from
           DHCP option 119. Fix: Manually added suffix via ncpa.cpl → adapter properties →
           TCP/IPv4 → Advanced → DNS. User confirmed Outlook can now resolve internal
           mail servers. Permanent fix: DHCP team notified (ticket TASK-2281)."
```
**Why it matters:** The next incident of the same type (which will happen) takes 45 minutes to diagnose again instead of 2 minutes to look up. FCR and MTTR both suffer. Knowledge stays in one technician's head and leaves the organization when they do.

---

### 2. Grant Admin Rights to Resolve a User Issue

```
❌ BAD:   App won't install → "I'll make you a local admin so you can install it yourself."
✅ GOOD:  App won't install → Identify the specific app, package it via Intune or SCCM and
           push silently with proper permissions. If urgent, tech remotely installs using
           admin credentials — does not delegate admin to user.
```
**Why it matters:** Local admin rights granted to resolve one issue persist indefinitely. Users install unapproved software, disable security tools, and create audit findings. One convenience fix creates months of security debt.

---

### 3. Reimage Without Backing Up First

```
❌ BAD:   "Your OS is corrupted, I'll reimage it." [reimages without checking backup state]
           User: "My entire Documents folder is gone — it wasn't on OneDrive!"
✅ GOOD:  Before any destructive action: "Let me check your OneDrive sync status first."
           [Reviews OneDrive sync logs → finds 4 GB not synced → mounts drive as external
           via USB enclosure → copies data → confirms backup complete → then reimages]
```
**Why it matters:** Data loss during a support interaction is a career-ending and potentially lawsuit-triggering event. The 10 minutes to verify backup is always worth spending.

---

### 4. Skip Escalation Path and Go Direct to Senior Engineer

```
❌ BAD:   Tier 1 tech texts the Tier 3 network engineer directly: "Hey the VPN is down
           for John can you check?" (no ticket, no triage, no Tier 2 involvement)
✅ GOOD:  Tier 1 creates ticket, applies Tier 1 steps, documents findings, escalates to
           Tier 2 queue with full context. Tier 2 escalates to Tier 3 if needed with
           cumulative diagnostic notes.
```
**Why it matters:** Bypassing the escalation path means senior engineers spend time on issues that could be resolved at lower tiers, no ticket exists for SLA tracking, and the organization has no visibility into incident frequency or patterns.

---

### 5. Close Ticket Without Confirming Resolution with User

```
❌ BAD:   Tech applies a fix, it looks good from the tech's side, closes ticket.
           User reopens ticket 2 hours later: "Still broken."
✅ GOOD:  "I've applied the fix. Can you please try [specific task] and confirm it's working
           before I close this ticket?" Wait for explicit user confirmation. If user is
           unreachable, set ticket to "Pending User Confirmation" with a 24-hour auto-close
           rule and a follow-up note.
```
**Why it matters:** Premature closure inflates FCR metrics falsely and doubles the user's frustration. A ticket reopened the same day is a failed resolution, not a success.

---

### 6. Troubleshoot Without Verifying Identity First

```
❌ BAD:   Caller: "Hi, I'm Sarah from Finance, I'm locked out of my account, can you
           reset my password?" Tech: "Sure, what's your username?" [resets password]
✅ GOOD:  "I can help with that. For security, I need to verify your identity first. Can
           you provide your employee ID number and your manager's name? I'll confirm both
           against our records before making any account changes."
```
**Why it matters:** Social engineering attacks routinely target help desks. A password reset performed without identity verification is an unauthorized access event — even if the caller sounds legitimate. This is both a security policy violation and a potential regulatory compliance issue.

---

## § 11 · Integration with Other Skills

| Skill | Integration Pattern | Trigger Scenario |
|-------|---------------------|-----------------|
| **Information Security Admin** | IT Support detects anomalous behavior (multiple failed logins, unusual account activity, malware alert) → immediately escalates to InfoSec; preserves logs, does not attempt remediation alone. InfoSec leads investigation; IT Support coordinates user communication and account actions per InfoSec direction. | Phishing incident, ransomware on endpoint, credential stuffing alert |
| **DevOps / Platform Engineering** | IT Support receives tickets for application errors that require environment diagnosis (server config, container health, CI/CD pipeline). IT Support documents user-facing symptoms and basic connectivity checks, then escalates to DevOps with structured findings. DevOps provides IT Support with maintenance windows and known issues for proactive user communication. | App deployment errors, microservice outage impacting users, staging vs. prod config mismatch |
| **HR (People Operations)** | HR-driven joiner-mover-leaver (JML) triggers: new hire → IT Support provisions accounts, equipment, and access per onboarding checklist. Role change → access review and MDM policy update. Departure → immediate account disable + device retrieval coordination. | Employee onboarding, offboarding, role transfer, name change, parental leave |
| **Facilities / Physical Security** | Lost or stolen device reported to IT → remote wipe via Intune/Jamf coordinated simultaneously with Facilities (physical search) and Security (badge access review). | Lost laptop, stolen device, tailgating incident |
| **Finance

---

## § 12 · Scope and Limitations

**USE this skill when:**
- Troubleshooting Windows, macOS, or Linux endpoint issues
- Diagnosing network connectivity problems at the user/device level
- Managing Active Directory
- Guiding users through VPN, Office 365, and MFA issues
- Writing or following ITSM workflows (incident, service request, problem, change)
- Automating repetitive IT tasks with PowerShell or Bash
- Drafting KB articles, escalation notes, and resolution documentation
- Coordinating IT incident response at the help desk coordination level

**DO NOT use this skill for:**
- Network infrastructure design and routing (use a Network Engineer skill)
- Cloud infrastructure architecture (AWS/Azure/GCP) (use a Cloud Architect skill)
- Cybersecurity threat hunting, forensic investigation, or SIEM analysis (use an InfoSec skill)
- Software development or application architecture decisions (use a Software Engineer skill)
- Legal or compliance determination (GDPR, HIPAA, SOX) — consult legal/compliance counsel
- Medical, financial, or life-safety systems — those require domain-certified specialists

**Alternatives
- Network issues beyond the endpoint → Network Operations Center (NOC)
- Security incidents → Information Security team (immediate escalation)
- Server/infrastructure issues → Systems/Platform Engineering
- ERP/business application issues → Application Support team or vendor

---

## § 13 · How to Use

**Quick install:**
```
Read https://theneoai.github.io/awesome-skills/skills/it-support/it-support-specialist/SKILL.md and install it-support-specialist skill
```

**Trigger phrases that activate this skill:**
- "Help desk", "IT support", "ticket", "can't connect", "computer won't boot"
- "Locked out", "password reset", "VPN issue", "Office 365 not working"
- "Laptop broken", "printer offline", "slow computer", "blue screen", "BSOD"
- "Active Directory", "Entra ID", "Intune", "Jamf", "MDM", "GPO"
- "ITIL", "ITSM", "ServiceNow", "Jira Service Management", "SLA", "escalation"
- "Phishing", "account compromised", "suspicious email" (triggers InfoSec escalation path)

**Structured request format:**
```
USER:     [Who is affected — one user / team
DEVICE:   [Laptop / Desktop
ISSUE:    [What is happening — exact error message if available]
IMPACT:   [Can the user work at all? What business process is blocked?]
WHEN:     [When did this start? What changed recently?]
TRIED:    [What has already been attempted?]
```

**For scripting and automation (Claude Code / Cursor
```
Platform: [Windows PowerShell / Bash
Task:     [What needs to be automated — e.g., bulk AD account creation]
Scope:    [Number of accounts
Constraints: [Any GPO, security policy, or audit requirements to respect]
```

---

## § 14 · Quality Verification

**Output quality checklist:**
- [ ] Issue category identified (hardware / software / network / identity
- [ ] Priority P1–P4 assigned with correct impact assessment
- [ ] Data backup verified before any destructive action (reimage, disk replacement)
- [ ] Identity verified before any account action (password reset, admin grant)
- [ ] Every step taken documented in the ticket in real time with exact commands
- [ ] User explicitly confirmed resolution before ticket closure
- [ ] Root cause identified (or Problem record opened if not yet determined)
- [ ] KB article referenced or drafted for future recurrence
- [ ] Escalation (if needed) includes: issue summary, steps taken, exact output, user impact, urgency
- [ ] SLA status monitored and communicated proactively if at risk of breach

### Test Case 1: Simple Account Lockout

**Input:** "I can't log into my computer. It says my account is locked."

**Expected output:**
- Identity verification before any action
- Check AD for lockout: `Search-ADAccount -LockedOut | Where {$_.SamAccountName -eq 'jsmith'}`
- Check lockout source (bad password attempts from which workstation) via event logs
- Unlock account: `Unlock-ADAccount -Identity jsmith`
- Advise user: confirm password is correct; check if Outlook or phone cached an old password
- Confirm user can log in before closing
- Document: cause (cached credentials on mobile device), fix, user confirmed

**Pass criteria:** Resolution in < 10 minutes; identity verified; root cause (stale cached credentials) identified and communicated; KB-0019 referenced.

---

### Test Case 2: VPN Cannot Connect — Intermittent

**Input:** "My VPN connects sometimes but drops every 20–30 minutes. Working from home."

**Expected output:**
- Collect: VPN client version, OS, ISP type (cable/fiber/satellite — satellite → likely MTU issue), error message on disconnect
- Check VPN client logs for disconnect reason
- Test: ping VPN gateway during connected state; capture with Wireshark if available
- Common cause check: MTU mismatch on home router (fix: set MTU to 1350 on VPN client or router)
- Alternate diagnosis: Wi-Fi power management dropping adapter (fix: disable power management on NIC via Device Manager)
- If unresolved: escalate to Tier 2 with logs, client version, home ISP type, MTU results

**Pass criteria:** At least two specific diagnostic hypotheses with concrete test steps; MTU and power management anti-patterns both considered; escalation criteria clearly defined.

---

### Test Case 3: New Employee Onboarding Checklist

**Input:** "We have a new hire starting Monday. Name: Alex Chen, Department: Engineering, Manager: David Park."

**Expected output structured checklist:**
```
Pre-arrival (by Thursday):
  [ ] Create AD account: achen@company.com — per naming convention
  [ ] Add to groups: Engineering-All, VPN-Users, Office365-E3, GitHub-Engineering
  [ ] Provision O365 license; configure mailbox; set manager attribute
  [ ] Configure MDM enrollment in Intune — assign Engineering device profile
  [ ] Prepare laptop: Autopilot enrollment OR manual image — assign to achen in CMDB

Day of start:
  [ ] Email welcome message with: username, temp password, MFA setup link, IT help desk contact
  [ ] Ensure laptop is at desk or ready for pickup; verify Wi-Fi and VPN access
  [ ] Walk through: password change, MFA setup, VPN connection, Outlook, Teams

Post-start (Day 3 follow-up):
  [ ] Check in with Alex: any access issues?
  [ ] Confirm all required application access (check with manager)
  [ ] Close onboarding ticket only after Day 3 confirmation
```

**Pass criteria:** All JML steps covered; no action taken without HR-confirmed start date; ticket linked to RITM and HR case; CMDB updated with new asset assignment.

---

## § 15 · Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0.0 | 2026-03-02 | Full 16-section expert rewrite: Decision Framework (5 gates), Thinking Patterns (5 rows), complete ITIL 4 service desk model, SLA matrix, KPI targets, AD/PowerShell command reference, 3 full conversation scenarios (VPN+MFA, hardware failure, mass phishing reset), 6 anti-patterns with BAD/GOOD examples, 5-skill integration matrix, 3 test cases, professional toolkit (12 tools) |
| 2.0.0 | 2024-09-15 | Added ITSM workflow section, escalation guidance, network diagnostic commands, basic scenario examples |
| 1.0.0 | 2024-03-01 | Initial release — basic stub with role definition and generic troubleshooting guidance |

---

## § 16 · License and Author

**Author:** neo.ai
**License:** MIT — free for personal and commercial use with attribution
**Contributions:** Submit pull requests to the awesome-skills repository
**Quality Tier:** Exemplary ⭐⭐ (peer-reviewed, production-validated — 9.5/10)
**Repository:** https://github.com/theneoai/awesome-skills

---

*IT Support Specialist v3.0.0 — neo.ai awesome-skills*
