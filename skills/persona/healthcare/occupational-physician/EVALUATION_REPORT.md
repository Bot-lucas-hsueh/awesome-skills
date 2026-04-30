# Skill Evaluation Report: occupational-physician

## 1. Metadata Summary

| Field | Value |
|-------|-------|
| Name | occupational-physician |
| Version | 3.0.0 |
| Category | healthcare |
| Difficulty | intermediate |
| Current Score | 8.4/10 |
| Quality | production |

## 2. Six-Dimension Evaluation

### Dimension 1: Prompt Quality (20%)
**Score: 9.3/10**

| Criteria | Assessment |
|----------|------------|
| Role definition clarity | ✅ Board-certified, ACOEM, MRO certification |
| Decision framework | ✅ 3 gates (compensability, OSHA, fitness) |
| Thinking patterns | ✅ 3 dimensions (causation, compliance, restoration) |
| Communication style | ✅ Documented, standard-referenced, collaborative |

**Strengths:**
- Clear OSHA regulatory focus
- NIOSH causation criteria
- Functional restoration focus

---

### Dimension 2: Domain Knowledge (25%)
**Score: 9.5/10**

| Criteria | Assessment |
|----------|------------|
| Depth of expertise | ✅ OSHA, NIOSH, ILO frameworks |
| Technical accuracy | ✅ 29 CFR 1910/1926, PELs, TLVs |
| Practical applicability | ✅ Causation analysis, return-to-work |

**Strengths:**
- OSHA recordkeeping (29 CFR 1904)
- NIOSH causation criteria
- AMA Guides for functional capacity
- ILO pneumoconiosis classification

**Gaps:**
- Could include more on emerging occupational health issues (psychosocial, remote work)

---

### Dimension 3: Workflow Clarity (15%)
**Score: 8.8/10**

| Criteria | Assessment |
|----------|------------|
| Workflow completeness | ✅ 4-phase illness evaluation, 5-step RTW |
| Step specificity | ✅ Detailed phases |
| Reproducibility | ✅ Clear protocols |

**Strengths:**
- Occupational health triangle in §4.1
- Exposure assessment phases
- Return-to-work evaluation steps

**Issues:**
- §9 Scenarios 1-4 generic filler

---

### Dimension 4: Risk Documentation (10%)
**Score: 9.4/10**

| Criteria | Assessment |
|----------|------------|
| Risk identification | ✅ 5 occupational-specific risks |
| Mitigation clarity | ✅ NIOSH criteria, documentation emphasis |
| Warning emphasis | ✅ ⚠️ IMPORTANT with independence clause |

**Strengths:**
- Misdiagnosis of work-relatedness as top risk
- OSHA recordkeeping failures
- Silent conditions (silicosis, asbestosis)

---

### Dimension 5: Examples Quality (20%)
**Score: 9.0/10**

| Criteria | Assessment |
|----------|------------|
| Scenario relevance | ✅ 2 occupational scenarios (NIHL, back injury) |
| Example depth | ✅ NIOSH criteria tables, functional assessment |
| Domain specificity | ✅ OSHA/occupational-specific |

**Strengths:**
- 9.1 noise-induced hearing loss with NIOSH criteria
- 9.2 return-to-work with AMA Guides framework

**Issues:**
- §9 Scenarios 1-4 boilerplate

---

### Dimension 6: Metadata Completeness (10%)
**Score: 9.5/10**

| Field | Status |
|-------|--------|
| name | ✅ Valid |
| description | ✅ 263 chars, includes Chinese trigger |
| license | ✅ MIT |
| metadata fields | ✅ All 9 fields present |
| YAML validity | ✅ Clean |

---

## 3. Overall Score Calculation

| Dimension | Weight | Score |
|-----------|--------|-------|
| Prompt Quality | 20% | 9.3 |
| Domain Knowledge | 25% | 9.5 |
| Workflow Clarity | 15% | 8.8 |
| Risk Documentation | 10% | 9.4 |
| Examples Quality | 20% | 9.0 |
| Metadata | 10% | 9.5 |
| **Total** | 100% | **9.18/10** |

**Tier: Expert** (≥7.0)

---

## 4. Anti-Pattern Detection

| # | Anti-Pattern | Severity | Status |
|---|--------------|----------|--------|
| 1 | Generic Scenarios in §9 | 🟡 | Boilerplate, not occ-phys specific |
| 2 | Boilerplate Sections 16-21 | 🟡 | Generic content |
| 3 | Over 500 lines | 🔴 | 596 lines exceeds budget |
| 4 | Truncated Tool Table | 🟡 | §6 ends abruptly with "SPO2" |

---

## 5. Recommended Actions

| Priority | Action | Impact |
|----------|--------|--------|
| 🔴 HIGH | Move generic §9 scenarios to references/ | Reduce ~80 lines |
| 🔴 HIGH | Remove/reduce §§16-21 boilerplate | Reduce ~150 lines |
| 🔴 HIGH | Fix truncated §6 tool table | Complete table or remove |
| 🟡 MEDIUM | Add psychosocial workplace health | Improve relevance |

---

## 6. Evaluation Summary

| Aspect | Result |
|--------|--------|
| Tier | Expert ⭐ |
| Overall Score | 9.18/10 |
| Primary Strengths | OSHA/NIOSH integration, causation framework, RTW protocols |
| Primary Weaknesses | Generic filler, line count, truncated table |
| Token Budget | ⚠️ 596 lines (exceeds 500 limit) |

**Recommendation:** Fix §6 table, trim boilerplate. After cleanup: ~370 lines, score ~9.5/10.
