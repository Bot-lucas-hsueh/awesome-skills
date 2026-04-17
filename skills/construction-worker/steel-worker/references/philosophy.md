## § 4 · Core Philosophy

### 4.1 Rebar Design Decision Matrix

```
                    ┌─────────────────────────────────────┐
                    │     DETERMINE STRUCTURAL FUNCTION    │
                    │  (beam, column, wall, slab, footing) │
                    └──────────────┬──────────────────────┘
                                   │
        ┌──────────────────────────┼──────────────────────────┐
        │                          │                          │
┌───────▼────────┐      ┌──────────▼──────────┐    ┌────────▼────────┐
│ TENSION ZONE   │      │ COMPRESSION ZONE     │    │  SHEAR REGION   │
│ (bottom of     │      │ (top of column,      │    │  (stirrups,     │
│  beams/slabs)  │      │  top of beams)       │    │   ties)         │
└───────┬────────┘      └──────────┬──────────┘    └────────┬────────┘
        │                          │                          │
        ▼                          ▼                          ▼
┌───────────────────┐   ┌─────────────────────┐    ┌──────────────────┐
│ Main bars required│   │ Main bars +         │    │ Shear reinf.     │
│ + development     │   │ confinement ties    │    │ per ACI 318      │
│ + splice location │   │ per ACI 318         │    │ §11.4            │
└───────────────────┘   └─────────────────────┘    └──────────────────┘
```

Rebar placement is not random—every bar addresses a specific structural demand.

### 4.2 Guiding Principles

1. **Cover is Structural**: Concrete cover protects rebar from corrosion and provides fire resistance. Less cover = less durability = shorter structural life.
2. **Development is Non-Negotiable**: The bar must be fully developed before it can reach its yield strength. Under-development is a code violation.
3. **Constructability Drives Detailing**: A theoretically correct rebar layout that cannot be placed is worthless. Detail for field installation.

---

