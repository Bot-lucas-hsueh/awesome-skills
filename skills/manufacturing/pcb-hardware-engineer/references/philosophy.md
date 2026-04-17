## § 4 Core Philosophy

```
┌─────────────────────────────────────────────────────────────────┐
│              PCB DESIGN DECISION FLOW                            │
│                                                                 │
│  SCHEMATIC ──► STACKUP ──► COMPONENT PLACEMENT ──► ROUTING     │
│       │            │              │                 │           │
│   [Decoupling]  [Impedance]   [Partitioning]    [Length match]│
│   [Terminators] [Material]    [Power planes]    [Diff pairs]  │
│                                                            │
│       ▼            ▼              ▼                 ▼           │
│  SI/PI ANALYSIS ──► EMC OPTIMIZATION ──► DFM CHECK ──► OUTPUT │
│   [Eye diagram]   [Filtering]      [DFM rules]    [Gerber]     │
│   [Power noise]   [Shielding]      [Assembly]     [DFF]        │
│                                                            │
│  GATE REVIEWS: Schematic → Stackup → Placement → Routing → DFM │
│  EXIT CRITERIA: SI margins > 20%, EMI < 6dB margin, DFM clean  │
└─────────────────────────────────────────────────────────────────┘
```

**Principle 1 — Stackup Is the Foundation:** Without a proper stackup, SI, PI, and EMC all suffer. Always define stackup with the fab house before starting layout — changing later is expensive.

**Principle 2 — Ground is Reference, Not Noise:** Every signal must have a continuous reference plane. Splitting planes for "clean" and "dirty" power creates impedance discontinuities.

**Principle 3 — Decoupling Is the Backbone:** Each power pin needs local decap within 0.5mm; bulk caps at board entry; use multiple decap values (1μF + 0.1μF + 0.01μF) for broad frequency coverage.

---

