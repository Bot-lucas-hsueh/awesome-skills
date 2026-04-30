# Evaluation Report: superconducting-materials-researcher

## Summary
**Score: 7.8/10 → Expert ⭐**  
**Quality: production**

## 6-Dimension Rubric Scoring

| Dimension | Score | Weight | Weighted | Tier |
|-----------|-------|--------|----------|------|
| System Prompt Depth | 9/10 | 20% | 1.80 | Expert |
| Domain Knowledge Density | 8/10 | 25% | 2.00 | Expert |
| Workflow Actionability | 6/10 | 15% | 0.90 | Community |
| Risk Documentation | 8/10 | 10% | 0.80 | Expert |
| Example Quality | 7/10 | 20% | 1.40 | Community |
| Metadata Completeness | 9/10 | 10% | 0.90 | Expert |

## Strengths
- **System Prompt**: Excellent 5-gate decision tree in §4, Jc characterization philosophy, flux pinning framework
- **Domain Knowledge**: Deep technical content (REBCO, Nb3Sn, Jc(B,T,θ), flux pinning), Python code examples
- **Risk Documentation**: 5 domain-specific risks (quench, cryogen loss, strain damage, flux jump, chemical incompatibility)
- **Metadata**: All 9 fields complete, description 172 chars

## Weaknesses
- **Workflow** (6/10): Generic 4-phase workflow template that could apply to any domain. Domain-specific content exists in Phase 1-3 sections but main §8 is generic "Discovery/Analysis/Implementation/Review"
- **Examples** (7/10): 5 anti-patterns are excellent but scenarios are generic templates. Need superconductor-specific multi-turn examples
- **Filler content**: §16-21 are generic templates that should be moved to references/

## Issues to Fix

### Critical
1. **§8 Workflow is too generic**: Replace with superconductor-specific workflow (e.g., Material Selection → Characterization → Fabrication → Magnet Integration)

### High Priority
2. **Add 2 domain-specific scenarios**: Current Scenario 1-4 are generic templates. Add superconducting-specific examples:
   - "Design flux pinning strategy for REBCO tape at 12T, 4.2K"
   - "Compare Nb3Sn vs REBCO for DEMO fusion coil"
3. **Move §16-21 to references/**: These are generic filler sections that add token cost without value

### Medium Priority
4. **Platform Support missing**: No §5 Platform Support section for installation instructions
5. **Trigger words in §13**: Should include specific trigger phrases for the skill

## Token Budget
- SKILL.md: 788 lines (exceeds 500-line limit)
- References: 4 files present (code-block-1/2/3.md, workflow.md)
- Offload priority: §16-21 should move to references/

## Recommendation
**Upgrade to Expert Verified**: All dimensions ≥6. Fix workflow to be domain-specific. Move filler sections to references/.