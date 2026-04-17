## § 8 · Standard Workflow

### Phase 1: Security Baseline Assessment

```
Input: New environment or compliance mandate
Output: Gap assessment report with prioritized remediation roadmap

Steps:
  1.1 Asset inventory: enumerate all systems, data stores, cloud services (CIS Control 1-2)
  1.2 Data classification: identify Restricted/Confidential/Internal/Public data stores
  1.3 Access review: pull all user accounts, identify over-privileged, stale, and shared accounts
  1.4 Vulnerability scan: run authenticated Nessus scan; export CVSS-prioritized finding list
  1.5 Control gap assessment: map current controls to target framework (ISO 27001
  1.6 Risk register: document top 20 risks with likelihood × impact scores and owners

[✓ Done] Gap report delivered with risk-ranked remediation tasks and owner assignments
[✗ FAIL] Missing asset inventory → cannot scope controls; conduct discovery before proceeding
```

### Phase 2: Access Control Hardening

```
Input: Baseline assessment; active directory
Output: Least-privilege access model implemented; MFA enforced; PAM deployed

Steps:
  2.1 Remove stale accounts: disable accounts inactive >90 days; delete after 30-day hold
  2.2 Right-size privileges: remove unnecessary group memberships; implement RBAC model
  2.3 Enforce MFA: conditional access policy for all users; hardware key for admins
  2.4 Deploy PAM: vault all privileged credentials in CyberArk/Delinea; enable session recording
  2.5 Implement JML process: Joiner (provision day 1) / Mover (update within 24h)
  2.6 Service account audit: rotate all service account passwords; document purpose and owner

[✓ Done] Zero standing admin access outside PAM; MFA adoption 100%; stale accounts removed
[✗ FAIL] Shared accounts remaining → individually accountable users only; no shared credentials
```

### Phase 3: SIEM Detection Engineering

```
Input: SIEM platform (Splunk/Sentinel); log sources configured
Output: Detection rule set with <0.5% false positive rate; alert triage process documented

Steps:
  3.1 Log source inventory: ensure coverage of DC, endpoints, firewall, email, cloud (CIS 8.2)
  3.2 Map ATT&CK coverage: identify top 20 techniques to detect; prioritize by threat intel
  3.3 Write detection rules: correlation logic for brute force, lateral movement, exfiltration
  3.4 Tune false positives: 2-week baseline period; whitelist legitimate patterns; adjust thresholds
  3.5 Build alert tiers: P1 (auto-page SOC on-call) / P2 (email + ticket)
  3.6 Document runbooks: each alert has step-by-step triage and escalation procedure

[✓ Done] MTTD <4h; false positive rate <0.5%; all alerts have runbooks; ATT&CK coverage ≥70%
[✗ FAIL] >5% false positive rate → analysts stop triaging; tune before adding new rules
```

### Phase 4: Incident Response Execution

```
Input: Security incident detected (ransomware / phishing
Output: Incident contained, eradicated, and systems restored; RCA report delivered

Steps:
  4.1 DETECT & TRIAGE (0-15 min): confirm incident, classify severity (P1-P4), activate IR team
  4.2 CONTAIN (15-60 min): isolate affected systems from network; preserve forensic state
  4.3 INVESTIGATE (1-24h): collect logs, memory dumps, IOCs; establish attack timeline
  4.4 ERADICATE (parallel with investigate): remove malware, revoke compromised credentials,
      patch exploited vulnerability
  4.5 RECOVER (24-72h): restore from clean backup; verify integrity; monitor for re-infection
  4.6 POST-INCIDENT (72h+): write RCA report; regulatory notification if required (GDPR: 72h);
      implement corrective actions to prevent recurrence

[✓ Done] Systems restored; RCA delivered; corrective actions tracked in risk register
[✗ FAIL] Evidence not preserved before containment → forensic investigation blocked; preserve first
```

---

