# Skill Evaluation Report: translator

## Overview
| Field | Value |
|-------|-------|
| Skill Path | skills/creative/translator/SKILL.md |
| Current Score | 7.9/10 (claimed: 9.5/10) |
| Category | Creative |
| Difficulty | Expert |
| Version | 3.0.0 |
| Last Updated | 2026-03-21 |

---

## Before/After Analysis

### Before (Current State)
- **Score:** 7.9/10 (self-reported: 9.5/10)
- **Issues:** 
  - Workflow section is generic project management, not translation-specific
  - Body overflow: 767 lines (exceeds 500-line limit)
  - Scenario examples in §9 are generic templates, not real translation scenarios
  - Section numbering inconsistency
  - Duplicate test case content across sections

### After (Target State)
- **Score Target:** ≥8.5/10 (Expert tier)
- **Actions Required:**
  - Replace §8 with translation-specific workflow
  - Remove generic scenario templates from §9 (references already have real examples)
  - Reduce body to ≤500 lines
  - Standardize section numbering

---

## Dimension Scores

| Dimension | Score (1-10) | Weight | Weighted Score |
|-----------|--------------|--------|----------------|
| **Prompt** | 8.5 | 0.20 | 1.70 |
| **Domain Knowledge** | 9.0 | 0.25 | 2.25 |
| **Workflow** | 5.5 | 0.15 | 0.83 |
| **Risk** | 8.5 | 0.10 | 0.85 |
| **Examples** | 7.5 | 0.20 | 1.50 |
| **Metadata** | 8.0 | 0.10 | 0.80 |
| **Total** | | 1.00 | **7.93** |

**Classification:** Community → Expert borderline (needs Workflow fix)

---

## Specific Issues Found

### Issue 1: Generic Workflow (CRITICAL)
**Location:** §8 — Workflow  
**Problem:** The workflow describes generic project management phases (Discovery & Assessment, Analysis & Strategy, Implementation & Execution, Review & Optimization) that apply to ANY project, not specifically to translation work.

**Impact:** This is the skill's most critical flaw. A translator needs a domain-specific workflow like:
1. Source analysis (domain, register, audience, cultural delta, stakes assessment)
2. Terminology extraction and glossary building
3. Segment-by-segment translation with consistency checks
4. Self-review (read as target reader)
5. QA tool checks (consistency, tags, numbers)
6. Back-translation for high-stakes content
7. Final delivery with translator's notes

**Current text that's wrong:**
```
### Phase 1: Discovery & Assessment
**Objective:** Fully understand the problem context and requirements.
**Key Activities:**
1. **Context Gathering** — Collect relevant background information and data
2. **Stakeholder Mapping** — Identify all affected parties and their needs
```

This is not translation workflow.

### Issue 2: Body Overflow
**Location:** SKILL.md (entire file)  
**Problem:** 767 lines, exceeding the 500-line limit.

**Impact:** High token cost per invocation. However, key content is already externalized to references/ — the remaining bloat is:
- Generic scenario templates in §9 (should be removed)
- Duplicate content between §14 test cases and references/
- Sections §19-21 appear to be leftover content

### Issue 3: Generic Scenario Templates in §9
**Location:** §9 — Scenario Examples  
**Problem:** Lines 358-509 contain four generic scenario templates (Initial Consultation, Complex Problem Solving, Strategic Planning, Quality Assurance) that are not translation-specific.

**Impact:** These templates don't demonstrate translation capability. The references/scenario-examples.md already contains 4 excellent, real translation scenarios (Technical Manual, Marketing Transcreation, Legal Clause, MTPE). The SKILL.md should reference those, not duplicate generic templates.

### Issue 4: Section Numbering Inconsistency
**Location:** Throughout  
**Problem:** Mixed numbering styles:
- §1, §2, §3, §4, §5, §6 (sections 1-6, 12-16)
- §7 · Standards & Reference (with bullet)
- §8 · Workflow (with bullet)
- §9 · Scenario Examples (with bullet)
- §10 · Common Pitfalls (with bullet)

**Impact:** Minor - inconsistent formatting, should standardize to §7, §8, §9, §10 without bullet.

### Issue 5: Duplicate Test Cases
**Location:** §14 vs references/scenario-examples.md  
**Problem:** Test Case 1 (Technical Register), Test Case 2 (Marketing Transcreation), Test Case 3 (MTPE Accuracy) duplicate content already in references/scenario-examples.md.

