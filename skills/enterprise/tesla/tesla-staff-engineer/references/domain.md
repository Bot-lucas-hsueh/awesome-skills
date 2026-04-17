## § 2 — Domain Knowledge

### § 2.1 Tesla Company Deep Dive (2025)

#### Financial & Operational Metrics

| Metric | 2024 Value | 2025 Value | Trend | Notes |
|--------|------------|------------|-------|-------|
| Annual Revenue | $97.69B | $94.83B | -2.93% | First YoY decline since 2009 |
| Net Income | $7.09B | TBD | Stabilizing | Post-2023 tax benefit normalization |
| R&D Investment | $4.54B | ~$5B+ | Growing | AI, FSD, battery, manufacturing |
| Global Employees | 125,665 | 125,000+ | Stable | Austin grew 86% in 2023 to 22,777 |
| Vehicle Deliveries | 1.79M | ~1.8M+ | Recovering | 2024 decline, 2025 recovery expected |
| Vehicle Production | 1.77M | TBD | Growing | Fremont, Shanghai, Berlin, Texas |
| Energy Storage | 31.4 GWh | 40+ GWh | +67% YoY | Fastest growing segment |
| Supercharger Stations | 7,000+ | 7,500+ | Expanding | 55,000+ connectors globally |
| 4680 Cell Production | 100M+ | 150M+ | Ramping | Dry electrode breakthrough Q4 2025 |

#### Product Portfolio

| Product | Status | Key Specs | Mission Contribution |
|---------|--------|-----------|---------------------|
| **Model 3** | Production | 272-333 mi range, $38,990+ | Mass-market EV adoption |
| **Model Y** | Production (Juniper refresh 2025) | 310-330 mi range, #1 selling car globally | Scale EV adoption |
| **Model S** | Production (2025 limited) | 405 mi range, luxury sedan | Technology flagship |
| **Model X** | Production (2025 limited) | 348 mi range, falcon doors | Premium SUV |
| **Cybertruck** | Production | 340+ mi range, bulletproof exoskeleton | Truck market electrification |
| **Tesla Semi** | Pilot production | 500 mi range, Class 8 truck | Freight electrification |
| **Cybercab (Robotaxi)** | Austin launch 2025 | Purpose-built autonomous vehicle | Autonomous transport |
| **Affordable Model** | Development | Target <$30,000 | Mass-market breakthrough |

### § 2.2 First Principles Decision Tree

```
START: Problem or "industry standard" approach presented
│
├─→ Q1: Does this accelerate sustainable energy transition? [No → Challenge requirement]
│
├─→ Q2: Solved physics problem? [Yes → Use known solution, don't reinvent]
│
├─→ Q3: Deconstruct to material/energy/labor costs? [Yes → Build bottom-up cost model]
│   ├─ ❌ BAD: "Battery costs $130/kWh because that's market rate"
│   └─ ✅ GOOD: "Li: $15/kg, Ni: $18/kg, Co: $33/kg → $80/kWh floor + $15/kWh mfg = $95/kWh"
│
├─→ Q4: Tradition vs physics? [Target: >80% physics-based decisions]
│   ├─ ❌ BAD: "Use 18650 because that's standard"
│   └─ ✅ GOOD: "4680 gives 5× energy via tabless design; reduces parts from 4,400 to 828"
│
├─→ Q5: Within 10× of theoretical physics limit? [Target: 10× or closer]
│   ├─ Li-ion theoretical: 400 Wh/kg | Current: 250 Wh/kg = 62.5% → Within 2× ✅
│   └─ If >100× from limit: Question fundamental approach
│
└─→ OUTPUT: Physics-grounded solution with validated cost model
```

### § 2.3 Five-Step Algorithm Flowchart

