# EVALUATION_REPORT.md - independent-consultant

## Skill Overview
- **Name:** independent-consultant
- **Category:** freelancer
- **Current Score:** 8.4/10 (self-reported)
- **Target Tier:** Expert ⭐

---

## 6-Dimension Quality Rubric Assessment

### 1. System Prompt Depth (Score: 8/10)
| Aspect | Assessment |
|--------|------------|
| Role Definition | ✅ Clear 10+ year expert identity with "Practical Impact Framework" |
| Decision Framework | ✅ 3 gates with specific fail actions |
| Thinking Patterns | ✅ 4 dimensions with consultant-specific perspectives |
| Communication Style | ✅ Executive brevity, structured recommendations |

**Strengths:** Strong identity, distinctive methodology, actionable decision framework.

**Gaps:** No specific communication nuances that would distinguish from general business advisor.

---

### 2. Domain Knowledge Density (Score: 8/10)
| Aspect | Assessment |
|--------|------------|
| Tools & Processes | ✅ 6 professional tools with purposes |
| Frameworks | ✅ 4 consulting frameworks with key steps |
| Quantified Metrics | ⚠️ Metrics table has broken formulas (lines 225-228) |

**Strengths:** Practical Impact Framework visualization, actionable frameworks.

**Gaps:** 
- Metrics table formulas incomplete/malformed
- Knowledge maturity model is generic (not domain-specific)

---

### 3. Workflow Actionability (Score: 7/10)
| Aspect | Assessment |
|--------|------------|
| Phases | ✅ 3 phases with sub-steps for new client engagement |
| Templates | ✅ Checkpoints in workflow |
| Failure Criteria | ⚠️ Not explicitly defined |

**Strengths:** Clear phase structure, advisory conversation steps.

**Gaps:** No measurable output tests defined.

---

### 4. Risk Documentation (Score: 8/10)
| Aspect | Assessment |
|--------|------------|
| Risk Count | ✅ 6 risks with severity |
| Mitigation | ✅ Domain-specific |
| Escalation Triggers | ⚠️ Not explicitly defined |

**Strengths:** Good risk coverage, clear severity ratings.

**Gaps:** Missing escalation triggers and example consequences.

---

### 5. Example Quality (Score: 7/10)
| Aspect | Assessment |
|--------|------------|
| Scenario Count | ⚠️ 2 rich scenarios + 4 generic (duplicated content) |
| Full Flows | ⚠️ Scenarios 1-4 are generic templates, not domain-specific |
| Anti-Pattern Correction | ✅ 5 anti-patterns with ❌/✅ contrasts |

**Strengths:** 9.1 and 9.2 are good domain-specific examples.

**Gaps:** 
- Duplicate generic scenarios (lines 326-424 duplicate the 277-323 content)
- No flow explicitly correcting an anti-pattern

---

### 6. Metadata Completeness (Score: 7/10)
| Aspect | Assessment |
|--------|------------|
| Required Fields | ✅ 9 fields present |
| Description Quality | ⚠️ Missing explicit "Works with" statement |

**Strengths:** Proper YAML, version, tags.

**Gaps:** 
- Description could be more "pushy" with trigger verbs upfront
- Missing platforms field

---

## Critical Issues

### 🔴 Blockers
1. **Line count: 621 lines** - Exceeds 500 line limit (141 lines over)
2. **Missing §5 Platform Support** - No installation instructions for 7 platforms
3. **Duplicate content** - Scenarios 9.1/9.2 appear twice (lines 277-323 AND 326-424)
4. **Generic filler sections 16-21** - Not domain-specific, should be removed or moved to references/

### 🟡 Warnings
5. **Metrics table broken** - Formulas incomplete at lines 225-228
6. **Generic Knowledge Maturity Model** - Lines 518-527 duplicate generic content across all skills
7. **Missing test case validation** - No actual test case outputs defined

---

## Before/After Analysis

| Dimension | Before | After (Target) |
|-----------|--------|----------------|
| **System Prompt** | 8/10 | 9/10 (add heuristics) |
| **Domain Knowledge** | 8/10 | 8/10 (fix metrics) |
| **Workflow** | 7/10 | 8/10 (add failure criteria) |
| **Risk** | 8/10 | 8/10 |
| **Examples** | 7/10 | 8/10 (remove duplicates) |
| **Metadata** | 7/10 | 9/10 (add platforms) |
| **Line Count** | 621 | <500 |
| **Platform Support** | ❌ Missing | ✅ Required |

---

## Upgrade Priority

1. **Remove duplicate scenarios** (lines 326-424)
2. **Add §5 Platform Support** with 7-platform installation
3. **Move generic sections to references/** (sections 16-21 = ~120 lines)
4. **Fix metrics table** (lines 225-228)
5. **Add explicit test case outputs**

---

## Estimated Target Score: 8.5/10 (Expert ⭐)
