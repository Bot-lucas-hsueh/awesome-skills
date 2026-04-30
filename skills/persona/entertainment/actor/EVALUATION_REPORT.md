# EVALUATION REPORT — Actor Skill

## Skill: skills/entertainment/actor/SKILL.md

| Attribute | Value |
|-----------|-------|
| **Version** | 3.0.0 |
| **Current Score** | 8.3/10 (claimed) |
| **Quality Tier** | production |
| **Review Date** | 2026-03-24 |
| **Reviewer** | skill-writer methodology |

---

## Executive Summary

The actor skill has **strong core content** (§1-4, §6-10, §11-12) but suffers from **critical structural violations** that inflate line count with irrelevant content. The skill delivers genuine acting expertise in its first 400 lines but then pollutes itself with 170 lines of generic corporate content (§16-21) that has zero relevance to acting.

**Verdict:** Requires restructuring to remove filler; after cleanup, likely Expert tier (7-8).

---

## Scoring — 6-Dimension Rubric

| Dimension | Weight | Score | Justification |
|-----------|--------|-------|---------------|
| **System Prompt** | 20% | 9/10 | Excellent role definition with decision framework, thinking patterns, and communication style. Distinctive actor perspective. |
| **Domain Knowledge** | 25% | 8/10 | Strong acting frameworks (Stanislavski, Meisner, Cold Reading), professional toolkit, anti-patterns. Missing numeric thresholds in some tables. |
| **Workflow** | 15% | 8/10 | Character development and audition preparation workflows are actionable with phases and steps. Checkpoints present. |
| **Risk** | 10% | 7/10 | 4 domain risks with severity. Some risks lack escalation triggers. Additional §18 content is irrelevant. |
| **Examples** | 20% | 8/10 | §9.1 and §9.2 are excellent acting-specific examples. However §9 scenarios 1-4 are generic business content - wrong. |
| **Metadata** | 10% | 5/10 | Has extra non-standard fields (text_score, runtime_score, variance). Missing §5 Platform Support section. Description acceptable. |

**Weighted Score: 7.7/10 → Expert ⭐**

---

## Before / After Analysis

### BEFORE (Current State)
- **570 lines** (bloat: 170 lines of irrelevant content)
- Sections 16-21 = generic corporate filler
- Scenarios 1-4 in §9 = wrong domain
- Missing §5 Platform Support
- Extra non-standard metadata fields

### AFTER (Target State)
- **~400 lines** (removing filler + restructuring)
- Clean 14-section structure per standards.md §7.3
- All scenarios in §9 relate to acting
- §5 Platform Support added
- Standard 9 metadata fields only

---

## Issues Found

### 🔴 Critical Issues

| # | Issue | Location | Severity | Fix |
|---|-------|----------|----------|-----|
| 1 | **§16-21 are generic corporate/technical filler** - Content about "strategic misalignment," "resource constraints," "excellence framework," "best practices library" has ZERO relevance to acting | Lines 461-570 | 🔴 Critical | DELETE sections 16-21 entirely |
| 2 | **Missing §5 Platform Support** - Required for skill installation across 7 platforms | N/A | 🔴 Critical | ADD new §5 with platform installation table |
| 3 | **§9 Scenarios 1-4 are generic business content** - Initial consultation, problem resolution, strategic planning, quality assurance - wrong domain | Lines 286-384 | 🔴 Critical | REPLACE with acting-specific scenarios OR remove if §9.1-9.2 suffice |
| 4 | **Extra non-standard metadata fields** - text_score, runtime_score, variance not in spec | Lines 16-18 | 🔴 Critical | REMOVE these 3 fields; keep only standard 9 |

### 🟠 Major Issues

| # | Issue | Location | Severity | Fix |
|---|-------|----------|----------|-----|
| 5 | **Missing §13 How to Use This Skill** - Triggers listed at end, not in proper section | End of file | 🟠 Major | ADD §13 with install command + organized trigger list |
| 6 | **Trigger words not organized** - Scattered at end (lines 429-437) | End | 🟠 Major | MOVE to §13; consolidate |

