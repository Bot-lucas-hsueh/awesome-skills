## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **PHI Exposure** | 🔴 High | Telemedicine systems process protected health information; breach can result in OCR enforcement and patient harm | Implement encryption at rest (AES-256) and in transit (TLS 1.3), role-based access controls, and comprehensive audit logging |
| **Clinical Misdiagnosis from Tech Failure** | 🔴 High | Video freeze, data loss, or sync errors can cause missed symptoms or incorrect diagnosis | Design for resilience: automatic reconnection, local caching, clinical escalation protocols |
| **Regulatory Non-Compliance** | 🔴 High | HIPAA violations carry fines up to $1.5M per violation category; state-specific telehealth laws vary | Map every feature to specific regulatory requirement; maintain compliance matrix |
| **Cross-Border Data Transfer** | 🟡 Medium | Transferring patient data across jurisdictions triggers GDPR, local data residency laws | Design for data localization; use approved transfer mechanisms (SCCs, adequacy decisions) |
| **Informed Consent Gaps** | 🟡 Medium | Telehealth requires specific consent documentation; verbal consent may be insufficient | Embed consent workflows into platform; version control and audit trail required |

**⚠️ IMPORTANT:**
- Never suggest using consumer-grade video tools (Zoom, FaceTime) for clinical encounters without BAA and HIPAA safeguards
- AI-assisted triage is not a diagnosis; always recommend clinician review
- Retention periods for telemedicine records follow state-specific requirements (often 7-10 years)

---
