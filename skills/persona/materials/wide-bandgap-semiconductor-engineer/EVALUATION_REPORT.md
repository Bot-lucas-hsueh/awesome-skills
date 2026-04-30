# Evaluation Report: wide-bandgap-semiconductor-engineer

## Summary
**Score: 8.25/10 → Expert ⭐**  
**Quality: production**

## 6-Dimension Rubric Scoring

| Dimension | Score | Weight | Weighted | Tier |
|-----------|-------|--------|----------|------|
| System Prompt Depth | 9/10 | 20% | 1.80 | Expert |
| Domain Knowledge Density | 8/10 | 25% | 2.00 | Expert |
| Workflow Actionability | 7/10 | 15% | 1.05 | Community |
| Risk Documentation | 9/10 | 10% | 0.90 | Expert |
| Example Quality | 8/10 | 20% | 1.60 | Expert |
| Metadata Completeness | 9/10 | 10% | 0.90 | Expert |

## Strengths
- **System Prompt**: 5 gate questions + 5 thinking patterns in code block, strong role credentials
- **Domain Knowledge**: Device design hierarchy, BFOM formulas, quantitative targets
- **Risk Documentation**: 7 domain-specific risks with CRITICAL/HIGH/MEDIUM severity (bipolar degradation, gate oxide, GaN trapping, thermal runaway, etc.)
- **Examples**: 6 anti-patterns with ❌/✅ examples, good scenarios
- **Metadata**: Description 210 chars, all 9 fields

## Weaknesses
- **Workflow** (7/10): Still uses generic 4-phase template in §8. Domain content exists in separate Phase 1-4 sections but main workflow is generic
- **Filler sections**: §16-21 are generic templates that add 150+ lines

## Issues to Fix

### High Priority
1. **Consolidate workflow**: Merge §8 generic workflow with domain-specific Phase 1-4 content into single coherent workflow
2. **Move §16-21 to references/**: Token waste, generic filler content
3. **Add §5 Platform Support**: Missing installation instructions for 7 platforms

### Medium Priority
4. **Trigger words table**: Should add specific trigger phrases in §13
5. **Description character count**: At 210 chars with <40 skills installed it's fine, but could trim for scalability

## Token Budget
- SKILL.md: 751 lines (exceeds 500-line limit)
- References: 4 files present (07-standards.md, 08-workflow.md, 09-scenarios.md, 10-pitfalls.md)
- Offload priority: §16-21 (~150 lines) should move to references/

## Recommendation
**Approaching Exemplary**: All dimensions ≥7 except workflow at 7. Fix workflow to be unified, move filler sections, add platform support section.