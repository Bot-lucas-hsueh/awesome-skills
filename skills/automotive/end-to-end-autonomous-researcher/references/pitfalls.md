## 10. Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Open-Loop Metric Conflation

**Why it matters:** Treating L2 displacement or nuScenes NDS as proof of driving quality leads to architectures optimized for replay rather than safe closed-loop control.

❌ BAD:
```
"Our model achieves L2@3s = 0.38m, outperforming all baselines,
demonstrating superior autonomous driving capability."
```

✅ GOOD:
```
"Our model achieves L2@3s = 0.38m on nuScenes open-loop validation,
improving over UniAD (0.48m). We additionally validate on nuPlan
PDM-Closed achieving 84.2 PDM-Score, confirming the open-loop
improvement translates to closed-loop driving quality."
```

### Anti-Pattern 2: BEV Resolution Cargo-Culting

**Why it matters:** Higher BEV resolution does not always improve downstream planning quality and dramatically increases memory and compute cost.

❌ BAD:
```python
bev_h, bev_w = 400, 400  # "more resolution = better" — untested assumption
# Result: 4x memory cost, 3x slower training, only +0.3% NDS improvement
```

✅ GOOD:
```python
# Profile the resolution-performance trade-off empirically
for res in [100, 200, 300, 400]:
    nds, l2_3s, fps = run_ablation(bev_h=res, bev_w=res)
    print(f"Res {res}: NDS={nds:.3f}, L2@3s={l2_3s:.3f}m, FPS={fps:.1f}")
# Choose the knee of the curve — typically 200x200 for camera-only,
# 300x300 for camera+LiDAR fusion
```

### Anti-Pattern 3: Ignoring Temporal Window Length

**Why it matters:** Using too few temporal frames loses velocity context; too many frames causes memory explosion and introduces stale history noise.

❌ BAD:
```python
# Only current frame: no velocity information available
bev_feat = bev_encoder(current_frame_only)
```

✅ GOOD:
```python
# 3-4 historical BEV frames with temporal deformable attention
temporal_feats = [bev_encoder(frame) for frame in frames[-4:]]
bev_feat = temporal_attention(
    query=current_bev_query,
    key_value=temporal_feats,
    ego_motion=ego_transforms[-4:]  # align history to current frame
)
# Provides implicit velocity via feature motion without explicit flow
```

### Anti-Pattern 4: Skipping Per-Modality Ablation

**Why it matters:** Claiming sensor fusion benefit without ablating each modality individually makes it impossible to attribute performance gains.

❌ BAD: Report only fusion model result; no camera-only or LiDAR-only baselines in the paper.

✅ GOOD:
```
Table 3 — Sensor Modality Ablation (nuScenes val)
| Modality             | NDS   | L2@3s | Collision |
|----------------------|-------|-------|-----------|
| Camera only          | 0.601 | 0.52m | 0.31%     |
| LiDAR only           | 0.683 | 0.45m | 0.22%     |
| Camera + LiDAR (ours)| 0.741 | 0.38m | 0.14%     |
```

### Anti-Pattern 5: Training on nuScenes trainval Without Strict Holdout

**Why it matters:** nuScenes trainval includes scenes that geographically overlap with val; training on both inflates numbers and prevents honest comparison.

❌ BAD:
```python
# Using trainval split and reporting on val — data leakage
split = "trainval"  # includes val geography
```

✅ GOOD:
```python
# Strict split: train only on train split; never touch val during development
train_scenes = load_nuscenes_split('train')   # 700 scenes
val_scenes   = load_nuscenes_split('val')     # 150 scenes, holdout
# Final paper numbers submitted to official test server (blind evaluation)
```

