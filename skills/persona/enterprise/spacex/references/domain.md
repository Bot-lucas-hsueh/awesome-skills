## §2 · Domain Knowledge

### §2.1 Launch Vehicles

**Falcon 9 (Workhorse)**
- **Stats**: 500+ total launches, 167 in 2025 alone, 99.4% success rate
- **Reusability**: First stage lands on drone ship or RTLS, boosters flown 32+ times (record)
- **Cost**: $62M per launch (vs ULA $400M+ for equivalent performance)
- **Performance**: 22,800 kg to LEO (expendable), 17,500 kg (reusable)
- **Merlin Engines**: 9x sea-level on first stage, 1x vacuum on second stage
  - Merlin 1D: 845 kN SL thrust, 311s Isp vacuum
  - Gas generator cycle, RP-1/LOX

**Falcon Heavy (Heavy Lift)**
- **Configuration**: 3 Falcon 9 cores (27 engines total)
- **Performance**: 63,800 kg to LEO, 26,700 kg to GTO
- **Operations**: Side boosters RTLS, center core expended or droneship landing
- **Notable Missions**: USSF-67, Viasat-3, Psyche asteroid mission

**Starship (Next Generation)**
- **Architecture**: Fully reusable super-heavy system
- **Super Heavy Booster**: 33 Raptor engines, 7,590 tons thrust (2x Saturn V)
- **Ship**: 6 Raptor engines (3 SL, 3 vacuum), 150 ton LEO payload goal
- **Current Status**: Tower-catch achieved Oct 2024, booster re-flight May 2025, 5 suborbital tests in 2025
- **Goals**: $10/kg to orbit, Mars cargo missions by 2026, human missions by 2028-2031

### §2.2 Propulsion Systems

**Raptor Engine (Flagship)**
- **Cycle**: Full-flow staged combustion (first ever flown)
- **Propellant**: Liquid methane / liquid oxygen (methalox)
- **Versions**:
  | Version | Thrust (SL) | Chamber Pressure | Status |
  |---------|-------------|------------------|--------|
  | Raptor 1 | 185 tons | 250 bar | Retired |
  | Raptor 2 | 230+ tons | 300 bar | Operational |
  | Raptor 3 | 280 tons | 350 bar | Testing (2025) |
- **Isp**: 330s (SL), 380s (vacuum)
- **Design Life**: Target 1,000+ flights per engine
- **Manufacturing**: Simplified plumbing, 3D-printed components

**Advantages of Full-Flow Staged Combustion:**
- All propellant flows through preburners (max efficiency)
- Separate fuel-rich and oxygen-rich turbines
- Cooler turbine temperatures → longer life
- No interpropellant seals needed

**Merlin Engine (Falcon)**
- **Cycle**: Gas generator (open cycle)
- **Propellant**: RP-1 (kerosene) / LOX
- **Thrust**: 845 kN sea level, 914 kN vacuum
- **Isp**: 282s (SL), 311s (vacuum)
- **Mass**: 470 kg (thrust-to-weight: 180:1, best in class)

### §2.3 Spacecraft Systems

**Crew Dragon**
- **Capacity**: 4-7 astronauts
- **Launch Vehicle**: Falcon 9
- **Missions**: ISS crew rotation (Crew-1 through Crew-12), Axiom private missions
- **Firsts**: First private spacecraft to carry humans to ISS (Demo-2, May 2020)
- **Reusability**: Certified for 5 flights, targeting 15 with NASA approval
- **Abort System**: SuperDraco thrusters (16 engines), launch escape capability
- **Splashdown**: Parachute-assisted ocean landing

**Cargo Dragon**
- **Mission**: ISS resupply (CRS program)
- **Capacity**: 6,000 kg pressurized, external trunk for unpressurized
- **Return**: 3,000 kg cargo return capability

**Dragon 2 Improvements:**
- Touchscreen controls (with physical backup)
- Modern life support architecture
- Autonomous docking capability
- Reusable heat shield (PICA-X)

### §2.4 Satellite Constellations

**Starlink Architecture**
- **Constellation Size**: ~11,500 satellites launched, ~9,900 active (early 2026)
- **Orbital Planes**: 550 km altitude, 53° inclination (primary shell)
- **Generations**:
  | Gen | Mass | Capability | Launcher |
  |-----|------|------------|----------|
  | V1 | 260 kg | Baseline | Falcon 9 |
  | V1.5 | 307 kg | Laser links | Falcon 9 |
  | V2 Mini | 730 kg | Larger array | Falcon 9 |
  | V2 | 1,250 kg | Full capability | Starship |
  | V3 | 1,500 kg | Next-gen | Starship |

**Starlink Performance (2025-2026):**
- Subscribers: 9+ million globally (9.2M end of 2025)
- Revenue: $10.4B in 2025 (69% of SpaceX total revenue)
- Coverage: 155+ countries
- Speed: Up to 215 Mbps (residential)
- Latency: 20-40 ms
- Direct-to-Cell: Text messaging operational, voice/data planned

**Starshield (Government Variant)**
- Encrypted communications
- Hosted payloads for DoD/NRO
- Inter-satellite laser links
- Proliferated Space Architecture participant

### §2.5 Mars Architecture

**Strategic Goals:**
1. Establish self-sustaining civilization on Mars
2. Reduce cost-per-ton to Mars by 10,000x
3. Create backup for humanity

**Technical Pillars:**
- **Full Reusability**: Both stages return and refly
- **Orbital Refueling**: Tanker variant fills ship in LEO
- **ISRU**: Produce methane/LOX from Martian CO2 and water ice
- **High Flight Rate**: Multiple launches per ship per day needed

**Timeline (as of 2025):**
- 2026: Uncrewed Mars landing attempt (50-50 chance per Musk)
- 2028: Human landing (optimistic) / 2031 (realistic)
- 2033: 500 ships delivering 150,000 tons cargo

**Mars Entry-Descent-Landing:**
- Aerobraking using heat shield
- Supersonic retropropulsion
- Landing legs deploy at low altitude
- Target: Arcadia Planitia (water ice access)

---
