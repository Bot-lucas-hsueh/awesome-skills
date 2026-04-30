## § 3 Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| **Mid-Air Collision (MAC)** | CATASTROPHIC | Loss of vehicles, third-party casualties, regulatory shutdown | Layered CD&R (strategic→tactical→DAA); minimum separation standards; emergency priority handling; always-available C2 link monitoring |
| **UTM System Outage** | CRITICAL | All authorized operations grounded or operating without deconfliction service; cascading failures | Active-active redundancy; graceful degradation to last-known authorization; operator kill-switch and contingency procedures |
| **Communication Link Loss** | SERIOUS | UAS operating without real-time traffic picture; conformance monitoring failure | C2 link loss procedures mandated per operation; autonomous Return-to-Home or land-in-place triggers; ATC notification protocols |
| **Cyber Attack on UTM** | CRITICAL | Spoofed authorizations, false traffic injection, denial of service to safety systems | Zero-trust architecture; mutual TLS authentication; rate limiting; anomaly detection on trajectory data; air-gapped backup systems |
| **Airspace Complexity Overload** | SERIOUS | CD&R algorithm latency exceeds tactical window; human controllers overwhelmed | Load shedding with priority queuing; algorithmic complexity bounds (≤500ms for tactical CD&R); automation of routine conflict resolution |
| **Regulatory Non-Compliance** | CRITICAL | Operations suspended, significant fines, loss of ANSP trust, industry setback | Continuous compliance monitoring; maintain regulatory mapping matrix; engage ANSP and regulator during design, not after deployment |

---
