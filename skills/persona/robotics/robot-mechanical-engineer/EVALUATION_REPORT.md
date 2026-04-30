# Skill Evaluation Report: robot-mechanical-engineer

**Evaluation Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  
**Quality Tier:** Expert ⭐ (7.6/10)

---

## 1. System Prompt Depth (Score: 9/10)

| Criterion | Assessment |
|-----------|------------|
| Role Definition | Principal Robot Mechanical Engineer with 12+ years, specific companies, 3 manipulators to production |
| Decision Framework | 5 gates: Requirements Freeze, Load Case, Material-Process Fit, Kinematic Feasibility, Safety Factor |
| Thinking Patterns | 5 patterns: Mass budget, Stiffness drives, Topology before geometry, Interface tolerance, DFM |
| Communication Style | Load cases numerically, cite material properties, MATLAB/Python formulas |

**Strengths:** Excellent mass budget allocation framework; specific ISO 9283, ISO 10218-1 references.

---

## 2. Domain Knowledge Density (Score: 9/10)

| Dimension | Evidence |
|-----------|----------|
| Frameworks | DH parameter optimization, GII (Global Isotropy Index), FEA methodology |
| Quantified Metrics | Safety factor ≥ 3.0 on yield, ωn > 30Hz for 3Hz bandwidth |
| Real Scenarios | CFRP monocoque, Al7075-T6, harmonic drive selection |

---

## 3. Workflow Actionability (Score: 6/10)

| Phase | Assessment |
|-------|------------|
| All phases | Generic template |

---

## 4. Risk Documentation (Score: 8/10)

| Risk | Severity | Quality |
|------|----------|---------|
| Incomplete load case | 🔴 Critical | Excellent - 8 standard load cases |
| FEA mesh sensitivity | 🔴 Critical | Excellent - mesh convergence |
| Material property temp | 🟡 High | Good |
| Tolerance stack-up | 🟡 High | Good - RSS method |
| CFRP anisotropy | 🟡 High | Good |
| Fastener preload | 🟢 Medium | Good |

---

## 5. Example Quality (Score: 6/10)

| Scenario | Assessment |
|----------|------------|
| All scenarios | Generic patterns |

**Missing:** No robot mechanical-specific examples (link design, FEA setup, tolerance stack-up).

---

## 6. Metadata Completeness (Score: 8/10)

| Field | Status |
|-------|--------|
| All required | ✓ Present |
| platforms | ✓ Section present |

---

## Weighted Score Calculation

```
Score = (9×0.20) + (9×0.25) + (6×0.15) + (8×0.10) + (6×0.20) + (8×0.10)
      = 1.8 + 2.25 + 0.9 + 0.8 + 1.2 + 0.8 = 7.75 → 7.6 Expert
```

---

## Summary

| Dimension | Score | Tier |
|-----------|-------|------|
| System Prompt | 9/10 | Exemplary |
| Domain Knowledge | 9/10 | Exemplary |
| Workflow | 6/10 | Community |
| Risk Docs | 8/10 | Expert |
| Examples | 6/10 | Community |
| Metadata | 8/10 | Expert |
| **Weighted** | **7.6/10** | **Expert ⭐** |

**Self-Score:** 7.8/10 (close)
