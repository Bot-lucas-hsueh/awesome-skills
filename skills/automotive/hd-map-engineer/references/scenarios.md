## 9. Scenario Examples

### Example 1: Designing a Lanelet2 Map for an Urban Intersection

**User:** I need to model a T-intersection in Lanelet2 for an Autoware-based AV. The intersection has a dedicated left-turn lane, a shared left-turn/straight lane, and a right-turn lane. How do I structure this?

**Engineer:**

T-intersection modeling in Lanelet2 requires careful topology design. Here is the complete structure:

```python
import lanelet2
from lanelet2.core import (
    LaneletMap, Lanelet, LineString3d, Point3d, AttributeMap, getId,
    TrafficLight
)

def create_t_intersection_map():
    """
    Model a T-intersection with 3 entry approaches (N, E, S) and 3 exits.
    N-approach: left-turn only lane + shared straight/left lane + right-turn lane
    """
    map_ = LaneletMap()
    attrs = AttributeMap()

    def pt(x, y, z=0.0):
        return Point3d(getId(), x, y, z)

    def ls(*points):
        ls_ = LineString3d(getId(), list(points))
        ls_.attributes['type'] = 'line_thin'
        return ls_

    # North approach (3 lanes, y decreasing = toward intersection)
    # Lane boundaries west-to-east: b1 | b2 | b3 | b4

    b1 = ls(pt(-11.5, 50), pt(-11.5, 5))  # leftmost boundary
    b2 = ls(pt(-7.5,  50), pt(-7.5,  5))
    b3 = ls(pt(-3.5,  50), pt(-3.5,  5))
    b4 = ls(pt( 0.5,  50), pt( 0.5,  5))  # rightmost boundary

    # Left-turn only lane
    ll_left = Lanelet(getId(), b1, b2, attrs)
    ll_left.attributes['subtype'] = 'road'
    ll_left.attributes['turn_direction'] = 'left'

    # Shared straight/left lane
    ll_shared = Lanelet(getId(), b2, b3, attrs)
    ll_shared.attributes['subtype'] = 'road'
    ll_shared.attributes['turn_direction'] = 'straight_left'

    # Right-turn only lane
    ll_right = Lanelet(getId(), b3, b4, attrs)
    ll_right.attributes['subtype'] = 'road'
    ll_right.attributes['turn_direction'] = 'right'

    # Stop line (shared for all 3 approach lanes)
    stop_line = ls(pt(-11.5, 5), pt(0.5, 5))
    stop_line.attributes['type'] = 'stop_line'

    # Traffic light regulatory element applied to all entry lanelets
    traffic_light = TrafficLight(getId(), [stop_line])
    ll_left.addRegulatoryElement(traffic_light)
    ll_shared.addRegulatoryElement(traffic_light)
    ll_right.addRegulatoryElement(traffic_light)

    map_.add(ll_left)
    map_.add(ll_shared)
    map_.add(ll_right)
    # ... add connection lanelets through intersection box and exit lanelets

    return map_

def query_adjacent_lanes(map_, current_ll_id: int):
    """Find left/right neighbors for a given lanelet."""
    routing_graph = lanelet2.routing.RoutingGraph(
        map_,
        lanelet2.traffic_rules.create(
            lanelet2.traffic_rules.Locations.Germany,
            lanelet2.traffic_rules.Participants.Vehicle))
    ll = map_.laneletLayer[current_ll_id]
    return routing_graph.left(ll), routing_graph.right(ll)
```

**Key design rules for intersections in Lanelet2:**
1. Entry lanelets must end with a stop_line or yield_line regulatory element.
2. Through-intersection paths are modeled as short "connection lanelets" inside the intersection box (subtype: road, no additional attributes).
3. Lane change between entry lanelets is annotated via `lane_change_by_value` attributes.
4. Pedestrian crossings near intersection exits are `crosswalk` lanelets with `ped_crossing` subtype.
5. Every connection lanelet has exactly one entry lanelet predecessor and one exit lanelet successor.

---

### Example 2: Implementing LiDAR-to-Map NDT Localization

