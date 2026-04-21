## 7. Standards & Reference

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
