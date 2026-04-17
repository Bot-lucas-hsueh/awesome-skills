## 10. Common Pitfalls & Anti-Patterns

### Anti-Pattern 1 — Wrong Coordinate Frame Convention

```python
# BAD: Assuming camera frame = robot frame
# BAD: X forward, Z up vs X right, Z forward — ROS REP-103 violation
point_robot = T_camera_robot @ point_camera  # Wrong order!

# GOOD: Use TF2 for all frame transforms
from tf2_ros import Buffer, TransformListener
import tf2_geometry_msgs

tf_buffer = Buffer()
tf_listener = TransformListener(tf_buffer, node)
# Always query at the exact message timestamp
transform = tf_buffer.lookup_transform(
    target_frame='base_link',
    source_frame='camera_color_optical_frame',
    time=msg.header.stamp,
    timeout=rclpy.duration.Duration(seconds=0.1)
)
```
**Why it matters**: Wrong frame convention silently produces detections that appear to work in static scenes but diverge catastrophically during motion.

### Anti-Pattern 2 — VoxelGrid Downsampling Before Ground Removal

```python
# BAD: Downsample first → ground points contaminate feature extraction
pcd_down = pcd.voxel_down_sample(voxel_size=0.1)
pcd_no_ground = remove_ground(pcd_down)  # Already lost ground detail

# GOOD: Remove ground first, then downsample the objects separately
pcd_ground, pcd_objects = patchworkpp_ground_removal(pcd)
pcd_objects_down = pcd_objects.voxel_down_sample(voxel_size=0.05)
# Ground kept at full resolution for terrain analysis if needed
```
**Why it matters**: Downsampling first merges ground and object points in the same voxel, causing objects near the ground to be partially removed and incorrect cluster heights.

### Anti-Pattern 3 — Fixed Detection Confidence Threshold

```python
# BAD: Hard-coded threshold ignores sensor degradation
if detection.score > 0.5:
    publish(detection)

# GOOD: Adaptive threshold based on sensor health and range
def adaptive_threshold(detection, range_m: float, sensor_health: float) -> float:
    base = 0.5
    range_penalty = max(0, (range_m - 30) * 0.005)  # Stricter beyond 30m
    health_boost = (1.0 - sensor_health) * 0.1       # Stricter if sensor degraded
    return base + range_penalty + health_boost

if detection.score > adaptive_threshold(detection, det_range, lidar_health):
    publish(detection)
```
**Why it matters**: Distant or occluded objects score 0.3-0.4 at 50m but are real. A fixed 0.5 threshold creates systematic blind spots at range while passing false positives at short range.

### Anti-Pattern 4 — Ignoring IMU Bias Initialization

```python
# BAD: Start SLAM immediately after boot
slam.start()

# GOOD: Collect stationary IMU data for bias estimation before motion
import time
imu_samples = []
print("Keep robot stationary for 5 seconds...")
start = time.time()
while time.time() - start < 5.0:
    imu_samples.append(collect_imu_sample())
accel_bias = np.mean([s.accel for s in imu_samples], axis=0)
gyro_bias = np.mean([s.gyro for s in imu_samples], axis=0)
slam.initialize_bias(accel_bias, gyro_bias)
slam.start()
```
**Why it matters**: Un-initialized IMU bias (typically 0.1-0.3 m/s² for accelerometers) integrates to 5m position error in 10 seconds — making VIO initialization impossible.

### Anti-Pattern 5 — Using rosbag play Without Rate Control for Testing

```bash
# BAD: Plays bag at recorded speed, may overwhelm slow algorithms
ros2 bag play recording.bag

# GOOD: Throttle to system processing rate, pause on overload
ros2 bag play recording.bag --rate 0.5  # 50% speed for slower hardware
# Or: use sim_time and pause logic in your node with /clock subscriber
```
**Why it matters**: Playing bags faster than the algorithm can process causes message queue buildup, producing out-of-order processing and false latency measurements that obscure real performance issues.

## 11. Integration with Other Skills

| Combination | Workflow | Result |
|-------------|----------|--------|
| **Perception + Motion Control** | Perception node publishes obstacle occupancy grid and target object pose → Motion control consumes via `/costmap` and `/target_pose` topics | Closed-loop pick-and-place: perception drives inverse kinematics goal selection in real-time |
| **Perception + Robot Mechanical Design** | Mechanical engineer defines sensor mounting brackets and FoV requirements → Perception engineer validates overlap and blind spots in simulation (Gazebo/Isaac Sim) | Optimal sensor placement that eliminates blind spots near manipulator workspace without exceeding weight budget |
| **Perception + Embodied AI** | Perception provides semantic scene graph (objects, relations, affordances) → Embodied AI planner uses VLM to reason over scene and generate task plans | Language-conditioned manipulation: "pick the red mug on the left shelf" resolved end-to-end |

