# Skill Evaluation Report — propulsion-engineer

## Metadata
| Field | Value |
|-------|-------|
| **name** | propulsion-engineer |
| **version** | 2.0.0 |
| **difficulty** | expert |
| **category** | aerospace |
| **current_score** | 9.5/10 (self-reported) |

---

## 6-Dimension Scoring

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| **System Prompt Depth** | 20% | 9/10 | Professional DNA (Thermodynamicist, Aerodynamicist, Controls Engineer, Integration Specialist). Decision hierarchy (Thermal Efficiency → Propulsive Efficiency → Weight → Reliability → Certification). |
| **Domain Knowledge Density** | 25% | 9/10 | Engine parameter tables (BPR, OPR, TIT ranges for different aircraft types). Brayton cycle efficiency formula. Thrust equation. Real programs (GE9X, GTF, LEAP, UltraFan). |
| **Workflow Actionability** | 15% | 8/10 | 5 phases (Concept→Service) with done/fail criteria. Clear milestones but lacks templates. |
| **Risk Documentation** | 10% | 8/10 | Risk matrix (Surge/Stall, HCF/LCF, Bird Strike, Schedule Delay) with likelihood/impact/mitigation. |
| **Example Quality** | 20% | 7/10 | 5 scenarios with links. Full conversation flows not in body. |
| **Metadata Completeness** | 10% | 9/10 | All 9 fields. Tags include gas-turbine, fadec, engine-design. |

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
1. **Technical formulas**: Brayton cycle efficiency, thrust equation included
2. **Real engine data**: GE9X (105,000 lbf), GTF (16% fuel reduction), LEAP (35M flight hours)
3. **Turbofan configurations**: Low/Medium/High BPR with use cases
4. **Material selection matrix**: Temperature ranges with materials and technology

---

## Areas for Improvement

| Issue | Severity | Recommendation |
|-------|----------|----------------|
| **Example flows not visible** | 🟡 | Add 1-2 full conversation flows showing cycle optimization |
| **No FADEC code example** | 🟡 | Could add control law pseudo-code |
| **Operating line visualization** | 🟢 | Would benefit from surge margin diagram reference |

---

## Token Budget Check
- **SKILL.md body**: 375 lines ✅ (≤500 limit)
- **Description chars**: ~135 chars ✅ (≤263 limit)

---

## Evaluation Summary

| Metric | Value |
|--------|-------|
| **Weighted Score** | 8.35/10 |
| **Tier** | Expert ⭐ |
| **Self-Reported Score** | 9.5/10 |
| **Discrepancy** | -1.15 |
| **Recommendation** | APPROVED — Add conversation flows for Exemplary tier |

---

*Evaluated: 2026-03-24 | Method: skill-writer 6-dimension rubric*
