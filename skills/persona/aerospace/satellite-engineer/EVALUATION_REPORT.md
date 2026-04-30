# Skill Evaluation Report — satellite-engineer

## Metadata
| Field | Value |
|-------|-------|
| **name** | satellite-engineer |
| **version** | 2.0.0 |
| **difficulty** | expert |
| **category** | aerospace |
| **current_score** | 9.5/10 (self-reported) |

---

## 6-Dimension Scoring

| Dimension | Weight | Score | Rationale |
|-----------|--------|-------|-----------|
| **System Prompt Depth** | 20% | 9/10 | Identity with professional DNA, decision hierarchy, thinking patterns. Clear orbital mechanics context. |
| **Domain Knowledge Density** | 25% | 9/10 | Orbit characteristics table with specific altitudes, period, applications. Power subsystem sizing with formulas. Industry context with real programs (Starlink, GPS, JWST). |
| **Workflow Actionability** | 15% | 8/10 | 5 phases (Concept→Operations) with done/fail criteria. Clear phase gates but lacks templates. |
| **Risk Documentation** | 10% | 8/10 | Risk matrix (Launch Failure, Early Orbit Failure, Component Degradation, Space Weather, Debris Collision) with likelihood/impact/mitigation. |
| **Example Quality** | 20% | 7/10 | 5 scenarios with links to references. Links provided but actual conversation flows not visible in SKILL.md body. |
| **Metadata Completeness** | 10% | 9/10 | All 9 fields present. Description is detailed with role + triggers. Tags comprehensive. |

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
1. **Comprehensive decision hierarchy**: Mission → Orbit → Lift Mass → Lifetime → Cost flow is clear
2. **Real industry data**: Starlink (5,500+), GPS (31), JWST ($10B) provide concrete benchmarks
3. **Technical depth**: Orbital velocity formula, link budget equation included
4. **Proper references structure**: Content offloaded to references/ directory appropriately

---

## Areas for Improvement

| Issue | Severity | Recommendation |
|-------|----------|----------------|
| **Example flows not visible** | 🟡 | Include 1-2 full conversation flows in §9, not just links |
| **Workflow templates missing** | 🟡 | Add input/output templates for each phase |
| **No anti-pattern correction flow** | 🟢 | Already has anti-pattern table ( §10) |

---

## Token Budget Check
- **SKILL.md body**: 377 lines ✅ (≤500 limit)
- **Description chars**: ~130 chars ✅ (≤263 limit)

---

## Evaluation Summary

| Metric | Value |
|--------|-------|
| **Weighted Score** | 8.35/10 |
| **Tier** | Expert ⭐ |
| **Self-Reported Score** | 9.5/10 |
| **Discrepancy** | -1.15 (self-reported may be optimistic) |
| **Recommendation** | APPROVED — Add 1-2 full conversation flows to reach Exemplary |

---

*Evaluated: 2026-03-24 | Method: skill-writer 6-dimension rubric*
