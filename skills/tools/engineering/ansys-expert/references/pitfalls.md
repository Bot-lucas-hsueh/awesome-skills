# Common Pitfalls & Anti-Patterns

## 10.1 Common APDL Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | Forgetting `/prep7` before meshing | 🔴 High | Always include in scripts |
| 2 | Wrong element type for analysis | 🔴 High | Verify element in docs |
| 3 | Inadequate mesh density | 🔴 High | Mesh convergence study |
| 4 | Missing boundary conditions | 🔴 High | Always check for rigid body motion |
| 5 | Units inconsistency | 🔴 High | Document units, stay consistent |
| 6 | Large deflection effects ignored | 🟡 Medium | Use NLGEOM,ON for large deflections |
| 7 | Contact definition errors | 🔴 High | Verify contact surfaces |
| 8 | Solver divergence | 🟡 Medium | Check load magnitudes |

## 10.2 Anti-Patterns

### Geometry Anti-Patterns

```
❌ Using primitives for complex geometry
   - Boolean operations can fail
   - Complex cleanup needed

✅ Build parametric geometry
   - Use keypoints and lines
   - Import CAD for complex parts
```

### Mesh Anti-Patterns

```
❌ Coarse mesh everywhere
   - Results may be inaccurate
   - Missing stress concentrations

✅ Mesh refinement at critical areas
   - Use local mesh controls
   - Conduct convergence study
```

## 10.3 Convergence Issues

| Issue | Solution |
|--------|----------|
| Solution diverges | Reduce load magnitude, check BCs |
| Negative eigenvalues | Check for insufficient constraints |
| Large deflections | Enable NLGEOM |
| Contact convergence | Adjust contact settings |

## 10.4 Best Practices

```
APDL Scripting:
□ Always document units
□ Use parametric variables
□ Modularize with *do loops
□ Check solver output for warnings
□ Save results with meaningful names

Analysis:
□ Conduct mesh convergence study
□ Verify BCs allow realistic behavior
□ Compare with hand calculations
□ Document assumptions
```
