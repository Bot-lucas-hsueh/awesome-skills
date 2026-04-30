# EVALUATION REPORT: psychologist

**Date:** 2026-03-24  
**Reviewer:** Skill Writer (skill-writer methodology)  
**Tier:** Community ⭐ → Expert ⭐

---

## 6-Dimension Quality Rubric Score

| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| **System Prompt Depth** | 20% | 8/10 | Structured prompt with decision framework, thinking patterns. Strong clinical approach with empathy-first communication. |
| **Domain Knowledge Density** | 25% | 8/10 | CBT/DBT/ACT frameworks, PHQ-9/GAD-7/PCL-5 severity guides, DBT skills (TIPP/PLEASE/FAST). Evidence-based treatment matching table. |
| **Workflow Actionability** | 15% | 7/10 | Phase 1-2 detailed with tables, checkpoints, fail criteria. Missing Phase 3-4 for full workflow. |
| **Risk Documentation** | 10% | 6/10 | Risk matrix present but contains generic content (lines 431-517). Clinical risks well-documented but diluted by business content. |
| **Example Quality** | 20% | 3/10 | **CRITICAL GAP**: §9 scenarios (lines 253-362) are generic business templates, NOT psychologist-specific. No therapeutic conversation flows. |
| **Metadata Completeness** | 10% | 7/10 | All 9 fields present. Description is duplicated/padded ("Expert-level Clinical Psychologist skill providing..." appears twice). |

### Weighted Score Calculation
```
Score = (8×0.20) + (8×0.25) + (7×0.15) + (6×0.10) + (3×0.20) + (7×0.10)
      = 1.6 + 2.0 + 1.05 + 0.6 + 0.6 + 0.7 = 6.55 → Community
```

**Current Tier: Community** (Target: Expert ⭐)

---

## Key Issues Identified

### 🔴 Critical
1. **§9 Examples are Generic** (lines 253-362): All 4 scenarios are copy-pasted business templates. Should contain:
   - Therapeutic assessment conversation
   - Crisis intervention example
   - Psychoeducation session
   - Safety screening demonstration

### 🟡 High
2. **Bloating Content** (lines 410-517): Sections §16-21 contain generic business content unrelated to clinical psychology. Remove or move to references/.
3. **Description Duplication**: "Expert-level Clinical Psychologist skill..." appears twice in description.

---

## Recommended Fixes

| Priority | Fix | Expected Score Impact |
|----------|-----|----------------------|
| **1** | Replace §9 with 4 psychologist-specific scenarios | +2.4 pts (3→9 on Examples) |
| **2** | Remove lines 410-517 (generic business content) | +0.4 pts |
| **3** | Clean up description field | +0.2 pts |

**Projected Score After Fixes:**
```
Score = (8×0.20) + (8×0.25) + (7×0.15) + (7×0.10) + (9×0.20) + (8×0.10)
      = 1.6 + 2.0 + 1.05 + 0.7 + 1.8 + 0.8 = 7.95 → Expert ⭐
```

---

## Strengths

- Strong system prompt with clear clinical decision framework
- Excellent risk documentation (crisis protocols, mandatory reporting)
- Good evidence-based treatment matching table
- Appropriate disclaimer language

---

## Anti-Patterns Detected

| Anti-Pattern | Location | Severity |
|--------------|----------|----------|
| **Examples-First Violation** | §9 | 🔴 Critical - No real psychologist scenarios |
| **Content Bloat** | §16-21 | 🟡 Medium - Generic business content |

---

## Decision

**NOT READY** for Expert tier. Fix critical example gap before promotion.

**Action Required:** Rewrite §9 with domain-specific therapeutic scenarios per skill-writer methodology.
