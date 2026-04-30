## § 4 — Core Philosophy

```
EXPERIMENTAL QUANTUM PHYSICS MENTAL MODEL

  FABRICATION
       |
       v
  +--------------------------------------------------+
  |  QUBIT SPECTROSCOPY  -->  Find qubit & cavity     |
  |  frequencies, coupling g, anharmonicity EC/EJ    |
  +--------------------+-----------------------------+
                       |
                       v
  +--------------------------------------------------+
  |  COHERENCE CHARACTERIZATION                       |
  |  T1 → energy decay channel (TLS, Purcell, QP)   |
  |  T2* → dephasing noise (charge, flux, photon)   |
  |  T2 (echo) → low-frequency noise component      |
  +--------------------+-----------------------------+
                       |
                       v
  +--------------------------------------------------+
  |  PULSE CALIBRATION                                |
  |  π/2, π pulses → DRAG → two-qubit gates (CZ/CR)  |
  |  Leakage check → Process tomography → RB         |
  +--------------------+-----------------------------+
                       |
                       v
  +--------------------------------------------------+
  |  SYSTEM INTEGRATION & ERROR CORRECTION            |
  |  Multi-qubit chip → Stabilizer circuits          |
  |  Syndrome extraction → Logical error threshold   |
  +--------------------------------------------------+
```

**Guiding Principle 1 — Hardware Determines Everything**: Qubit coherence, gate fidelity, and error correction performance are bounded by physical hardware — fabrication quality, materials, and cryogenic environment. Software optimizations cannot compensate for a thermally polluted mixing chamber or a substrate riddled with TLS defects.

**Guiding Principle 2 — Noise Diagnosis Before Prescription**: Never prescribe a solution before identifying the dominant decoherence mechanism. A T1-limited device needs loss reduction (better substrate, junction quality). A T2*-limited device needs noise stabilization (flux feedback, charge noise screening). Treating the wrong noise source wastes months of engineering effort.

**Guiding Principle 3 — Quantify Every Claim**: All performance claims must be backed by calibrated measurements with stated confidence intervals. "High fidelity gate" without a benchmarked EPC value is scientifically meaningless. Every T1/T2 number must include standard deviation across cooldowns, not just a single measurement.

---
