## § 4 Core Philosophy

```
┌──────────────────────────────────────────────────────────────────┐
│           WIDE BANDGAP DEVICE DESIGN HIERARCHY                   │
│                                                                  │
│  MATERIAL PROPERTIES                                             │
│  E_g, E_crit, μ_n, λ_th, ε_r                                   │
│       │                                                          │
│       ▼                                                          │
│  DEVICE ARCHITECTURE                                             │
│  Drift layer (N_D, t_drift), MOS/HEMT structure, termination    │
│       │                                                          │
│       ▼                                                          │
│  FABRICATION PROCESS                                             │
│  Epitaxy → Implant → Gate oxide → Metallization → Passivation   │
│       │                                                          │
│       ▼                                                          │
│  CHARACTERIZATION & QUALIFICATION                                │
│  I-V, C-V, Hall, BV, switching, AEC-Q101                        │
│       │                                                          │
│       ▼                                                          │
│  SYSTEM INTEGRATION                                              │
│  Gate driver, thermal stack, EMI, system efficiency              │
└──────────────────────────────────────────────────────────────────┘
```

**Principle 1 — Material Properties Are Non-Negotiable:** The Baliga figure-of-merit (BFOM = ε × μ × E_crit³) determines the theoretical R_ds(on) limit. SiC has 400× and GaN 1000× BFOM advantage over Si — design to approach this limit.

**Principle 2 — Interface Quality Determines Reliability:** SiC MOS channel mobility is limited by interface traps (D_it ~ 10¹¹–10¹² cm⁻² eV⁻¹). Nitric oxide (NO) annealing reduces D_it by 10×; this single step often determines whether a device qualifies for automotive use.

**Principle 3 — Qualification Is the Product:** A device datasheet value is meaningless without a test escape rate < 1 DPPM and demonstrated field reliability. Design for reliability from the first epitaxial layer, not as an afterthought.

---

