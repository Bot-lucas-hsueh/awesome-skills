# Skill Evaluation Report: social-worker

**Skill:** `skills/healthcare/social-worker/SKILL.md`  
**Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  

---

## 1. Executive Summary

| Metric | Score | Tier |
|--------|-------|------|
| **Weighted Average** | 8.4/10 | Expert ⭐ |
| System Prompt Depth | 9/10 | Exemplary |
| Domain Knowledge Density | 9/10 | Exemplary |
| Workflow Actionability | 7/10 | Expert |
| Risk Documentation | 9/10 | Exemplary |
| Example Quality | 7/10 | Expert |
| Metadata Completeness | 10/10 | Exemplary |

**Classification:** Expert Verified  
**Recommendation:** Production-ready. Similar to medical-social-worker; addresses broader social work scope.

---

## 2. Dimension Analysis

### 2.1 System Prompt Depth (9/10)

**Strengths:**
- Senior Clinical Social Worker with 20+ years
- LCSW license, supervised graduate interns
- NASW Code of Ethics reference
- 5 decision gates with specific questions
- Thinking patterns table (Ecological, Strengths, Safety, Cultural, Systems)
- Communication style defined

**Verdict:** Exemplary - comprehensive system prompt with decision framework.

---

### 2.2 Domain Knowledge Density (9/10)

**Strengths:**
- Ecological systems framework (micro/meso/exo/macro)
- Biopsychosocial assessment
- Case management, crisis intervention, therapy, advocacy, group work
- NASW Code of Ethics
- Motivational Interviewing, trauma-informed practice
- Resource directories

**Verdict:** Exemplary - deep frameworks across multiple social work domains.

---

### 2.3 Workflow Actionability (7/10)

**Strengths:**
- 4-phase generic workflow (Discovery → Analysis → Implementation → Review)
- Done/Fail criteria for each phase

**Areas for Improvement:**
- Workflow is generic (boilerplate), not social-worker specific
- No case management workflow, crisis intervention steps, or assessment templates

**Verdict:** Meets basic Expert threshold but could be domain-specific.

---

### 2.4 Risk Documentation (9/10)

**Strengths:**
- Structured risk table in §3 with 7 risks:
  - Mandatory Reporting (🔴 Critical)
  - Confidentiality Breach (🔴 Critical)
  - Boundary Violation (🔴 High)
  - Vicarious Trauma (🟡 High)
  - Safety Risk (🔴 Critical)
  - Case Overload (🟡 Medium)
  - Improper Discharge (🟡 High)
- Severity ratings and mitigation strategies

**Verdict:** Exemplary risk documentation.

---

### 2.5 Example Quality (7/10)

**Strengths:**
- Test cases in §14:
  - Crisis Intervention (SI/HI assessment)
  - Biopsychosocial Assessment (new client)
- §9 has 4 generic scenarios

**Areas for Improvement:**
- No full conversation flows in §9
- Generic scenarios don't show social work frameworks in action
- Missing: mandatory reporting scenario, strengths assessment example

**Verdict:** Basic examples present but could be more comprehensive.

---

### 2.6 Metadata Completeness (10/10)

**Strengths:**
- All 9 fields present
- Version 3.0.0
- Comprehensive tags (social-services, case-management, etc.)
- Score fields (8.1/10)

**Verdict:** Exemplary.

---

## 3. Top Issues & Rewrite Suggestions

### Issue 1: Generic Workflow (Priority: HIGH)

**Current:** 4-phase boilerplate workflow

**Suggested Rewrite:**
```markdown
## § 8 · Standard Workflow

### 8.1 Crisis Intervention Process
```
Phase 1: Immediate Safety
├── Assess immediate danger
├── De-escalate if needed
└── Activate crisis protocol if high risk

Phase 2: Assessment
├── Identify presenting problem
├── Assess ideation, plan, intent, means
└── Identify protective factors

Phase 3: Intervention
├── Safety plan development
├── Resource connection
└── Follow-up scheduling

Phase 4: Documentation & Follow-Up
├── Document assessment and plan
├── Coordinate with providers
└── Schedule follow-up
```

### Issue 2: Missing Platform Support (Priority: MEDIUM)

Add §5 Platform Support per standards.md §7.11.

---

## 4. Section Compliance Check

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 1 | System Prompt | ✅ Present | Excellent |
| 2 | What This Skill Does | ✅ Present | 8 functions |
| 3 | Risk Disclaimer | ✅ Present | 7 risks |
| 4 | Core Philosophy | ✅ Present | Ecological framework |
| 5 | Platform Support | ❌ Missing | - |
| 6 | Professional Toolkit | ✅ Present | - |
| 7 | Standards & Quality | ❌ Missing | - |
| 8 | Workflow | ⚠️ Generic | Needs SW-specific phases |
| 9 | Scenario Examples | ⚠️ Weak | Generic only |
| 10 | Common Pitfalls | ✅ Present | - |
| 11 | Integration | ✅ Present | - |
| 12 | Scope & Limitations | ✅ Present | - |
| 13 | How to Use | ❌ Missing | - |
| 14 | Quality Verification | ⚠️ Weak | - |
| 15 | Version History | ❌ Missing | - |
| 16 | License & Author | ✅ Present | MIT |

---

## 5. Token Budget Analysis

| Metric | Current | Target (Expert) | Status |
|--------|---------|------------------|--------|
| Total lines | 676 | 300-600 | ⚠️ Above target |
| System prompt | ~30 lines | 15-30 | ✅ In range |

---

## 6. Final Verdict

**Classification:** Expert Verified ⭐

**Upgrade Path to Exemplary:**
1. Add §5 Platform Support
2. Add §13 How to Use
3. Replace generic workflow with social-work specific phases (crisis, assessment, case management)
4. Expand §9 with full conversation flows

**Strengths:** Excellent system prompt and risk documentation  
**Weaknesses:** Generic workflow, minimal scenario examples, missing sections

---

## 7. Comparison: social-worker vs medical-social-worker

| Dimension | social-worker | medical-social-worker |
|-----------|--------------|----------------------|
| Scope | General SW (medical, psychiatric, child welfare, community) | Hospital-based MSW (discharge, care coordination) |
| System Prompt | 9/10 | 9/10 |
| Domain Knowledge | 9/10 (broader) | 9/10 (focused) |
| Risk Documentation | 9/10 (7 risks) | 9/10 (4 risks) |
| Workflow | Generic | Domain-specific (discharge) |
| Examples | Basic | Better (2 detailed MSW scenarios) |

**Recommendation:** Keep both skills. `medical-social-worker` is more specialized for hospital settings; `social-worker` is broader for community/clinical settings.
