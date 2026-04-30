# Evaluation Report: bus-driver

**Skill:** bus-driver  
**Path:** skills/transport-worker/bus-driver/SKILL.md  
**Date:** 2026-03-24

## 6-Dimension Quality Rubric

| Dimension | Score | Tier | Notes |
|-----------|-------|------|-------|
| System Prompt Depth | 8.0 | Expert | Good credentials, but decision framework has 5 gates |
| Domain Knowledge Density | 7.5 | Expert | Decent content in §1-§7, but loses focus in §8-§21 |
| Workflow Actionability | 6.5 | Community | Sections §8-§21 are generic placeholders, not bus-specific |
| Risk Documentation | 7.5 | Expert | 7 risks with severity |
| Example Quality | 6.0 | Community | Only generic scenarios in §8-§21 |
| Metadata Completeness | 7.5 | Expert | Has tags but some fields missing |

**Weighted Score:** 7.1 → **Expert ⭐**

## Issues Found

### Critical Issues
1. **Sections §8-§21 are generic placeholders** - These sections copy a generic "Discovery → Analysis → Implementation → Review" workflow that applies to any domain. Should be replaced with bus-specific content:
   - Section 8: Should describe actual bus operations workflow
   - Section 9-21: Should be removed or replaced with bus-specific content
2. **Scenarios in §8 are generic** - "Initial Consultation", "Problem Resolution" - not bus operations scenarios
3. **Line count excessive** - 719 lines far exceeds 500 line limit

### Anti-Patterns Detected
- **Scope Creep**: Undefined domain focus in later sections
- **Generic Content**: §8-§21 appear to be template copy-paste

### Recommendations
- Remove or replace §8-§21 with bus-specific content
- Reduce total lines to ≤500
- Add proper school bus operation scenarios (stop arm, loading, evacuation)

## Compliance Issues

- [x] YAML present but quality: standard (not exemplary)
- [ ] SKILL.md ≤500 lines (719 lines - EXCEEDS)
- [ ] Sections §8-§21 contain domain-specific content (NO - generic)

## Final Verdict

**Status:** Expert ⭐ - Needs upgrade. Sections §8-§21 should be replaced with domain-specific content per References-First principle.