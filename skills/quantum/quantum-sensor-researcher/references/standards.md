## § 7 — Standards & Reference

**Key Sensitivity Limits and Metrics**

- **Standard Quantum Limit (projection noise)**: δφ_SQL = 1/√N per measurement. For gravimetry: δg = δφ/(k_eff·T²) where k_eff = 2×(2π/λ) and T is free-fall time.
- **Heisenberg Limit**: δφ_HL = 1/N. Only achievable with maximally entangled (GHZ) states. Realistic squeezing provides δφ_sq = ξ/√N where ξ² < 1 is the Wineland spin squeezing parameter.
- **Quantum Fisher Information**: F_Q bounds sensitivity: δφ ≥ 1/√(n·F_Q) where n is number of measurements. For pure states, F_Q = 4·Var(Ĥ)/ℏ² where Ĥ is the generator.

**Metrics Table**

| Metric | Formula / Definition | Target
|--------|---------------------|------------------------|-------|
| Gravimeter sensitivity | δg = δφ/(k_eff·T²) | 10^−9 g/√Hz (lab), 10^−7 g/√Hz (portable) | T = free-fall time; k_eff = 2×2π/780nm for Rb |
| Gravity gradiometer | Γ = (g₁−g₂)/Δz | 1–10 E/√Hz (1 E = 10^−9 s^−2) | Rejects common-mode laser noise and vibration |
| SQUID field sensitivity | δB = √(S_Φ/A²_eff) | 1–10 fT/√Hz (SQUID + flux concentrator) | S_Φ: flux noise PSD; A_eff: effective loop area |
| NV-center DC sensitivity | δB_DC = 1/(γ_e·C·√(N·T₂)) | 1–100 nT/√Hz (single NV), 1 pT/√Hz (ensemble) | γ_e = 28 GHz/T; C = contrast; N = NV number |
| Optical clock instability | σ_y(τ) = (1/Q)·(1/(SNR·√τ)) | 10^−18 at τ = 10^4 s (Sr, Yb lattice clocks) | Q = ν/Δν; SNR limited by atom shot noise |
| Allan deviation (white noise) | σ_y(τ) = σ_0/√τ | σ_0 = white noise floor | Slope −1/2 on log-log plot |
| Ramsey fringe contrast | C = (P_max − P_min)/(P_max + P_min) | >0.9 in optimized systems | Contrast loss: decoherence, detection noise, inhomogeneous broadening |
| Spin squeezing parameter | ξ² = N·Var(Jz_min)/⟨Jx⟩² | ξ² < 1 for squeezing; >−10 dB achieved | Wineland parameter; sets factor of improvement below SQL |
| Atom shot noise | δN/N = 1/√N | N ~ 10^6 atoms: δN/N ~ 10^−3 | Fundamental Poissonian counting noise |

---

## Phase 1 — Sensing Platform Design
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

