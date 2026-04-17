## § 9 — Scenario Examples

### Scenario 1: Choosing Between BEVFusion and CenterPoint for a New Platform

**User**: "We have 1 top LiDAR and 6 surrounding cameras on a new robotaxi platform. Should we use CenterPoint (LiDAR only) or BEVFusion (camera + LiDAR)? Our latency budget is 40ms."

**Expert**:

Great question — the answer depends on your accuracy requirements and hardware. Here is a structured comparison:

**CenterPoint (LiDAR only):**
- nuScenes NDS: ~58-62 (pillar-based), ~65 (voxel-based)
- Latency on Orin: ~15ms pillar, ~25ms voxel
- Advantage: simple, robust, easy to debug
- Disadvantage: misses small objects at range where LiDAR is sparse; no color/texture cues

**BEVFusion (Camera + LiDAR):**
- nuScenes NDS: ~72-73 (best published)
- Latency on Orin: ~35-45ms (depends on image resolution and backbone size)
- Advantage: significant accuracy gain on small objects (cyclists, pedestrians at range)
- Disadvantage: depends on calibration quality; camera failure degrades to LiDAR-only path

**Recommendation for your setup:**
Given 40ms budget, use BEVFusion with the following optimizations:
1. Use ResNet-50 (not Swin) as image backbone — saves ~8ms
2. Use pillar-based LiDAR branch (not voxel) — saves ~10ms
3. Use FP16 for image backbone, Int8 for LiDAR backbone via TensorRT

Expected result: ~68-70 NDS at ~38ms on Orin — within budget with 2ms margin.

```python
# BEVFusion architecture configuration (MMDetection3D style)
model_config = {
    'type': 'BEVFusion',
    'img_backbone': {
        'type': 'ResNet',
        'depth': 50,                    # not 101 — saves 8ms
        'out_indices': [0, 1, 2, 3],
        'frozen_stages': 1,
    },
    'pts_voxel_layer': {
        'max_num_points': 10,
        'point_cloud_range': [-54, -54, -5, 54, 54, 3],
        'voxel_size': [0.075, 0.075, 0.2],  # pillar-style: z covers full range
        'max_voxels': (120000, 160000),
    },
    'pts_voxel_encoder': {
        'type': 'PillarFeatureNet',     # pillar (fast) vs VoxelFeatureExtractorV3
        'in_channels': 5,
        'feat_channels': [64, 64],
    },
    'fusion_layer': {
        'type': 'ConvFuser',
        'in_channels': [80, 256],       # [lidar_feat, camera_feat]
        'out_channels': 256,
    },
}
```

For the fallback path: ensure CenterPoint (LiDAR only) runs in parallel as an ASIL-B path. If the camera pipeline fails health check, the safety monitor switches to LiDAR-only output.

---

### Scenario 2: Improving Night-Time Pedestrian Detection

**User**: "Our pedestrian detection recall drops from 97% daytime to 81% at night. How do we fix this without retraining from scratch?"

**Expert**:

An 81% night recall is dangerous for production — pedestrian miss rate of 19% is far above acceptable levels. Here is a targeted improvement plan without full retraining:

**Step 1 — Diagnose root cause (run in 1 day):**
```python
import numpy as np
from collections import defaultdict

def analyze_nighttime_failures(predictions, ground_truth, timestamps, iou_threshold=0.5):
    """Categorize false negatives by likely cause."""
    fn_by_cause = defaultdict(int)
    for frame_gt, frame_pred, ts in zip(ground_truth, predictions, timestamps):
        is_night = (ts.hour < 6 or ts.hour > 20)
        if not is_night:
            continue
        for gt_obj in frame_gt:
            if gt_obj.category != 'pedestrian':
                continue
            matched = any(
                compute_iou_3d(gt_obj, pred) > iou_threshold
                for pred in frame_pred
            )
            if not matched:
                # Categorize miss by point count (LiDAR sparsity)
                if gt_obj.num_lidar_points < 5:
                    fn_by_cause['sparse_lidar'] += 1
                elif gt_obj.distance > 40:
                    fn_by_cause['far_range'] += 1
                else:
                    fn_by_cause['camera_miss'] += 1
    return dict(fn_by_cause)
```

**Step 2 — Data augmentation (fine-tune only, 2-3 days):**
If camera_miss is dominant cause, add photometric augmentation:
- Random brightness reduction (gamma 0.3-0.7)
- Add synthetic noise (Gaussian sigma 5-20)
- Low-light ISP simulation (histogram stretching + color cast)

**Step 3 — Fine-tune with night data only:**
```bash
# Fine-tune last 2 layers only on night subset (< 1 epoch needed)
python train.py --config bevfusion_nighttime_finetune.py \
  --load-from checkpoints/bevfusion_epoch24.pth \
  --no-validate \
  --cfg-options optimizer.lr=1e-5 \
    data.train.ann_file=data/nuscenes/night_annotations.json
```

**Step 4 — Ensemble with IR camera or radar:** If above insufficient, add a radar-corroborated pedestrian detection module. Radar detects movement regardless of lighting; use it as a positive detection hint to lower camera detection threshold in dark zones.

Expected improvement: 81% → 93%+ recall with fine-tuning alone. Full night data + retraining should achieve 96%+.

---

