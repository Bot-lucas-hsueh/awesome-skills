# Skill Evaluation Report: dietitian

**Skill:** `skills/healthcare/dietitian/SKILL.md`  
**Date:** 2026-03-24  
**Evaluator:** skill-writer methodology  

---

## 1. Executive Summary

| Metric | Score | Tier |
|--------|-------|------|
| **Weighted Average** | 8.1/10 | Expert ⭐ |
| System Prompt Depth | 8/10 | Expert |
| Domain Knowledge Density | 9/10 | Exemplary |
| Workflow Actionability | 7/10 | Expert |
| Risk Documentation | 6/10 | Community |
| Example Quality | 8/10 | Expert |
| Metadata Completeness | 10/10 | Exemplary |

**Classification:** Expert Verified  
**Recommendation:** Ready for production. Address risk documentation gaps for Exemplary tier.

---

## 2. Dimension Analysis

### 2.1 System Prompt Depth (8/10)

**Strengths:**
- Role definition with 12+ years clinical experience
- Python code blocks for Mifflin-St Jeor, activity factors, protein targets
- Decision frameworks with specific thresholds (protein g/kg by condition)
- Thinking patterns table present

**Areas for Improvement:**
- System prompt embedded in §1 but mixed with other content
- Consider separating core framework code from system prompt definition

**Verdict:** Strong foundation; meets Expert threshold.

---

### 2.2 Domain Knowledge Density (9/10)

**Strengths:**
- Deep frameworks with quantified metrics (Mifflin-St Jeor, protein targets 0.6-2.0 g/kg)
- Clinical assessment tools (SGA, MUST screening)
- MNT protocols for diabetes, CKD, enteral/parenteral nutrition
- Food-drug interactions with specific examples (warfarin/vitamin K, tyramine-MAOI)
- Sports nutrition with specific timing and targets

**Verdict:** Exemplary depth; specific thresholds throughout.

---

### 2.3 Workflow Actionability (7/10)

**Strengths:**
- 4 distinct phases with detailed steps
- Done/Fail criteria defined for each phase
- Templates present (SGA scoring, CKD diet example)

**Areas for Improvement:**
- Generic "Discovery & Assessment" language not dietitian-specific
- §8 workflow is boilerplate, not domain-specific
- Consider dietitian-specific workflow: Assessment → Diagnosis → Intervention → Monitoring

**Verdict:** Meets Expert threshold but could be more domain-specific.

---

### 2.4 Risk Documentation (6/10)

**Strengths:**
- Has §3 Risk Disclaimer (educational only)
- §10 "Gotchas & Anti-Patterns" has 5 clinical pitfalls with explanations

**Areas for Improvement:**
- §3 lacks structured risk matrix (no severity ratings, no escalation triggers)
- Risk content is brief (1 sentence generic disclaimer)
- Missing: counter-indications, adverse outcomes with severity levels

**Verdict:** Community level; needs formal risk matrix with severity.

---

### 2.5 Example Quality (8/10)

**Strengths:**
- 3 detailed clinical scenarios in core framework (§9):
  - Diabetes Carbohydrate Counting (with carb budgets, GI guidance, plate method)
  - Critical Care Enteral Nutrition (ICU case with formula, rates, advance protocol)
  - Weight Loss Plan (deficit calculation, macro breakdown, Mediterranean approach)
- SGA scoring example in Phase 1
- CKD diet example in Phase 2

**Verdict:** Strong examples covering major use cases.

---

### 2.6 Metadata Completeness (10/10)

**Strengths:**
- All 9 required fields present
- Version: 3.0.0, updated 2026-03-21
- Tags comprehensive
- Score fields present (7.8/10, 8.4 text, 7.1 runtime)

**Areas for Improvement:**
- Description is 263 chars (at limit); could add more triggers

**Verdict:** Exemplary completeness.

---

## 3. Top Issues & Rewrite Suggestions

### Issue 1: Risk Documentation (Priority: HIGH)

**Current:** Brief disclaimer in §3 + anti-patterns in §10

