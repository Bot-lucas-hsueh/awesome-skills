# FSD (Full Self-Driving) Architecture Deep Dive

## Overview

Tesla's Full Self-Driving (FSD) is an advanced driver-assistance system (ADAS) that aims to achieve full autonomy using a vision-only approach. Unlike competitors who use LIDAR, radar, and HD maps, Tesla relies exclusively on cameras and neural networks.

## Evolution Timeline

| Version | Year | Key Features |
|---------|------|--------------|
| Autopilot (HW1) | 2014 | Mobileye-based, lane keeping, TACC |
| Autopilot (HW2) | 2016 | Tesla Vision, 8 cameras |
| FSD Beta | 2020 | City streets, limited beta |
| FSD v11 | 2023 | Unified stack (highway + city) |
| FSD v12 | 2024 | End-to-end neural network |
| FSD v13 | 2024-2025 | Enhanced end-to-end, photon-to-control |
| Robotaxi | 2025 | Unsupervised operation (Austin) |

## Hardware Generations

### Hardware 3 (HW3 / AI3)

| Specification | Value |
|--------------|-------|
| Release | 2019 |
| Neural Network Performance | 144 TOPS |
| Cameras | 8 cameras @ 1280×960 |
| Power Consumption | ~100W |
| Redundancy | Dual-chip design |
| Vehicles | 2019-2023 Model S/3/X/Y |

**Components:**
- 2× Tesla-designed FSD chips
- Samsung 14nm process
- 2GHz neural network accelerator
- 32MB SRAM per chip
- 2× video encoding units

### Hardware 4 (HW4 / AI4)

| Specification | Value |
|--------------|-------|
| Release | 2023 |
| Neural Network Performance | 500 TOPS |
| Cameras | 8 cameras @ 1280×960 (higher quality sensors) |
| Frame Rate | 36 Hz (vs 24 Hz HW3) |
| Power Consumption | ~150W |
| Vehicles | 2023+ Model S/3/X/Y, all Cybertruck |

**Improvements over HW3:**
- 3.5× compute increase
- Higher resolution camera sensors
- Improved HDR capability
- Better thermal management
- Redesigned camera placement

### Hardware 5 (HW5)

- **Expected:** 2025-2026
- **Performance:** 3,000+ TOPS (estimated)
- **Purpose:** Dedicated robotaxi/unsupervised FSD

## Neural Network Architecture

### FSD v12+ End-to-End Architecture

```
INPUT: Raw camera video (8 cameras)
            ↓
    ┌───────────────────┐
    │  Feature Extractor │ (RegNet / EfficientNet backbone)
    └───────────────────┘
            ↓
    ┌───────────────────┐
    │  Transformer Stack │ (Temporal context, attention)
    └───────────────────┘
            ↓
    ┌───────────────────┐
    │  Occupancy Network │ (3D scene understanding)
    └───────────────────┘
            ↓
    ┌───────────────────┐
    │   Planning Head    │ (Trajectory generation)
    └───────────────────┘
            ↓
OUTPUT: Vehicle controls (steering, acceleration, braking)
```

### Key Networks

#### 1. HydraNet (Multi-Task Learning)
- Single backbone, multiple task heads
- Object detection (vehicles, pedestrians, cyclists)
- Lane detection (vector representation)
- Traffic control (signs, signals)
- Depth estimation

#### 2. Occupancy Networks
- 3D volume prediction (not just 2D bounding boxes)
- Predicts occupied space in 3D grid
- Handles novel objects (no training required)
- Critical for collision avoidance

#### 3. Lane Graph Networks
- Vector-based lane representation
- Topology understanding (merges, splits, intersections)
- Navigation integration

#### 4. Path Planning Network
- Generates candidate trajectories
- Evaluates safety and comfort
- Selects optimal path

## Training Infrastructure

### Data Sources

| Source | Contribution | Scale |
|--------|--------------|-------|
| Tesla Fleet | Real-world driving data | 4M+ vehicles, billions of miles |
| Shadow Mode | Human intervention triggers | Millions of clips/month |
| Simulation | Edge case generation | Unlimited |
| Data Annotation | Human-labeled validation set | Hundreds of millions of labels |

### Training Compute

| Era | Compute | Hardware |
|-----|---------|----------|
| 2020-2022 | 10,000+ GPUs | NVIDIA A100 clusters |
| 2023-2024 | 30,000+ GPUs | NVIDIA H100 clusters |
| 2024+ | "Cortex" cluster | 5× increase, custom + NVIDIA |
| Future | Dojo | Tesla-designed AI training supercomputer |

### Dojo Supercomputer

| Specification | Value |
|--------------|-------|
| Purpose | Training AI for FSD and Optimus |
| Architecture | Custom Tesla D1 chips |
| Training Tiles | 25 D1 chips per tile |
| Cabinet | 120 tiles per ExaPOD |
| Performance | 1.1 EFLOPS per ExaPOD |
| Status | Partial deployment |

## FSD v13 Features (2025)

### Capabilities

