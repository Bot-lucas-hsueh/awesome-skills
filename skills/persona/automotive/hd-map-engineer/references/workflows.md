## 8. Standard Workflow

### Phase 1 — Survey and Map Building

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
