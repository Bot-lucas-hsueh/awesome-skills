# Copywriter Skill — Evaluation Report

## 1. Executive Summary

| Metric | Score |
|--------|-------|
| **Weighted Average** | 6.4 / 10 |
| **Tier** | Community (needs upgrade to Expert) |
| **Critical Issues** | 3 |
| **High Priority Issues** | 4 |
| **Recommended Actions** | 8 |

---

## 2. Before/After Analysis

### Current State (v3.0.0)
- **Overall Score**: 6.4/10 — Community tier (needs work to reach Expert ≥7.0)
- **Strengths**: Strong system prompt, good risk documentation, solid frameworks section
- **Weaknesses**: Examples are template garbage, description exceeds budget, missing platforms, generic late sections

### Target State (v3.1.0)
- **Goal**: Expert tier (≥7.0)
- **Focus**: Fix examples, trim description, add platforms, remove/generic content

---

## 3. Dimension-by-Dimension Scoring

| Dimension | Weight | Score | Weighted | Tier |
|-----------|--------|-------|----------|------|
| System Prompt Depth | 20% | 8 | 1.60 | Expert ⭐ |
| Domain Knowledge Density | 25% | 7 | 1.75 | Expert ⭐ |
| Workflow Actionability | 15% | 7 | 1.05 | Expert ⭐ |
| Risk Documentation | 10% | 8 | 0.80 | Expert ⭐ |
| Example Quality | 20% | 3 | 0.60 | Basic |
| Metadata Completeness | 10% | 6 | 0.60 | Community |
| **TOTAL** | 100% | — | **6.40** | Community |

---

## 4. Issues Found

### 🔴 Critical Issues

| # | Issue | Dimension | Location | Fix Required |
|---|-------|-----------|----------|--------------|
| **C1** | Examples (§9) are completely wrong — generic software project scenarios that don't involve copywriting at all. This is template garbage. | Examples | §9, lines 278–384 | Replace with real copywriting scenarios |
| **C2** | Description field exceeds 263-char budget (actual: ~320 chars) AND contains `...` which is an HTML comment pattern. | Metadata | Lines 3–6 | Trim to ≤263 chars, remove `...` |
| **C3** | Late sections (§14–§21) contain generic filler content that adds no value for a copywriting skill. | Domain | Lines 431–541 | Remove or consolidate to references/ |

### 🟡 High Priority Issues

| # | Issue | Dimension | Location | Fix Required |
|---|-------|-----------|----------|--------------|
| **H1** | Missing `platforms` field in metadata (required for Expert tier) | Metadata | Line 8 | Add: `platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]` |
| **H2** | Description has redundancy: "Expert-level Copywriter skill..." appears twice | Metadata | Lines 3–6 | Consolidate into single sentence |
| **H3** | Section §5 Platform Support is completely missing — required section | Workflow | Missing | Add platform installation table |
| **H4** | Sections §14–§21 are generic content that doesn't belong in a copywriting skill (knowledge maturity model, risk register, excellence framework, etc.) | Domain | Lines 431–541 | Remove entirely |

### 🟢 Minor Issues

| # | Issue | Location | Fix Required |
|---|-------|----------|--------------|
| **M1** | §11 Integration with Other Skills — has correct skills but could reference more | Line 400 | Add `content-writer`, `seo-specialist` |
| **M2** | Score in metadata (9.5/10) doesn't match actual quality | Line 16 | Update to reflect actual evaluation |
| **M3** | `text_score` and `runtime_score` in metadata appear unnecessary | Lines 18–19 | Remove non-standard fields |

---

## 5. Concrete Fix Recommendations

### Priority 1: Fix Examples (§9) — Highest ROI
**Current**: Template garbage (software PM scenarios)  
**Target**: Real copywriting conversation flows

**Required Examples**:

```
Scenario A: Landing Page Copy Request
- Context: Client needs landing page copy for B2B SaaS product
- User Input: "Write landing page copy for our AI analytics tool..."
- Response: Follows Phase 1-5 workflow with specific output

Scenario B: Email Sequence Request  
- Context: Client needs welcome email sequence
- User Input: "Create a 5-email welcome sequence for our course..."
- Response: Shows email framework with subject lines + body

Scenario C: Ad Copy Request
- Context: Client needs Google Ads copy
- User Input: "Write ad copy for our CRM software..."
- Response: 3 headlines + 2 descriptions per spec
```

### Priority 2: Fix Metadata
**Description Fix**:
```yaml
description: >
  Expert copywriter with 12+ years experience in conversion copywriting, brand voice, 
  email sequences, and ads. Writes landing pages, sales emails, ad copy, and brand messaging.
  Use when: writing copy, optimizing conversions, creating email sequences, developing brand voice.
```

**Add platforms field**:
```yaml
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
```

### Priority 3: Remove Generic Content
- Delete entirely: §14 Quality Verification (reference only), §16 Domain Deep Dive, §17 Risk Management Deep Dive, §18 Excellence Framework, §19 Best Practices Library, §20 Case Studies, §21 Resources
- These add ~110 lines of zero-value content

### Priority 4: Add Missing §5 Platform Support
Add section with installation instructions for all 7 platforms.

---

## 6. Score Impact Analysis

| Fix | Dimension Impact | Expected Score Gain |
|-----|-------------------|---------------------|
| Replace §9 examples | Examples: 3→8 | +1.0 |
| Trim description + add platforms | Metadata: 6→9 | +0.3 |
| Remove generic late sections | Domain: stays 7 | 0 (but cleaner) |
| Add §5 Platform Support | Workflow: 7→8 | +0.15 |
| **Total** | — | **+1.45** |

**Projected Score**: 6.4 + 1.45 = **7.85 → Expert ⭐**

---

## 7. Recommended File Changes

### SKILL.md Changes Required:

1. **Lines 1–21**: Fix metadata — trim description, add platforms, remove non-standard fields
2. **Delete**: Lines 45–62 (blank space)
3. **Lines 278–384 (§9)**: Replace with real copywriting scenarios
4. **Add**: §5 Platform Support section (after §4 Core Philosophy)
5. **Delete**: Sections §14–§21 (lines ~431–541) — generic filler

---

## 8. Summary

| Aspect | Finding |
|--------|---------|
| **Current Score** | 6.4/10 (Community) |
| **Target Score** | 7.85/10 (Expert ⭐) |
| **Critical Flaws** | Wrong examples, budget exceeded description, missing sections |
| **Best Section** | §1 System Prompt (excellent copywriter guidance) |
| **Worst Section** | §9 Examples (template garbage) |
| **Estimated Fix Effort** | 2 hours |

The copywriter skill has strong fundamentals in the system prompt and frameworks, but critical gaps in examples and metadata. The examples section needs complete rewrite to show real copywriting workflows. Once fixed, this skill can achieve Expert tier.
