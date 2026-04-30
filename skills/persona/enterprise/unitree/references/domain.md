## § 2 — Domain Knowledge

### 2.1 Robot Portfolio

**Quadruped Robots — Foundation of Expertise:**

| Model | Target | Key Specs | Price (USD) |
|-------|--------|-----------|-------------|
| **Go2** | Research/Education | 4D LiDAR L1, 1-2hr battery, 3.5 m/s, 5-7kg payload | ~$1,600-$3,000 |
| **Go2-W** | Research + Wheels | Wheeled variant for smooth surfaces, faster transit | ~$2,500-$4,000 |
| **B2** | Industrial | 6 m/s, 40kg sustained load, 5hr endurance, IP67 | ~$15,000-$25,000 |
| **B2-W** | Industrial + Wheels | Wheeled industrial for warehouses, long corridors | ~$20,000-$30,000 |

**Humanoid Robots — Market Disruptors:**

| Model | Height | Weight | DOF | Key Specs | Price (USD) |
|-------|--------|--------|-----|-----------|-------------|
| **G1** | 127-132cm | ~35kg | 23-43 | 90-120 N·m knee torque, 2hr runtime, folding | $16,000-$73,900 |
| **G1 EDU** | 127-132cm | ~35kg | 23-43 | Jetson Orin, SDK access, research-focused | $40,000-$73,900 |
| **H1** | ~180cm | ~47kg | 19-27 | 360 N·m max torque, 3.3 m/s run, backflip capable | ~$90,000-$112,000 |
| **H1-2** | ~178cm | ~70kg | 27 | Enhanced version, 189 N·m/kg torque density | ~$112,000 |

### 2.2 Core Technology Stack

**M107 Joint Motor — The Secret Sauce:**

```
┌─────────────────────────────────────────────────────────────────┐
│  UNITREE M107 HIGH-PERFORMANCE JOINT MOTOR                       │
├─────────────────────────────────────────────────────────────────┤
│  Specifications:                                                  │
│  ├── Peak Torque: 360 N·m (H1 legs) / 220 N·m (H1 hips)          │
│  ├── Torque Density: 220 N·m/kg (industry-leading)               │
│  ├── Motor Type: Low-inertia internal-rotor PMSM                 │
│  ├── Cooling: Local air cooling for sustained operation          │
│  ├── Bearings: Industrial crossed-roller (high precision)        │
│  ├── Encoders: Dual encoders for precise position control        │
│  └── Routing: Full joint-hollow for clean cable management       │
├─────────────────────────────────────────────────────────────────┤
│  Joint Range (G1 EDU):                                            │
│  ├── Waist Z: ±155°                                               │
│  ├── Hip P: ±154° | Hip R: -30° ~ +170° | Hip Y: ±158°          │
│  ├── Knee: 0° ~ 165°                                              │
│  └── Wrist (EDU): P ±92.5° | Y ±92.5°                            │
└─────────────────────────────────────────────────────────────────┘
```

**4D LiDAR L1 — Spatial Intelligence:**

| Feature | Specification |
|---------|---------------|
| Coverage | 360° × 90° hemispherical |
| Min Detection | 0.05m (ultra-low blind spot) |
| Technology | Solid-state MEMS |
| Integration | Self-developed by Unitree |
| Use Cases | SLAM, obstacle avoidance, terrain mapping |

**Computing Architecture:**

| Component | G1 | G1 EDU | H1 |
|-----------|-----|--------|-----|
| Main CPU | 8-core high-performance | 8-core + Jetson Orin | Intel Core i5/i7 |
| AI Compute | — | 100 TOPS (Orin) | Optional Jetson Orin NX |
| WiFi | WiFi 6 | WiFi 6 | WiFi 6/6E |
| Bluetooth | 5.2 | 5.2 | 5.2 |

### 2.3 Software & Development

**ROS2 Support:**

```bash
# Unitree ROS2 Setup (supports Go2, B2, H1, G1)
git clone https://github.com/unitreerobotics/unitree_ros2.git
cd unitree_ros2
# CycloneDDS-based communication
# Direct ROS2 message compatibility
```

**SDK & APIs:**

| SDK | Languages | Features |
|-----|-----------|----------|
| unitree_sdk2 | C++, Python | Core robot control, gait generation |
| unitree_ros2 | C++, Python | ROS2 Humble/Foxy integration |
| Livox SDK2 | C++ | LiDAR integration (G1) |

**Simulation Support:**
- Gazebo/Ignition Fortress integration
- URDF models available
- Sim-to-real transfer for gait policies

### 2.4 Company History

```
2016 — Wang Xingxing develops XDog as master's project
        └─ Low-cost external rotor brushless motors
        └─ Full-DOF actuation system
        
2017 — Unitree Robotics founded, Laikago released

2019 — Aliengo industrial quadruped

2021 — A1 quadruped (~$10K), Go1 launch
        └─ Spring Festival Gala performance
        
2022 — Go1 at Beijing Winter Olympics

2023 — Go2 (4D LiDAR), B2 industrial, H1 humanoid
        └─ H1: China's first full-size running humanoid
        
2024 — G1 humanoid launched at $16,000
        └─ Price breakthrough: 1/6th of competitors
        
2025 — World Humanoid Robot Games: 11 medals (4 gold)
        └─ H1 sets Guinness speed record: 3.3 m/s
        └─ CCTV Spring Festival Gala performance
        └─ Series C funding: $1.7B valuation
        └─ IPO documentation planned Oct-Dec 2025
```

---
