# Scenario Examples

## 9.1 Engineering Scenarios

### External Aerodynamics

**User:** "How to simulate a car exterior flow?"

**Expert:**
> **Setup for Automotive External Flow:**
>
> 1. **Mesh**: Use snappyHexMesh with:
>    - Car surface refinement (level 3-4)
>    - Wake refinement box
>    - Prism layers (10-15 layers, y+ ~30)
>
> 2. **Physics**: simpleFoam with:
>    - k-ε or SST k-ω turbulence
>    - symmetry on sides, slip on ground
>    - inlet velocity ~30-50 m/s
>
> 3. **Convergence**: Aim for residuals < 1e-5

### Turbo machinery

**User:** "How to set up a centrifugal pump simulation?"

**Expert:**
> **MRF vs. Transient:**
>
> - **MRF (Multiple Reference Frame)**: steady-state, faster
>   - Define `constant/MRFProperties`
>   - Set RPM and rotation axis
>   - Use simpleFoam with MRF
>
> - **Transient (Sliding Mesh)**: accurate, captures unsteady
>   - Use AMI (Arbitrary Mesh Interface)
>   - Run pisoFoam/transientSimpleFoam
>   - Need ~10+ revolutions for statistical average

### Multi phase Flow

**User:** "How to simulate a dam break?"

**Expert:**
> **InterFoam Setup:**
>
> 1. **Initial condition**: Use setFields to define water region
> 2. **Alpha fields**: alpha.water (0 = air, 1 = water)
> 3. **Properties**: Define surface tension and viscosity
> 4. **Schemes**: Use `vanLeer` or `limitedLinear` for alpha
> 5. **Solver**: interFoam with PISO

## 9.2 Industry Applications

| Industry | Application | Typical Solver |
|----------|-------------|----------------|
| Automotive | Exterior aerodynamics | simpleFoam |
| Aerospace | Turbomachinery | rhoSimpleFoam |
| Marine | Ship resistance | interFoam |
| Energy | Wind turbine wakes | actuatorDisk |
| Chemical | Reacting flows | reactingFoam |
| Civil | Wind on structures | simpleFoam |
| Biomedical | Blood flow | icoFoam |

## 9.3 Automation

### Python Script Example

```python
import subprocess
import os

def run_openfoam_case(case_dir, solver, n_procs=4):
    """Run OpenFOAM case with automation."""
    os.chdir(case_dir)
    
    # Decompose
    subprocess.run(["decomposePar"], check=True)
    
    # Run parallel
    subprocess.run([
        "mpirun", "-np", str(n_procs),
        solver, "-parallel"
    ], check=True)
    
    # Reconstruct
    subprocess.run(["reconstructPar"], check=True)
```

### Batch Processing

```bash
#!/bin/bash
# Run parametric studies

for angle in 0 5 10 15 20; do
    cp -r template_case case_$angle
    sed -i "s/ANGLE/$angle/" case_$angle/0/U
    cd case_$angle
    blockMesh && snappyHexMesh -overwrite && simpleFoam
    cd ..
done
```