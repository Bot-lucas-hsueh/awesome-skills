# Unitree SDK and Development Guide

## Overview

Unitree provides comprehensive software development kits for their robots, enabling researchers and developers to build custom applications. The SDK ecosystem supports C++, Python, and ROS2.

## SDK Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                    APPLICATION LAYER                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐  │
│  │   Python    │  │    C++      │  │        ROS2             │  │
│  │    SDK      │  │    SDK      │  │     (unitree_ros2)      │  │
│  └──────┬──────┘  └──────┬──────┘  └───────────┬─────────────┘  │
└─────────┼────────────────┼────────────────────┼────────────────┘
          │                │                    │
          └────────────────┴────────────────────┘
                             │
┌────────────────────────────┼────────────────────────────────────┐
│                    UNITREE SDK2 (Core)                         │
│  ┌─────────────────────────────────────────────────────────┐   │
│  │  Communication Layer (CycloneDDS)                       │   │
│  │  ├── Low-level motor control                            │   │
│  │  ├── Sensor data streaming                              │   │
│  │  └── State machine management                           │   │
│  └─────────────────────────────────────────────────────────┘   │
└────────────────────────────────────────────────────────────────┘
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
          ┌─────────────┐    ┌─────────────┐
          │   Go2/B2    │    │   G1/H1     │
          │  Quadruped  │    │  Humanoid   │
          └─────────────┘    └─────────────┘
```

## unitree_sdk2 — Core SDK

### Installation

```bash
# Clone the SDK
git clone https://github.com/unitreerobotics/unitree_sdk2.git
cd unitree_sdk2

# Build
mkdir build && cd build
cmake ..
make -j$(nproc)
sudo make install
```

### Dependencies

| Dependency | Version | Purpose |
|------------|---------|---------|
| CMake | 3.10+ | Build system |
| CycloneDDS | Latest | DDS communication |
| gRPC | 1.40+ | RPC interface |

### C++ Example: Basic Control

```cpp
#include <unitree_sdk2/unitree_sdk2.h>
#include <iostream>

using namespace unitree;

int main() {
    // Initialize robot interface
    RobotInterface robot;
    
    // Connect to robot
    if (!robot.Init()) {
        std::cerr << "Failed to initialize robot" << std::endl;
        return -1;
    }
    
    // Set robot to standing mode
    robot.SetControlMode(ControlMode::STAND);
    
    // Wait for standing
    std::this_thread::sleep_for(std::chrono::seconds(2));
    
    // Set to locomotion mode
    robot.SetControlMode(ControlMode::WALK);
    
    // Send velocity command
    VelocityCommand cmd;
    cmd.linear_x = 0.5;  // m/s forward
    cmd.linear_y = 0.0;  // m/s lateral
    cmd.angular_z = 0.0; // rad/s rotation
    
    robot.SetVelocity(cmd);
    
    // Run for 5 seconds
    std::this_thread::sleep_for(std::chrono::seconds(5));
    
    // Stop
    cmd.linear_x = 0.0;
    robot.SetVelocity(cmd);
    
    return 0;
}
```

### Python Bindings

```bash
# Install Python SDK
pip install unitree-sdk2-python
```

```python
from unitree_sdk2 import RobotInterface, ControlMode, VelocityCommand
import time

# Initialize robot
robot = RobotInterface()
robot.init()

# Stand up
robot.set_control_mode(ControlMode.STAND)
time.sleep(2)

# Start walking
robot.set_control_mode(ControlMode.WALK)

# Move forward
cmd = VelocityCommand()
cmd.linear_x = 0.5  # m/s
cmd.linear_y = 0.0
cmd.angular_z = 0.0
robot.set_velocity(cmd)

time.sleep(5)

# Stop
cmd.linear_x = 0.0
robot.set_velocity(cmd)
```

---

## unitree_ros2 — ROS2 Integration

### Supported Robots

| Robot | ROS2 Distro | Status |
|-------|-------------|--------|
| Go2 | Humble, Foxy | ✅ Supported |
| B2 | Humble, Foxy | ✅ Supported |
| H1 | Humble, Foxy | ✅ Supported |
| G1 | Humble, Foxy | ✅ Supported |

### Installation

```bash
# 1. Install ROS2 Humble (Ubuntu 22.04)
sudo apt update
sudo apt install ros-humble-desktop

# 2. Install CycloneDDS
sudo apt install ros-humble-rmw-cyclonedds-cpp

