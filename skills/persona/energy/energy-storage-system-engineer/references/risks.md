## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **Thermal Runaway** | 🔴 High | Propagation from cell-to-module-to-rack can cause fire/explosion in enclosed BESS | Require UL 9540A test data; specify appropriate fire suppression; maintain spacing per NFPA 855 |
| **Arc Flash** | 🔴 High | DC systems up to 1500V present significant arc flash hazard | Specify proper PPE category; design for remote operation; use DC disconnectors |
| **Code Non-Compliance** | 🔴 High | Installing non-UL listed systems violates NEC; insurance may be void | Verify UL  listing for all major components; obtain AHJ approval |
| **Grid Stability** | 🟡 Medium | Improper grid-tied BESS can cause islanding, frequency excursions | Ensure IEEE 1547 compliance; coordinate with utility; use UL 1741 certified inverters |
| **Degradation Misestimation** | 🟡 Medium | Overestimating capacity leads to unmet performance guarantees | Use validated degradation curves; specify measurement tolerance; require performance bonds |
| **Ground Fault** | 🟢 Low | Undetected DC ground faults can lead to fire in grounded systems | Specify ground fault detection/interruption; regular testing protocol |

**⚠️ IMPORTANT:**
- Never specify battery chemistries or configurations without confirming UL 9540 listing status
- Always require thermal runaway propagation testing (UL 9540A) for large-scale installations
- Grid-connected systems require licensed electrical engineer stamp in most jurisdictions

---
