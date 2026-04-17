## § 7 · Standards & Reference

**7.1 Key Algorithms and Frameworks:**

| Algorithm/Framework | Reference | Key Innovation | Use Case |
|--------------------|-----------|--------------|---------|
| Frenet-Frame Lattice Planner | Werling et al., ICRA 2010 | Decoupled s/d planning, polynomial trajectories | Highway/structured road planning |
| MPDM (Multipolicy Decision Making) | Galceran et al., ICRA 2015 | Forward simulate policy outcomes, select best expected | Intersection + lane change decisions |
| EPSILON | Chen et al., ICRA 2021 | Game-theoretic interaction-aware planning | Dense urban multi-agent scenes |
| PDM (Privileged Decision Making) | Dauner et al., CoRL 2023 | IDM-based centerline following with reactive replanning | nuPlan SOTA closed-loop planner |
| Contingency Planning | Chen et al., IV 2023 | Maintain N branches for K uncertain agent modes | High-uncertainty scenarios |
| POMDP (DESPOT/POMCP) | Ye et al., 2017; Silver et al. 2010 | Belief-space planning over intention uncertainty | Pedestrian crossing, agent intent |
| IDM (Intelligent Driver Model) | Treiber et al., 2000 | Deterministic car-following with desired headway | Longitudinal speed control |
| MOBIL | Kesting et al., 2007 | Incentive-based lane change with courtesy/safety | Lane change decision logic |

**7.2 Key Metrics and Targets:**

| Metric | Formula | Target Value | Notes |
|--------|---------|-------------|-------|
| nuPlan PDM-Score | Weighted sum: collision, drivable area, TTC, comfort | > 80 (good), > 90 (excellent) | SOTA PDM-Closed: 92.1 |
| Collision Rate (closed-loop) | # collisions / 100 km | < 0.1 / 100 km | From CARLA/nuPlan reactive |
| Planning Frequency | Hz | ≥ 10 Hz motion planner | ≥ 1 Hz behavior planner |
| Trajectory Jerk (longitudinal) | max |s̈̇| over horizon | < 5 m/s³ | ISO 2631 comfort limit |
| Lateral Acceleration | max |ÿ| over horizon | < 3 m/s² | City driving comfort bound |
| Lateral Jerk | max |ÿ̇| over horizon | < 2 m/s³ | Motion sickness threshold |
| Time-to-Collision (TTC) | relative_dist
| Path Smoothness (κ) | max curvature | < 0.2 m⁻¹ (city), < 0.05 m⁻¹ (highway) | Kinematic feasibility |
| MPC Solver Time | ms per planning cycle | < 25 ms (P95) for 35Hz | Leaves margin in 28.5ms cycle |
| Replanning Rate | fraction of cycles requiring full replan | < 5% | High rate indicates instability |

---

## Phase 1 — Scenario Analysis and Algorithm Selection

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

