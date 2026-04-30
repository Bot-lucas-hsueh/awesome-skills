# Skill Evaluation Report: radiologist

**Skill:** `skills/healthcare/radiologist/SKILL.md`  
**Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  

---

## 1. Executive Summary

| Metric | Score | Tier |
|--------|-------|------|
| **Weighted Average** | 7.9/10 | Expert ⭐ |
| System Prompt Depth | 8/10 | Expert |
| Domain Knowledge Density | 9/10 | Exemplary |
| Workflow Actionability | 7/10 | Expert |
| Risk Documentation | 6/10 | Community |
| Example Quality | 8/10 | Expert |
| Metadata Completeness | 10/10 | Exemplary |

**Classification:** Expert Verified  
**Recommendation:** Production-ready. Address risk documentation for Exemplary tier.

---

## 2. Dimension Analysis

### 2.1 System Prompt Depth (8/10)

**Strengths:**
- Board-certified diagnostic radiologist, 15+ years
- Subspecialty experience listed (body imaging, neuroradiology, MSK, breast, IR)
- Structured reporting frameworks mentioned (BI-RADS, TI-RADS, Fleischner, LI-RADS)
- Radiation dose calculation, ALARA principles
- Contrast safety screening

**Areas for Improvement:**
- No explicit decision framework gates
- No thinking patterns table
- System prompt is descriptive, not prescriptive

**Verdict:** Strong but lacks decision framework structure.

---

### 2.2 Domain Knowledge Density (9/10)

**Strengths:**
- Python functions for CT density characterization, radiation dose estimation, contrast safety screening
- BI-RADS categories table with cancer risk percentages
- Fleischner Society guidelines (2017) with Python implementation
- Systematic review approach (ABCDE for chest X-ray)
- ACR Appropriateness Criteria rating scale
- Contrast thresholds by eGFR

**Verdict:** Exemplary - specific thresholds and calculations.

---

### 2.3 Workflow Actionability (7/10)

**Strengths:**
- 4-phase generic workflow
- Done/Fail criteria for each phase

**Areas for Improvement:**
- Workflow is boilerplate, not radiologist-specific
- Missing: image interpretation workflow, reporting workflow, QA process

**Verdict:** Basic Expert threshold.

---

### 2.4 Risk Documentation (6/10)

**Strengths:**
- §3 Risk Disclaimer present
- Risk table with 4 mitigation items

**Areas for Improvement:**
- Risks lack severity ratings (🔴🟠🟡)
- No escalation triggers
- Brief content

**Verdict:** Community level - needs formal risk matrix.

---

### 2.5 Example Quality (8/10)

**Strengths:**
- §8 has "Scenario 2: Complex Problem Solving" with radiologist context
- §9 scenario examples (Initial Consultation, Problem Resolution, Strategic Planning)
- Pitfalls section in §8 with 5 common errors:
  - Satisfaction of search
  - Overcalling density
  - Ignoring incidental findings
  - Adult contrast thresholds for pediatric
  - SUV confusion on PET

**Areas for Improvement:**
- No full conversation flows showing structured reporting
- Missing: BI-RADS reporting example, Fleischner recommendation example

**Verdict:** Good but could use full flows.

---

### 2.6 Metadata Completeness (10/10)

**Strengths:**
- All 9 fields complete
- Version 3.0.0
- Comprehensive tags
- Score fields (7.6/10)

**Verdict:** Exemplary.

---

## 3. Top Issues & Rewrite Suggestions

### Issue 1: Risk Documentation (Priority: HIGH)

**Current:** Brief risk section without severity

**Suggested Rewrite:**
```markdown
## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Missed diagnosis** | 🔴 Critical | Satisfaction of search error | Systematic review approach; clinical correlation |
| **Contrast-induced nephropathy** | 🔴 Critical | CIN in low eGFR patients | eGFR screening; hydration protocol |
| **Radiation exposure** | 🟠 High | Excessive dose without justification | ALARA; clinical indication required |
| **Incidental findings** | 🟡 Medium | Follow-up not recommended | Fleischner guidelines; document recommendation |
```

### Issue 2: Decision Framework (Priority: MEDIUM)

Add decision gates to §1:
```
| Gate | Question | Action |
|------|----------|--------|
| 1 | Modality selected? | Verify ACR Appropriateness Criteria rating |
| 2 | Contrast needed? | Screen eGFR, allergy history |
| 3 | Prior studies available? | Compare for change assessment |
| 4 | Incidental finding? | Apply follow-up guidelines |
```

---

## 4. Section Compliance Check

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 1 | System Prompt | ⚠️ Partial | Missing decision gates |
| 2 | What This Skill Does | ✅ Present | 6 capabilities |
| 3 | Risk Disclaimer | ⚠️ Weak | Needs severity matrix |
| 4 | Core Philosophy | ✅ Present | - |
| 5 | Platform Support | ❌ Missing | - |
| 6 | Professional Toolkit | ✅ Present | - |
| 7 | Standards & Quality | ❌ Missing | - |
| 8 | Workflow | ⚠️ Generic | - |
| 9 | Scenario Examples | ⚠️ Partial | - |
| 10 | Common Pitfalls | ✅ Present | - |
| 11 | Integration | ✅ Present | GP, Clinical Pharmacist, Epidemiologist |
| 12 | Scope & Limitations | ✅ Present | - |
| 13 | How to Use | ⚠️ Present | URL only |
| 14 | Quality Verification | ⚠️ Weak | - |
| 15 | Version History | ❌ Missing | - |
| 16 | License & Author | ✅ Present | MIT |

---

## 5. Token Budget Analysis

| Metric | Current | Target (Expert) | Status |
|--------|---------|------------------|--------|
| Total lines | 814 | 300-600 | ⚠️ Above target |
| System prompt | ~10 lines | 15-30 | ⚠️ Below range |

---

## 6. Final Verdict

**Classification:** Expert Verified ⭐

**Upgrade Path to Exemplary:**
1. Add decision framework gates to §1
2. Add structured risk matrix to §3 with severity ratings
3. Add §5 Platform Support
4. Add §7 Standards with self-test
5. Make §8 workflow radiology-specific (interpretation → reporting → QA)

**Strengths:** Excellent domain knowledge (Python functions, BI-RADS, Fleischner), comprehensive metadata  
**Weaknesses:** Risk documentation weak, system prompt lacks decision structure, missing sections

---

## 7. Clinical Value Assessment

This skill provides strong educational value for:
- Imaging modality selection (ACR Appropriateness Criteria)
- Structured reporting (BI-RADS, TI-RADS, Fleischner)
- Radiation dose calculation
- Contrast safety screening

The Python functions are particularly valuable - they provide specific, implementable calculations.
