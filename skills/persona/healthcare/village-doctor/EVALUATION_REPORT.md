# Skill Evaluation Report: village-doctor

## 1. Metadata Summary

| Field | Value |
|-------|-------|
| Name | village-doctor |
| Version | 3.0.0 |
| Category | healthcare |
| Difficulty | intermediate |
| Current Score | 8.5/10 |
| Quality | production |

## 2. Six-Dimension Evaluation

### Dimension 1: Prompt Quality (20%)
**Score: 9.3/10**

| Criteria | Assessment |
|----------|------------|
| Role definition clarity | ✅ Rural health practitioner, limited resources |
| Decision framework | ✅ 4 gates (resources, referral, prevention, public health) |
| Thinking patterns | ✅ 4 dimensions (constraints, community, prevention, referral) |
| Communication style | ✅ Plain language, culturally sensitive, family-inclusive |

**Strengths:**
- Clear resource constraint acknowledgment
- Community-centered approach
- Referral threshold emphasis

---

### Dimension 2: Domain Knowledge (25%)
**Score: 9.4/10**

| Criteria | Assessment |
|----------|------------|
| Depth of expertise | ✅ Basic medicine, public health, referral triage |
| Technical accuracy | ✅ IMCI, WHO emergency signs, red flags |
| Practical applicability | ✅ Essential medicines, basic diagnostics |

**Strengths:**
- IMCI framework for childhood illness
- WHO emergency signs (ABCDE)
- Red flag checklist
- Essential medicines concept

**Gaps:**
- Could expand on tropical diseases specific to rural areas

---

### Dimension 3: Workflow Clarity (15%)
**Score: 9.0/10**

| Criteria | Assessment |
|----------|------------|
| Workflow completeness | ✅ 4-phase patient encounter, 5-step referral |
| Step specificity | ✅ Detailed sub-steps |
| Reproducibility | ✅ Clear protocols |

**Strengths:**
- Visual decision matrix in §4.1
- Patient encounter phases
- Referral decision flowchart

**Issues:**
- §9 Scenarios 1-4 generic filler

---

### Dimension 4: Risk Documentation (10%)
**Score: 9.3/10**

| Criteria | Assessment |
|----------|------------|
| Risk identification | ✅ 5 risks specific to rural medicine |
| Mitigation clarity | ✅ Resource-aware mitigation |
| Warning emphasis | ✅ ⚠️ IMPORTANT with scope boundaries |

**Strengths:**
- Missed diagnosis risk with mitigation
- Inappropriate treatment, delayed referral
- Clear scope of practice guidance

---

### Dimension 5: Examples Quality (20%)
**Score: 9.2/10**

| Criteria | Assessment |
|----------|------------|
| Scenario relevance | ✅ 2 realistic rural scenarios |
| Example depth | ✅ Clinical detail, red flag recognition |
| Domain specificity | ✅ Village doctor-specific |

**Strengths:**
- 9.1 URI management with health education
- 9.2 pediatric fever with red flag recognition
- Parental concern ("not playing normally") as critical indicator

**Issues:**
- §9 Scenarios 1-4 boilerplate

---

### Dimension 6: Metadata Completeness (10%)
**Score: 9.5/10**

| Field | Status |
|-------|--------|
| name | ✅ Valid |
| description | ✅ Appropriate length |
| license | ✅ MIT |
| metadata fields | ✅ All 9 fields present |
| YAML validity | ✅ Clean |

---

## 3. Overall Score Calculation

| Dimension | Weight | Score |
|-----------|--------|-------|
| Prompt Quality | 20% | 9.3 |
| Domain Knowledge | 25% | 9.4 |
| Workflow Clarity | 15% | 9.0 |
| Risk Documentation | 10% | 9.3 |
| Examples Quality | 20% | 9.2 |
| Metadata | 10% | 9.5 |
| **Total** | 100% | **9.24/10** |

**Tier: Expert** (≥7.0)

---

## 4. Anti-Pattern Detection

| # | Anti-Pattern | Severity | Status |
|---|--------------|----------|--------|
| 1 | Generic Scenarios in §9 | 🟡 | Boilerplate |
| 2 | Boilerplate Sections 16-21 | 🟡 | Generic content |
| 3 | Over 500 lines | 🔴 | 597 lines exceeds budget |

---

## 5. Recommended Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 HIGH | Move generic §9 scenarios to references/ | Reduce ~80 lines |
| 🔴 HIGH | Remove/reduce §§16-21 boilerplate | Reduce ~150 lines |
| 🟡 MEDIUM | Add tropical disease protocols | Improve regional relevance |

---

## 6. Evaluation Summary

| Aspect | Result |
|--------|--------|
| Tier | Expert ⭐ |
| Overall Score | 9.24/10 |
| Primary Strengths | Resource consciousness, referral thresholds, community focus |
| Primary Weaknesses | Generic filler, line count |
| Token Budget | ⚠️ 597 lines (exceeds 500 limit) |

**Recommendation:** Trim boilerplate. After cleanup: ~370 lines, score ~9.6/10.
