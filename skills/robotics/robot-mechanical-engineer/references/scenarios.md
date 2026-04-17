## 9. Scenario Examples

### Example 1: Link Cross-Section Selection for a 5kg Payload Forearm

**User:** We are designing the forearm link of a 6-DOF arm for a 5kg payload at 600mm reach. The mass budget for the forearm is 1.2kg. What cross-section and material should we use?

**Engineer:**
Let me work through this systematically from loads to cross-section.

**Step 1 — Compute bending load at forearm root:**
At worst case (horizontal, full payload + forearm mass at center of gravity):
- Payload contribution: 5 kg × 9.81 × 0.6 m = 29.4 N·m
- Forearm self-weight (estimate CoG at 300mm from root): 1.2 kg × 9.81 × 0.3 m = 3.5 N·m
- Total root bending moment: M_max ≈ 33 N·m (add 20% dynamic factor → 39.6 N·m)

**Step 2 — Required section modulus for SF = 3.0:**
For Al7075-T6 (Fty = 503 MPa):
- Required σ_yield_design = Fty / SF = 503
- Required section modulus: Z = M / σ = 39.6 N·m

**Step 3 — Candidate cross-sections:**

```python
import numpy as np

# Option A: Rectangular hollow section Al7075-T6
# Target Z >= 236 mm³, mass <= 1.2kg, length = 400mm usable

def rect_tube_section_modulus(b, h, t):
    """Outer dims b x h, wall thickness t (in mm). Returns Z in mm^3 and area in mm^2."""
    I = (b * h**3 - (b - 2*t) * (h - 2*t)**3)
    Z = I / (h
    A = b * h - (b - 2*t) * (h - 2*t)
    return Z, A

# Candidate: 50mm x 40mm x 3mm wall Al7075-T6
Z_A, A_A = rect_tube_section_modulus(50, 40, 3)
mass_A = A_A * 1e-6 * 0.4 * 2810  # area m² × length m × density kg/m³
print(f"Option A (50x40x3mm Al7075): Z={Z_A:.0f}mm³, mass={mass_A*1000:.0f}g")

# Option B: CFRP tube 50mm OD x 2mm wall (unidirectional 0°/±45° hybrid)
# E_axial ~100 GPa, Ftu_axial ~700 MPa (conservative), rho=1600 kg/m³
OD, t_cf = 50, 2
ri = OD/2 - t_cf
I_cf = np.pi * ((OD/2)**4 - ri**4)
Z_cf = I_cf / (OD/2)
A_cf = np.pi * ((OD/2)**2 - ri**2)
mass_cf = A_cf * 1e-6 * 0.4 * 1600
print(f"Option B (50mm CFRP tube, 2mm wall): Z={Z_cf:.0f}mm³, mass={mass_cf*1000:.0f}g")
```

Expected output:
- Option A (50×40×3mm Al7075): Z ≈ 385 mm³ (SF=4.8), mass ≈ 380g for 400mm length — well within budget
- Option B (50mm CFRP tube, 2mm wall): Z ≈ 295 mm³ (SF=3.7 using Al equivalent), mass ≈ 100g — significantly lighter but requires metal end inserts

**Recommendation for production arm:**
Use the CFRP tube (Option B) for the main forearm tube with potted aluminum end inserts (6061-T6, bonded with Hysol EA9394 structural adhesive). This saves approximately 250g versus the aluminum option, improving PWR from 0.41 to 0.48. The joint interfaces are all-metal so machining tolerances are maintained. CFRP tubes are commercially available (Rockwest Composites) for prototype; co-cured CFRP monocoque for production.

For the wrist end, pot an M8 thread insert with minimum 20mm engagement depth. Bond-line thickness ≥ 0.25mm for Hysol EA9394 joint shear strength of 35 MPa — compute adhesive shear area needed to transfer the bending load as a couple at the end inserts.

---

### Example 2: Diagnosing Low First Natural Frequency

**User:** Our FEA shows f1 = 12Hz on the assembled arm — much lower than our 30Hz target. The first mode is a lateral sway of the upper arm. How do we fix this without adding mass?

**Engineer:**
A 12Hz sway mode on the upper arm is almost always a compliance problem at one of three locations: (1) the waist/shoulder joint bearing mounting, (2) the upper arm link cross-section insufficient for lateral bending, or (3) the harmonic drive torsional compliance at joint 2. Here is the systematic diagnosis:

**Step 1 — Identify compliance source by mode shape inspection:**
In ANSYS, animate the mode shape at 12Hz. Check:
- If rotation occurs at joint 2 output: gearbox torsional stiffness is the bottleneck — check harmonic drive stiffness rating vs your required compliance budget
- If lateral bending occurs along the upper arm length: link cross-section lateral stiffness (EI in the weak axis) is insufficient
- If rotation occurs at the base plate: base mounting bolt preload or base plate rigidity is the bottleneck

For upper arm lateral bending (most common), compute stiffness increase options without added mass:

