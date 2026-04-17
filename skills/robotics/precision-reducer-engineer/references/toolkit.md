## § 6 · Professional Toolkit

### Analysis Software
- **KISSsoft / KISSsys** — Gear pair analysis, rating per AGMA 2001/ISO 6336, harmonic drive module
- **ROMAX Designer** — System-level gearbox dynamics, bearing loads, fatigue analysis
- **ANSYS Mechanical** — FEA: flexspline cup stress (≤380 MPa allowable for 17-7PH), cycloidal disc contact stress
- **MATLAB/Simulink** — Torsional stiffness nonlinearity modeling, ATE frequency analysis
- **Calyx/Klingelnberg WZG** — Cycloidal disc grinding simulation and profile correction
- **Python (SciPy, NumPy)** — Custom fatigue life integration (Miner's rule, load spectrum analysis)

### Manufacturing Equipment
- **Profile Grinding**: Klingelnberg P-series (flexspline), Gleason Phoenix (bevel gear style cycloidal discs)
- **Hobbing**: Liebherr LC series (spur stage in RV)
- **Honing**: Präwema SynchroFine (finish internal splines, Ra ≤ 0.4 μm)
- **CMM**: Zeiss CONTURA — tooth profile measurement (ISO 1328 Grade ≤6), flange runout ≤5 μm
- **Gear Analyzer**: Klingelnberg P40/P65 — pitch error, profile slope, helix deviation

### Reference Standards
- **ISO 6336** — Calculation of load capacity of spur and helical gears (σH, σF)
- **AGMA 2001-D04** — Fundamental rating factors for spur/helical gears
- **ISO 1328-1:2013** — Cylindrical gear accuracy (Grade 3–12)
- **AGMA 6133** — Materials for spur and helical gears
- **DIN 3990** — Tragfähigkeitsberechnung von Stirnrädern
- **ISO 281:2007** — Rolling bearing life calculation (L10)
- **ASTM A959

## Phase 1: Requirements & Sizing (Days 1–3)

**Input Requirements Collection:**
- [ ] Joint torque: rated torque T_r (Nm), peak torque T_p (Nm), emergency stop T_e (Nm)
- [ ] Speed: max input speed n_in (rpm), typical operating speed
- [ ] Gear ratio: i (exact or range)
- [ ] Positioning accuracy: lost-motion budget (arcmin), repeatability (±μm at end-effector)
- [ ] Service life: L10 (hours) at given duty cycle (% of rated torque)
- [ ] Environmental: temperature range, IP rating, lubrication type
- [ ] Packaging: outer diameter, length, shaft bore diameter, weight limit

**Preliminary Sizing — Harmonic Drive:**
```python
import numpy as np

def harmonic_drive_sizing(T_rated_Nm, safety_factor=1.5, ratio=100):
    """
    Select harmonic drive size based on rated torque.
    Returns minimum frame size number per Harmonic Drive SE catalog.
    """
    T_design = T_rated_Nm * safety_factor  # design torque with SF

    # HD-LW series rated average torque (Nm) by frame size
    # Source: Harmonic Drive SE HD-LW catalog 2024
    hd_catalog = {
        8:  {'T_avg': 7,   'T_peak': 22,  'T_emergency': 35,  'ratio_range': (50, 160)},
        11: {'T_avg': 18,  'T_peak': 56,  'T_emergency': 90,  'ratio_range': (50, 160)},
        14: {'T_avg': 34,  'T_peak': 114, 'T_emergency': 180, 'ratio_range': (50, 160)},
        17: {'T_avg': 56,  'T_peak': 181, 'T_emergency': 285, 'ratio_range': (50, 160)},
        20: {'T_avg': 107, 'T_peak': 309, 'T_emergency': 490, 'ratio_range': (50, 160)},
        25: {'T_avg': 163, 'T_peak': 490, 'T_emergency': 784, 'ratio_range': (50, 160)},
        32: {'T_avg': 275, 'T_peak': 853, 'T_emergency': 1372,'ratio_range': (50, 160)},
    }

    for size, specs in sorted(hd_catalog.items()):
        if specs['T_avg'] >= T_design and specs['ratio_range'][0] <= ratio <= specs['ratio_range'][1]:
            return size, specs
    return None, None

# Example: 6-DOF robot J3 joint
T_rated = 85  # Nm at output
size, specs = harmonic_drive_sizing(T_rated, safety_factor=1.5, ratio=100)
print(f"Minimum HD size: {size}, Rated avg torque: {specs['T_avg']} Nm")
# → Minimum HD size: 20, Rated avg torque: 107 Nm
```

✓ Size selected with SF ≥ 1.5
✓ Ratio within catalog range
✗ Do not select size where T_design > 0.9 × T_avg (marginal safety)

### Phase 2: Detailed Analysis (Days 4–10)

**Hertzian Contact Stress — Cycloidal Disc Pin Engagement:**
```python
def hertz_contact_stress_pin_disc(F_n, R_pin, R_disc_concave, E_pin=210e3, E_disc=210e3,
                                    nu_pin=0.3, nu_disc=0.3, contact_length=10.0):
    """
    Calculate Hertzian contact stress for pin-in-concave-disc contact (RV reducer).
    F_n: Normal force per pin (N)
    R_pin: Pin radius (mm)
    R_disc_concave: Concave radius on cycloidal disc (mm), negative for concave
    contact_length: Effective contact length (mm)
    Returns: max contact stress σH (MPa)
    """
    # Equivalent radius (convex pin + concave disc)
    # 1/R_eq = 1/R_pin - 1/R_disc  (concave disc: R_disc negative → subtract)
    R_eq = 1.0 / (1.0/R_pin - 1.0/R_disc_concave)  # R_disc_concave > R_pin for valid contact

    # Equivalent modulus
    E_eq = 1.0 / ((1 - nu_pin**2)/E_pin + (1 - nu_disc**2)/E_disc)

    # Hertz line contact (cylinder-on-cylinder formula)
    # b = sqrt(4 * F_n * R_eq
    b = np.sqrt(4 * F_n * R_eq

    p0 = 2 * F_n

    return p0, b

# RV-40C example: 8 pins, rated torque 127 Nm, eccentricity 2 mm
n_pins_engaged = 8       # typically N/2 pins engaged simultaneously
T_output = 127           # Nm
R_output = 35e-3         # m (radius to pin center)
F_per_pin = T_output
F_per_pin_N = F_per_pin * 1000  # N

sigma_H, b_mm = hertz_contact_stress_pin_disc(
    F_n=F_per_pin_N, R_pin=5.0, R_disc_concave=5.2,  # tight conformity
    contact_length=12.0
)
print(f"Contact stress: {sigma_H:.0f} MPa, Half-width: {b_mm:.3f} mm")
# Allowable: σH_allow ≤ 1500 MPa for 58-62 HRC carburized steel (ISO 6336 ZNT)
```

**Flexspline Fatigue Analysis:**
```python
def flexspline_bending_stress(M_bend, r_mean, t_wall, K_stress_concentration=1.3):
    """
    Hoop bending stress in flexspline cup wall under wave generator deflection.
    M_bend: bending moment per unit width (Nm/m) from wave generator
    r_mean: mean radius of flexspline (mm)
    t_wall: wall thickness (mm)
    Returns: peak bending stress (MPa)
    """
    # Thin-wall beam bending: σ = M * c / I, where c = t/2, I = t^3/12 per unit width
    sigma_bend = M_bend * (t_wall/2) / (t_wall**3
    return sigma_bend  # MPa

# Deflection δ of wave generator creates bending in flexspline wall
# δ = 2 * eccentricity = module * tooth_count_FS
# Typical: delta/r ≈ 0.002 (0.2% radial deflection)
# Material: 17-7PH precipitation hardened SS, σ_allow = 380 MPa (safety factor ≥ 2 on fatigue)
```

✓ Contact stress < 1500 MPa (ISO 6336 SH factor ≥ 1.2)
✓ Flexspline bending < 380 MPa (σ_allow 17-7PH at 10^7 cycles)
✓ L10 life ≥ 20,000 hours at rated torque
✗ Avoid T_applied > T_peak even momentarily (catastrophic fracture risk)

### Phase 3: Manufacturing & Validation (Days 11–20)

**Tooth Profile Inspection Criteria:**
```python
# ISO 1328-1 Grade 5 tolerance limits (typical for precision reducers)
# Module m = 0.5 mm (harmonic drive), pitch diameter d = 50 mm
def iso1328_tolerances(module_mm, pitch_diameter_mm, grade=5):
    """
    Calculate ISO 1328-1 gear accuracy tolerances.
    Returns dict of tolerances in μm.
    """
    m = module_mm
    d = pitch_diameter_mm

    # Base tolerance factor f_pt (single pitch deviation)
    f_pt = (0.3 * (m + 0.4 * np.sqrt(d)) + 4) * np.sqrt(2)**(grade-5) * 1.0

    # Profile total deviation F_alpha
    F_alpha = (3.2 * np.sqrt(m) + 0.22 * np.sqrt(d) + 0.7) * np.sqrt(2)**(grade-5)

    # Helix total deviation F_beta (for helical; = 0 for harmonic spur)
    F_beta = (0.1 * np.sqrt(d) + 0.63 * np.sqrt(10) + 4.2) * np.sqrt(2)**(grade-5)

    return {'f_pt': round(f_pt, 1), 'F_alpha': round(F_alpha, 1), 'F_beta': round(F_beta, 1)}

tol = iso1328_tolerances(module_mm=0.5, pitch_diameter_mm=50, grade=5)
print(f"Grade 5 tolerances: f_pt={tol['f_pt']}μm, F_alpha={tol['F_alpha']}μm")
# → f_pt ≈ 3.5 μm, F_alpha ≈ 4.8 μm
```

**Process Control — Cpk Requirement:**
- Grinding center distance Cpk ≥ 1.33 (4σ process capability)
- Cycloidal disc eccentricity Cpk ≥ 1.67 (5σ for critical dimension)
- Roundness (circularity) of wave generator bearing race ≤ 1 μm

✓ CMM inspection 100% on cycloidal discs
✓ Gear analyzer sampling 5% on harmonic drive flexsplines
✓ Assembly torque-angle signature recorded and archived
✗ No skip on final backlash/lost-motion test before shipping

## 🔬 Scenario Examples

### 🚫 Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: Selecting Reducer at 100% Rated Average Torque
**Wrong:** T_applied = T_avg_rated → "meets spec"
**Why it fails:** Rated life (L10) is at T_avg_rated. Even 10% overload reduces life by ~33% (life ∝ T^-3). Duty cycle peaks easily cause 1.2–1.5× rated torque.
**Correct:** Apply service factor Ks ≥ 1.5 for robot joints with shock loads. Size to T_design = T_rated × Ks ≤ T_avg_catalog.

### Anti-Pattern 2: Ignoring Thermal Derating
**Wrong:** Operating HD-20 at rated torque in T_ambient = 60°C enclosure without derating.
**Why it fails:** Grease viscosity drops ~50% per 15°C above reference (40°C). Film thickness → EHD failure → surface pitting within 1,000 hours.
**Correct:** Derate rated torque by 10% per 10°C above 40°C, OR use high-viscosity grease (SK-2 instead of SK-1A), OR add forced air cooling to maintain T_housing ≤ 60°C.

### Anti-Pattern 3: Linear Stiffness Assumption in Control Model
**Wrong:** Using K_stiffness = K_max (catalog max value) for all deflection angles in servo controller.
**Why it fails:** Actual stiffness at small deflections (< 1 arcmin) is 5–10× lower. This causes servo oscillation or position error > 1 arcmin under load.
**Correct:** Implement three-region nonlinear stiffness model (K1/K2/K3) or use measured torque-angle curve; add feedforward load torque compensation.

### Anti-Pattern 4: Reusing Grease Without Flushing After Contamination
**Wrong:** Topping up grease after water ingress without complete flush and refill.
**Why it fails:** Water contamination accelerates corrosive wear by 10–50× (fretting corrosion on flexspline). Mixing old and new grease may form soap incompatibilities.
**Correct:** Full disassembly, ultrasonic cleaning of all parts, inspection for corrosion pitting (reject if pits > 0.1 mm depth), complete refill with correct grease type and quantity.

### Anti-Pattern 5: Specifying Backlash Without Lost-Motion Distinction
**Wrong:** Specifying "backlash ≤ 1 arcmin" — harmonic drives have zero backlash but non-zero lost-motion.
**Why it fails:** Harmonic drives have zero mechanical backlash (continuous tooth engagement) but exhibit lost-motion (±0.5–2 arcmin) from elastic hysteresis of flexspline. These are different phenomena requiring different test methods.
**Correct:** Specify both: backlash (AGMA 2010 test, ±direction reversal) AND lost-motion (ISO 9283 test: deadband at zero load crossing). Typical HD-LW: backlash = 0, lost-motion ≤ ±1 arcmin.

