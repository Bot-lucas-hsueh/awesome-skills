# EVALUATION REPORT: airworthiness-certification-engineer

## Summary
| Metric | Value |
|--------|-------|
| **Weighted Score** | 7.45/10 |
| **Tier** | Expert ⭐ |
| **Original Score** | 7.9/10 |
| **Variance** | 0.45 |

---

## Dimension Scores

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| System Prompt Depth | 20% | 8 | 1.60 |
| Domain Knowledge Density | 25% | 8 | 2.00 |
| Workflow Actionability | 15% | 7 | 1.05 |
| Risk Documentation | 10% | 8 | 0.80 |
| Example Quality | 20% | 6 | 1.20 |
| Metadata Completeness | 10% | 8 | 0.80 |
| **Total** | 100% | — | **7.45** |

---

## Detailed Analysis

### Strengths ✅

1. **System Prompt (8/10)**: Strong identity - 20+ years experience, DER, Form 1 signatory. 5-gate decision framework (Regulatory Basis, Product Category, Novelty, Safety Assessment, Jurisdiction). Thinking patterns specific to certification.

2. **Domain Knowledge (8/10)**: Comprehensive - FAA/EASA/CAAC certification, DO-178C/DO-254, ARP4761/4754A, safety assessment, BASA validation. References specific standards (14 CFR Part 23/25/27/29/33).

3. **Workflow (7/10)**: 4-phase generic workflow present. Could be more certification-specific.

4. **Risk Documentation (8/10)**: 6 risks with CATASTROPHIC/CRITICAL/SERIOUS/MODERATE severity. Specific mitigation actions.

5. **Anti-Patterns Present**: Good anti-patterns in §7 covering DO-178C documentation, failure classification, Issue Paper timing, BASA scope.

### Issues ❌

1. **Examples (6/10)**: 4 scenarios but **generic** with [problem] placeholders. Not specific to airworthiness certification workflows.

2. **Missing §5 Platform Support**: No install instructions for 7 platforms.

3. **References-First Violations**:
   - §6: "See references/07-standards.md" - should have content
   - §7: "See references/08-workflow.md" - should have content
   - §10: Anti-patterns exist in body but should be in references/

4. **Body Length**: 695 lines - exceeds 500-line domain skill limit. Needs offloading.

---

## Anti-Patterns Detected

| # | Anti-Pattern | Severity | Location |
|---|--------------|----------|----------|
| 1 | Generic examples | 🟡 Medium | §9 |
| 2 | Missing §5 Platform | 🟡 Medium | Section absent |
| 3 | Body exceeds 500 lines | 🔴 High | 695 lines |
| 4 | Content in references/ | 🟢 Low | §6, §7 |

---

## Upgrade Recommendations

### Priority 1: Reduce Body Length
- Move anti-patterns (§10) to references/10-anti-patterns.md
- Move §6 Standards to references/
- Move §7 Workflow to references/
- Target: ≤500 lines

### Priority 2: Fix Examples
- Create certification-specific scenarios:
  - "FAA denies our TC application - next steps"
  - "DO-178C DAL-A software has MC/DC gap"

### Priority 3: Add §5 Platform Support

---

## Verdict

**Tier: Expert ⭐** (7.45 ≥ 7.0)

Strong certification domain knowledge. Main issues: body overflow, generic examples, missing platform section. Fixing body length is critical for token budget compliance.

---
*Generated: 2026-03-24 | Skill Writer v12+*