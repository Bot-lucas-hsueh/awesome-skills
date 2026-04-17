# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **Incompatible meshes** | 🔴 High | Use coupled physics mesh |
| 2 | **Missing boundary conditions** | 🔴 High | Check all domains/boundaries |
| 3 | **Wrong element order** | 🔴 High | Adjust in physics settings |
| 4 | **Unit inconsistency** | 🔴 High | Verify all parameters |
| 5 | **Poor mesh in gradients** | 🔴 High | Add local mesh refinement |
| 6 | **Non-convergent coupling** | 🔴 High | Adjust coupling iteration |
| 7 | **Singular matrix** | 🔴 High | Check BCs, constraints |
| 8 | **Time step too large** | 🔴 High | Reduce initial step size |

## 10.2 Solver Convergence Issues

### Convergence Failures

**Symptoms**: Solver fails to converge, error messages

**Common Causes & Solutions**:

| Cause | Solution |
|-------|----------|
| Singular matrix | Check BCs, constraints, loads |
| Poor mesh quality | Refine mesh, improve elements |
| Nonlinear instability | Use damping, reduce step |
| Contact separation | Adjust contact settings |
| Time step too large | Reduce initial step |

### Slow Convergence

**Solutions**:
1. Use fully coupled instead of segregated
2. Adjust relaxation factors
3. Increase nonlinear iterations
4. Use better preconditioner
5. Check scaling of variables

### Multiphysics Stability

**Tips**:
- Start with single physics
- Add couplings incrementally
- Use proper coupling iterations
- Consider steady-state for initial guess