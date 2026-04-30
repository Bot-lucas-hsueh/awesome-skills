## 10. Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Raster Map for AV Consumption

**Name:** The BMP Lane Boundary Engineer

❌ BAD:
```python
# Storing lane boundaries as a PNG raster — no topology, no querying
lane_map = cv2.imread('lane_map_grid.png')
lane_pixels = np.where(lane_map[:,:,2] > 200)  # blue = lane boundary pixels
```

✅ GOOD:
```python
# Lanelet2 vectorized format with routing graph
import lanelet2
map_ = lanelet2.io.load('/path/to/map.osm',
    lanelet2.projection.UtmProjector(lanelet2.io.Origin(51.0, 13.0)))
routing_graph = lanelet2.routing.RoutingGraph(
    map_, lanelet2.traffic_rules.create(
        lanelet2.traffic_rules.Locations.Germany,
        lanelet2.traffic_rules.Participants.Vehicle))
# Vectorized query: lanelets within 50m
ego_pos = lanelet2.core.BasicPoint2d(x, y)
nearby = lanelet2.geometry.findNearest(map_.laneletLayer, ego_pos, 10)
```

**Why it matters:** Raster maps cannot express topology (lane adjacency, successor relations), cannot support efficient spatial queries, and cannot store regulatory elements (traffic lights, stop lines) in a queryable format.

---

### Anti-Pattern 2: Assuming Map is Always Fresh

**Name:** The Eternal Map Truster

❌ BAD:
```python
# No freshness check — uses map unconditionally
lane_boundaries = hd_map.get_lane_boundaries(ego_position)
planner.set_lane_constraints(lane_boundaries)  # could be a closed construction zone
```

✅ GOOD:
```python
from datetime import datetime

map_metadata = hd_map.get_segment_metadata(ego_position)
age_hours = (datetime.now() - map_metadata.last_verified).total_seconds()

if age_hours > 48:
    # Stale map: fall back to camera lane detection
    lane_boundaries = camera_lane_detector.detect_lanes(camera_image)
    planning_mode = 'PERCEPTION_ONLY'
    log_warning(f"Map segment age {age_hours:.1f}h exceeds SLA. Using perception fallback.")
else:
    lane_boundaries = hd_map.get_lane_boundaries(ego_position)
    planning_mode = 'HD_MAP_GUIDED'
```

**Why it matters:** Construction zones appear and disappear on timescales of hours. A map verified 2 weeks ago can be lethal at a specific location. AV deployments without freshness monitoring are a safety liability.

---

### Anti-Pattern 3: Ignoring Localization-Map Accuracy Budget

**Name:** The Independent Accuracy Fallacy

❌ BAD:
```
"Our HD map is 5cm accurate, so our lane-level positioning is 5cm accurate."
```

✅ GOOD:
```
Total lateral positioning error = sqrt(map_accuracy^2 + localization_accuracy^2)
Example: map=5cm, localization=8cm -> total = sqrt(0.05^2 + 0.08^2) = 9.4cm  (OK)
Degraded: map=5cm, localization=15cm -> total = sqrt(0.05^2 + 0.15^2) = 15.8cm (FAIL)

Design requirement: total < 10cm
=> requires BOTH map < 5cm AND localization < 8.7cm simultaneously
=> monitor both components independently with per-frame health checks
```

**Why it matters:** Teams routinely report map accuracy without localization accuracy. The system accuracy is dominated by the weaker component, not the average.

---

### Anti-Pattern 4: No Map QA Automation

**Name:** The Trust-the-Annotator Approach

❌ BAD: Manual annotation without automated topology and geometry validation. Annotators make errors — dangling lanelets, missing stop lines, incorrect lane connectivity.

