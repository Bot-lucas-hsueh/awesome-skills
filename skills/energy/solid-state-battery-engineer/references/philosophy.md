## § 4 · Core Philosophy

### 4.1 Solid Electrolyte Selection Matrix

```
┌──────────────────────────────────────────────────────────────────────────────────────┐
│                    SOLID ELECTROLYTE DECISION FRAMEWORK                               │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Step 1: Application Requirements                                                     │
│  ├── Energy Density Priority → Sulfide (highest conductivity, can use Li metal)     │
│  ├── Safety/Temperature Priority → Oxide LLZO (thermal stability, wide temp range)  │
│  └── Processability Priority → Polymer (flexible, roll-to-roll compatible)           │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Step 2: Conductivity vs Stability Trade-off                                          │
│                                                                                       │
│  High ──┬── Li10GeP2S12 (12 mS/cm) ───────────── Sulfide ── High conductivity       │
│        │                                                                     │         │
│        ├── Li6PS5Cl (9 mS/cm) ──────────────── Argyrodite ── Good balance            │
│        │                                                                     │         │
│        ├── Li7La3Zr2O12 (1 mS/cm) ───────────── Oxide ──── Stable but lower          │
│        │                                                                     │         │
│        └── PEO-LiTFSI (0.1 mS/cm) ───────────── Polymer ── Low but easy to process   │
│                                                                                       │
│  Low ──────────────────────────────────────────────── Low stability                  │
│                                                                                       │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Step 3: Interface Compatibility                                                     │
│  ├── With NMC/NCA (4.2V+) → Need protective涂层 (LNO, LiNbO3, Li3PO4)              │
│  ├── With Li metal → LLZO preferred (thermodynamically stable)                       │
│  └── With Sulfide → Very limited cathode compatibility                                │
├──────────────────────────────────────────────────────────────────────────────────────┤
│  Step 4: Manufacturing Considerations                                                 │
│  ├── Sulfide → Solvent-based processing impossible, dry mixing required             │
│  ├── Oxide → High-temp sintering (700-1200°C), expensive equipment                  │
│  └── Polymer → Solution casting, roll-to-roll feasible                               │
└──────────────────────────────────────────────────────────────────────────────────────┘
```

The framework prioritizes application requirements, then evaluates conductivity-stability trade-offs, interface compatibility, and manufacturing scalability at each step.

### 4.2 Guiding Principles

1. **Conductivity is NOT the Bottleneck**: Most solid electrolytes exceed liquid conductivity; the challenge is interfaces, not bulk transport
2. **Mechanical Properties Matter for Dendrites**: High shear modulus (>10 GPa) alone doesn't prevent dendrites; grain boundary engineering is critical
3. **Composite Cathodes are the Hard Part**: 70%+ volume is active material, but must maintain ion percolation
4. **Manufacturing Defines Viability**: Lab cells with hot-presses don't scale; process must be economically feasible

---

