# Skill Evaluation Report

## Skill: restaurant-server

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Prompt Quality** | 7.5 | Has extra §1.1-1.4 generic framework before proper role def |
| **Domain Knowledge** | 9.0 | Excellent restaurant content (table management, allergies, wine) |
| **Workflow Clarity** | 9.0 | Clear service cycles and timing standards |
| **Risk Documentation** | 9.0 | Comprehensive risk table (allergens, alcohol, food safety) |
| **Examples Quality** | 8.5 | Test case is domain-appropriate; scenarios generic |
| **Metadata Quality** | 8.0 | Complete YAML |

**Overall Score: 8.5/10 → Community**

---

## Critical Issues

### 1. Generic Content Bloat (Severity: 🔴 High)
Lines 75-130 contain generic "System Prompt" boilerplate irrelevant to restaurant server:
- "1.1 Role Definition" — generic corporate fluff
- "1.2 Decision Framework" — generic first principles
- "1.3 Thinking Patterns" — generic analytical approach

Then sections §8-21 (lines 479-639) add another 160+ lines of generic business content.

### 2. Section Structure Issue (Severity: 🟡 Medium)
The extra §1.1-1.4 content breaks the standard 16-section template and adds confusion.

### 3. Duplicate Section 8 (Severity: 🟡 Medium)
Section §8 appears twice: once as generic workflow (lines 479-530) and earlier content.

---

## Recommendations

| Priority | Action |
|----------|--------|
| **P0 (Required)** | Remove lines 75-130 (extra System Prompt section) |
| **P1 (Required)** | Remove sections §8-21 duplicate (lines 479-639) |
| **P2 (Medium)** | Clean up duplicate sections |

---

## Score Breakdown

```
Prompt × 0.20 = 7.5 × 0.20 = 1.50
Domain × 0.25 = 9.0 × 0.25 = 2.25
Workflow × 0.15 = 9.0 × 0.15 = 1.35
Risk × 0.10 = 9.0 × 0.10 = 0.90
Examples × 0.20 = 8.5 × 0.20 = 1.70
Metadata × 0.10 = 8.0 × 0.10 = 0.80
─────────────────────────────────
Total = 8.50
```

---

## Tier Classification

| Tier | Threshold | This Skill |
|------|-----------|------------|
| Exemplary ⭐⭐ | ≥9.0 | No |
| Expert ⭐ | ≥7.0 | Yes → Community |
| Basic | <5.0 | No |

**Recommendation:** Upgrade to Expert by removing generic content and duplicate sections.
