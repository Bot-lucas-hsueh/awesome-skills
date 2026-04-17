## § 4 — Core Philosophy

```
          AUTOMOTIVE PERCEPTION DESIGN SPACE
    +------------------------------------------------+
    |  SENSORS                                       |
    |  Camera(s) --> Intrinsic/Extrinsic Calibrated  |
    |  LiDAR(s)  --> Voxelized
    |  Radar(s)  --> Doppler + CFAR detections        |
    +----------+----------+-----------+--------------+
               |          |           |
    +----------v----------v-----------v--------------+
    |         FEATURE EXTRACTION (per modality)      |
    |  Img backbone (ResNet/Swin) | VoxelEncoder      |
    +----------+------------------+------------------+
               |       BEV PROJECTION                |
    +----------v-------------------------------------|
    |  BIRD'S EYE VIEW (BEV) FEATURE MAP             |
    |  [Lift-Splat-Shoot | BEVFormer | Pillar pooling]|
    +----------+-------------------------------------+
               |     FUSION (BEV space)
    +----------v-------------------------------------+
    |  MULTI-MODAL BEV FEATURES                      |
    |  Concatenate / Cross-attention
    +----------+-------------------------------------+
               |     DETECTION
    +----------v-----------+------------------------+
    |  3D Detection Head   | Semantic Seg Head       |
    |  (CenterPoint style) | (HDMapNet style)        |
    +----------+-----------+------------------------+
               |
    +----------v-------------------------------------+
    |  TEMPORAL FUSION + TRACKING                    |
    |  ByteTrack / EKF
    +------------------------------------------------+
```

**Guiding Principle 1 — BEV as Common Currency**: All sensor modalities should be projected into a unified BEV representation before fusion. This decouples the sensor-specific processing from the task-specific heads and simplifies multi-modal alignment.

**Guiding Principle 2 — Accuracy Without Latency is Irrelevant**: A model achieving 75 NDS at 200ms is less valuable than 68 NDS at 35ms for real-time AV deployment. Always report the Pareto frontier.

**Guiding Principle 3 — Production is the Ground Truth**: Benchmark numbers on nuScenes are directional indicators. Real validation requires testing on the production sensor configuration, in production-representative weather and lighting conditions.

---
