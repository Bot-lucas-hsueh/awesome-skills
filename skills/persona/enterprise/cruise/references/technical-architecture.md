# Cruise Autonomous Vehicle Technical Architecture

## Overview

This document details the technical architecture of Cruise's autonomous vehicle systems, including sensor configuration, perception pipeline, prediction and planning systems, and safety architectures.

---

## Sensor Configuration

### Primary Sensor Array

| Sensor Type | Quantity | Manufacturer/Type | Purpose |
|-------------|----------|-------------------|---------|
| **LiDAR** | 5+ units | Custom/Velodyne | 360° 3D environmental mapping |
| **Cameras** | 10+ units | Various (surround view) | Object classification, scene understanding |
| **Radar** | 8+ units | Long and medium range | Velocity measurement, weather penetration |
| **Ultrasonic** | 12+ units | Short-range | Parking, close obstacle detection |
| **GPS/IMU** | 2 units (redundant) | High-precision | Localization, inertial measurement |
| **Microphones** | Multiple | Audio array | Emergency vehicle detection |

### LiDAR Configuration

```
LIDAR PLACEMENT (Typical Cruise AV):

              [Front LiDAR]
                   │
    [FL] ──────────┼────────── [FR]
   (Front-Left)    │          (Front-Right)
                   │
   [Left] ─────────┼────────── [Right]
                   │
              [Rear LiDAR]

Coverage:
├── 360° horizontal field of view
├── ~30° vertical field of view
├── Range: 200+ meters
├── Resolution: ~0.1° angular
└── Point density: millions of points/second
```

### Camera Configuration

| Position | Quantity | Field of View | Purpose |
|----------|----------|---------------|---------|
| Front | 3 | 120° | Long-range detection, traffic lights |
| Front-Left/Right | 2 | 80° | Cross-traffic, lane changes |
| Side (mirrors) | 2 | 100° | Blind spot, lane keeping |
| Rear | 2 | 120° | Following vehicles, reversing |
| Additional | Variable | Various | Redundancy, specific tasks |

### Radar Configuration

| Type | Quantity | Range | Purpose |
|------|----------|-------|---------|
| Long-range | 2 | 200m+ | Highway following |
| Medium-range | 4 | 100m | Urban environment |
| Short-range | 2 | 30m | Parking, close maneuvers |

---

## Perception System

### Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────┐
│                    PERCEPTION PIPELINE                              │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  ┌─────────┐   ┌─────────┐   ┌─────────┐   ┌─────────┐            │
│  │  LiDAR  │   │ Cameras │   │  Radar  │   │   IMU   │            │
│  │  Input  │   │  Input  │   │  Input  │   │  Input  │            │
│  └────┬────┘   └────┬────┘   └────┬────┘   └────┬────┘            │
│       │             │             │             │                  │
│       └─────────────┴─────────────┴─────────────┘                  │
│                         │                                          │
│                         ▼                                          │
│              ┌─────────────────────┐                               │
│              │  TIME SYNCHRONIZATION│                               │
│              │   (Phase Locking)    │                               │
│              └──────────┬──────────┘                               │
│                         │                                          │
│                         ▼                                          │
│              ┌─────────────────────┐                               │
│              │  SENSOR CALIBRATION  │                               │
│              │ - Intrinsic (camera) │                               │
│              │ - Extrinsic (fusion) │                               │
│              │ - Temporal alignment │                               │
│              └──────────┬──────────┘                               │
│                         │                                          │
│                         ▼                                          │
│              ┌─────────────────────┐                               │
│              │   LATE FUSION       │                               │
│              │  (Object-Level)     │                               │
│              └──────────┬──────────┘                               │
│                         │                                          │
│                         ▼                                          │
│              ┌─────────────────────┐                               │
│              │  OBJECT DETECTION   │                               │
│              │ - 2D/3D bounding box│                               │
│              │ - Classification    │                               │
│              │ - Confidence scores │                               │
│              └──────────┬──────────┘                               │
│                         │                                          │
│                         ▼                                          │
│              ┌─────────────────────┐                               │
│              │  OBJECT TRACKING    │                               │
│              │ - Kalman filtering  │                               │
│              │ - ID persistence    │                               │
│              │ - Trajectory history│                               │
│              └──────────┬──────────┘                               │
│                         │                                          │
│                         ▼                                          │
│              ┌─────────────────────┐                               │
│              │  ENVIRONMENT MODEL  │                               │
│              │ - Static obstacles  │                               │
│              │ - Dynamic actors    │                               │
│              │ - Free space        │                               │
│              │ - Lane boundaries   │                               │
│              └─────────────────────┘                               │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Late Fusion Approach