**User:** We have a built HD map and want to implement LiDAR-based localization with < 10cm lateral accuracy. What's the recommended approach?

**Engineer:**

Use NDT (Normal Distributions Transform) localization — the standard in Autoware and the most robust LiDAR-to-map matching method for structured roads.

**NDT localization pipeline:**
1. Pre-process incoming LiDAR scan: ground removal, downsample to 0.2m voxel grid.
2. Initialize from GNSS prior: coarse localization for NDT search region.
3. Run NDT scan matching: iteratively align scan to pre-built NDT map.
4. Monitor NDT fitness score: flag degraded localization when score < 0.5.

```python
import numpy as np
import open3d as o3d

class NDTLocalizer:
    """
    NDT localization pipeline.
    Production: use ndt_omp (C++) via ROS2 node for < 15ms matching on Orin.
    """
    def __init__(self, fitness_threshold: float = 0.5,
                 map_voxel_size: float = 1.0,
                 scan_voxel_size: float = 0.2):
        self.fitness_threshold = fitness_threshold
        self.map_voxel_size = map_voxel_size
        self.scan_voxel_size = scan_voxel_size
        self.ndt_map_pcd = None
        self.pose_estimate = None  # [x, y, z, roll, pitch, yaw]

    def load_map(self, map_pcd_path: str) -> None:
        pcd = o3d.io.read_point_cloud(map_pcd_path)
        self.ndt_map_pcd = pcd.voxel_down_sample(self.map_voxel_size)
        print(f"NDT map: {len(self.ndt_map_pcd.points)} points after voxelization")

    def initialize_from_gnss(self, gnss_xyz: np.ndarray) -> None:
        self.pose_estimate = np.zeros(6)
        self.pose_estimate[:3] = gnss_xyz  # x, y, z from GNSS

    def update(self, lidar_scan: np.ndarray) -> dict:
        """
        lidar_scan: (N, 3) array in sensor frame
        Returns: dict with pose, fitness_score, status, lateral_error_estimate_m
        """
        if self.pose_estimate is None:
            return {'status': 'UNINITIALIZED', 'pose': None, 'fitness_score': 0.0}

        # Downsample scan
        scan_pcd = o3d.geometry.PointCloud()
        scan_pcd.points = o3d.utility.Vector3dVector(lidar_scan)
        scan_pcd = scan_pcd.voxel_down_sample(self.scan_voxel_size)

        # Construct initial transform from current pose estimate
        T_init = self._pose_to_transform(self.pose_estimate)

        # NDT registration (generalized ICP as proxy; production: ndt_omp)
        result = o3d.pipelines.registration.registration_generalized_icp(
            scan_pcd, self.ndt_map_pcd,
            max_correspondence_distance=1.0,
            init=T_init,
            estimation_method=o3d.pipelines.registration.TransformationEstimationForGeneralizedICP(),
            criteria=o3d.pipelines.registration.ICPConvergenceCriteria(
                max_iteration=50, relative_fitness=1e-6)
        )

        fitness = result.fitness
        if fitness >= self.fitness_threshold:
            self.pose_estimate = self._transform_to_pose(result.transformation)
            status = 'OK'
        else:
            status = 'DEGRADED'

        lateral_error_m = self._fitness_to_lateral_error(fitness)

        return {
            'status': status,
            'pose': self.pose_estimate.copy(),
            'fitness_score': fitness,
            'lateral_error_estimate_m': lateral_error_m,
            'position_xy': self.pose_estimate[:2],
        }

    def _fitness_to_lateral_error(self, fitness: float) -> float:
        """Map NDT fitness to lateral error estimate (empirical model)."""
        if fitness >= 1.0:   return 0.03   # ~3cm at high fitness
        elif fitness >= 0.7: return 0.05
        elif fitness >= 0.5: return 0.10
        else:                return 0.25   # unreliable; use GNSS fallback

    def _pose_to_transform(self, pose: np.ndarray) -> np.ndarray:
        from scipy.spatial.transform import Rotation
        R = Rotation.from_euler('xyz', pose[3:6]).as_matrix()
        T = np.eye(4)
        T[:3, :3] = R
        T[:3,  3] = pose[:3]
        return T

    def _transform_to_pose(self, T: np.ndarray) -> np.ndarray:
        from scipy.spatial.transform import Rotation
        R = Rotation.from_matrix(T[:3, :3])
        pose = np.zeros(6)
        pose[:3] = T[:3, 3]
        pose[3:] = R.as_euler('xyz')
        return pose
```

