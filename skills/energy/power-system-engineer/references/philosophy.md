## § 4 · Core Philosophy

### 4.1 The N-1 Reliability Framework

```
                    ┌─────────────────────────────────────────┐
                    │           System Planning               │
                    │         (Generation + Transmission)      │
                    └─────────────────────────────────────────┘
                                    │
           ┌────────────────────────┼────────────────────────┐
           │                        │                        │
    ┌──────▼──────┐         ┌──────▼──────┐         ┌───────▼──────┐
    │  Contingency │         │  Contingency │         │  Contingency │
    │   Analysis   │         │   Analysis   │         │   Analysis   │
    │  (N-1 most   │         │  (N-1 severe │         │   (N-1 gen   │
    │   severe)    │         │   double)    │         │   loss)      │
    └──────┬──────┘         └──────┬──────┘         └──────┬──────┘
           │                        │                        │
           └────────────────────────┼────────────────────────┘
                                    │
                    ┌─────────────────────────────────────────┐
                    │      Acceptance Criteria Met?          │
                    │  • Voltage: 0.95-1.05 pu per ANSI C84.1│
                    │  • Thermal: <100% continuous rating     │
                    │  • Stability: CCT > critical clearing  │
                    └─────────────────────────────────────────┘
```

The N-1 criterion requires that the system remain stable and within operational limits after any single element (generator, transformer, line) is lost. All planning studies must demonstrate compliance.

### 4.2 Guiding Principles

1. **Reliability is Non-Negotiable**: Design to N-1 contingency—plan for the loss of any single element without cascading failure
2. **Standards Are the Baseline**: Apply IEEE, IEC, NERC standards as default—deviation requires documented technical justification
3. **Quantify Everything**: Specify exact values (voltage limits in pu, thermal ratings in MVA, fault levels in kA) not qualitative terms
4. **Safety Before Economy**: Arc flash, grounding, and protection design default to conservative—cost optimization comes after safety margins are met

---

