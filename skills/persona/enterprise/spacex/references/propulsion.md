# SpaceX Propulsion Systems Reference

## Raptor Engine

### Overview
The Raptor engine is the first full-flow staged combustion engine to fly. It uses methane and liquid oxygen (methalox) propellant, chosen for Mars ISRU compatibility.

### Full-Flow Staged Combustion Cycle

```
┌─────────────────────────────────────────────────────────────────┐
│              FULL-FLOW STAGED COMBUSTION CYCLE                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   LOX Tank ────────┐                                            │
│                    ↓                                            │
│   CH4 Tank ────────┼──→ ┌─────────────────┐                     │
│                      ┌→ │  OXYGEN-RICH    │                     │
│                      │  │   PREBURNER     │──→ Turbopump ─→     │
│                      │  │   (hot O2 gas)  │    (drives LOX)     │
│                      │  └─────────────────┘                     │
│                      │                                          │
│                      │  ┌─────────────────┐                     │
│                      └──│   FUEL-RICH     │                     │
│                         │   PREBURNER     │──→ Turbopump ─→     │
│                         │  (hot CH4 gas)  │    (drives CH4)     │
│                         └─────────────────┘                     │
│                                    ↓                            │
│                           ┌─────────────────┐                   │
│                           │ MAIN COMBUSTION │                   │
│                           │    CHAMBER      │──→ Nozzle         │
│                           │   (300+ bar)    │                   │
│                           └─────────────────┘                   │
│                                                                 │
│   Key: ALL propellant flows through preburners (full-flow)      │
│        No gas dumped (closed cycle)                             │
└─────────────────────────────────────────────────────────────────┘
```

### Advantages Over Other Cycles

| Cycle | Efficiency | Complexity | Raptor Advantage |
|-------|------------|------------|------------------|
| Gas Generator (Merlin) | Lower (open cycle) | Simple | 15% more efficient |
| Staged Combustion (RD-180) | Medium | Moderate | Full flow = higher pressure |
| Full-Flow Staged (Raptor) | Highest | Complex | 300+ bar chamber pressure |

### Raptor Versions

#### Raptor 1 (2019-2021)
| Parameter | Value |
|-----------|-------|
| Sea Level Thrust | 185 tons (1,816 kN) |
| Vacuum Thrust | 200 tons (1,961 kN) |
| Chamber Pressure | 250 bar |
| Isp (SL) | 330s |
| Isp (Vac) | 355s |
| Status | Retired |

#### Raptor 2 (2021-present)
| Parameter | Value |
|-----------|-------|
| Sea Level Thrust | 230+ tons (2,255 kN) |
| Vacuum Thrust | 258 tons (2,530 kN) |
| Chamber Pressure | 300 bar |
| Isp (SL) | 327s |
| Isp (Vac) | 350s |
| Mass | ~1,600 kg |
| Status | Operational |

Key improvements over Raptor 1:
- Eliminated external heat shield
- Reduced parts count significantly
- Simplified plumbing with more welding
- Integrated electronics

#### Raptor 3 (2025)
| Parameter | Value |
|-----------|-------|
| Sea Level Thrust | 280 tons (2,746 kN) |
| Chamber Pressure | 350 bar |
| Mass | ~1,525 kg (lighter than R2) |
| Status | Testing/production |

Key improvements:
- Further parts count reduction via additive manufacturing
- Integrated chill lines
- Even cleaner external appearance
- Target: 1,000+ flights per engine

### Technical Specifications

| Feature | Specification |
|---------|---------------|
| Propellants | Liquid Methane / Liquid Oxygen |
| Mixture Ratio (O/F) | 3.6:1 |
| Throat Diameter | ~220 mm |
| Exit Diameter | 1.3 m (SL variant) |
| Area Ratio | 40:1 (SL), 90:1 (Vac) |
| Cooling | Regenerative (CH4 through channels) |
| Ignition | Torch igniters (methane/oxygen) |
| Gimbal Range | ±15° (inner engines) |

### Manufacturing

**Key Technologies:**
- **3D Printing**: Turbopump housings, injectors
- **Friction Stir Welding**: Chamber, nozzle jacket
- **Automated CNC**: Complex valve bodies
- **Vertical Integration**: 95%+ parts made in-house

**Production Rate Target:**
- Current: ~500 engines/year
- Target (Raptor 3): 1,000+ engines/year
- McGregor, TX test facility capacity expansion ongoing

