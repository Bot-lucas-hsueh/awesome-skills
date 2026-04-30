## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **Network disruption** | 🔴 High | Single DC failure disrupts entire region—requires contingency planning | Design multi-DC coverage with backup routing; specify 99.5%+ availability |
| **Demand forecast error** | 🔴 High | Network designed for wrong volume causes capacity issues | Use scenario planning with 3 demand scenarios (base, high, low) |
| **Carrier concentration** | 🔴 High | Relying on single carrier creates capacity risk | Require 2+ carriers per lane with volume splits |
| **Regulatory changes** | 🟡 Medium | New DOT regulations, emissions zones affect routing | Build regulatory review into annual network audit |
| **Fuel cost volatility** | 🟡 Medium | Fuel surcharge changes alter route economics | Use fuel-inclusive pricing models; design fuel-efficient routes |

**⚠️ IMPORTANT:**
- Always provide contingency plans for network disruptions
- Geographic scope must be defined before network design—international vs. regional vs. urban have different constraints
- Never recommend removing all redundancy; single points of failure are unacceptable in critical supply chains

---
