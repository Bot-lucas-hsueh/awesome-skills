# EVALUATION REPORT — military-officer Skill

**Date:** 2026-03-24  
**Reviewer:** skill-writer  
**Version:** 3.0.0 → 3.1.0

---

## 1. Executive Summary

| Dimension | Score | Weight | Weighted |
|-----------|-------|--------|----------|
| **System Prompt Depth** | 8/10 | 20% | 1.60 |
| **Domain Knowledge Density** | 7/10 | 25% | 1.75 |
| **Workflow Actionability** | 7/10 | 15% | 1.05 |
| **Risk Documentation** | 8/10 | 10% | 0.80 |
| **Example Quality** | 7/10 | 20% | 1.40 |
| **Metadata Completeness** | 6/10 | 10% | 0.60 |
| **TOTAL** | — | 100% | **7.20** |

**Tier:** Expert ⭐ (≥7.0)

---

## 2. Before/After Analysis

### Before Evaluation
- **Score:** Self-reported 8.3/10 (unverified)
- **Status:** production quality
- **Line count:** 579 lines (exceeds 500-line limit)

### After Evaluation
- **Score:** 7.20/10 (calculated)
- **Status:** Expert tier, needs fixes
- **Critical issues:** 4 blocking, 6 non-blocking

---

## 3. Specific Issues Found

### 🔴 CRITICAL (Blocking)

| # | Issue | Location | Severity | Fix Required |
|---|-------|----------|----------|--------------|
| **1** | Missing `platforms` field in YAML | Lines 8-20 | 🔴 Critical | Add platforms array per §7.2 |
| **2** | Missing §5 Platform Support section | SKILL.md | 🔴 Critical | Add 7-platform install matrix |
| **3** | Broken table syntax | Lines 201-203 | 🔴 Critical | Fix incomplete Military Metrics table |
| **4** | Line count exceeds budget | 579 lines | 🔴 Critical | Move §16-21 to `references/` |

### 🟡 MEDIUM (Non-Blocking)

| # | Issue | Location | Severity | Fix Recommendation |
|---|-------|----------|----------|---------------------|
| **5** | Generic scenario examples | §9.1-9.4 | 🟡 Medium | Add military-specific context |
| **6** | No decision point templates in workflow | §8 | 🟡 Medium | Add templates per phase |
| **7** | References files numbered inconsistently | references/ | 🟡 Medium | Rename to match section numbers |
| **8** | Self-score inconsistency | Line 462 | 🟡 Medium | Update to reflect actual score |
| **9** | Missing trigger word examples in description | YAML | 🟡 Medium | Add explicit trigger phrases |

---

## 4. Score Breakdown by Dimension

### 4.1 System Prompt Depth — 8/10

**Strengths:**
- Well-structured role definition (20+ years experience)
- Decision framework with 3 gates
- Thinking patterns (Mission-Oriented, Risk-Calculated, Chain-of-Command, Terrain-Minded)
- Clear communication style guidelines

**Issues:**
- No explicit "fail action" details for each gate
- Could add domain-specific heuristics

### 4.2 Domain Knowledge Density — 7/10

**Strengths:**
- Mission Command Framework (clear visual)
- 5 guiding principles with military precision
- Professional toolkit with 5 tools
- Decision frameworks in §7

**Issues:**
- Military Metrics table broken (lines 201-203 truncated)
- Some sections (§16-21) are verbose and should be moved to references/
- Lacks specific numeric thresholds for some metrics

### 4.3 Workflow Actionability — 7/10

**Strengths:**
- Strategic planning has 4 phases with sub-steps
- Risk assessment has 7 steps with clear progression

**Issues:**
- No [✓ Done] checkpoints per step
- No ✗ FAIL blocks defined
- Missing templates (OPORD, AAR templates referenced but not provided)

### 4.4 Risk Documentation — 8/10

**Strengths:**
- 4 domain risks with severity ratings
- Additional risk register in §17 with probability × impact matrix
- Clear mitigation strategies

**Issues:**
- Risk register in §17 is generic (not military-specific)
- Could add escalation triggers for each risk
- Missing example consequences

### 4.5 Example Quality — 7/10

**Strengths:**
- 2 detailed examples (9.1, 9.2) with full structure
- Scenario examples cover different contexts

**Issues:**
- §9.1-9.4 scenarios are overly generic (could apply to any profession)
- No full conversation flows
- No edge case or anti-pattern correction example
- Missing military-specific edge case (e.g., "what if I need to escalate to command?")

### 4.6 Metadata Completeness — 6/10

**Strengths:**
- 8 metadata fields present
- Version, author, category, tags, difficulty all present

**Issues:**
- ❌ **Missing `platforms` field** — Critical for Agent Skills Standard
- Description lacks explicit trigger phrases
- No `works-with` statement
- Score values appear inconsistent (self-reported 8.3 vs. calculated 7.2)

---

## 5. Concrete Fix Recommendations

### Priority 1: Critical Fixes (Must Fix)

1. **Add platforms field**
   ```yaml
   platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
   ```

2. **Add §5 Platform Support** — Install matrix for all 7 platforms
   - OpenCode: `/skill install military-officer`
   - OpenClaw, Claude Code, Cursor, Codex, Cline, Kimi: session + persistent paths

3. **Fix broken table** — Lines 201-203:
   ```
   | **Readiness Rate** | (Units certified ready / Total units) × 100 | >90% |
   | **Attrition Ratio** | Enemy losses ÷ Friendly losses | >1.0 |
   ```

4. **Reduce line count** — Move to references/:
   - §16 Domain Deep Dive
   - §17 Risk Management Deep Dive
   - §18 Excellence Framework
   - §19 Best Practices Library
   - §20 Case Studies
   - §21 Resources & References

### Priority 2: High-Impact Fixes

5. **Add full conversation flow in §9** — At least one complete multi-turn example
6. **Add OPORD template** — Provide actual template in §6 or references/
7. **Add decision checkpoints in §8** — [✓ Done] per step
8. **Update self-score** — Reflect calculated 7.20

### Priority 3: Polish

9. **Add explicit trigger phrases** to description
10. **Rename reference files** to match section numbers (07-standards.md → 07-standards.md is correct, but 08-workflow.md etc.)
11. **Add specific thresholds** to domain frameworks

---

## 6. Dimension Fix Priority (ROI)

| Fix This First | Current Score | Max Weighted Gain |
|----------------|---------------|-------------------|
| **Metadata** | 6/10 | +0.4 pts |
| **Example Quality** | 7/10 | +0.4 pts |
| **Workflow** | 7/10 | +0.3 pts |
| **Domain Knowledge** | 7/10 | +0.5 pts |

---

## 7. Recommendation

**Action:** Upgrade to v3.1.0 with critical fixes

**Next Steps:**
1. Add platforms field and §5 Platform Support section (Priority 1)
2. Fix broken table and reduce line count (Priority 1)
3. Add conversation flow examples (Priority 2)
4. Update self-score to reflect actual calculation

**Estimated Post-Fix Score:** 7.8-8.2 (Expert tier with room for Exemplary)

---

*Generated by skill-writer methodology v12*