### 🟡 Minor Issues

| # | Issue | Location | Severity | Fix |
|---|-------|----------|----------|-----|
| 7 | **Risk section could use escalation triggers** | §3 | 🟡 Minor | Add concrete escalation triggers to each risk |
| 8 | **§7 frameworks lack numeric thresholds** | Tables in §7 | 🟡 Minor | Add target ranges where applicable |

---

## Concrete Fix Recommendations

### Step 1: Remove Filler (High ROI)
```
DELETE: §16 (Domain Deep Dive) - 21 lines of generic table
DELETE: §17 (Risk Management Deep Dive) - 24 lines of irrelevant risk register
DELETE: §18 (Excellence Framework) - 18 lines of corporate jargon
DELETE: §19 (Best Practices Library) - 11 lines of generic practices
DELETE: §20 (Case Studies) - 9 lines of wrong-domain examples
DELETE: §21 (Resources & References) - 8 lines of placeholder
DELETE: Lines 561-570 (Quality Checklist, Additional Resources) - 10 lines

TOTAL: ~170 lines removed
```

### Step 2: Fix §9 Scenarios
```
OPTION A (Recommended): Remove scenarios 1-4 entirely since §9.1-9.2 are excellent
OPTION B: Replace with 2 additional acting-specific scenarios (callback prep, cold read)
```

### Step 3: Add Missing Sections
```
ADD: §5 Platform Support - 7-platform installation table per standards.md §7.11
ADD: §13 How to Use This Skill - Consolidate trigger words + install guidance
```

### Step 4: Clean Metadata
```
REMOVE: text_score, runtime_score, variance from YAML frontmatter
KEEP: name, description, license, metadata (author, version, updated, tags, category, difficulty, score, quality)
```

---

## Target Structure (14 Sections)

After fixes, the skill should have:

| # | Section | Status | Notes |
|---|---------|--------|-------|
| 1 | System Prompt | ✅ Keep | Excellent as-is |
| 2 | What This Skill Does | ✅ Keep | Good |
| 3 | Risk Disclaimer | ⚠️ Enhance | Add escalation triggers |
| 4 | Core Philosophy | ✅ Keep | Good |
| 5 | Platform Support | ❌ Add | MISSING - add 7-platform table |
| 6 | Professional Toolkit | ✅ Keep | Good |
| 7 | Standards & Quality | ⚠️ Trim | Remove §14 reference pointer |
| 8 | Standard Workflow | ✅ Keep | Good |
| 9 | Scenario Examples | ⚠️ Fix | Keep §9.1-9.2; remove/replace 1-4 |
| 10 | Common Pitfalls | ✅ Keep | Good |
| 11 | Integration | ✅ Keep | Good |
| 12 | Scope & Limitations | ✅ Keep | Good |
| 13 | How to Use This Skill | ❌ Add | MISSING - consolidate triggers |
| 14 | License & Author | ✅ Keep | Present |

---

## Token Budget Analysis

| Metric | Current | After Fix | Budget |
|--------|---------|-----------|--------|
| SKILL.md lines | 570 | ~350 | ≤500 ✅ |
| Non-§1 sections >3 lines | 6 (sections 16-21) | 0 | ≤3 ✅ |
| Description chars | 130 | 130 | ≤263 ✅ |

**Savings:** Removing 170 lines saves ~1,700 tokens per invocation.

---

## Summary

| Dimension | Before | After (Projected) |
|-----------|--------|-------------------|
| System Prompt | 9/10 | 9/10 |
| Domain Knowledge | 8/10 | 8/10 |
| Workflow | 8/10 | 8/10 |
| Risk | 7/10 | 8/10 |
| Examples | 8/10 | 8/10 |
| Metadata | 5/10 | 8/10 |
| **Weighted Score** | **7.7** | **8.2** |
| **Tier** | Expert ⭐ | Expert ⭐ |

**Recommendation:** Proceed with fixes to achieve cleaner structure, proper platform support, and remove 170 lines of irrelevant content.