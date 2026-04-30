# EVALUATION REPORT: emergency-manager

## Overall Assessment

| Metric | Value |
|--------|-------|
| **Weighted Score** | 9.3/10 |
| **Quality Tier** | Exemplary ⭐⭐ |
| **Recommendation** | APPROVED - Minimal updates needed |

---

## Dimension Scores

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| **System Prompt Depth** | 9.5 | 20% | 1.90 |
| **Domain Knowledge Density** | 9.5 | 25% | 2.38 |
| **Workflow Actionability** | 9.5 | 15% | 1.43 |
| **Risk Documentation** | 9.5 | 10% | 0.95 |
| **Example Quality** | 9.5 | 20% | 1.90 |
| **Metadata Completeness** | 8.0 | 10% | 0.80 |
| **TOTAL** | | 100% | **9.3** |

---

## Detailed Evaluation

### ✅ System Prompt Depth (9.5/10)
- **Strengths**: Comprehensive identity with 20+ years experience, CEM certification; decision framework with priority hierarchy (Life Safety → Incident Stabilization → Property Protection → Restoration → Recovery); 4 quality gates; 4 detailed thinking patterns (ICS structure, THIRA, Crisis Communication, Comprehensive Emergency Management Cycle)
- **Suggestions**: Consider adding domain-specific heuristics for special scenarios (CBRN, pandemic variants)

### ✅ Domain Knowledge Density (9.5/10)
- **Strengths**: ICS positions table with responsibilities; ESFs table with lead agencies; Federal disaster assistance programs; comprehensive NIMS coverage
- **Suggestions**: Add international disaster frameworks (UNDAC, Sphere Standards)

### ✅ Workflow Actionability (9.5/10)
- **Strengths**: 3-phase workflow (Initial Response, Sustained Operations, Extended Operations) with clear deliverables and checkpoints
- **Suggestions**: Add failure criteria for each phase

### ✅ Risk Documentation (9.5/10)
- **Strengths**: 7 risks in matrix format with severity (🔴 Critical, 🟠 Medium, 🟡) and mitigation; covers command failure, communication breakdown, resource shortage, staff fatigue, public panic, secondary disasters, recovery delay
- **Suggestions**: Add escalation triggers and example consequences

### ✅ Example Quality (9.5/10)
- **Strengths**: 5 diverse, comprehensive scenarios: Hurricane Response, Active Shooter, Hazardous Materials, Wildfire Evacuation, Pandemic Response; each with detailed tables, action items, decision criteria
- **Suggestions**: All scenarios are high-quality; consider adding one edge case that corrects an anti-pattern

### ⚠️ Metadata Completeness (8.0/10)
- **Strengths**: All required fields present: name, description, author, version, category, difficulty, tags
- **Issues**: 
  - Non-standard YAML block format with custom fields (runtime_score, variance)
  - Missing platforms field (should list: [opencode, openclaw, claude, cursor, codex, cline, kimi])
  - Description is 320+ chars (may be invisible with 40+ skills installed)

---

## Token Budget Analysis

| Metric | Current | Limit | Status |
|--------|---------|-------|--------|
| SKILL.md lines | 783 | 500 | ⚠️ OVER |
| Description chars | ~320 | 263 | ⚠️ OVER |

**Recommendations**:
- Move reference tables to `references/` directory
- Trim description to ≤263 chars (or ≤130 if 60+ skills installed)

---

## Recommendations

### Priority 1 - Required
1. Add `platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]` to metadata
2. Trim description to ≤263 characters
3. Move extended reference content to `references/` to reduce SKILL.md below 500 lines

### Priority 2 - Suggested
4. Add failure criteria to workflow phases
5. Add international disaster frameworks to Domain Knowledge

---

## Summary

This skill is **Exemplary** quality with comprehensive coverage of emergency management. The main issues are token budget (line count and description length) and missing platforms field. With minor updates to format, this skill meets all Expert/Exemplary criteria.

**Self-Score Verification**: 9.5/10 → 9.3/10 (adjusted for metadata format)
