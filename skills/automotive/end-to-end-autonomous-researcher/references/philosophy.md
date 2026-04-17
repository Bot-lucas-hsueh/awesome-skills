## § 4 · Core Philosophy

```
         END-TO-END AUTONOMOUS DRIVING MENTAL MODEL
         ============================================

  Raw Sensors                  Unified BEV Space              Structured Output
  +-----------+               +------------------+           +------------------+
  | Camera x N|--LSS/BEVFormer| BEV Feature      |--Queries--| Agent Tracks     |
  | LiDAR     |--Voxelization | H x W x C        |           | Map Geometry     |
  | Radar     |--Pillar Net   | (t, t-1, t-2)    |           | Occupancy Grid   |
  +-----------+               +------------------+           | Ego Trajectory   |
                                      |                      +------------------+
                              +-------v--------+
                              |  World Model   |
                              |  Future Pred   |
                              |  t+1 ... t+T   |
                              +-------+--------+
                                      |
                              +-------v--------+
                              |  Ego Planner   |
                              |  (IL or RL)    |
                              +----------------+

  EVALUATION PYRAMID:
        ^  Real World (Ground Truth, hardest)
       ^^  Closed-Loop Sim (CARLA, nuPlan, Waymo Sim)
      ^^^  Open-Loop Replay (nuScenes, Waymo OD)
     ^^^^  Offline Metrics (L2, mAP, NDS, FDE)
```

**Guiding Principles:**

1. **Closed-Loop is King** — open-loop metrics (L2 displacement, mAP) are necessary proxies but insufficient evidence of safe driving. Every research claim must be grounded in at least one closed-loop evaluation protocol, even if approximate (PDM-Open, CARLA Town05).

2. **BEV as the Universal Representation** — all sensor modalities should be lifted into a shared BEV coordinate frame before multi-task decoding. This enables geometry-consistent fusion, temporal aggregation via deformable attention, and structured output queries that are interpretable and modular.

3. **Interpretability Through Structure** — prefer architectures with structured intermediate representations (object queries with 3D anchors, lane graph queries, occupancy voxel grids) over fully implicit black-box mappings. Structured outputs enable safety monitoring and failure mode analysis.

---

