# Skill Evaluation Report: funeral-director

**Skill Path:** `skills/public-service/funeral-director/SKILL.md`  
**Evaluation Date:** 2026-03-24  
**Reviewer:** Skill Writer Architecture  

---

## Executive Summary

| Dimension | Score | Tier |
|-----------|-------|------|
| System Prompt Depth | 8.5/10 | Expert |
| Domain Knowledge Density | 8.5/10 | Expert |
| Workflow Actionability | 7.5/10 | Expert |
| Risk Documentation | 8.5/10 | Expert |
| Example Quality | 6.5/10 | Community |
| Metadata Completeness | 6.0/10 | Community |
| **Weighted Average** | **7.7/10** | **Expert** |

**Recommendation:** Expert tier - requires minor fixes for metadata and examples.

---

## Before/After Analysis

### Current State
- **System Prompt:** Comprehensive role definition with decision framework, thinking patterns
- **Domain Knowledge:** Strong frameworks (§4, §7), professional toolkit, standards reference
- **Workflow:** Phased workflows with sub-steps
- **Risk:** 4 high-severity risks with mitigation + §17 deep dive
- **Examples:** 2 good funeral-specific examples (§9.1, §9.2) + 4 generic business examples (§9.3-§9.6) that don't match domain
- **Metadata:** Partial - missing `platforms`, `display_name`, `quality`

### Issues Found
1. **Body Overflow:** 608 lines (>500 limit) - sections §16-21 should move to references/
2. **Irrelevant Examples:** §9.3-§9.6 are generic business/strategy scenarios (not funeral-related)
3. **Incomplete Metadata:** Missing required fields for Expert tier
4. **Description Vague:** Current description lacks specific trigger verbs and measurable outcome

---

## Dimension-by-Dimension Analysis

### 1. System Prompt Depth (8.5/10) ⭐ Expert

**Strengths:**
- Role definition with 20+ years experience identity
- 3-gate decision framework with fail actions
- 4 thinking patterns (Family-Centered, Dignity-First, Legal-Compliant, Culturally-Aware)
- Clear communication style guidelines

**Issues:** None significant

---

### 2. Domain Knowledge Density (8.5/10) ⭐ Expert

**Strengths:**
- §4 Family-Centered Service Framework with 5 phases
- §7 Standards & Reference with 3 frameworks and service metrics
- Professional toolkit with 5 specific tools
- Cultural customs integration guidance

**Issues:**
- Sections §16-21 (lines ~494-607) are generic content that belongs in references/

---

### 3. Workflow Actionability (7.5/10) ⭐ Expert

**Strengths:**
- §8.1 Initial Family Consultation: 4 phases with detailed sub-steps
- §8.2 Service Coordination: 6 specific steps

**Issues:**
- Could benefit from templates/checkpoints per phase (Expert hallmark)
- No failure criteria defined

---

### 4. Risk Documentation (8.5/10) ⭐ Expert

**Strengths:**
- §3: 4 high-severity risks with severity ratings and mitigation
- §17: Risk register with probability/impact scoring
- Risk response strategies included

**Issues:** None significant

---

### 5. Example Quality (6.5/10) 🟡 Community

**Strengths:**
- §9.1: Buddhist funeral planning example (excellent - specific, budget-aware, culturally accurate)
- §9.2: Grief support example (empathetic, resource-oriented)

**Issues:**
- **§9.3-§9.6 (lines 322-417):** Generic business scenarios unrelated to funeral direction
  - Scenario 1: "funeral director" used generically (not actual funeral services)
  - Scenario 2: "critical situation" with business triage
  - Scenario 3: "world-class" strategic planning
  - Scenario 4: "quality verification" for business deliverables
- These examples don't demonstrate funeral-specific expertise

---

### 6. Metadata Completeness (6.0/10) 🟡 Community

**Current YAML fields:**
```yaml
name: funeral-director ✓
description: 'Professional funeral director...' ✓
license: MIT ✓
author: neo.ai ✓
version: 3.0.0 ✓
updated: 2026-03-21 ✓
tags: [funeral, bereavement, mortuary, death-care, memorial] ✓
category: public-service ✓
difficulty: expert ✓
score: 8.3/10 ✓
quality: production ✓
text_score: 9.1 ✓
runtime_score: 7.5 ✓
variance: 1.6 ✓
```

**Missing for Expert tier:**
- `platforms` field (required for Expert Verified)
- `display_name` field
- Description should be more precise with trigger verbs

---

## Concrete Fix Recommendations

### Priority 1: Fix Examples (Highest ROI - +1.8 points)
**Current:** 6.5 → **Target:** 8.0+

Replace §9.3-§9.6 with funeral-specific scenarios:
1. **Legal Navigation** - Death certificate handling, permits
2. **Cultural Integration** - Multi-faith family arrangements
3. **Budget-Conscious Planning** - Affordable options for families

### Priority 2: Fix Metadata (+0.7 points)
**Current:** 6.0 → **Target:** 7.5+

Add to YAML header:
```yaml
display_name: Funeral Director
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
```

Rewrite description to front-load triggers:
```yaml
description: >
  Professional funeral director providing funeral arrangements, cremation services,
  and bereavement support. Plans memorial services, coordinates logistics, handles
  death certificates and permits, and provides grief support resources.
  Use when: "funeral planning", "bereavement support", "death care arrangements",
  "memorial service", "cremation services"
```

### Priority 3: Reduce Body Overflow
Move sections §16-21 to `references/funeral-director-advanced.md`:
- §16 Domain Deep Dive
- §17 Risk Management Deep Dive
- §18 Excellence Framework
- §19 Best Practices Library
- §20 Case Studies
- §21 Resources & References

This saves ~115 lines (>100 tokens/invocation).

---

## Action Plan

| Action | Status |
|--------|--------|
| Replace §9.3-§9.6 with funeral-specific examples | Required |
| Add `platforms` and `display_name` to YAML | Required |
| Rewrite description with trigger verbs | Required |
| Move §16-21 to references/ | Recommended |
| Verify total lines ≤500 after changes | Required |

---

## Score Calculation

```
Score = (Prompt×0.20) + (Domain×0.25) + (Workflow×0.15) 
      + (Risk×0.10) + (Examples×0.20) + (Metadata×0.10)

     = (8.5×0.20) + (8.5×0.25) + (7.5×0.15) 
       + (8.5×0.10) + (6.5×0.20) + (6.0×0.10)
     
     = 1.70 + 2.125 + 1.125 + 0.85 + 1.30 + 0.60
     = 7.70 → Expert ⭐
```

---

## Conclusion

This skill is **Expert tier (7.7/10)** with strong fundamentals in system prompt, domain knowledge, and risk documentation. The main gaps are:
1. Irrelevant examples (§9.3-§9.6)
2. Missing metadata fields (platforms, display_name)
3. Body overflow (>500 lines)

With the recommended fixes, this skill can achieve **8.5+ (Expert Verified)**.