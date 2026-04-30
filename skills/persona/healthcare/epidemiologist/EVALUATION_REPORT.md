# EVALUATION_REPORT: epidemiologist

**Skill:** `skills/healthcare/epidemiologist/SKILL.md`
**Evaluator:** skill-writer (6-dimension rubric)
**Date:** 2026-03-24

---

## §7.1 Quality Rubric Assessment

| Dimension | Weight | Score (1-10) | Notes |
|-----------|--------|--------------|-------|
| **System Prompt Depth** | 20% | 9.0 | Role + decision framework + thinking patterns |
| **Domain Knowledge Density** | 25% | 9.5 | Outbreak investigation, R0/Rt estimation, study design, Bradford Hill criteria |
| **Workflow Actionability** | 15% | 8.5 | Detection → Investigation → Analysis → Control → Reporting (5 phases) |
| **Risk Documentation** | 10% | 8.5 | 4 risks with severity, but lacks full mitigation details |
| **Example Quality** | 20% | 9.5 | 5 scenarios: foodborne outbreak, R0 estimation, case-control, surveillance, vaccine effectiveness |
| **Metadata Completeness** | 10% | 8.5 | Most fields, but missing `platforms` and `display_name` |
| **WEIGHTED TOTAL** | 100% | **9.00** | **Expert ⭐** |

---

## §7.2 Metadata Verification

| Field | Required | Present | Value |
|-------|----------|---------|-------|
| name | ✓ | ✓ | `epidemiologist` |
| display_name | — | ✗ | Missing |
| author | ✓ | ✓ | `neo.ai <lucas_hsueh@hotmail.com>` |
| version | ✓ | ✓ | `3.0.0` |
| difficulty | ✓ | ✓ | `expert` |
| category | ✓ | ✓ | `healthcare` |
| tags | ✓ | ✓ | 9 tags ✅ |
| platforms | — | ✗ | Missing |
| description | ✓ | ✓ | ~220 chars ✅ |

**Status:** ⚠️ PARTIAL — Missing `display_name` and `platforms`.

---

## §7.3 16-Section Compliance

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 1 | System Prompt | ✅ Present | 60 lines |
| 2 | What This Skill Does | ✅ Present | 6 capabilities (table) |
| 3 | Risk Disclaimer | ✅ Present | 4 risks |
| 4 | Core Philosophy | ✅ Present | Epidemiological method hierarchy |
| 5 | Platform Support | ❌ MISSING | No §5 section |
| 6 | Professional Toolkit | ✅ Present | Software + formulas |
| 7 | Domain Knowledge | ✅ Present | Outbreak steps, epidemic curves |
| 8 | Scenario Examples | ✅ Present | 5 scenarios |
| 9 | Workflow | ✅ Present | 5 phases |
| 10 | Anti-Patterns | ✅ Present | 5 anti-patterns |
| 11 | References | ✅ Present | Agency URLs |
| 12 | Integration | ✅ Present | Brief mention |
| — | §13-§16 | ❌ MISSING | No How to Use, License, Version |

**Status:** ❌ FAIL — Missing §5, §13-§16.

---

## §7.9 Token Budget

| Metric | Limit | Actual | Status |
|--------|-------|--------|--------|
| SKILL.md body | ≤500 lines | 380 lines | ✅ PASS |
| Description chars | ≤263 chars | ~220 chars | ✅ PASS |

**Status:** ✅ PASS

---

## Strengths

1. **R0/Rt transmission dynamics** — Epidemiological modeling with formulas
2. **Bradford Hill criteria** — Causal inference framework
3. **Study design comparison** — Cohort, case-control, cross-sectional with use cases
4. **5 realistic scenarios** — Foodborne outbreak, R0 estimation, case-control, surveillance, vaccine effectiveness
5. **Software toolkit** — R, SAS, Python, Epi Info with specific uses
6. **Epidemic curve interpretation** — Point source, propagated, continuous, mixed patterns

---

## Issues

| Priority | Issue | Fix Required |
|----------|-------|--------------|
| 🔴 HIGH | Missing §5 Platform Support | Add all 7 platforms |
| 🔴 HIGH | Missing §13 How to Use | Add trigger words, install instructions |
| 🔴 HIGH | Missing §14-§16 License/Version | Add MIT + version history |
| 🟡 MEDIUM | YAML: missing `display_name` | Add `display_name: Epidemiologist` |
| 🟡 MEDIUM | YAML: missing `platforms` | Add `platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]` |
| 🟡 MEDIUM | Risk section lacks detailed mitigation | Expand each risk with specific actions |

---

## Recommendation

**⚠️ NEEDS SIGNIFICANT FIX — Expert tier (9.00)**

Content is strong but missing critical structural sections.

**Required Actions:**
1. Add §5 Platform Support (all 7 platforms)
2. Add §13 How to Use with trigger words and install instructions
3. Add §14-§16 License, Author, Version History
4. Add `display_name` and `platforms` to YAML metadata
