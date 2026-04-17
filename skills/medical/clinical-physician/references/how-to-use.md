## § 7 · How to Use

```
Read https://theneoai.github.io/awesome-skills/skills/medical/clinical-physician/SKILL.md and install
```

Typical prompts: "Walk me through a systematic differential for acute dyspnea in a 65yo," "Calculate HEART score for this chest pain presentation," "Teach me DKA management step by step," "Apply Bayesian reasoning to a positive D-dimer with low pre-test PE probability."

---

## 7b. Quality Verification

Ask: "Calculate Wells PE score for: DVT signs present, PE is primary diagnosis, HR 112, immobilization from 6-hour flight, no prior DVT/PE, no hemoptysis, no malignancy."

**Expected response elements:**
- DVT signs: +3; PE primary dx: +3; HR>100: +1.5; immobilization: +1.5 = total 9.0
- Score >6 → HIGH probability; PE prevalence ~67%
- Recommendation: CTPA immediately; do not wait for D-dimer (D-dimer is for LOW/MODERATE pretest only)
- Anticoagulation consideration while awaiting CTPA if no contraindication
- ⚠️ Educational disclaimer included

---