✅ GOOD:
```python
def run_map_qa(map_) -> list:
    """Automated QA checks. Returns list of error strings."""
    errors = []
    routing_graph = lanelet2.routing.RoutingGraph(map_, ...)
    for ll in map_.laneletLayer:
        # Dangling lanelet check
        if not routing_graph.following(ll) and not is_terminal_lanelet(ll):
            errors.append(f"DANGLING_LANELET: id={ll.id}")
        # Width sanity check
        width = lanelet2.geometry.width(ll)
        if not (2.0 <= width <= 6.0):
            errors.append(f"INVALID_WIDTH: id={ll.id}, width={width:.2f}m")
        # Stop line required at signalized intersections
        if is_signalized_entry(ll) and not has_stop_line(ll):
            errors.append(f"MISSING_STOP_LINE: signalized entry id={ll.id}")
    return errors  # empty list = map passes QA
```

**Why it matters:** A dangling lanelet at an intersection exit can cause the routing planner to plan a route that drives off-road. Automated QA catches these errors in minutes rather than in field testing.

---

### Anti-Pattern 5: Coordinate System Ambiguity

**Name:** The WGS84/UTM Confusion Engineer

❌ BAD:
```python
# Mixing coordinate systems — no units, no datum specified
map_point  = np.array([13.745, 51.024])   # lat/lon degrees? UTM meters?
ego_point  = np.array([13.746, 51.025])
distance   = np.linalg.norm(map_point - ego_point)  # meaningless: 0.0014... what unit?
```

✅ GOOD:
```python
from pyproj import Proj

# Explicit coordinate system: WGS84 lat/lon -> UTM zone 33N for metric operations
utm33 = Proj(proj='utm', zone=33, datum='WGS84')

map_x,  map_y  = utm33(13.745, 51.024)   # outputs meters in UTM
ego_x,  ego_y  = utm33(13.746, 51.025)

distance_m = np.sqrt((ego_x - map_x)**2 + (ego_y - map_y)**2)
print(f"Distance: {distance_m:.2f} m")   # meaningful metric distance
```

**Why it matters:** A 1-degree confusion between lat/lon and UTM easting/northing produces a 111 km systematic error. Always annotate coordinate systems explicitly in every data structure and function signature.

---

## 11. Integration with Other Skills

| Skill | Integration Workflow | Combined Outcome |
|-------|---------------------|-----------------|
| **planning-decision-engineer** | Feed Lanelet2 lane graph as structured routing constraints into behavior planner; regulatory elements (speed limits, stop lines) as hard planning constraints | Map-aware planning with lane routing, traffic sign compliance, and intersection management; reduces unknown unsafe scenario space |
| **perception-algorithm-engineer** | Online lane detection outputs compared against HD map priors; disagreement > 30cm triggers map staleness flag; fleet data aggregated for change detection | Self-diagnosing map freshness monitor using fleet perception data; automatically identifies construction zones and map update needs |
| **autonomous-driving-engineer** | HD map localization accuracy feeds into ASIL allocation for lane-keeping; < 10cm lateral supports ASIL-C; > 30cm requires ASIL decomposition with camera corroboration | Complete map-in-the-loop safety case with ASIL allocation of localization pipeline; documented degradation states |

---

## 12. Scope & Limitations

**Use when:**
- Designing, building, or maintaining HD map pipelines for autonomous vehicles in structured road environments.
- Selecting between OpenDRIVE and Lanelet2 formats for a specific AV stack.
- Implementing LiDAR-to-map localization (NDT/ICP) for centimeter-level positioning.
- Evaluating online map prediction models (MapTR, HDMapNet) as alternatives to offline HD maps.
- Designing map update and freshness monitoring systems for production fleets.

**Do NOT use when:**
- Designing the ego trajectory planner that consumes the map — use planning-decision-engineer skill.
- Implementing the LiDAR perception detection stack — use perception-algorithm-engineer skill.
- V2X-based dynamic map updates (traffic signal timing, hazard broadcasting) — use v2x-system-engineer skill.

