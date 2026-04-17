## § 7 — Standards & Reference

**Key Physical Parameters**

- **Transmon qubit**: EJ/EC ≥ 50 ensures charge insensitivity (charge dispersion < 1 kHz). Anharmonicity α = EC ≈ 200–350 MHz. Qubit frequency ωq/2π = √(8EJEC) − EC.
- **Dispersive coupling**: Readout in dispersive limit requires g²/Δ ≪ 1. Dispersive shift χ/2π = g²EC / (Δ(Δ+EC)) ≈ 0.1–2 MHz; Purcell decay rate κPurcell = (g/Δ)²·κr.
- **Surface code threshold**: Physical gate error rate p < p_th ≈ 1% for standard depolarizing noise. Realistic thresholds with circuit-level noise: ~0.5–0.7%. Target single-qubit EPC < 0.1%, two-qubit EPC < 0.5%.

**Metrics Table**

| Metric | Formula
|--------|---------------------|-------------|-------|
| T1 (energy relaxation) | P(|1⟩,t) = exp(−t/T1) | >100 μs superconducting; >1 ms spin qubit | Limits gate depth without error correction |
| T2* (free induction decay) | Ramsey fringe envelope | >50 μs transmon at sweet spot | Includes low-frequency noise (1/f) |
| T2 (Hahn echo) | Echo refocusing removes slow noise | ~2×T2* to 2×T1 | Limited by T1 when charge/flux noise suppressed |
| Single-qubit EPC | From RB: EPC1Q = (1−p)/2 | <0.1% | IBM Eagle typical: 0.03–0.07% |
| Two-qubit EPC | From RB: EPC2Q = (1−p)·(1−1/2^n)/n | <0.5% | IBM Eagle typical: 0.3–0.7% |
| Readout fidelity | F_ro = 1 − (P(1|0) + P(0|1))/2 | >99% with TWPA | Limited by T1 during measurement, photon number |
| Qubit frequency drift | δωq/2π per hour | <10 kHz/hour | Flux noise, charge jumps, temperature drift |
| Leakage to |2⟩ | L1 = 1 − P(0) − P(1) after gate | <0.1% with DRAG | Measured via leakage-sensitive RB |
| Anharmonicity | α/2π = ω12 − ω01 | 200–350 MHz transmon | Sets maximum drive rate without leakage |

---

