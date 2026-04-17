## § 7 · Standards & Reference

**7.1 Key Formats and Frameworks:**

| Format/Framework | Version | Key Features | Use Case |
|-----------------|---------|-------------|---------|
| OpenDRIVE | 1.6 (ASAM) | Road/junction topology, lane sections, road objects, signals | Simulation (CARLA), planning tools, interchange format |
| Lanelet2 | v1.2 | Lanelet topology, routing graph, regulatory elements, OSM-based | Autoware, open-source AV stacks, production maps |
| HERE HD Live Map | v3 | Real-time map updates, NDS format, cloud-synced | Commercial L3/L4 systems with OTA map updates |
| OpenStreetMap | — | Crowd-sourced road network; free but SD resolution | Base map layer, map gap detection, crowdsourcing workflows |
| NDS (Navigation Data Standard) | 2.x | Tile-based, compressed, efficient for embedded | Production navigation chips and embedded AV systems |
| Apollo HD Map | v2 | Protobuf-based, Baidu Apollo integration | Apollo-based robotaxi deployments |

**7.2 Key Metrics and Targets:**

| Metric | Formula | Target Value | Notes |
|--------|---------|-------------|-------|
| Lateral localization accuracy | abs(lateral_error) in map frame vs. ground truth | < 10 cm | Minimum for lane-level positioning |
| Absolute position accuracy | sqrt(dx^2 + dy^2) vs. surveyed reference | < 0.3 m | GPS-anchored map accuracy |
| Online MapTR IoU (lane divider) | Intersection
| Online MapTR Chamfer Distance | Mean min-dist between predicted and GT polylines | < 0.5 m | Vectorized prediction quality |
| Map annotation density | Map elements per km^2 (lane lines, signs, markings) | > 500 elements/km^2 urban | Completeness target |
| Map freshness SLA | Time since last verification of map segment | < 48 h construction zone, < 30 days stable road | Fleet crowdsource update target |
| Localization dropout rate | Fraction of frames with NDT fitness < threshold | < 0.1% | NDT fitness threshold: 0.5 |
| Tile loading latency | Time to load map tiles for current position | < 50 ms | Streaming tile server requirement |

---

## Phase 1 — Survey and Map Building

**Steps:**
1. Plan survey routes: 3+ passes per road segment for statistically robust point cloud; ensure all lane markings captured at > 60 km/h (optimal LiDAR density).
2. Run LiDAR SLAM (LIO-SAM or HDL-SLAM) to build globally consistent map; apply loop closure at known landmarks; GPS-anchor map to WGS84 via GNSS tie points.
3. Extract ground intensity reflectance map from LiDAR returns; identify lane markings as high-reflectance linear features.
4. Generate semantic segmentation of ground features: lane markings, curbs, stop lines from reflectance + geometry.

**[✓ Done]** criteria: LiDAR map covers 100% of planned route; GPS-anchored map has absolute accuracy < 0.3m at tie points; reflectance map shows clear lane marking separation.
**[✗ FAIL]** criteria: Loop closure error > 0.5m; gaps in route coverage > 50m; lane markings not distinguishable in reflectance map.

### Phase 2 — Lane Annotation and Format Export

**Steps:**
1. Import point cloud and reflectance map into RoadRunner or JOSM; annotate lane boundaries as polylines with semantic attributes (solid/dashed, white/yellow, lane width).
2. Build lane graph topology: assign successor/predecessor relations; define lane change permissions; annotate intersection structure with entry/exit lanelets.
3. Annotate regulatory elements: stop lines, speed limits, traffic light positions, crosswalk boundaries; link each regulatory element to its applicable lanelets.
4. Export to target formats: OpenDRIVE 1.6 for CARLA/simulation tools; Lanelet2 OSM format for Autoware; custom protobuf tiles for production server.
5. Run automated QA suite (topology, geometry, completeness checks) — see Phase 3.

**[✓ Done]** criteria: Full lane graph with 100% topology connections; all intersections have entry/exit lanelets; automated QA passes.
**[✗ FAIL]** criteria: Dangling lanelets (no successor at non-terminal position); missing stop lines at any signalized intersection; geometry self-intersection.

### Phase 3 — Automated QA and Validation

**Steps:**
1. Topology checks: verify all lanelets have valid successor/predecessor except route endpoints; check lane change links are bidirectional where permitted.
2. Geometry validation: no lane boundary self-intersections, minimum lane width > 2.5m, maximum curvature < 0.3 m^-1 for highway, < 0.5 m^-1 for urban.
3. Semantic completeness: every signalized intersection has >= 1 stop line; every speed zone transition has annotation; all crosswalks have lanelet2 pedestrian crossing elements.
4. Localization test: drive test vehicle with NDT localization; verify lateral accuracy < 10 cm over 95% of route; log frames where NDT fitness drops below 0.5.
5. Human review: annotators review all QA-flagged segments and correct; second-pass review for new roads.

**[✓ Done]** criteria: Zero automated QA failures; localization accuracy < 10 cm at P95 on test route; human review complete with zero open issues.
**[✗ FAIL]** criteria: Any dangling lanelet unfixed; localization accuracy > 15 cm at P95; any intersection with missing regulatory elements.

---

