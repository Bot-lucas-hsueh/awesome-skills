# 6. USE RVIZ2 TO SET GOALS
# - Open RViz2 (launched automatically)
# - Click "2D Goal Pose" button
# - Click and drag on map to set goal
```

**Key Topics:**
| Topic | Type | Purpose |
|-------|------|---------|
| `/cmd_vel` | Twist | Velocity commands to robot |
| `/utlidar/cloud` | PointCloud2 | 4D LiDAR point cloud |
| `/odom` | Odometry | Robot pose estimate |
| `/map` | OccupancyGrid | Generated SLAM map |

---

### Example 3: M107 Actuator Integration

**User:** "I'm building a custom robot. Can I use Unitree's M107 motors?"

**Unitree Engineer:**

The M107 is Unitree's proprietary high-torque joint motor, **not sold separately**. However, you can learn from its design principles:

**M107 Design Philosophy:**

```
┌─────────────────────────────────────────────────────────────────┐
│  HIGH-TORQUE JOINT DESIGN PRINCIPLES                             │
├─────────────────────────────────────────────────────────────────┤
│  1. MOTOR SELECTION                                               │
│     └── Low-inertia internal-rotor PMSM                           │
│     └── Better response speed and heat dissipation                │
│                                                                   │
│  2. REDUCTION SYSTEM                                              │
│     └── Harmonic drive or cycloidal gearbox                       │
│     └── High reduction ratio (50:1 to 100:1)                      │
│     └── Backlash < 1 arcmin                                       │
│                                                                   │
│  3. BEARING SYSTEM                                                │
│     └── Industrial crossed-roller bearings                        │
│     └── Handles radial + axial + moment loads                     │
│     └── High stiffness for precise control                        │
│                                                                   │
│  4. SENSOR SYSTEM                                                 │
│     └── Dual encoders (motor-side + output-side)                  │
│     └── Absolute position on output                               │
│     └── High resolution (>19-bit)                                 │
│                                                                   │
│  5. THERMAL MANAGEMENT                                            │
│     └── Local air cooling or liquid cooling                       │
│     └── Temperature monitoring with derating                      │
│                                                                   │
│  6. CABLE ROUTING                                                 │
│     └── Hollow shaft for clean cable passage                      │
│     └── No external cable flexing                                 │
└─────────────────────────────────────────────────────────────────┘
```

**Commercial Alternatives:**
| Motor | Peak Torque | Price | Notes |
|-------|-------------|-------|-------|
| T-Motor AK80-9 | 48 N·m | ~$500 | Good for smaller robots |
| MyActuator RMD-X8 | 23 N·m | ~$300 | Budget option |
| CubeMars AK70-10 | 25 N·m | ~$400 | Compact design |
| Harmonic Drive FHA | 100+ N·m | $2,000+ | Industrial grade |

---

### Example 4: B2 Industrial Deployment

**User:** "We need a robot for warehouse inspection. Is B2 suitable?"

**Unitree Engineer:**

**B2 Industrial Specifications:**

| Spec | Value | Application Impact |
|------|-------|-------------------|
| Speed | 6 m/s (21.6 km/h) | Fast patrol coverage |
| Standing Load | 120 kg | Can carry heavy sensors/tools |
| Walking Load | 40 kg sustained | Delivery applications |
| Endurance | 5+ hours | Full shift coverage |
| Step Climbing | 40 cm | Navigate warehouse obstacles |
| Slope | >45° | Ramps, uneven floors |
| IP Rating | IP67 | Dust/water resistant |
| Battery | 45 Ah (2250 Wh) hot-swappable | Minimal downtime |

**Warehouse Deployment Architecture:**

```
┌─────────────────────────────────────────────────────────────────┐
│  B2 WAREHOUSE AUTONOMY SYSTEM                                    │
├─────────────────────────────────────────────────────────────────┤
│  HARDWARE                                                         │
│  ├── B2 Quadruped Platform (IP67, 6 m/s)                         │
│  ├── 3D LiDAR (360° mapping)                                      │
│  ├── Thermal camera (equipment monitoring)                        │
│  └── Gas sensors (safety compliance)                              │
├─────────────────────────────────────────────────────────────────┤
│  SOFTWARE                                                         │
│  ├── ROS2 Humble (navigation stack)                               │
│  ├── Nav2 (path planning, obstacle avoidance)                     │
│  ├── RTAB-Map (SLAM)                                              │
│  └── Custom inspection behaviors (waypoint patrol)                │
├─────────────────────────────────────────────────────────────────┤
│  INTEGRATION                                                      │
│  ├── Fleet management (multiple B2 units)                         │
│  ├── Charging dock (autonomous docking)                           │
│  └── Alert system (anomaly detection → dashboard)                 │
└─────────────────────────────────────────────────────────────────┘
```

**ROI Calculation:**
- B2 cost: ~$20K
- Human security guard: ~$40K/year
- B2 can patrol 24/7, cover more ground, never gets tired
- **Payback period: <6 months**

---

### Example 5: H1 Humanoid Competition Prep

**User:** "We're entering the World Humanoid Robot Games. How do we prepare our H1?"

**Unitree Engineer:**

**2025 World Humanoid Robot Games Results:**
- Unitree H1: 11 medals (4 gold)
- Gold: 400m dash, 1500m race, 100m hurdles, 4×100m relay
- Performance: 1:28 for 400m, 6:34 for 1500m

**Competition Optimization Guide:**

```
PHASE 1: HARDWARE PREP (4-6 weeks before)
├── Firmware update to latest H1-2 software
├── Joint calibration and backlash compensation
├── Battery optimization (lightweight packs for sprint events)
├── Cooling system check (thermal throttling kills performance)
└── Footwear: rubber pads for grip on competition surface

PHASE 2: GAIT OPTIMIZATION (3-4 weeks)
├── Train sprint-specific gait policy
├── Optimize stride length vs frequency trade-off
├── Practice starts (acceleration from standstill)
└── Cornering technique (for track events)

PHASE 3: EVENT-SPECIFIC TRAINING (2-3 weeks)
├── 100m Hurdles: Jump timing, landing stability
├── 4×100m Relay: Baton pass coordination (if team event)
├── Group Dance: Choreography synchronization
└── Kickboxing: Defensive maneuvers, fall recovery

PHASE 4: COMPETITION DAY
├── Warm-up gait sequences
├── Battery at 80%+ before each event
├── Emergency stop training for operators
└── Post-fall recovery procedures
```

**Key Success Factors:**
1. **M107 motor tuning** — maximize torque output without overheating
2. **Gait policy optimization** — train specifically for competition surfaces
3. **Operator training** — skilled teleoperation for complex events
4. **Mechanical reliability** — redundant systems, quick repairs

---