---

## Merlin Engine

### Overview
The Merlin engine powers Falcon 9 and Falcon Heavy. It's a gas-generator cycle engine using RP-1 (refined kerosene) and liquid oxygen.

### Merlin 1D Specifications

| Parameter | Sea Level | Vacuum |
|-----------|-----------|--------|
| Thrust | 845 kN | 914 kN |
| Isp | 282s | 311s |
| Chamber Pressure | ~97 bar | ~97 bar |
| Mass | ~470 kg | ~490 kg |
| TWR | ~180:1 | ~190:1 |

### Design Features
- **Pintle Injector**: Simple, reliable, enables deep throttling
- **Ablative Cooling**: Nozzle extension (Vacuum variant)
- **Gas Generator Cycle**: ~3% of propellant drives turbopump
- **Restart Capability**: Up to 4 restarts (second stage)

### Versions

| Version | Thrust | Usage |
|---------|--------|-------|
| Merlin 1A | 340 kN | Falcon 1 (early) |
| Merlin 1C | 420 kN | Falcon 1/9 v1.0 |
| Merlin 1D | 845 kN | Falcon 9 v1.1+ |
| Merlin 1D+ | 914 kN | Current production |
| Merlin 1D Vac | 934 kN | Second stage |

### Deep Throttling
- Can throttle to ~40% of max thrust
- Enables controlled descent for landing
- Throttle bucket for max dynamic pressure (Max-Q)

---

## SuperDraco Engine

### Overview
SuperDracos provide launch escape capability for Crew Dragon and precision landing control.

### Specifications

| Parameter | Value |
|-----------|-------|
| Thrust (each) | 71 kN (16,000 lbf) |
| Propellant | MMH / NTO (hypergolic) |
| Isp | 235s |
| Number per Dragon | 16 (4 pods × 4 engines) |
| Response Time | <100 ms |

### Functions
1. **Launch Escape**: Pull crew away from failing rocket
2. **Landing Propulsion**: Propulsive landing (designed, not currently used)
3. **Orbital Maneuvering**: Backup to Draco thrusters

---

## Draco Thrusters

### Overview
Draco thrusters provide attitude control and orbital maneuvering for Dragon spacecraft.

### Specifications

| Parameter | Value |
|-----------|-------|
| Thrust (each) | 400 N (90 lbf) |
| Propellant | MMH / NTO |
| Isp | 300s |
| Number per Dragon | 18 |

### Functions
- Attitude control (pitch, yaw, roll)
- Small orbital adjustments
- Rendezvous and docking
- Deorbit burn

---

## Kestrel Engine (Retired)

### Historical Note
The Kestrel powered the Falcon 1 second stage. It was a pressure-fed engine using RP-1/LOX.

| Parameter | Value |
|-----------|-------|
| Thrust | 31 kN |
| Isp | 317s |
| Used on | Falcon 1 (2006-2009) |

---

## Propulsion Comparison

| Engine | Vehicle | Cycle | Propellant | Thrust | Isp (Vac) |
|--------|---------|-------|------------|--------|-----------|
| Raptor 3 | Starship | Full-flow staged | CH4/LOX | 2,746 kN | 380s |
| Raptor 2 | Starship | Full-flow staged | CH4/LOX | 2,255 kN | 350s |
| Merlin 1D Vac | Falcon 9 | Gas generator | RP-1/LOX | 934 kN | 311s |
| Merlin 1D | Falcon 9 | Gas generator | RP-1/LOX | 845 kN | 282s |
| SuperDraco | Dragon | Pressure-fed | MMH/NTO | 71 kN | 235s |
| Draco | Dragon | Pressure-fed | MMH/NTO | 400 N | 300s |

---

## Fuel Choices Rationale

### Why Methane for Raptor/Starship?

| Factor | Methane | RP-1 | Hydrogen |
|--------|---------|------|----------|
| Density | Good | Better | Poor |
| Isp | Good | Good | Best |
| Coking/Soot | No | Yes | No |
| Mars ISRU | Yes (CO2 + H2O) | No | Possible |
| Storage | Easy | Easy | Cryogenic (-253°C) |
| Cost | Low | Low | High |

**Decision**: Methane offers the best balance for Mars missions while avoiding RP-1's coking issues in reusable engines.

---

**Document Version**: 1.1  
**Last Updated**: 2026-03-21
