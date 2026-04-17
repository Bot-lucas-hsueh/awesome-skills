## § 4 Core Philosophy

### Mental Model: The Simulation Coverage Pyramid

```
                    ▲

                  / C \    ← Critical
                 /─────\      3-sigma events, adversarial NPC, sensor failure

               /─────────\  ← Boundary Cases (uncommon, tested systematically)

             /─────────────\

           /─────────────────\  clear weather, standard intersections, highway cruise
          ───────────────────────
          Real-World Distribution
```

**Pyramid Principle**: Nominal scenarios validate correctness; boundary scenarios validate robustness; critical scenarios validate safety margins. All three tiers must be covered — over-indexing on nominal gives false confidence.

### Guiding Principles

1. **Fidelity is a spectrum, not a binary**: Match sensor model fidelity to the validation question. Behavioral tests can use simplified sensor proxies; perception model validation requires physics-accurate simulation. Never use high-fidelity simulation where it adds cost without proportional coverage benefit.

2. **Scenarios are first-class software artifacts**: Version-control all scenarios (OpenSCENARIO files, map assets, NPC behavior scripts) with semantic versioning. Treat scenario deprecation with the same rigor as API deprecation — failed scenarios are regressions.

3. **Coverage is a KPI, not a feature**: Define Scenario Coverage Index (SCI) as a primary engineering metric alongside recall and precision. Report SCI trends in every sprint review. A simulation platform with no coverage metric is a data generator, not a validation system.

---

