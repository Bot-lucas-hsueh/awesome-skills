## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Over-engineering** | 🔴 Critical | Microservices for 5-person team → 10× ops overhead | Start modular monolith; extract when pain measured |
| **Premature Optimization** | 🔴 Critical | Optimizing wrong layer before profiling | Profile production load; identify actual bottleneck |
| **Distributed Monolith** | 🔴 Critical | Services share database → tight coupling | Service owns data; no cross-service table access |
| **Missing Observability** | 🟠 High | 4-hour incident diagnosis vs. 15 minutes | OpenTelemetry mandatory; SLOs before production |
| **Vendor Lock-in** | 🟠 High | Deep proprietary service usage → $5M migration | Abstract behind interfaces; document lock-in decisions |
| **Conway's Law Violation** | 🟡 Medium | Architecture fights org structure | Align service boundaries with team boundaries |

---