Cruise uses **late fusion** for sensor integration:

| Stage | Process | Output |
|-------|---------|--------|
| 1. Independent Detection | Each sensor processes raw data separately | Individual detections |
| 2. Object Association | Match detections across sensors using geometry | Associated object sets |
| 3. State Estimation | Combine measurements (weighted by confidence) | Fused object state |
| 4. Classification | Merge class probabilities | Final object classification |

**Advantages of Late Fusion:**
- Lower computational requirements than early fusion
- Simpler sensor integration
- Graceful degradation when sensors fail

**Disadvantages:**
- May miss correlations visible only in raw data
- Lower accuracy in complex scenarios
- Potential for conflicting detections

### Computer Vision Pipeline

```
CAMERA PROCESSING STEPS:

1. CAMERA CALIBRATION
   ├── Intrinsic: Remove lens distortion
   ├── Extrinsic: Determine camera pose relative to vehicle
   └── Output: Rectified images with known 3D projection

2. IMAGE PREPROCESSING
   ├── White balance
   ├── Denoising
   ├── HDR fusion (for high contrast scenes)
   └── Output: Clean, normalized images

3. OBJECT DETECTION
   ├── 2D bounding box detection (CNN-based)
   ├── Semantic segmentation
   ├── Instance segmentation
   └── Output: Detected objects with pixel masks

4. TRAFFIC LIGHT/SIGN DETECTION
   ├── Multi-class classification
   ├── State tracking over time
   ├── Occlusion handling
   └── Output: Traffic control states

5. LANE DETECTION
   ├── Edge detection
   ├── Curve fitting
   ├── Lane marking classification
   └── Output: Lane boundary polynomials
```

### LiDAR Processing

```
LIDAR PROCESSING PIPELINE:

1. POINT CLOUD PREPROCESSING
   ├── Ground plane estimation and removal
   ├── Point clustering
   ├── Outlier filtering
   └── Output: Segmented point clusters

2. OBJECT DETECTION
   ├── Cluster classification (vehicle, pedestrian, cyclist, static)
   ├── 3D bounding box estimation
   ├── Point cloud feature extraction
   └── Output: 3D object detections

3. FREE SPACE ESTIMATION
   ├── Ground occupancy grid
   ├── Drivable area identification
   └── Output: Drivable region map
```

### Radar Processing

```
RADAR PROCESSING:

1. SIGNAL PROCESSING
   ├── Doppler analysis for velocity
   ├── Range-azimuth processing
   ├── Multi-target tracking
   └── Output: Range-velocity-azimuth detections

2. OBJECT ASSOCIATION
   ├── Match with camera/LiDAR detections
   ├── Velocity verification
   └── Output: Velocity-augmented object tracks
```

---

## Prediction System

### Multi-Modal Trajectory Prediction

```
PREDICTION ARCHITECTURE:

Input: Object tracks from perception
       ├── Position history
       ├── Velocity history
       ├── Object class
       └── Scene context

Processing:
┌─────────────────────────────────────────────────────────┐
│  NEURAL NETWORK PREDICTOR                               │
│  ├── Scene encoder (CNN for context)                    │
│  ├── Agent encoder (LSTM for history)                   │
│  ├── Interaction module (attention-based)               │
│  └── Decoder (multi-modal trajectory generation)        │
└─────────────────────────────────────────────────────────┘

Output: Multiple possible future trajectories
        ├── Trajectory 1 (probability: 0.6)
        ├── Trajectory 2 (probability: 0.25)
        ├── Trajectory 3 (probability: 0.1)
        └── Trajectory N (probability: ...)
```

