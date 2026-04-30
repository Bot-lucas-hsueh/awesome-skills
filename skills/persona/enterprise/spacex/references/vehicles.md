# SpaceX Vehicle Reference

## Falcon 9

### Overview
The Falcon 9 is the world's most flown orbital rocket with 500+ total missions and 167 flights in 2025 alone. It revolutionized space access through first-stage reusability.

### Specifications

| Parameter | Value |
|-----------|-------|
| Height | 70 m (229.6 ft) |
| Diameter | 3.7 m (12.1 ft) |
| Mass | 549,054 kg |
| Stages | 2 |
| First Flight | June 4, 2010 |
| Success Rate | ~99.4% |

### Performance

| Configuration | LEO Payload | GTO Payload |
|--------------|-------------|-------------|
| Expendable | 22,800 kg | 8,300 kg |
| Reusable | 17,500 kg | 5,500 kg |

### First Stage

| Feature | Specification |
|---------|--------------|
| Engines | 9 × Merlin 1D |
| Thrust (SL) | 7,607 kN (1.7M lbf) |
| Thrust (Vac) | 8,227 kN (1.85M lbf) |
| Burn Time | 162 seconds |
| Fuel | RP-1 / LOX |
| Landing | RTLS or ASDS |

### Reusability Records
- Most flights by single booster: 24 (B1067)
- Fastest turnaround: 13 days, 12 hours
- Target certification: 40+ flights per booster
- Cost reduction: ~50% for reused boosters

### Landing Options
1. **RTLS** (Return to Launch Site): Cape Canaveral or Vandenberg
2. **ASDS** (Autonomous Spaceport Drone Ship): "Of Course I Still Love You", "Just Read the Instructions", "A Shortfall of Gravitas"

---

## Falcon Heavy

### Overview
Falcon Heavy is the most powerful operational rocket, consisting of three Falcon 9 first stages. It can lift more than twice the payload of the next closest vehicle at one-third the cost.

### Specifications

| Parameter | Value |
|-----------|-------|
| Height | 70 m (229.6 ft) |
| Width | 12.2 m (39.9 ft) |
| Mass | 1,420,788 kg |
| Total Thrust | 22,819 kN (5.13M lbf) |
| First Flight | February 6, 2018 |

### Performance

| Destination | Payload |
|-------------|---------|
| LEO | 63,800 kg |
| GTO | 26,700 kg |
| Mars | 16,800 kg |
| Pluto | 3,500 kg |

### Configuration
- **Center Core**: Modified Falcon 9 first stage, reinforced structure
- **Side Boosters**: Standard Falcon 9 first stages
- **Second Stage**: Standard Falcon 9 second stage
- **Total Engines**: 27 Merlin 1D (9 per core)

### Notable Missions
- USSF-67 (national security)
- Viasat-3 (communications)
- Europa Clipper (NASA mission to Jupiter's moon)
- Psyche (asteroid mission)

---

## Starship

### Overview
Starship is a fully reusable super-heavy launch system designed for Mars colonization. It represents the next generation of SpaceX launch vehicles.

### Architecture

```
┌─────────────────────────────────────────────┐
│              STARSHIP SYSTEM                │
├─────────────────────────────────────────────┤
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │         STARSHIP (Upper Stage)      │   │
│  │  • 6 Raptor engines (3 SL, 3 Vac)   │   │
│  │  • 50m height, 9m diameter          │   │
│  │  • 1200 t propellant capacity       │   │
│  │  • Payload: 100-150 t to LEO        │   │
│  │  • Heat shield: 18,000 tiles        │   │
│  └─────────────────────────────────────┘   │
│                                             │
│  ┌─────────────────────────────────────┐   │
│  │     SUPER HEAVY (First Stage)       │   │
│  │  • 33 Raptor engines                │   │
│  │  • 71m height, 9m diameter          │   │
│  │  • 3,400 t propellant capacity      │   │
│  │  • Thrust: 7,590 t (16.7M lbf)      │   │
│  │  • Tower catch landing              │   │
│  └─────────────────────────────────────┘   │
│                                             │
└─────────────────────────────────────────────┘
```

### Super Heavy Booster

| Parameter | Value |
|-----------|-------|
| Height | 71 m |
| Diameter | 9 m |
| Engines | 33 × Raptor 2/3 |
| Thrust | 74,000 kN |
| Propellant | 3,400 tons CH4/LOX |
| Landing | Tower catch (Mechazilla arms) |

### Starship Upper Stage (Ship)

| Parameter | Value |
|-----------|-------|
| Height | 50 m |
| Diameter | 9 m |
| Engines | 3 × Raptor SL + 3 × Raptor Vacuum |
| Payload to LEO | 100-150 tons (reusable) |
| Payload to Mars | 100 tons |
| Heat Shield | TPS tiles, stainless steel backup |

### Variants

| Variant | Purpose | Key Features |
|---------|---------|--------------|
| Ship | Human/cargo transport | Life support, windows, payload bay |
| Tanker | On-orbit refueling | Maximum propellant load |
| Lunar Lander | Artemis HLS | No heat shield, landing legs |
| Depot | Propellant storage | Long-duration cryogenic storage |

### Development Status (2025-2026)
- Flight 7-11: Multiple successful tests in 2025
- Flight 12: Targeting April 2026 (Starship V3 debut)
- Tower catch achieved: October 2024 (booster)
- Booster re-flight: First reuse achieved May 2025
- Ship catch: Targeting 2026
- Orbital refueling: Development ongoing
- Target cadence: 25+ flights/year (2025), 100+/year (2026+)

---

## Dragon Spacecraft

### Crew Dragon

| Parameter | Value |
|-----------|-------|
| Crew Capacity | 4-7 astronauts |
| Pressurized Volume | 9.3 m³ |
| Diameter | 3.7 m |
| Height | 8.1 m |
| Launch Vehicle | Falcon 9 |
| Heat Shield | PICA-X (reusable) |

#### SuperDraco Engines
- 16 engines for launch escape
- 71 kN thrust each
- Propellant: MMH/NTO
- Redundant propulsion for abort

#### Flight History
- Demo-1: March 2019 (uncrewed ISS docking)
- Demo-2: May 2020 (first crewed flight, Behnken & Hurley)
- Crew-1 through Crew-12: Operational ISS rotations
- Axiom missions: Private astronaut flights
- Polaris Dawn: First commercial spacewalk (2024)

### Cargo Dragon

| Parameter | Value |
|-----------|-------|
| Pressurized Cargo | 6,000 kg up, 3,000 kg down |
| Unpressurized | External trunk |
| Berthing | ISS nadir port |
| Recovery | Splashdown |

### Dragon Fleet Status (2025)
| Vehicle | Flights | Status |
|---------|---------|--------|
| Endeavour (C206) | 5 | Active |
| Resilience (C207) | 4 | Active |
| Endurance (C210) | 4 | Active |
| Freedom (C212) | 4 | Active |
| C213 | 0 | Final vehicle, entered service 2025 |

---

## Vehicle Comparison

| Metric | Falcon 9 | Falcon Heavy | Starship |
|--------|----------|--------------|----------|
| Height | 70m | 70m | 121m |
| Mass | 549t | 1,421t | 5,000t |
| Thrust | 7,607kN | 22,819kN | 74,000kN |
| LEO Payload | 22.8t | 63.8t | 100-150t |
| Reusable | First stage | Side boosters | Full stack |
| Cost/launch | $62M | $90-150M | Target: <$10M |
| First flight | 2010 | 2018 | 2023 (test) |

---

**Document Version**: 1.1  
**Last Updated**: 2026-03-21
