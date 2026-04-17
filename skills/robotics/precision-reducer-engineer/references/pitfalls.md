# Real-World Examples

## 10.1 Robot Joint Reducer Sizing for a 6-Axis Industrial Arm

**Scenario:** An OEM is designing a 6-axis articulated robot for welding applications. Each joint has different torque requirements. The shoulder joint requires the highest torque (650 Nm continuous, 1,800 Nm peak). Must select precision reducers for all joints while meeting cost and size constraints.

**Approach:**
1. **Kinematics & Dynamics Analysis:**
   - Build CAD model of complete robot arm (link masses, CG positions)
   - Perform inverse dynamics simulation across the full welding trajectory using MATLAB/Roboanalyzer
   - Extract torque profile for each joint: continuous torque, peak torque, peak speed, duty cycle

2. **Joint-by-Joint Reducer Selection:**

   | Joint | Continuous Torque | Peak Torque | Speed (rpm) | Selected Reducer |
   |-------|-------------------|-------------|-------------|------------------|
   | J1 (Shoulder) | 650 Nm | 1,800 Nm | 30 | RV-320N (1,960 Nm rated) |
   | J2 (Shoulder) | 580 Nm | 1,600 Nm | 30 | RV-280N (1,715 Nm rated) |
   | J3 (Elbow) | 350 Nm | 950 Nm | 45 | RV-160N (980 Nm rated) |
   | J4-6 (Wrist) | 80 Nm | 250 Nm | 60 | Harmonic SGA-35A-120 (305 Nm rated) |

3. **Key Calculations:**
   - Inertia ratio check: Target <3:1. For J1, motor rotor inertia J_m = 0.05 kg·m², reflected load inertia J_load = 0.12 kg·m². Ratio = 2.4:1 — acceptable with good servo tuning.
   - Thermal check: Shoulder joint operates at 45% of rated torque continuously. At 40°C ambient, no cooling required.
   - Mounting verification: J1 reducer output flange requires 320mm bolt circle — matches mounting interface. Confirmed.

4. **Results:** Reducers selected with 30-35% torque margin above peak. All joints meet ISO 9283 accuracy and repeatability requirements. Total reducer cost: $8,400 (within budget of $9,000).

## 10.2 Cobot Gripper Reducer Selection for Collaborative Robot

**Scenario:** A cobot (collaborative robot) OEM needs a compact, low-backlash reducer for the wrist joint of a 7kg payload cobot. The reducer must be flanged directly to the robot arm and accept the gripper mounting interface. Space is severely constrained.

**Requirements:**
- Available envelope: 120mm diameter × 80mm length max
- Continuous torque: 150 Nm
- Backlash: <3 arc-minutes (ISO 9283 Class C positioning requirement)
- IP65 rating preferred

**Approach:**
1. **Evaluate Harmonic Drive (CSF) vs. RV Mini:**
   - Harmonic CSF-25-100: 120mm dia, 77mm length, 150 Nm rated, 2 arc-min backlash, sealed option. Best fit.
   - Nabtesco RV-80N: 86mm dia but 115mm length — exceeds envelope.

2. **Thermal & Life Analysis:**
   - Gripper cycle rate: 8 cycles/minute, 60% duty cycle
   - Effective torque: 90 Nm (60% of 150 Nm)
   - Life calculation per ISO 281: L10h = (C/P)^3 × 10^6 / (60 × n) = (196/90)^3 × 10^6 / (60 × 30) = 17,200 hours
   - Cobot warranty requirement: 30,000 hours. At 90 Nm continuous, life is insufficient.

3. **Alternative Selection:**
   - Select Harmonic CSF-32-100 (larger, 220 Nm rated): L10h = 45,000 hours — meets warranty.
   - Trade-off: CSF-32 is 135mm dia × 85mm length — exceeds diameter constraint.
   - Compromise: Use CSF-25 with reduced payload derating and extended warranty from supplier (20,000 hours).

4. **Mounting Integration:**
   - Design aluminum adapter plate to interface CSF-25 to robot arm (M6 bolts, 100mm PCD)
   - Specify dual-lip seal on input and output for IP54 base rating
   - Use Flexspline with integrated output flange for direct gripper mounting

5. **Results:** Selected CSF-25-100 with adapter plate. Backlash verified at 1.8 arc-min (<3 arc-min requirement). Life at derated conditions: 24,000 hours. Accepted by OEM with 3-year extended warranty from Harmonic Drive AG.

## 10.3 Fatigue Life Calculation for a Pick-and-Place Application

**Scenario:** A high-speed pick-and-place machine uses a harmonic drive (SHD-20-100) in the wrist joint. The application requires 120 picks per minute, 20 hours per day, 6 days per week. The customer demands L10 life estimate for maintenance planning.

**Given Data:**
- Reducer: SHD-20-100, rated torque 78 Nm, rated input speed 3,500 rpm
- Application torque: 35 Nm (average), 60 Nm (peak during acceleration)
- Input speed: 600 rpm (60 picks/min × 10:1 ratio for two heads)
- Operating hours: 4,800 hours/year
- Ambient temperature: 35°C

**Approach:**
1. **Calculate Equivalent Dynamic Load (P_eq):**
   Using Miner's rule for variable load spectrum:
   - P1 = 35 Nm at 70% of cycle → 2,520 cycles/hour
   - P2 = 60 Nm at 30% of cycle → 1,080 cycles/hour
   - P_eq = [(P1^3 × 0.7 + P2^3 × 0.3)]^(1/3) = [(35³×0.7 + 60³×0.3)]^(1/3) = 44.5 Nm

