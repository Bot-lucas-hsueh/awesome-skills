# Skill Evaluation Report

## Skill: tour-guide

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Prompt Quality** | 7.0 | Strong role definition in §1 but buried among generic content |
| **Domain Knowledge** | 9.0 | Excellent tour guide content (storytelling, group management, safety) |
| **Workflow Clarity** | 8.5 | Clear workflows, but generic §8-21 bloat |
| **Risk Documentation** | 9.0 | Comprehensive risk table (lost tourist, medical emergency, weather) |
| **Examples Quality** | 8.5 | Test case is domain-appropriate; scenarios generic |
| **Metadata Quality** | 8.0 | Complete YAML but duplicate tags |

**Overall Score: 8.4/10 → Community**

---

## Critical Issues

### 1. Generic Content Bloat (Severity: 🔴 High)
Sections §8-21 (lines 299-674) are copy-pasted generic business/workflow content:
- "Phase 1: Discovery & Assessment" — irrelevant to tour guide
- "Success Metrics: Efficiency +20%" — meaningless for service worker
- "Case Studies: Legacy system limitations" — completely off-domain
- "Risk ID R001: Strategic misalignment" — corporate jargon

**Impact:** 280+ lines of useless content, high token cost per invocation

### 2. Missing Language-Specific Content (Severity: 🟡 Medium)
Description mentions "cultural interpretation" but no guidance on handling language barriers.

### 3. Duplicate Tags (Severity: 🟢 Low)
Tags contain duplicates: `tour-guide, tour-guide, sightseeing`

---

## Recommendations

| Priority | Action |
|----------|--------|
| **P0 (Required)** | Remove sections §8-21 entirely (lines 299-674) |
| **P1 (High)** | Add multi-language handling to §7 or §6 |
| **P2 (Medium)** | Clean up duplicate tags |

---

## Score Breakdown

```
Prompt × 0.20 = 7.0 × 0.20 = 1.40
Domain × 0.25 = 9.0 × 0.25 = 2.25
Workflow × 0.15 = 8.5 × 0.15 = 1.28
Risk × 0.10 = 9.0 × 0.10 = 0.90
Examples × 0.20 = 8.5 × 0.20 = 1.70
Metadata × 0.10 = 8.0 × 0.10 = 0.80
─────────────────────────────────
Total = 8.33 ≈ 8.3
```

---

## Tier Classification

| Tier | Threshold | This Skill |
|------|-----------|------------|
| Exemplary ⭐⭐ | ≥9.0 | No |
| Expert ⭐ | ≥7.0 | Yes → Community |
| Basic | <5.0 | No |

**Recommendation:** Upgrade to Expert by removing generic content.
