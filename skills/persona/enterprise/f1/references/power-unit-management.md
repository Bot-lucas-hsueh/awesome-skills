# Power Unit Management

## Hybrid Power Unit Architecture (2024)

### System Overview

The modern F1 power unit is a complex hybrid system combining internal combustion with electrical energy recovery. Total power output exceeds 1000 horsepower.

```
Power Unit Components:
├── Internal Combustion Engine (ICE)
│   ├── 1.6L V6 turbocharged
│   ├── 90° cylinder angle
│   └── ~15,000 RPM limit
├── Turbocharger (TC)
│   ├── Single turbo, unlimited boost
│   └── Connected to MGU-H
├── Motor Generator Unit - Heat (MGU-H)
│   ├── Recovers exhaust energy
│   └── Eliminated for 2026
├── Motor Generator Unit - Kinetic (MGU-K)
│   ├── Recovers braking energy
│   └── Deploys electrical power
├── Energy Store (ES)
│   ├── 4 MJ capacity
│   └── Lithium-ion battery
└── Control Electronics (CE)
    └── Manages all systems
```

### Energy Flow Management

**Energy Recovery:**
- MGU-K: Maximum 2 MJ per lap recovered
- MGU-H: Unlimited recovery
- Total deployment: Maximum 4 MJ per lap via MGU-K

**Deployment Strategy:**

| Track Section | ERS Deployment | Rationale |
|---------------|----------------|-----------|
| Long straights | High (80-100%) | Maximize speed, defend/attack |
| Medium straights | Medium (40-60%) | Balance speed vs. recovery |
| Corners | None (recovery) | Harvest under braking |
| Exit of slow corners | High (70-90%) | Acceleration assistance |

### Thermal Efficiency

**Current Generation Performance:**
- Thermal efficiency: 50%+ (world's most efficient engines)
- Fuel flow limit: 100 kg/hour
- Race fuel allowance: 110 kg (adjusted per race)

**Efficiency Factors:**
- Lean burn combustion
- High compression ratio
- Advanced knock detection
- Turbo compounding (MGU-H)

## Power Unit Modes

### Qualifying Modes

**Party Mode (Q3 only):**
- Maximum power extraction
- Aggressive engine mapping
- Full ERS deployment
- Limited by reliability constraints

**Race Preparation Mode:**
- Balance power and longevity
- Calibrate systems for race distance
- Validate cooling performance

### Race Modes

**Mode 1 - Maximum Attack:**
- Full power available
- High ERS deployment
- Used: Race start, overtaking, defense
- Risk: High component stress

**Mode 2 - Standard Race:**
- Optimal power/reliability balance
- Standard ERS strategy
- Used: Majority of race

**Mode 3 - Conservation:**
- Reduced power output
- High energy recovery
- Used: Safety Car periods, cooling issues

**Mode 4 - Reliability:**
- Significant power reduction
- Maximum component protection
- Used: Component degradation warnings

## ERS Strategy

### Deployment Zones by Circuit

**High-ERS Tracks (e.g., Monza, Spa):**
- Multiple long straights
- Strategy: Deploy on all straights, recover in corners
- Battery management: Critical (risk of depletion)

**Medium-ERS Tracks (e.g., Silverstone, COTA):**
- Mix of corners and straights
- Strategy: Selective deployment on key straights
- Battery management: Moderate

**Low-ERS Tracks (e.g., Monaco, Hungary):**
- Few long straights
- Strategy: Deploy exiting slow corners
- Battery management: Easier (constant recovery)

### Overtaking Battery Strategy

**Pre-Overtake Preparation:**
1. Harvest ERS for 2-3 laps before attempt
2. Enter overtaking zone with full battery
3. Deploy maximum power on straight
4. Post-overtake: Recover while maintaining position

**Defensive Battery Strategy:**
1. Monitor competitor's ERS status
2. Maintain sufficient charge for defense
3. Deploy selectively to break DRS tow
4. Force competitor to use more ERS than optimal

## Power Unit Reliability

### Component Lifing

**ICE (Internal Combustion Engine):**
- Target life: 6-8 race weekends
- Limiting factors: Piston wear, valve train, turbo
- Degradation: ~0.1s/lap over life

**Turbocharger:**
- Target life: 6-8 race weekends
- Limiting factors: Bearing wear, blade erosion
- Degradation: Power loss, slower spool

**MGU-K:**
- Target life: 6-8 race weekends
- Limiting factors: Bearing wear, electrical insulation
- Degradation: Reduced energy recovery

**MGU-H:**
- Target life: 6-8 race weekends
- Limiting factors: Thermal stress, bearing wear
- Degradation: Reduced energy recovery

**Energy Store:**
- Target life: Full season (2 units allowed)
- Limiting factors: Cycle count, thermal degradation
- Degradation: Reduced capacity, power output

### Reliability Monitoring

**Key Parameters:**
- Oil pressure and temperature
- Coolant temperature
- Exhaust gas temperatures
- Turbo shaft speed
- ERS temperatures
- Knock sensor data

**Warning Thresholds:**
- Oil temp > 120°C: Reduce power
- EGT > 1050°C: Reduce power
- Knock detection: Immediate ignition adjustment

## 2026 Power Unit Changes

### Major Modifications

**Elimination:**
- MGU-H removed (cost and complexity reduction)
- Simpler, more road-relevant technology

**Enhancement:**
- MGU-K power: 120kW → 350kW
- Electrical deployment: ~50% of total power
- 100% sustainable synthetic fuels

**Performance Target:**
- Total power: 1000+ hp maintained
- Thermal:ICE power ratio: ~50:50
- Simplified packaging

### Strategic Implications

**Energy Management Priority:**
- Electrical power becomes dominant strategy variable
- Battery state of charge critical to performance
- Overtaking strategy fundamentally changes

**Active Aerodynamics Integration:**
- Wing modes affect power requirements
- Energy deployment linked to aero configuration
- New strategic optimization required

---

*Technical data based on FIA regulations and manufacturer specifications*
