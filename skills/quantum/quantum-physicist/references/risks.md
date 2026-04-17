## § 3 — Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|-------------------|------------|
| Cryogenic safety: LHe/LN2 asphyxiation risk | CRITICAL | Oxygen displacement in confined spaces can be fatal | Install O2 monitors; maintain ventilation; follow established cryogen handling protocols |
| Qubit frequency collision in multi-qubit chips | HIGH | Spectral crowding causes crosstalk; gates fail; frequency tuning space exhausted | Use frequency planning tools (e.g., IBM's frequency allocation algorithm); verify isolated spectra before proceeding |
| TLS-induced T1 degradation post-processing | HIGH | Substrate surface damage introduces new TLS baths; T1 drops 2-10x | Measure T1 at every fabrication step; use Al2O3/SiN passivation; avoid resist residues |
| Thermal photon excitation masking intrinsic T1 | HIGH | Apparent T1 attributed to qubit loss actually dominated by warm-stage thermal photons | Verify qubit excited-state population at thermal equilibrium; add 20+ dB cold attenuation on drive lines |
| Pulse leakage to |2⟩ state | MEDIUM | Gate errors increase; state preparation corrupted; non-unitary leakage undetected by standard RB | Implement DRAG calibration; monitor leakage via leakage RB protocol; verify anharmonicity > 5× drive bandwidth |
| Flux noise causing dephasing in tunable qubits | MEDIUM | T2* < 1 μs in tunable transmons at non-sweet spots; gate fidelity limited by flux line noise | Operate at flux sweet spot; use low-noise bias sources (< 1 nA/√Hz); implement flux feedback stabilization |
| Measurement-induced dephasing | MEDIUM | Strong dispersive measurement drives qubit dephasing during ancilla readout; logical error rates elevated | Optimize readout power to minimize Purcell decay; use parametric amplifiers (TWPA/JPA) to reduce measurement time |

---
