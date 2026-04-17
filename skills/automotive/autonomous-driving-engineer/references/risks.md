## § 3 — Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|--------------------|------------|
| Incorrect sensor fusion leading to phantom objects | CRITICAL | False braking/swerving causing rear-end collision | Dual-independent detection paths; ASIL-D safety monitor with probabilistic gating |
| Over-reliance on HD map in unmapped/stale zones | HIGH | Navigation into construction zone or wrong-way driving | Map confidence layer; graceful degradation to camera-only lane keeping |
| MPC solver timeout causing stale control output | CRITICAL | Vehicle follows last command, potential runaway | Watchdog timer; safe-stop actuator command on solver timeout >5ms |
| Adversarial patch attacks on DNN perception | HIGH | Stop-sign misclassification; pedestrian miss-detection | Ensemble models; physics-based sanity checks; LiDAR corroboration |
| SOTIF unknown unsafe scenarios in ODD | CRITICAL | Undetected hazard causing fatality | Systematic ODD definition; SOTIF Part 2 scenario coverage analysis |
| Software update regression in production fleet | HIGH | Fleet-wide functional regression post-OTA | Shadow mode validation; canary rollout; automated regression gate |
| Thermal throttling of compute platform on hot day | MEDIUM | Increased inference latency, reduced sensor fusion rate | Thermal design margin; watchdog on compute latency; fan control loop |

> **IMPORTANT**: This skill provides engineering guidance only. All AV software must undergo formal safety validation per applicable standards (ISO 26262, ISO 21448, UN-ECE WP.29) before deployment on public roadways. Field testing without appropriate permits, insurance, and safety drivers is illegal in most jurisdictions.

---
