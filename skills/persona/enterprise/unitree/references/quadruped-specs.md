# Unitree Quadruped Specifications

## Go2 — Consumer/Research Quadruped

### Overview
The Unitree Go2 is an advanced quadruped robot designed for research, education, and light industrial applications. It features Unitree's self-developed 4D LiDAR L1 and embodied AI capabilities.

### Physical Specifications

| Parameter | Value |
|-----------|-------|
| Weight | ~15 kg |
| Dimensions | ~70cm × 40cm × 50cm (standing) |
| Degrees of Freedom | 12 (3 per leg) |
| Max Speed | 3.5 m/s |
| Payload | 5-7 kg (depending on variant) |

### Perception System

**4D LiDAR L1:**
- Coverage: 360° × 90° hemispherical
- Minimum detection distance: 0.05m
- Technology: Solid-state MEMS
- Applications: SLAM, obstacle avoidance, terrain mapping

**Additional Sensors:**
- Front camera for visual navigation
- IMU for balance and orientation
- Foot force sensors (EDU variant)

### Computing

| Component | Specification |
|-----------|---------------|
| Main Processor | 8-core ARM high-performance CPU |
| AI Processing | Built-in NPU for gait optimization |
| Connectivity | WiFi 6, Bluetooth 5.2 |

### Battery & Power

- Capacity: ~8,000 mAh
- Runtime: 1-2 hours (depending on activity)
- Charging: AC adapter, ~1 hour charge time

### Variants

| Variant | Target | Key Features |
|---------|--------|--------------|
| Go2 Air | Entry | Basic features, lower speed |
| Go2 Pro | Research | 4D LiDAR, enhanced computing |
| Go2 EDU | Education | Full SDK, ROS2 support |

### Software Support

- **ROS2**: Full support via unitree_ros2
- **SDK**: C++ and Python APIs
- **Simulation**: Gazebo/Ignition Fortress

---

## B2 — Industrial Quadruped

### Overview
The Unitree B2 is an industrial-grade quadruped designed for heavy-duty applications including inspection, security patrol, and logistics. It offers superior speed, payload capacity, and endurance.

### Physical Specifications

| Parameter | Value |
|-----------|-------|
| Weight | ~60 kg |
| Dimensions | ~80cm × 50cm × 70cm (standing) |
| Degrees of Freedom | 12 (3 per leg) |
| Max Speed | 6 m/s (21.6 km/h) |
| Standing Load | 120 kg |
| Sustained Walking Load | 40 kg |

### Mobility

| Capability | Specification |
|------------|---------------|
| Step Climbing | Up to 40 cm |
| Slope Traversal | >45° |
| Jump Distance | >1.6m (long jump) |
| Terrain | All-terrain: indoor, outdoor, stairs |

### Endurance

| Condition | Runtime |
|-----------|---------|
| Unloaded continuous walking | 5+ hours |
| 20 kg load continuous walking | 4+ hours |
| Standby | 8+ hours |

### Environmental Protection

- **IP Rating**: IP67
- **Dust**: Complete dust ingress protection
- **Water**: Protected against immersion up to 1m
- **Temperature**: Operating range -10°C to 40°C

### Perception System

| Sensor | Count | Purpose |
|--------|-------|---------|
| 3D LiDAR | 1 | Mapping, SLAM |
| Depth Cameras | 2 | Obstacle detection |
| Optical Cameras | 2 | Visual inspection |
| IMU | 1 | Balance, orientation |

### Computing Architecture

| Tier | Processor | Purpose |
|------|-----------|---------|
| Platform | Intel Core i5 | Core robot functions |
| Development | Intel Core i7 | User development |
| AI (Optional) | NVIDIA Jetson Orin NX | AI/ML workloads |

### Battery System

- **Capacity**: 45 Ah (2250 Wh)
- **Type**: Hot-swappable lithium battery
- **Swap Time**: <30 seconds
- **Charging**: External charger or autonomous docking

### Applications

1. **Industrial Inspection**
   - Power substation patrol
   - Manufacturing facility monitoring
   - Equipment thermal scanning

2. **Security Patrol**
   - Perimeter monitoring
   - Intrusion detection
   - Alarm response

3. **Emergency Response**
   - Hazardous environment reconnaissance
   - Search and rescue support
   - Disaster assessment

4. **Logistics**
   - Warehouse inventory transport
   - Last-50-meters delivery
   - Tool/equipment carrying

### B2-W Variant

The B2-W adds wheels to the feet for enhanced mobility on flat surfaces:
- **Advantage**: Faster transit on smooth floors
- **Use Case**: Warehouses, corridors, paved areas
- **Trade-off**: Slightly reduced rough-terrain capability

---

## Comparison: Go2 vs B2

| Feature | Go2 | B2 |
|---------|-----|-----|
| **Target Market** | Research/Education | Industrial/Commercial |
| **Price** | ~$1,600-$3,000 | ~$15,000-$25,000 |
| **Weight** | ~15 kg | ~60 kg |
| **Max Speed** | 3.5 m/s | 6 m/s |
| **Payload** | 5-7 kg | 40 kg sustained |
| **Endurance** | 1-2 hours | 5+ hours |
| **IP Rating** | Consumer grade | IP67 |
| **LiDAR** | 4D L1 | 3D LiDAR |
| **Hot-swap Battery** | No | Yes |
| **Outdoor Use** | Limited | Full capability |

---

## Development Guide

### ROS2 Setup

```bash
# Install ROS2 Humble
sudo apt install ros-humble-desktop

# Install CycloneDDS
sudo apt install ros-humble-rmw-cyclonedds-cpp

# Clone Unitree ROS2
git clone https://github.com/unitreerobotics/unitree_ros2.git
cd unitree_ros2

# Build
colcon build
source install/setup.bash
```

### Basic Control

```python
# Python example for Go2/B2 velocity control
import rclpy
from geometry_msgs.msg import Twist

rclpy.init()
node = rclpy.create_node('unitree_controller')
pub = node.create_publisher(Twist, '/cmd_vel', 10)

# Move forward
cmd = Twist()
cmd.linear.x = 0.5  # m/s
cmd.angular.z = 0.0  # rad/s
pub.publish(cmd)
```

### Available Topics

| Topic | Message Type | Description |
|-------|--------------|-------------|
| `/cmd_vel` | Twist | Velocity commands |
| `/joint_states` | JointState | Joint positions, velocities |
| `/imu` | Imu | IMU data |
| `/utlidar/cloud` | PointCloud2 | LiDAR point cloud |
| `/odom` | Odometry | Odometry estimate |

---

*Last Updated: 2026-03-21*
