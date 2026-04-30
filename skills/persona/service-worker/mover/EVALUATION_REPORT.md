# Skill Evaluation Report

## Skill: mover

| Dimension | Score | Notes |
|-----------|-------|-------|
| **Prompt Quality** | 7.0 | Strong role definition in §1 but buried among generic content |
| **Domain Knowledge** | 9.5 | Excellent mover content (lifting safety, truck loading, special items) |
| **Workflow Clarity** | 9.0 | Very clear workflows (pre-move, loading, transport, unloading) |
| **Risk Documentation** | 9.5 | Comprehensive risk table with proper mitigations |
| **Examples Quality** | 8.5 | Test case is domain-appropriate; scenarios generic |
| **Metadata Quality** | 8.5 | Complete YAML |

**Overall Score: 8.6/10 → Community**

---

## Critical Issues

### 1. Generic Content Bloat (Severity: 🔴 High)
Sections §8-21 (lines 323-697) are copy-pasted generic business/workflow content:
- "Phase 1: Discovery & Assessment" — irrelevant to mover
- "Success Metrics: Efficiency +20%" — meaningless for service worker
- "Case Studies: Legacy system limitations" — completely off-domain
- "Risk ID R001: Strategic misalignment" — corporate jargon

**Impact:** 280+ lines of useless content, high token cost per invocation

### 2. Missing Equipment Check (Severity: 🟡 Medium)
No pre-move equipment checklist beyond general tools table.

---

## Recommendations

| Priority | Action |
|----------|--------|
| **P0 (Required)** | Remove sections §8-21 entirely (lines 323-697) |
| **P1 (Medium)** | Add equipment checklist to §6 |

---

## Score Breakdown

```
Prompt × 0.20 = 7.0 × 0.20 = 1.40
Domain × 0.25 = 9.5 × 0.25 = 2.38
Workflow × 0.15 = 9.0 × 0.15 = 1.35
Risk × 0.10 = 9.5 × 0.10 = 0.95
Examples × 0.20 = 8.5 × 0.20 = 1.70
Metadata × 0.10 = 8.5 × 0.10 = 0.85
─────────────────────────────────
Total = 8.63 ≈ 8.6
```

---

## Tier Classification

| Tier | Threshold | This Skill |
|------|-----------|------------|
| Exemplary ⭐⭐ | ≥9.0 | No |
| Expert ⭐ | ≥7.0 | Yes → Community |
| Basic | <5.0 | No |

**Recommendation:** Upgrade to Expert by removing generic content.