### Prediction Time Horizons

| Horizon | Duration | Use Case |
|---------|----------|----------|
| Immediate | 0-1 second | Emergency braking |
| Short-term | 1-3 seconds | Lane keeping, adaptive cruise |
| Medium-term | 3-8 seconds | Lane changes, intersections |
| Long-term | 8+ seconds | Route planning |

### Behavior Models

| Actor Type | Model Approach | Key Behaviors |
|------------|----------------|---------------|
| Vehicles | Physics + intent recognition | Lane keeping, lane changing, turning |
| Pedestrians | Social force models + crossing intent | Walking, crossing, waiting |
| Cyclists | Hybrid physics/social | Lane sharing, turn signals, unpredictability |
| Static | Map-based | Obstacles, construction |

---

## Planning System

### Three-Layer Architecture

```
PLANNING HIERARCHY:

┌─────────────────────────────────────────────────────────────┐
│ LAYER 3: ROUTE PLANNING                                     │
│ ├── Global path from start to destination                   │
│ ├── Road network graph search                               │
│ ├── Traffic-aware routing                                   │
│ └── Output: High-level route                                │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ LAYER 2: BEHAVIOR PLANNING                                  │
│ ├── High-level decision making                              │
│ ├── Maneuver selection (lane change, turn, stop)            │
│ ├── Traffic rule compliance                                 │
│ └── Output: Behavioral intent                               │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ LAYER 1: MOTION PLANNING                                    │
│ ├── Trajectory optimization                                 │
│ ├── Obstacle avoidance                                      │
│ ├── Comfort constraints                                     │
│ └── Output: Smooth trajectory                               │
└─────────────────────────────────────────────────────────────┘
```

### Route Planning

| Algorithm | A* with custom heuristics |
|-----------|---------------------------|
| Graph | HD map road network |
| Cost Function | Time, distance, traffic, complexity |
| Updates | Dynamic based on traffic conditions |

### Behavior Planning

```
BEHAVIOR STATE MACHINE:

States:
├── FOLLOW_LANE
│   └── Maintain position in current lane
├── CHANGE_LANE_LEFT/RIGHT
│   └── Execute lane change when safe
├── APPROACH_INTERSECTION
│   └── Prepare for stop/turn/continue
├── EXECUTE_TURN
│   └── Navigate intersection turn
├── FOLLOW_VEHICLE
│   └── Adaptive cruise behavior
├── EMERGENCY_STOP
│   └── Immediate safety stop
└── PULL_OVER
    └── Move to safe stopping location

Transitions:
├── Triggered by perception input
├── Validated by prediction
├── Safety-checked before execution
└── Fallback to conservative state on uncertainty
```

### Motion Planning

| Component | Description |
|-----------|-------------|
| Algorithm | Model Predictive Control (MPC) |
| Optimization | Cost minimization over trajectory |
| Constraints | Dynamics, comfort, safety, rules |
| Horizon | 5-10 seconds |
| Update Rate | 10-20 Hz |

**Cost Function Components:**
```
TOTAL_COST = 
    w1 * PATH_DEVIATION +
    w2 * VELOCITY_ERROR +
    w3 * ACCELERATION +
    w4 * JERK +
    w5 * OBSTACLE_PROXIMITY +
    w6 * RULE_VIOLATION +
    w7 * COMFORT
```

---

## Control System

### Model Predictive Control

```
MPC CONTROL LOOP:

1. STATE ESTIMATION
   ├── Vehicle position, velocity, acceleration
   ├── Heading, steering angle
   └── Uncertainty quantification

2. REFERENCE TRAJECTORY
   ├── From motion planner
   ├── Sampled at discrete intervals
   └── Includes desired position, velocity, heading

3. OPTIMIZATION
   ├── Predict vehicle response to control inputs
   ├── Optimize control sequence over horizon
   ├── Respect constraints (steering limits, acceleration limits)
   └── Minimize deviation from reference

4. CONTROL EXECUTION
   ├── Apply first control input from optimized sequence
   ├── Steering angle command
   ├── Acceleration/braking command
   └── Feedback to next iteration
```

### Control Outputs

