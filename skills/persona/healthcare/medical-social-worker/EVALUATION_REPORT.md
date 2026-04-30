# Skill Evaluation Report: medical-social-worker

**Skill:** `skills/healthcare/medical-social-worker/SKILL.md`  
**Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  

---

## 1. Executive Summary

| Metric | Score | Tier |
|--------|-------|------|
| **Weighted Average** | 8.6/10 | Expert ⭐ |
| System Prompt Depth | 9/10 | Exemplary |
| Domain Knowledge Density | 9/10 | Exemplary |
| Workflow Actionability | 8/10 | Expert |
| Risk Documentation | 9/10 | Exemplary |
| Example Quality | 7/10 | Expert |
| Metadata Completeness | 10/10 | Exemplary |

**Classification:** Expert Verified  
**Recommendation:** Production-ready. Minor improvements possible for Exemplary tier.

---

## 2. Dimension Analysis

### 2.1 System Prompt Depth (9/10)

**Strengths:**
- Detailed role definition: LCSW, LMSW, 12+ years, Level I trauma center experience
- Decision framework gates with specific questions and fail actions
- Thinking patterns table with MSW perspective
- Communication style defined (collaborative, concrete, documentation-ready)

**Verdict:** Exemplary - includes decision gates and thinking patterns.

---

### 2.2 Domain Knowledge Density (9/10)

**Strengths:**
- Discharge planning framework with ASCII diagram
- Biopsychosocial assessment process
- Interqual/MCG criteria knowledge
- PHQ-9, GAD-7 screening tools
- Specific resource examples with names/numbers
- Community resource database, insurance portals, EMR modules

**Verdict:** Exemplary - deep frameworks with specific tools.

---

### 2.3 Workflow Actionability (8/10)

**Strengths:**
- 4-phase discharge planning process (Assessment → Planning → Implementation → Follow-Up)
- Psychosocial assessment with 5-step process
- Done/Fail criteria for each phase
- Detailed sub-steps

**Verdict:** Strong but could include MSW-specific templates.

---

### 2.4 Risk Documentation (9/10)

**Strengths:**
- Structured risk table in §3 with 4 high-severity risks:
  - Unsafe discharge (🔴 High)
  - Missed safety concerns (🔴 High)
  - Inappropriate resource placement (🔴 High)
  - Insurance non-compliance (🔴 High)
- Mitigation strategies for each
- ⚠️ IMPORTANT callout box

**Verdict:** Exemplary risk documentation with severity ratings.

---

### 2.5 Example Quality (7/10)

**Strengths:**
- 9.1 Discharge Planning scenario (78F CHF, diabetes, CKD4 - complex case)
- 9.2 Crisis Intervention scenario (suicidal ideation assessment)
- Specific resources provided (Meals on Wheels, NeedyMeds, medical alert)
- Safety assessment steps detailed

**Areas for Improvement:**
- §9 scenarios are generic (Initial Consultation, Problem Resolution, Strategic Planning)
- Only 2 domain-specific scenarios; need more variety
- No full conversation flow showing AI applying frameworks

**Verdict:** Good but could use more domain-specific scenario variety.

---

### 2.6 Metadata Completeness (10/10)

**Strengths:**
- All 9 fields complete
- Version 3.0.0, updated 2026-03-21
- Comprehensive tags
- Score fields (8.3/10)

**Verdict:** Exemplary.

---

## 3. Top Issues & Rewrite Suggestions

### Issue 1: §9 Generic Scenarios (Priority: MEDIUM)

**Current:** §9 has generic "Initial Consultation" templates

**Suggested Enhancement:** Add more MSW-specific scenarios:
- **Scenario: Insurance Authorization Denial** - appeal process
- **Scenario: Patient Refuses Discharge** - documentation and escalation
- **Scenario: Homeless Patient Discharge** - housing resources

### Issue 2: Missing Platform Support (Priority: MEDIUM)

**Current:** No §5 Platform Support section

**Suggested Addition:**
```markdown
## § 5 · Platform Support

| Platform | Install Method | Verification |
|----------|----------------|--------------|
| OpenCode | `/skill install medical-social-worker` | Run trigger word test |
| Claude Code | Read and activate role from §1 | - |
| Cursor | skill.json configuration | - |
```

---

## 4. Section Compliance Check

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 1 | System Prompt | ✅ Present | Excellent - gates + thinking patterns |
| 2 | What This Skill Does | ✅ Present | 6 capabilities |
| 3 | Risk Disclaimer | ✅ Present | 4 risks with severity |
| 4 | Core Philosophy | ✅ Present | Discharge framework diagram |
| 5 | Platform Support | ❌ Missing | - |
| 6 | Professional Toolkit | ✅ Present | - |
| 7 | Standards & Quality | ❌ Missing | - |
| 8 | Workflow | ✅ Present | 4-phase process |
| 9 | Scenario Examples | ⚠️ Partial | 2 domain + 4 generic |
| 10 | Common Pitfalls | ✅ Present | Anti-patterns with severity |
| 11 | Integration | ✅ Present | Tables with workflows |
| 12 | Scope & Limitations | ✅ Present | Explicit boundaries |
| 13 | How to Use | ❌ Missing | - |
| 14 | Quality Verification | ⚠️ Weak | References external |
| 15 | Version History | ❌ Missing | - |
| 16 | License & Author | ✅ Present | MIT |

---

## 5. Token Budget Analysis

| Metric | Current | Target (Expert) | Status |
|--------|---------|------------------|--------|
| Total lines | 663 | 300-600 | ⚠️ Above target |
| System prompt | ~20 lines | 15-30 | ✅ In range |
| §9 scenarios | 6 scenarios (mixed) | 2+ full flows | ⚠️ Need more domain-specific |

**Recommendation:** Reduce boilerplate in §16-21; move to `references/`.

---

## 6. Final Verdict

**Classification:** Expert Verified ⭐

**Upgrade Path to Exemplary:**
1. Add §5 Platform Support per standards.md §7.11
2. Add §13 How to Use with install instructions
3. Expand §9 with 2-3 more domain-specific full flows (insurance denial, homeless discharge)
4. Add §7 Standards with self-test cases

**Strengths:** Excellent system prompt with decision gates, strong risk matrix, comprehensive domain knowledge  
**Weaknesses:** Missing platform support, generic §9 scenarios
