# EVALUATION REPORT: remote-sensing-data-scientist

## Summary
| Metric | Value |
|--------|-------|
| **Weighted Score** | 7.85/10 |
| **Tier** | Expert ⭐ |
| **Original Score** | 8.4/10 |
| **Variance** | 0.55 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| System Prompt Depth | 20% | 8 | 1.60 |
| Domain Knowledge Density | 25% | 9 | 2.25 |
| Workflow Actionability | 15% | 8 | 1.20 |
| Risk Documentation | 10% | 8 | 0.80 |
| Example Quality | 20% | 6 | 1.20 |
| Metadata Completeness | 10% | 8 | 0.80 |
| **Total** | 100% | — | **7.85** |

---

## Detailed Analysis

### Strengths ✅

1. **System Prompt (8/10)**: Comprehensive identity with credentials, 4-gate decision framework, thinking patterns, communication style. Domain-specific heuristics present.

2. **Domain Knowledge (9/10)**: Excellent depth - SAR processing, multispectral classification, change detection, GEE, geospatial DL, quantitative retrieval. Specific metrics (Kappa >0.85), tools (SNAP, torchgeo, GEE), datasets (BigEarthNet, SpaceNet).

3. **Workflow (8/10)**: Detailed 3-phase workflow with ✓ Done/✗ FAIL criteria for each step. Specific to remote sensing domain.

4. **Risk Documentation (8/10)**: 6 risks with severity ratings (🔴 Critical, 🟡 High, 🟢 Medium). Domain-specific mitigations.

5. **Metadata (8/10)**: All 9 fields present. Description has role + triggers + works-with.

### Issues ❌

1. **Examples (6/10)**: 4 scenarios present but **generic** - not specific to remote sensing domain. All scenarios use placeholder [problem] instead of domain-specific situations. Should demonstrate actual remote sensing workflows.

2. **Missing §5 Platform Support**: No platform installation instructions for 7 platforms.

3. **References-First Violation**: 
   - §7 "See references/07-standards.md" - content should be in body
   - §10 references code-block files - content should be referenced, not just linked
   - Lines 470-483 contain substantial anti-pattern content that should be in references/

4. **Body Length**: 629 lines approaches 500-line limit but acceptable for domain skill.

---

## Anti-Patterns Detected

| # | Anti-Pattern | Severity | Location |
|---|--------------|----------|----------|
| 1 | Generic examples not domain-specific | 🟡 Medium | §9 all scenarios |
| 2 | Missing §5 Platform Support | 🟡 Medium | Section absent |
| 3 | Content in references/ that belongs in body | 🟢 Low | §7, §10 |

---

## Upgrade Recommendations

### Priority 1: Fix Examples (§9)
- Replace generic scenarios with actual remote sensing workflows
- Example: "Sentinel-2 cloud mask failing over tropical forests - diagnose and fix"
- Add anti-pattern correction scenario (e.g., fixing random pixel split issue)

### Priority 2: Add §5 Platform Support
- Add install instructions for all 7 platforms per standards.md §7.11

### Priority 3: Move content to references/
- Move §7 Standards to references/ with 1-line pointer
- Move §10 anti-patterns to references/ with 1-line pointer

---

## Verdict

**Tier: Expert ⭐** (7.85 ≥ 7.0)

This skill demonstrates strong domain knowledge and professional frameworks. Main gap is example specificity. With the recommended fixes, this skill can achieve Exemplary tier (≥9.0).

---
*Generated: 2026-03-24 | Skill Writer v12+*