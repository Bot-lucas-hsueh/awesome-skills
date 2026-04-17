## § 8 Standard Workflow

### Phase 1: Site Selection & Feasibility
```
1.1 Site Identification & Screening
  - [ ] Define service area and target locations (proximity to demand generators)
  - [ ] Screen candidate sites: rooftop structural load capacity, building height clearance
  - [ ] Check airspace compatibility: no IFR approach conflicts, OLS compliance possible
  - [ ] Verify utility capacity: minimum 1 MVA per 4-pad vertiport
  - [✓ Done] Output: Shortlist of 3-5 sites with feasibility scoring matrix
  - [✗ FAIL] If structural load bearing < 150 lb/ft² → ground-level or purpose-built structure required

1.2 Detailed Site Assessment
  - [ ] Commission structural engineering assessment (load bearing, seismic, wind)
  - [ ] File FAA Form 7460-1 (Notice of Proposed Construction) for each site
  - [ ] Conduct noise impact assessment for neighbors within 1 km
  - [ ] Identify all required permits: building, planning, utility easements, fire marshal
  - [✓ Done] Output: Site Assessment Report with recommended site and permit roadmap
  - [✗ FAIL] If FAA issues Determination of Hazard → site must be abandoned or redesigned
```

### Phase 2: Vertiport Design
```
2.1 Airside Design (Aviation Authority Jurisdiction)
  - [ ] Size FATO and TLOF per FAA AC 150/5390-2D (or EASA equivalent)
  - [ ] Design Obstacle Limitation Surfaces (approach, departure, transitional)
  - [ ] Design vertipad lighting (threshold lights, FATO perimeter, TLOF center)
  - [ ] Design wind indicator (windsock) placement
  - [ ] Design fire suppression system per NFPA 418 (foam system for each pad)
  - [✓ Done] Output: Airside Design Drawing Package for FAA review
  - [✗ FAIL] If obstacle penetrates OLS → modify approach path or remove obstacle

2.2 Charging & Power Infrastructure
  - [ ] Size electrical service: N pads × 350 kW + 30% contingency
  - [ ] Design transformer and switchgear room (minimum 10m from FATO)
  - [ ] Specify charger type (CCS2/CHAdeMO/proprietary aviation connector)
  - [ ] Design arc flash protection and emergency disconnect within 3 sec
  - [✓ Done] Output: Electrical Single-Line Diagram and load schedule
  - [✗ FAIL] If utility cannot supply required kVA within 12 months → battery energy storage buffer required

2.3 Terminal & Landside Design
  - [ ] Passenger flow: arrival → check-in → security → gate → boarding bridge/walkway
  - [ ] Baggage handling for weight-limited cabin (eVTOL typically 20-30 kg/PAX)
  - [ ] ADA-compliant path of travel from ground transportation to boarding
  - [ ] Operations center: 24/7 staffed; UTM interface displays; emergency coordination
  - [✓ Done] Output: Terminal Layout Drawing with circulation analysis
```

### Phase 3: Regulatory Approval & Commissioning
```
3.1 Regulatory Submissions
  - [ ] Submit vertiport design package to FAA Airport District Office (ADO)
  - [ ] File building permit with local authority
  - [ ] Submit noise impact analysis to local planning board
  - [ ] Coordinate with electric utility for grid connection agreement
  - [✓ Done] Output: All regulatory approvals received (target: 12-18 months for rooftop)
  - [✗ FAIL] If local planning board rejects → appeal process or alternate site

3.2 Construction & Commissioning
  - [ ] Construction oversight: FATO surface, lighting installation, fire system commissioning
  - [ ] FAA safety inspection before first operations
  - [ ] Fire department acceptance test of suppression system
  - [ ] Electrical commissioning: arc flash study verification, charger function test
  - [✓ Done] Output: FAA-inspected vertiport with Certificate of Occupancy
```

