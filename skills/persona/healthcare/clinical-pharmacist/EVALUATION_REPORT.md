# Skill Evaluation Report: clinical-pharmacist

**Skill:** `skills/healthcare/clinical-pharmacist/SKILL.md`  
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
**Recommendation:** Production-ready. Similar to radiologist - strong domain knowledge, weak risk documentation.

---

## 2. Dimension Analysis

### 2.1 System Prompt Depth (8/10)

**Strengths:**
- PharmD-credentialed, 12+ years experience
- Hospital (ICU, oncology, cardiology), ambulatory care, MTM
- Pharmacokinetic/pharmacodynamic reasoning mentioned
- CrCl-based dosing, Child-Pugh, CYP450 interactions
- TDM (vancomycin AUC-guided dosing)
- MICROMEDEX, Lexicomp, Beers Criteria reference

**Areas for Improvement:**
- No decision framework gates
- No thinking patterns table
- Descriptive rather than prescriptive

**Verdict:** Strong but lacks decision structure.

---

### 2.2 Domain Knowledge Density (9/10)

**Strengths:**
- Python functions for Cockcroft-Gault CrCl calculation
- Renal dosing guide table (Vancomycin, Piperacillin-Tazobactam, Ciprofloxacin, Metformin)
- Vancomycin AUC-guided dosing (2020 ASHP/IDSA guidelines)
- Drug interaction 4-step assessment framework
- Antimicrobial PK/PD targets table
- Beers Criteria screening
- CMR (Comprehensive Medication Review) checklist

**Verdict:** Exemplary - specific thresholds, dosing tables, guidelines.

---

### 2.3 Workflow Actionability (7/10)

**Strengths:**
- 4-phase generic workflow
- Done/Fail criteria for each phase

**Areas for Improvement:**
- Workflow is boilerplate, not pharmacy-specific
- Missing: medication reconciliation workflow, TDM workflow, antimicrobial stewardship workflow

**Verdict:** Basic Expert threshold.

---

### 2.4 Risk Documentation (6/10)

**Strengths:**
- §3 Risk Disclaimer present
- 4 risk mitigation items in table format

**Areas for Improvement:**
- No severity ratings (🔴🟠🟡)
- No escalation triggers
- Brief content

**Verdict:** Community level - needs formal risk matrix.

---

### 2.5 Example Quality (8/10)

**Strengths:**
- §8 has scenario examples with clinical pharmacist context
- §9 scenarios (Initial Consultation, Problem Resolution, Strategic Planning)
- Pitfalls section with 5 common errors:
  - SCr alone without CrCl
  - Trough-only vancomycin
  - Dismissing moderate interactions
  - Forgetting oral antibiotic renal adjustments
  - CYP2D6 phenotype with codeine

**Areas for Improvement:**
- No full conversation flows
- Missing: actual drug interaction analysis example, CrCl calculation example

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

**Current:** Brief risks without severity

**Suggested Rewrite:**
```markdown
## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Significant drug interactions** | 🔴 Critical | Contraindicated/major interactions | Classify severity; consult prescriber |
| **Narrow TI drug toxicity** | 🔴 Critical | Toxicity from improper dosing | TDM; conservative dose changes |
| **Renal dosing errors** | 🔴 Critical | Wrong dose in CKD | Calculate CrCl; use dosing tables |
| **Beers Criteria meds in elderly** | 🟠 High | Inappropriate prescribing in ≥65 | Screen; discuss alternatives |
```

### Issue 2: Decision Framework (Priority: MEDIUM)

Add gates to §1:
```
| Gate | Question | Action |
|------|----------|--------|
| 1 | New medication? | Verify indication, dose, interactions |
| 2 | Renal impairment? | Calculate CrCl; adjust dose |
| 3 | Elderly patient? | Screen Beers Criteria |
| 4 | Antimicrobial? | Verify PK/PD target, de-escalation plan |
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
| 11 | Integration | ✅ Present | GP, Epidemiologist |
| 12 | Scope & Limitations | ✅ Present | - |
| 13 | How to Use | ⚠️ Present | URL only |
| 14 | Quality Verification | ⚠️ Weak | - |
| 15 | Version History | ❌ Missing | - |
| 16 | License & Author | ✅ Present | MIT |

---

## 5. Token Budget Analysis

| Metric | Current | Target (Expert) | Status |
|--------|---------|------------------|--------|
| Total lines | 692 | 300-600 | ⚠️ Above target |
| System prompt | ~10 lines | 15-30 | ⚠️ Below range |

---

## 6. Final Verdict

**Classification:** Expert Verified ⭐

**Upgrade Path to Exemplary:**
1. Add decision framework gates to §1
2. Add structured risk matrix to §3 with severity ratings
3. Add §5 Platform Support
4. Add §7 Standards with self-test
5. Make §8 workflow pharmacy-specific (medication review → intervention → monitoring)

**Strengths:** Excellent domain knowledge (CrCl calculator, renal dosing tables, AUC-guided vancomycin, Beers Criteria)  
**Weaknesses:** Risk documentation weak, system prompt lacks decision structure, missing sections

---

## 7. Clinical Value Assessment

This skill provides strong educational value for:
- Drug interaction analysis (CYP450, severity classification)
- Renal dose adjustment (Cockcroft-Gault, dosing tables)
- Antimicrobial stewardship (PK/PD targets, de-escalation)
- Geriatric pharmacology (Beers Criteria)
- Therapeutic drug monitoring (vancomycin AUC)

The Python CrCl calculator and renal dosing guide are particularly valuable for clinical practice.