# 3. Create workspace
mkdir -p ~/unitree_ws/src
cd ~/unitree_ws/src

# 4. Clone repositories
git clone https://github.com/unitreerobotics/unitree_ros2.git
git clone https://github.com/unitreerobotics/unitree_sdk2.git

# 5. Install dependencies
cd ~/unitree_ws
rosdep install --from-paths src --ignore-src -r -y

# 6. Build
colcon build --cmake-args -DCMAKE_BUILD_TYPE=Release

# 7. Source
source install/setup.bash
```

### CycloneDDS Configuration

Create `~/.ros/cyclonedds_config.xml`:

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<CycloneDDS xmlns="https://cdds.io/config"
            xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
            xsi:schemaLocation="https://cdds.io/config
                                https://raw.githubusercontent.com/eclipse-cyclonedds/cyclonedds/master/etc/cyclonedds.xsd">
    <Domain id="any">
        <General>
            <NetworkInterfaceAddress>auto</NetworkInterfaceAddress>
            <AllowMulticast>true</AllowMulticast>
        </General>
    </Domain>
</CycloneDDS>
```

Set environment:
```bash
export RMW_IMPLEMENTATION=rmw_cyclonedds_cpp
export CYCLONEDDS_URI=file://$HOME/.ros/cyclonedds_config.xml
```

### ROS2 Topics

#### Go2/B2 Topics

| Topic | Type | Publisher | Description |
|-------|------|-----------|-------------|
| `/cmd_vel` | geometry_msgs/Twist | User | Velocity commands |
| `/joint_states` | sensor_msgs/JointState | Robot | Joint positions/velocities |
| `/imu` | sensor_msgs/Imu | Robot | IMU data |
| `/utlidar/cloud` | sensor_msgs/PointCloud2 | Robot | 4D LiDAR point cloud |
| `/odom` | nav_msgs/Odometry | Robot | Odometry estimate |
| `/robot_status` | unitree_go2_msgs/RobotState | Robot | Robot state |

#### G1/H1 Topics

| Topic | Type | Publisher | Description |
|-------|------|-----------|-------------|
| `/joint_states` | sensor_msgs/JointState | Robot | Joint positions |
| `/imu/data` | sensor_msgs/Imu | Robot | IMU data |
| `/livox/lidar` | sensor_msgs/PointCloud2 | Robot | LiDAR point cloud |
| `/camera/color/image_raw` | sensor_msgs/Image | Robot | RGB camera |
| `/camera/depth/image_rect_raw` | sensor_msgs/Image | Robot | Depth camera |

### ROS2 Control Example

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
import threading

class UnitreeController(Node):
    def __init__(self):
        super().__init__('unitree_controller')
        
        # Publisher for velocity commands
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        
        # Subscriber for joint states
        self.joint_sub = self.create_subscription(
            JointState, '/joint_states', self.joint_callback, 10)
        
        # Current joint positions
        self.joint_positions = {}
        
    def joint_callback(self, msg):
        for name, position in zip(msg.name, msg.position):
            self.joint_positions[name] = position
            
    def move_forward(self, speed=0.5, duration=5.0):
        """Move forward at specified speed for duration"""
        cmd = Twist()
        cmd.linear.x = speed
        
        start_time = self.get_clock().now()
        while (self.get_clock().now() - start_time).nanoseconds < duration * 1e9:
            self.cmd_pub.publish(cmd)
            rclpy.spin_once(self, timeout_sec=0.1)
        
        # Stop
        cmd.linear.x = 0.0
        self.cmd_pub.publish(cmd)
        
    def rotate(self, angular_speed=0.5, duration=3.0):
        """Rotate at specified angular speed"""
        cmd = Twist()
        cmd.angular.z = angular_speed
        
        start_time = self.get_clock().now()
        while (self.get_clock().now() - start_time).nanoseconds < duration * 1e9:
            self.cmd_pub.publish(cmd)
            rclpy.spin_once(self, timeout_sec=0.1)
        
        # Stop
        cmd.angular.z = 0.0
        self.cmd_pub.publish(cmd)

def main():
    rclpy.init()
    controller = UnitreeController()
    
    # Move forward
    controller.move_forward(speed=0.5, duration=5.0)
    
    # Rotate
    controller.rotate(angular_speed=0.3, duration=3.0)
    
    controller.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
```

---

## Navigation with Nav2

### Installation

```bash
sudo apt install ros-humble-navigation2 ros-humble-nav2-bringup
```

### Launch Navigation

```bash
# Terminal 1: Start robot
ros2 launch unitree_go2 go2.launch.py