2. **Basic Rating Life (ISO 281):**
   - C (rated dynamic load) = 980 Nm for SHD-20-100
   - L10 = (C/P_eq)³ × 10^6 / (60 × n_in) = (980/44.5)³ × 10^6 / (60 × 600)
   - L10 = 1,068 × 10^6 / 36,000 = 29,700 hours

3. **Temperature Correction (ISO 281):**
   - Operating temp 35°C + self-heating ~20°C = 55°C
   - Temperature factor a_T = 1.0 at 55°C (synthetic grease rating)
   - L10_modified = 29,700 × 1.0 = 29,700 hours

4. **Reliability Adjustment for 99% (not 90%):**
   - L1 = L10 × (ln(1/R) / ln(0.9)) where R = 0.99
   - L1 = 29,700 × (0.01005 / 0.10536) = 2,830 hours — this is L1 life (99% survival)

5. **Annual Maintenance Interval:**
   - L10 of 29,700 hours / 4,800 hours/year = 6.2 years to L10
   - Recommend inspection and grease replacement at 20,000 hours (~4 years)

6. **Results:** L10 life = 29,700 hours (6.2 years). Customer scheduled preventive maintenance at 20,000 hours. No unplanned failures in first 3 years of operation.

## 10.4 Replacing a Failed Harmonic Drive in a Semiconductor Wafer Robot

**Scenario:** A wafer-handling robot in a semiconductor fab has developed excessive backlash in its wrist harmonic drive after 14,000 hours of operation. The robot's positioning accuracy has degraded below the required 0.05mm repeatability. The fab needs a quick replacement with minimal downtime.

**Approach:**
1. **Diagnosis (2 hours):**
   - Measure backlash with dial indicator: 6 arc-minutes (original spec: <1 arc-min) — confirms flexspline fatigue
   - Check oil analysis: metal particles consistent with flexspline wear
   - Torque check: required 40 Nm to rotate output at no-load (original: 5 Nm) — confirms bearing wear

2. **Replacement Selection (same day):**
   - Match original part: Harmonic Drive SHG-25-100-2SO (same ratio, same interface)
   - Verify same-day availability from regional distributor
   - Order spare unit as stock (critical fab application)

3. **Installation (4 hours downtime window):**
   - Remove failed unit: clean mounting surfaces, inspect for wear on mating flanges
   - Install replacement: use new dowel pins, apply anti-seize to output shaft
   - Torque mounting bolts to spec (25 Nm, crosswise pattern)
   - Connect coupling and motor

4. **Verification (2 hours):**
   - Run-in procedure: 30% rated torque for 2 hours, 60% for 2 hours, full load for 2 hours
   - Measure backlash: 0.8 arc-min — within spec
   - Run robot calibration routine
   - Verify repeatability with laser interferometer: 0.03mm — meets 0.05mm requirement
   - Run production test wafer

5. **Results:** Total downtime: 8 hours. Replacement unit restored performance to original spec. Root cause analysis of failed unit: shock load event 3 months prior had initiated flexspline crack. Recommend adding shock absorber to gripper mount.

## 10.5 Custom RV Reducer Sizing for a Surgical Robot

**Scenario:** A medical device company is developing a 4-DOF surgical robot for minimally invasive procedures. The wrist articulation joint requires a reducer with near-zero backlash, high rigidity, and biocompatibility. Regulatory approval (FDA 510(k)) requires documented design history file (DHF) including all component selections.

**Requirements:**
- Continuous torque: 50 Nm
- Peak torque: 150 Nm (during instrument insertion)
- Backlash: <1 arc-minute
- Output flange: custom interface to instrument shaft
- Must be sterilizable (autoclave 134°C)
- Full DHF documentation for FDA submission

**Approach:**
1. **Sizing Analysis:**
   - Evaluate available options: standard RV reducers (not autoclavable), custom harmonic drives (autoclavable), strain wave with special seals
   - Select Harmonic Drive FCSG-25-100-H with custom output flange: rated torque 127 Nm (>150 Nm peak), backlash <1 arc-min, stainless steel internals

2. **Biocompatibility Verification:**
   - Confirm all internal components are SS 440C or equivalent
   - Verify lubricant is FDA-approved food-grade (Klüberfood NH1 14-402)
   - Document material certificates per ISO 10993 (biocompatibility)

3. **Thermal Analysis Under Sterilization:**
   - Autoclave cycle: 134°C for 18 minutes
   - Thermal simulation: max internal temp during cooling phase
   - Verify seal integrity after 1,000 autoclave cycles (design life)
   - Document sterilization compatibility report

4. **Regulatory Documentation:**
   - Create Design Input/Output matrices linking requirements to specifications
   - Document tolerance stack-up analysis for backlash
   - Compile test reports: torque capacity, life test, sterilization, biocompatibility
   - Prepare risk analysis (FMEA) per ISO 14971

5. **Verification Testing:**
   - Endurance test: 50 Nm continuous, 150 Nm peak at 10 cycles/min, 10 million cycles
   - Backlash measurement after every 2 million cycles — all <1 arc-min
   - Sterilization aging: 500 cycles accelerated aging equivalent to clinical life

6. **Results:** Reducer passed all tests. FDA 510(k) cleared for commercial launch. Backlash maintained at 0.7-0.9 arc-min throughout endurance test. Product launched commercially 18 months after initial sizing.
