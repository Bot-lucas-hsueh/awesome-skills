## § 4 · Core Philosophy

```
                    ROBOT PERCEPTION STACK
    ┌─────────────────────────────────────────────────┐
    │  SENSORS                                        │
    │  Camera(s) ──┐                                  │
    │  LiDAR ──────┤──► TIME SYNC ──► PREPROCESSING  │
    │  IMU ────────┘     (PTP/HW)      (filter,crop)  │
    └─────────────────────────────────────────────────┘
                              │
    ┌─────────────────────────▼───────────────────────┐
    │  FEATURE EXTRACTION                             │
    │  Image: backbone(ResNet/ConvNeXt) + FPN neck    │
    │  PC:    voxelize → sparse3D-conv → BEV pillars  │
    │  IMU:   preintegration → bias correction        │
    └─────────────────────────────────────────────────┘
                              │
    ┌─────────────────────────▼───────────────────────┐
    │  PERCEPTION (parallel threads)                  │
    │  ┌──────────┐  ┌──────────┐  ┌──────────────┐  │
    │  │Detection │  │ Semantic │  │ Ego-Motion   │  │
    │  │ 3D BBox  │  │  Segm.   │  │ SLAM
    │  └────┬─────┘  └────┬─────┘  └──────┬───────┘  │
    └───────┼─────────────┼────────────────┼──────────┘
            └─────────────▼────────────────┘
    ┌─────────────────────────────────────────────────┐
    │  FUSION & TRACKING                              │
    │  Multi-object tracker (BYTETrack, OC-SORT)      │
    │  Occupancy grid
    │  Scene graph
    └─────────────────────────────────────────────────┘
                              │
                              ▼ Robot Planning & Control
```

**Principle 1 — Calibration First**: No algorithm compensates for bad calibration. Measure reprojection error (< 0.3px), LiDAR-camera registration error (< 2cm), and IMU noise parameters (Allan deviation) before integration.

**Principle 2 — Fail-Safe Degradation**: Design perception to degrade gracefully. If LiDAR fails, switch to stereo-only SLAM with reduced speed limits. If camera is blinded by sun, rely on LiDAR segmentation. Explicit uncertainty propagation is mandatory.

**Principle 3 — Measure Everything**: Every perception node publishes latency histograms, confidence distributions, and sensor health status. Alerts fire at P95 latency > 2× baseline. Perception KPIs (mAP, ATE) are computed continuously against map-based ground truth.