| Step | Action | Go Criteria | No-Go Criteria | Tesla Example |
|------|--------|-------------|----------------|---------------|
| **1. Question** | Attach name; ask Why 5× | ≥70% requirements have named owner | >30% "standard/best practice" | Why modules? → Tradition, not physics |
| **2. Delete** | Remove 30-50% scope | ≥30% deleted | <10% deleted | Remove modules, tabs, wiring |
| **3. Simplify** | Optimize what's left | Parts count -50% or unified | Adding complexity to compensate | Structural pack = pack + body |
| **4. Accelerate** | Parallelize, compress time | Cycle time -50% | Speeding up complex process | 10 months vs 3 years development |
| **5. Automate** | Automate LAST | Cpk >1.33 manual process | Automating unstable process | 4680 lines: manual → automated ramp |

### § 2.4 Battery Technology: 4680 Deep Dive

#### 4680 vs 2170 Comparison

| Attribute | 2170 (Legacy) | 4680 (Tesla) | Improvement |
|-----------|---------------|--------------|-------------|
| Dimensions | 21mm × 70mm | 46mm × 80mm | 5.5× volume |
| Energy Capacity | ~18 Wh | ~98 Wh | 5.4× per cell |
| Cells per Pack | 4,416 | 828 | 81% fewer |
| Power Output | Baseline | 6× improvement | Tabless electrode |
| Manufacturing | Wet coating | Dry coating (Maxwell) | 10× reduction in equipment footprint |
| Cost Target | $120-130/kWh | <$80/kWh | 35%+ reduction |
| Dry Electrode | No | Yes (Q4 2025 breakthrough) | Solvent-free, 7-10× faster production |

#### Cell-to-Vehicle Structural Integration

```
TRADITIONAL PACK ARCHITECTURE:
Cells → Modules → Pack → Vehicle Structure
[4,400 cells] → [Modules with wiring/cooling] → [Structural enclosure] → [Bolted to chassis]
Parts: ~1,700 | Weight: ~480kg | Energy: 75kWh

TESLA STRUCTURAL PACK (4680):
Cells → Structural Pack → Vehicle
[828 cells] → [Pack IS floor structure] → [Integrated]
Parts: ~370 | Weight: ~420kg | Energy: 67-82kWh

BENEFITS:
- 370 vs 1,700 parts (78% reduction)
- Stiffer vehicle structure (torsion)
- Manufacturing: 10 steps → 3 steps
- Service: Replace module? No, entire pack (cost tradeoff)
```

### § 2.5 FSD (Full Self-Driving) Architecture

#### FSD v13 Technical Specifications

| Feature | Specification |
|---------|---------------|
| Hardware | AI4 (HW4) — 500 TOPS |
| Camera Input | 8 cameras × 1280×960 @ 36fps (AI4 native resolution) |
| Processing Rate | 36 Hz video input |
| Training Data | 4× scaling vs FSD 12 |
| Latency | 2× lower photon-to-control latency |
| Training Compute | Cortex cluster — 5× increase |
| Key Capabilities | Parked-to-parked, reverse, unprotected turns |

#### Neural Network Architecture (HydraNet)

```
HYDRANET (Multi-Task Learning):
Input: 8 cameras × 1280×960 @ 36fps
      ↓
Shared Backbone: RegNet/BiFPN feature extraction
      ↓
Task Heads:
├── Object detection (vehicles, pedestrians, cyclists)
├── Lane detection (vector representation)
├── Depth estimation (pseudo-LIDAR from stereo)
├── Traffic control (signs, signals)
├── Path planning (trajectory prediction)
└── Occupancy networks (3D volume, not 2D boxes)

KEY INNOVATIONS:
- End-to-end neural network (raw video → driving actions)
- Single network, multiple tasks (efficiency)
- Video architecture (temporal context)
- Occupancy networks (3D volume prediction)
- Fleet data: 4M+ vehicles providing training data
```

#### Robotaxi (Cybercab) Specifications

| Attribute | Specification |
|-----------|---------------|
| Launch | Austin, June 2025 |
| Operation | Unsupervised (no human driver) |
| Vehicle | Purpose-built, no steering wheel/pedals |
| Range | 200 miles (projected) |
| Charging | Inductive (wireless) |
| Cost Target | $0.25/mile (vs $2-3/mile human rideshare) |

### § 2.6 Optimus Humanoid Robot

#### Optimus Generations

