## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Calibration Drift** | 🔴 Critical | Extrinsic calibration between LiDAR and camera degrades with thermal cycles and vibration, causing misaligned projections and ghost detections | Re-calibrate every 200 operating hours; implement online calibration residual monitoring using feature correspondences |
| **Time Synchronization Errors** | 🔴 Critical | IMU at 400Hz and camera at 30Hz with no hardware sync causes up to 16ms temporal misalignment, corrupting visual-inertial odometry | Use hardware trigger GPIO lines; implement software PTP (IEEE 1588) with < 1ms jitter; log stamp offsets |
| **Point Cloud Sparsity at Range** | 🟡 Warning | LiDAR density drops as 1/r²; objects beyond 50m have < 5 points, causing detection failures for small obstacles | Fuse with radar for long-range; use range-conditioned detection thresholds; flag low-confidence detections |
| **Dynamic Object Contamination in Maps** | 🟡 Warning | Moving pedestrians/vehicles get baked into SLAM maps, causing localization drift and spurious obstacles | Apply moving object removal (MOT + map filtering); use occupancy map with decay; validate map freshness |
| **Edge GPU Thermal Throttling** | 🟡 Warning | Jetson Orin throttles from 60W to 15W at 85°C, causing inference latency spikes from 25ms to 120ms | Implement active cooling; monitor tegrastats; use power budget-aware model switching (fast vs accurate) |
| **Adversarial LiDAR Spoofing** | 🟢 Low | Replay attacks or laser spoofing can inject phantom objects in safety-critical environments | Cross-validate detections across modalities; implement temporal consistency checks; anomaly scoring |
