## § 8 Standard Workflow

### Phase 1 — RTL Design & Verification
- Write RTL in synthesizable SystemVerilog; apply SpyGlass lint before simulation
- Develop UVM testbench; target >95% code coverage, >90% functional coverage
- Run formal CDC analysis with SpyGlass or JasperGold; resolve all CDC violations
- [✓ Done]: Zero lint errors, coverage targets met, formal CDC clean, no X-propagation
- [✗ FAIL]: Unresolved X-propagation, unconstrained CDC paths, coverage gap >10%

### Phase 2 — Synthesis & Constraints
- Write SDC with create_clock, set_input_delay, set_output_delay, set_false_path
- Run DC/Genus; analyze timing, area, and power QoR reports
- Iterate: pipeline balancing, logic restructuring, register retiming
- [✓ Done]: WNS ≥ 0, TNS = 0 at synthesis corner; area within 10% of target
- [✗ FAIL]: > 100 timing violations; area > 120% of budget; unresolvable false paths

### Phase 3 — Physical Design (P&R)
- Floorplan: aspect ratio, power ring, macro placement, pin assignment
- CTS: target skew < 50 ps, insertion delay < 500 ps; use clock shielding
- Route: resolve DRC hotspots; add antenna diodes; verify signal integrity
- Run incremental Calibre DRC after each routing stage
- [✓ Done]: Zero routing DRC, zero antenna violations, IR drop < 3% static
- [✗ FAIL]: Unrouted nets, congestion overflow > 1%, power grid violations

### Phase 4 — Sign-off & Tapeout
- MCMM STA with PrimeTime: SS/FF/TT corners, −40°C to 125°C, ±10% VDD variation
- Final Calibre DRC/LVS clean on full-chip GDS
- ATPG: generate and verify scan patterns; simulate patterns at gate level
- Freeze GDS; submit to foundry with process runset version documented
- [✓ Done]: Zero DRC/LVS violations, WNS ≥ 0 all corners, fault coverage ≥ 99%
- [✗ FAIL]: Any open DRC/LVS violation; timing fail in even one PVT corner

