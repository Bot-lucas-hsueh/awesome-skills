# Evaluation Report: pilot

**Skill:** pilot  
**Path:** skills/transport-worker/pilot/SKILL.md  
**Date:** 2026-03-24

## 6-Dimension Quality Rubric

| Dimension | Score | Tier | Notes |
|-----------|-------|------|-------|
| System Prompt Depth | 8.0 | Expert | Strong credentials, P.A.V.E. decision model |
| Domain Knowledge Density | 7.5 | Expert | Good but sections §7-§21 are generic |
| Workflow Actionability | 6.5 | Community | Sections §7-§21 not aviation-specific |
| Risk Documentation | 7.5 | Expert | 7 aviation-specific risks in §3 |
| Example Quality | 6.0 | Community | Generic placeholder scenarios |
| Metadata Completeness | 7.5 | Expert | Has tags but score lower |

**Weighted Score:** 7.1 → **Expert ⭐**

## Issues Found

### Critical Issues
1. **Sections §7-§21 are generic placeholders** - Same pattern as bus-driver
2. **Line count** - 714 lines exceeds 500 limit
3. **Scenarios in §8 are generic** - Not aviation-specific scenarios

### Comparison to truck-driver/taxi-driver
The first 6 sections are strong aviation content:
- Strong system prompt with ATPL, 12,000 hours
- P.A.V.E. decision model
- 7 critical aviation risks
- Good core philosophy with GO/NO-GO framework

But sections §7-§21 break the pattern with generic content.

## Recommendations
- Remove §7-§21 or replace with aviation-specific content
- Keep content under 500 lines
- Add real aviation scenario examples (fuel calculation, go/no-go, approach)

## Compliance Issues

- [x] YAML present
- [ ] SKILL.md ≤500 lines (714 lines)
- [ ] Sections §7-§21 are domain-specific (NO)

## Final Verdict

**Status:** Expert ⭐ - Needs upgrade. Content before §7 is strong but latter sections are generic.