**Suggested Rewrite:**
```markdown
## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **High-protein in CKD** | 🔴 Critical | Protein 1.2 g/kg in non-dialysis CKD4 causes hyperfiltration | Verify GFR; use 0.6-0.8 g/kg |
| **Hypoglycemia risk** | 🔴 Critical | Low-carb without insulin adjustment in T1D causes hypoglycemia | Coordinate with prescriber |
| **Phosphorus additives** | 🟡 High | Inorganic phosphate 100% absorbed vs 40-60% organic | Read labels; avoid processed foods |
| **Malnutrition misdiagnosis** | 🟠 Moderate | Using BMI in edema overestimates nutritional needs | Use dry weight |
```

### Issue 2: Workflow Not Domain-Specific (Priority: MEDIUM)

**Current:** Generic "Discovery & Assessment" phases

**Suggested Rewrite:** Replace §8 with dietitian-specific workflow:
```
Phase 1: Nutrition Assessment
├── SGA scoring (weight trend, intake, GI, function, physical exam)
├── Anthropometrics (BMI, waist circumference, MUAMC)
└── Lab interpretation (albumin, prealbumin, CRP)

Phase 2: MNT Diagnosis & Planning
├── Identify nutrition diagnosis (e.g., "inadequate caloric intake")
├── Set SMART goals with patient
└── Design meal plan based on condition

Phase 3: Intervention Implementation
├── Patient education on modified diet
├── Coordinate with culinary/OT for meal prep
└── Schedule follow-up

Phase 4: Monitoring & Evaluation
├── Track weight, labs, symptom resolution
├── Adjust plan as needed
└── Discharge when goals met
```

---

## 4. Section Compliance Check

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 1 | System Prompt | ✅ Present | Embedded in content; could separate |
| 2 | What This Skill Does | ✅ Present | 6 capabilities |
| 3 | Risk Disclaimer | ⚠️ Weak | Needs risk matrix |
| 4 | Core Philosophy | ✅ Present | Guiding principles |
| 5 | Platform Support | ❌ Missing | No platform install instructions |
| 6 | Professional Toolkit | ✅ Present | Tables present |
| 7 | Standards & Quality | ❌ Missing | No self-test section |
| 8 | Workflow | ⚠️ Generic | Needs dietitian-specific phases |
| 9 | Scenario Examples | ✅ Present | 3 detailed examples |
| 10 | Common Pitfalls | ✅ Present | Gotchas section |
| 11 | Integration | ✅ Present | GP, Clinical Pharmacist |
| 12 | Scope & Limitations | ✅ Present | Explicit boundaries |
| 13 | How to Use | ❌ Missing | No install/usage instructions |
| 14 | Quality Verification | ⚠️ Weak | References external only |
| 15 | Version History | ❌ Missing | In metadata only |
| 16 | License & Author | ✅ Present | MIT |

**Missing Sections:** 5 (Platform), 7 (Standards), 13 (How to Use)  
**Weak Sections:** 3 (Risk), 8 (Workflow), 14 (Quality)

---

## 5. Token Budget Analysis

| Metric | Current | Target (Expert) | Status |
|--------|---------|------------------|--------|
| Total lines | 650 | 300-600 | ⚠️ Above target |
| System prompt | ~30 lines | 15-30 | ✅ In range |
| §9 scenarios | 3 full flows | 2+ full flows | ✅ Met |

**Recommendation:** Consider moving §16-21 (Domain Deep Dive through Resources) to `references/` to reduce token cost.

---

## 6. Final Verdict

**Classification:** Expert Verified ⭐

**Upgrade Path to Exemplary:**
1. Add structured risk matrix in §3 with 5+ risks, severity ratings, escalation triggers
2. Add §5 Platform Support (per standards.md §7.11)
3. Add §13 How to Use with install instructions
4. Add self-test in §14 Quality Verification
5. Make §8 workflow dietitian-specific

**Strengths:** Excellent domain knowledge, strong examples, comprehensive metadata  
**Weaknesses:** Risk documentation not formal, missing platform support section
