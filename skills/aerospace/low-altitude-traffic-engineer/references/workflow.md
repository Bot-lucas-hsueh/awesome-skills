## § 8 Standard Workflow

### Phase 1: Airspace Assessment & Requirements
```
1.1 Airspace Classification Mapping
  - [ ] Map operational area to airspace classes (A/B/C/D/E/G)
  - [ ] Identify LOA (Letter of Agreement) requirements with controlling ANSP
  - [ ] Document population density and critical infrastructure density
  - [✓ Done] Output: Airspace Integration Plan (AIP) approved by ANSP
  - [✗ FAIL] If ANSP refuses LOA → Escalate to regulatory working group or modify operational area

1.2 Traffic Demand Modeling
  - [ ] Estimate peak simultaneous operations (PSO) per km² at 5-year horizon
  - [ ] Define peak/off-peak traffic patterns (time-of-day, seasonal)
  - [ ] Calculate required separation maintenance rate (target: 99.99%)
  - [✓ Done] Output: Traffic Demand Model with capacity requirements
  - [✗ FAIL] If PSO > 500/km² → Escalate to advanced UTM architecture (sector-based)
```

### Phase 2: UTM System Architecture Design
```
2.1 USS/FIMS Architecture
  - [ ] Define USS roles (Flight Planning, Geo-Awareness, Traffic Info, Weather)
  - [ ] Design DSS federation topology (single DSS vs. federated multi-region)
  - [ ] Specify API interfaces (ASTM F3548 compliant REST/WebSocket)
  - [ ] Define data residency and sovereignty requirements (critical for EU)
  - [✓ Done] Output: UTM Architecture Document with API specification
  - [✗ FAIL] If DSS synchronization latency > 100ms → Redesign topology or reduce federation scope

2.2 Conflict Detection Algorithm Selection
  - [ ] Choose strategic CD: Volume reservation (FCFS) vs. Priority-based vs. Market-based
  - [ ] Choose tactical CD: Geometric (cylinder intersection) vs. RRT* vs. Velocity Obstacle
  - [ ] Characterize O(n) complexity at target traffic density
  - [ ] Define false alarm rate (FAR) and missed detection rate (MDR) requirements
  - [✓ Done] Output: CD&R Algorithm Specification with performance bounds
  - [✗ FAIL] If latency > 500ms at target density → Spatial indexing (R-tree, KD-tree) required
```

### Phase 3: Integration, Testing & Certification
```
3.1 ANSP Integration
  - [ ] Implement SWIM (System Wide Information Management) interface for ATC data
  - [ ] Define conflict of interest protocol (manned vs. unmanned priority)
  - [ ] Test emergency procedures (VFR emergency squawk, lost comm protocols)
  - [✓ Done] Output: Signed LOA with controlling ANSP + joint SOP
  - [✗ FAIL] If ATC rejects integration → Escalate to national aviation authority

3.2 Regulatory Certification
  - [ ] Complete UTM ConOps document per ICAO GUAS template
  - [ ] Submit USS certification package to competent authority (FAA/EASA)
  - [ ] Pass UTM interoperability test (ASTM F3548 conformance test suite)
  - [✓ Done] Output: Certified USS with regulatory approval letter
  - [✗ FAIL] If conformance test fails → Log failure, triage algorithm or interface bug

3.3 Operational Readiness
  - [ ] Load test UTM at 2× expected peak traffic (chaos engineering)
  - [ ] Validate all contingency procedures with tabletop exercise
  - [ ] Train operator community on flight planning interface
  - [✓ Done] Output: Go-live approval with monitoring dashboard active
```

