# EVALUATION REPORT: medical-equipment-engineer

**Date:** 2026-03-24  
**Reviewer:** Skill Writer (skill-writer methodology)  
**Tier:** Community → Expert ⭐

---

## 6-Dimension Quality Rubric Score

| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| **System Prompt Depth** | 20% | 9/10 | Excellent biomedical engineer role, decision framework with 4 gates, thinking patterns (patient safety, risk-based prioritization). |
| **Domain Knowledge Density** | 25% | 9/10 | Strong IEC 60601-1 electrical safety limits, PM protocols, FMEA, regulatory compliance (FDA, Joint Commission, CMS). |
| **Workflow Actionability** | 15% | 8/10 | References external files (§7, §8, §10) instead of inline content. Risk of missing content if references not present. |
| **Risk Documentation** | 10% | 9/10 | Comprehensive risk matrix: patient injury, electrical shock, regulatory non-compliance, downtime, warranty, firmware. |
| **Example Quality** | 20% | 6/10 | §9 has generic business templates. Need medical equipment-specific scenarios. |
| **Metadata Completeness** | 10% | 9/10 | All 9 fields present. Good Chinese trigger words. Description clean. |

### Weighted Score Calculation
```
Score = (9×0.20) + (9×0.25) + (8×0.15) + (9×0.10) + (6×0.20) + (9×0.10)
      = 1.8 + 2.25 + 1.2 + 0.9 + 1.2 + 0.9 = 8.25 → Expert ⭐
```

**Current Tier: Community** (Target: Expert ⭐)

---

## Key Issues Identified

### 🟡 High
1. **External References**: Sections §7, §8, §10 reference external files (references/07-standards.md, etc.) that may not exist or be loaded. Inline key content.
2. **§9 Examples Generic**: Replace with medical equipment-specific scenarios.

### 🟢 Minor
3. Self-score claims 9.5 but weighted calculation shows 8.25 - metadata may need correction.

---

## Recommended Fixes

| Priority | Fix | Expected Score Impact |
|----------|-----|----------------------|
| **1** | Inline §7, §8, §10 key content or verify references exist | +0.4 pts |
| **2** | Add 2 specific clinical equipment scenarios to §9 | +0.6 pts |

**Projected Score After Fixes:**
```
Score = (9×0.20) + (9×0.25) + (9×0.15) + (9×0.10) + (8×0.20) + (9×0.10)
      = 1.8 + 2.25 + 1.35 + 0.9 + 1.6 + 0.9 = 8.8 → Expert ⭐
```

---

## Strengths

- Excellent electrical safety knowledge (IEC 60601-1 limits)
- Strong regulatory awareness (FDA MDR, recall management)
- Good decision gates for safety and scope
- Comprehensive equipment lifecycle model

---

## Anti-Patterns Detected

| Anti-Pattern | Location | Severity |
|--------------|----------|----------|
| **External References** | §7, §8, §10 | 🟡 Medium - Risk of missing content |
| **Generic Examples** | §9 | 🟡 Medium |

---

## Decision

**NEARLY READY** for Expert tier. Inline key reference content and add equipment-specific examples.

**Action Required:** Inline §7/§8/§10 content. Add PM failure response and electrical safety test failure scenarios to §9.
