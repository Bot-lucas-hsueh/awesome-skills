# Evaluation Report: graphic-designer Skill

## Overview
| Attribute | Value |
|-----------|-------|
| File | `skills/creative/graphic-designer/SKILL.md` |
| Current Score | Self-reported 9.5/10 |
| Revised Score | **5.8/10** (Community tier) |
| Status | Requires major fixes |

---

## Before/After Analysis

| Dimension | Before | After | Issue |
|-----------|--------|-------|-------|
| System Prompt | 8 | 7 | Adequate but missing decision framework |
| Domain Knowledge | 9 | 6 | Core is good but bloated with irrelevant content (§16-21) |
| Workflow | 7 | 6 | Decent phases but generic scenarios |
| Risk Documentation | 8 | 7 | Good but missing escalation triggers |
| Examples | 6 | 4 | Generic placeholder content, not graphic-design specific |
| Metadata | 3 | 5 | Repetition error, missing platforms, truncated description |
| **Weighted Total** | 7.5 | **5.8** | → Community tier |

---

## Specific Issues Found

### 🔴 Critical (Must Fix)

1. **Description repetition error** (Lines 3-6)
   - "A world-class graphic designer..." appears twice
   - Indicates copy-paste error during editing
   - Causes: description ~400 chars (target ≤263)

2. **Missing §5 Platform Support** (Required section)
   - No installation instructions for any of 7 platforms
   - Violates 16-section standard

3. **Non-standard section structure (§16-21)**
   - Sections 16-21 contain generic content (Knowledge Maturity, Risk Management Framework, Excellence Framework)
   - This content appears copied from a different skill template
   - Does not belong in a graphic designer skill
   - Creates 60+ lines of irrelevant content

4. **Incomplete §11 Integration** (Line 321)
   - "Marketing" entry is truncated
   - Creates malformed table

### 🟡 Medium (Should Fix)

5. **Generic scenario examples** (§9)
   - Scenario 1-4 are consultation/management templates, not graphic design specific
   - Do not demonstrate actual design decision-making
   - Should show: logo design brief, brand guidelines development, print production issue, etc.

6. **Empty placeholder sections** (Lines 431-438)
   - Performance Metrics table with no data
   - Additional Resources with no content

7. **Risk section missing escalation triggers**
   - Good severity ratings but no example consequences
   - Missing edge cases (e.g., color blindness, cultural symbolism)

---

## Concrete Fix Recommendations

### Fix 1: Correct Metadata (Priority: Critical)
```yaml
description: >
  A world-class graphic designer specializing in visual identity, branding, 
  layout, and typography. Creates brand identities, marketing collateral, 
  social media assets, and print-ready specifications. 
  Use when: logo design, brand guidelines, typography, color palette, 
  print production, layout composition.
```

### Fix 2: Add Platform Support (§5)
Add section after §4:
```markdown
## § 5 · Platform Support

→ See `assets/INSTALL.md` for installation across all 7 platforms.

Quick install: `/skill install graphic-designer` (OpenCode)
```

### Fix 3: Remove Irrelevant Sections (§16-21)
Delete lines 331-438 entirely. Replace with:
```markdown
## § 16 · License & Author

MIT with Attribution — See [LICENSE](../../../LICENSE)
```

### Fix 4: Fix §11 Integration
Complete the truncated table entry or remove if no valid integrations.

### Fix 5: Replace Generic Scenarios
Replace §9 with graphic-design specific scenarios:
- Logo design brief → concept development
- Brand guidelines document creation
- Print production issue (bleed/color mode)
- Accessibility audit (color contrast)

---

## Score Breakdown

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| System Prompt | 20% | 7 | 1.40 |
| Domain Knowledge | 25% | 6 | 1.50 |
| Workflow | 15% | 6 | 0.90 |
| Risk Documentation | 10% | 7 | 0.70 |
| Example Quality | 20% | 4 | 0.80 |
| Metadata Completeness | 10% | 5 | 0.50 |
| **Total** | 100% | — | **5.8** |

**Tier: Community** (4.0–6.9)

---

## Summary

The graphic-designer skill has a strong foundation in the system prompt and core domain knowledge, but suffers from:
- Critical metadata errors (description repetition)
- Missing required sections (Platform Support)
- Non-compliant structure (§16-21 template pollution)
- Generic examples that don't showcase graphic design expertise

**Recommended action**: Apply fixes 1-5 and re-evaluate for Expert tier eligibility.