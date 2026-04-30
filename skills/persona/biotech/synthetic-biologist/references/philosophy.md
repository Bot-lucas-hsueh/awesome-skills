## § 4 — Core Philosophy

```
        SYNTHETIC BIOLOGY DESIGN HIERARCHY
        ┌────────────────────────────────────┐
        │         BIOLOGICAL SYSTEM          │
        │    (Cell / Organism
        ├────────────────────────────────────┤
        │         GENETIC DEVICE             │
        │    (Circuit / Pathway
        ├────────────────────────────────────┤
        │         GENETIC PART               │
        │   (Promoter / RBS / CDS
        └────────────────────────────────────┘
              Abstraction + Modularity

        DBTL CYCLE (Iterative Engineering)
        Design → Build → Test → Learn → (repeat)
           ↑_________________________________↓
```

**Principle 1: Characterize Before Composing**

Every genetic part must be characterized in its intended context before being assembled into a larger system. A promoter measured in a reporter context (GFP) may behave 3–10× differently adjacent to a metabolic gene due to mRNA secondary structures at the 5' UTR. Always measure in situ.

**Principle 2: Model First, Then Experiment**

FBA and ODE kinetic models are cheap; fermentation experiments cost $500–$5,000 per run. Build a minimal kinetic model (COBRApy, MATLAB SimBiology) to predict metabolic flux distribution and identify which interventions have the highest theoretical yield impact before building strains.

**Principle 3: Scale-up Is a Separate Engineering Problem**

Lab-scale results (250 mL flask, 30°C, 200 rpm) do not automatically translate to pilot (50 L, pH-controlled, fed-batch) or industrial (10,000 L) scale. Oxygen transfer rate (kLa), mixing time (θ_mix), and CO2 stripping change non-linearly. Plan scale-up as a distinct phase with distinct metrics.

---
