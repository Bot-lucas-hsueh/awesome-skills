## § 8 · Scenario Examples

### Example 1: APT Group Profile Update

**Context**: New campaign from known APT group targeting healthcare.

**Intelligence Report**:
```
Classification: TLP:AMBER
Subject: APT29 (Cozy Bear) Targeting Healthcare Sector

Key Findings:
├── New spear-phishing lures using COVID-19 vaccine themes
├── Updated malware: WellMess variant with new C2
├── Targeting: Pharmaceutical R&D organizations
├── Geographic focus: US, UK, Germany

TTPs:
├── Initial Access: Spear-phishing (T1566)
├── Execution: PowerShell (T1059.001)
├── Persistence: WMI event subscription (T1546.003)
├── Exfiltration: Cloud storage services (T1567)

IOC List:
├── [Hashes: 3 samples]
├── [Domains: 5 C2 domains]
├── [IPs: 10 C2 IPs]
└── [YARA rules: 2 signatures]

Confidence: High
Sources: 3 independent
```

---

### Example 2: Ransomware Campaign Tracking

**Context**: Tracking evolution of LockBit ransomware operations.

**Analysis**:
```
Campaign: LockBit 3.0 Operations
Timeline: Active since March 2024

Affiliate Model Analysis:
├── Ransom-as-a-Service structure
├── 50+ active affiliates tracked
├── Variable TTPs based on affiliate

Evolution:
├── v2.0: Standard encryption
├── v3.0: Enhanced stealth, Linux variant
├── BlackMatter code integration

Targeting Patterns:
├── Critical infrastructure (40%)
├── Healthcare (25%)
├── Manufacturing (20%)
├── Other (15%)

Predictive Assessment:
├── Likely to continue growth (High confidence)
├── Possible regulation targeting affiliates (Medium)
```

---

### Example 3: Strategic Threat Assessment

**Context**: Annual threat landscape report for board presentation.

**Report Structure**:
```
Executive Summary:
├── Top 3 threats to organization
├── Risk trend (increasing/stable/decreasing)
└── Recommended investments

Threat Landscape:
├── Nation-state: Increased targeting of sector
├── Cybercrime: Ransomware remains primary risk
├── Supply chain: Third-party risk growing

Industry-Specific:
├── Peer breaches analysis
├── Sector TTP trends
├── Regulatory implications

Recommendations:
├── Enhance email security (ROI: High)
├── Implement Zero Trust (ROI: Medium)
├── Increase threat hunting (ROI: High)
```

---

### Example 4: Malware Family Analysis

**Context**: New malware sample from incident response.

**Technical Analysis**:
```
Sample: Trojan.Win32.NewFamily
Analysis Date: 2024-03-21

Capabilities:
├── Credential theft (browsers, LSASS)
├── Keylogging
├── Screenshot capture
├── File exfiltration
├── Persistence via scheduled task

Code Analysis:
├── Written in C++
├── Packed with custom packer
├── Anti-analysis techniques present
├── C2: HTTPS to domains [redacted]

Attribution Clues:
├── Code similarities to known malware
├── Infrastructure overlap with APT group X
├── Language artifacts suggest origin

Confidence: Likely linked to APT group X
```

---

### Example 5: Threat Hunting Support

**Context**: Develop hunting rules based on intelligence.

**Hunting Package**:
```
Hypothesis: APT group using living-off-the-land techniques

Behavioral Indicators:
├── PowerShell encoded commands
├── WMI process creation
├── Unusual LOLBIN execution patterns

Hunting Queries:
├── Splunk: Encoded PowerShell detection
├── EDR: WMI lateral movement
├── Network: C2 beaconing patterns

Validation:
├── Test in lab environment
├── Adjust for false positives
├── Deploy to production hunt
```

---
