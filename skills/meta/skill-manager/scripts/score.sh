#!/usr/bin/env bash
# score.sh — Automated text quality pre-check
# Usage: ./score.sh path/to/SKILL.md
# Produces a quick heuristic score across the 6 text dimensions.
# NOT a replacement for human + LLM evaluation — use as a first filter.

set -euo pipefail

SKILL_FILE="${1:-}"
if [[ -z "$SKILL_FILE" || ! -f "$SKILL_FILE" ]]; then
  echo "Usage: $0 path/to/SKILL.md"
  exit 1
fi

SKILL_DIR=$(dirname "$SKILL_FILE")

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  TEXT QUALITY PRE-CHECK"
echo "  $(basename "$SKILL_DIR")"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

TOTAL=0
MAX=0

# Helper: score a dimension, print result, accumulate weighted score
# dim_score NAME WEIGHT SCORE NOTES
dim_score() {
  local name="$1" weight="$2" score="$3" notes="$4"
  local weighted
  weighted=$(echo "scale=2; $score * $weight / 100" | bc)
  TOTAL=$(echo "scale=2; $TOTAL + $weighted" | bc)
  MAX=$(echo "scale=2; $MAX + $weight / 100 * 10" | bc)
  printf "  %-22s %2d/10  (×%.2f)  %s\n" "$name" "$score" "$(echo "scale=2; $weight/100" | bc)" "$notes"
}

# ── Dimension 1: System Prompt (20%) ───────────────────────────────────────
SP_SCORE=2
SP_NOTES=""
HAS_SP=$(grep -ci "system prompt\|§ 1\b" "$SKILL_FILE" || true)
HAS_11=$(grep -c "1\.1\|§ 1\.1" "$SKILL_FILE" || true)
HAS_12=$(grep -c "1\.2\|§ 1\.2" "$SKILL_FILE" || true)
HAS_13=$(grep -c "1\.3\|§ 1\.3" "$SKILL_FILE" || true)

[[ $HAS_SP -gt 0 ]] && SP_SCORE=$((SP_SCORE+2)) && SP_NOTES+="has-header "
[[ $HAS_11 -gt 0 ]] && SP_SCORE=$((SP_SCORE+2)) && SP_NOTES+="§1.1 "
[[ $HAS_12 -gt 0 ]] && SP_SCORE=$((SP_SCORE+2)) && SP_NOTES+="§1.2 "
[[ $HAS_13 -gt 0 ]] && SP_SCORE=$((SP_SCORE+2)) && SP_NOTES+="§1.3 "
[[ $SP_SCORE -gt 10 ]] && SP_SCORE=10
dim_score "System Prompt" 20 "$SP_SCORE" "$SP_NOTES"

# ── Dimension 2: Domain Knowledge (20%) ────────────────────────────────────
DK_SCORE=4
DK_NOTES=""
# Check for specific data signals: percentages, years, named frameworks
SPECIFICS=$(grep -cE "[0-9]+%|[0-9]+\.[0-9]+|McKinsey|TOGAF|ISO |RFC |v[0-9]+\.[0-9]" "$SKILL_FILE" || true)
GENERICS=$(grep -ciE "\bprofessional\b|\bindustry.leader\b|\bbest practices\b|\bexpert\b|\bworld.class\b" "$SKILL_FILE" || true)

[[ $SPECIFICS -ge 5 ]] && DK_SCORE=$((DK_SCORE+3)) && DK_NOTES+="specific-data "
[[ $SPECIFICS -ge 2 ]] && [[ $DK_SCORE -lt 7 ]] && DK_SCORE=$((DK_SCORE+1)) && DK_NOTES+="some-data "
[[ $GENERICS -ge 5 ]] && DK_SCORE=$((DK_SCORE-2)) && DK_NOTES+="⚠generic-content "
[[ $DK_SCORE -lt 1 ]] && DK_SCORE=1
[[ $DK_SCORE -gt 10 ]] && DK_SCORE=10
dim_score "Domain Knowledge" 20 "$DK_SCORE" "$DK_NOTES"

# ── Dimension 3: Workflow (20%) ─────────────────────────────────────────────
WF_SCORE=3
WF_NOTES=""
HAS_WORKFLOW=$(grep -ci "workflow\|§ [0-9]\+.*workflow\|## Workflow\|## Phase\|Step [0-9]" "$SKILL_FILE" || true)
HAS_DONE=$(grep -ci "done.criteri\|done:" "$SKILL_FILE" || true)
HAS_FAIL=$(grep -ci "fail.criteri\|fail:" "$SKILL_FILE" || true)
HAS_PHASES=$(grep -cE "Phase [1-9]|Step [1-9]" "$SKILL_FILE" || true)

[[ $HAS_WORKFLOW -gt 0 ]] && WF_SCORE=$((WF_SCORE+2)) && WF_NOTES+="has-workflow "
[[ $HAS_PHASES -ge 3 ]] && WF_SCORE=$((WF_SCORE+2)) && WF_NOTES+="${HAS_PHASES}-phases "
[[ $HAS_DONE -gt 0 ]] && WF_SCORE=$((WF_SCORE+1)) && WF_NOTES+="done-criteria "
[[ $HAS_FAIL -gt 0 ]] && WF_SCORE=$((WF_SCORE+1)) && WF_NOTES+="fail-criteria "
[[ $WF_SCORE -gt 10 ]] && WF_SCORE=10
dim_score "Workflow" 20 "$WF_SCORE" "$WF_NOTES"