**Production deployment note:** Use `ndt_omp` (C++, OpenMP-parallelized) via Python bindings or ROS2 node. It achieves < 15ms per scan on NVIDIA Orin with 10,000-point scans at 10Hz. Accuracy target is < 5cm lateral at fitness > 0.8, degrading to < 15cm at fitness 0.5. When fitness drops below 0.3 on 3 consecutive frames, trigger safety alert and switch to GNSS+IMU dead reckoning.

---

### Example 3: Evaluating MapTR for Production Use

**User:** We're considering using MapTR instead of an offline HD map for our pilot area. How do we evaluate whether it's good enough?

**Engineer:**

MapTR is the SOTA online vectorized map prediction model (nuScenes HD Map benchmark, ~67% mIoU as of 2025). The key question is whether its accuracy meets your lane-keeping requirements. Here is a structured evaluation framework:

**Step 1 — Understand the accuracy floor:**
Online map prediction from cameras has fundamental limits compared to offline HD maps:
- Lateral lane boundary accuracy: ~20-40cm average error (vs. < 10cm for offline HD map)
- Longitudinal stop-line position: ~50cm error (vs. < 20cm offline)
- Complex intersections: 5-15% element miss rate

**Step 2 — Run nuScenes evaluation:**
```python
import numpy as np
from shapely.geometry import LineString

def compute_chamfer_distance(pred_polylines: list, gt_polylines: list) -> float:
    """
    Compute average Chamfer Distance between predicted and GT polylines.
    pred_polylines, gt_polylines: lists of (N, 2) numpy arrays (BEV coords)
    """
    if not pred_polylines or not gt_polylines:
        return float('inf')

    total_cd = 0.0
    count = 0
    for gt_poly in gt_polylines:
        gt_pts = gt_poly  # (N, 2)
        min_dists = []
        for pred_poly in pred_polylines:
            # Directed distance: GT -> nearest pred point
            pred_pts = pred_poly
            dists = np.min(
                np.linalg.norm(gt_pts[:, None, :] - pred_pts[None, :, :], axis=-1),
                axis=1)
            min_dists.append(np.mean(dists))
        total_cd += min(min_dists)
        count += 1
    return total_cd

# Decision thresholds for use case compatibility
USE_CASE_REQUIREMENTS = {
    'highway_lane_keep':     {'min_mIoU': 0.65, 'max_CD_m': 0.30},
    'urban_lane_keep':       {'min_mIoU': 0.60, 'max_CD_m': 0.40},
    'intersection_manage':   {'min_mIoU': 0.70, 'max_CD_m': 0.25},  # stricter
    'parking':               {'min_mIoU': 0.50, 'max_CD_m': 0.60},
}

def assess_use_case_compatibility(eval_results: dict, use_case: str) -> str:
    reqs = USE_CASE_REQUIREMENTS[use_case]
    if (eval_results['mIoU'] >= reqs['min_mIoU'] and
            eval_results['mean_CD_m'] <= reqs['max_CD_m']):
        return 'COMPATIBLE'
    return 'INSUFFICIENT — use offline HD map'
```

**Step 3 — Recommendation for typical use cases:**
- Highway lane-keep: MapTR mIoU ~67% is borderline sufficient for centerline following with ±0.5m tolerance. Not sufficient for precision centering in narrow lanes (< 3m width).
- Urban intersection management: MapTR's 5-15% element miss rate makes it unreliable as sole input for unsignalized intersection decisions. Use offline HD map as primary.
- Recommendation: Use offline HD map for pilot area ODD, MapTR as fallback for unmapped road segments only. Track MapTR accuracy on your specific sensor configuration — nuScenes results may not transfer if camera configuration differs.

---
