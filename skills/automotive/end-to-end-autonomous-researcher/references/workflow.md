## 8. Standard Workflow

### Phase 1 — Research Scoping and Baseline Reproduction

**Steps:**
1. Define evaluation protocol: specify benchmark (nuScenes val / Waymo val v1.4
2. Select baseline architecture matching compute budget and data regime (camera-only vs fusion).
3. Reproduce baseline numbers exactly — set random seeds, use official devkit, match data splits.
4. Profile compute: measure FPS on target hardware (e.g., RTX 4090, Orin), memory usage, training GPU-hours.

**[✓ Done]** criteria: Reproduced baseline within +/-1% of reported metric on official val split.
**[✗ FAIL]** criteria: >3% gap from reported numbers — check augmentation pipeline, learning rate schedule, checkpoint averaging.

### Phase 2 — Architecture Modification and Ablation

**Steps:**
1. Formulate single hypothesis per ablation (e.g., "replacing LSS with BEVFormer encoder improves planning L2").
2. Implement modification; keep all other hyperparameters frozen.
3. Run ablation on 20% val subset first to detect regressions early (saves compute).
4. Run full val ablation; log all metrics including secondary ones (velocity error, attribute error).
5. Perform statistical significance check (bootstrap resampling over scenes, p < 0.05).

**[✓ Done]** criteria: Ablation shows statistically significant improvement on primary metric; no regression on safety-critical collision rate.
**[✗ FAIL]** criteria: Improvement <0.5% on NDS or L2 — likely within noise; require larger ablation or revisit hypothesis.

### Phase 3 — Closed-Loop Validation and Paper Submission

**Steps:**
1. Transfer best open-loop model to closed-loop evaluation (CARLA or nuPlan reactive sim).
2. Run 100+ episodes per scenario type; report mean +/- std; identify failure mode taxonomy.
3. Perform sensitivity analysis: vary weather, traffic density, sensor noise level.
4. Draft paper: evaluation section must clearly delineate open-loop vs closed-loop results.
5. Submit to benchmark leaderboard (nuScenes test server, Waymo eval server) for blind evaluation.

**[✓ Done]** criteria: Closed-loop driving score within 10% of open-loop expectation; failure modes documented.
**[✗ FAIL]** criteria: Closed-loop collapse (driving score < 30%) despite good open-loop — covariate shift; requires DAgger or online training.

