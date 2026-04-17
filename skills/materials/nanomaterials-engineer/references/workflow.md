## § 8 Standard Workflow

### Phase 1 — Synthesis Protocol Design and Initial Synthesis

**Steps:**
1. Review target material specification: size range, size distribution (σ/d < 10%), phase, surface chemistry.
2. Perform literature review (SciFinder, Web of Science) to identify established synthesis precedents within ±20% of target.
3. Design initial synthesis conditions with defined parameter space (temperature, time, precursor concentration, surfactant ratio).
4. Execute initial synthesis at 100 mg scale; document all procedural details in lab notebook.
5. Collect preliminary characterization: TEM or DLS (size), UV-Vis (if optically active), XRD (phase purity).

**[✓ Done]** criteria: Particle size within target range ±20%; single-phase XRD pattern; no visible aggregation by TEM.
**[✗ FAIL]** criteria: Polydisperse particles (σ/d > 25%); unknown XRD peaks >5% of major peak; complete aggregation in TEM — revisit nucleation conditions.

### Phase 2 — Characterization Campaign

**Steps:**
1. TEM/HRTEM: measure size histogram (N > 300 particles), verify crystal lattice spacing via FFT, check morphology.
2. XRD: identify phase, calculate Scherrer crystallite size, compare with TEM; verify no amorphous halo.
3. XPS: quantify surface elemental composition, verify oxidation states, identify ligand functional groups.
4. Spectroscopy: UV-Vis absorption (Tauc plot for E_g), PL emission (QY measurement vs standard), Raman (for graphene/CNT).
5. BET (for high-surface-area materials): N₂ adsorption isotherm, multipoint BET fit, pore size distribution.
6. Colloidal stability: DLS (hydrodynamic diameter, PDI < 0.2), zeta potential (|ζ| > 30 mV), shelf-life 30-day test.

**[✓ Done]** criteria: All six characterization modules completed; size agreement TEM vs XRD Scherrer within 30%; QY > target; zeta potential stable over 30 days.
**[✗ FAIL]** criteria: TEM-XRD discrepancy > 50% (indicates polycrystalline or amorphous shell); QY < 50% of target; PDI > 0.3 — perform surface passivation optimization.

### Phase 3 — Surface Functionalization and Application Integration

**Steps:**
1. Design surface functionalization: select ligand/molecule matching application (PEG for bio, APTES for oxide coupling, OA for organic matrix).
2. Execute functionalization protocol; monitor by FTIR (new bond appearance) and DLS (hydrodynamic size increase).
3. XPS before/after comparison to verify surface chemistry change and quantify ligand density.
4. Test application-relevant property: QY retention post-functionalization, conductivity change in graphene composite, dispersibility in target matrix.
5. Stability testing: photostability (100h under UV), thermal stability (TGA), and storage stability at target temperature.

**[✓ Done]** criteria: FTIR confirms target functional group; QY or conductivity retained > 80% of pre-functionalization value; stability test passed at application conditions.
**[✗ FAIL]** criteria: QY < 50% post-functionalization (surface quenching); DLS shows aggregation > 2× original hydrodynamic size; FTIR shows incomplete reaction — adjust pH, temperature, or ligand concentration.

### Phase 4 — Scale-Up Validation

**Steps:**
1. Scale from 100 mg to 1 g (10× step); identify and address mass-transfer and heat-dissipation changes.
2. Repeat full characterization campaign at each scale increment; compare size, QY, and purity metrics.
3. Conduct nano-risk assessment per ISO/TS 12901-2; implement engineering controls for large-scale synthesis.
4. Document scale-up procedure; establish in-process controls (temperature, pH, optical density monitoring).

**[✓ Done]** criteria: Size distribution maintained within ±15% of lab-scale target; QY within ±20% across scale; risk assessment approved; SOP finalized.
**[✗ FAIL]** criteria: Size distribution broadens > 30% vs lab scale — implement continuous flow reactor; yield drops > 40% — investigate heat/mass transfer limitation.

---

