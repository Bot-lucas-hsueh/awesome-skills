# Skill Evaluation Report: healthcare-executive

## Overview

| Metric | Value |
|--------|-------|
| **Skill Name** | healthcare-executive |
| **Location** | `skills/healthcare/healthcare-executive/SKILL.md` |
| **Current Score** | 8.4/10 (metadata) |
| **Evaluation Date** | 2026-03-24 |
| **Evaluator** | skill-writer |

---

## 6-Dimension Quality Rubric Assessment

| Dimension | Weight | Score (1-10) | Assessment |
|-----------|--------|--------------|------------|
| **System Prompt Depth** | 20% | 9.0 | Role + decision framework (4 gates) + thinking patterns + communication style |
| **Domain Knowledge Density** | 25% | 9.0 | Healthcare-specific frameworks: Triple Aim, HRO, Lean, Just Culture, quality metrics |
| **Workflow Actionability** | 15% | 8.0 | Quality improvement (4 phases) + budget planning (7 steps) |
| **Risk Documentation** | 10% | 8.0 | 5 healthcare risks with severity ratings |
| **Example Quality** | 20% | 8.0 | Two realistic scenarios: CLABSI reduction + nurse retention with ROI |
| **Metadata Completeness** | 10% | 10.0 | All 9 fields present |

### Weighted Score Calculation

```
Score = (9.0 × 0.20) + (9.0 × 0.25) + (8.0 × 0.15) + (8.0 × 0.10) + (8.0 × 0.20) + (10.0 × 0.10)
      = 1.80 + 2.25 + 1.20 + 0.80 + 1.60 + 1.00
      = 8.65
```

**Result: Expert ⭐ (8.65/10)**

---

## Detailed Dimension Analysis

### ✅ System Prompt Depth (9.0/10)

**Strengths:**
- Clear healthcare executive identity: 20+ years, CMO/VP experience, MD/MBA
- 4 decision gates: Patient Safety, Regulatory/Compliance, Financial Impact, Clinical Staff
- Thinking patterns: Triple Aim, Regulatory Navigation, Change Management, Financial Stewardship
- Communication style: executive presence, balanced transparency, stakeholder-appropriate messaging

**Minor Issues:**
- Could add more domain-specific heuristics for healthcare

### ✅ Domain Knowledge Density (9.0/10)

**Strengths:**
- Healthcare Leadership Framework (ASCII diagram) covering Vision/Strategy → Quality/Safety, Operations, Finance → Execution/Culture
- Comprehensive frameworks: HRO (5 principles), Lean Healthcare (5 steps), Just Culture, ACMA/CHAMPS
- Healthcare metrics: HAC rate, 30-day readmission, HCAHPS, Operating Margin, Staff Turnover
- Clear integration patterns with other healthcare roles

**Minor Issues:**
- Could add more specific threshold values for metrics

### ✅ Workflow Actionability (8.0/10)

**Strengths:**
- Quality Improvement Initiative: 4 phases with detailed sub-steps (Assessment → Strategy → Implementation → Sustainment)
- Budget Planning Cycle: 7 clear steps (Environmental scan → Board approval → Monitoring)

**Suggestions:**
- Add measurable checkpoints per phase
- Include failure criteria

### ✅ Risk Documentation (8.0/10)

**Strengths:**
- 5 healthcare-specific risks: Patient Safety Impact, Regulatory Violations, Clinical Staff Burnout, Financial Unsustainability, Liability Exposure
- Severity ratings (🔴 High) for all
- Clear mitigation strategies
- IMPORTANT notes covering fiduciary responsibility, quality/finance alignment, compliance as minimum bar

**Suggestions:**
- Add escalation triggers for each risk

### ✅ Example Quality (8.0/10)

**Strengths:**
- Scenario 9.1: CLABSI reduction - comprehensive with current state/target table, initiative design, question about nurse engagement
- Scenario 9.2: Nurse retention with ROI calculation - shows $5.4M cost vs $1.2M investment with break-even analysis

**Strengths:**
- Both scenarios demonstrate executive-level thinking (data-driven, ROI-focused)

**Minor Issues:**
- Could add scenario covering regulatory crisis or merger integration

### ✅ Metadata Completeness (10/10)

All 9 fields present:
- name, version, author, difficulty, category, tags
- score, quality, text_score, runtime_score, variance

---

## Issues Found

| Issue | Severity | Description |
|-------|----------|-------------|
| No failure criteria in workflows | 🟡 Minor | Could specify what indicates phase failure |
| Lines 504-618 are boilerplate | 🟡 Minor | Generic filler sections (Domain Deep Dive, Risk Management, Excellence) |
| Could add more metric thresholds | 🟡 Minor | Some metrics lack specific target values |

---

## Recommendations

1. **Remove boilerplate sections** - Lines 504-618 are generic filler that doesn't add healthcare executive value
2. **Add failure criteria to workflows** - e.g., "Phase fails if baseline metrics unavailable"
3. **Add metric thresholds** - Specify targets like "HAC rate < 0.5 per 1000 line days"
4. **Consider adding scenarios** - Regulatory crisis, merger integration, physician recruitment

---

## Conclusion

This is a well-structured Expert-level skill with strong healthcare-specific frameworks, realistic executive-level scenarios with ROI analysis, and comprehensive risk documentation. The main issue is generic boilerplate content that should be removed.

**Current Tier: Expert ⭐**  
**Recommendation: Maintain at Expert level**  
**Priority Fix: Remove §16-21 boilerplate (lines 504-618)**

---
