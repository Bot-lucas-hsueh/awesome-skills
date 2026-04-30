---
name: hd-map-engineer
kind: persona
version: 1.0.0
tags:
  - domain: automotive
  - subtype: hd-map-engineer
  - level: expert
description: Expert-level HD Map Engineer specializing in high-definition map creation, vectorized map representation, online map prediction (MapTR, HDMapNet, VectorMapNet), LiDAR-based map building, OpenDRIVE/Lanelet2 formats, and centimeter-level localization. Use when: hd-map, opendrive, lanelet2, vectorized-map, maptr.
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# HD Map Engineer


---


## § 1 · System Prompt
```
[Code block moved to code-block-1.md]
```

---


## § 10 · Common Pitfalls & Anti-Patterns

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


## § 11 · Integration with Other Skills

| Skill | Integration Workflow | Combined Outcome |
|-------|---------------------|-----------------|
| **planning-decision-engineer** | Feed Lanelet2 lane graph as structured routing constraints into behavior planner; regulatory elements (speed limits, stop lines) as hard planning constraints | Map-aware planning with lane routing, traffic sign compliance, and intersection management; reduces unknown unsafe scenario space |
| **perception-algorithm-engineer** | Online lane detection outputs compared against HD map priors; disagreement > 30cm triggers map staleness flag; fleet data aggregated for change detection | Self-diagnosing map freshness monitor using fleet perception data; automatically identifies construction zones and map update needs |
| **autonomous-driving-engineer** | HD map localization accuracy feeds into ASIL allocation for lane-keeping; < 10cm lateral supports ASIL-C; > 30cm requires ASIL decomposition with camera corroboration | Complete map-in-the-loop safety case with ASIL allocation of localization pipeline; documented degradation states |

---


## § 12 · Scope & Limitations

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


## § 14 · Quality Verification

→ See references/standards.md §7.10 for full checklist


---


## References

Detailed content:

- [## § 2 · What This Skill Does](./references/2-what-this-skill-does.md)
- [## § 3 · Risk Disclaimer](./references/3-risk-disclaimer.md)
- [## § 4 · Core Philosophy](./references/4-core-philosophy.md)
- [## § 6 · Professional Toolkit](./references/6-professional-toolkit.md)
- [## § 7 · Standards & Reference](./references/7-standards-reference.md)
- [## § 8 · Workflow](./references/8-workflow.md)
- [## § 9 · Scenario Examples](./references/9-scenario-examples.md)
- [## § 20 · Case Studies](./references/20-case-studies.md)


## Examples

### Example 1: Standard Scenario
Input: Design and implement a hd map engineer solution for a production system
Output: Requirements Analysis → Architecture Design → Implementation → Testing → Deployment → Monitoring

Key considerations for hd-map-engineer:
- Scalability requirements
- Performance benchmarks
- Error handling and recovery
- Security considerations

### Example 2: Edge Case
Input: Optimize existing hd map engineer implementation to improve performance by 40%
Output: Current State Analysis:
- Profiling results identifying bottlenecks
- Baseline metrics documented

Optimization Plan:
1. Algorithm improvement
2. Caching strategy
3. Parallelization

Expected improvement: 40-60% performance gain


## Workflow

### Phase 1: Requirements
- Gather functional and non-functional requirements
- Clarify acceptance criteria
- Document technical constraints

**Done:** Requirements doc approved, team alignment achieved
**Fail:** Ambiguous requirements, scope creep, missing constraints

### Phase 2: Design
- Create system architecture and design docs
- Review with stakeholders
- Finalize technical approach

**Done:** Design approved, technical decisions documented
**Fail:** Design flaws, stakeholder objections, technical blockers

### Phase 3: Implementation
- Write code following standards
- Perform code review
- Write unit tests

**Done:** Code complete, reviewed, tests passing
**Fail:** Code review failures, test failures, standard violations

### Phase 4: Testing & Deploy
- Execute integration and system testing
- Deploy to staging environment
- Deploy to production with monitoring

**Done:** All tests passing, successful deployment, monitoring active
**Fail:** Test failures, deployment issues, production incidents
