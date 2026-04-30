## § 8 · Standard Workflow

### 8.1 Gas Distribution System Design

```
Phase 1: Load Analysis
├── Identify customers: residential, commercial, industrial
├── Determine load: heating, cooking, process (Btu/hr or scfh)
├── Apply diversity: not all equipment operates simultaneously
├── Peak demand: Design for coldest day (degree-day correlation)
└── Future growth: 10-20% reserve capacity

Phase 2: System Planning
├── Pressure class: High, medium, or low based on load/distance
├── Network configuration: Branched, looped, or grid
├── Regulator locations: Downstream pressure zones
├── Metering: Regulated vs. 1st stage vs. 2nd stage
└── Routing: Minimize length, avoid conflicts

Phase 3: Component Sizing
├── Mains: Flow calculation, size for <10% pressure drop
├── Services: Individual customer load, 0.5" w.c. drop max
├── Regulators: Capacity vs. setpoint, 25% turndown
├── Meters: Rotary or turbine for commercial, diaphragm for residential
└── Risers: Vertical routing, support, corrosion protection

Phase 4: Safety Systems
├── Overpressure: Relief valves, slam shuts at each pressure reduction
├── Odorization: For all odorless gas distribution
├── Leak detection: Portable and fixed detection
├── Emergency response: Shutdown procedures, public awareness
└── Documentation: As-built records, operating procedures
```

### 8.2 Pressure Regulator Selection

```
Step 1: Define Conditions
├── Inlet pressure range: Minimum to maximum available
├── Outlet pressure: Required downstream pressure
├── Flow rate: Maximum and minimum expected
├── Temperature range: Ambient operating conditions

Step 2: Select Regulator Type
├── Spring-loaded: Simple, inexpensive, good accuracy
├── Pilot-operated: Better capacity, stable outlet
├── Bigas/Cortez: High capacity, industrial applications
└── Electronic: For SCADA-controlled systems

Step 3: Size the Regulator
├── Use manufacturer's capacity tables
├── Apply 25% safety factor on flow
├── Verify <10% droop at maximum flow
└── Check for cavitation at low inlet

Step 4: Specify Overpressure Protection
├── Relief valve: 4:1 safety factor to inlet rating
├── Slam shut: For excessive pressure or low pressure
├── Monitor regulator: Parallel redundant protection
└── Relief vent: Discharge to safe location
```

---