## 12. Scope & Limitations

**Use When:**
- Building perception stacks for mobile robots, manipulators, AGVs, or outdoor UGVs
- Integrating multiple sensor modalities (camera, LiDAR, IMU, radar, ToF)
- Deploying deep learning perception to edge hardware (Jetson Orin, RK3588, Hailo-8)
- Debugging SLAM drift, detection failures, or sensor fusion inconsistencies
- Designing calibration workflows for multi-sensor rigs

**Do NOT Use When:**
- Aerial drone perception with very specific flight dynamics (use specialized drone stacks — PX4 + VIO)
- Medical imaging analysis — requires domain-specific regulatory knowledge (FDA, MDR)
- Pure computer vision tasks without robotics context (use a CV-specialist skill)
- ASIC/FPGA hardware design for sensor interfaces — requires hardware engineering skill

## 13. How to Use This Skill

**Quick Install:**
```bash
# OpenCode
opencode skill add robot-perception-engineer

# Cursor — create rules file
mkdir -p .cursor/rules
cp robot-perception-engineer.md .cursor/rules/robot-perception-engineer.mdc

# Claude Code — load system prompt
claude --system-prompt "$(sed -n '/^```$/,/^```$/p' robot-perception-engineer.md | head -n -1 | tail -n +2)"
```

**Trigger Words
- `robot perception engineer`
- `point cloud processing`
- `lidar slam`
- `sensor fusion`
- `tensorrt deployment`
- `camera lidar calibration`
- `object detection robot`
- `depth estimation`

## 14. Quality Verification

**Self-Checklist:**
- [ ] All 5 decision gates evaluated before recommending any solution
- [ ] Coordinate frames explicitly named (base_link, camera_color_optical_frame, lidar_frame)
- [ ] Latency budget stated with hardware context (Orin NX vs Orin AGX)
- [ ] Calibration residuals quantified (reprojection px, registration cm)
- [ ] Code snippets include error handling and logging
- [ ] ROS2 conventions used (rclpy/rclcpp, REP-103 frames, SI units)
- [ ] Failure modes and graceful degradation addressed

**Test Cases:**

| # | Input | Expected Output |
|---|-------|-----------------|
| 1 | "My ORB-SLAM3 works indoors but fails in a white corridor" | Diagnosis: feature starvation in textureless environments. Recommendation: switch to LiDAR-based SLAM (LIO-SAM) or add artificial texture. Provide LIO-SAM parameter YAML for corridor geometry. |
| 2 | "Convert YOLOv8n to TensorRT for Jetson Orin NX 8GB, need < 10ms" | Complete Python TensorRT build script with FP16 flag, expected 5-7ms result, validation protocol comparing ONNX vs TRT mAP on 500-image set |
| 3 | "LiDAR points are offset from camera image by ~15cm at 5m range" | Root cause: extrinsic calibration error. Provide checklist: verify board size input, check if rotation matrix is transposed, run reprojection error per-frame plot to detect per-sequence inconsistency |

## 15. Version History

| Version | Date | Changes |
|---------|------|---------|
| **3.0.0** | 2026-03-04 | Full rewrite to exemplary standard. Added 16-section structure, complete TensorRT INT8 calibration code, Patchwork++ ground removal, BEVFusion reference, 5-gate decision framework, thermal throttling mitigation, timestamp sync anti-pattern |
| **2.0.0** | 2025-09-01 | Added FAST-LIO2 and LIO-SAM integration guides, Jetson Orin optimization section, ROS2 Iron compatibility |
| **1.0.0** | 2025-03-01 | Initial release with basic ORB-SLAM3, PCL, and TensorRT overview |

## 16. License & Author

**License**: MIT License — free to use, modify, and distribute with attribution.

**Author**: neo.ai — Advanced Robotics & AI Engineering Skills Platform

**Attribution**: When using or adapting this skill, include: "Robot Perception Engineer skill by neo.ai (v3.0.0)"

**Contact**: For enterprise licensing, custom skill development, or technical collaboration: skills@neo.ai

**Disclaimer**: Perception algorithms in safety-critical applications (autonomous vehicles, surgical robots, industrial cobots) require independent validation, formal verification, and domain-specific regulatory certification (ISO 26262, IEC 62061, FDA 510k). This skill provides engineering guidance — not certification.
