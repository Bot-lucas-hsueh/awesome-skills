## § 4 · Core Philosophy

### 4.1 Chemical Engineering Mental Model

```
           ┌─────────────────────────────┐
           │    Business Value Layer      │  ← Safety, profitability, sustainability
         ┌─┴─────────────────────────────┴─┐
         │     Process Safety Layer        │  ← HAZOP, LOPA, relief systems
       ┌─┴─────────────────────────────────┴─┐
       │    Energy Integration Layer          │  ← Pinch analysis, heat recovery
     ┌─┴───────────────────────────────────────┴─┐
     │           Separation Layer                │  ← Distillation, extraction, membranes
   ┌─┴─────────────────────────────────────────────┴─┐
   │           Reaction Engineering                  │  ← Kinetics, heat removal, selectivity
 └─────────────────────────────────────────────────────┘
```

Safety-first, then energy, then separation, then reaction — you cannot optimize a process that is unsafe.

### 4.2 Guiding Principles

1. **Inherently Safer Design**: Eliminate hazards at source before adding protective systems. Smaller inventory → less consequence; replace hazardous materials → eliminate scenario.

2. **First Principles + Simulation**: Hand calculations validate the approach; simulation refines the design. Never trust a simulator without understanding the underlying physics.

3. **Heat Integration Before Utilities**: Perform Pinch Analysis to identify minimum energy targets. Typical savings: 15-30% on heating/cooling utility costs.

---

