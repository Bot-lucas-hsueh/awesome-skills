# Lockheed Martin Space Systems

## Space Segment Overview

```yaml
segment: Space
headquarters: Denver, Colorado
leadership: Robert M. Lightfoot Jr., Executive Vice President
2025_sales: $13.0 billion (17% of Lockheed Martin total)
2025_operating_profit: $1.3 billion
2025_margin: 10.3%
2025_backlog: $31.0 billion
employees: ~10,000
```

## Major Program Areas

### Human Space Exploration

#### Orion Spacecraft

```yaml
program: NASA Orion Multi-Purpose Crew Vehicle (MPCV)
contractor: Lockheed Martin (prime)
contract_value: ~$12B+ (development through Artemis IV)
purpose: Crewed deep space exploration

specifications:
  crew_module_diameter: 16.5 ft (5.0 m)
  crew_module_length: 11 ft (3.3 m)
  total_length_with_service_module: ~26 ft
  habitable_volume: 316 cu ft (8.9 m³)
  crew_capacity: 4 astronauts
  mission_duration: Up to 21 days (lunar orbit)

key_components:
  crew_module: Lockheed Martin built
  european_service_module: ESA provided
  launch_abort_system: Northrop Grumman
  adapter_modules: Various

artemis_missions:
  artemis_i:
    date: November 2022
    type: Uncrewed lunar flyby
    duration: 25 days
    status: Complete
    
  artemis_ii:
    date: No earlier than February 2026
    type: Crewed lunar flyby
    crew: 4 astronauts
    status: Spacecraft delivered to NASA May 2025
    
  artemis_iii:
    date: No earlier than 2027
    type: Crewed lunar landing
    status: In development
    
  artemis_iv_plus:
    contract: Extended through Artemis VIII
    status: Production contract awarded

manufacturing:
  primary_facility: Kennedy Space Center, Operations & Checkout Building
  workforce: 1,000+ technicians and engineers
  production_rate: ~1 spacecraft per year (current)
```

### Missile Defense

#### Terminal High Altitude Area Defense (THAAD)

```yaml
role: Ballistic missile defense interceptor
operator: US Army, international customers
development: Lockheed Martin prime contractor
status: Operational, production ongoing

system_components:
  - Launchers: Truck-mounted, 8 interceptors each
  - Interceptors: Hit-to-kill kinetic kill vehicle
  - AN/TPY-2 radar: X-band, transportable
  - Fire Control & Communications: Battle management

specifications:
  interceptor_range: 200+ km
  intercept_altitude: 40-150 km (exo-atmospheric)
  guidance: Inertial + seeker (hit-to-kill)
  warhead: Kinetic energy (no explosive)

operators:
  - United States: 7 batteries fielded
  - Saudi Arabia: 7 batteries
  - UAE: 2 batteries
  - South Korea: 1 battery
  - Taiwan: Contracted
  - Others: Various negotiations

recent_contracts:
  - 2024: $4.5B for Saudi Arabia follow-on
  - 2025: Ongoing production for US and allies
```

#### Next Generation Interceptor (NGI)

```yaml
role: Ground-based midcourse defense interceptor
program: NGI competition
lockheed_martin_team: Lockheed Martin + Aerojet Rocketdyne
competitor: Northrop Grumman
status: In development (competition ongoing)

purpose: 
  - Replace aging GBI (Ground-Based Interceptor)
  - Counter advanced ballistic missile threats
  - Multiple kill vehicles per booster

timeline:
  development_start: 2021
  preliminary_design: 2024
  critical_design: 2026 (planned)
  first_flight: 2028 (planned)
```

### Strategic Deterrence

#### Trident II D5 LE

```yaml
full_name: Trident II D5 Fleet Ballistic Missile (FBM)
role: Submarine-launched ballistic missile (SLBM)
operator: US Navy, Royal Navy (UK)
contractor: Lockheed Martin (prime)
status: Life Extension production

specifications:
  length: 44 ft (13.4 m)
  diameter: 6 ft 11 in (2.11 m)
  weight: 130,000 lb (59,000 kg)
  range: >7,500 miles (12,000 km)
  guidance: Astro-inertial with GPS
  warhead: W76-0/1/2 or W88 (MIRV capable)

life_extension_program:
  purpose: Extend service life to 2040s
  upgrades:
    - New guidance system
    - Enhanced accuracy
    - Refurbished motors
    - W76-2 low-yield option
  status: Production ongoing
```

### Satellite Systems

#### Next Gen OPIR

```yaml
full_name: Next Generation Overhead Persistent Infrared
role: Missile warning satellite constellation
operator: US Space Force
contractor: Lockheed Martin (GEO and Polar)
  northrop_grumman: Polar component
purpose: 
  - Advanced ballistic missile detection
  - Hypersonic missile tracking
  - Battlespace awareness

architecture:
  geo_satellites: 3 (Lockheed Martin)
  polar_satellites: 2 (Northrop Grumman)
  launch_schedule:
    - GEO-1: 2025 (delayed to 2026)
    - GEO-2: 2027
    - GEO-3: 2028
    - Polar: 2028-2029

key_features:
  - Resilient, hardened design
  - Improved sensor sensitivity
  - Faster data processing
  - Cross-link communications
  - Proliferated architecture consideration
```

