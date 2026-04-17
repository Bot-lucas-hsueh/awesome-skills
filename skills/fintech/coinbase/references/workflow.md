## § 4 — Workflow

### 4.1 Three-Phase Security Development

#### PHASE 1: THREAT MODELING (Weeks 0-2)

| Task | ✓ Done When | ✗ FAIL If |
|------|-------------|-----------|
| Attack surface mapping | All entry points documented | >10% surface uncovered |
| Threat actor analysis | MITRE ATT&CK aligned | No adversary profiles |
| Risk scoring | CVSS v3.1 scores assigned | No quantitative assessment |
| Security requirements | REQ-SEC-XXX documented | Requirements <90% coverage |

#### PHASE 2: SECURE DEVELOPMENT (Weeks 2-8)

| Task | ✓ Done When | ✗ FAIL If |
|------|-------------|-----------|
| Static analysis | SAST clean (SonarQube/Checkmarx) | Critical/high findings |
| Dependency scan | No known CVEs | Unpatched critical CVEs |
| Penetration test | External firm engaged | No test plan approved |
| Code review | 2+ senior engineers approved | Single reviewer |

#### PHASE 3: PRODUCTION READINESS (Weeks 8-10)

| Task | ✓ Done When | ✗ FAIL If |
|------|-------------|-----------|
| Security sign-off | CISO approval documented | Conditional approval only |
| Compliance review | Legal/Compliance approved | Open regulatory questions |
| Incident response | Runbook tested, pager configured | No on-call rotation |
| Monitoring | SIEM alerts configured | Missing critical alerts |

### 4.2 Regulatory Compliance Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│                     COMPLIANCE ENGINE                           │
│                                                                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────────────┐         │
│  │   Onboarding│───→│   Identity  │───→│   Risk      │         │
│  │   (Jumio)   │    │   Graph     │    │   Scoring   │         │
│  └─────────────┘    └─────────────┘    └──────┬──────┘         │
│                                               │                  │
│  ┌─────────────┐    ┌─────────────┐    ┌─────┴─────┐           │
│  │  Transaction│←───│   Chainalysis│←──│  Decision │           │
│  │  Monitoring │    │  (Elliptic)  │   │   Engine  │           │
│  └──────┬──────┘    └─────────────┘    └───────────┘           │
│         │                                                       │
│         ↓                                                       │
│  ┌─────────────┐                                                │
│  │   SAR Filing│  (FinCEN within 24h for suspicious activity)  │
│  │   (Automated)│                                                │
│  └─────────────┘                                                │
└─────────────────────────────────────────────────────────────────┘
```

---
