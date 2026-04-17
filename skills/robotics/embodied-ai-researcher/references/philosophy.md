## § 4 — Core Philosophy

```
                    EMBODIED AI RESEARCH MENTAL MODEL
                    ==================================

        Real World                          Simulation
        ──────────                          ──────────
        [Robot HW] <── policy(obs) ──> action
             |                              |
        [Sensors]──obs──>[Policy]<──obs──[Sim Env]
             |              |               |
        [Human Demos]  [World Model]  [Domain Rand.]
             |              |               |
             └──────────────┴───────────────┘
                            |
                   [Evaluation Benchmark]
                LIBERO / RLBench
                            |
                   [Research Insight]
                   Publication -> Community

    DATA FLYWHEEL:  Demos -> Policy -> Deploy -> Failures -> More Demos
    ABSTRACTION:    Primitives -> Skills -> Tasks -> Long-Horizon Plans
    GENERALIZATION: Single object -> Category -> Novel objects -> Novel tasks
```

**Guiding Principle 1 — Data is the real bottleneck.** Architecture choices matter far less than data quality and quantity. A well-curated 200-demo dataset with diverse object poses beats a sophisticated model trained on 50 demos. Invest in teleoperation infrastructure and data collection pipelines before architecting the policy.

**Guiding Principle 2 — Evaluate on distribution shift, not i.i.d. performance.** A policy that succeeds 95% on training-distribution objects but only 20% on novel objects is scientifically uninteresting. Always report generalization metrics (novel object poses, novel object instances, novel backgrounds) as primary results, not supplementary tables.

**Guiding Principle 3 — Simulation is a tool, not a shortcut.** Simulation accelerates iteration but cannot replace real-world validation. Use sim to debug policy architectures and data pipelines; use real hardware to validate sim2real assumptions at every major milestone. Never submit a paper with only sim results if real-robot experiments are feasible.

---
