# Standard Workflow

## 8.1 Simulation Workflow

```
Phase 1: Preprocessing
├── Import geometry (STL, STEP, OBJ)
├── Create mesh (blockMesh → snappyHexMesh)
├── Check mesh quality (checkMesh)
├── Set boundary conditions
├── Configure physical models
└── Define solver settings

Phase 2: Solution
├── Decompose domain (decomposePar)
├── Initialize fields (setFields, patchIntegrate)
├── Run solver (mpirun -np N solver)
├── Monitor convergence (foamLog, log files)
└── Reconstruct results (reconstructPar)

Phase 3: Postprocessing
├── Visualize (paraFoam, ParaView)
├── Extract data (sample, probe)
├── Calculate quantities (integral, forces)
├── Generate reports
└── Validate against experimental data
```

## 8.2 Model Setup Workflow

### Step 1: Geometry Preparation
1. Export CAD geometry as STL (triangulated)
2. Ensure watertight, manifold geometry
3. Apply scale factor if needed (units)
4. Define refinement surfaces/hierarchies

### Step 2: Mesh Generation
1. Create `system/blockMeshDict` for base mesh
2. Define cell zones and refinement regions
3. Configure `system/snappyHexMeshDict`:
   - locationInMesh (seed point)
   - refinement surfaces
   - layer addition settings
4. Run `checkMesh` - resolve any errors

### Step 3: Physics Setup
1. Copy template case (e.g., pitzDaily)
2. Edit `0/` directory - initial/boundary fields
3. Edit `constant/` - transport, turbulence
4. Edit `system/` - fvSolution, fvSchemes
5. Configure residual control in controlDict

### Step 4: Solver Execution
1. Decompose with `decomposePar`
2. Run with proper parallel launch:
   ```bash
   mpirun -np 8 simpleFoam -parallel > log.simpleFoam &
   ```
3. Monitor with `foamLog` or tail residual files
4. Reconstruct with `reconstructPar`

## 8.3 Validation/Verification Workflow

### Verification (Code Verification)
- Compare against analytical solutions
- Use method of manufactured solutions (MMS)
- Check grid convergence (GCI study)
- Verify temporal convergence

### Validation (Experimental Validation)
- Compare against wind tunnel data
- Compare against benchmark cases (ERCOFTAC, NASA)
- Quantify uncertainty (V&V framework)
- Document validation database

### Mesh Quality Metrics
- Aspect ratio (< 100 for viscous layers)
- Skewness (< 0.5 for hex cells)
- Non-orthogonality (< 70°)
- Jacobian determinant (> 0.3)