## § 8 Standard Workflow

### Phase 1 — Schematic & Stackup Definition
- Create schematic with proper decoupling, termination, and filter networks
- Define PCB stackup (layers, materials, thicknesses) with fab house
- Calculate controlled impedance requirements for all high-speed nets
- [✓ Done]: Schematic complete, stackup approved by fab, impedance targets defined
- [✗ FAIL]: Missing decoupling, stackup undefined, no impedance spec

### Phase 2 — Component Placement & Partitioning
- Place components following signal flow; partition by function (analog/digital/power)
- Ensure decoupling caps within 0.5mm of power pins
- Position connectors at board edge; place mounting holes per mechanical draft
- [✓ Done]: Placement optimized, power partitioning defined, keepout areas marked
- [✗ FAIL]: Poor signal flow, decoupling > 1mm from pins, connectors not at edge

### Phase 3 — Routing & Signal Integrity
- Route high-speed signals first (DDR, USB, PCIe); maintain impedance control
- Apply length matching (DQS to DQ, clock skew); use diff pairs for >100Mbps
- Verify crosstalk < 5% on sensitive nets; add guard traces if needed
- [✓ Done]: All high-speed nets routed with <20% timing margin remaining
- [✗ FAIL]: Uncontrolled impedance, >5% crosstalk, length mismatch > spec

### Phase 4 — DFM & Manufacturing Output
- Verify design meets fab capabilities (min trace/space, via aspect ratio)
- Run DRC (design rule check) and vs. manufacturing capabilities
- Generate Gerber files, assembly drawing, pick-and-place, and fab notes
- [✓ Done]: DRC clean, all DFM issues resolved, Gerbers validated
- [✗ FAIL]: DRC errors, DFM violations, missing manufacturing output

