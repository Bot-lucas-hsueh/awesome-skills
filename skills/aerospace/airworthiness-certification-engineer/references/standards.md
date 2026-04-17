## § 7 Standards & Reference

### DAL Assignment Decision Tree (ARP4754A)
```
Failure Condition Classification (per FHA)?
├─ Catastrophic (probability < 1×10⁻⁹/FH) → DAL A
│   Software: MC/DC structural coverage required
│   Hardware: Complex ASIC requires elemental analysis or structured coverage
├─ Hazardous (probability < 1×10⁻⁷/FH) → DAL B
│   Software: Decision Coverage required (100% of decisions)
│   Hardware: Functional testing + anomaly detection
├─ Major (probability < 1×10⁻⁵/FH) → DAL C
│   Software: Statement Coverage required
│   Hardware: Normal development assurance
├─ Minor (probability < 1×10⁻³/FH) → DAL D
│   Software: Basic lifecycle documentation
└─ No Safety Effect → DAL E
    No specific development assurance required
```

### Compliance Matrix Structure
| Req. No. | Regulatory Requirement | MoC Type | Document Reference | Status | Finding Closure |
|----------|----------------------|----------|-------------------|--------|----------------|
| 25.1309-1 | Equipment/system failure no hazardous effect | Analysis (FTA/FMEA) | SSA-001 Rev C | Open | — |
| 25.571(a) | Damage tolerance evaluation | Analysis + Test | DTA-Rev-4 + TR-123 | Closed | DER-2025-441 |

### Key Probabilities Reference
| Failure Condition | Maximum Probability | Regulatory Reference |
|------------------|--------------------|--------------------|
| Catastrophic | < 1×10⁻⁹ per flight hour | FAR §25.1309(b)(1); CS-25 AMC 25.1309 |
| Hazardous | < 1×10⁻⁷ per flight hour | FAR §25.1309(b)(2) |
| Major | < 1×10⁻⁵ per flight hour | FAR §25.1309(b)(3) |
| Minor | < 1×10⁻³ per flight hour | FAR §25.1309(b)(4) |

