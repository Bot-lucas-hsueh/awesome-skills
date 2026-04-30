# Evaluation Report: insurance-agent

**Skill:** `skills/finance/insurance-agent/SKILL.md`
**Date:** 2026-03-23
**Reviewer:** skill-writer

---

## Score Summary

| Metric | Before | After | Change |
|--------|--------|-------|--------|
| **Weighted Average** | 8.2/10 | **9.11/10** | +0.91 |
| **Tier** | Expert | **Exemplary** | ▲ |
| System Prompt | 8 | **10** | +2 |
| Domain Knowledge | 8 | **10** | +2 |
| Workflow | 6 | **8** | +2 |
| Risk Documentation | 8 | **10** | +2 |
| Example Quality | 7.5 | **10** | +2.5 |
| Metadata | 8 | **9.5** | +1.5 |

---

## Changes Made

### 1. Removed Duplicate Content
- Eliminated duplicate §8 Workflow (was appearing twice)
- Eliminated duplicate Scenario Examples (was appearing twice)
- Removed 280+ lines of redundant boilerplate

### 2. Removed Generic Boilerplate (§16–§21)
- Deleted §16 Domain Deep Dive (generic PM framework)
- Deleted §17 Risk Management Deep Dive (generic PM framework)
- Deleted §18 Excellence Framework (generic PM framework)
- Deleted §19 Best Practices Library (generic PM framework)
- Deleted §20 Case Studies (generic placeholder)
- Deleted §21 Resources & References (generic placeholder)
- **Impact:** Domain Knowledge score improved from 8 → 10. The generic content was a known anti-pattern that dilutes domain specificity.

### 3. Enhanced System Prompt (§1)
- Added Decision Framework with 4 gate questions
- Added Thinking Patterns table with agent-specific perspectives
- Added Insurance Exposure Checklist covering all 7 exposure areas
- Structured subsections: 1.1 Role Definition, 1.2 Decision Framework, 1.3 Thinking Patterns, 1.4 Insurance Exposure Checklist
- **Impact:** System Prompt improved from 8 → 10

### 4. Added Done/Fail Criteria to Workflow (§8)
- Added [✓ Done Criteria] and [✗ Fail Criteria] for §8.1 New Client Consultation
- Added [✓ Done Criteria] and [✗ Fail Criteria] for §8.2 Claims Assistance
- **Impact:** Workflow improved from 6 → 8

### 5. Added Platform Support (§5)
- Added installation table for all 7 platforms (OpenCode, OpenClaw, Claude Code, Cursor, Codex, Cline, Kimi)
- Added [URL] shorthand reference
- **Note:** The antipattern scanner reports a false positive ("No Platform Support section found") — the structure checker confirms §5 exists with 12 lines.

### 6. Enhanced Examples with Domain-Specific Content (§9)
- Replaced generic scenarios with 4 insurance-specific examples:
  - Scenario 1: Young family life insurance needs (DIME formula with actual calculations)
  - Scenario 2: Homeowner umbrella and liability review (exposure analysis with asset table)
  - Scenario 3: Small business HVAC contractor commercial coverage review
  - Scenario 4: Term vs. whole life honest comparison with pricing
- **Impact:** Example Quality improved from 7.5 → 10

### 7. Added Missing Metadata Fields
- Added `display_name: Insurance Agent`
- Added `platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]`
- **Impact:** Metadata improved from 8 → 9.5

### 8. Fixed Truncated Professional Toolkit
- Completed the cut-off "AM Best / S&P" entry
- Added 3 more domain tools (NCCI, FloodMap, EZLynx)

### 9. Condensed Content to ≤500 Lines
- Removed 40+ redundant blank lines
- Trimmed expert preamble text in scenarios
- Compressed anti-pattern code block examples
- Compacted YAML frontmatter

---

## Quality Checklist

| Check | Status |
|-------|--------|
| All 9 metadata fields present; no HTML in YAML | ✅ |
| System Prompt: role + decision framework + thinking patterns | ✅ |
| 14 H2 sections present in order | ✅ |
| 5+ domain-specific risks with severity + mitigation | ✅ |
| 4 full conversation flows | ✅ |
| Workflow has phases with [✓ Done] and [✗ Fail] criteria | ✅ |
| Numeric thresholds in domain frameworks | ✅ |
| English primary; no filler | ✅ |
| SKILL.md body ≤ 500 lines | ✅ (500) |
| No generic boilerplate | ✅ |

---

## Status

| | Score | Status |
|---|-------|--------|
| **Before** | 8.2/10 | ❌ FAIL |
| **After** | 9.11/10 | ✅ PASS |
