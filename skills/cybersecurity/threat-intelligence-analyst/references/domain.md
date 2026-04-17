## § 6 · Domain Knowledge

### 6.1 Major Threat Actor Categories

| Category | Motivation | Examples | Targeting |
|----------|------------|----------|-----------|
| **Nation-State** | Espionage, sabotage | APT29, Lazarus, Equation | Government, defense, tech |
| **Cybercrime** | Financial gain | FIN7, Carbanak, Evil Corp | Financial, healthcare, retail |
| **Hacktivist** | Ideology | Anonymous, LulzSec | Political, corporate targets |
| **Insider** | Various | Disgruntled employees | Internal systems, data theft |

### 6.2 MITRE ATT&CK for Intelligence

| Tactic | Common Techniques | Detection Opportunity |
|--------|-------------------|----------------------|
| **Initial Access** | Spear phishing, exploits | Email security, threat intel |
| **Persistence** | Registry run keys, services | Autoruns monitoring |
| **Defense Evasion** | Process injection, AMSI bypass | Behavioral analytics |
| **Credential Access** | LSASS dumping, Kerberoasting | Credential protection |
| **Exfiltration** | C2 channels, cloud storage | Network monitoring, DLP |

### 6.3 IOC Types and Confidence

| IOC Type | Confidence | Shelf Life | Example |
|----------|------------|------------|---------|
| **Hash** | High | Short (polymorphic) | File hash of malware |
| **Domain** | Medium | Medium | C2 domain |
| **IP Address** | Medium | Short (fast flux) | C2 IP |
| **YARA Rule** | High | Medium-Long | Behavioral signature |
| **TTP** | High | Long | MITRE technique |

---
