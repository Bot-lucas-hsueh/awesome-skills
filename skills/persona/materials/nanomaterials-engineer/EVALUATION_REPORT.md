# Evaluation Report: nanomaterials-engineer

## Summary
**Score: 8.15/10 → Expert ⭐**  
**Quality: standard**

## 6-Dimension Rubric Scoring

| Dimension | Score | Weight | Weighted | Tier |
|-----------|-------|--------|----------|------|
| System Prompt Depth | 9/10 | 20% | 1.80 | Expert |
| Domain Knowledge Density | 8/10 | 25% | 2.00 | Expert |
| Workflow Actionability | 7/10 | 15% | 1.05 | Community |
| Risk Documentation | 8/10 | 10% | 0.80 | Expert |
| Example Quality | 8/10 | 20% | 1.60 | Expert |
| Metadata Completeness | 9/10 | 10% | 0.90 | Expert |

## Strengths
- **System Prompt**: 5 gate questions + 5 thinking patterns in code block, strong role credentials
- **Domain Knowledge**: Materials engineering hierarchy, characterization pyramid, quantitative metrics
- **Risk Documentation**: 7 risks with 🔴/🟡/🟢 severity, domain-specific consequences (inhalation toxicity, heavy metal toxicity, pyrophoric hazards)
- **Examples**: Good anti-patterns, 4 scenarios with some Python code, integration table with 3 cross-skill combinations
- **Metadata**: Description 210 chars, all 9 fields

## Weaknesses
- **Workflow** (7/10): Generic 4-phase workflow template. Domain content exists separately in phases
- **References**: Points to references/standards-reference.md and references/common-pitfalls.md - verify these exist

## Issues to Fix

### High Priority
1. **Add §5 Platform Support**: Missing installation instructions for 7 platforms
2. **Consolidate workflow**: Merge generic §8 with domain-specific content
3. **Move §16-21 to references/**: ~150 lines of generic filler

### Medium Priority
4. **Trigger words table**: Should add specific trigger phrases in §13
5. **Verify references content**: Check referenced files exist and have complete content

## Token Budget
- SKILL.md: 688 lines (exceeds 500-line limit)
- References: 4 files (standards-reference.md, scenario-examples.md, standard-workflow.md, common-pitfalls.md)
- Offload priority: §16-21 (~150 lines) should move to references/

## Recommendation
**Approaching Exemplary**: Second-highest scoring (8.15). Close to Exemplary if workflow unified and platform support added.