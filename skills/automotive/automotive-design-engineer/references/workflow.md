## § 8 Standard Workflow

### Phase 1: Concept Design
```
1.1 Package Definition
  - [ ] Define vehicle exterior dimensions (L×W×H, wheelbase, overhang)
  - [ ] Locate H-point (hip point), eye ellipse, seating reference points for all seats
  - [ ] Allocate hard points: engine/motor, battery, suspension pickups, ADAS sensors
  - [ ] Confirm regulatory keep-out zones (pedestrian protection, 30° forward visibility)
  - [✓ Done] Output: Vehicle Package Drawing (side + plan + front/rear cross-sections)
  - [✗ FAIL] If H-point exceeds regulatory limits → adjust seating position before proceeding

1.2 Structural Concept
  - [ ] Define BIW structural topology: load paths for frontal/side/rear crash
  - [ ] Select material strategy: AHSS (Advanced High-Strength Steel), aluminum, CFRP
  - [ ] Estimate structural mass (parametric model: ~300-400 kg for mid-size sedan BIW)
  - [✓ Done] Output: BIW Structural Concept with load path description and mass estimate
  - [✗ FAIL] If BIW mass > budget + 15% at concept → initiate topology optimization study
```

### Phase 2: Engineering Design
```
2.1 BIW Structural Design
  - [ ] Design A-pillar, B-pillar, rocker sections (geometry + thickness + material)
  - [ ] Design front crash box + front rail for frontal crash energy absorption
  - [ ] Design floor cross-member for side crash intrusion management
  - [ ] Run crash FEA at concept sections; verify within ±15% of targets
  - [✓ Done] Output: BIW CAD model v1.0 with crash simulation correlation

2.2 Chassis & Suspension Design
  - [ ] Design suspension kinematics (KnC - Kinematics and Compliance targets)
  - [ ] Size spring rates, damper characteristics, anti-roll bar stiffness
  - [ ] Verify ride comfort (vertical acceleration PSD at driver H-point < 0.05 m²/s³)
  - [✓ Done] Output: Suspension Design Specification with K&C data

2.3 Powertrain & BEV Battery Integration
  - [ ] Package powertrain within allocated envelope; verify clearances at full jounce
  - [ ] Design battery box within BIW floor structure; verify ECE R100 Rev 3 compliance
  - [ ] Design battery thermal management routing; verify ingress protection (IP67 minimum)
  - [✓ Done] Output: Powertrain Integration Drawing with thermal management scheme
```

### Phase 3: Validation & Homologation
```
3.1 DVP&R Execution
  - [ ] Execute crash test program (ECE R94/R95 + NCAP protocol)
  - [ ] Execute durability test (300,000 km simulation on proving ground)
  - [ ] Execute NVH test (interior noise targets at cruise and acceleration)
  - [✓ Done] Output: DVP&R completed; all tests pass; ready for type approval

3.2 Homologation
  - [ ] Submit technical documentation to testing authority (TÜV, DEKRA, etc.)
  - [ ] Attend crash witness testing; submit conformity documentation
  - [✓ Done] Output: EC Type Approval (ECWVTA) or national equivalents
```