# Terminal 2: Start navigation
ros2 launch nav2_bringup navigation_launch.py

# Terminal 3: Start SLAM (optional)
ros2 launch slam_toolbox online_async_launch.py
```

### Custom Navigation Node

```python
import rclpy
from rclpy.action import ActionClient
from rclpy.node import Node
from nav2_msgs.action import NavigateToPose
from geometry_msgs.msg import PoseStamped

class Nav2Client(Node):
    def __init__(self):
        super().__init__('nav2_client')
        self._action_client = ActionClient(self, NavigateToPose, 'navigate_to_pose')
        
    def send_goal(self, x, y, theta):
        goal_msg = NavigateToPose.Goal()
        goal_msg.pose = PoseStamped()
        goal_msg.pose.header.frame_id = 'map'
        goal_msg.pose.header.stamp = self.get_clock().now().to_msg()
        goal_msg.pose.pose.position.x = x
        goal_msg.pose.pose.position.y = y
        goal_msg.pose.pose.orientation.z = np.sin(theta / 2)
        goal_msg.pose.pose.orientation.w = np.cos(theta / 2)
        
        self._action_client.wait_for_server()
        self._send_goal_future = self._action_client.send_goal_async(goal_msg)
        self._send_goal_future.add_done_callback(self.goal_response_callback)
```

---

## Simulation

### Gazebo/Ignition Setup

```bash
# Install Ignition Fortress
sudo apt install ignition-fortress ros-humble-ros-gz

# Launch simulation
ros2 launch unitree_go2 gazebo.launch.py
```

### URDF Models

URDF files are available in `unitree_ros2`:
- `go2_description`
- `b2_description`
- `g1_description`
- `h1_description`

### Sim-to-Real Transfer

1. **Train in simulation** using Isaac Gym or Gazebo
2. **Domain randomization** for robust policies
3. **Fine-tune on real robot** with small learning rate
4. **Safety validation** before autonomous operation

---

## Best Practices

### 1. Communication Safety

```cpp
// Always check connection status
if (!robot.IsConnected()) {
    // Handle disconnection
    robot.Reconnect();
}
```

### 2. Joint Limit Protection

```python
# Check joint limits before commanding
JOINT_LIMITS = {
    'hip_yaw': (-2.5, 2.5),
    'hip_roll': (-0.5, 2.0),
    'hip_pitch': (-2.5, 2.5),
    'knee': (0.0, 2.8),
}

def is_valid_command(joint_name, position):
    if joint_name in JOINT_LIMITS:
        min_val, max_val = JOINT_LIMITS[joint_name]
        return min_val <= position <= max_val
    return True
```

### 3. Emergency Stop

```python
import signal
import sys

def emergency_stop(signum, frame):
    """Emergency stop handler"""
    print("EMERGENCY STOP TRIGGERED")
    robot.set_control_mode(ControlMode.STAND)
    robot.set_velocity(VelocityCommand())  # Zero velocity
    sys.exit(0)

signal.signal(signal.SIGINT, emergency_stop)
signal.signal(signal.SIGTERM, emergency_stop)
```

### 4. Thermal Monitoring

```python
def check_motor_temperatures(robot):
    """Monitor motor temperatures and throttle if needed"""
    temps = robot.get_motor_temperatures()
    for motor_id, temp in temps.items():
        if temp > 80:  # 80°C threshold
            print(f"Warning: Motor {motor_id} at {temp}°C")
            # Reduce torque limits
            robot.set_torque_limit(motor_id, 0.5)
        if temp > 90:  # 90°C critical
            print(f"Critical: Motor {motor_id} overheating!")
            robot.emergency_stop()
```

---

## Troubleshooting

### Connection Issues

| Problem | Solution |
|---------|----------|
| Cannot connect to robot | Check WiFi connection, ensure robot is powered on |
| Topics not visible | Verify CycloneDDS configuration, check network interface |
| High latency | Use Ethernet instead of WiFi, reduce topic frequency |
| Packet loss | Check network congestion, increase DDS buffer sizes |

### Control Issues

| Problem | Solution |
|---------|----------|
| Robot doesn't move | Check control mode (must be WALK for locomotion) |
| Jerky motion | Reduce velocity commands, check joint calibration |
| Falls frequently | Check gait parameters, verify flat ground |
| Motors hot | Reduce load, add cooling breaks, check for binding |

---

*Last Updated: 2026-03-21*
