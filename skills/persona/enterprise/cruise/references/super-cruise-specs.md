# Super Cruise Technical Specifications

## Overview

Super Cruise is General Motors' hands-free advanced driver assistance system (ADAS). This document provides comprehensive technical specifications, capabilities, and comparison with Cruise's former robotaxi technology.

---

## System Specifications

### Core Capabilities

| Feature | Specification |
|---------|---------------|
| **SAE Automation Level** | Level 2 (Hands-off, Eyes-on) |
| **Hands-Free Operation** | Yes (on approved highways) |
| **Eyes-Off Operation** | No (driver attention required) |
| **Geographic Coverage** | 400,000+ miles of highways (North America) |
| **Maximum Speed** | Varies by vehicle (typically up to 85 mph) |
| **Lane Change** | Automatic (when properly equipped) |

### System Launch Timeline

| Year | Milestone |
|------|-----------|
| 2017 | Super Cruise launches on Cadillac CT6 |
| 2020 | Expansion to additional Cadillac models |
| 2022 | Ultra Cruise announced (enhanced capabilities) |
| 2023 | Available on 20+ GM vehicle models |
| 2024 | Cruise technology integration begins |
| 2028 | Eyes-off/hands-off system planned |

---

## Hardware Architecture

### Sensor Configuration

| Sensor Type | Quantity | Specification |
|-------------|----------|---------------|
| **Forward Camera** | 1 | Primary road monitoring |
| **Long-Range Radar** | 1 | Vehicle detection (150m+) |
| **Short-Range Radars** | 2 | Side/rear monitoring |
| **Driver Monitoring Camera** | 1 | Infrared, steering column mounted |
| **GPS Receiver** | 1 | High-precision |
| **IMU** | 1 | Inertial measurement |

### Comparison: Super Cruise vs. Cruise AV

| Component | Super Cruise (L2) | Cruise AV (L4) |
|-----------|-------------------|----------------|
| **LiDAR** | No (uses pre-mapped data) | Yes (multiple units) |
| **Cameras** | 1 forward + 1 driver | 10+ surround view |
| **Radar** | 3 units | 8+ units |
| **Compute** | Integrated | Dedicated AV computer |
| **Maps** | Pre-mapped highways | Real-time perception |
| **Redundancy** | Driver as fallback | System redundancy |

### HD Mapping

```
SUPER CRUISE MAPPING:

Source: LiDAR-mapped highways by GM
├── 400,000+ miles covered
├── 200,000+ miles in North America (initial)
├── Updated semi-annually
└── Includes:
    ├── Lane geometry
    ├── Curve data
    ├── Highway exits/entries
    ├── Merge zones
    └── Construction zones (static)

Usage:
├── Precise lane centering
├── Anticipatory speed adjustment
├── Curve negotiation
└── Geo-fencing activation
```

---

## Driver Monitoring System

### Camera Specifications

| Attribute | Specification |
|-----------|---------------|
| **Type** | Infrared (IR) camera |
| **Location** | Steering column, driver-facing |
| **Function** | Head position and eye tracking |
| **Operation** | Works with sunglasses, low light |
| **Privacy** | Images processed locally, not stored |

### Attention Detection

```
DRIVER ATTENTION MONITORING:

1. ATTENTION CONFIRMATION
   ├── Eyes on road detection
   ├── Head position tracking
   ├── Attention pattern analysis
   └── Confidence scoring

2. ESCALATION SEQUENCE
   ┌─────────────────────────────────────────────────────┐
   │ Level 1: Visual warning (light bar on steering)     │
   ├─────────────────────────────────────────────────────┤
   │ Level 2: Audible alert + haptic seat vibration      │
   ├─────────────────────────────────────────────────────┤
   │ Level 3: Voice command to take control              │
   ├─────────────────────────────────────────────────────┤
   │ Level 4: Super Cruise disengagement                 │
   ├─────────────────────────────────────────────────────┤
   │ Level 5: Gradual deceleration, hazard lights        │
   ├─────────────────────────────────────────────────────┤
   │ Level 6: Emergency stop, OnStar notification        │
   └─────────────────────────────────────────────────────┘

3. RE-ENGAGEMENT
   ├── Driver must manually reactivate
   ├── System checks attention before enabling
   └── Requires new highway section confirmation
```

---

## Operational Capabilities

### Hands-Free Driving Features

| Feature | Availability | Description |
|---------|--------------|-------------|
| **Lane Centering** | Standard | Maintains position within lane |
| **Adaptive Cruise** | Standard | Speed and following distance control |
| **Speed Limit Adaptation** | Standard | Adjusts to posted limits |
| **Automatic Lane Change** | Available | Initiates and completes lane changes |
| **Traffic Jam Assist** | Available | Low-speed following in congestion |

### Operating Conditions

| Condition | Support Level |
|-----------|---------------|
| **Divided Highways** | Full Super Cruise capability |
| **Non-Divided Highways** | Limited availability |
| **Urban Streets** | Not available (Geo-fenced) |
| **Construction Zones** | Disengagement recommended |
| **Adverse Weather** | System may limit or disengage |
| **Night Driving** | Full capability (with clear lane markings) |

### Lane Change Functionality

