#!/usr/bin/env bash
# eval.sh — Dual-track evaluation workflow driver
# Usage: ./eval.sh path/to/SKILL.md [quick|standard|deep]
# Guides you through both text and runtime evaluation, saves results.

set -euo pipefail

SKILL_FILE="${1:-}"
DEPTH="${2:-standard}"

if [[ -z "$SKILL_FILE" || ! -f "$SKILL_FILE" ]]; then
  echo "Usage: $0 path/to/SKILL.md [quick|standard|deep]"
  echo ""
  echo "Depths:"
  echo "  quick     5 min  — screening"
  echo "  standard  20 min — regular check (default)"
  echo "  deep      60 min — critical skills"
  exit 1
fi

SKILL_DIR=$(dirname "$SKILL_FILE")
SKILL_NAME=$(basename "$SKILL_DIR")
TIMESTAMP=$(date +%Y%m%d-%H%M)
REPORT_FILE="$SKILL_DIR/EVALUATION_REPORT.md"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  DUAL-TRACK EVALUATION — $DEPTH"
echo "  Skill: $SKILL_NAME"
echo "  Date:  $(date '+%Y-%m-%d %H:%M')"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# ── Step 0: Validate first ──────────────────────────────────────────────────
echo "[ Step 0: Validate frontmatter ]"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
if bash "$SCRIPT_DIR/validate.sh" "$SKILL_FILE"; then
  echo "  → Validation passed, continuing"
else
  echo "  → Validation failed — fix errors before evaluating"
  exit 1
fi
echo ""

# ── Step 1: Text pre-check ──────────────────────────────────────────────────
echo "[ Step 1: Text pre-check ]"
bash "$SCRIPT_DIR/score.sh" "$SKILL_FILE"
echo ""

read -rp "Continue to manual text scoring? [Y/n] " CONT
[[ "${CONT:-y}" =~ ^[Nn] ]] && exit 0

# ── Step 2: Manual text scoring ─────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "[ Step 2: Text Quality Scoring ]"
echo "  Reference: $(realpath "$SKILL_DIR")/../../skill-manager/references/evaluate.md"
echo ""
echo "  Rate each dimension 1–10 using references/evaluate.md rubric:"
echo ""

read -rp "  System Prompt (20%):       " T1
read -rp "  Domain Knowledge (20%):    " T2
read -rp "  Workflow (20%):            " T3
read -rp "  Error Handling (15%):      " T4
read -rp "  Examples (15%):            " T5
read -rp "  Metadata (10%):            " T6

TEXT_SCORE=$(echo "scale=2; ($T1*0.20 + $T2*0.20 + $T3*0.20 + $T4*0.15 + $T5*0.15 + $T6*0.10)" | bc)
echo ""
echo "  Text Score: $TEXT_SCORE/10"

if [[ "$DEPTH" == "quick" ]]; then
  echo ""
  echo "  Quick mode: skipping runtime evaluation."
  echo "  Overall (text only): $TEXT_SCORE/10"
  RUNTIME_SCORE="-"
  OVERALL=$TEXT_SCORE
  VARIANCE="-"
else
  # ── Step 3: Runtime scoring ─────────────────────────────────────────────
  echo ""
  echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
  echo "[ Step 3: Runtime Quality Scoring ]"
  echo "  Reference: evaluate.md — Runtime section"
  echo ""

  if [[ "$DEPTH" == "standard" ]]; then
    echo "  Standard protocol (20 min):"
    echo "  1. Identity check (turn 1)"
    echo "  2. One framework execution"
    echo "  3. Actionability test"
    echo "  4. 3 knowledge facts verified"
    echo "  5. 5-turn stability check"
    echo ""
  else
    echo "  Deep protocol (60 min) — see evaluate.md for full test suite"
    echo ""
  fi

  read -rp "  Role Immersion (20%):           " R1
  read -rp "  Framework Execution (20%):      " R2
  read -rp "  Output Actionability (20%):     " R3
  read -rp "  Knowledge Accuracy (15%):       " R4
  read -rp "  Long-Conv Stability (15%):      " R5
  read -rp "  Resilience & Edge Cases (10%):  " R6

  RUNTIME_SCORE=$(echo "scale=2; ($R1*0.20 + $R2*0.20 + $R3*0.20 + $R4*0.15 + $R5*0.15 + $R6*0.10)" | bc)
  OVERALL=$(echo "scale=2; ($TEXT_SCORE * 0.5 + $RUNTIME_SCORE * 0.5)" | bc)
  VARIANCE=$(echo "scale=2; $TEXT_SCORE - $RUNTIME_SCORE" | bc | tr -d -)

  echo ""
  echo "  Runtime Score: $RUNTIME_SCORE/10"
  echo "  Variance:      $VARIANCE"
