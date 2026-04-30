# SpaceX Operations Reference

## Launch Sites

### Cape Canaveral Space Force Station, Florida

#### Space Launch Complex 40 (SLC-40)
| Attribute | Value |
|-----------|-------|
| Location | Cape Canaveral, FL |
| Primary Use | Falcon 9 |
| First Launch | 2010 |
| Turnaround Record | 2 days, 15 hours, 53 minutes |
| Pads | Single |
| Landing | ASDS or expendable |

**Features:**
- Transporter-Erector-Launcher (TEL)
- RP-1 and LOX storage
- Helium storage
- Payload integration facility

#### Launch Complex 39A (LC-39A)
| Attribute | Value |
|-----------|-------|
| Location | Kennedy Space Center, FL |
| Primary Use | Falcon 9, Falcon Heavy, Crew missions |
| First Launch | 1967 (Apollo 4), 2017 (SpaceX) |
| Historical | Apollo 11, Saturn V, Shuttle launches |
| Crew Access Arm | Yes |

**Features:**
- Fixed Service Structure (FSS) modified for Falcon
- Crew Access Tower for Dragon
- Falcon Heavy capability
- Future Starship modifications planned

### Vandenberg Space Force Base, California

#### Space Launch Complex 4 East (SLC-4E)
| Attribute | Value |
|-----------|-------|
| Location | Vandenberg, CA |
| Primary Use | Falcon 9 (polar orbits) |
| First SpaceX Launch | 2013 |
| Turnaround Record | 3 days, 15 hours, 23 minutes |
| Landing | RTLS or ASDS (Pacific) |

**Use Cases:**
- Sun-synchronous orbits
- Polar orbits
- Iridium constellation
- West coast Starlink

### Starbase, Boca Chica, Texas

#### Overview
Starbase is the primary development and launch site for Starship.

| Attribute | Value |
|-----------|-------|
| Location | Boca Chica, TX |
| Primary Use | Starship development and launch |
| Orbital Launch Pad | OLP (since 2022) |
| Test Facilities | Massey's, Rocket Garden |
| Production | Starfactory (1M sq ft) |

#### Launch Infrastructure

**Orbital Launch Mount:**
- 20-story launch tower
- "Mechazilla" chopstick arms for booster catch
- QD (Quick Disconnect) arms for propellant loading
- Flame diverter and sound suppression

**Production Facilities:**
- **Starfactory**: 1M sq ft manufacturing facility (2024)
- **Rig**: Stacking high-bay
- **Sanchez Site**: Additional production

#### Environmental Assessment
- FAA approval for 25 flights/year (2024)
- Tiered assessment for increased cadence
- Wildlife conservation measures

---

## Launch Operations Flow

### Falcon 9 Launch Timeline (T-minus)

```
T-38:00  ┐
         │ Vehicle power on, systems check begins
T-35:00  │ RP-1 (rocket fuel) loading begins
T-35:00  │ Liquid oxygen (LOX) loading begins (1st stage)
T-16:00  │ LOX loading begins (2nd stage)
T-07:00  ┤ Falcon 9 begins engine chill (thermal conditioning)
T-05:00  │ Dragon transition to internal power (if crewed)
T-01:00  │ Flight computer assumes control
T-00:45  │ Launch Director verifies go for launch
T-00:07  │ Engine ignition sequence begins
T-00:00  ┘ LIFTOFF

+00:01:00  Max-Q (maximum dynamic pressure)
+00:02:30  MECO (Main Engine Cutoff) - 1st stage
+00:02:38  Stage separation
+00:02:40  Second engine ignition
+00:03:30  Fairing separation (if applicable)
+00:08:30  Second engine cutoff (SECO-1)
+00:09:00  1st stage landing (if recovering)
+00:45:00  SECO-2 (final orbit insertion)
```

### Countdown Holds
- **T-20:00**: Built-in hold for final checks
- **T-05:00**: Final go/no-go poll
- Can recycle to T-20 if issues arise

---

## Recovery Operations

### Drone Ships (Autonomous Spaceport Drone Ships)

| Name | Abbreviation | Home Port | Ocean |
|------|--------------|-----------|-------|
| Of Course I Still Love You | OCISLY | Port Canaveral, FL | Atlantic |
| Just Read the Instructions | JRTI | Port Canaveral, FL | Atlantic |
| A Shortfall of Gravitas | ASOG | Port Canaveral, FL | Atlantic |
| (Unnamed Pacific) | - | Long Beach, CA | Pacific |

**Specifications:**
- Length: ~91m (300 ft)
- Width: ~52m (170 ft)
- Propulsion: Diesel-powered thrusters
- Positioning: GPS-guided, dynamic positioning
- Landing deck: Reinforced steel

### Booster Recovery Process

