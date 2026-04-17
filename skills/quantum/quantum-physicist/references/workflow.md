## § 8 — Standard Workflow

### Phase 1 — Device Bring-Up & Spectroscopy
- [ ] Mount chip in dilution refrigerator; verify < 20 mK at mixing chamber plate
- [ ] Verify thermal equilibration: qubit excited state population < 1% (dark counts from transmission spectroscopy)
- [ ] Perform VNA transmission sweep to identify readout resonator frequencies (4–8 GHz)
- [ ] Drive qubit spectroscopy (two-tone) to find qubit transition frequency ωq
- [ ] Measure anharmonicity via two-photon spectroscopy (ω02/2 ≠ ω01)
- [✓ Done] Qubit and resonator identified; dispersive shift χ measured; Q_internal > 10^5
- [✗ FAIL] No qubit signal visible — check junction oxidation, dilution fridge wiring attenuation, and drive power calibration

### Phase 2 — Coherence Characterization
- [ ] T1 measurement: inversion recovery sequence (π → delay → readout), fit to exp(−t/T1)
- [ ] T2* measurement: Ramsey sequence (π/2 → delay → π/2), fit to Gaussian decay envelope
- [ ] T2 measurement: Hahn echo (π/2 → delay/2 → π → delay/2 → π/2)
- [ ] CPMG sequence (N echo pulses) to extract noise spectral density S(ω)
- [ ] Identify dominant decoherence: T2 ≈ 2T1 → limited by T1; T2 ≪ 2T1 → dephasing noise
- [✓ Done] T1 > 50 μs, T2 > 50 μs; noise spectral density dominated by identifiable mechanism
- [✗ FAIL] T1 < 10 μs at sweet spot — likely TLS or quasiparticle poisoning; inspect junction quality and substrate

### Phase 3 — Pulse Calibration
- [ ] Calibrate π pulse amplitude via Rabi oscillation (driving until population inversion)
- [ ] Fine-tune pulse via ALLXY protocol (21 gate pairs; ideal: [1,1,0.5,0.5,0.5,...]  )
- [ ] Implement DRAG: optimize β parameter to suppress |2⟩ leakage while maintaining gate fidelity
- [ ] Two-qubit gate calibration (CZ or CR): tune drive frequency, amplitude, and duration
- [ ] Verify two-qubit gate via Bell state preparation + tomography (expect F > 99%)
- [✓ Done] Single-qubit EPC < 0.1% from RB; two-qubit EPC < 0.5% from two-qubit RB
- [✗ FAIL] ALLXY shows systematic Z-rotation bias — recheck LO frequency calibration and IQ mixer imbalance

### Phase 4 — Benchmarking & System Integration
- [ ] Run standard RB (50+ random sequences, depths [1,2,4,8,16,32,64,128 Clifford]); fit decay p
- [ ] Run Interleaved RB for each target gate to extract per-gate EPC
- [ ] Multi-qubit: run simultaneous RB to detect crosstalk; compare individual vs simultaneous EPCs
- [ ] Stabilizer measurement: implement ancilla-based parity readout for surface code plaquette
- [ ] Extract syndrome extraction speed and measurement fidelity; compare to threshold requirements
- [✓ Done] All qubits meet individual and simultaneous benchmarks; syndrome fidelity > 97%
- [✗ FAIL] Simultaneous RB EPC > 2× individual RB — crosstalk present; increase qubit frequency spacing or add echo sequences

---

