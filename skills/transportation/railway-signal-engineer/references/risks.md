## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **Safety-critical failure** | 🔴 High | Signaling failure can cause train collisions, derailments, or fatalities | Require SIL 4 verification; never recommend bypassing safety interlockings |
| **Regulatory non-compliance** | 🔴 High | Non-compliant design fails approval, causing project delays | Always specify applicable standard (CENELEC, AREMA, NR, BAV); request regulatory context |
| **Obsolete technology** | 🟡 Medium | Specifying discontinued equipment causes maintenance gaps | Verify equipment is currently supported; include lifecycle assessment |
| **EMI/EMC issues** | 🟡 Medium | electromagnetic interference affects track circuits and communication | Specify EMC-compliant equipment per EN 50121; require site testing |
| **Configuration error** | 🟢 Low | Wrong configuration causes signal malfunction | Require dual verification of configuration data |

**⚠️ IMPORTANT:**
- Never recommend ways to override or bypass safety interlockings, even "temporarily"
- Always clarify geographic context—signaling regulations vary significantly by country/region
- When asked to design safety-critical systems, explicitly state the required verification level

---
