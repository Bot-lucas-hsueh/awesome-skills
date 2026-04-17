## § 10 — Common Pitfalls

### Anti-Pattern 1: Training Without LiDAR Beam Drop Augmentation
**Name**: The Perfect-Sensor Trainer

❌ BAD:
```python
train_pipeline = [
    dict(type='LoadPointsFromFile', coord_type='LIDAR', load_dim=5),
    dict(type='LoadAnnotations3D'),
    dict(type='RandomFlip3D', flip_ratio_bev_horizontal=0.5),
    dict(type='DefaultFormatBundle3D'),
]
```

✅ GOOD:
```python
train_pipeline = [
    dict(type='LoadPointsFromFile', coord_type='LIDAR', load_dim=5),
    dict(type='LoadAnnotations3D'),
    dict(type='RandomFlip3D', flip_ratio_bev_horizontal=0.5),
    # Simulate rain/partial occlusion by randomly dropping LiDAR beams
    dict(type='PointsRangeFilter',
         point_cloud_range=[-54, -54, -5, 54, 54, 3]),
    dict(type='RandomDropPoints', drop_ratio_range=(0.0, 0.3)),  # custom aug
    dict(type='DefaultFormatBundle3D'),
]
```

**Why it matters**: Production LiDAR degrades in rain, fog, and partial occlusion. Models trained only on clean data show 15-25% mAP drop in adverse weather without this augmentation.

---

### Anti-Pattern 2: Ignoring NMS Latency at Deployment
**Name**: The Benchmark Hero

❌ BAD: Reporting model FLOPs and GPU inference time without including NMS, post-processing, and data transfer latency. A "10ms model" often becomes a 35ms system.

✅ GOOD: Always measure end-to-end latency including: preprocessing (voxelization), backbone forward pass, neck/head forward pass, NMS/decoding, and DtoH transfer. Profile with `torch.cuda.synchronize()` before/after each stage.

**Why it matters**: NMS on 200k anchors can take 20ms alone. Switching to anchor-free center-based detection (CenterPoint) eliminates NMS and saves 15-20ms on typical configurations.

---

### Anti-Pattern 3: Using 2D IoU for 3D Track Association
**Name**: The Flat-World Tracker

❌ BAD: Associating 3D detections using 2D BEV box IoU only, ignoring height and z-coordinate.

✅ GOOD: Use full 3D IoU for association, or at minimum add a z-distance gate (|z_det - z_trk| < 1.0m) before computing BEV IoU. This prevents cross-floor matching in multi-level structures.

**Why it matters**: In parking garages and highway overpasses, 2D IoU-based association matches detections from different floors, causing catastrophic track merges.

---

### Anti-Pattern 4: Fixed Confidence Threshold Across All Object Classes
**Name**: The One-Threshold-Fits-All

❌ BAD:
```python
final_detections = [d for d in all_detections if d.score > 0.3]
```

✅ GOOD:
```python
# Per-class thresholds tuned to achieve target recall at acceptable FPR
CLASS_THRESHOLDS = {
    'pedestrian': 0.25,   # lower threshold, higher recall for safety-critical class
    'car': 0.35,
    'cyclist': 0.28,
    'truck': 0.40,
}
final_detections = [
    d for d in all_detections
    if d.score > CLASS_THRESHOLDS.get(d.category, 0.35)
]
```

**Why it matters**: Pedestrians require higher recall than trucks. A uniform threshold optimized for overall mAP will under-detect pedestrians at the operating point that matters most.

---

### Anti-Pattern 5: Calibration Treated as One-Time Task
**Name**: The Set-and-Forget Calibrator

❌ BAD: Performing LiDAR-camera calibration once at vehicle assembly and never monitoring for drift.

✅ GOOD: Implement an online calibration health monitor that computes LiDAR point-to-image reprojection error on detected lane markings or checkerboard targets at startup. Alert maintenance when reprojection error exceeds 2 pixels.

**Why it matters**: Vibration, thermal cycles, and minor collisions cause extrinsic drift of 0.5-2 degrees over months. At 40m range, a 1-degree rotation error causes 0.7m lateral position error in fused detections.

---

### Anti-Pattern 6: Evaluating Only on nuScenes, Ignoring Production Sensor Config
**Name**: The Benchmark-Only Validator

❌ BAD: Reporting 70 NDS on nuScenes and assuming production performance will be similar without testing on the actual sensor configuration.

✅ GOOD: Transfer learning from nuScenes weights, then fine-tune on at minimum 500 internally collected scenes with the production sensor configuration. Evaluate on a held-out internal test set before benchmarking.

**Why it matters**: Different LiDAR models (Velodyne HDL-64E vs Luminar Halo vs Ouster OS1-128) produce dramatically different point densities and return patterns. Models trained on one sensor can lose 10-15 NDS when applied to another without adaptation.

---

