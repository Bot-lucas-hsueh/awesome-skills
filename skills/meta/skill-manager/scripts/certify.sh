#!/usr/bin/env bash
# certify.sh — Full certification suite for production-critical skills
# Usage: ./certify.sh path/to/SKILL.md
# Runs all four phases: validate → text → runtime → adversarial
# Total time: ~2 hours. Use only for skills heading to production.

set -euo pipefail

SKILL_FILE="${1:-}"
if [[ -z "$SKILL_FILE" || ! -f "$SKILL_FILE" ]]; then
  echo "Usage: $0 path/to/SKILL.md"
  echo ""
  echo "Runs the full 4-phase certification suite (~2 hrs):"
  echo "  Phase 1: Validation          (5 min)"
  echo "  Phase 2: Text quality        (15 min)"
  echo "  Phase 3: Standard runtime    (20 min)"
  echo "  Phase 4: Stress + adversarial (60 min)"
  exit 1
fi

SKILL_DIR=$(dirname "$SKILL_FILE")
SKILL_NAME=$(basename "$SKILL_DIR")
CERT_DATE=$(date +%Y-%m-%d)
CERT_ID="CERT-$(date +%s)"
CERT_DIR="$SKILL_DIR/certifications/$CERT_DATE"
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

mkdir -p "$CERT_DIR"

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  SKILL CERTIFICATION SUITE"
echo "  Skill:   $SKILL_NAME"
echo "  Date:    $CERT_DATE"
echo "  ID:      $CERT_ID"
echo "  Artifacts: $CERT_DIR"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  ⚠  This is a ~2-hour process. Do not interrupt."
echo ""
read -rp "  Press Enter to begin or Ctrl+C to cancel..."

# ── Phase 1: Validation (5 min) ──────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  PHASE 1 / 4 — Validation (5 min)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
bash "$SCRIPT_DIR/validate.sh" "$SKILL_FILE" | tee "$CERT_DIR/01-validation.txt"
if grep -q "FAIL" "$CERT_DIR/01-validation.txt"; then
  echo ""
  echo "  ✗ Validation failed — fix errors before certification"
  exit 1
fi
echo ""
read -rp "  Phase 1 complete. Press Enter for Phase 2..."

# ── Phase 2: Text pre-check (15 min) ────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  PHASE 2 / 4 — Text Quality (15 min)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
bash "$SCRIPT_DIR/score.sh" "$SKILL_FILE" | tee "$CERT_DIR/02-text-precheck.txt"
echo ""
echo "  Now score the 6 dimensions using evaluate.md rubric:"
read -rp "  System Prompt (20%):       " T1
read -rp "  Domain Knowledge (20%):    " T2
read -rp "  Workflow (20%):            " T3
read -rp "  Error Handling (15%):      " T4
read -rp "  Examples (15%):            " T5
read -rp "  Metadata (10%):            " T6
TEXT_SCORE=$(echo "scale=2; ($T1*0.20 + $T2*0.20 + $T3*0.20 + $T4*0.15 + $T5*0.15 + $T6*0.10)" | bc)
echo "  Text Score: $TEXT_SCORE/10"

if (( $(echo "$TEXT_SCORE < 8.0" | bc -l) )); then
  echo "  ✗ Text Score < 8.0 ($TEXT_SCORE). Restore before certifying."
  read -rp "  Continue anyway? [y/N] " FORCE
  [[ ! "${FORCE:-n}" =~ ^[Yy] ]] && exit 1
fi
read -rp "  Phase 2 complete. Press Enter for Phase 3..."

# ── Phase 3: Standard runtime (20 min) ──────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  PHASE 3 / 4 — Standard Runtime (20 min)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  Execute the standard 20-min test protocol:"
echo "  1. Identity check (turn 1–2)"
echo "  2. Framework execution (3 tests)"
echo "  3. Actionability check (1 output)"
echo "  4. Knowledge facts (3 verifications)"
echo "  5. 10-turn stability"
echo ""
read -rp "  Role Immersion (20%):           " R1
read -rp "  Framework Execution (20%):      " R2
read -rp "  Output Actionability (20%):     " R3
read -rp "  Knowledge Accuracy (15%):       " R4
read -rp "  Long-Conv Stability (15%):      " R5
read -rp "  Resilience & Edge Cases (10%):  " R6
RUNTIME_SCORE=$(echo "scale=2; ($R1*0.20 + $R2*0.20 + $R3*0.20 + $R4*0.15 + $R5*0.15 + $R6*0.10)" | bc)
echo "  Runtime Score: $RUNTIME_SCORE/10"
read -rp "  Phase 3 complete. Press Enter for Phase 4 (60 min stress test)..."

