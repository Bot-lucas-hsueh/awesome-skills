# Unitree Humanoid Specifications

## G1 — Compact Humanoid Robot

### Overview
The Unitree G1 is a compact humanoid robot launched in May 2024 at a breakthrough price of $16,000 (Basic). It democratizes access to humanoid robotics for researchers, startups, and educational institutions.

### Physical Specifications

| Parameter | G1 Basic | G1 EDU |
|-----------|----------|--------|
| Height (standing) | 127 cm | 127-132 cm |
| Height (folded) | 69 cm | 69 cm |
| Width/Thickness | 45 cm × 20 cm | 45 cm × 20 cm |
| Weight | ~35 kg | ~35 kg |

### Degrees of Freedom

| Configuration | DOF | Details |
|---------------|-----|---------|
| G1 Basic | 23 | Head, arms, legs, basic torso |
| G1 EDU Standard | 23-30 | + Enhanced joints |
| G1 EDU Plus | 30+ | + 3-DOF waist articulation |
| G1 EDU Ultimate D | 43 | + Dexterous hands, full sensing |

### Joint Specifications (G1 EDU)

| Joint | Range | Max Torque |
|-------|-------|------------|
| Waist Z | ±155° | — |
| Hip P (pitch) | ±154° | 220 N·m |
| Hip R (roll) | -30° ~ +170° | 220 N·m |
| Hip Y (yaw) | ±158° | 220 N·m |
| Knee | 0° ~ 165° | 90 N·m (G1) / 120 N·m (G1 EDU) |
| Ankle | Multi-axis | 59 N·m |
| Shoulder | Multi-axis | ~75 N·m |
| Wrist (EDU) | P ±92.5°, Y ±92.5° | — |

### Actuator Technology

**M107 Joint Motor (adapted for G1):**
- Type: Low-inertia internal-rotor PMSM
- Bearings: Industrial crossed-roller
- Encoders: Dual encoders per joint
- Cooling: Local air cooling
- Routing: Full joint-hollow cable management

### Perception System

| Component | Specification |
|-----------|---------------|
| Depth Camera | Intel RealSense D435/D435i |
| LiDAR | Livox MID-360 (3D) |
| IMU | Integrated |
| Microphone Array | 4-mic array |
| Speaker | 5W |

### Computing

| Variant | Compute Platform |
|---------|------------------|
| G1 Basic | 8-core high-performance CPU |
| G1 EDU | 8-core CPU + NVIDIA Jetson Orin (100 TOPS) |

### Power System

| Parameter | Value |
|-----------|-------|
| Battery Type | 13-series smart lithium |
| Capacity | 9,000 mAh |
| Voltage | 54V |
| Runtime | ~2 hours (mixed workload) |
| Charging | 54V 5A charger |
| Battery Cost | ~$800 (spare) |

### Arm Specifications

| Parameter | G1 | G1 EDU |
|-----------|-----|--------|
| Total Arm Length | ~338 mm × 2 | ~338 mm × 2 |
| Max Load | ~2 kg | ~3 kg |
| Hand Type | Basic gripper | Optional dexterous hands |

### Pricing (2026)

| Variant | Price (USD) | Target User |
|---------|-------------|-------------|
| G1 Basic | $21,600 | Demo users, HRI studies |
| G1 EDU Standard | $40,000+ | Researchers, universities |
| G1 EDU Plus | $52,000 | Advanced manipulation research |
| G1 EDU Ultimate D | $73,900 | Competition, cutting-edge research |

### Software Support

- **ROS2**: Full support (unitree_ros2)
- **SDK**: C++ and Python (EDU variants only)
- **Simulation**: Gazebo/Ignition with URDF

---

## H1 — Full-Size Humanoid Robot

### Overview
The Unitree H1 is a full-size general-purpose humanoid robot launched in 2023. It holds the Guinness World Record as the fastest full-sized humanoid robot at 3.3 m/s (7.38 mph).

### Physical Specifications

| Parameter | Value |
|-----------|-------|
| Height | ~180 cm (human-scale) |
| Weight | ~47 kg (H1) / ~70 kg (H1-2) |
| Thigh/Calf Length | 400 mm each |
| Total Arm Length | 338 mm each |

### Degrees of Freedom

| Body Part | DOF | Configuration |
|-----------|-----|---------------|
| Each Leg | 5 | Hip × 3, Knee × 1, Ankle × 1 |
| Each Arm | 4 | Expandable |
| Torso | Varies | Waist articulation |
| Total | 19-27 | Depending on configuration |

### Performance Records

