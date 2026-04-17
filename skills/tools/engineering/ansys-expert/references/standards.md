# Standards & Reference

## 7.1 Official Documentation

- [ANSYS Help](https://ansyshelp.ansys.com/)
- [ANSYS Customer Portal](https://support.ansys.com/)
- [ANSYS Learning Hub](https://learning.ansys.com/)
- [ANSYS Developer Portal](https://developer.ansys.com/)
- [ANSYS APDL Reference](https://ansyshelp.ansys.com/public///Views/Secured/corp/v252/en/mech_object/ds_Commands_o_r.html)
- [ANSYS Workbench Guide](https://ansyshelp.ansys.com/public//Views/Secured/corp/v252/en/pdf/Workbench_Users_Guide.pdf)

## 7.2 APDL Command Reference

### Common APDL Commands

| Command | Syntax | Description |
|---------|--------|-------------|
| `/prep7` | `/prep7` | Enter preprocessor |
| `et` | `et,itype,ename` | Define element type |
| `mp` | `mp,lab,mat,co` | Define material property |
| `k` | `k,npt,x,y,z` | Create keypoint |
| `l` | `l,p1,p2` | Create line |
| `a` | `a,p1,p2,...` | Create area |
| `v` | `v,p1,p2,...` | Create volume |
| `esize` | `esize,ndiv` | Set global element size |
| `vmesh` | `vmesh,all` | Mesh volumes |
| `amesh` | `amesh,all` | Mesh areas |

### Element Types

| Element | Type | Use Case |
|---------|------|----------|
| SOLID185 | 3D Structural Solid | General 3D stress analysis |
| SOLID186 | 3D Structural Solid | Higher order |
| PLANE182 | 2D Solid | Plane strain/stress |
| BEAM188 | Beam | Beam elements |
| SHELL181 | Shell | Thin shell structures |
| LINK180 | Link | Truss elements |
| CONTACT174 | Contact | Contact analysis |

## 7.3 Material Properties

```apdl
! Steel material
mp,ex,1,200000          ! Young's modulus (MPa)
mp,prxy,1,0.3            ! Poisson's ratio
mp,dens,1,7.85e-9        ! Density (tonne/mm³)

! Aluminum
mp,ex,2,70000
mp,prxy,2,0.33
mp,dens,2,2.7e-9

! Thermal properties
mp,kxx,1,60              ! Thermal conductivity
mp,c,1,450               ! Specific heat
mp,dens,1,7850
```

## 7.4 Analysis Types

| Analysis | APDL Module | Key Commands |
|----------|-------------|-------------|
| Static Structural | `/prep7` → `/solu` | `solve` |
| Modal | `/prep7` → `/solu` | `modopt,lanb` |
| Transient | `/prep7` → `/solu` | `timint,on`, `solve` |
| Thermal | `/prep7` → `/solu` | `bfe,all,heat` |
| Buckling | `/prep7` → `/solu` | `bucopt,lanb` |

## 7.5 Version Compatibility

| ANSYS Version | Release | Key Features |
|-------------|---------|-------------|
| 2025 R2 | Current | AI-enhanced meshing |
| 2025 R1 | Supported | HPC improvements |
| 2024 R2 | Supported | Workbench enhancements |
| 2024 R1 | Supported | Cloud options |
| 2023 R1+ | Legacy | APDL scripting |

## 7.6 Solver Settings

| Parameter | Typical Value | Description |
|----------|---------------|-------------|
| `neqit` | 100-1000 | Max equilibrium iterations |
| `tolout` | 0.001 | Convergence tolerance |
| `cutcontrol` | 0.2 | Adaptive descent |
| `cnvtol` | 0.001 | Convergence criterion |
