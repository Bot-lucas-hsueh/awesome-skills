# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **No contact stabilization** | 🔴 High | Add small friction or stabilize |
| 2 | **Wrong element type** | 🔴 High | Select appropriate family |
| 3 | **Poor mesh in stress gradients** | 🔴 High | Refine in high stress regions |
| 4 | **Ignoring material nonlinearity** | 🔴 High | Use NLGEOM, proper plasticity |
| 5 | **Insufficient convergence tolerance** | 🟡 Medium | Tighten tolerances |
| 6 | **Missing boundary conditions** | 🔴 High | Review free DOFs |
| 7 | **Units inconsistency** | 🔴 High | Use consistent units |
| 8 | **No initial increment estimate** | 🟡 Medium | Specify initial increment |

## 10.2 Solver Convergence Issues

### Convergence Failures

**Symptoms**: Analysis terminates, severe discontinuity

**Common Causes & Solutions**:

| Cause | Solution |
|-------|----------|
| Unstable contact | Use contact stabilization |
| Element distortion | Refine mesh, use adaptive |
| Plastic instability | Use Riks method |
| Snap-through | Use staticriks, arc-length |
| Hourglassing (explicit) | Use hourglass control |

### Slow Convergence

**Solutions**:
1. Use automatic time stepping
2. Increase number of iterations
3. Use line search option
4. Adjust convergence criteria
5. Check for rigid body motion

### Explicit Stability

**Common Issues**:
- **Hourglass modes**: Use enhanced hourglass
- **Energy errors**: Check total energy balance
- **Penetration**: Refine contact, reduce time step
- **Mass scaling**: Use minimally, understand effect