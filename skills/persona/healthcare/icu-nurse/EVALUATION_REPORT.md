# Skill Evaluation Report: icu-nurse

## Summary
| Attribute | Value |
|-----------|-------|
| **Score** | 8.6/10 |
| **Tier** | Expert ⭐ |
| **File** | `skills/healthcare/icu-nurse/SKILL.md` |
| **Lines** | 631 (exceeds 500 limit) |

---

## Dimension Scores

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| System Prompt Depth | 9/10 | 20% | 1.80 |
| Domain Knowledge Density | 9/10 | 25% | 2.25 |
| Workflow Actionability | 9/10 | 15% | 1.35 |
| Risk Documentation | 9/10 | 10% | 0.90 |
| Example Quality | 8/10 | 20% | 1.60 |
| Metadata Completeness | 9/10 | 10% | 0.90 |

---

## Rubric Analysis

### System Prompt Depth: 9/10 ✅
- Critical Care Nurse with 8+ years, CCRN certification
- ACLS proficiency
- 3 decision gates (emergency, physician orders, scope of practice)
- 4 thinking patterns (Stability First, Trend Analysis, Bundle Compliance, Device Vigilance)
- Communication style: SBAR format

### Domain Knowledge Density: 9/10 ✅
- ICU Assessment Priority Framework (ABCs + Neurology + Other)
- Care bundles (Ventilator, Central Line, Sepsis, Rapid Response)
- ICU quality metrics (VAP, CLABSI, Pressure Injury, Ventilator-Free Days)
- Professional toolkit (ventilator waveforms, hemodynamic parameters, sedation scales)

### Workflow Actionability: 9/10 ✅
- 4-phase shift assessment (Safety → Comprehensive Assessment → Prioritize → Documentation)
- Emergency response 5-step workflow
- Clear phase objectives with detailed sub-steps

### Risk Documentation: 9/10 ✅
- 4 high-severity risks: Delayed Escalation, Ventilator Complications, Hemodynamic Instability, Medication Errors
- Severity ratings with specific mitigation
- Medical disclaimer prominently displayed

### Example Quality: 8/10 ⚠️
- 2 domain-specific examples: Ventilator Alarm Troubleshooting, Hemodynamic Instability
- Both have assessment tables with actions
- §9 scenarios are generic
- Could use more clinical scenario variety

### Metadata Completeness: 9/10 ⚠️
- 8 fields present (missing platforms)
- Description: 253 chars (within limit ✅)
- Version, author, difficulty, category, tags present

---

## Issues Identified

| Issue | Severity | Action |
|-------|----------|--------|
| File length 631 lines | 🔴 High | Exceeds 500 line limit; move §16-21 to references/ |
| Missing platforms field | 🟡 Medium | Add platforms array |
| Generic §9 scenarios | 🟡 Medium | Add more critical care scenarios |

---

## Recommendations

1. **Move to references/**: §16-21
2. **Add platforms field**: For Agent Skills standard
3. **Enhance §9 examples**: Add scenarios like sepsis management, sedation titration, CRRT

---

## Verdict

**Expert ⭐** — Strong critical care nursing skill with comprehensive frameworks and good examples. Primary issue is file length.

**Recommendation**: Accept with file length fix.
