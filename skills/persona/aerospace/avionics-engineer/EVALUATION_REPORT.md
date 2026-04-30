# Skill Evaluation Report — avionics-engineer

## Metadata
| Field | Value |
|-------|-------|
| **name** | avionics-engineer |
| **version** | 2.0.0 |
| **difficulty** | expert |
| **category** | aerospace |
| **current_score** | 9.5/10 (self-reported) |

---

## 6-Dimension Scoring

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| **System Prompt Depth** | 20% | 9/10 | Strong identity (DO-178C, DO-254 certification focus). Professional DNA (Systems Architect, Software Engineer, Hardware Engineer, Integration Specialist). DAL assignment framework included. |
| **Domain Knowledge Density** | 25% | 9/10 | ARINC standards table (429, 653, 664, 661, 702). DO-178C objectives by DAL table. Flight control system types (Conventional→Power-Assisted→FBW→FBL). GNSS accuracy budget. |
| **Workflow Actionability** | 15% | 8/10 | 5 phases (Requirements→Verification) with done/fail criteria. Clear certification workflow. |
| **Risk Documentation** | 10% | 8/10 | Risk matrix (Common Mode Failure, Software Error, EMI/EMC, Integration Failures, Schedule Delays) with likelihood/impact/mitigation. |
| **Example Quality** | 20% | 7/10 | 5 scenarios with links. Full conversation flows not visible. |
| **Metadata Completeness** | 10% | 9/10 | All 9 fields. Tags include flight-control, navigation, fadec. |

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
1. **Certification focus**: DO-178C, DO-254, DO-160 coverage with DAL objectives table
2. **ARINC standards**: Comprehensive table with purpose and applications
3. **IMA vs Federated decision matrix**: Clear comparison with winner column
4. **Real aircraft examples**: Boeing 787 (6.5M LOC), A350 (IMA), F-35 (8M+ LOC)

---

## Areas for Improvement

| Issue | Severity | Recommendation |
|-------|----------|----------------|
| **Example flows not visible** | 🟡 | Add 1-2 full conversation flows (e.g., DO-178C planning) |
| **No code examples** | 🟡 | Could add ARINC 429 word parsing or pseudo-code |
| **Safety analysis flow vague** | 🟡 | Add FHA→PSSA→SSA decision tree |

---

## Token Budget Check
- **SKILL.md body**: 353 lines ✅ (≤500 limit)
- **Description chars**: ~145 chars ✅ (≤263 limit)

---

## Evaluation Summary

| Metric | Value |
|--------|-------|
| **Weighted Score** | 8.35/10 |
| **Tier** | Expert ⭐ |
| **Self-Reported Score** | 9.5/10 |
| **Discrepancy** | -1.15 |
| **Recommendation** | APPROVED — Add conversation flows to reach Exemplary |

---

*Evaluated: 2026-03-24 | Method: skill-writer 6-dimension rubric*
