# Evaluation Report: lockheed-martin

## Metadata
| Field | Value |
|-------|-------|
| name | lockheed-martin |
| author | skill-restorer v7 |
| version | N/A (not in frontmatter) |
| quality | excellence (claimed) |
| score | 7.2/10 |

## 6-Dimension Scoring

| Dimension | Weight | Score | Weighted |
|-----------|--------|-------|----------|
| **System Prompt Depth** | 20% | 8.0 | 1.60 |
| **Domain Knowledge** | 25% | 8.0 | 2.00 |
| **Workflow Actionability** | 15% | 8.0 | 1.20 |
| **Risk Documentation** | 10% | 5.0 | 0.50 |
| **Example Quality** | 20% | 8.0 | 1.60 |
| **Metadata Completeness** | 10% | 3.0 | 0.30 |
| **TOTAL** | 100% | — | **7.20** |

**Tier: Expert ⭐ (7.0-8.9)**

---

## Dimension Analysis

### ✅ System Prompt Depth (8/10)
**Strengths:**
- Clear VP Engineering persona
- Mission Readiness Priority Hierarchy (5 levels)
- Decision Criteria Matrix with weights
- Thinking patterns: threat-driven development, systems-of-systems, lifecycle optimization
- DoD terminology and MIL-STD reference guidance

**Improvements:**
- Add more domain-specific heuristics

### ✅ Domain Knowledge Density (8/10)
**Strengths:**
- Comprehensive LM program coverage: F-35, C-130, C-5, Black Hawk, CH-53K, Orion, missiles
- Current 2025 data: $75B revenue, 191 F-35 deliveries
- Technical specifications for major programs
- Skunk Works heritage and current focus
- Space systems and advanced development

**Improvements:**
- Reference-heavy; more content could be inline

### ✅ Workflow Actionability (8/10)
**Strengths:**
- 5 phases aligned with DoD acquisition lifecycle
- Detailed activities per phase
- Clear decision points (Milestone A/B/C)
- Sustainment metrics included

**Improvements:**
- Add done/fail criteria per phase

### ⚠️ Risk Documentation (5/10)
**Weaknesses:**
- No explicit risk section
- No risk matrix table
- Could benefit from program-specific risks (F-35 sustainment, Columbia-class, etc.)

**Priority Fix:** Add explicit risk section

### ✅ Example Quality (8/10)
**Strengths:**
- 5 detailed example scenarios:
  - F-35 TR-3/Block 4 integration
  - C-130 fleet modernization
  - Skunk Works autonomous teaming
  - Space domain architecture
  - International industrial participation
- Technical depth in each
- Decision frameworks provided

**Improvements:**
- Could add one anti-pattern correction

### ⚠️ Metadata Completeness (3/10)
**Critical Issues:**
- NO YAML frontmatter at all
- Missing: name, version, author, description, category, platforms, tags
- Title only "Lockheed Martin"

**Priority Fix:** Add proper YAML frontmatter per skill-writer standard

---

## Recommended Actions

1. **Add YAML Frontmatter (Critical):**
```yaml
---
name: lockheed-martin
version: 1.0.0
author: skill-restorer v7
description: 'Lockheed Martin VP Engineering perspective on defense programs...'
quality: expert
---
```

2. **Add Risk Section** — Explicit risk matrix for program/schedule/cost risks

3. **Add Platform Support** — Installation instructions for skill

---

## Summary

| Status | Assessment |
|--------|------------|
| **Overall** | Expert ⭐ (7.2/10) |
| **Highest** | Examples, Workflow, Domain Knowledge, System Prompt (8/10) |
| **Lowest** | Metadata (3/10), Risk (5/10) |
| **Blocking Issue** | Missing YAML frontmatter |
| **Quick Win** | Add metadata + risk section |

**Recommendation:** Add metadata frontmatter and risk section. Content quality is high — structural compliance needed.

---
*Evaluated: 2026-03-24 | skill-writer methodology*