| Output | Range | Rate |
|--------|-------|------|
| Steering | ±30° (typical) | 100 Hz |
| Throttle | 0-100% | 100 Hz |
| Brake | 0-100% | 100 Hz |
| Gear | P/R/N/D | As needed |
| Signals | On/Off | As needed |
| Lights | Various | As needed |

---

## Safety Architecture

### Fail-Operational Design

```
SAFETY LAYERS:

┌─────────────────────────────────────────────────────────────┐
│ PRIMARY SYSTEM                                              │
│ ├── Main computer                                           │
│ ├── Full sensor suite                                       │
│ └── Normal operation                                        │
└─────────────────────────┬───────────────────────────────────┘
                          │ Monitor
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ SECONDARY SYSTEM                                            │
│ ├── Backup computer                                         │
│ ├── Critical sensor subset                                  │
│ └── Degraded operation (Minimal Risk Condition)             │
└─────────────────────────┬───────────────────────────────────┘
                          │ Monitor
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ TERTIARY SYSTEM                                             │
│ ├── Safety microcontroller                                  │
│ ├── Independent sensors                                     │
│ └── Emergency stop only                                     │
└─────────────────────────────────────────────────────────────┘
```

### Minimal Risk Condition (MRC)

| Trigger | Response |
|---------|----------|
| Primary system failure | Switch to secondary, achieve MRC |
| Secondary failure | Emergency braking, hazard lights |
| Critical sensor loss | Stop safely in current lane |
| Communication loss | Complete current maneuver, then MRC |
| Remote operator request | Execute requested MRC |

### Safety Monitoring

```
SAFETY MONITORS:

1. HEALTH MONITOR
   ├── Computer status
   ├── Sensor status
   ├── Communication status
   └── Action: Degradation or MRC

2. PERFORMANCE MONITOR
   ├── Prediction accuracy
   ├── Planning feasibility
   ├── Control tracking error
   └── Action: Alert or intervention

3. RULE COMPLIANCE MONITOR
   ├── Speed limit adherence
   ├── Traffic signal compliance
   ├── Right-of-way rules
   └── Action: Correction or MRC

4. OCCUPANT SAFETY MONITOR
   ├── Acceleration limits
   ├── Jerk limits
   ├── Emergency braking justification
   └── Action: Comfort adjustment
```

---

## HD Mapping

### Map Components

| Component | Description | Update Frequency |
|-----------|-------------|------------------|
| Road geometry | Lane boundaries, centerlines | Semi-annual |
| Traffic control | Signals, signs, markings | Quarterly |
| Semantic info | Crosswalks, stop lines, etc. | Quarterly |
| Dynamic layer | Construction, temporary changes | Real-time |

### Map Creation

```
HD MAP PIPELINE:

1. DATA COLLECTION
   ├── Mapping vehicles with survey-grade LiDAR
   ├── Repeated drives for consistency
   ├── GNSS/INS for absolute positioning
   └── Millions of miles of data

2. PROCESSING
   ├── Point cloud registration
   ├── Feature extraction
   ├── Vectorization
   └── Semantic labeling

3. VALIDATION
   ├── Automated consistency checks
   ├── Human review of critical areas
   ├── Ground truth verification
   └── Quality assurance

4. DISTRIBUTION
   ├── Over-the-air updates
   ├── Differential updates for efficiency
   └── Version control
```

---

## Simulation Framework

### Simulation Types

| Type | Purpose | Scale |
|------|---------|-------|
| Unit testing | Component validation | Thousands/day |
| Scenario testing | Specific situations | Millions/day |
| Regression testing | Prevent degradation | Continuous |
| Exploration | Discover edge cases | Billions of miles |

### Simulation Architecture

