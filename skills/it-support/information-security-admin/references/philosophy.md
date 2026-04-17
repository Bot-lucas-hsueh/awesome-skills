## § 4 · Core Philosophy

### Mental Model: The Security Administration Operating Model

```
┌──────────────────────────────────────────────────────────────┐
│                   GOVERNANCE LAYER                           │
│  Policy · Risk Register · Compliance · Executive Reporting   │
├──────────────────────────────────────────────────────────────┤
│                   IDENTITY LAYER                             │
│     IAM · PAM · MFA · RBAC · Joiner-Mover-Leaver Process    │
├──────────────────────────────────────────────────────────────┤
│                   PROTECTION LAYER                           │
│    Firewall · DLP · Endpoint Protection · Email Security     │
├──────────────────────────────────────────────────────────────┤
│                   DETECTION LAYER                            │
│         SIEM · EDR · UEBA · Vulnerability Scanner           │
├──────────────────────────────────────────────────────────────┤
│                   RESPONSE LAYER                             │
│     IR Playbooks · SOAR · Forensics · Backup & Recovery      │
├──────────────────────────────────────────────────────────────┤
│                   ASSET & DATA LAYER                         │
│     Asset Inventory · Data Classification · Shadow IT        │
└──────────────────────────────────────────────────────────────┘
```

### Guiding Principles

1. **Least Privilege is Non-Negotiable** — Every account, service, and process should have exactly the permissions needed to perform its function, nothing more. Review and right-size access quarterly.

2. **Security Controls Must Be Measurable** — "We have a firewall" is not a control; "Our firewall blocks 99.7% of known malicious IPs with <0.1% false positive rate on outbound traffic" is. Instrument every control.

3. **Assume Breach, Design for Resilience** — Prevention will eventually fail; detection speed and recovery capability are what separate a contained incident from a catastrophic breach.

---

