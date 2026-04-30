# Skill Evaluation Report: disease-investigator

## Overview

| Metric | Value |
|--------|-------|
| **Skill Name** | disease-investigator |
| **Location** | `skills/healthcare/disease-investigator/SKILL.md` |
| **Current Score** | 8.3/10 (metadata) |
| **Evaluation Date** | 2026-03-24 |
| **Evaluator** | skill-writer |

---

## 6-Dimension Quality Rubric Assessment

| Dimension | Weight | Score (1-10) | Assessment |
|-----------|--------|--------------|------------|
| **System Prompt Depth** | 20% | 8.5 | Role + decision framework (4 gates) + thinking patterns + communication style |
| **Domain Knowledge Density** | 25% | 9.0 | Excellent epidemiologic frameworks, metrics (R₀, attack rate, serial interval), surveillance protocols |
| **Workflow Actionability** | 15% | 9.0 | 5-phase outbreak investigation + 8-step contact tracing with templates |
| **Risk Documentation** | 10% | 8.0 | 5 risks with severity ratings + domain-specific mitigation |
| **Example Quality** | 20% | 9.0 | Two strong scenarios: foodborne outbreak + COVID-19 contact tracing |
| **Metadata Completeness** | 10% | 10.0 | All 9 fields present |

### Weighted Score Calculation

```
Score = (8.5 × 0.20) + (9.0 × 0.25) + (9.0 × 0.15) + (8.0 × 0.10) + (9.0 × 0.20) + (10.0 × 0.10)
      = 1.70 + 2.25 + 1.35 + 0.80 + 1.80 + 1.00
      = 8.90
```

**Result: Expert ⭐ (8.90/10)**

---

## Detailed Dimension Analysis

### ✅ System Prompt Depth (8.5/10)

**Strengths:**
- Clear role definition with 10+ years experience, Master's/PhD, field epidemiology training
- 4 decision gates with fail actions
- Thinking patterns table covering descriptive epidemiology, chain of transmission, attack rate analysis
- Communication style emphasizes technical accuracy and actionable recommendations

**Areas for Improvement:**
- Could add more domain-specific heuristics (e.g., "when R₀ > 5, prioritize contact tracing speed over completeness")

### ✅ Domain Knowledge Density (9.0/10)

**Strengths:**
- 8-step outbreak investigation framework with ASCII diagram
- Comprehensive metrics table: Attack Rate, R₀, Serial Interval, Incubation Period, CFR
- Investigation protocols for multiple scenarios: Standard, Contact Tracing, Foodborne, Respiratory
- Decision framework tables for epidemic curve interpretation

**Minor Issues:**
- §7 references some external files; could be more self-contained

### ✅ Workflow Actionability (9.0/10)

**Strengths:**
- Outbreak investigation: 5 phases with detailed sub-steps (Hours → Days → Weeks)
- Contact tracing: 8 clearly defined steps with contact classification
- Clear phase descriptions with timelines

**Suggestions:**
- Add measurable checkpoints per phase
- Include failure criteria

### ✅ Risk Documentation (8.0/10)

**Strengths:**
- 5 domain-specific risks: Delayed Response, Incomplete Contact Tracing, Privacy, Misclassification, Over-Reaction
- Severity ratings (🔴 High / 🟡 Medium)
- IMPORTANT notes covering privacy, action under uncertainty, cultural competency, data security

**Suggestions:**
- Add escalation triggers for each risk
- Include example consequences

### ✅ Example Quality (9.0/10)

**Strengths:**
- Scenario 9.1: Restaurant foodborne outbreak - complete with attack rate analysis, hypothesis generation, case-control approach
- Scenario 9.2: COVID-19 contact tracing - detailed timeline, infectious period, high/medium risk classification
- Both scenarios include actionable recommendations

**Minor Issues:**
- Could add one more scenario covering non-infectious disease patterns

### ✅ Metadata Completeness (10/10)

All 9 fields present:
- name, version, author, difficulty, category, tags
- score, quality, text_score, runtime_score, variance

---

## Issues Found

| Issue | Severity | Description |
|-------|----------|-------------|
| §7 references external files | 🟡 Minor | Some sections reference `references/07-standards.md` - should be self-contained |
| No failure criteria in workflows | 🟡 Minor | Could specify what indicates phase failure |
| Lines 555-669 are boilerplate | 🟡 Minor | Domain Deep Dive, Risk Management, Excellence Framework sections are generic filler |

---

## Recommendations

1. **Remove boilerplate sections (lines 555-669)** - These are generic and don't add domain-specific value
2. **Add failure criteria to workflows** - e.g., "Phase fails if no cases identified within 48 hours"
3. **Consider adding more scenarios** - Vector-borne outbreak, healthcare-associated infection cluster
4. **Self-contain §7** - Either integrate referenced content or remove links

---

## Conclusion

This is a well-structured Expert-level skill with strong epidemiologic frameworks, realistic scenarios, and comprehensive risk documentation. The main areas for improvement are removing generic boilerplate content and adding failure criteria to workflow phases.

**Current Tier: Expert ⭐**  
**Recommendation: Maintain at Expert level**  
**Priority Fix: Remove §16-21 boilerplate (lines 555-669)**

---
