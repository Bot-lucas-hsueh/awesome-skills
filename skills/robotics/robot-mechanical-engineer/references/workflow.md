## 8. Standard Workflow

### Phase 1 — Requirements Definition and Preliminary Sizing

**Steps:**
1. Freeze requirements: payload (kg), TCP reach (mm), orientation workspace (degrees), cycle time (s), mass budget (kg), IP rating, operating temperature, mounting (floor/ceiling/wall).
2. Enumerate load cases: rated static, rated dynamic (acceleration and deceleration), e-stop deceleration (estimate as 3× rated torque), maximum reach with full payload, worst-case combined (payload + acceleration + gravity).
3. Compute joint torques analytically for each load case using free-body diagram approach; include link mass contribution from mass allocation budget.
4. Preliminary actuator sizing: select gearbox ratio and motor frame size for each joint based on required peak torque with 20% margin over e-stop load case.
5. Allocate mass budget per sub-assembly; verify total robot mass meets target ± 10%.

**[✓ Done]** criteria: All load cases documented in an FMEA-style table with numerical values; preliminary joint torques computed and actuators selected; mass allocation sheet shows total within budget.

**[✗ FAIL]** criteria: Any load case without a numerical torque value; mass budget exceeding target by more than 15% — must redesign kinematic chain or reduce payload specification before continuing.

### Phase 2 — Kinematic Chain Design and Workspace Analysis

**Steps:**
1. Set up DH parameter table for the proposed kinematic configuration; include joint limits based on mechanical stops.
2. Plot workspace reachability using forward kinematics sweep across all joint combinations; verify required task workspace fits within robot reachability.
3. Compute Global Isotropy Index (GII) across workspace; identify regions with poor dexterity (GII < 0.2); adjust DH offsets or link lengths to improve dexterity in task-critical regions.
4. Perform singularity analysis: identify wrist singularity (axes 4-5-6 align), elbow singularity (arm fully extended), and shoulder singularity (axis 1 and 4 align); verify task trajectories avoid singular zones with ≥ 10° margin.
5. Update DH parameters in MATLAB/Python model to validate kinematics numerically before committing to CAD.

**[✓ Done]** criteria: Reachability map confirms full task workspace covered; GII > 0.3 in primary task volume; no singularity within 10° of planned trajectories; DH parameter table finalized and versioned.

**[✗ FAIL]** criteria: Task workspace partially outside reachable volume — extend link length or adjust joint limits. GII < 0.15 in task volume — redesign link lengths. Singularity within 5° of planned path — restructure trajectory or change kinematic configuration.

### Phase 3 — Structural Design and FEA Validation

**Steps:**
1. Develop link cross-sections: for primary load-bearing links, use topological optimization in ANSYS (Density method, 30% volume retention target) to find load path; translate result into manufacturable geometry (round tubes, I-sections, box sections, or CFRP shells).
2. Build FEA model in ANSYS Mechanical: import SolidWorks geometry via Parasolid; define material properties (Al7075-T6: Fty = 503 MPa, E = 71.7 GPa, ρ = 2.81 g/cm³); apply boundary conditions (fixed at base, force at flange for each load case).
3. Perform mesh convergence: start with element size = 0.1 × smallest feature; refine at fillets, holes, and contact regions until peak stress changes < 5% between refinements.
4. Run static analysis for all load cases; extract safety factor contour map; identify regions below SF = 3.0.
5. Run modal analysis: extract first 10 natural frequencies; verify f1 > 30Hz; identify mode shapes that correspond to control-relevant deformation modes.
6. Run fatigue analysis using nCode integration (if ANSYS nCode available) or manually from S-N curve: compute stress amplitude at critical locations; verify N > 10^7 cycles at rated load.
7. Redesign any under-strength features (add material, increase fillet radii, add gussets) and re-run FEA until all criteria met.

**[✓ Done]** criteria: All load cases show SF_yield ≥ 3.0 throughout structure; first natural frequency f1 ≥ 30Hz; fatigue life ≥ 10^7 cycles at rated amplitude; tip deflection ≤ 0.5mm at rated load and reach.

**[✗ FAIL]** criteria: Any region with SF < 2.5 must be redesigned before continuing. f1 < 20Hz requires mass reduction or stiffness increase. Fatigue life < 10^6 cycles at rated load is a disqualifying failure.

### Phase 4 — Joint Mechanism Design and DFM Review

**Steps:**
1. Select reducer type per joint: harmonic drive for joints 4-6 (high ratio, compact, zero backlash); RV or cycloidal for joints 1-3 (high shock resistance, higher rated torque, moderate backlash < 1 arcmin).
2. Design bearing arrangement: crossed-roller bearing for output flanges requiring moment load capacity; angular contact pair (face-to-face) for shaft supports under combined radial and axial loads. Compute bearing life L10 = (C/P)^3 × 10^6 revolutions; target L10 > 20,000h.
3. Specify all tolerances on joint interface features (output flange bore, shaft journals, encoder mounting). Perform 1D tolerance stack-up for concentricity of bearing bore to output flange face; target < 0.005mm TIR.
4. Define sealing strategy: for IP67 joints, use dual-lip dynamic radial seal on rotary shaft plus labyrinth drainage feature; static O-ring seals on all cover interfaces; verify seal compatibility with lubricant type.
5. Conduct DFM review: verify minimum wall thickness ≥ 2.5mm for machined Al, ≥ 1.5mm for Ti; all tapped holes depth ≥ 1.5×D; machining datums clearly defined; no internal undercuts requiring 5-axis or EDM without explicit approval.
6. Issue first-article inspection plan: define all critical dimensions to be measured on first 3 parts; compare against tolerance stack-up targets.

**[✓ Done]** criteria: All bearings show L10 > 20,000h; IP67 seal design validated by standard IP ingress protection test plan; DFM review sign-off from manufacturing engineer; first-article inspection plan issued.

**[✗ FAIL]** criteria: L10 < 10,000h requires bearing size increase or load reduction. Sealing design leaks in IP test simulation — redesign seal groove geometry. Wall thickness below minimum DFM requirement — add material or change material to Al7075 from Al6061 for strength retention at thinner section.

---

