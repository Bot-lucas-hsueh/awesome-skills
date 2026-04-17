## § 4 · Core Philosophy

### 4.1 Safety-First Design Framework

```
┌─────────────────────────────────────────────────────────────────┐
│                    BESS DESIGN DECISION TREE                    │
├─────────────────────────────────────────────────────────────────┤
│  Step 1: Application Classification                             │
│  ├── Life Safety Critical → UL 9540 + Fire Marshal + AHJ       │
│  ├── Utility Scale (>1MWh) → NFPA 855 + UL 9540A               │
│  └── Commercial/Industrial → UL 9540 + Local amendments        │
├─────────────────────────────────────────────────────────────────┤
│  Step 2: Chemistry Selection                                    │
│  ├── LFP → Long life, thermal stability, lower energy density   │
│  ├── NMC/NCA → Higher energy, stricter thermal management       │
│  └── LTO → Ultra-fast charge, wide temp range, expensive         │
├─────────────────────────────────────────────────────────────────┤
│  Step 3: Architecture Decisions                                  │
│  ├── Containerized → Outdoor, large scale                       │
│  ├── Rack/Cabinet → Indoor, commercial                          │
│  └── Distributed → Retrofit, space-constrained                  │
├─────────────────────────────────────────────────────────────────┤
│  Step 4: Safety Systems                                         │
│  ├── Detection → Smoke, gas (H2, CO), temperature               │
│  ├── Suppression → Novec, FM-200, water mist                   │
│  ├── Ventilation → HVAC, explosive gas dilution                 │
│  └── Monitoring → BMS, SCADA, remote surveillance               │
└─────────────────────────────────────────────────────────────────┘
```

The safety framework moves from application requirements → chemistry selection → physical architecture → protective systems. Each decision constrains the next.

### 4.2 Guiding Principles

1. **Verify Before Specifying**: Never specify components without confirming UL listing status; thermal runaway propagation must be characterized via UL 9540A
2. **Design for Failure**: Assume any cell can fail; engineer containment, detection, and suppression at each level (cell → module → rack → container)
3. **Quantify Everything**: Specify exact C-rates, temperatures, efficiencies, and tolerances; vague requirements lead to scope disputes
4. **Life-Cycle Economics**: Design for 10,000+ cycles at 80% DoD; calculate LCOS including O&M, replacement, and decommissioning costs

---

