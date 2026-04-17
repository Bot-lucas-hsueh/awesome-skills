## 8. Standard Workflow

### 8.1 Penetration Testing (PTES Framework)

```
Phase 1: Pre-Engagement (授权阶段)
├── Obtain written authorization (scope document, rules of engagement)
├── Define scope: IP ranges, domains, applications, time windows
├── Emergency contacts (if production is accidentally impacted)
└── [✓ Done]: Signed authorization document with explicit scope
    [✗ FAIL]: No written authorization → DO NOT PROCEED under any circumstances

Phase 2: Reconnaissance (侦察阶段)
├── Passive (OSINT): Shodan, Censys, theHarvester, GitHub dorking
│   └── github.com: org:target "api_key" OR "SECRET" OR "password"
├── Active (with permission): Nmap port scan, DNS enumeration
│   └── nmap -sS -sV -sC -O --script vuln -p- target.example.com
└── [✓ Done]: Full attack surface map; technology fingerprints documented

Phase 3: Vulnerability Assessment (漏洞评估)
├── Web: Burp Suite Pro active scan, Nuclei templates, OWASP ZAP baseline
├── Cloud: Prowler (AWS), ScoutSuite (multi-cloud)
├── Container: Trivy, Grype CVE scan
└── [✓ Done]: All findings documented with reproduction steps

Phase 4: Exploitation → Reporting (利用与报告)
├── Validate exploitability (not theoretical); capture proof
├── STOP when objective reached; don't expand scope without approval
├── Report: Executive summary + Technical findings (CVSS + PoC) + Remediation roadmap
└── [✓ Done]: Report delivered; each finding rated Critical/High/Medium/Low/Info
    [✗ FAIL]: Scope expansion discovered → stop, notify client, get written approval
```

### 8.2 DevSecOps Implementation

```
Week 1-2: Zero-friction quick wins
├── Enable Dependabot on all repos (automated vulnerable dependency PRs)
├── Add Gitleaks pre-commit hook (blocks credential commits)
├── Enable GitHub secret scanning (zero setup, free)
└── [✓ Done]: CI fails on new critical CVEs; 0 new secrets committed

Month 1: Shift-left automation
├── Add Semgrep SAST to CI (warn on PRs; block on merge to main for OWASP rules)
├── Add Trivy image scanning to Docker build pipeline
├── Generate SBOM for every release (syft
├── Enable AWS GuardDuty in all regions
└── [✓ Done]: Security checks run on every PR; Critical findings block merge

Month 2: Identity & access hygiene
├── Enforce MFA via IdP (no exceptions, including admins)
├── Implement JIT access for privileged operations (approval + auto-expire)
├── Review and right-size IAM roles (IAM Access Analyzer)
├── Enable CloudTrail + CloudWatch Logs for all accounts
└── [✓ Done]: Zero users without MFA; all privileged access time-limited

Month 3: Program maturity
├── Threat model top 3 highest-risk services (STRIDE workshop)
├── Establish vulnerability SLA: Critical 24h, High 7d, Medium 30d
├── Launch VDP/bug bounty program (HackerOne, Bugcrowd)
└── [✓ Done]: SLA compliance tracked in metrics; first external bug report received
```

---

