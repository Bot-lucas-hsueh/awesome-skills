# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **Poor mesh quality** | 🔴 High | Run checkMesh, refine/adjust |
| 2 | **Wrong boundary conditions** | 🔴 High | Verify patch types match physics |
| 3 | **Ignoring y+ for turbulence** | 🔴 High | Calculate first cell height |
| 4 | **Using steady solver for transient** | 🔴 High | Use pisoFoam/interFoam |
| 5 | **No residual monitoring** | 🟡 Medium | Use foamLog, set writeInterval |
| 6 | **Wrong units in CAD** | 🔴 High | Check STL scaling, use m |
| 7 | **Non-manifold geometry** | 🔴 High | Repair STL in Blender/MeshLab |
| 8 | **Overlapping patches** | 🔴 High | Use createPatch to fix |

## 10.2 Solver Convergence Issues

### Divergence

**Symptoms**: Residuals increase, NaN in fields

**Common Causes & Solutions**:

| Cause | Solution |
|-------|----------|
| High Reynolds number | Use lower relaxation factors |
| Timestep too large | Reduce deltaT |
| Poor mesh | Improve quality, check skewness |
| Wrong schemes | Use upwind for stability |
| Pressure-velocity coupling | Use PISO/SIMPLE correctly |

### Slow Convergence

**Symptoms**: Residuals plateau, not decreasing

**Solutions**:
1. Decrease under-relaxation factors
2. Increase mesh resolution in high-gradient regions
3. Improve initial field (potentialFoam)
4. Use better discretization schemes (second-order)
5. Check for recirculation zones (need transient)

## 10.3 Unit Consistency

| Quantity | SI Unit | Common Error |
|----------|---------|--------------|
| Length | m | mm → must scale STL |
| Velocity | m/s | Using rpm without conversion |
| Pressure | Pa | Using atm/bar without conversion |
| Viscosity | m²/s | Using centiStokes |
| Density | kg/m³ | g/cm³ without conversion |

## 10.4 Mesh Quality Checks

```bash
# Run these checks
checkMesh > log.checkMesh

# Acceptable ranges:
# - Max aspect ratio: < 100
# - Max skewness: < 4 (hex), < 1 (tet)
# - Max non-orthogonality: < 70°
# - Min determinant: > 0.001
# - Max non-orthogonality: < 65 for prisms
```