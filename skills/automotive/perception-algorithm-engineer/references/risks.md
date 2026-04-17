## § 3 — Risk Disclaimer

| Risk | Severity | Domain Consequence | Mitigation |
|------|----------|--------------------|------------|
| False negative on pedestrian at night | CRITICAL | Collision with undetected person | Multi-modal corroboration; nighttime-augmented training data; minimum detection recall gate |
| LiDAR rain/snow point cloud corruption | HIGH | Ghost detections or missed real objects | Weather-robust preprocessing; radar corroboration; weather detector module |
| Camera intrinsic drift over temperature | HIGH | Systematic misalignment in projection-based fusion | Online calibration monitoring; temperature-compensation model; re-calibration trigger |
| Temporal ID switch on fast-moving objects | MEDIUM | Track loss causing planning hesitation | Appearance embedding in tracker; re-identification module; Kalman velocity gating |
| Quantization error degrading model accuracy | HIGH | Production model underperforms vs. FP32 benchmark | Int8 calibration with representative data; per-layer sensitivity analysis; accuracy gate |
| Adversarial objects (sticker patches) | HIGH | Stop-sign misclassification; pedestrian suppression | Ensemble detection; LiDAR geometry validation; anomaly detection on classifier confidence |
| Out-of-distribution sensor configuration | MEDIUM | Model trained on 64-beam LiDAR fails on 32-beam | Beam-drop augmentation during training; beam-agnostic voxelization |

> **IMPORTANT**: Perception systems for autonomous driving are safety-critical. All models deployed in vehicles must undergo validation against representative real-world datasets, adversarial scenario testing, and integration testing with downstream planning/control modules before production deployment.

---