| Record | Value | Date |
|--------|-------|------|
| Running Speed | 3.3 m/s (7.38 mph) | Jan 2025 |
| Recognition | Guinness World Record | Jan 2025 |
| 400m Race | 1:28 | Aug 2025 |
| 1500m Race | 6:34:40 | Aug 2025 |

### Actuator Specifications

**M107 Joint Motor (full power):**

| Joint Location | Peak Torque |
|----------------|-------------|
| Knee | ~360 N·m |
| Hip | ~220 N·m |
| Ankle | ~59 N·m |
| Arm | ~75 N·m |

**Torque Density**: 189 N·m/kg (peak)

### Perception System

| Component | Specification |
|-----------|---------------|
| 3D LiDAR | Integrated |
| Depth Camera | Intel RealSense or equivalent |
| Coverage | 360° depth sensing |
| IMU | High-precision |

### Computing

| Tier | Processor | Purpose |
|------|-----------|---------|
| Platform | Intel Core i5 | Core motion control |
| Development | Intel Core i7 | User development |
| AI (Optional) | NVIDIA Jetson Orin NX | AI/ML workloads |

### Power System

| Parameter | Value |
|-----------|-------|
| Battery Capacity | 15 Ah (864 Wh) |
| Max Voltage | 67.2V |
| Runtime | ~2 hours |
| Hot-swap | Yes |

### Capabilities

- **Locomotion**: Walking, running, stair climbing
- **Dynamic Moves**: Backflip (first electric humanoid), jumping
- **Stability**: Balance recovery when pushed
- **Terrain**: Indoor/outdoor, uneven surfaces

### H1-2 Enhancements

| Feature | H1 | H1-2 |
|---------|-----|------|
| Weight | ~47 kg | ~70 kg |
| Torque Density | 189 N·m/kg | Enhanced |
| Joint Performance | Standard | Upgraded |
| Applications | Research | Heavy-duty |

---

## G1 vs H1 Comparison

| Feature | G1 | H1 |
|---------|-----|-----|
| **Price** | $16K-$74K | ~$90K-$112K |
| **Height** | 127 cm | 180 cm |
| **Weight** | ~35 kg | ~47-70 kg |
| **DOF** | 23-43 | 19-27 |
| **Max Speed** | 2+ m/s | 3.3 m/s (world record) |
| **Knee Torque** | 90-120 N·m | ~360 N·m |
| **Portability** | Folds to 69cm, transportable | Full-size, less portable |
| **Target** | Research, education | Advanced research, enterprise |
| **Compute** | Jetson Orin (EDU) | Intel i5/i7 + Jetson |

---

## Applications

### G1 Applications

1. **Research & Education**
   - Locomotion research
   - Human-robot interaction
   - Embodied AI
   - Manipulation studies

2. **Competitions**
   - RoboCup Humanoid League
   - World Humanoid Robot Games
   - Academic competitions

3. **Entertainment**
   - Public demonstrations
   - Marketing events
   - Interactive exhibits

### H1 Applications

1. **Advanced Research**
   - Full-size humanoid dynamics
   - Human-scale manipulation
   - Human-robot collaboration

2. **Industrial Pilot Programs**
   - Light factory tasks
   - Inspection at human height
   - Training scenarios

3. **Competition Performance**
   - Sprinting events
   - Obstacle courses
   - Complex athletic tasks

---

## Development Guide

### G1 EDU Setup

```bash
# 1. Network Connection
# Connect to G1 via WiFi (default network: UNITREE-G1-XXXX)
# SSH access available for EDU variants

# 2. ROS2 Setup
git clone https://github.com/unitreerobotics/unitree_ros2.git
cd unitree_ros2/colcon_ws
colcon build
source install/setup.bash

# 3. Launch G1 control
ros2 launch unitree_g1 g1_control.launch.py
```

### Key Topics (G1/H1)

| Topic | Type | Description |
|-------|------|-------------|
| `/joint_states` | JointState | All joint positions/velocities |
| `/imu/data` | Imu | IMU sensor data |
| `/livox/lidar` | PointCloud2 | LiDAR point cloud |
| `/camera/color/image_raw` | Image | RGB camera |
| `/camera/depth/image_rect_raw` | Image | Depth camera |

### Safety Considerations

1. **Always use safety perimeter** — H1 moves fast and has significant mass
2. **Emergency stop** — Keep within reach during operation
3. **Joint limits** — Respect mechanical limits to prevent damage
4. **Thermal monitoring** — Motors can overheat under sustained load
5. **Fall recovery** — Have clear space for potential falls

---

*Last Updated: 2026-03-21*