fi

# ── Step 4: Gap analysis ────────────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "[ Step 4: Gap Analysis ]"
echo ""

read -rp "  Top improvement (or press Enter to skip): " GAP1
read -rp "  Second improvement (or Enter to skip):    " GAP2
read -rp "  Third improvement (or Enter to skip):     " GAP3

# ── Write report ─────────────────────────────────────────────────────────────
cat > "$REPORT_FILE" <<REPORT
# Evaluation Report

**Skill:** $SKILL_NAME
**Date:** $(date '+%Y-%m-%d %H:%M')
**Depth:** $DEPTH

---

## Scores

| Track | Score |
|-------|-------|
| Text Quality | $TEXT_SCORE/10 |
| Runtime Quality | ${RUNTIME_SCORE}/10 |
| Variance | $VARIANCE |
| **Overall** | **${OVERALL}/10** |

### Text Dimensions

| Dimension | Weight | Score |
|-----------|--------|-------|
| System Prompt | 20% | $T1/10 |
| Domain Knowledge | 20% | $T2/10 |
| Workflow | 20% | $T3/10 |
| Error Handling | 15% | $T4/10 |
| Examples | 15% | $T5/10 |
| Metadata | 10% | $T6/10 |

REPORT

if [[ "$DEPTH" != "quick" ]]; then
cat >> "$REPORT_FILE" <<RUNTIME
### Runtime Dimensions

| Dimension | Weight | Score |
|-----------|--------|-------|
| Role Immersion | 20% | $R1/10 |
| Framework Execution | 20% | $R2/10 |
| Output Actionability | 20% | $R3/10 |
| Knowledge Accuracy | 15% | $R4/10 |
| Long-Conv Stability | 15% | $R5/10 |
| Resilience & Edge Cases | 10% | $R6/10 |

RUNTIME
fi

cat >> "$REPORT_FILE" <<GAPS

## Certification

$(if (( $(echo "$TEXT_SCORE >= 8.0" | bc -l) )) && [[ "$RUNTIME_SCORE" != "-" ]] && (( $(echo "$RUNTIME_SCORE >= 8.0" | bc -l) )) && (( $(echo "$VARIANCE < 1.0" | bc -l) )); then
  echo "- [x] Text Score ≥ 8.0: $TEXT_SCORE ✅"
  echo "- [x] Runtime Score ≥ 8.0: $RUNTIME_SCORE ✅"
  echo "- [x] Variance < 1.0: $VARIANCE ✅"
  echo ""
  echo "**Result: CERTIFIED FOR PRODUCTION ✅**"
else
  [[ $(echo "$TEXT_SCORE >= 8.0" | bc -l) -eq 1 ]] && echo "- [x] Text Score ≥ 8.0: $TEXT_SCORE ✅" || echo "- [ ] Text Score ≥ 8.0: $TEXT_SCORE ❌"
  [[ "$RUNTIME_SCORE" != "-" ]] && {
    [[ $(echo "$RUNTIME_SCORE >= 8.0" | bc -l) -eq 1 ]] && echo "- [x] Runtime Score ≥ 8.0: $RUNTIME_SCORE ✅" || echo "- [ ] Runtime Score ≥ 8.0: $RUNTIME_SCORE ❌"
    [[ $(echo "$VARIANCE < 1.0" | bc -l) -eq 1 ]] && echo "- [x] Variance < 1.0: $VARIANCE ✅" || echo "- [ ] Variance < 1.0: $VARIANCE ❌"
  }
  echo ""
  echo "**Result: NOT CERTIFIED — see gaps below**"
fi)

## Improvements

1. ${GAP1:-No issues noted}
2. ${GAP2:-No issues noted}
3. ${GAP3:-No issues noted}
GAPS

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  EVALUATION COMPLETE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Overall: $OVERALL/10  (Text: $TEXT_SCORE, Runtime: ${RUNTIME_SCORE}, Variance: ${VARIANCE})"
echo "  Report saved: $REPORT_FILE"