# ── Dimension 4: Error Handling (15%) ──────────────────────────────────────
EH_SCORE=3
EH_NOTES=""
HAS_EH=$(grep -ci "error.handling\|edge case\|anti.pattern\|risk\|failure\|recovery" "$SKILL_FILE" || true)
HAS_ANTIPATTERNS=$(grep -ci "anti-pattern\|Anti-Pattern" "$SKILL_FILE" || true)

[[ $HAS_EH -ge 3 ]] && EH_SCORE=$((EH_SCORE+3)) && EH_NOTES+="error-scenarios "
[[ $HAS_ANTIPATTERNS -gt 0 ]] && EH_SCORE=$((EH_SCORE+2)) && EH_NOTES+="anti-patterns "
[[ $HAS_EH -ge 1 ]] && [[ $EH_SCORE -lt 6 ]] && EH_SCORE=$((EH_SCORE+1)) && EH_NOTES+="some-coverage "
[[ $EH_SCORE -gt 10 ]] && EH_SCORE=10
dim_score "Error Handling" 15 "$EH_SCORE" "$EH_NOTES"

# ── Dimension 5: Examples (15%) ─────────────────────────────────────────────
EX_SCORE=2
EX_NOTES=""
EXAMPLE_SECTIONS=$(grep -cE "^## .*[Ee]xample|^### .*[Ee]xample|^\| [0-9]+ \|.*[Ee]xample" "$SKILL_FILE" || true)
EXAMPLE_MENTIONS=$(grep -ci "example\|scenario\|use case" "$SKILL_FILE" || true)

[[ $EXAMPLE_SECTIONS -ge 5 ]] && EX_SCORE=9 && EX_NOTES+="5+-sections "
[[ $EXAMPLE_SECTIONS -ge 3 ]] && [[ $EX_SCORE -lt 9 ]] && EX_SCORE=7 && EX_NOTES+="3-4-sections "
[[ $EXAMPLE_SECTIONS -ge 1 ]] && [[ $EX_SCORE -lt 7 ]] && EX_SCORE=5 && EX_NOTES+="1-2-sections "
[[ $EXAMPLE_MENTIONS -ge 3 ]] && [[ $EX_SCORE -lt 5 ]] && EX_SCORE=4 && EX_NOTES+="mentions-only "
[[ $EXAMPLE_SECTIONS -eq 0 && $EXAMPLE_MENTIONS -eq 0 ]] && EX_NOTES+="⚠no-examples "
dim_score "Examples" 15 "$EX_SCORE" "$EX_NOTES"

# ── Dimension 6: Metadata (10%) ─────────────────────────────────────────────
MD_SCORE=4
MD_NOTES=""
HAS_NAME=$(grep -c "^name:" "$SKILL_FILE" || true)
HAS_DESC=$(grep -c "^description:" "$SKILL_FILE" || true)
HAS_LICENSE=$(grep -c "^license:" "$SKILL_FILE" || true)
HAS_META=$(grep -c "^metadata:" "$SKILL_FILE" || true)

[[ $HAS_NAME -gt 0 ]] && MD_SCORE=$((MD_SCORE+2)) && MD_NOTES+="name "
[[ $HAS_DESC -gt 0 ]] && MD_SCORE=$((MD_SCORE+2)) && MD_NOTES+="description "
[[ $HAS_LICENSE -gt 0 ]] && MD_SCORE=$((MD_SCORE+1)) && MD_NOTES+="license "
[[ $HAS_META -gt 0 ]] && MD_SCORE=$((MD_SCORE+1)) && MD_NOTES+="metadata "
[[ $MD_SCORE -gt 10 ]] && MD_SCORE=10
dim_score "Metadata" 10 "$MD_SCORE" "$MD_NOTES"

# ── Overall score ───────────────────────────────────────────────────────────
echo ""
echo "  ─────────────────────────────────────────"
FINAL=$(echo "scale=1; $TOTAL" | bc)
echo "  Text Score (heuristic):  ${FINAL}/10"
echo ""

# Grade
if (( $(echo "$FINAL >= 9.0" | bc -l) )); then
  echo "  Grade: EXEMPLARY ✓  (Text ≥ 9.0)"
elif (( $(echo "$FINAL >= 8.0" | bc -l) )); then
  echo "  Grade: CERTIFIED ✓  (Text ≥ 8.0)"
elif (( $(echo "$FINAL >= 7.0" | bc -l) )); then
  echo "  Grade: GOOD         (Text ≥ 7.0)"
elif (( $(echo "$FINAL >= 6.0" | bc -l) )); then
  echo "  Grade: ACCEPTABLE   (needs improvement)"
else
  echo "  Grade: BELOW STANDARD — restore before shipping"
fi

echo ""
echo "  Note: This is a heuristic check, not a full evaluation."
echo "  Run: ./eval.sh $SKILL_FILE  for dual-track assessment."
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
