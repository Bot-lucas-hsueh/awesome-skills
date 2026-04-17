## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| **False Positive Safety Warning** | SERIOUS | Driver over-reacts to false alert; dangerous maneuver; potential collision | Strict message validation; position accuracy requirements (< 1.5m 95th percentile); plausibility checks on received BSMs |
| **Channel Congestion Failure** | CRITICAL | Safety messages not received in dense V2X environment; intersection collision without warning | DCC (ETSI TS 102 687) mandatory; CBR monitoring; adaptive transmission rate and power reduction |
| **GPS Spoofing Attack** | CRITICAL | Malicious BSM with falsified position; misleads cooperative perception; safety system failure | Position plausibility check; cross-reference with map and sensor data; misbehavior detection and reporting |
| **Certificate Revocation Delay** | SERIOUS | Compromised V2X unit continues broadcasting for minutes after revocation | Short pseudonym certificate lifetime (5-7 min); online revocation check at infrastructure; misbehavior detection |
| **Regulatory Non-Compliance** | CRITICAL | V2X device using unauthorized spectrum or transmit power; FCC/ETSI enforcement action | Type approval per FCC Part 95S (USA) or ETSI EN 302 663 (EU); pre-deployment spectrum authorization |
| **Interoperability Failure** | SERIOUS | OBU from one vendor cannot communicate with RSU from another; field deployment unusable | DSRC certification (DSRC Center of Excellence tests); C-V2X conformance testing; OBU-RSU interoperability field test |

---
