## § 5 · Domain Knowledge

### CrowdStrike Falcon Modules Deep Dive

| Module | Function | Key Features |
|--------|----------|--------------|
| **Falcon Prevent** | Next-Gen AV | ML-based malware prevention, exploit blocking, ransomware protection |
| **Falcon Insight** | EDR/XDR | Behavioral detection, Event Search, real-time response |
| **Falcon OverWatch** | Threat Hunting | 24/7 expert hunting, cross-domain coverage, intel feedback |
| **Falcon Complete** | MDR | End-to-end managed detection and response |
| **Falcon Horizon** | CSPM | Agentless cloud posture, compliance, attack path analysis |
| **Falcon Cloud Workload** | CWP | Runtime protection, container security, serverless |
| **Falcon Identity** | IDP | AD/Azure AD protection, Kerberoasting detection, risk-based MFA |
| **Falcon Next-Gen SIEM** | SIEM | LogScale ingestion, 10-year retention, unified investigation |
| **Falcon Fusion** | SOAR | Workflow automation, playbook orchestration |
| **Falcon Spotlight** | Vuln Mgmt | Real-time exposure assessment, exploit prioritization |
| **Falcon X** | Threat Intel | IOC enrichment, adversary tracking, automated intel |
| **Charlotte AI** | AI Assistant | Detection triage, investigation, agentic workflows |

### Threat Intelligence: Key Adversaries

| Adversary | Origin | Motivation | Notable TTPs |
|-----------|--------|------------|--------------|
| **BEAR** | Russia | Nation-state | Supply chain attacks, living off the land |
| **CHOLLIMA** | North Korea | Financial/espionage | Fast breakout, destructive attacks |
| **PANDA** | China | Espionage | Long dwell time, credential harvesting |
| **SPIDER** | Various | eCrime | Ransomware, affiliate models |
| **KITTEN** | Iran | Geopolitical | Watering holes, social engineering |
| **LEOPARD** | Various | Hacktivism | DDoS, defacement, data leaks |

### Detection Engineering

**IOA (Indicator of Attack) vs IOC (Indicator of Compromise):**
- **IOC**: Known-bad artifacts (hashes, IPs, domains) — reactive, easily changed
- **IOA**: Behavioral patterns (PowerShell encoded commands, unusual parent-child processes) — proactive, harder to evade

**Detection Development Lifecycle:**
```
1. Threat Intel / Research → Identify adversary TTP
2. Hypothesis Formation → Predict how TTP would appear in telemetry
3. Query Development → Build Event Search query to detect behavior
4. Validation → Test against known-good and known-bad datasets
5. Deployment → Convert to IOA or scheduled hunt
6. Tuning → Reduce false positives, improve fidelity
7. Feedback Loop → Update based on adversary evolution
```


