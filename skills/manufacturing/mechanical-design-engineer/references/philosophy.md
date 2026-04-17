## § 4 Core Philosophy

```
┌─────────────────────────────────────────────────────────────────┐
│              MECHANICAL DESIGN DECISION FLOW                     │
│                                                                 │
│  REQUIREMENTS ──► CONCEPT ──► CAD ──► GD&T ──► DFM/DFA        │
│       │             │          │         │           │           │
│   [User needs]  [Sketch &    [3D model] [Tolering]  [Mold flow] │
│   [Performance]  prototype]                            │
│                                                            │
│       ▼            ▼          ▼         ▼           ▼           │
│  TOLERANCE STACK ──► DFMEA ──► FEA ──► DRAWING ──► TOOLING   │
│   [RSS/Worst]    [RPN calc]  [Stress] [Release]   [Prototypes] │
│                                                            │
│  GATE REVIEWS: Concept Review → Design Review → Tooling Buyoff │
│  EXIT CRITERIA: All DFM issues closed, DFMEA RPN < 100, FOS > 1.5│
└─────────────────────────────────────────────────────────────────┘
```

**Principle 1 — Manufacturability Before Tolerancing:** Design the geometry for the process first; tight tolerancing without DFM optimization is wasted effort. A well-designed part with loose tolerances beats a poorly-designed part with tight tolerances.

**Principle 2 — GD&T Controls Function, Not Geometry:** Every GDOT symbol must map to a measurable functional requirement. If you cannot define how to inspect it, do not specify it.

**Principle 3 — Variation Is Inevitable; Scatter Is Quantifiable:** Use Cpk and process capability studies. At production scale, variation compounds — plan for it mathematically, not experimentally.

---

