## § 2 — Domain Knowledge

### 2.1 Waymo Company Deep Dive

#### 2.1.1 Corporate & Financial Metrics (2025-2026)

| Metric | Value | Context |
|--------|-------|---------|
| Valuation | $126 billion | Feb 2026 post-money (up from $45B in 2024) |
| Total Funding | $16 billion+ | Series led by Dragoneer, DST Global, Sequoia |
| Parent Investment | Alphabet majority owner | Google contributed ~$13B of latest round |
| Annual Revenue | Est. $1-5B | Rapidly scaling with ride volume |
| Employees | ~2,500-5,000 | Engineering-heavy organization |
| Co-CEOs | Tekedra Mawakana & Dmitri Dolgov | Since April 2021 |

#### 2.1.2 Waymo One Robotaxi Operations

| City | Status | Launch Date | Notes |
|------|--------|-------------|-------|
| **Phoenix, AZ** | ✅ Full commercial | Oct 2020 | First city, 500+ vehicles |
| **San Francisco** | ✅ Full commercial | June 2024 | Dense urban environment |
| **Los Angeles** | ✅ Full commercial | Nov 2024 | 700 vehicles |
| **Austin, TX** | ✅ Full commercial | Mar 2025 | Via Uber partnership |
| **Atlanta, GA** | ✅ Full commercial | June 2025 | Via Uber partnership |
| **Miami, FL** | 🟡 Waitlist service | Jan 2026 | Fleet partner: Moove |

**Planned 2026 Expansions:** Washington D.C., Detroit, Las Vegas, San Diego, Denver, Dallas, Houston, San Antonio, Orlando, Nashville, London (first international), Tokyo (testing)

#### 2.1.3 Fleet & Operational Metrics

| Metric | 2025 Value | Growth |
|--------|------------|--------|
| Total Fleet | 2,500+ vehicles | Up from 1,500 (Apr 2025) |
| Weekly Paid Rides | 400,000+ | Target: 1M/week by end 2026 |
| Rider-Only Miles | 170M+ (Dec 2025) | 467,000 miles/day average |
| Cumulative Trips | 20M+ | 15M in 2025 alone (3× 2024) |
| Passenger Hours | 3.8M+ cumulative | Exponential growth curve |

### 2.2 Waymo Driver Technology Stack

#### 2.2.1 Sixth-Generation Waymo Driver (2024-2026)

```
SENSOR SUITE (42% reduction vs 5th gen, improved performance):
├── 13 cameras (down from 29) — 17MP high-res, 500m range
├── 4 LiDARs (down from 5) — 360° coverage, custom-designed
├── 6 radar units — all-weather detection, velocity measurement
└── External audio receivers (EARs) — emergency vehicle detection

COMPUTE & SOFTWARE:
├── Custom silicon — Google TPUs for ML inference
├── Sensor fusion engine — multi-modal perception
├── Motion planner — trajectory optimization
├── HD maps — centimeter-accurate, constantly updated
└── Simulation platform — billions of virtual miles

VEHICLE PLATFORMS:
├── Jaguar I-PACE (current fleet backbone)
├── Zeekr RT / "Ojai" (purpose-built robotaxi with Geely)
├── Hyundai IONIQ 5 (50,000 unit order, largest in AV history)
└── Toyota partnership (consumer vehicles)

COST TARGET: <$20,000 per Waymo Driver (hardware only)
```

#### 2.2.2 Safety Performance Data

| Safety Metric | Waymo vs Human | Statistical Significance |
|---------------|----------------|------------------------|
| Serious injury crashes | **92% fewer** | Based on 170M miles |
| Crashes with airbag deployment | **83% fewer** | NHTSA SGO data |
| Any injury crashes | **82% fewer** | Peer-reviewed study |
| Pedestrian injury crashes | **92% fewer** | Traffic Injury Prevention journal |
| Cyclist injury crashes | **85% fewer** | Waymo Safety Impact Hub |
| Motorcycle injury crashes | **81% fewer** | Comprehensive analysis |
| Intersection injury crashes | **96% fewer** | Vulnerable road user focus |

### 2.3 Sensor Fusion Architecture

```
PERCEPTION HIERARCHY:

Level 1 — Raw Sensing
├── LiDAR: 3D point clouds, precise depth, works in darkness
├── Cameras: Color, texture, semantic understanding (signs, signals)
└── Radar: Velocity measurement, all-weather penetration

Level 2 — Object Detection & Tracking
├── Static objects (barriers, parked vehicles)
├── Dynamic objects (vehicles, pedestrians, cyclists)
├── Vulnerable road users (priority detection)
└── Road infrastructure (lanes, signs, signals)

Level 3 — Prediction & Planning
├── Intent prediction (what will others do?)
├── Trajectory forecasting (where will they be?)
├── Motion planning (safe, efficient path)
└── Fallback planning (what if something fails?)

Level 4 — Control & Execution
├── Steering commands
├── Throttle/braking
├── Turn signals, horn, lights
└── Emergency stop capability
```

### 2.4 Regulatory & Insurance Framework

#### 2.4.1 Key Partnerships

| Partner | Relationship | Purpose |
|---------|--------------|---------|
| **Uber** | Commercial partner | Waymo One rides in Austin, Atlanta via Uber app |
| **Lyft** | Fleet management | Nashville operations |
| **Moove** | Fleet operations | Phoenix, Austin, Atlanta, Miami, London |
| **Avis** | Fleet services | Dallas and future cities |
| **Munich Re** | Insurance underwriting | Passenger trip coverage via Trov |
| **Trov** | Insurance platform | On-demand passenger protection |
| **Hyundai** | OEM partner | 50,000 IONIQ 5 vehicle supply |
| **Geely/Zeekr** | OEM partner | Purpose-built robotaxi platform |
| **Toyota** | OEM partner | Consumer AV deployment |

#### 2.4.2 Insurance Model

- **Passenger Coverage:** Trip-based insurance automatically included
- **Underwriter:** Munich Re (world's largest reinsurer)
- **Coverage:** Lost property, trip interruption, medical expenses
- **Model:** Software-triggered, mile-by-mile coverage
- **History:** First AV passenger insurance (2017 partnership)

---
