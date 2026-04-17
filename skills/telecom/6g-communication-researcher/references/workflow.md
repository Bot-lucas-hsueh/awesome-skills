## 8. Standard Workflow

### Phase 1 — Research Problem Formulation and Channel Model Setup

**Steps:**
1. Map research question to specific IMT-2030 KPI gap; state the KPI being addressed and current shortfall.
2. Select target frequency band; compute Rayleigh distance (2D²/λ) for proposed array aperture D; determine near-field vs far-field regime.
3. Configure channel model: select 3GPP TR 38.901 scenario (UMi, UMa, InH, InF) or QuaDRiGa; extend to target frequency with path loss model from ITU-R P.1411 or measured data.
4. Compute molecular absorption loss via ITU-R P.676 at target frequency/humidity; include in link budget.
5. Establish baseline performance using classical algorithm (MMSE estimator, MRT/ZF precoder, OFDM modulation) with exact parameter configuration documented.

**[✓ Done]** criteria: Link budget closes with realistic hardware (NF, PA backoff, quantization noise); baseline performance reproducible within ±0.5 dB with published simulation parameters.
**[✗ FAIL]** criteria: Link budget assumes idealized hardware (0 dB NF, linear PA, infinite resolution ADC) — restart with impairment-aware model.

### Phase 2 — Algorithm Design, Simulation, and Ablation

**Steps:**
1. Formulate algorithm objective as explicit optimization problem (sum-rate maximization, MSE minimization, outage probability bound).
2. Derive theoretical performance bound (Shannon capacity, Cramér-Rao bound, or MMSE Wiener filter floor) as upper bound on achievable performance.
3. Implement proposed algorithm; verify against bound and baseline on canonical test cases before full simulation.
4. Run Monte Carlo simulation: minimum 1000 channel realizations per SNR point; report 95% confidence intervals on BER/rate curves.
5. Ablation: isolate each design choice (array size, codebook resolution, neural network depth) with single-variable controlled experiments.

**[✓ Done]** criteria: Performance gain over baseline is >0.5 dB or >5% throughput improvement; gain is statistically significant (p<0.05); complexity analysis shows feasible implementation.
**[✗ FAIL]** criteria: Performance gain disappears when hardware impairments are included — design must be impairment-robust; re-examine phase noise sensitivity.

### Phase 3 — System-Level Validation and Publication

**Steps:**
1. Scale from link-level to system-level: implement inter-cell interference, mobility (Doppler), and multi-user scheduling.
2. Validate against standardized evaluation methodology (ITU IMT-2030 evaluation guidelines or 3GPP system simulation assumptions).
3. Quantify complexity: FLOPS per channel use, memory footprint, online adaptation overhead for AI-based schemes.
4. Document reproducibility: random seeds, dataset version, exact software environment (MATLAB R2024b, Python 3.11, Sionna 0.18).
5. Compare to IMT-2030 KPI targets; state gap and propose roadmap for closing it.

**[✓ Done]** criteria: System-level results within factor of 2 of IMT-2030 KPI target; complexity budget compatible with IMT-2030 processing power assumption.
**[✗ FAIL]** criteria: System-level gain is less than 20% of link-level gain — interference model or mobility model likely oversimplified; revisit inter-cell coordination assumptions.