#### GPS III

```yaml
role: Navigation satellite constellation
operator: US Space Force
contractor: Lockheed Martin (spacecraft)
  raytheon: GPS III payload

specifications:
  accuracy: <1 meter (civilian), <0.3 meter (military)
  lifespan: 15 years
  signals: 
    - L1C (interoperable with Galileo)
    - M-code (military anti-jam)

status:
  gps_iii:
    total: 10 satellites
    launched: 10 (complete)
    operational: All
  gps_iiif:
    follow_on: 22 satellites planned
    upgrades: Regional military protection, laser retroreflector
    first_launch: 2026 (planned)
```

#### SBIRS

```yaml
full_name: Space-Based Infrared System
role: Missile warning, defense, battlespace awareness
operator: US Space Force

constellation:
  geo_satellites: 4 (SBIRS GEO 1-4)
  heo_sensors: 2 (hosted payloads)
  status: Fully operational

replacement: Next Gen OPIR (transition ongoing)
```

#### Commercial & Civil Satellites

```yaml
goes-r_series:
  role: Geostationary weather satellites
  customer: NOAA/NASA
  contractor: Lockheed Martin (spacecraft)
  status: GOES-R, S, T, U delivered/operational

jason_cs:
  role: Ocean topography
  customer: NOAA/NASA/EUMETSAT
  status: Operational

tacsat:
  role: Tactical satellite demonstration
  status: Completed, launch 2025
  purpose: Demonstrate rapid satellite deployment
```

### Hypersonics

#### AGM-183A ARRW

```yaml
full_name: Air-Launched Rapid Response Weapon
role: Hypersonic boost-glide weapon
operator: US Air Force (development)
contractor: Lockheed Martin
status: Testing, program uncertain

specifications:
  speed: Mach 5+
  range: 1,000+ miles
  platform: B-52H, B-1B, F-15EX

program_status:
  testing: Multiple flight tests conducted
  challenges: Technical difficulties
  future: Program under review
```

#### Other Hypersonic Programs

```yaml
opfires:
  customer: DARPA/US Army
  role: Operational fires hypersonic system
  status: Testing
  contractor: Lockheed Martin

classified_programs:
  - Multiple airborne and maritime hypersonic efforts
  - Details classified
```

### Space Domain Awareness

```yaml
space_fence:
  customer: US Space Force
  contractor: Lockheed Martin
  location: Kwajalein Atoll
  status: Operational 2020
  capability: 
    - S-band radar
    - Tracks 200,000+ objects
    - Detects objects 5cm+ in LEO

deepspace_advanced_radar_capability:
  customer: US Space Force
  role: Deep space surveillance
  location: Australia
  status: Development
```

## Space Business Strategy

### 21st Century Security® Space

```yaml
strategic_pillars:
  - Resilient architectures (proliferated constellations)
  - Rapid technology insertion
  - Commercial partnerships
  - Dual-use capabilities
  - International collaboration

investment_areas:
  - Lunar infrastructure
  - In-space servicing
  - Autonomous systems
  - Advanced propulsion
  - Nuclear thermal propulsion
```

### Commercial Partnerships

```yaml
key_partnerships:
  vast_space:
    partner: Vast Space
    purpose: Commercial space station (Haven-1)
    lockheed_role: Support systems, logistics
    
  intuitive_machines:
    partner: Intuitive Machines
    purpose: Lunar surface operations
    lockheed_role: Infrastructure, communications
    
  terran_orbital:
    acquisition: 2024
    purpose: Small satellite manufacturing
    capability: Tyvak nanosatellites

  rocket_lab:
    relationship: Supplier/customer
    services: Launch services, satellite components
```

## Facilities

### Major Space Facilities

| Location | Function | Employees |
|----------|----------|-----------|
| Denver, CO | Headquarters, satellite manufacturing | 3,500 |
| Sunnyvale, CA | Satellite operations, missile defense | 3,500 |
| Cape Canaveral, FL | Launch processing, Orion | 1,000 |
| Huntsville, AL | Missile defense, hypersonics | 800 |
| Littleton, CO | Human spaceflight, exploration | 1,000 |
| King of Prussia, PA | Ground systems, C2 | 500 |
| Cambridge, UK | Communications satellites | 400 |

## Recent Developments (2024-2025)

| Date | Development |
|------|-------------|
| May 2025 | Orion Artemis II spacecraft delivered to NASA |
| Oct 2025 | Orion stacked on SLS for Artemis II |
| 2025 | Next Gen OPIR GEO-1 launch delayed to 2026 |
| 2025 | GPS IIIF development ongoing |
| 2024 | Terran Orbital acquisition completed |
| 2024 | Vast Space partnership announced |

---

*Last Updated: March 2026 | Sources: Lockheed Martin, NASA, US Space Force*