| Generation | Timeline | Key Features | Status |
|------------|----------|--------------|--------|
| **Gen 1** | 2022 (AI Day) | Walking prototype, proof of concept | Historical |
| **Gen 2** | 2023-2024 | 10kg lighter, 30% faster, 11-DoF hands | Factory deployment |
| **Gen 2.5** | 2025 | Improved mobility, task learning | Current production |
| **Gen 3** | 2026 | Mass production design, 25-DoF hands | Development |

#### Optimus Technical Specs

| Specification | Value |
|---------------|-------|
| Height | 5'11" (1.7m) |
| Weight | 160 lbs (73 kg) |
| Battery | 2.3 kWh |
| Power (rest) | 100W |
| Power (active) | 500W |
| DoF (Gen 2) | 40+ (11 per hand) |
| DoF (Gen 3 hands) | 50 total (25 per hand) |
| Target Price | $20,000-30,000 |
| 2025 Target | 5,000 units (internal use) |
| 2026 Target | 50,000 units |
| Long-term Target | 1M units/year |

### § 2.7 Supercharger Network & NACS

#### Supercharger Network (2025)

| Metric | Value |
|--------|-------|
| Stations | 7,000+ |
| Connectors | 55,000+ |
| V4 Superchargers | Rolling out (350kW capability) |
| 500kW Charging | Cybertruck only (800V architecture) |
| NACS Adopters | All major OEMs (Ford, GM, Rivian, BMW, Mercedes, Hyundai, etc.) |

#### NACS Adoption Timeline

| Brand | Adapter Available | Native NACS |
|-------|-------------------|-------------|
| Ford | 2024 | 2025 |
| GM | 2024 | 2025 |
| Rivian | 2024 | 2025 |
| BMW | 2025 | 2025 |
| Mercedes | 2024 | 2025 |
| Hyundai/Kia | 2025 | 2025 |
| Stellantis | 2026 | 2027 |

### § 2.8 Energy Products

#### Energy Ecosystem

```
┌─────────────────────────────────────────────────────────────┐
│                    TESLA ENERGY ECOSYSTEM                    │
│                                                              │
│  GENERATION          STORAGE              CONSUMPTION       │
│  ───────────         ────────             ───────────       │
│                                                              │
│  Solar Roof    ───►  Powerwall    ───►   Residential       │
│  Solar Panels        Megapack            Commercial         │
│                                            Industrial       │
│                                                              │
│  VEHICLE INTEGRATION:                                        │
│  - Vehicle-to-Home (V2H): Car powers house during outage    │
│  - Vehicle-to-Grid (V2G): Car sells power back to grid      │
│                                                              │
│  SOFTWARE INTEGRATION:                                       │
│  - Tesla App controls all energy products                    │
│  - Autobidder: AI trades energy for maximum value           │
│  - Storm Watch: Auto-prepare for weather events             │
└─────────────────────────────────────────────────────────────┘
```

#### Energy Deployment (2024)

| Product | Deployment | Growth |
|---------|------------|--------|
| Megapack (utility) | 25+ GWh | 67% YoY |
| Powerwall (residential) | 500K+ installed | Growing |
| Solar Roof | Production ramping | Steady |
| Solar Panels | Selective deployment | Stable |

### § 2.9 Gigafactory Network

| Facility | Location | Primary Output | Capacity/Status |
|----------|----------|----------------|-----------------|
| **Gigafactory Nevada** | Sparks, NV | 4680 cells, Semi | 100 GWh 4680 expansion underway |
| **Gigafactory Shanghai** | Shanghai, China | Model 3/Y | >750K vehicles/year |
| **Gigafactory Berlin** | Brandenburg, DE | Model Y | 375K+/year, 500K milestone March 2025 |
| **Gigafactory Texas** | Austin, TX | Model Y, Cybertruck, 4680 | 250K+/year, 4K/week peak |
| **Megafactory Shanghai** | Shanghai, China | Megapack | 10K units/year, 40 GWh |
| **Megafactory Lathrop** | California, USA | Megapack | Operational |

---
