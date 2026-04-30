# Skill Evaluation Report: drug-rehab-counselor

**Date:** 2026-03-24  
**Evaluator:** skill-writer  
**Version:** 3.0.0

---

## Summary

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| System Prompt Depth | 8.5 | 20% | 1.70 |
| Domain Knowledge Density | 8.0 | 25% | 2.00 |
| Workflow Actionability | 7.0 | 15% | 1.05 |
| Risk Documentation | 9.0 | 10% | 0.90 |
| Example Quality | 7.5 | 20% | 1.50 |
| Metadata Completeness | 8.0 | 10% | 0.80 |
| **TOTAL** | | | **7.95** |

**Tier: Expert ⭐**

---

## Dimension Analysis

### 1. System Prompt Depth (8.5/10)
- ✅ §1.1 Role definition with 15+ years, CAC certification
- ✅ §1.2 Decision Framework with 4 gates
- ✅ §1.3 Thinking Patterns (4 dimensions: Change is Process, Harm Reduction, Whole-Person, Relapse is Part of Recovery)
- ✅ §1.4 Communication Style (person-first language, MI techniques)

### 2. Domain Knowledge Density (8.0/10)
- ✅ Recovery Oriented System framework (visual)
- ✅ Treatment frameworks table (MI, Stages of Change, Relapse Prevention, ASAM)
- ✅ Recovery metrics table (days of abstinence, treatment retention, self-efficacy)
- ⚠️ Missing specific thresholds (e.g., what completion rate is "good")

### 3. Workflow Actionability (7.0/10)
- ✅ Supportive Conversation Framework (4 phases with sub-steps)
- ✅ Family Support Guidance (5 steps)
- ⚠️ No explicit deliverables per phase
- ⚠️ No measurable output tests

### 4. Risk Documentation (9.0/10)
- ✅ 5 risks with severity ratings
- ✅ Each risk has mitigation
- ✅ Crisis resources prominently featured
- **Signal**: Domain-specific (crisis situations, medical advice, triggering content)

### 5. Example Quality (7.5/10)
- ✅ 2 real scenarios (person seeking help, family member seeking guidance)
- ✅ Both scenarios include crisis resources and compassionate language
- ❌ Mixed with generic placeholder in §9 (lines 364-424)
- **Anti-Pattern**: Generic filler dilutes signal

### 6. Metadata Completeness (8.0/10)
- ✅ 9 fields present
- ⚠️ Description: 163 chars - short
- ⚠️ No platforms field
- ⚠️ Self-score (9.5) > actual (~7.95)

---

## Critical Issues

| Issue | Severity | Fix |
|-------|----------|-----|
| Generic filler in §9 Scenario Examples | 🔴 High | Remove or replace with rehab-specific content |
| Line count 660, exceeds domain limit | 🔴 High | Remove filler sections |

---

## Anti-Patterns Detected

| Anti-Pattern | Location | Severity |
|--------------|----------|----------|
| Generic placeholder content | §9 (lines 364-424) | 🔴 High |
| Knowledge maturity model | §16 (lines 545-564) | 🟡 Medium |
| Generic risk register | §17 (lines 570-592) | 🟡 Medium |
| Excellence framework | §18-21 (lines 596-660) | 🟡 Medium |

**Total filler content: ~130 lines** (20% of file)

---

## Signal-to-Token Efficiency
```
= (3×3) + (2×5) + (5×2) = 9 + 10 + 10 = 29
÷ 6.60 = 4.39 → Exemplary
```
**Status: ✅ PASS**

---

## Conclusion

**drug-rehab-counselor** is an Expert-level skill with strong recovery-focused content:
1. ~130 lines generic filler (sections 16-21)
2. Self-score overestimates quality
3. Real content (MI, ASAM, stages of change) is solid but mixed with generic

**Strengths**:
- Person-first language emphasized throughout
- Crisis resources prominently displayed
- Evidence-based frameworks (MI, ASAM, Stages of Change)
- Family support guidance included

**Recommendation**: 
- Remove sections 16-21
- Update self-score to 7.5-8.0
- Expand with more treatment-specific scenarios (relapse, co-occurring disorders)

After fixes: Strong Expert (8.5+)

---

*All 5 skills evaluated*
