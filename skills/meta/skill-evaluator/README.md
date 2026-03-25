# Skill Evaluator v2

> **Dual-Track Validation** — Text quality + Runtime quality = True competence

---

## Philosophy

**A skill is not a document. A skill is a capability.**

- **Text quality** = Potential (what it claims)
- **Runtime quality** = Reality (what it delivers)
- **Gap** = Risk (where it might fail)

**Golden Rule:** Text must equal Runtime. Neither can compensate.

**Deep Testing:** Stress test, adversarial test, long-run validation.

---

## Test Levels

| Level | Time | Tests | Use When |
|-------|------|-------|----------|
| **Quick** | 5 min | 4 basic tests | Initial screening |
| **Standard** | 20 min | 6 runtime dimensions | Regular evaluation |
| **Deep** | 60 min | Extended stress tests | Critical skills |
| **Certification** | 2-3 hrs | Full adversarial suite | Production release |

---

## Quick Start

### 30-Second Evaluation

```bash
./scripts/quick-eval.sh path/to/SKILL.md
```

### Standard Evaluation (20 min)

```bash
./scripts/dual-eval.sh path/to/SKILL.md
```

### Deep Stress Test (60 min)

```bash
./scripts/deep-test.sh path/to/SKILL.md
```

### Full Certification (2-3 hrs)

```bash
./scripts/certify-skill.sh path/to/SKILL.md
```

---

## Dual-Track System

```
                    RUNTIME QUALITY
              Low      Good      Excellent
            (<7)      (7-8.9)    (>8.5)
           ┌─────────┬──────────┬──────────┐
    High   │Fix      │ Good     │ EXCELLENT│
   (>8.5)  │Runtime  │ Match    │ ⭐⭐       │
           │         │          │          │
TEXT       ├─────────┼──────────┼──────────┤
QUALITY    │ Risky   │ SOLID    │ Good     │
  Good     │ ⚠️      │ ⭐        │ Match    │
  (7-8.5)  │         │          │          │
           ├─────────┼──────────┼──────────┤
    Low    │ Broken  │ Fix      │ Mismatch │
   (<7)    │ ✗       │ Text     │ Fix Text │
           │         │          │          │
           └─────────┴──────────┴──────────┘
```

---

## Quality Tiers

| Tier | Text | Runtime | Gap | Status |
|------|------|---------|-----|--------|
| **Exemplary** ⭐⭐ | ≥9.0 | ≥8.5 | ≤1.0 | Showcase |
| **Expert** ⭐ | ≥7.5 | ≥7.5 | ≤1.5 | Production |
| **Community** | ≥6.0 | ≥6.0 | ≤2.0 | Caution |
| **Needs Work** | <6.0 | <6.0 | >2.0 | Fix first |

---

## Resources

### Core Documentation

| Resource | Purpose |
|----------|---------|
| `references/text-evaluation.md` | Text quality 6 dimensions |
| `references/runtime-evaluation.md` | Runtime 6 dimensions |
| `references/deep-runtime-testing.md` | Extended stress tests |
| `references/adversarial-testing.md` | Security & integrity |
| `references/dual-track-rubric.md` | Scoring system |
| `references/gap-analysis.md` | Diagnose & fix gaps |
| `references/anti-patterns.md` | Common failures |
| `references/comprehensive-test-checklist.md` | Master checklist |

### Historical Assets

| Resource | Purpose |
|----------|---------|
| `EVALUATION-REPORT-ACTUAL.md` | 58 skills tested |
| `EXPECTED-VS-ACTUAL.md` | Gap analysis |
| `RETROSPECTIVE.md` | Lessons learned |
| `METHODOLOGY.md` | Methodology deep dive |
| `PROCESS.md` | Process flowcharts |
| `COMPARISON-V1-V2.md` | Version comparison |

---

## Scripts

```bash
# Quick scan (2 minutes)
./scripts/quick-eval.sh skill.md

# Standard dual-track (20 minutes)
./scripts/dual-eval.sh skill.md

# Text quality only
./scripts/quick-text-check.sh skill.md

# Deep stress test (60 minutes)
./scripts/deep-test.sh skill.md

# Adversarial testing (60 minutes)
./scripts/adversarial-test.sh skill.md

# Full certification (2-3 hours)
./scripts/certify-skill.sh skill.md
```

---

## Test Categories

### 1. Marathon Tests
- 20-turn conversation stability
- Multi-session consistency
- Interruption recovery
- Context retention

### 2. Adversarial Tests
- Prompt injection resistance
- Role break attempts
- Misinformation handling
- Emotional manipulation defense
- Jailbreak prevention

### 3. Complexity Tests
- Compound problems
- Constraint accumulation
- Conflicting requirements
- Multi-skill integration

### 4. Real-World Simulations
- Crisis handling
- Stakeholder management
- Ambiguous requirements
- Time pressure

---

## Key Innovations

### 1. Token Efficiency
```
SKILL.md: ~80 lines (~500 tokens)
References: Detailed guides (on demand)
Result: Fast load, deep evaluation when needed
```

### 2. Text = Runtime
```
No more "beautiful but broken" skills
No more "working but messy" skills
Both must be high
```

### 3. Gap Diagnosis
```
5 patterns:
- Beautiful but Broken → Fix runtime
- Working but Messy → Fix text
- Degradation → Fix stability
- Framework Fail → Fix execution
- Knowledge Rot → Update facts
```

### 4. Deep Testing
```
Marathon: 20+ turn conversations
Adversarial: 50+ attack vectors
Stress: Compound complexity
Certification: Production readiness
```

---

## Usage Examples

### Evaluate New Skill

```bash
# Step 1: Quick check
./scripts/quick-eval.sh my-skill/SKILL.md

# Step 2: Standard evaluation
./scripts/dual-eval.sh my-skill/SKILL.md

# Step 3: Check gap
# If gap > 1.5, apply fixes from gap-analysis.md

# Step 4: Deep test (if critical)
./scripts/deep-test.sh my-skill/SKILL.md
```

### Production Certification

```bash
# Full certification for production
./scripts/certify-skill.sh critical-skill/SKILL.md

# Outputs certification ID and artifacts
# Archive for audit trail
```

### Monthly Regression

```bash
# Test random sample of skills
for skill in skills/enterprise/*/; do
  if [ $((RANDOM % 5)) -eq 0 ]; then
    ./scripts/dual-eval.sh "$skill/SKILL.md"
  fi
done
```

---

## Integration with Skill Writer

```
Create skill (skill-writer)
    ↓
Quick eval (5 min)
    ↓
If passes → Standard eval (20 min)
    ↓
If gap > 1.5 → Back to writer
If gap <= 1.5 → Deep test (if critical)
    ↓
If certified → Production
```

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 2.0.0 | 2026-03-21 | Deep testing, adversarial tests, certification suite |
| 1.0.0 | 2026-03-20 | Initial dual-track validation |

---

## License

MIT

**Core Principle:** True skill competence = Text quality × Runtime quality × Resilience

---

**Next:** Read `references/comprehensive-test-checklist.md` to start your evaluation.
