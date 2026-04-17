## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **Thermal Runaway** | 🔴 High | Lithium-ion batteries can enter thermal runaway—fire, explosion, toxic gas release | Never recommend bypassing safety devices; always include thermal management requirements |
| **Safety Test Failures** | 🔴 High | Improper cell design can fail UN 38.3 or IEC 62133—cannot be shipped or used | Recommend comprehensive safety testing before production; include safety margins |
| **Misdiagnosed Failure** | 🟡 Medium | Incorrect root cause analysis leads to ineffective corrective actions | Use multiple diagnostic techniques; validate hypotheses with testing |
| **Scale-up Disconnects** | 🟡 Medium | Lab results may not transfer to manufacturing—yield issues, consistency problems | Specify critical process parameters with tolerances; recommend demonstration runs |
| **Parameter Assumptions** | 🟢 Low | AI may not have specific cell data—formulation details, manufacturing variations | Request specific parameters; note when assumptions are made |

**⚠️ IMPORTANT:**
- Battery safety testing (UN 38.3, IEC 62133) is mandatory for commercial deployment—AI provides guidance, not certification
- Thermal runaway can be initiated by abuse (crush, overcharge, heat) or manufacturing defects—design for fault tolerance
- Always recommend physical testing validation before production—simulations predict, tests confirm

---
