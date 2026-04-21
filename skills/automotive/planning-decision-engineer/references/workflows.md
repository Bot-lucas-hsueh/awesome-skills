## 8. Standard Workflow

### Phase 1 — Scenario Analysis and Algorithm Selection

**Steps:**
1. Characterize the driving scenario by ODD: structured highway vs. urban unstructured vs. parking; identify complexity drivers (number of agents, intersection type, occlusion level).
2. Select planning architecture appropriate to scenario: Frenet-frame lattice for structured roads; sampling + optimization for unstructured; MPDM/POMDP for high-uncertainty interactive scenarios.
3. Define cost function components with initial weights: J_total = w_s·J_safety + w_c·J_comfort + w_e·J_efficiency + w_r·J_reference_deviation.
4. Establish baseline using PDM (centerline following with IDM) as a sanity check — if PDM solves the scenario, the planning problem is tractable.

**[✓ Done]** criteria: Algorithm selected with documented rationale; baseline PDM result establishes performance floor.
**[✗ FAIL]** criteria: Chosen algorithm has no published benchmark result for the target ODD — require ablation before deployment.

### Phase 2 — Core Planning Implementation and Tuning

**Steps:**
1. Implement Frenet-frame trajectory generation: sample (T, s_f, d_f) combinations, fit quintic polynomials, compute cost for each candidate.
2. Implement kinematic bicycle model feasibility check: verify curvature κ = d̈/(ṡ²) ≤ κ_max and steering rate within actuator limits.
3. Tune cost function weights via grid search on nuPlan val scenarios; track PDM-Score, collision rate, and comfort metrics separately.
4. Implement fallback: if no feasible trajectory found, return constant-deceleration-to-stop in current lane as safety fallback.
5. Validate planning frequency: profile compute on target hardware; ensure 10 Hz sustained with < 5% deadline misses.

**[✓ Done]** criteria: Planning achieves PDM-Score > 75 on nuPlan val; comfort metrics satisfied in > 98% of frames; no deadline misses.
**[✗ FAIL]** criteria: Planning frequency < 8 Hz; comfort violations > 5% of frames; any null return from planner without fallback.

### Phase 3 — Closed-Loop Integration and Validation

**Steps:**
1. Run closed-loop evaluation on nuPlan reactive benchmark (1000+ scenarios, intelligent agents).
2. Run CARLA adversarial scenarios: cut-in, jaywalker, sudden braking, construction zone.
3. Analyze failure taxonomy: categorize failures as constraint violation, solver timeout, prediction error, or behavior edge case.
4. Implement MPDM extension for 3+ highest-frequency failure scenarios; validate improvement.
5. Perform sensitivity analysis: vary IDM parameters ±30%, verify stability of planning output.

**[✓ Done]** criteria: PDM-Score > 80 on nuPlan reactive; CARLA adversarial pass rate > 90%; failure taxonomy fully documented.
**[✗ FAIL]** criteria: Closed-loop collision rate > 0.5/100km; any undocumented failure mode; comfort violation in > 10% of adversarial scenarios.

---
