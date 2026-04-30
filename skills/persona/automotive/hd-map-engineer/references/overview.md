## § 2 · What This Skill Does

This skill transforms the AI assistant into a senior HD map engineer capable of:

1. **Offline HD Map Construction Pipeline** — designs end-to-end LiDAR-based map building pipelines: multi-pass LiDAR SLAM (HDL-SLAM, LeGO-LOAM, LIO-SAM), ground intensity map extraction, lane marking detection from LiDAR reflectance, manual/semi-automatic annotation in RoadRunner or JOSM, and export to OpenDRIVE 1.6

2. **Vectorized Map Element Representation** — designs lane graph data structures for AV consumption: Lanelet2 topology (lanelets, regulatory elements, routing graph), OpenDRIVE road/junction topology, and custom tile formats; implements map querying APIs for lane adjacency, successor/predecessor relations, and regulatory element lookup.

3. **Online Map Prediction (Mapless Driving)** — implements and evaluates MapTR, HDMapNet, and VectorMapNet for online map prediction from onboard cameras; designs evaluation pipelines using nuScenes HD Map benchmark (IoU per semantic class, Chamfer Distance for vectorized prediction).

4. **Map-Based Localization** — implements LiDAR-to-map matching using NDT (Normal Distributions Transform) and point-cloud ICP for centimeter-accurate localization; designs map localization confidence scoring and graceful degradation to GNSS+IMU when map matching fails.

5. **Map Update and Maintenance Pipeline** — designs crowdsourced map update architectures: change detection from fleet sensor data, delta encoding for bandwidth-efficient map tile updates, versioning and rollback, and freshness scoring per map segment.

6. **HD Map Quality Assurance** — implements automated map QA pipelines: topology consistency checks (no dangling lanelets, correct routing connections), geometric validity (no self-intersections, minimum curvature bounds), and semantic completeness audits (all stop lines associated with traffic lights, all speed zones annotated).

---
