## § 8 — Standard Workflow

### Phase 1 — Problem Analysis
- [ ] Identify problem class (optimization, simulation, search, factoring)
- [ ] Determine classical complexity and best classical algorithm baseline
- [ ] Assess whether quantum advantage is asymptotic, practical, or speculative
- [✓ Done] Problem is mapped to quantum Hilbert space with clear qubit encoding
- [✗ FAIL] Classical solver outperforms at the target problem size — reconsider quantum approach

### Phase 2 — Algorithm & Circuit Design
- [ ] Select algorithm family (gate-based, variational, adiabatic)
- [ ] Design qubit encoding (one-hot, binary, unary, Jordan-Wigner)
- [ ] Construct ansatz or oracle circuit; count two-qubit gate depth
- [ ] Transpile to target hardware native gate set and topology
- [✓ Done] Circuit depth is within T1-limited coherence budget (depth x gate_time < T1/10)
- [✗ FAIL] SWAP overhead doubles depth beyond coherence limit — redesign with better qubit mapping

### Phase 3 — Simulation & Error Analysis
- [ ] Validate circuit on statevector simulator (up to 30 qubits) or tensor network
- [ ] Run noisy simulation with hardware-calibrated error model
- [ ] Apply error mitigation (ZNE: fold circuit at scale factors 1,3,5; fit Richardson extrapolation)
- [ ] Estimate shot count for target statistical precision (N_shots >= 1/epsilon^2)
- [✓ Done] Mitigated result within 10% of ideal; overhead no more than 10x shot count
- [✗ FAIL] Mitigation overhead >100x or bias exceeds target — switch to PEC or CDR

### Phase 4 — Hardware Execution & Benchmarking
- [ ] Submit to QPU with runtime error mitigation enabled
- [ ] Run RB to confirm gate fidelities match calibration specs
- [ ] Compute QV and CLOPS for the execution session
- [ ] Compare against classical baseline at identical problem size
- [ ] Document T1/T2 at time of run, gate error rates, readout fidelity
- [✓ Done] Results reproducible across 3+ QPU runs; quantum result at least as good as classical within error bars
- [✗ FAIL] Variance across runs >20% — hardware calibration drift suspected; re-calibrate

---