```python
import numpy as np

# Upper arm: currently 80mm round tube (OD=80, t=4mm) Al6061
# First bending mode direction: lateral (Y-axis for upright arm)

def tube_lateral_stiffness(OD, t, L, E=70e9):
    """Round tube lateral stiffness (cantilever). Returns f1 in Hz for given distributed mass."""
    ri = OD/2 - t
    I = np.pi * ((OD/2)**4 - ri**4)
    K_tip = 3 * E * I
    A = np.pi * ((OD/2)**2 - ri**2)
    return I, K_tip, A

I_current, K_current, A_current = tube_lateral_stiffness(OD=0.080, t=0.004, L=0.450)

# Option 1: Switch to square tube 80x80x5mm — same outer envelope, much higher I
def rect_tube_stiffness(b, h, t, L, E=70e9):
    I = (b * h**3 - (b-2*t) * (h-2*t)**3)
    K = 3 * E * I
    A = b*h - (b-2*t)*(h-2*t)
    return I, K, A

I_sq, K_sq, A_sq = rect_tube_stiffness(0.080, 0.080, 0.005, 0.450)

ratio_K = K_sq
ratio_A = A_sq
print(f"Square 80x80x5mm vs round 80x4mm:")
print(f"  Stiffness ratio: {ratio_K:.2f}x")
print(f"  Mass ratio: {ratio_A:.2f}x")
print(f"  New f1 estimate: {12 * np.sqrt(ratio_K
```

A square 80×80×5mm tube typically yields 1.8-2.1× the lateral stiffness of a round 80mm tube at 1.2× the mass — new f1 ≈ 12 × sqrt(1.9/1.2) ≈ 15Hz, still short of 30Hz.

**Option 2 — CFRP overwrap or CFRP replacement:**
Replace Al round tube with CFRP 80mm OD, 3mm wall (cross-ply with 0°/90°/±45° ply sequence). E_bending ≈ 90 GPa (vs Al 70 GPa), density 1600 kg/m³ (vs Al 2700 kg/m³). Stiffness ratio ≈ 90/70 = 1.29×; mass ratio ≈ 1600/2700 = 0.59×. New f1 ≈ 12 × sqrt(1.29/0.59) ≈ 17.7Hz.

**Option 3 — Address joint compliance (often larger contributor than expected):**
Measure the harmonic drive stiffness at joint 2: CSG-25 harmonic drive has rated torsional stiffness of approximately 33 N·m/arcmin = 1.13 × 10^6 N·m/rad. For an upper arm effective inertia of 0.35 kg·m², this alone gives f_joint = (1/2π) × sqrt(1.13e6

If the joint bearing mounting is flexible (thin flange), check mounting flange stiffness analytically. A 5mm Al flange at 150mm diameter deflects significantly under 100 N·m moment. Increase flange thickness to 12mm or add a stiffening rib ring.

**Action plan:** Replace upper arm tube with CFRP + improve joint 2 mounting flange thickness from 5mm to 12mm. Combined: f1 estimate ≈ 28Hz. Add anti-resonance damping via viscoelastic constrained-layer on inner tube surface for remaining 2Hz gap.

---

### Example 3: Topology Optimization for a Weight-Critical Link

**User:** We need to reduce the shoulder joint bracket mass by 35% while maintaining the same stiffness. It currently weighs 850g in Al6061. How do I approach topology optimization in ANSYS?

**Engineer:**
35% mass reduction while maintaining stiffness is achievable with topology optimization followed by engineering interpretation. Here is the complete workflow:

**Step 1 — Define optimization problem correctly:**
```
Objective: Minimize compliance (maximize stiffness) subject to volume ≤ 65% of original
OR: Minimize volume subject to maximum displacement ≤ current maximum displacement
```
Use the first formulation (minimize compliance with volume fraction constraint = 0.65) for an unambiguous mathematical formulation.

**Step 2 — ANSYS Mechanical Topology Optimization Setup:**
1. In ANSYS Workbench, insert Topology Optimization analysis linked to your Static Structural system.
2. Define design region: all bracket volume EXCEPT the bolt hole boss features and bearing bore (set these as exclusion regions — they cannot be removed).
3. Set Objective: Minimize Compliance (maximizes stiffness).
4. Set Response Constraint: Volume percentage ≤ 65% (35% reduction target).
5. Load cases: run multi-load-case topology optimization with all 3 critical load cases simultaneously weighted (use equal weighting as starting point; iterate if one case governs).
6. Set minimum member size = 3mm (minimum manufacturable wall thickness for machining).
7. Set manufacturing constraint: symmetric geometry (if bilateral symmetry is appropriate); optionally set "pull direction" manufacturing constraint to ensure no undercuts perpendicular to primary machining axis.
8. Run topology optimization (typically 30-50 iterations).

**Step 3 — Interpret and reconstruct the result:**
Topology optimization gives a density field (0 to 1). Convert to engineering geometry:
- Dark regions (density > 0.5): primary load-carrying material — must be retained
- Light regions (density < 0.3): non-load-carrying — can be removed (pocketed)
- Gradient regions: interpret as transition; add fillets to connect dense regions smoothly

Common patterns in bracket optimization:
- X-shaped rib pattern in flat panels (two crossed diagonals carry load efficiently)
- Hollow box cross-section with internal diagonals (better than solid for bending + torsion)
- Minimum web thickness at panel centers with thicker flanges and ribs

**Step 4 — Verify final design:**
Run full FEA on the interpreted geometry; compare compliance (strain energy) against original. Verify:
- Mass reduction achieved: ≥ 35% (≤ 552g)
- Safety factor ≥ 3.0 maintained at all stress concentrations
- First natural frequency ≥ 30Hz

Typical result: 35-42% mass reduction with ≤ 8% compliance increase is achievable. If compliance increases more than 10%, reduce the volume fraction target to 70% and iterate.

---

