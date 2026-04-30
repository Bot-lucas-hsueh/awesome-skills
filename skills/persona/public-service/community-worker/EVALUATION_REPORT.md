# Evaluation Report: community-worker Skill

**Date**: 2026-03-24  
**Skill**: skills/public-service/community-worker/SKILL.md  
**Version**: 3.0.0  
**Score**: 8.35/10 (Expert ⭐)  

---

## 1. Executive Summary

The community-worker skill demonstrates strong domain expertise in social services, welfare programs, and crisis intervention. It has well-developed frameworks (ESA, Crisis Triage, Resource Matching) and appropriate risk documentation. However, the skill suffers from **token overflow** (587 lines vs 500 limit) due to generic template content in §16-21 that dilutes its focus.

**Recommendation**: Clean up template filler; move non-essential sections to references/; maintain Expert tier.

---

## 2. Before/After Analysis

| Aspect | Current State | Target State | Gap |
|--------|---------------|--------------|-----|
| **Line Count** | 587 lines | ≤500 lines | -87 lines |
| **System Prompt** | 21 lines, structured | Already optimal | ✓ |
| **Domain Frameworks** | ESA, Crisis, Matrix | Already optimal | ✓ |
| **Examples** | 2 real + 3 template | 2-3 real, no filler | Remove §9.3-9.5 |
| **Risk Section** | 5 risks, severity | Already optimal | ✓ |
| **Metadata** | Duplicate text | Clean description | Fix duplication |

---

## 3. Dimension Scores

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| System Prompt Depth | 20% | 9.0 | 1.80 |
| Domain Knowledge Density | 25% | 9.0 | 2.25 |
| Workflow Actionability | 15% | 8.0 | 1.20 |
| Risk Documentation | 10% | 8.0 | 0.80 |
| Example Quality | 20% | 7.0 | 1.40 |
| Metadata Completeness | 10% | 8.0 | 0.80 |
| **Total** | 100% | — | **8.35** |

---

## 4. Specific Issues Found

### 🔴 Critical Issues

1. **Token Overflow (§16-21)**
   - Location: Lines 473-586
   - Issue: Generic "Domain Deep Dive", "Risk Management Deep Dive", "Excellence Framework", "Best Practices Library", "Case Studies" sections contain ~100+ lines of template content
   - Fix: Remove entirely or move to `references/`

2. **Generic Examples in §9.3-9.5**
   - Location: Lines 300-395
   - Issue: "Initial Consultation", "Problem Resolution", "Strategic Planning", "Quality Assurance" are generic project management templates, NOT community worker scenarios
   - Fix: Replace with actual community worker scenarios (e.g., benefits appeal, domestic violence intake, senior services referral)

### 🟡 Medium Issues

3. **Description Duplicate Text**
   - Location: Lines 3-6
   - Issue: "Expert community worker providing..." appears twice
   - Fix: Consolidate to single concise description

4. **Self-Reference in §14**
   - Location: Line 454
   - Issue: "See references/standards.md §7.10" creates circular dependency
   - Fix: Embed key checklist items directly

### 🟢 Minor Issues

5. **Section 14 Quality Verification**
   - Location: Lines 452-471
   - Issue: References external file; self-score is inflated
   - Fix: Simplify or remove

---

## 5. Concrete Fix Recommendations

### Priority 1: Remove Generic Template Content (~60 lines)

| Section | Lines | Action |
|---------|-------|--------|
| §16 Domain Deep Dive | 473-493 | Delete - generic knowledge maturity model |
| §17 Risk Management Deep Dive | 494-519 | Delete - generic risk register |
| §18 Excellence Framework | 520-537 | Delete - generic excellence cycle |
| §19 Best Practices Library | 540-551 | Delete - generic practices |
| §20 Case Studies | 553-560 | Delete - no real community worker cases |
| §21 Resources & References | 562-586 | Delete - empty metric table + generic resources |

### Priority 2: Replace §9.3-9.5 with Real Scenarios (~50 lines)

Replace generic project management templates with:
- **Scenario 3**: "Benefits Appeal" — client denied SNAP, explaining appeal process
- **Scenario 4**: "Senior Services" — elderly client needing in-home care referral
- **Scenario 5**: "Child Welfare" — mandated reporter guidance

### Priority 3: Clean Metadata (~5 lines)

- Fix description duplicate
- Keep all required fields

---

## 6. After Fixes - Expected Metrics

| Metric | Before | After |
|--------|--------|-------|
| Line Count | 587 | ~480 |
| Token Cost/Invoc | ~5900 | ~4800 |
| Example Quality | 7/10 | 8/10 |
| Domain Relevance | 70% | 95% |
| **Final Score** | 8.35 | ~8.6 |

---

## 7. Summary

| Dimension | Status | Notes |
|-----------|--------|-------|
| System Prompt | ✅ Good | Decision gates, thinking patterns, communication style all solid |
| Domain Knowledge | ✅ Good | ESA framework, crisis protocols, specific program details |
| Workflow | ⚠️ OK | Phases present but could add more templates |
| Risk | ✅ Good | 5 domain risks with severity and mitigations |
| Examples | ⚠️ OK | 2 real examples + 5 generic templates |
| Metadata | ⚠️ OK | Duplicate description, otherwise complete |

**Action**: Apply fixes to achieve cleaner, more focused skill while maintaining Expert tier.

---

*Evaluation methodology: skill-writer quality rubric (6 dimensions, weighted scoring)*