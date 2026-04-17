## 10. Common Pitfalls & Anti-Patterns

### Anti-Pattern 1: FEA Without Mesh Convergence Study

**Why it matters:** Default automatic meshing in SolidWorks Simulation or ANSYS produces element sizes that may be 5-10× too large at stress concentrations (fillets, holes, notches), underestimating peak stress by 40-60%.

❌ BAD:
```
Run static FEA with default mesh → peak von Mises = 120 MPa → SF = 503/120 = 4.2 → conclude safe
```

✅ GOOD:
```
Convergence study at critical fillet (R=3mm on shoulder bracket):
  Element size 3mm: σ_peak = 148 MPa, SF = 3.4
  Element size 1mm: σ_peak = 187 MPa, SF = 2.7
  Element size 0.5mm: σ_peak = 198 MPa, SF = 2.5
  Element size 0.25mm: σ_peak = 201 MPa, SF = 2.5
  → Converged at 0.5mm; SF = 2.5 < 3.0 → fillet must be enlarged to R = 5mm
```

---

### Anti-Pattern 2: Ignoring Fastener Preload in Structural Model

**Why it matters:** Bolted flanges in compression (under preload) have effectively infinite stiffness in the joint. Without proper preload modeling, FEA assumes a perfectly bonded interface — but in reality, joints separate when external moment exceeds preload moment, creating nonlinear compliance at the interface.

❌ BAD:
```python
# Simply bonding all contact surfaces in FEA — overestimates stiffness by 2-5x at bolted flanges
contact_type = "bonded"  # Assumes infinite preload
```

✅ GOOD:
```python
# Use Frictional contact at flange mating faces; add bolt pretension elements
# Bolt M12-12.9 (μ=0.15 dry): pretension = 0.7 × Fp = 0.7 × 68,000N = 47,600N
contact_type = "frictional"  # friction coefficient = 0.15 for dry steel/Al
bolt_pretension = 47600  # N per M12-12.9 bolt
# Check that contact pressure remains > 0 under all load cases (no separation)
# If separation detected → add more bolts or increase bolt size
```

---

### Anti-Pattern 3: Specifying CFRP Stiffness Without Ply Orientation

**Why it matters:** CFRP stiffness varies by factor of 10 depending on ply angle. A tube specified as "CFRP" with 90° fibers has nearly zero axial stiffness. Design documents must specify fiber orientation, ply count, and lay-up sequence.

❌ BAD:
```
Material: CFRP, E = 130 GPa  ← What direction? 0°, 90°, ±45°?
```

✅ GOOD:
```
Material: CFRP unidirectional prepreg (Toray T700/epoxy, Vf = 0.60)
Lay-up: [0°/±45°/90°/±45°/0°]s  (symmetric, quasi-isotropic)
E_axial (0°): 135 GPa; E_transverse (90°): 8.5 GPa
G_12: 4.5 GPa; ν_12: 0.28; ρ: 1580 kg/m³
Use CLT (Classical Laminate Theory) to compute [A,B,D] stiffness matrices for
actual loading combination (bending + torsion + axial).
```

---

### Anti-Pattern 4: Workspace Analysis with Only End-Effector Reachability

**Why it matters:** End-effector reachability (position only) is necessary but insufficient. Many positions in the positional workspace cannot be reached with all required end-effector orientations (full SE(3) dexterity). A robot that can reach a position only in a single arm configuration is nearly useless for manipulation tasks.

❌ BAD:
```python
# Check only that TCP position is within reach
reachable = np.linalg.norm(tcp_pos) <= max_reach
```

✅ GOOD:
```python
import roboticstoolbox as rtb
import numpy as np

robot = rtb.models.DH.Panda()  # or custom DH model

def check_dexterous_reach(robot, target_pos, target_orientations):
    """Check that position is reachable with ALL required orientations."""
    results = {}
    for orient_name, R in target_orientations.items():
        T = np.eye(4)
        T[:3,:3] = R
        T[:3,3] = target_pos
        sol = robot.ikine_LM(T, q0=robot.qz)  # Levenberg-Marquardt IK
        results[orient_name] = sol.success
    # Point is dexterous only if all orientations are reachable
    return all(results.values()), results

# Test 6 canonical orientations at each workspace grid point
canonical_orientations = {
    'tool_down': np.array([[1,0,0],[0,-1,0],[0,0,-1]]),
    'tool_horizontal_x': np.eye(3),
    'tool_horizontal_y': np.array([[0,1,0],[-1,0,0],[0,0,1]]),
    # ... add all required task orientations
}
```

---

### Anti-Pattern 5: No Thermal Derating in Material Properties

**Why it matters:** Robot joint housings around direct-drive or SEA actuators reach 60-90°C during sustained operation. Al7075-T6 yield strength decreases from 503 MPa at room temperature to approximately 430 MPa at 100°C — a 15% reduction that pushes a design with SF = 3.0 down to SF = 2.55, below the required minimum.

❌ BAD:
```
FEA uses: Al7075-T6 Fty = 503 MPa (room temperature)
Operating temperature: 80°C during continuous duty
Result: Actual SF = 2.7 × (430/503) = 2.3 — UNSAFE
```

✅ GOOD:
```
Step 1: Measure housing temperature after 2h continuous duty cycle
Step 2: Apply temperature correction factor from MIL-HDBK-5 Figure 3.7.1.0(b)
        At 80°C: Fty_corrected = 503 × 0.88 = 443 MPa
Step 3: Rerun FEA with Fty = 443 MPa for joint housing components
Step 4: Verify SF ≥ 3.0 at operating temperature, not just room temperature
Step 5: For components above 100°C, consider Al2024-T4 (better elevated temperature
        strength) or 17-4PH stainless steel for joint housings
```

---

