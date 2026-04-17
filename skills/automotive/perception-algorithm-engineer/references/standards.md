## § 7 — Standards & Reference

**Key Standards & Benchmarks:**
- **nuScenes** — Standard AV perception benchmark: 1000 scenes, 6 cameras, 1 LiDAR, 5 radars; metrics: NDS, mAP, AMOTA.
- **Waymo Open Dataset** — High-resolution LiDAR+camera; metrics: 3D AP/APH at L1/L2 difficulty.
- **KITTI** — Legacy benchmark: cameras + Velodyne; metrics: 3D AP at easy/moderate/hard.
- **nuScenes Occupancy** — Emerging benchmark for occupancy prediction evaluation.
- **ISO 8855** — Road vehicles: vehicle dynamics and road-holding ability terminology (coordinate systems).

**Performance Metrics Table:**

| Metric | Formula | Target Range | Notes |
|--------|---------|--------------|-------|
| nuScenes NDS | 0.5*mAP + 0.1*(1-mATE) + 0.1*(1-mASE) + 0.1*(1-mAOE) + ... | > 65 (production) | BEVFusion: 72.9 |
| 3D mAP | mean over classes of AP at IoU=0.5/0.25 | > 55 nuScenes | CenterPoint: 58.0 |
| Tracking AMOTA | Sum over classes of MOTA at multiple thresholds | > 0.55 nuScenes | ByteTrack: 0.57+ |
| Inference Latency | ms per frame on target SoC (P95) | < 40 ms on Orin | Full stack budget 100ms |
| Point Cloud Processing | ms per frame for voxelization + backbone | < 15 ms on Orin | CenterPoint pillar: 8ms |
| Calibration Reprojection Error | mean pixel error on calibration target | < 0.5 pixels RMS | LiDAR-camera extrinsic |
| Velocity Estimation Error | mean absolute velocity error (MAVE) | < 0.5 m/s (longitudinal) | Critical for prediction |
| Track ID Switch Rate | ID switches

---

