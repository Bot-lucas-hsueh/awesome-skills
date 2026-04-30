## § 7 · Standards & Reference

### 7.1 Telemedicine Architecture Frameworks

| Framework| When to Use| Key Steps|
|-----------------|----------------------|-------------------|
| **HIPAA Security Rule (Technical Safeguards)** | Designing any system handling PHI | 1. Access Control (§164.312(a)(1)) → implement role-based access → 2. Audit Controls (§164.312(b)) → logging → 3. Integrity Controls (§164.312(c)(1)) → validation → 4. Transmission Security (§164.312(e)(1)) → encryption |
| **IHE XDS (Cross-Enterprise Document Sharing)** | Multi-hospital health information exchange | 1. Document Register → 2. Document Repository → 3. Patient Identity Cross-referencing → 4. Document consumption |
| **mHealth Evidence Reporting and Assessment (mERA)** | Mobile health app evaluation | 1. Infrastructure → 2. Usability → 3. Technical → 4. Clinical |

### 7.2 Telemedicine Metrics

| Metric| Formula| Target|
|--------------|--------------|---------------|
| **Video Latency** | Round-trip time from capture to display | <200ms (clinical grade) |
| **Uptime SLA** | (Total minutes - downtime) / Total minutes | ≥99.9% (8.76 hours/year downtime) |
| **Session Recovery Rate** | Sessions restored after failure
| **PHI Encryption Coverage** | PHI fields encrypted at rest + in transit | 100% |

---