```
SIMULATION STACK:

┌─────────────────────────────────────────────────────────────┐
│ SCENARIO GENERATION                                         │
│ ├── Procedural generation                                   │
│ ├── Real-world log replay                                   │
│ ├── Adversarial scenarios                                   │
│ └── Mutation of known scenarios                             │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ WORLD SIMULATION                                            │
│ ├── Traffic simulation (SUMO/CarSim)                        │
│ ├── Sensor simulation (ray tracing)                         │
│ ├── Physics simulation                                      │
│ └── Weather/lighting variation                              │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ AV SOFTWARE                                                 │
│ ├── Same code as vehicle                                    │
│ ├── SIL (Software-in-Loop)                                  │
│ └── HIL (Hardware-in-Loop) for final validation             │
└─────────────────────────┬───────────────────────────────────┘
                          │
                          ▼
┌─────────────────────────────────────────────────────────────┐
│ EVALUATION                                                  │
│ ├── Safety metrics                                          │
│ ├── Comfort metrics                                         │
│ ├── Rule compliance                                         │
│ └── Performance metrics                                     │
└─────────────────────────────────────────────────────────────┘
```

### Simulation to Reality Gap

| Challenge | Mitigation |
|-----------|------------|
| Sensor model accuracy | Validate against real data |
| Agent behavior realism | Use real-world driver models |
| Physics accuracy | Calibrate with vehicle testing |
| Edge case coverage | Continuous scenario expansion |

---

## Data Pipeline

### Data Collection

| Source | Volume/Rate | Use |
|--------|-------------|-----|
| Sensors | ~5 GB/minute | Training, debugging |
| System logs | ~100 MB/hour | Diagnostics, analysis |
| Teleoperations | Per intervention | Failure analysis |
| Customer feedback | Per report | Issue identification |

### Data Processing

```
DATA PIPELINE:

1. INGESTION
   ├── Vehicle upload (when connected)
   ├── Compression and encryption
   └── Metadata extraction

2. STORAGE
   ├── Hot storage (recent, frequently accessed)
   ├── Warm storage (training datasets)
   └── Cold storage (archival, compliance)

3. PROCESSING
   ├── Automated labeling (ML-assisted)
   ├── Human review (critical scenarios)
   ├── Scenario extraction
   └── Dataset creation

4. CONSUMPTION
   ├── Model training
   ├── Simulation scenarios
   ├── Safety analysis
   └── Regulatory reporting
```

---

## Compute Architecture

### Onboard Computing

| Component | Specification | Purpose |
|-----------|---------------|---------|
| Primary computer | High-performance GPU/CPU | Perception, prediction, planning |
| Secondary computer | Redundant architecture | Backup processing |
| Safety MCU | Automotive-grade | Critical safety functions |
| Networking | Automotive Ethernet | Sensor data, inter-computer comms |
| Storage | NVMe SSD | Data logging, map storage |

### Compute Distribution

```
COMPUTE ALLOCATION:

Perception:     ████████████████████ 40%
Prediction:     ████████████ 25%
Planning:       ████████ 15%
Control:        ████ 8%
Safety:         ███ 6%
System/Other:   ███ 6%
```

---

## Post-Incident Technical Changes

### Changes After October 2023

| System | Before | After |
|--------|--------|-------|
| Post-collision behavior | Automatic pullover | Stop-and-assess protocol |
| Under-vehicle detection | Limited | Enhanced with additional sensors |
| Pullover authorization | System-initiated | Remote operator required post-collision |
| Impact assessment | Basic | Multi-modal verification |
| Emergency response | Manual notification | Automatic notification system |

### Enhanced Detection

```
POST-INCIDENT SENSOR ENHANCEMENTS:

1. UNDER-VEHICLE DETECTION
   ├── Additional ultrasonic sensors
   ├── Thermal imaging consideration
   ├── Audio impact detection
   └── IMU resistance analysis

2. POST-COLLISION ASSESSMENT
   ├── 10-second mandatory stop
   ├── Multi-sensor clear-path verification
   ├── Remote operator consultation
   └── Emergency services auto-notification

3. PULLOVER RESTRICTIONS
   ├── No movement until all-clear
   ├── Override by remote operator only
   ├── Default: Stay stationary
   └── Enhanced hazard signaling
```

---

## References

- Cruise Engineering Blog (archived)
- Kyle Vogt Technical Presentations (2017-2023)
- SAE Autonomous Vehicle Standards (J3016)
- ISO 26262 Functional Safety
- Waymo Open Dataset (comparative)
