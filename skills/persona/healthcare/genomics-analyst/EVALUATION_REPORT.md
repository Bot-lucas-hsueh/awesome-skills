# Skill Evaluation Report: genomics-analyst

## Summary
| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| System Prompt Depth | 9/10 | 20% | 1.80 |
| Domain Knowledge Density | 9/10 | 25% | 2.25 |
| Workflow Actionability | 8/10 | 15% | 1.20 |
| Risk Documentation | 7/10 | 10% | 0.70 |
| Example Quality | 9/10 | 20% | 1.80 |
| Metadata Completeness | 9/10 | 10% | 0.90 |
| **TOTAL** | | 100% | **8.75** |

**Tier: Expert ⭐⭐ (Exemplary)**

---

## Dimension Analysis

### 1. System Prompt Depth (9/10)
**Strengths:**
- Role with 12+ years, ACMG/ABMGG board certification
- Clear identity: clinical variant curation, NGS pipelines, genomic translator
- Decision framework with 3 gates (ACMG criteria, clinically actionable vs incidental, clinical correlation)
- Thinking patterns: Evidence Hierarchy, Gene-Disease Validity, Bayesian Thinking

**Areas for Improvement:**
- Excellent — no significant gaps

### 2. Domain Knowledge Density (9/10)
**Strengths:**
- ACMG Variant Classification Pyramid (ASCII diagram) — excellent
- Variant interpretation workflow with 5 phases
- Quality metrics table with targets (>95% coverage, >100x depth, >80% Q30)
- Tools: ClinVar, ClinGen, gnomAD, HGMD, SIFT/PolyPhen, VEP

**Areas for Improvement:**
- Could add more gene-specific interpretation examples

### 3. Workflow Actionability (8/10)
**Strengths:**
- Variant Interpretation: 5 phases with detailed steps
- NGS Data Quality Assessment: 6-step process

**Areas for Improvement:**
- Missing [✓ Done] checkpoints per step

### 4. Risk Documentation (7/10)
**Strengths:**
- 4 risks (Incorrect Variant Classification, VUS Misinterpretation, Incidental Findings, Data Quality)
- Severity ratings and mitigation strategies

**Areas for Improvement:**
- Could add more domain-specific escalation triggers

### 5. Example Quality (9/10)
**Strengths:**
- Excellent BRCA1 classification example with full ACMG criteria table
- VUS handling with patient communication script
- Shows actual reasoning, not just templates

**Areas for Improvement:**
- §9 Scenarios 1-4 are generic templates
- Could add more variant types (deletion, splice site, copy number)

### 6. Metadata Completeness (9/10)
**Strengths:**
- All required fields
- Description ~271 chars (slightly over, but acceptable)
- Proper category, difficulty, tags

**Areas for Improvement:**
- YAML frontmatter duplicates description
- Extra fields in metadata block

---

## Critical Issues

| Issue | Severity | Description |
|-------|----------|-------------|
| §9 Generic Scenarios | 🟡 | Scenarios 1-4 are template placeholders |
| Redundant Sections | 🟡 | §16-21 duplicate generic content |
| YAML Duplication | 🟢 | Description repeated in metadata |

---

## Recommendations

1. Replace §9 Scenarios 1-4 with real genomics examples (e.g., splice site variant, copy number variant)

2. Trim redundant §16-21 content

---

## Verdict

**Expert ⭐⭐ — Exemplary**

Strong ACMG framework alignment, excellent variant interpretation workflow, best example quality among the 5 skills. Minor cleanup for token efficiency.