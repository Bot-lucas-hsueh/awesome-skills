# Skill Evaluation Report — systems-engineer

## Metadata
| Field | Value |
|-------|-------|
| **name** | systems-engineer |
| **version** | 2.0.0 |
| **difficulty** | expert |
| **category** | aerospace |
| **current_score** | 9.5/10 (self-reported) |

---

## 6-Dimension Scoring

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| **System Prompt Depth** | 20% | 9/10 | Strong identity (INCOSE CSEP/ASEP), professional DNA (Requirements Architect, Integration Manager, V&V Leader, Risk Manager). V-Model framework included. |
| **Domain Knowledge Density** | 25% | 9/10 | Requirements quality criteria table (Complete, Consistent, Unambiguous, Verifiable, Traceable). MBSE artifacts with SysML diagram types. Industry context (Boeing 787, NASA Orion, F-35). |
| **Workflow Actionability** | 15% | 8/10 | 5 phases with done/fail criteria. Clear phase gates but lacks input/output templates. |
| **Risk Documentation** | 10% | 8/10 | Risk matrix (Requirements Creep, Interface Issues, Verification Gaps, Emergent Behavior, Schedule Pressure) with likelihood/impact/mitigation. |
| **Example Quality** | 20% | 7/10 | 5 scenarios with links to references. Full flows not visible in SKILL.md body. |
| **Metadata Completeness** | 10% | 9/10 | All 9 fields present. Tags include systems-engineering, requirements, MBSE. |

---

## Weighted Score Calculation

```
Score = (9×0.20) + (9×0.25) + (8×0.15) + (8×0.10) + (7×0.20) + (9×0.10)
      = 1.80 + 2.25 + 1.20 + 0.80 + 1.40 + 0.90
      = 8.35 / 10
```

**Tier: Expert ⭐** (7.0-8.9)

---

## Strengths
1. **Industry-standard V-Model**: Left/Right decomposition and verification clearly shown
2. **SMART requirements quick reference**: Concrete example provided
3. **MBSE tools coverage**: Cameo, Rhapsody, Sparx EA, MATLAB/Simulink
4. **Verification traceability matrix example**: Shows requirement→design→test linking

---

## Areas for Improvement

| Issue | Severity | Recommendation |
|-------|----------|----------------|
| **Example flows not visible** | 🟡 | Include 1-2 full conversation flows in §9 |
| **No decision tree** | 🟡 | Add requirement allocation decision tree with thresholds |
| **DOORS/Jama tools not detailed** | 🟢 | Already has reference structure |

---

## Token Budget Check
- **SKILL.md body**: 360 lines ✅ (≤500 limit)
- **Description chars**: ~135 chars ✅ (≤263 limit)

---

## Evaluation Summary

| Metric | Value |
|--------|-------|
| **Weighted Score** | 8.35/10 |
| **Tier** | Expert ⭐ |
| **Self-Reported Score** | 9.5/10 |
| **Discrepancy** | -1.15 |
| **Recommendation** | APPROVED — Add full conversation flows to reach Exemplary |

---

*Evaluated: 2026-03-24 | Method: skill-writer 6-dimension rubric*
