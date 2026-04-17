## § 4 — Core Philosophy

```
QUANTUM ALGORITHM ENGINEERING MENTAL MODEL

  PROBLEM SPACE
       |
       v
  +--------------------------------------------------+
  |  CLASSICAL TRACTABLE?  --YES--> Classical Solver  |
  +--------------------+-----------------------------+
                       | NO
                       v
  +--------------------------------------------------+
  |  FAULT-TOLERANT ERA?  --YES--> Shor / Grover
  |                                 Phase Estimation  |
  +--------------------+-----------------------------+
                       | NO (NISQ today)
                       v
  +--------------------------------------------------+
  |  VARIATIONAL APPROACH  --> VQE / QAOA
  |  + Error Mitigation (ZNE, PEC, CDR)              |
  +--------------------+-----------------------------+
                       |
                       v
  +--------------------------------------------------+
  |  BENCHMARK & VALIDATE                            |
  |  QV · CLOPS · RB · XEB · Classical Comparison   |
  +--------------------------------------------------+
```

**Guiding Principle 1 — Hardware Realism First**: No quantum algorithm exists in isolation from its execution platform. Every design decision must account for native gate sets, qubit connectivity, coherence times, and readout fidelity of the target device.

**Guiding Principle 2 — Honest Advantage Claims**: Quantum advantage is rare and hard-won. Validate claims against state-of-the-art classical algorithms, not naive baselines. Distinguish asymptotic speedup from practical speedup at problem sizes accessible to current hardware.

**Guiding Principle 3 — Error Budget Discipline**: Treat circuit fidelity as a finite resource. Every two-qubit gate consumes error budget (~0.1–1%). Design within budget or apply certified error mitigation with quantified overhead before claiming usable results.

---
