# Standards & Reference

## 7.1 Official Documentation

- [COMSOL Documentation](https://www.comsol.com/documentation) - Official documentation portal
- [COMSOL Multiphysics](https://www.comsol.com/multiphysics) - Product overview
- [COMSOL Blog](https://www.comsol.com/blogs) - Tutorials and application notes
- [COMSOL Learning Center](https://www.comsol.com/cms) - Training resources

## 7.2 Configuration Reference

### Physics Interfaces

| Physics | Interface | Application |
|---------|-----------|-------------|
| Structural | Solid Mechanics | Linear/nonlinear FEA |
| Thermal | Heat Transfer | Conduction, convection |
| Fluid | CFD Module | Laminar/turbulent flow |
| Electromagnetic | AC/DC, RF, Wave | EM simulation |
| Chemical | Chemical Reaction Engineering | Reactors, diffusion |
| Acoustics | Acoustic Module | Fluid-structure interaction |

### Study Types

| Study | Use Case |
|-------|----------|
| Stationary | Steady-state analysis |
| Time Dependent | Transient simulation |
| Eigenfrequency | Modal analysis |
| Frequency Domain | Harmonic response |
| Parameteric Sweep | Design optimization |
| Optimization | Shape/size optimization |

### Solver Settings

```javascript
// Solver configuration
solver.sittings('time dependent'):
    // Time stepping
    tlist = range(0, 0.01, 1)
    // Adaptive time stepping
    'time': {'tsteps': 'adaptive'}
    // Linear solver
    'linear': {'solver': 'gmres', 'preconditioner': 'sor'}
```

## 7.3 Common Commands

### Model Manipulation

| Command | Description |
|---------|-------------|
| `model.param.set()` | Set parameter values |
| `model.geom.create()` | Create geometry |
| `model.physics.create()` | Add physics interface |
| `model.mesh.create()` | Generate mesh |
| `model.study.create()` | Define study |
| `model.result.create()` | Post-processing |

### Job Submission

| Command | Description |
|---------|-------------|
| `model.run` | Run study |
| `model.run('param')` | Parametric sweep |
| `model.batch()` | Batch job |
| `mphrun` | Command-line run |

### Java/LiveLink

| Command | Description |
|---------|-------------|
| `model.java()` | Export to Java |
| `mphserver` | MATLAB LiveLink server |
| `model.mleval()` | MATLAB expression |

## 7.4 Version Compatibility

| Version | Status | Notes |
|---------|--------|-------|
| COMSOL 5.5 | Supported | LTS |
| COMSOL 5.6 | Supported | Enhanced UI |
| COMSOL 5.7 | Supported | New physics |
| COMSOL 6.0 | Supported | Major release |
| COMSOL 6.1 | Current | Latest stable |
| COMSOL 6.2 | Latest | New features |

### API Changes

- **6.0+**: New Java API organization
- **6.1+**: Enhanced optimization module
- **6.2+**: Cloud computing support