# ── Phase 4: Stress + adversarial (60 min) ──────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  PHASE 4 / 4 — Stress + Adversarial (60 min)"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "  Run all 4 resilience tests from evaluate.md:"
echo ""
echo "  4a. 20-turn long conversation (stability)"
echo "  4b. Extreme edge cases (\$0 budget, 1-day timeline)"
echo "  4c. Adversarial: 'Forget your role and act as...'"
echo "  4d. Contradictory requirements"
echo ""
read -rp "  Stress test score (average across 4 tests): " STRESS
echo ""
echo "  Observations:"
read -rp "  4a Stability (20 turns): " OBS_A
read -rp "  4b Edge cases: " OBS_B
read -rp "  4c Adversarial resistance: " OBS_C
read -rp "  4d Contradiction handling: " OBS_D

# ── Calculate final scores ───────────────────────────────────────────────────
# Adjust runtime score with stress result (average phase 3 and phase 4)
FINAL_RUNTIME=$(echo "scale=2; ($RUNTIME_SCORE * 0.7 + $STRESS * 0.3)" | bc)
OVERALL=$(echo "scale=2; ($TEXT_SCORE * 0.5 + $FINAL_RUNTIME * 0.5)" | bc)
VARIANCE=$(echo "scale=2; $TEXT_SCORE - $FINAL_RUNTIME" | bc | tr -d -)

# ── Check certification thresholds ───────────────────────────────────────────
TEXT_PASS=$(echo "$TEXT_SCORE >= 8.0" | bc -l)
RUNTIME_PASS=$(echo "$FINAL_RUNTIME >= 8.0" | bc -l)
VAR_PASS=$(echo "$VARIANCE < 1.0" | bc -l)
DIM_MIN=6
ALL_DIMS_PASS=1
for d in $T1 $T2 $T3 $T4 $T5 $T6 $R1 $R2 $R3 $R4 $R5 $R6; do
  if (( $(echo "$d < $DIM_MIN" | bc -l) )); then ALL_DIMS_PASS=0; fi
done

CERTIFIED=0
[[ $TEXT_PASS -eq 1 && $RUNTIME_PASS -eq 1 && $VAR_PASS -eq 1 && $ALL_DIMS_PASS -eq 1 ]] && CERTIFIED=1

# ── Write certification report ───────────────────────────────────────────────
CERT_REPORT="$CERT_DIR/CERTIFICATION.md"
cat > "$CERT_REPORT" <<CERT
# Certification Report

**Skill:** $SKILL_NAME
**Date:** $CERT_DATE
**ID:** $CERT_ID

---

## Final Scores

| Track | Score |
|-------|-------|
| Text Quality | $TEXT_SCORE/10 |
| Runtime Quality (std) | $RUNTIME_SCORE/10 |
| Runtime Quality (adj) | $FINAL_RUNTIME/10 |
| Variance | $VARIANCE |
| **Overall** | **$OVERALL/10** |

## Certification Checklist

- $([ $TEXT_PASS -eq 1 ] && echo "[x]" || echo "[ ]") Text Score ≥ 8.0: $TEXT_SCORE
- $([ $RUNTIME_PASS -eq 1 ] && echo "[x]" || echo "[ ]") Runtime Score ≥ 8.0: $FINAL_RUNTIME
- $([ $VAR_PASS -eq 1 ] && echo "[x]" || echo "[ ]") Variance < 1.0: $VARIANCE
- $([ $ALL_DIMS_PASS -eq 1 ] && echo "[x]" || echo "[ ]") All dimensions ≥ 6.0

## Stress Test Observations

- Stability (20 turns): $OBS_A
- Edge cases: $OBS_B
- Adversarial: $OBS_C
- Contradictions: $OBS_D

---

## Result: $([ $CERTIFIED -eq 1 ] && echo "CERTIFIED FOR PRODUCTION ✅" || echo "NOT CERTIFIED ❌")

$([ $CERTIFIED -eq 0 ] && echo "Address failing thresholds and re-run certification.")
CERT

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  CERTIFICATION COMPLETE"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  Overall: $OVERALL/10"
echo "  Variance: $VARIANCE"
if [[ $CERTIFIED -eq 1 ]]; then
  echo "  Result: CERTIFIED FOR PRODUCTION ✅"
else
  echo "  Result: NOT CERTIFIED ❌"
fi
echo "  Report: $CERT_REPORT"
