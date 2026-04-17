## § 8 Standard Workflow

### Phase 1: System Requirements & Concept
```
1.1 Mission Requirements Definition
  - [ ] Define coverage area, availability, data rate per terminal
  - [ ] Define frequency band (regulatory availability check first)
  - [ ] Define orbit type and altitude (coverage vs. latency trade)
  - [✓ Done] Output: System Requirements Document (SRD) with link performance requirements
  - [✗ FAIL] If required EIRP exceeds ITU PFD mask → redesign antenna or reduce coverage area

1.2 Top-Level Architecture Selection
  - [ ] GEO vs. LEO/MEO trade: latency, coverage, handover complexity, constellation size
  - [ ] HTS vs. widebeam: spectral efficiency vs. terminal size requirement
  - [ ] Ground segment topology: centralized hub vs. distributed gateways
  - [✓ Done] Output: System Architecture Document with selected approach
```

### Phase 2: Link Budget & RF Design
```
2.1 Forward Link Budget
  - [ ] Compute satellite EIRP per beam from transponder power and antenna gain
  - [ ] Apply ITU rain model (P.618) for rain fade at required availability
  - [ ] Size user terminal antenna for positive link margin (≥ 3 dB clear sky)
  - [ ] Select MODCOD table: peak efficiency at clear sky, robust fallback for rain fade
  - [✓ Done] Output: Forward Link Budget spreadsheet with margin analysis at all elevation angles
  - [✗ FAIL] If margin < 3 dB → increase terminal size, boost satellite EIRP, or reduce link rate

2.2 Return Link Budget
  - [ ] Compute terminal EIRP within ITU PFD mask constraints
  - [ ] Compute gateway G/T requirement for positive margin
  - [ ] Verify interference compliance with adjacent satellite (coordination arc ±6°)
  - [✓ Done] Output: Return Link Budget with ITU compliance verification
  - [✗ FAIL] If terminal EIRP exceeds PFD mask → reduce power, increase bandwidth, or use higher gain antenna

2.3 Interference Analysis
  - [ ] Adjacent satellite interference: compute C/I for worst-case satellite position
  - [ ] Self-interference: compute frequency reuse efficiency for HTS multibeam design
  - [ ] Uplink interference into adjacent satellite: verify compliance with coordination agreements
  - [✓ Done] Output: Interference Analysis Report with mitigation design
```

### Phase 3: Regulatory & Operational
```
3.1 ITU Coordination
  - [ ] File Advance Publication Information (API) with ITU BR (3-8 years before launch)
  - [ ] Identify coordination triggers (within coordination arc of existing networks)
  - [ ] Conduct bilateral coordination negotiations with affected administrations
  - [✓ Done] Output: ITU coordination completed; due diligence for protection obligations

3.2 National Licensing
  - [ ] File FCC earth station license (Part 25) or equivalent national license
  - [ ] Obtain terminal type approval for user equipment
  - [✓ Done] Output: FCC license granted or equivalent national authorization
```

