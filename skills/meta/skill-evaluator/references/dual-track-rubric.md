# Dual-Track Scoring System

> Combining text and runtime quality for true competence assessment

---

## The Golden Rule

```
Text Quality must EQUAL Runtime Quality
```

A skill can have:
- ✅ Perfect text quality but fail in practice
- ✅ Good runtime performance but poor documentation
- ✅ Both high = True competence

---

## Weighting Formula

```
Overall Score = (Text Score × 0.5) + (Runtime Score × 0.5)
```

Or for specific needs:

| Focus | Text Weight | Runtime Weight |
|-------|-------------|----------------|
| Documentation | 70% | 30% |
| Balanced | 50% | 50% |
| Performance | 30% | 70% |

---

## Text Quality (6 Dimensions)

| Dimension | Weight | Minimum |
|-----------|--------|---------|
| System Prompt | 20% | 6.0 |
| Domain Knowledge | 20% | 6.0 |
| Workflow | 20% | 6.0 |
| Error Handling | 15% | 5.0 |
| Examples | 15% | 5.0 |
| Metadata | 10% | 5.0 |

**Calculation:**
```
Text Score = Σ(Dimension Score × Weight) / 10
```

---

## Runtime Quality (6 Dimensions)

| Dimension | Weight | Minimum |
|-----------|--------|---------|
| Role Immersion | 20% | 6.0 |
| Framework Execution | 20% | 6.0 |
| Output Actionability | 20% | 6.0 |
| Knowledge Accuracy | 15% | 6.0 |
| Long-Conversation Stability | 15% | 6.0 |
| Resilience & Edge Cases | 10% | 5.0 |

**Calculation:**
```
Runtime Score = Σ(Dimension Score × Weight) / 10
```

---

## Variance Analysis

### Acceptable Variance

| Variance | Status | Action |
|----------|--------|--------|
| < 1.0 points | ✅ Balanced | None |
| 1.0-2.0 points | ⚠️ Imbalanced | Investigate |
| > 2.0 points | ❌ Critical | Major fix |

### Common Patterns

**Pattern 1: Text > Runtime**
- Over-engineered documentation
- Poor actual performance
- **Fix:** Simplify docs, test runtime

**Pattern 2: Runtime > Text**
- Works well but hard to use
- Missing documentation
- **Fix:** Add examples, clarify workflow

**Pattern 3: Both Low**
- Fundamental issues
- **Fix:** Complete rework

---

## Evaluation Levels

### Quick (5 minutes)
```
Text: Quick scan (2 min)
Runtime: Basic test (3 min)
```

### Standard (20 minutes)
```
Text: Full rubric (10 min)
Runtime: 6 dimensions (10 min)
```

### Deep (60 minutes)
```
Text: Detailed analysis (20 min)
Runtime: Extended testing (40 min)
```

### Certification (2 hours)
```
Text: Expert review (30 min)
Runtime: Full adversarial (90 min)
Analysis: Gap analysis (optional)
```

---

## Minimum Thresholds

| Dimension | Critical Threshold |
|-----------|-------------------|
| System Prompt | < 6 = Redesign needed |
| Role Immersion | < 6 = Not production-ready |
| Knowledge Accuracy | < 6 = Dangerous |
| Long-Conversation Stability | < 6 = Unreliable |

---

## Scoring Example

```
Skill: React Architect

Text Quality:
  System Prompt: 9/10 × 20% = 1.8
  Domain Knowledge: 9/10 × 20% = 1.8
  Workflow: 8/10 × 20% = 1.6
  Error Handling: 7/10 × 15% = 1.05
  Examples: 8/10 × 15% = 1.2
  Metadata: 9/10 × 10% = 0.9
  --------------------------------
  Text Score: 8.35/10

Runtime Quality:
  Role Immersion: 9/10 × 20% = 1.8
  Framework Execution: 9/10 × 20% = 1.8
  Output Actionability: 8/10 × 20% = 1.6
  Knowledge Accuracy: 9/10 × 15% = 1.35
  Long-Conversation Stability: 8/10 × 15% = 1.2
  Resilience: 8/10 × 10% = 0.8
  --------------------------------
  Runtime Score: 8.55/10

Overall: (8.35 + 8.55) / 2 = 8.45/10 ✅
Variance: 0.2 (within acceptable range) ✅
```

---

## Certification Criteria

| Criterion | Minimum |
|-----------|---------|
| Text Score | ≥ 8.0 |
| Runtime Score | ≥ 8.0 |
| Variance | < 1.0 |
| All Dimensions | ≥ 6.0 |
| Critical Dimensions | ≥ 7.0 |

---

**Lines:** ~150 | Load for scoring calculations