```
AUTOMATIC LANE CHANGE:

Trigger Methods:
├── Automatic: System-initiated to pass slower vehicle
└── Driver-Initiated: Tap turn signal

Process:
1. Driver activates turn signal (if manual)
2. System checks adjacent lane:
   ├── Clear of vehicles
   ├── Safe following distance
   └── No approaching traffic
3. System executes lane change:
   ├── Smooth steering input
   ├── Maintains speed
   └── Monitors completion
4. System resumes lane centering

Safety:
├── Driver can override at any time
├── System aborts if conditions change
└── Requires driver attention throughout
```

---

## Integration with Cruise Technology

### Post-December 2024 Enhancements

| Cruise Technology | Super Cruise Integration |
|-------------------|-------------------------|
| Perception algorithms | Enhanced object detection |
| Prediction models | Improved vehicle behavior forecasting |
| Simulation framework | Accelerated scenario testing |
| Safety validation | Enhanced testing protocols |
| 5M autonomous miles | Data-driven algorithm improvement |

### Technology Transfer Roadmap

```
CRUISE → SUPER CRUISE INTEGRATION:

2024-2025:
├── Perception algorithm improvements
├── Enhanced prediction capabilities
├── Simulation-based validation expansion
└── Safety culture integration

2025-2027:
├── Expanded operational domain
├── Improved edge case handling
├── Enhanced driver monitoring
└── City street capabilities (limited)

2027-2028:
├── Eyes-off highway system (Level 3)
├── Traffic jam chauffeur (Level 3)
└── Foundation for future Level 4 personal vehicles
```

---

## Business Model

### Subscription Pricing

| Component | Details |
|-----------|---------|
| **Initial Period** | 3 years included with vehicle purchase |
| **Renewal Options** | Annual or monthly subscription |
| **Estimated Price** | $25/month or $250/year (varies by model) |
| **Revenue Projection** | $2 billion annually by 2030 |

### Market Performance

| Metric | Value (2024) |
|--------|--------------|
| **Subscribers** | 360,000+ |
| **Monthly Active Users** | 60% of subscribers |
| **Miles Driven** | 10+ million per month |
| **Vehicle Models** | 23+ GM vehicles |
| **Customer Satisfaction** | 80% want on next vehicle |

---

## Safety Performance

### Safety Metrics

| Metric | Super Cruise Performance |
|--------|-------------------------|
| **Accident Rate** | Significantly lower than manual driving |
| **Disengagement Causes** | Primarily driver-initiated |
| **System Availability** | >95% on mapped highways |
| **Driver Attention** | Continuously monitored |

### Comparison with Competitors

| System | Level | Key Differentiator |
|--------|-------|-------------------|
| **Super Cruise** | L2 | HD maps, driver monitoring, hands-free |
| **Ford BlueCruise** | L2 | Hands-free, OTA updates |
| **Tesla Autopilot** | L2 | Vision-only (no LiDAR maps), frequent OTA |
| **Mercedes Drive Pilot** | L3 | Eyes-off (speed limited), first approved L3 in US |
| **BMW Highway Assistant** | L2 | Hands-free, eye monitoring |

---

## Future Roadmap

### Eyes-Off/Hands-Off System (2028)

| Attribute | Specification |
|-----------|---------------|
| **Target Launch** | 2028 |
| **Initial Vehicle** | Cadillac Escalade IQ |
| **Automation Level** | SAE Level 3 (conditional automation) |
| **Operating Domain** | Highways (expanded from current) |
| **Driver Role** | Eyes-off, available for takeover |
| **Sensors** | LiDAR, radar, cameras (enhanced from current) |

### Technical Requirements for L3

```
LEVEL 3 REQUIREMENTS:

1. ENHANCED PERCEPTION
   ├── LiDAR integration (from Cruise)
   ├── 360° monitoring
   ├── Higher accuracy classification
   └── Extended detection range

2. SYSTEM REDUNDANCY
   ├── Backup compute
   ├── Redundant sensors (critical functions)
   └── Fail-operational steering/braking

3. DRIVER STATE MONITORING
   ├── Enhanced availability detection
   ├── Takeover readiness assessment
   └── Minimum 10+ second takeover window

4. MINIMAL RISK CONDITION (MRC)
   ├── Safe stop capability
   ├── Hazard activation
   └── Emergency notification
```

---

## Regulatory Status

### Current Approvals

| Region | Status | Notes |
|--------|--------|-------|
| **United States** | Approved | All 50 states, L2 operation |
| **Canada** | Approved | Nationwide, L2 operation |
| **China** | Testing | Limited trials |
| **Europe** | Not available | Regulatory complexity |

### Level 3 Regulatory Path

| Step | Timeline | Action |
|------|----------|--------|
| 1 | 2024-2025 | Technical development |
| 2 | 2025-2026 | Certification preparation |
| 3 | 2026-2027 | Regulatory engagement |
| 4 | 2027-2028 | Limited deployment |
| 5 | 2028+ | Full rollout |

---

## Key Documents

| Resource | Location | Description |
|----------|----------|-------------|
| OnStar Super Cruise | onstar.com | Official consumer information |
| GM Investor Relations | gm.com | Business metrics and strategy |
| SAE J3016 | sae.org | Automation level definitions |
| NHTSA ADAS | nhtsa.gov | Safety guidelines |