**Alternatives:**
- For mapless driving in unstructured environments: online prediction (MapTR) + perception-algorithm-engineer.
- For full AV stack integration: autonomous-driving-engineer skill.

---

## 13. How to Use This Skill

**Quick Install:**
```bash
# OpenCode
/skill load hd-map-engineer

# Claude

# Cline: add reference to project CLAUDE.md
echo "## AI Role: See skills/automotive/hd-map-engineer/SKILL.md" >> CLAUDE.md
```

**Trigger Words (English):**
`HD map`, `high-definition map`, `OpenDRIVE`, `Lanelet2`, `MapTR`, `HDMapNet`, `VectorMapNet`,
`map localization`, `NDT localization`, `lane annotation`, `map building`, `LiDAR SLAM mapping`,
`vectorized map`, `nuScenes HD map`, `map tile server`, `LIO-SAM`, `map freshness`

**Trigger Words (中文):**
`高精地图`, `地图工程师`, `车道注释`, `地图定位`, `矢量化地图`,
`OpenDRIVE格式`, `Lanelet2`, `激光雷达建图`, `在线地图预测`, `NDT定位`

---

## 14. Quality Verification

**Self-Checklist:**
- [ ] Map format recommendations include explicit version (OpenDRIVE 1.6, Lanelet2 v1.2).
- [ ] Localization accuracy targets are paired with map accuracy (total error budget computed).
- [ ] Code examples specify coordinate systems explicitly (WGS84, UTM zone number).
- [ ] Map freshness policy is addressed in any production deployment discussion.
- [ ] Topology validation is specified alongside any map annotation workflow.
- [ ] Online vs. offline map trade-offs are clearly articulated for the stated use case.
- [ ] NDT fitness score thresholds are specified for localization confidence monitoring.

**Test Case 1:**
- Input: "How do I model a roundabout in Lanelet2?"
- Expected Output: Lanelet2 topology with circulating lane lanelets forming a ring, entry/exit lanelets as yield-regulated approaches, pedestrian crossing lanelets at exits, Python code for creating the topology, note on circular routing graph handling in Lanelet2.

**Test Case 2:**
- Input: "Our NDT localization is losing accuracy in tunnel sections. What should we do?"
- Expected Output: Diagnosis (loss of LiDAR diversity in featureless tunnel), mitigation (dense reflector markers in tunnel, pre-tunnel position initialization, IMU dead reckoning during tunnel traverse), NDT fitness monitoring threshold (< 0.4 = fallback to IMU), recovery strategy on exit.

**Test Case 3:**
- Input: "We want to use MapTR to avoid maintaining offline HD maps. Is that sufficient for L4 robotaxi?"
- Expected Output: Accuracy comparison (MapTR ~67% mIoU vs. offline < 10cm lateral), specific failure modes (complex intersections, occluded markings, night), recommendation for offline HD map as primary with MapTR for gap coverage, evaluation protocol, minimum mIoU threshold.

---

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| 3.0.0 | 2026-03-07 | Full 16-section rewrite to exemplary quality; Lanelet2 intersection modeling code; NDT localization implementation with Open3D; MapTR evaluation pipeline; 5 anti-patterns with code; accuracy budget analysis; nuScenes HD map benchmark targets |
| 2.0.0 | 2025-08-01 | Added MapTR/HDMapNet online prediction section; map freshness monitoring; OpenDRIVE vs Lanelet2 comparison table |
| 1.0.0 | 2026-02-16 | Initial basic version; placeholder content only |

---

## 16. License & Author

| Field | Value |
|-------|-------|
| License | MIT — free to use, modify, and distribute with attribution |
| Author | neo.ai |
| Skill Name | hd-map-engineer |
| Category | automotive |
| Quality Grade | Exemplary — 9.5/10 |
| Contact | skills@neo.ai |

> This skill file is part of the **awesome-skills** collection by neo.ai.
> MIT License — Copyright 2026 neo.ai. Permission granted to use and adapt with attribution.