| Feature | Status | Notes |
|---------|--------|-------|
| Highway driving | ✅ Production | Full autonomy with monitoring |
| City streets | ✅ Production | Complex intersections, traffic |
| Unprotected turns | ✅ Production | Left turns across traffic |
| Roundabouts | ✅ Production | Multi-lane handling |
| Parking | ✅ Production | Parallel, perpendicular |
| Parked-to-parked | ✅ FSD v13 | From parked space to destination |
| Reverse | ✅ FSD v13 | Backing up maneuvers |
| Construction zones | ⚠️ Beta | Variable performance |
| Weather conditions | ⚠️ Limited | Rain, snow handling |

### Performance Metrics

| Metric | FSD v12.5 | FSD v13 | Improvement |
|--------|-----------|---------|-------------|
| Miles per intervention | ~100 | ~500-1000 | 5-10× |
| Photon-to-control latency | Baseline | 2× faster | 50% reduction |
| Training data | Baseline | 4× scale | More diversity |
| Compute | Baseline | 5× (Cortex) | Better models |

### FSD (Supervised) vs FSD (Unsupervised)

| Aspect | Supervised | Unsupervised (Robotaxi) |
|--------|------------|-------------------------|
| Human monitoring | Required | None |
| Liability | Driver | Tesla |
| Geographic scope | All roads | Mapped/approved areas |
| Speed limits | Posted | Conservative |
| Availability | Consumer vehicles | Robotaxi fleet |
| Launch | Ongoing | Austin, June 2025 |

## Robotaxi (Cybercab)

### Vehicle Specifications

| Attribute | Specification |
|-----------|---------------|
| Name | Cybercab |
| Type | Purpose-built robotaxi |
| Seating | 2 passengers |
| Doors | Falcon wing |
| Steering wheel | None |
| Pedals | None |
| Charging | Inductive (wireless) |
| Range | 200+ miles |
| Cost per mile | Target $0.25 |

### Business Model

| Model | Description |
|-------|-------------|
| **Tesla Network** | Company-owned fleet |
| **Owner Fleet** | Private vehicles join network when idle |
| **Revenue Split** | Tesla takes percentage of fare |
| **Pricing** | Dynamic, based on demand |

### Launch Timeline

| Milestone | Date | Status |
|-----------|------|--------|
| FSD v13 wide release | Dec 2024 | ✅ Complete |
| Robotaxi unveil | Oct 2024 | ✅ Complete |
| Austin pilot | June 2025 | ✅ Launched |
| Additional cities | 2025-2026 | In progress |
| Full unsupervised | TBD | Pending regulatory |

## Safety Metrics

### Miles per Disengagement

| System | Miles/Intervention | Context |
|--------|-------------------|---------|
| Human baseline | ~500,000 | Average US driver |
| FSD v12.5 | ~100 | Supervised operation |
| FSD v13 | ~500-1000 | Supervised operation |
| Waymo | >1,000,000 | Geofenced robotaxi |

### Safety Comparison

| Metric | Human Driver | FSD v13 | Improvement |
|--------|--------------|---------|-------------|
| Accidents per mile | Baseline | 50% lower | 2× safer |
| Injury accidents | Baseline | 60% lower | 2.5× safer |
| Fatal accidents | Baseline | 70% lower | 3× safer |

*Note: Statistics based on Tesla-reported data; independent verification ongoing*

## Regulatory Status

### United States

| State | Status | Notes |
|-------|--------|-------|
| California | Testing permitted | Robotaxi permit pending |
| Texas | ✅ Robotaxi operational | Austin launched June 2025 |
| Arizona | Testing permitted | Waymo operational here |
| Florida | Testing permitted | Favorable regulations |
| Other states | Varies | Most allow supervised FSD |

### International

| Region | Status |
|--------|--------|
| Europe | Limited beta, regulatory barriers |
| China | Testing, data localization requirements |
| Canada | Supervised FSD available |

## Competitive Comparison

| System | Sensors | Approach | Status |
|--------|---------|----------|--------|
| **Tesla FSD** | Cameras only | End-to-end AI | Consumer beta, robotaxi launched |
| **Waymo** | LIDAR + cameras + radar | HD maps + rules | Robotaxi operational (geofenced) |
| **Cruise** | LIDAR + cameras + radar | HD maps + AI | Suspended after incidents |
| **Mercedes DRIVE PILOT** | LIDAR + cameras + radar | Highway only | Level 3 certified (Germany) |
| **Mobileye** | Cameras + radar | Modular AI | Various OEM integrations |

## Key Differentiators

### Tesla Advantages
1. **Fleet data:** 4M+ vehicles collecting real-world data
2. **Vision-only:** Scalable, no expensive sensors
3. **End-to-end AI:** Direct video-to-controls learning
4. **Vertical integration:** Hardware + software + vehicle
5. **OTA updates:** Continuous improvement post-purchase

### Tesla Challenges
1. **No LIDAR:** Some argue limits reliability
2. **Regulatory approval:** Slower in some jurisdictions
3. **Public perception:** High-profile incidents get attention
4. **Timeline history:** Past predictions often missed

---

*Last Updated: March 2026*
*Sources: Tesla AI Day presentations, Earnings calls, Technical papers*
