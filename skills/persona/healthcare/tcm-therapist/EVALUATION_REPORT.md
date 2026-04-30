# Skill Evaluation Report: tcm-therapist

## Overview

| Metric | Value |
|--------|-------|
| **Skill Name** | tcm-therapist |
| **Location** | `skills/healthcare/tcm-therapist/SKILL.md` |
| **Current Score** | 8.5/10 (metadata) |
| **Evaluation Date** | 2026-03-24 |
| **Evaluator** | skill-writer |

---

## 6-Dimension Quality Rubric Assessment

| Dimension | Weight | Score (1-10) | Assessment |
|-----------|--------|--------------|------------|
| **System Prompt Depth** | 20% | 8.0 | Role + decision framework (4 gates) + thinking patterns + communication style |
| **Domain Knowledge Density** | 25% | 9.0 | Strong TCM frameworks: 4 diagnostic methods, 8 principles, Zang-Fu, 5 elements, point combinations |
| **Workflow Actionability** | 15% | 8.0 | Patient consultation (4 phases) + acupuncture session (6 steps) |
| **Risk Documentation** | 10% | 8.0 | 5 risks with severity ratings + appropriate TCM safety concerns |
| **Example Quality** | 20% | 9.0 | Two strong clinical scenarios: chronic low back pain + insomnia |
| **Metadata Completeness** | 10% | 9.0 | All required fields; tags is a bit verbose |

### Weighted Score Calculation

```
Score = (8.0 × 0.20) + (9.0 × 0.25) + (8.0 × 0.15) + (8.0 × 0.10) + (9.0 × 0.20) + (9.0 × 0.10)
      = 1.60 + 2.25 + 1.20 + 0.80 + 1.80 + 0.90
      = 8.55
```

**Result: Expert ⭐ (8.55/10)**

---

## Detailed Dimension Analysis

### ✅ System Prompt Depth (8.0/10)

**Strengths:**
- Clear TCM practitioner identity with certifications and training
- 4 decision gates: scope of practice, safety concerns, emergency referral, adequate information
- Thinking patterns covering pattern differentiation, treatment principle, point combination, holistic view
- Communication style emphasizes explanatory and patient-centered approach

**Areas for Improvement:**
- Could add more TCM-specific heuristics (e.g., "when pulse is wiry + patient is irritable → consider Liver pattern first")

### ✅ Domain Knowledge Density (9.0/10)

**Strengths:**
- Excellent TCM treatment decision tree (ASCII diagram)
- Four diagnostic methods detailed
- 8 Principle differentiation, Zang-Fu Theory, Five Elements, Meridian Selection frameworks
- Common patterns table with key signs, treatment principle, and points (Liver Qi Stagnation, Spleen Qi Deficiency, Kidney Yin Deficiency, Blood Stasis)

**Minor Issues:**
- Some sections reference external files

### ✅ Workflow Actionability (8.0/10)

**Strengths:**
- Patient consultation workflow: 4 phases (Four Diagnostic Methods → Pattern Differentiation → Treatment Planning → Patient Education)
- Acupuncture session: 6 clear steps (Preparation → Point Location → Needle Insertion → Retention → Needle Removal → Documentation)

**Suggestions:**
- Add measurable checkpoints per step
- Include failure criteria for each phase

### ✅ Risk Documentation (8.0/10)

**Strengths:**
- 5 TCM-specific risks: Contraindicated Treatment, Herb-Drug Interactions, Missed Medical Diagnosis, Infection Risk, Qi Disturbance
- Severity ratings (🔴 High / 🟡 Medium)
- IMPORTANT notes covering scope recognition, contraindication screening, medication review, referral thresholds

**Suggestions:**
- Add escalation triggers for each risk

### ✅ Example Quality (9.0/10)

**Strengths:**
- Scenario 9.1: Chronic low back pain (Kidney Yang Deficiency with Cold-Damp) - complete with pattern differentiation, treatment principle, point selection, lifestyle advice
- Scenario 9.2: Stress/insomnia (Heart Blood Deficiency + Liver Qi Stagnation → Fire) - detailed TCM assessment and acupuncture points

Both scenarios demonstrate authentic TCM pattern differentiation with specific point combinations.

**Minor Issues:**
- Could add one scenario covering acute conditions or herb-drug interaction warning

### ✅ Metadata Completeness (9.0/10)

**Strengths:**
- name, version, author, difficulty, category, tags all present
- score, quality, text_score, runtime_score, variance

**Minor Issues:**
- tags field is verbose: `'[healthcare, tcm, traditional-medicine, acupuncture, massage, integrative]'` - should be simpler array

---

## Issues Found

| Issue | Severity | Description |
|-------|----------|-------------|
| Tags format verbose | 🟡 Minor | Should be simpler: `[tcm, acupuncture, herbal-medicine]` |
| §16-21 boilerplate | 🟡 Minor | Generic filler sections (lines 522-636) |
| No failure criteria in workflows | 🟡 Minor | Could add what indicates phase failure |

---

## Recommendations

1. **Simplify tags format** - Remove quotes and brackets: `tags: [tcm, acupuncture, herbal-medicine]`
2. **Remove boilerplate sections** - Lines 522-636 are generic filler
3. **Add failure criteria** - e.g., "Phase fails if no pattern can be differentiated"
4. **Add herb-drug interaction scenario** - Practical example showing how to screen medications

---

## Conclusion

This is a well-structured Expert-level skill with authentic TCM frameworks, realistic clinical scenarios, and appropriate safety documentation. The main issues are minor: cleaning up tags format and removing generic boilerplate content.

**Current Tier: Expert ⭐**  
**Recommendation: Maintain at Expert level**  
**Priority Fix: Simplify tags + remove §16-21 boilerplate**

---
