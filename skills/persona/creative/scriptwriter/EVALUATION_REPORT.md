# Scriptwriter Skill Evaluation Report

## Overview
- **Skill:** scriptwriter
- **Location:** skills/creative/scriptwriter/SKILL.md
- **Current Score:** 7.1/10 (Expert - needs structural fixes)
- **Target:** Exemplary ≥9.0

---

## 6-Dimensional Analysis

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| **Prompt** | 8.5/10 | 20% | 1.70 |
| **Domain Knowledge** | 8.0/10 | 25% | 2.00 |
| **Workflow** | 7.0/10 | 15% | 1.05 |
| **Risk** | 7.5/10 | 10% | 0.75 |
| **Examples** | 6.0/10 | 20% | 1.20 |
| **Metadata** | 4.0/10 | 10% | 0.40 |
| **TOTAL** | | | **7.10** |

---

## Before/After Analysis

### Before (Current State)
- **Section numbering:** Completely broken - missing §5, has 9.1 then §9, jumps to §16-§21
- **Empty space:** 52 empty lines (lines 21-72)
- **Description:** Duplicated text in YAML
- **Examples §9:** Contains generic business content, NOT scriptwriting scenarios
- **Sections §16-§21:** Non-existent sections with irrelevant content

### After (Target State)
- Standard 14-section structure per TEMPLATE.md
- All content relevant to scriptwriting
- Clean section numbering
- No empty wasted lines

---

## Issues Found

### 🔴 Critical Issues

| # | Issue | Location | Fix Required |
|---|-------|----------|--------------|
| 1 | **Missing §5 (Platform Support)** | N/A | Add platform installation table |
| 2 | **Wrong content in §9** | Lines 333-427 | Replace with scriptwriting scenarios |
| 3 | **Non-existent sections §16-§21** | Lines 506-620 | Remove entirely |
| 4 | **Section numbering chaos** | Throughout | Renumber to standard 1-14 |

### 🟡 High Issues

| # | Issue | Location | Fix Required |
|---|-------|----------|--------------|
| 5 | **52 empty lines** | Lines 21-72 | Remove |
| 6 | **Description duplication** | Line 5 | Fix YAML description |
| 7 | **Missing §13 (How to Use)** | N/A | Add trigger words + install info |
| 8 | **Missing §14 (License)** | N/A | Add license section |

### 🟢 Minor Issues

| # | Issue | Location | Fix Required |
|---|-------|----------|--------------|
| 9 | **Trigger words could be more specific** | §12 | Narrow to 4-6 high-precision triggers |

---

## Concrete Fix Recommendations

### Priority 1: Structural Fixes
1. **Remove lines 21-72** (empty space)
2. **Remove lines 506-620** (§16-§21 - non-existent sections)
3. **Add missing §5** - Platform Support table
4. **Add missing §13** - How to Use This Skill
5. **Add missing §14** - License & Author

### Priority 2: Content Fixes
6. **Fix §9 (Scenario Examples)** - Keep only 9.1 and 9.2 (scriptwriting examples), remove generic scenarios in lines 332-427
7. **Fix YAML description** - Remove duplication in line 5

### Priority 3: Polish
8. **Renumber sections** to standard 1-14 format
9. **Consolidate trigger words** to 4-6 specific phrases

---

## Dimension Breakdown

### Prompt (8.5/10)
✅ Strong system prompt with clear 15+ year screenwriter identity
✅ Good decision framework (4 gates)
✅ Thinking patterns are scriptwriting-specific
✅ Communication style is appropriate

**Room for improvement:** Could add more specific thinking patterns for different genres

### Domain Knowledge (8.0/10)
✅ Excellent screenplay frameworks (Three-Act, Save the Cat, Hero's Journey)
✅ Good professional toolkit (Final Draft, Celtx, etc.)
✅ Core philosophy ("Story Engine") is well-designed
✅ Script metrics table is useful

**Room for improvement:** Some generic content from §16-§21 dilutes domain focus

### Workflow (7.0/10)
✅ Feature film development workflow is solid
✅ Scene writing 7-step process is excellent
⚠️ Sections disordered, missing standard sections

### Risk (7.5/10)
✅ Good domain-specific risks (Derivative Storytelling, Exposition Dumps)
✅ Appropriate severity ratings
✅ Good mitigation strategies

**Issue:** Mixed with some generic risk content from non-existent sections

### Examples (6.0/10)
✅ 9.1 (Confrontation Scene) - Excellent, shows actual screenplay format
✅ 9.2 (Fixing Exposition) - Excellent demonstration
❌ §9 Scenarios 1-4 are generic business content, NOT scriptwriting

### Metadata (4.0/10)
❌ Section numbering completely broken
❌ Missing §5, §13, §14
❌ Description duplicated
❌ 52 empty lines wasted

---

## Action Plan

1. **Remove** empty lines 21-72
2. **Remove** sections §16-§21 (lines 506-620)
3. **Rewrite** §9 to keep only scriptwriting examples (9.1, 9.2)
4. **Add** §5 Platform Support
5. **Add** §13 How to Use This Skill  
6. **Add** §14 License & Author
7. **Fix** YAML description
8. **Renumber** all sections to standard 1-14

---

## Summary

The scriptwriter skill has **strong core content** (system prompt, frameworks, example scenes) but suffers from **severe structural issues** (broken section numbering, wrong content in §9, non-existent sections). After fixes, expected score: **8.5-9.0/10 (Exemplary)**.

**Key Strengths:**
- Professional-grade system prompt
- Industry-standard screenplay frameworks
- Excellent concrete examples (9.1, 9.2)

**Key Weaknesses:**
- Structural chaos (section numbering)
- Generic content pollution (§16-§21)
- Missing required sections (§5, §13, §14)