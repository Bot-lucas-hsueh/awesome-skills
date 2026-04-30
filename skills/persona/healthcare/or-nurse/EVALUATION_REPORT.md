# Skill Evaluation Report: or-nurse

## Overview

| Metric | Value |
|--------|-------|
| **Skill Name** | or-nurse |
| **Location** | `skills/healthcare/or-nurse/SKILL.md` |
| **Current Score** | 8.4/10 (metadata) |
| **Evaluation Date** | 2026-03-24 |
| **Evaluator** | skill-writer |

---

## 6-Dimension Quality Rubric Assessment

| Dimension | Weight | Score (1-10) | Assessment |
|-----------|--------|--------------|------------|
| **System Prompt Depth** | 20% | 9.0 | Role + decision framework (4 gates) + thinking patterns + communication style |
| **Domain Knowledge Density** | 25% | 9.0 | Strong OR frameworks: sterile technique, instrument management, counts, safety protocols |
| **Workflow Actionability** | 15% | 8.0 | Pre-op (3 phases), intraoperative responsibilities, count protocol |
| **Risk Documentation** | 10% | 8.0 | 5 OR-specific risks with severity ratings |
| **Example Quality** | 20% | 9.0 | Two strong scenarios: instrument count discrepancy + sterile field break |
| **Metadata Completeness** | 10% | 9.0 | Almost complete; missing platforms field |

### Weighted Score Calculation

```
Score = (9.0 × 0.20) + (9.0 × 0.25) + (8.0 × 0.15) + (8.0 × 0.10) + (9.0 × 0.20) + (9.0 × 0.10)
      = 1.80 + 2.25 + 1.20 + 0.80 + 1.80 + 0.90
      = 8.75
```

**Result: Expert ⭐ (8.75/10)**

---

## Detailed Dimension Analysis

### ✅ System Prompt Depth (9.0/10)

**Strengths:**
- Clear OR nurse identity: CNOR preferred, sterile technique expertise, surgical team member
- 4 decision gates: Training competency, sterile field integrity, patient risk factors, emergency response
- Thinking patterns: Infection Prevention, Count Awareness, Anticipatory Thinking, Patient as Priority
- Communication style: Standardized, assertive when needed, team-oriented, situational awareness

**Minor Issues:**
- Could add more OR-specific heuristics

### ✅ Domain Knowledge Density (9.0/10)

**Strengths:**
- Surgical Safety Matrix (ASCII diagram): Universal Protocol → Pre/Intra/Post-Operative phases
- OR nursing frameworks: Universal Protocol, Surgical Count (4 counts), Time-Out Protocol, Fire Triangle Assessment
- Professional toolkit: Instrument sets, sterile processing, count sheets, Universal Protocol, AORN Guidelines
- Comprehensive list of what OR nurses handle

**Minor Issues:**
- Could add more instrument categories

### ✅ Workflow Actionability (8.0/10)

**Strengths:**
- Pre-operative phase: 3 phases (Room Preparation, Patient Arrival, Pre-Incision Safety)
- Intraoperative: Ongoing tasks + Count Protocol (4 minimum counts)
- Clear step-by-step procedures

**Suggestions:**
- Add measurable checkpoints per phase
- Include failure criteria

### ✅ Risk Documentation (8.0/10)

**Strengths:**
- 5 OR-specific risks: Surgical Site Infection, Retained Items, Patient Positioning Injury, Wrong-Site Surgery, Fire Risk
- Severity ratings (🔴 High / 🟡 Medium)
- Clear mitigation strategies
- IMPORTANT notes: Speak up immediately, verify counts, universal protocol, documentation

**Suggestions:**
- Add escalation triggers

### ✅ Example Quality (9.0/10)

**Strengths:**
- Scenario 9.1: Instrument count discrepancy - complete protocol: STOP → ALERT → SEARCH → RECOUNT → XRay with documentation requirements
- Scenario 9.2: Sterile field break - immediate response with communication template ("Sterile break—gown sleeve contacted mayo stand")

Both scenarios demonstrate the critical "speak up for patient safety" principle.

**Minor Issues:**
- Could add emergency scenario (cardiac arrest, massive hemorrhage)

### ⚠️ Metadata Completeness (9.0/10)

**Strengths:**
- name, version, author, difficulty, category, tags present
- score, quality metrics present

**Missing:**
- platforms field (optional but recommended for skills)

---

## Issues Found

| Issue | Severity | Description |
|-------|----------|-------------|
| Missing platforms field | 🟡 Minor | Not required but recommended |
| No failure criteria in workflows | 🟡 Minor | Could specify what indicates phase failure |
| Lines 490-604 are boilerplate | 🟡 Minor | Generic filler sections |

---

## Recommendations

1. **Add platforms field** - `platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]`
2. **Remove boilerplate sections** - Lines 490-604 are generic filler
3. **Add failure criteria** - e.g., "Phase fails if time-out not completed"
4. **Consider adding emergency scenario** - Cardiac arrest or massive hemorrhage response

---

## Conclusion

This is a well-structured Expert-level skill with strong OR-specific frameworks, excellent safety-focused scenarios demonstrating the "speak up" principle, and comprehensive risk documentation. The main issues are minor: adding the platforms field and removing generic boilerplate.

**Current Tier: Expert ⭐**  
**Recommendation: Maintain at Expert level**  
**Priority Fix: Add platforms field + remove §16-21 boilerplate**

---
