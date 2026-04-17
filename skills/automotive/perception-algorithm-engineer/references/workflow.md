## § 8 — Standard Workflow

### Phase 1 — Sensor Configuration Analysis
- **Step 1.1**: Document sensor configuration: camera FoV/resolution/frame rate, LiDAR beams/range/spin rate, radar range/azimuth resolution.
- **Step 1.2**: Compute theoretical detection ranges and coverage gaps; identify blind zones.
- **Step 1.3**: Perform extrinsic calibration verification: compute re-projection errors, check temporal synchronization offsets.
- **Step 1.4**: Select evaluation dataset closest to production sensor configuration (or create internal benchmark).
- [✓ Done] Sensor coverage map; calibration error report < 0.5 pixel RMS; benchmark dataset selected.
- [✗ FAIL] Coverage gaps in safety-critical zones; calibration error > 1 pixel; no benchmark baseline.

### Phase 2 — Architecture Selection & Baseline
- **Step 2.1**: Choose representation: pillar-based (fast, less accurate) vs. voxel-based (accurate, slower) vs. point-based (flexible).
- **Step 2.2**: Select and reproduce a published baseline on the chosen benchmark dataset.
- **Step 2.3**: Profile baseline on target hardware (GPU memory, latency breakdown per module).
- **Step 2.4**: Identify top-3 bottlenecks (memory bandwidth, backbone FLOP, NMS overhead).
- [✓ Done] Reproducible baseline within 1 NDS point of published paper; profiling report.
- [✗ FAIL] Cannot reproduce baseline; latency exceeds budget by > 50%.

### Phase 3 — Model Development & Ablation
- **Step 3.1**: Implement modifications (fusion strategy, temporal module, additional head).
- **Step 3.2**: Run ablation study: one change at a time, measure delta NDS and delta latency.
- **Step 3.3**: Apply data augmentation: GT sampling, random flipping, rotation, scaling, beam drop (for LiDAR robustness).
- **Step 3.4**: Export to ONNX, convert to TensorRT, validate accuracy drop < 1 NDS for Int8.
- [✓ Done] Ablation table showing contribution of each component; TensorRT model with < 1 NDS drop.
- [✗ FAIL] Any component adds latency without measurable accuracy gain; TensorRT accuracy drop > 2 NDS.

### Phase 4 — Integration & Production Validation
- **Step 4.1**: Integrate model into perception pipeline; validate object ID consistency with tracker.
- **Step 4.2**: Test on production-representative data (night, rain, fog, sensor occlusion).
- **Step 4.3**: Run failure mode analysis: log frames where FP/FN occur, cluster by scenario type.
- **Step 4.4**: Set detection confidence thresholds to achieve target recall at acceptable precision.
- [✓ Done] Pedestrian recall > 99% at operating point; integration test suite passing > 95%.
- [✗ FAIL] Any known failure mode without documented mitigation; pedestrian recall < 98%.

---

