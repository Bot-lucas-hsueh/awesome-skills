# Tools Reference

> Four scripts that automate the skill management lifecycle. Use them in sequence.

---

## Overview

| Script | Stage | Time | Purpose |
|--------|-------|------|---------|
| `validate.sh` | Any | 5 sec | Check frontmatter against agentskills spec |
| `score.sh` | Create / Restore | 5 sec | Heuristic text quality pre-check |
| `eval.sh` | Evaluate | 5–60 min | Interactive dual-track evaluation |
| `certify.sh` | Ship | ~2 hrs | Full certification suite |

**Run order**: `validate.sh` → `score.sh` → `eval.sh` → `certify.sh`

---

## validate.sh

Checks the SKILL.md frontmatter against the agentskills open spec. Run this before anything else — a skill with an invalid name or description will not trigger correctly.

```bash
./scripts/validate.sh path/to/SKILL.md
```

**Checks**:
- Frontmatter delimiters present
- `name` field: matches directory name, lowercase + hyphens only, no consecutive hyphens, max 64 chars
- `description` field: present, 50–1024 chars
- No non-spec top-level keys (flags fields that should move to `metadata:`)
- SKILL.md line count: warn at > 300, fail at > 500
- `references/` directory presence
- System Prompt sections (§1.1/1.2/1.3) present

**Exit codes**: 0 = pass, 1 = fail

**Example output**:
```
[ Frontmatter ]
  ✓ Frontmatter delimiters present (lines 1–17)

[ name field ]
  ✓ name matches directory: skill-manager
  ✓ name characters valid
  ✓ name has no leading/trailing hyphens
  ✓ name has no consecutive hyphens
  ✓ name length: 13/64

[ description field ]
  ✓ description length: 312/1024

[ Optional fields ]
  ✓ No non-spec top-level fields

[ Progressive disclosure ]
  ✓ SKILL.md line count: 181 ✓
  ✓ references/ directory present (4 .md files)

[ Content structure ]
  ✓ System Prompt section found
  ✓ §1.1 Identity found
  ✓ §1.2 Decision Framework found
  ✓ §1.3 Thinking Patterns found

  PASS — No issues found
```

---

## score.sh

Heuristic text quality check. Uses pattern matching to estimate scores across the 6 dimensions in under 5 seconds. Accurate enough to catch major issues; not a substitute for human review.

```bash
./scripts/score.sh path/to/SKILL.md
```

**What it checks**:

| Dimension | Method |
|-----------|--------|
| System Prompt | Detects §1.1/1.2/1.3 headers |
| Domain Knowledge | Counts specific data signals (%, numbers, named frameworks); penalizes generic terms |
| Workflow | Counts workflow sections and Done/Fail criteria |
| Error Handling | Detects anti-pattern, edge case, risk sections |
| Examples | Counts example section headers and mentions |
| Metadata | Checks for name, description, license, metadata fields |

**Limitations**: Cannot evaluate content quality — only structure and signals. A skill can score 8/10 on score.sh and still have weak domain knowledge if it uses specific-looking but irrelevant data. Use as a fast filter, then run `eval.sh` for depth.

---

## eval.sh

Interactive dual-track evaluation. Guides you through both text and runtime scoring, then writes a structured `EVALUATION_REPORT.md`.

```bash
./scripts/eval.sh path/to/SKILL.md [quick|standard|deep]
```

**Depths**:

| Depth | Time | What it skips |
|-------|------|---------------|
| `quick` | 5 min | Runtime evaluation |
| `standard` | 20 min | Nothing — standard 20-min protocol |
| `deep` | 60 min | Nothing — extended runtime test |

**Process**:
1. Runs `validate.sh` — stops on validation failure
2. Runs `score.sh` — heuristic pre-check
3. Prompts for manual text dimension scores (1–10 each)
4. For standard/deep: prompts for runtime dimension scores
5. Computes: `Overall = (Text × 0.5) + (Runtime × 0.5)`, `Variance = |Text − Runtime|`
6. Prompts for top 3 improvements
7. Writes `EVALUATION_REPORT.md` in the skill directory

**Output file**: `path/to/skill/EVALUATION_REPORT.md`

---

## certify.sh

Full certification suite. Four phases, ~2 hours total. Use only for skills that will be widely distributed or used in critical workflows.

```bash
./scripts/certify.sh path/to/SKILL.md
```

**Four phases**:

| Phase | Time | What |
|-------|------|------|
| 1. Validation | 5 min | `validate.sh` — must pass to continue |
| 2. Text quality | 15 min | `score.sh` + manual scoring; blocks if Text < 8.0 |
| 3. Standard runtime | 20 min | 20-min protocol (same as `eval.sh standard`) |
| 4. Stress + adversarial | 60 min | 20-turn stability, extreme edge cases, adversarial resistance, contradictions |

**Certification thresholds** — all must pass:
- Text ≥ 8.0
- Runtime (adjusted) ≥ 8.0
- Variance < 1.0
- All dimensions ≥ 6.0

**Output**: `certifications/YYYY-MM-DD/CERTIFICATION.md` in the skill directory

---

## Integration: Where Each Tool Fits

### CREATE workflow

```bash
# After writing draft:
./scripts/validate.sh my-skill/SKILL.md    # Fix spec violations first
./scripts/score.sh my-skill/SKILL.md       # Quick quality check
# If score < 7.0, revise before evaluating
./scripts/eval.sh my-skill/SKILL.md standard
```

### EVALUATE workflow

```bash
# Start with pre-checks:
./scripts/validate.sh skill/SKILL.md
./scripts/score.sh skill/SKILL.md
# Full evaluation:
./scripts/eval.sh skill/SKILL.md standard   # → EVALUATION_REPORT.md
```

### RESTORE workflow

```bash
# Baseline before restoring:
./scripts/score.sh original/SKILL.md > before.txt
# After restoration:
./scripts/score.sh restored/SKILL.md > after.txt
diff before.txt after.txt
./scripts/eval.sh restored/SKILL.md standard
```

### Ship to production

```bash
# Only after eval.sh passes:
./scripts/certify.sh skill/SKILL.md        # → certifications/CERTIFICATION.md
```
