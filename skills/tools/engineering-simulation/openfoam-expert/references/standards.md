# Standards & Reference

## 7.1 Official Documentation

- [OpenFOAM Documentation](https://www.openfoam.com/documentation) - Official user guide and solver documentation
- [OpenFOAM v2312 Release Notes](https://www.openfoam.com/news/maintenance/v2312) - Latest release features and changes
- [OpenFOAM Wiki](https://wiki.openfoam.org/) - Community-contributed tutorials and guides
- [CFD Direct](https://cfdirect.co.uk/) - OpenFOAM consulting and training resources

## 7.2 Configuration Reference

### Solver Selection

| Application | Solver | Use Case |
|-------------|--------|----------|
| Incompressible | `simpleFoam` | Steady-state RANS |
| Incompressible | `pisoFoam` | Transient RANS |
| Incompressible | `icoFoam` | Transient laminar |
| Compressible | `rhoSimpleFoam` | Steady supersonic |
| Compressible | `rhoPisoFoam` | Transient compressible |
| Multiphase | `interFoam` | Free surface (VOF) |
| Multiphase | `multiphaseInterFoam` | Multiple phases |
| Combustion | `reactingFoam` | Premixed/non-premixed |
| Particles | `reactingParcelFoam` | Lagrangian particles |

### Boundary Conditions

```
/0/U
{
    type            fixedValue;
    value           uniform (10 0 0);
}

/0/p
{
    type            zeroGradient;
}

/constant/turbulenceProperties
{
    simulationType  RAS;
    RAS             kEpsilon;
}
```

### Material Properties (transportProperties)

```
transportModel  Newtonian;

nu              1e-05;  // kinematic viscosity [m²/s]
rho             1000;   // density [kg/m³]
```

## 7.3 Common Commands

### Mesh Generation

| Command | Description |
|---------|-------------|
| `blockMesh` | Generate mesh from blockMeshDict |
| `snappyHexMesh` | Generate hex-dominant mesh from STL |
| `cfMesh` | Generate cartesian/hex mesh |
| `checkMesh` | Validate mesh quality |
| `topoSet` | Modify cell/face sets |
| `createPatch` | Create patches from existing faces |

### Simulation Control

| Command | Description |
|---------|-------------|
| `decomposePar` | Decompose mesh for parallel |
| `mpirun -np 8 solver` | Run parallel simulation |
| `reconstructPar` | Reconstruct decomposed results |
| `foamLog` | Monitor convergence |
| `sample` | Extract field data along lines/surfaces |

### Post-Processing

| Command | Description |
|---------|-------------|
| `paraFoam` | Open ParaView for visualization |
| `foamToVTK` | Convert to VTK format |
| `calcEnum` | Calculate field statistics |
| `patchIntegrate` | Integrate flow on patches |

## 7.4 Version Compatibility

| Version | Status | Notes |
|---------|--------|-------|
| v7 (2020) | Supported | LTS, stable APIs |
| v8 (2021) | Supported | Improved AMR |
| v9 (2022) | Supported | New turbulence models |
| v10 (2023) | Supported | Enhanced Python binding |
| v2312 (2023) | Current | Recommended for new projects |
| v2406 (2024) | Latest | Current stable release |

### Key API Changes

- **v8+**: `fvOptions` replaces old forcing mechanisms
- **v9+**: New `immersedBoundary` framework
- **v10+**: Enhanced `pyFoam` utilities
- **v2312+**: Native GPU support (limited solvers)