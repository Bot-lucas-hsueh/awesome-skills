# Standard Workflow

## 8.1 Simulation Workflow

```
Phase 1: Preprocessing
├── Create/import geometry
├── Define material properties
├── Create sections (shell, solid, beam)
├── Apply loads and boundary conditions
├── Mesh geometry (seed → mesh → verify)
└── Define step and output requests

Phase 2: Solution
├── Create job
├── Select solver (Standard/Explicit)
├── Configure parallel processing
├── Submit analysis
└── Monitor messages (.msg) and status

Phase 3: Postprocessing
├── Open ODB in Viewer
├── Plot contours (stress, strain, displacement)
├── Create XY plots
├── Generate reports
└── Compare with analytical results
```

## 8.2 Model Setup Workflow

### Step 1: Geometry and Material
1. Create or import part geometry (STEP, IGES)
2. Create material definitions:
   - Elastic (Young's modulus, Poisson's ratio)
   - Plastic (yield stress vs. strain)
   - Hyperelastic (test data or strain energy)
3. Create sections and assign to geometry

### Step 2: Assembly and Mesh
1. Create assembly from parts
2. Define instance positioning
3. Apply mesh controls:
   - Element shape (tet/hex/wedge)
   - Algorithm (free, sweep, medial axis)
4. Assign element types
5. Seed and mesh

### Step 3: Loads and Steps
1. Create initial step (default)
2. Add analysis steps:
   - Static, General (nonlinear)
   - Static, Riks (staticriks)
   - Dynamic, Explicit
   - Frequency
3. Apply loads (force, pressure, thermal)
4. Apply boundary conditions
5. Define output requests (field, history)

### Step 4: Job and Solve
1. Create job with proper settings
2. Choose explicit vs. standard
3. Submit and monitor convergence
4. Review .msg file for warnings/errors

## 8.3 Validation/Verification Workflow

### Verification
- Use analytical solutions (beam bending, plate hole)
- Compare with published benchmarks
- Perform mesh convergence study
- Verify element formulation (integration points)

### Validation
- Compare with experimental data
- Quantify uncertainty
- Document model assumptions
- Check material model applicability

### Mesh Quality Checks
- Aspect ratio of elements
- Jacobian ratio
- Warpage
- Mesh sensitivity analysis