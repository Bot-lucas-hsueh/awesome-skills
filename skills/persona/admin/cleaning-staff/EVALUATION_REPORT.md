# Evaluation Report — cleaning-staff

## Skill Summary
| Field | Value |
|-------|-------|
| **Name** | cleaning-staff |
| **Version** | 1.0.0 |
| **Quality Tier** | Expert ⭐ |
| **Rubric Score** | 7.7/10 |
| **Line Count** | 657 |

---

## 6-Dimension Rubrubric Scores

| Dimension | Score | Weight | Weighted | Tier |
|-----------|-------|--------|----------|------|
| System Prompt Depth | 7.5 | 20% | 1.50 | Expert |
| Domain Knowledge Density | 7.5 | 25% | 1.875 | Expert |
| Workflow Actionability | 7.5 | 15% | 1.125 | Expert |
| Risk Documentation | 8.5 | 10% | 0.85 | Expert |
| Example Quality | 7.5 | 20% | 1.50 | Expert |
| Metadata Completeness | 7.5 | 10% | 0.75 | Expert |

---

## Strengths

### §1 System Prompt
- 15+ years, hospital-grade sanitation, ISSA certification
- Cleaning Hierarchy Framework (ASCII diagram: Sanitation → Disinfect → Clean → Remove)
- Specific certifications (OSHA bloodborne pathogens, EPA-registered disinfectants)
- Contact time awareness, cross-contamination prevention
- Chemical-specific knowledge (quaternary ammonium, hydrogen peroxide, enzymatic)

### §3 Risk Documentation — Strong
- 6 risks (4 🔴 High, 2 🟡 Medium)
- Bleach + ammonia toxicity warning
- EPA-registered disinfectant guidance
- Specific product names (Lysol, Clorox Hydrogen Peroxide)
- Dwell time non-negotiable warning

### §6 Professional Toolkit
- Specific tools with detailed descriptions (microfiber cloths, HEPA vacuum, steam cleaner)
- UV-C light scanner for bacteria detection
- pH test strips

### §7 Standards & Reference
- Disinfectant Contact Times table (5 types with dwell times: 10min quaternary ammonium, 1-5min hydrogen peroxide, 30sec IPA)
- Surface-Specific Cleaning Matrix (8 surfaces with pH requirements, techniques, and avoid list)
- **Verdict**: Excellent density — specific products, pH values, contact times

### §8 Workflow
- Complete Room Deep Clean (4 phases with specific steps)
- Move-In/Move-Out Deep Clean (9 steps)
- Very actionable with timing estimates

### §9 Examples
- §9.1: Kitchen deep clean after dinner party (table with area/product/technique/time)
- §9.2: Bathroom sanitization (priority order table, product selection)
- Both are practical with specific product recommendations

---

## Weaknesses

### ❌ Line Count Over Budget (Severity: High)
- **657 lines** — exceeds 500-line limit by 157 lines

### ❌ Missing §5 Platform Support
- No platform installation section

### ❌ Duplicate Generic Scenarios
- §9 Scenario Examples section with generic templates

### ❌ Duplicate Boilerplate Sections (Severity: High)
- §16-21 boilerplate (~150 lines)

### ❌ Duplicate §6 Professional Toolkit
- Lines 195-206 and 210-227 both contain toolkit content
- Second §6 is generic filler

### ❌ Non-Standard Metadata
- 10-field block
- Has `certified: true` which is non-standard

---

## Anti-Patterns Detected

| # | Anti-Pattern | Severity | Location |
|---|-------------|----------|----------|
| #4 | Token Waste — 657 lines | 🔴 High | Entire file |
| #4 | Token Waste — boilerplate + duplicate §6 | 🔴 High | §16-21, §6 duplicate |
| #9 | Platform Coverage Miss | 🔴 High | Missing section |
| — | Non-standard metadata | 🟡 Medium | Lines 8-17 |

---

## Token Budget Analysis

| Metric | Current | Target | Status |
|--------|---------|--------|--------|
| SKILL.md lines | 657 | ≤500 | ❌ Over by 157 lines |
| Post-cleanup estimate | ~500 lines | ≤500 | ✅ At target |

---

## Recommendation

**Tier: Expert ⭐** (7.7/10)

Best-in-class domain density among admin skills — specific disinfectant products, pH values, contact times, surface-specific guidance. Identical structural issues (boilerplate, missing platform support). The content quality is highest in the admin category.

**Immediate actions required:**
1. Strip boilerplate (§16-21) and duplicate §6
2. Add §5 Platform Support
3. Fix metadata

After cleanup: Estimated score → 8.2/10 Expert ⭐