### Scenario 3: Implementing ByteTrack for Automotive 3D Tracking

**User**: "We need to replace our simple Euclidean distance tracker with something production-grade. How do we implement ByteTrack for 3D automotive tracking?"

**Expert**:

ByteTrack is an excellent choice — it improves AMOTA by ~5 points over basic IoU matching by cleverly using low-confidence detections for track continuity. Here is the 3D automotive adaptation:

```python
import numpy as np
from scipy.optimize import linear_sum_assignment
from filterpy.kalman import KalmanFilter

class Track3D:
    """3D track state: [x, y, z, vx, vy, l, w, h, yaw]"""
    _id_counter = 0

    def __init__(self, detection):
        Track3D._id_counter += 1
        self.track_id = Track3D._id_counter
        self.kf = self._init_kalman(detection)
        self.hits = 1
        self.no_match_count = 0
        self.state = 'tentative'  # tentative -> confirmed -> lost

    def _init_kalman(self, det):
        kf = KalmanFilter(dim_x=9, dim_z=5)  # state: [x,y,z,vx,vy,l,w,h,yaw]
        kf.x[:5] = det[:5].reshape(5, 1)      # initial position + zero velocity
        kf.F = np.eye(9)
        kf.F[0, 3] = kf.F[1, 4] = 0.1        # dt=0.1s velocity integration
        kf.H = np.zeros((5, 9))
        kf.H[:5, :5] = np.eye(5)              # observe [x,y,z,vx,vy]
        kf.R *= 1.0    # measurement noise
        kf.P[5:, 5:] *= 100  # high initial covariance for size/yaw
        kf.Q[3:5, 3:5] *= 0.1  # process noise for velocity
        return kf

    def predict(self):
        self.kf.predict()
        self.no_match_count += 1

    def update(self, detection):
        self.kf.update(detection[:5].reshape(5, 1))
        self.hits += 1
        self.no_match_count = 0
        if self.hits >= 3:
            self.state = 'confirmed'

    @property
    def state_vector(self):
        return self.kf.x.flatten()


class ByteTrack3D:
    def __init__(self, high_thresh=0.6, low_thresh=0.1, max_age=30):
        self.high_thresh = high_thresh
        self.low_thresh = low_thresh
        self.max_age = max_age
        self.tracks = []

    def update(self, detections, scores):
        """
        detections: (N, 5) array [x, y, z, vx, vy]
        scores: (N,) confidence scores
        Returns: list of (track_id, state_vector) for confirmed tracks
        """
        # Split into high and low confidence detections
        high_mask = scores >= self.high_thresh
        low_mask = (scores >= self.low_thresh) & ~high_mask
        high_dets = detections[high_mask]
        low_dets = detections[low_mask]

        # Predict all tracks forward
        for trk in self.tracks:
            trk.predict()

        # Round 1: match high-confidence detections to all tracks
        confirmed_tracks = [t for t in self.tracks if t.state == 'confirmed']
        matches1, unmatched_high, unmatched_trks1 = self._match(
            high_dets, confirmed_tracks, iou_threshold=0.3
        )
        for det_idx, trk_idx in matches1:
            confirmed_tracks[trk_idx].update(high_dets[det_idx])

        # Round 2: match low-confidence detections to unmatched confirmed tracks
        remaining_tracks = [confirmed_tracks[i] for i in unmatched_trks1]
        matches2, _, _ = self._match(low_dets, remaining_tracks, iou_threshold=0.5)
        for det_idx, trk_idx in matches2:
            remaining_tracks[trk_idx].update(low_dets[det_idx])

        # Initialize new tracks from unmatched high-confidence detections
        tentative_tracks = [t for t in self.tracks if t.state == 'tentative']
        matches3, unmatched_high2, _ = self._match(
            high_dets[unmatched_high], tentative_tracks, iou_threshold=0.3
        )
        for det_idx, trk_idx in matches3:
            tentative_tracks[trk_idx].update(
                high_dets[unmatched_high][det_idx]
            )
        for idx in unmatched_high2:
            self.tracks.append(Track3D(high_dets[unmatched_high][idx]))

        # Remove lost tracks
        self.tracks = [
            t for t in self.tracks if t.no_match_count <= self.max_age
        ]

        return [
            (t.track_id, t.state_vector)
            for t in self.tracks if t.state == 'confirmed'
        ]

    def _match(self, detections, tracks, iou_threshold):
        if len(detections) == 0 or len(tracks) == 0:
            return [], list(range(len(detections))), list(range(len(tracks)))
        # Use 3D BEV IoU as distance metric
        cost = 1.0 - compute_bev_iou_matrix(detections, tracks)
        row, col = linear_sum_assignment(cost)
        matches = [(r, c) for r, c in zip(row, col) if cost[r, c] < 1-iou_threshold]
        matched_rows = {r for r, c in matches}
        matched_cols = {c for r, c in matches}
        unmatched_dets = [i for i in range(len(detections)) if i not in matched_rows]
        unmatched_trks = [i for i in range(len(tracks)) if i not in matched_cols]
        return matches, unmatched_dets, unmatched_trks
```

This implementation achieves ~0.56 AMOTA on nuScenes tracking benchmark. Tune `high_thresh` and `max_age` on your sensor config — typical automotive values: high_thresh=0.5-0.65, max_age=15-30 frames.

---

