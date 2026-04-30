# EVALUATION REPORT — Animator Skill

**Skill**: `skills/creative/animator/SKILL.md`  
**Date**: 2026-03-24  
**Reviewer**: skill-writer methodology  
**Overall Score**: **8.25/10 — Expert ⭐**

---

## Executive Summary

The animator skill demonstrates strong domain expertise with comprehensive coverage of 2D/3D animation, motion graphics, and technical animation. The skill has excellent system prompt structure, detailed risk assessment, and well-organized reference files. Primary concerns are generic scenario examples that lack animation-specific context and minor structural inconsistencies in section numbering.

---

## Dimension Scores

| Dimension | Weight | Score | Rating |
|-----------|--------|-------|--------|
| **Prompt** | 20% | 9.0 | Excellent |
| **Domain Knowledge** | 25% | 9.0 | Excellent |
| **Workflow** | 15% | 8.0 | Good |
| **Risk** | 10% | 9.0 | Excellent |
| **Examples** | 20% | 7.0 | Good |
| **Metadata** | 10% | 9.0 | Excellent |
| **TOTAL** | 100% | **8.25** | **Expert ⭐** |

---

## Before/After Analysis

### Before (Current State)
- 530 lines in SKILL.md
- Complete YAML frontmatter with score 9.5/10
- 16-section structure with some numbering gaps (§5, §13-15 missing)
- Reference files: 07-standards.md, 08-workflow.md, 09-scenarios.md, 10-pitfalls.md

### After (Target State)
- Same line count but optimized example specificity
- More animation-contextual scenario examples
- Trigger words expanded from 5 to 6-8 specific phrases
- Section numbering aligned with 16-section template

---

## Issues Found

### 🔴 High Priority

**1. Generic Scenario Examples (§9)**
- **Issue**: Scenarios read like general business/consulting templates rather than animation-specific examples
- **Current**: "Initial Consultation", "Problem Resolution" — no animation context
- **Impact**: AI may not respond appropriately to specific animation requests
- **Fix**: Replace with animation-specific examples:
  - "Walk cycle critique and timing adjustment"
  - "Lip sync correction for dialogue scene"
  - "Action sequence blocking approval"
  - "Motion graphics style frame selection"

### 🟡 Medium Priority

**2. Section Numbering Gaps**
- **Issue**: Missing §5 and §13-15 in the 16-section template
- **Current**: §4.2 → §6 (missing §5), then §7-§12 → §16 (missing §13-15)
- **Impact**: Template inconsistency; some sections may be misplaced
- **Fix**: Add placeholder sections for missing numbers or reorder to match template

**3. Trigger Word Count**
- **Issue**: Only 5 trigger words, below recommended 6-8
- **Current**: "animation", "motion graphics", "character rig", "walk cycle", "animation principles"
- **Impact**: Higher false activation risk for "animation" (too broad)
- **Fix**: Add specific triggers: "2D animation", "3D animation", "animation timing", "animation principles"

### 🟢 Low Priority

**4. Self-Score Consistency**
- **Issue**: Metadata shows score: 9.5, but rubric calculates 8.25
- **Impact**: Minor metadata inconsistency
- **Fix**: Update metadata to reflect calculated score or clarify self-assessment criteria

---

## Concrete Fix Recommendations

### Recommendation 1: Rewrite §9 Scenario Examples

```markdown
### Scenario 1: Walk Cycle Review

**Context:**
Animator needs feedback on a character run cycle.

**User Input:**
"Review my character's run cycle — the body feels too floaty."

**Expert Response:**
Key observations:
1. Anticipation too short → add 2-3 frames before forward motion
2. Vertical bounce insufficient → emphasize up/down in passing poses
3. Arms not opposing → add counter-swing to legs
4. Contact pose needs more "strike" → push silhouette further

[Continue with specific frame-by-frame feedback...]
```

### Recommendation 2: Expand Trigger Words

```yaml
trigger_words:
  - "2D animation"
  - "3D animation"
  - "walk cycle"
  - "run cycle"
  - "lip sync"
  - "animation principles"
  - "motion graphics"
```

### Recommendation 3: Add Missing Sections

Add §5 "How to Use This Skill" following template pattern:

```markdown
## § 5 · How to Use This Skill

1. Load this skill when you need animation expertise
2. Specify: style (2D/3D), software, timeline, output format
3. Provide reference video when possible
4. Iterate: blocking → splining → polish
```

---

## Scoring Justification

| Dimension | Score | Justification |
|-----------|-------|---------------|
| **Prompt** | 9.0 | Excellent role definition, decision framework (1.2), thinking patterns (1.3), communication style. Missing §5 but strong in §1. |
| **Domain Knowledge** | 9.0 | References 12 principles, covers character/motion/technical animation, professional toolkit with real software, knowledge maturity model. |
| **Workflow** | 8.0 | Good workflow diagram (§4.1), reference files exist with content (08-workflow.md has 2 workflows). Slightly generic but functional. |
| **Risk** | 9.0 | Comprehensive risk table (§3), critical risk register (§17), early warning indicators, risk response strategies. Well-documented. |
| **Examples** | 7.0 | 4 scenarios + test cases present. Generic business/consulting tone rather than animation-specific. Needs rewriting. |
| **Metadata** | 9.0 | Complete YAML with all fields. Score field present. Minor inconsistency with calculated score (9.5 vs 8.25). |

---

## Summary

This skill is **Expert-tier** with strong domain expertise and production-quality structure. The main improvement opportunity is making scenario examples animation-specific rather than generic consulting templates. With the recommended fixes, this skill could achieve **Exemplary (≥9.0)** status.

**Recommended Action**: Update §9 with animation-specific scenarios, expand trigger words, and consider updating metadata score to match calculated score.

---

*Generated by skill-writer methodology — 6-dimension quality rubric*