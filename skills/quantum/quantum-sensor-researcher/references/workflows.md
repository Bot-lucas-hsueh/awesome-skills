## § 8 — Standard Workflow

### Phase 1 — Sensing Platform Design
- [ ] Define measurand (gravity, B-field, time, rotation, force) and target sensitivity
- [ ] Select quantum sensing platform based on measurand, SWaP, and environment
- [ ] Compute SQL and Heisenberg limit for available atom/photon number N
- [ ] Identify dominant noise sources and set noise budget
- [✓ Done] Platform selected; SQL computed; noise budget shows path to target sensitivity
- [✗ FAIL] Target sensitivity is below Heisenberg limit for available N — increase N or accept classical-quantum hybrid approach

### Phase 2 — Protocol Design & Simulation
- [ ] Design interrogation sequence (Ramsey, Mach-Zehnder, CPMG) for target measurand
- [ ] Compute phase sensitivity and transfer function H(f) from measurand to output signal
- [ ] Simulate Ramsey fringe with realistic decoherence (T2, detection efficiency)
- [ ] Identify systematic error sources and design rejection strategies
- [✓ Done] Protocol designed; sensitivity within factor 2 of SQL; systematic error budget < statistical precision target
- [✗ FAIL] Simulated contrast C < 0.5 — check decoherence time vs interrogation time ratio; reduce T or improve state preparation

### Phase 3 — Calibration & Characterization
- [ ] Characterize noise floor in quiet conditions (atom/photon shot noise limited?)
- [ ] Measure Ramsey fringe: extract contrast C, frequency, linewidth
- [ ] Compute sensitivity: δφ = π/(C·√N_det) per measurement; convert to physical units
- [ ] Collect 1000+ measurements; compute Allan deviation; identify white noise vs flicker floor
- [✓ Done] Allan deviation shows √τ improvement over > 1 hour; SQL-limited performance confirmed
- [✗ FAIL] Allan deviation flattens at τ < 100 s — systematic drift or environmental noise floor identified; must diagnose and mitigate

### Phase 4 — Systematic Error Characterization
- [ ] Identify all relevant systematic shifts (Zeeman, AC Stark, BBR, collisions, wavefront)
- [ ] Measure each systematic shift as function of operating parameter
- [ ] Quantify bias uncertainty contribution to total error budget
- [ ] Implement rejection strategies (differential measurement, modulation, shielding)
- [ ] Verify total systematic uncertainty < 10% of target statistical precision
- [✓ Done] Systematic budget closed; total systematic uncertainty ≤ statistical floor at maximum integration time
- [✗ FAIL] Zeeman shift dominates — implement better magnetic shielding (< 1 nT) and bias field stabilization (< 1 ppm)

---
