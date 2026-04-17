## § 7 Standards & Reference

See [references/07-standards.md](references/07-standards.md)

---

---

## Phase 2: Laminate Design & Analysis

**Objectives:** Define ply stacking sequence, compute laminate properties, check failure criteria

**Activities:**
- [ ] Generate symmetric, balanced laminate (no [B] coupling matrix, no shear-extension coupling)
- [ ] Apply 10% rule: minimum 10% of plies in each of 0°, ±45°, 90° orientations
- [ ] Compute [A], [B], [D] matrices using CLT; derive effective engineering constants
- [ ] Evaluate failure indices using Tsai-Wu or Hashin criteria under all load cases
- [ ] Check interlaminar stresses at free edges, ply drops, and cut-outs using 3D FEA
- [ ] Verify buckling load factors (eigenvalue analysis) with at least 1.5× margin on limit load
- [ ] Document ply book: sequence, orientations, material, thickness per ply

**✓ Done:** Failure index < 1.0 under all load cases with ETW allowables; buckling margin > 1.5; interlaminar stresses within matrix toughness limits; ply book complete
**✗ FAIL:** Unsymmetric or unbalanced laminate in a structural application; failure index ≥ 1.0 under any load case; missing ETW analysis

---

### Phase 3: Manufacturing Process Design

**Objectives:** Define manufacturing method, tooling concept, cure cycle, quality plan

**Activities:**
- [ ] Select manufacturing process (autoclave, RTM, OOA/VBO, filament winding, AFP)
- [ ] Define tooling material and concept (Invar, CFRP tool, aluminum) based on CTE matching requirements
- [ ] Specify cure cycle: heat-up rate (typically 1–3°C/min), dwell temperature and time, pressure (typically 690 kPa
- [ ] Set void content acceptance limit (typically ≤ 2% for structural, ≤ 1% for primary structure)
- [ ] Define NDT plan: 100% C-scan for primary structure; acceptance criteria per ASTM D2564 or customer spec
- [ ] Establish first-article inspection (FAI) requirements per AS9102

**✓ Done:** Cure cycle validated by thermal modeling (Raven, COMPRO, or equivalent); void content ≤ specified limit; NDT plan approved by engineering; FAI requirements documented
**✗ FAIL:** Cure cycle copied from datasheet without thermal survey of tooling; no void content specification; 100% NDT not planned for primary structure

---

### Phase 4: Testing & Certification

**Objectives:** Execute test program per building block approach, generate material qualification data

**Activities:**
- [ ] Level 1 (Coupon): ASTM D3039 (tensile), D6641 (compression), D3518 (shear), D5528 (GIC), D7136/D7137 (CAI)
- [ ] Level 2 (Element): Stiffened panel buckling, bonded joint strength, open-hole tension/compression
- [ ] Level 3 (Sub-component): Representative structural elements with load introduction
- [ ] Level 4 (Component): Full-scale structure or major component proof test
- [ ] Statistical analysis: generate A-basis (99th percentile, 95% confidence) or B-basis (90/95) allowables per CMH-17 methodology
- [ ] Document test reports traceable to individual specimen manufacture and test records

**✓ Done:** All building block levels tested; statistical allowables calculated; test reports complete and traceable; certification data package submitted
**✗ FAIL:** Skipping building block levels without justification; using mean values instead of A/B-basis for primary structure; non-traceable test data

---

