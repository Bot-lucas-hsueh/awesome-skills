# Sports Referee Skill - Evaluation Report

## Overview

| Dimension | Score | Status |
|-----------|-------|--------|
| **Prompt** | 7.5/10 | Good - needs cleanup |
| **Domain Knowledge** | 8.5/10 | Strong |
| **Workflow** | 8.0/10 | Good - well structured |
| **Risk** | 8.5/10 | Comprehensive |
| **Examples** | 6.0/10 | Needs improvement |
| **Metadata** | 5.0/10 | Needs rewrite |
| **Overall** | **7.3/10** | Community tier |

---

## Before/After Analysis

### Before (Current State)
- 632 lines (exceeds 500 limit)
- Mixed structure: good core content + generic template sections
- YAML has incorrect fields
- Good domain examples but mixed with generic consulting templates

### After (Recommended Target)
- ≤500 lines (move §9.2-9.4, §17-21 to references/)
- Clean YAML metadata
- Domain-specific examples only (remove generic consulting templates)
- Add missing required sections (§5, §13, §15, §16)

---

## Specific Issues Found

### 1. Structure Violations (Critical)
| Issue | Location | Severity |
|-------|----------|----------|
| SKILL.md exceeds 500 lines | Entire file | 🔴 High |
| Empty lines at start | Lines 1-50 | 🟡 Medium |
| Missing §5 Platform Support | - | 🔴 High |
| Missing §13 How to Use | - | 🔴 High |
| Missing §15 Version History | - | 🟡 Medium |
| Missing §16 License | - | 🟡 Medium |
| Sections 9.2-9.4 in main file | SKILL.md:239-362 | 🟡 Medium |
| Generic sections §17-21 | SKILL.md:518-632 | 🟡 Medium |
| §11 Integration copied from business domain | SKILL.md:473-481 | 🟡 Medium |

### 2. YAML Metadata Issues (Critical)
| Issue | Current | Required |
|-------|---------|----------|
| description | Contains repetition, 300+ chars | ≤263 chars |
| score/text_score/runtime_score | Present (not user-provided) | Remove - these are auto-calculated |
| tags | Has 7 tags, acceptable | Keep top 4-6 |
| Missing: triggers | Not present | Add trigger words |

### 3. Content Quality Issues
| Issue | Location | Fix |
|-------|----------|-----|
| Generic consulting scenarios | §9:365-462 | Replace with domain-specific referee scenarios |
| Generic risk register | §17:541-564 | Remove - irrelevant to referee domain |
| Generic excellence framework | §18:565-582 | Remove - doesn't apply |
| Generic case studies | §20:597-605 | Remove - placeholder only |

### 4. Positive Content (Keep)
- §1 System Prompt - excellent referee persona
- §3 Risk Disclaimer - comprehensive and well-structured
- §4 Core Philosophy - strong game management triangle
- §6 Professional Toolkit - practical
- §9.2-9.4 Examples - high quality, move to references/
- References files - good content

---

## Concrete Fix Recommendations

### Priority 1: YAML Fix
```yaml
---
name: sports-referee
description: 'Expert sports referee for basketball, soccer, volleyball, and combat sports. Applies rules, manages games, resolves conflicts. Use when: sports officiating, rule interpretation, game management, conflict resolution.'
license: MIT
metadata:
  author: neo.ai <lucas_hsueh@hotmail.com>
  version: 3.0.0
  updated: 2026-03-21
  tags: [sports, referee, officiating, game-rules]
  category: entertainment
  difficulty: expert
  triggers:
    - 裁判
    - 体育裁判
    - sports referee
    - officiating
    - 越位
    - 判罚
---
```

### Priority 2: Move Content to References
- Move §9.2 (Combat Sports) → references/09-scenarios.md
- Move §9.3 (Offside Decision) → references/09-scenarios.md
- Move §9.4 (Anti-Pattern) → references/09-scenarios.md
- Move §17-21 → delete (generic templates)

### Priority 3: Add Missing Sections
Add after §4:
```
## § 5 · Platform Support
→ See assets/INSTALL.md for per-platform setup

## § 6 · How to Use This Skill
[Standard template from skill-writer references]
```

### Priority 4: Replace Generic Scenarios
Replace §9 Scenario 1-4 with referee-specific examples:
- Pre-game preparation question
- In-game ruling dispute
- Post-game incident documentation
- Player ejection handling

---

## Scoring Breakdown

### Prompt (7.5/10)
- ✓ Strong persona definition with 15+ years experience
- ✓ Clear decision framework with gates
- ✓ Good thinking patterns table
- ✗ Some generic project management content mixed in

### Domain Knowledge (8.5/10)
- ✓ Deep knowledge of multiple sports
- ✓ Correct technical terminology
- ✓ Practical examples (offside, combat sports)
- ✗ Some irrelevant sections (risk register, excellence framework)

### Workflow (8.0/10)
- ✓ Pre-game, in-game, post-game protocols
- ✓ Clear decision flow for calls
- ✓ References to external workflow files

### Risk (8.5/10)
- ✓ Comprehensive risk table with severity ratings
- ✓ Clear mitigation strategies
- ✓ Important safety disclaimer

### Examples (6.0/10)
- ✓ Real examples in §9.2-9.4 are high quality
- ✗ Generic consulting templates in §9.1 don't fit domain
- ✗ Placeholder case studies

### Metadata (5.0/10)
- ✗ Description too long with repetition
- ✗ Incorrect fields (score, text_score)
- ✗ Missing triggers field

---

## Recommended Actions

1. **Clean YAML** - Fix description, remove auto-calc fields, add triggers
2. **Reduce SKILL.md** - Target ≤500 lines by moving §9.2-9.4 to references/
3. **Remove generic content** - Delete §17-21 templates
4. **Add missing sections** - §5 Platform Support, §13 How to Use
5. **Replace scenarios** - Add 4 referee-specific scenario examples

---

## Estimated Improvement
After fixes: **8.0/10** (Expert tier)

Key improvements:
- YAML compliance → cleaner activation
- Line count reduction → lower token cost
- Domain-specific examples → higher utility
- Missing sections added → complete structure