```
┌──────────────────────────────────────────────────────────────┐
│                  BOOSTER RECOVERY FLOW                        │
├──────────────────────────────────────────────────────────────┤
│                                                               │
│  1. ENTRY BURN (T+ ~6 minutes)                               │
│     └─ 3 center engines reignite to slow descent             │
│                                                               │
│  2. AERODYNAMIC GUIDANCE                                     │
│     └─ Grid fins steer toward landing zone                   │
│                                                               │
│  3. LANDING BURN (T+ ~8 minutes)                             │
│     └─ Single center engine ignites for final descent        │
│                                                               │
│  4. LANDING                                                  │
│     ├─ RTLS: Return to launch site (LZ-1 or LZ-4)           │
│     └─ ASDS: Land on drone ship downrange                    │
│                                                               │
│  5. SECURING                                                 │n│     └─ Octograbber robot secures booster to deck             │
│                                                               │
│  6. TRANSPORT                                                │
│     └─ Towed to port, then trucked to refurbishment          │
│                                                               │
│  7. REFURBISHMENT                                            │
│     └─ Inspection, engine swap if needed, re-flight prep     │
│                                                               │
└──────────────────────────────────────────────────────────────┘
```

### Fairing Recovery

| Aspect | Details |
|--------|---------|
| Cost per pair | ~$6M |
| Recovery method | Parachute + catcher ships |
| Catcher ships | GO Ms. Tree, GO Ms. Chief (retired) |
| Current method | Water recovery, refurbishment |
| Most flights per fairing | 22+ |

---

## Dragon Recovery

### Splashdown Process

**Crew Dragon:**
1. Deorbit burn using Draco thrusters
2. Trunk separation
3. Nosecone closure
4. Atmospheric entry (heat shield facing forward)
5. Drogue parachutes deploy (2) at ~5.5 km
6. Main parachutes deploy (4) at ~2 km
7. Splashdown in Atlantic or Pacific
8. Recovery ship retrieves capsule
9. Crew egress within ~1 hour

**Recovery Ships:**
- GO Searcher (primary)
- GO Navigator (backup)
- Fast boats for initial approach
- Medical personnel on board

---

## Testing Operations

### McGregor Test Facility, Texas

**Capabilities:**
- Engine acceptance testing (all Raptor, Merlin)
- Stage testing (Falcon 9 first stage)
- Vertical test stand (Raptor)
- Horizontal test stand (Merlin)

**Test Types:**

| Test | Duration | Purpose |
|------|----------|---------|
| Component | Seconds | Valve, igniter checkout |
| Short Duration | 5-10 seconds | Basic function |
| Medium Duration | 30-60 seconds | Full power validation |
| Long Duration | 2-3 minutes | Mission profile simulation |
| Acceptance | Full duration | Flight qualification |

### Starship Testing

**Test Sequence:**
1. **Cryo Proof**: Pressure test with liquid nitrogen
2. **Static Fire**: Engine ignition while held down
3. **Wet Dress Rehearsal**: Full countdown with propellant
4. **Flight Test**: Actual launch attempt

**Test Sites:**
- **Starbase**: Orbital flight tests
- **Massey's**: Suborbital hops (early development)

---

## Mission Control

### Hawthorne Mission Control

**Location**: SpaceX HQ, Hawthorne, CA

**Functions:**
- All Falcon 9/Heavy launches
- Dragon operations
- Starlink constellation management
- Starship test flights

**Positions:**
- Flight Director
- Propulsion Engineer
- GNC (Guidance, Navigation, Control)
- Electrical/Avionics
- Recovery Coordinator
- Range Liaison

### Launch Control at Cape Canaveral

**Responsibilities:**
- Final countdown operations
- Range coordination
- Pad safety
- Weather monitoring

---

## Launch Statistics

### 2024 Performance

| Metric | Value |
|--------|-------|
| Total Launches | 167 (Falcon 9) |
| Success Rate | 99.25% (133/134) |
| Booster Landings | 130 successful |
| Dragon Missions | 6 (2 crew, 4 cargo) |
| Starlink Satellites | 3,000+ launched |

### 2025 Performance (projected)

| Metric | Value |
|--------|-------|
| Falcon 9 Launches | 167 |
| Starship Flights | 5 (suborbital tests) |
| Total Orbital | 190+ |

### All-Time Records (as of 2025)

| Record | Value | Date |
|--------|-------|------|
| Most flown booster | 32 flights | New record |
| Fastest turnaround | 13d 12h 34m | B1080 |
| Most annual launches | 167 | 2025 |
| Consecutive landings | 267 | Streak ended Aug 2024 |
| Total Falcon launches | 500+ | Cumulative |
| Total booster landings | 589+ | Cumulative |

---

**Document Version**: 1.1  
**Last Updated**: 2026-03-21
