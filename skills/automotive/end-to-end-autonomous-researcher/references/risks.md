## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| Open-loop metric overfit | 🔴 Critical | Models optimized for L2 displacement can have worse closed-loop driving performance; open-loop SOTA does not guarantee real-world safety | Always pair open-loop with at least CARLA closed-loop eval; use nuPlan reactive benchmark as minimum bar |
| Imitation learning covariate shift | 🔴 Critical | BC-trained policies fail catastrophically on states outside training distribution, especially recovery from near-collision states | Use DAgger or online IL; augment with adversarial perturbations; evaluate OOD robustness explicitly |
| Benchmark data leakage | 🟡 High | nuScenes test set contamination via overfit to val set or public leaderboard submissions inflates reported numbers | Use strict train/val splits; report results on official test server with single submission |
| Compute cost underestimation | 🟡 High | E2E models (BEVFormer-Large) require 8xA100 for 24h+ training; reproducing SOTA requires significant cloud budget | Report exact GPU-hours and hardware specs; provide lightweight ablation configs |
| Sim-to-real generalization gap | 🟡 High | CARLA closed-loop scores do not directly translate to real-world performance; domain randomization is insufficient for sensor realism | Validate on real vehicle data; use domain adaptation techniques; report gap explicitly |
| Adversarial robustness blind spots | 🟢 Medium | E2E models lack explicit scene graph; adversarial patches on road signs or spoofed LiDAR points can cause silent failures | Include adversarial evaluation in safety analysis; do not deploy without red-team testing |

---