**Impact:** Redundancy increases token cost. Should reference the scenario examples file instead.

### Issue 6: Sections §19-21 Are Orphaned
**Location:** End of file  
**Problem:** Lines 726-767 contain:
- §19 · Best Practices Library (4 lines)
- §20 · Case Studies (6 lines)
- §21 · Resources & References (10 lines)
- Performance Metrics (empty table)
- Additional Resources (3 bullet points)

**Impact:** These appear to be leftover content from a template copy-paste. They add no value and bloat the file.

---

## Concrete Fix Recommendations

### Fix 1: Replace §8 with Translation-Specific Workflow
**Priority:** CRITICAL  
**Action:** Replace the entire §8 section with:

```markdown
## § 8 — Translation Workflow

### Phase 1: Source Analysis (5 minutes)
- Identify domain: Technical / Legal / Medical / Literary / Marketing / Software
- Determine register: Formal / Neutral / Informal / Creative
- Map audience: Expert / Informed layperson / General public
- Flag cultural deltas: idioms, units, dates, cultural references
- Assess stakes: Safety-critical → dual review; Commercial → cultural review; General → standard

### Phase 2: Preparation (10-30 minutes)
- Extract terminology from source text
- Build or consult domain glossary
- Review client style guide (if provided)
- Check translation memory for previous matches

### Phase 3: Translation & Consistency (Variable)
- Translate segment-by-segment using glossary
- Apply consistent terminology throughout
- Add translator's notes for non-obvious choices
- Flag cultural adaptations for client approval

### Phase 4: Self-Review (10-15% of translation time)
- Read as target-language reader, NOT as translator
- Check for natural flow and readability
- Verify all terms used consistently
- Run back-translation check on high-stakes segments

### Phase 5: QA Validation
- Run xBench/QA Distiller: consistency, numbers, tags, omissions
- Verify locale-specific formatting (dates, numbers, currency)
- Confirm file format integrity (XLIFF, PO, JSON structure)

### Phase 6: Delivery
- Deliver in requested format with locale code
- Include translator's notes and glossary updates
- Document any unresolved ambiguities

**✓ Done Criteria:**
- [ ] Domain and register explicitly identified
- [ ] Glossary consulted/built for all key terms
- [ ] Cultural adaptations flagged with rationale
- [ ] Self-review completed (read as target reader)
- [ ] QA tool check passed (zero critical errors)
- [ ] Back-translation completed (high-stakes content only)
```

### Fix 2: Remove Generic Scenario Templates from §9
**Priority:** HIGH  
**Action:** Replace §9 content with:

```markdown
## § 9 — Scenario Examples

→ See [references/scenario-examples.md](./references/scenario-examples.md)
```

This removes ~150 lines of bloat and properly references the externalized content.

### Fix 3: Remove Duplicate Test Cases from §14
**Priority:** MEDIUM  
**Action:** Replace Test Cases section with reference:

```markdown
## § 14 — Quality Verification

### Self-Checklist Before Delivery
[Keep existing checklist]

### Test Cases
→ See [references/scenario-examples.md](./references/scenario-examples.md) — Test Cases 1-3
```

### Fix 4: Remove Orphaned Sections §19-21
**Priority:** MEDIUM  
**Action:** Delete lines 726-767 entirely.

### Fix 5: Standardize Section Numbering
**Priority:** LOW  
**Action:** Change all `§ N ·` to `§ N —` for consistency.

---

## Expected Results After Fixes

| Metric | Before | After |
|--------|--------|-------|
| Body Lines | 767 | ~420 |
| Token Cost | High | Medium |
| Workflow | Generic (5.5) | Translation-specific (~8.5) |
| Scenario Examples | Generic templates | References only |
| Total Score | 7.93 | ~8.5 |

---

## Summary

**Key Finding:** This skill has excellent domain knowledge (§1 system prompt is strong), good risk documentation, and well-externalized references. The critical weakness is §8 - a generic project management workflow that undermines the skill's translation-specific identity.

**Primary Fix Required:** Replace §8 with translation-specific workflow phases.

**Score Progression:** 7.93 → 8.5+ (Expert tier)

---

*Evaluation Date: 2026-03-24*
*Evaluator: skill-writer methodology*
