# Dancer Skill — Evaluation Report

## Overview

| Metric | Value |
|--------|-------|
| **Skill** | skills/entertainment/dancer/SKILL.md |
| **Current Score** | 8.3/10 (metadata) |
| **Evaluated Score** | 7.15/10 |
| **Tier** | Community → Expert |
| **Evaluator** | skill-writer v12 |
| **Date** | 2026-03-24 |

---

## 1. Dimension Scores

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| **System Prompt Depth** | 20% | 8.0 | 1.60 |
| **Domain Knowledge** | 25% | 7.0 | 1.75 |
| **Workflow Actionability** | 15% | 8.0 | 1.20 |
| **Risk Documentation** | 10% | 9.0 | 0.90 |
| **Example Quality** | 20% | 5.0 | 1.00 |
| **Metadata Completeness** | 10% | 9.0 | 0.90 |
| **TOTAL** | 100% | — | **7.35** |

---

## 2. Before/After Analysis

### Current Strengths
- Excellent system prompt with clear decision gates (what dance style, experience level, purpose, context)
- Strong risk documentation with injury prevention emphasis
- Good Dance Development Pyramid framework
- Professional toolkit with practical tools

### Critical Issues Found

| Issue | Severity | Location |
|-------|----------|----------|
| **Irrelevant business content** | 🔴 Critical | §16-21 (lines 464-577) |
| **Generic scenario examples** | 🔴 Critical | §9 Scenario 1-4 (lines 290-387) |
| **Misaligned section structure** | 🟡 Medium | §5 missing platform support |
| **Workflow dilution** | 🟡 Medium | §8 mixed with business phases |

---

## 3. Specific Issues

### Issue 1: Irrelevant Content in §16-21 (CRITICAL)
**Problem:** Sections 16-21 contain generic business/management content that has nothing to do with dance:
- §16: "Domain Deep Dive" with rows about "Foundation, Implementation, Optimization, Innovation" - meaningless for dance
- §17: "Risk Management Deep Dive" with risks about "Strategic misalignment, Resource constraints" - not dance risks
- §18: "Excellence Framework" with business metrics
- §19-21: Generic best practices, case studies, resources

**Impact:** ~115 lines of irrelevant content dilute the skill's focus and waste tokens.

### Issue 2: Generic Scenarios in §9 (CRITICAL)
**Problem:** §9 contains 4 generic "business" scenarios that don't match dance:
- Scenario 1: "Initial Consultation" - talks about "stakeholders", "strategy development"
- Scenario 2: "Problem Resolution" - uses project management language
- Scenario 3: "Strategic Planning" - 18-month roadmap with efficiency metrics
- Scenario 4: "Quality Assurance" - corporate deliverables

Meanwhile, the actual dance examples (§9.1 Beginner, §9.2 Intermediate) are good but sparse.

**Impact:** Confuses the skill's identity; reduces example quality score.

### Issue 3: Missing Platform Support §5
**Problem:** §5 should contain platform-specific installation but is empty (the skill doesn't provide this).

**Impact:** Missing required section per skill-writer standards.

---

## 4. Fix Recommendations

### Priority 1: Remove Irrelevant Content (Immediate)
**Action:** Delete §16-21 entirely (~115 lines). This content adds zero dance value.

### Priority 2: Replace Generic Scenarios (Immediate)
**Action:** Replace §9 Scenarios 1-4 with 2-3 dance-specific scenarios:
- Scenario: "Audition Preparation" - how to prepare for dance audition
- Scenario: "Injury Recovery" - returning to dance after injury
- Keep §9.1 and §9.2 as they are good

### Priority 3: Add Platform Support (Medium)
**Action:** Add §5 with platform installation guidance per standards, or clearly mark as "N/A for agent platforms" if truly not applicable.

### Priority 4: Add Trigger Words to Metadata (Medium)
**Action:** The current description is good but could front-load trigger verbs:
```
Current: "Professional dancer with expertise in multiple dance styles..."
Proposed: "Dance instructor and choreographer. Use when: learning dance technique, creating choreography, preparing for performance."
```

---

## 5. Target State After Fixes

| Dimension | Current | Target |
|-----------|---------|--------|
| System Prompt | 8.0 | 8.5 |
| Domain Knowledge | 7.0 | 8.5 |
| Workflow | 8.0 | 8.0 |
| Risk Docs | 9.0 | 9.0 |
| Examples | 5.0 | 8.0 |
| Metadata | 9.0 | 9.0 |
| **TOTAL** | **7.35** | **8.45** |

**New Tier:** Expert ⭐

---

## 6. Scoring Rationale

### System Prompt (8.0/10)
- ✅ Has role definition with 15+ years experience
- ✅ Decision framework with 4 gates and fail actions
- ✅ Thinking patterns table specific to dance
- ✅ Communication style examples
- ⚠️ Could add more domain-specific heuristics

### Domain Knowledge (7.0/10)
- ✅ Dance Development Pyramid is excellent framework
- ✅ Professional toolkit with 6 dance-specific tools
- ✅ Standards with frameworks and quantified metrics
- ❌ §16-21 business content dilutes domain focus
- ⚠️ Could add more dance-specific thresholds

### Workflow (8.0/10)
- ✅ 3-phase technique development workflow
- ✅ 5-step choreography creation process
- ✅ Sub-steps with clear checkpoints
- ⚠️ Could add failure criteria

### Risk Documentation (9.0/10)
- ✅ 4 dance-specific risks with severity
- ✅ Proper mitigation strategies
- ✅ Strong warning language ("no pain no gain")
- ✅ Good emphasis on injury prevention

### Example Quality (5.0/10)
- ✅ §9.1 and §9.2 are good beginner/intermediate examples
- ❌ §9 Scenarios 1-4 are generic business content
- ⚠️ Only 2 dance-specific examples (should have 3+)

### Metadata (9.0/10)
- ✅ All 9 required fields present
- ✅ Version history tracked
- ✅ Good tags and category
- ⚠️ Description could front-load triggers

---

## 7. Recommended Fix Commands

```bash
# Delete irrelevant sections
# Remove §16 (Domain Deep Dive) - lines 464-484
# Remove §17 (Risk Management Deep Dive) - lines 486-509
# Remove §18 (Excellence Framework) - lines 511-528
# Remove §19 (Best Practices Library) - lines 531-541
# Remove §20 (Case Studies) - lines 544-551
# Remove §21 (Resources & References) - lines 554-577

# Replace §9 scenarios with dance-specific ones
# Add Scenario: Audition Preparation
# Add Scenario: Injury Recovery & Return to Dance
```

---

## 8. Conclusion

The dancer skill has strong bones: good system prompt, excellent risk awareness, solid workflow. However, it's significantly diluted by ~115 lines of irrelevant business content in §16-21 and 4 generic scenarios that don't belong in a dance skill.

**Fix required:** Remove §16-21, replace generic scenarios, and the skill easily crosses into Expert tier (8.0+).

---

*Evaluated using skill-writer Quality Rubric (6 dimensions, weighted scoring)*
