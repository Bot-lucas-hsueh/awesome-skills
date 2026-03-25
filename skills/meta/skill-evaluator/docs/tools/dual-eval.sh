#!/bin/bash
# Dual-track skill evaluation
# Usage: ./dual-eval.sh path/to/SKILL.md

SKILL_FILE="$1"

if [[ ! -f "$SKILL_FILE" ]]; then
  echo "Usage: $0 path/to/SKILL.md"
  exit 1
fi

SKILL_NAME=$(basename $(dirname "$SKILL_FILE"))

echo "═══════════════════════════════════════════════════"
echo "  DUAL-TRACK SKILL EVALUATION"
echo "═══════════════════════════════════════════════════"
echo ""
echo "Skill: $SKILL_NAME"
echo "File: $SKILL_FILE"
echo ""

# Quick file check
echo "--- PHASE 1: FILE CHECK ---"
LINES=$(wc -l < "$SKILL_FILE")
if [[ $LINES -lt 150 ]]; then
  TIER="Lite"
elif [[ $LINES -lt 400 ]]; then
  TIER="Standard"
else
  TIER="Enterprise"
fi
echo "Lines: $LINES → $TIER tier"

# Check YAML
if head -20 "$SKILL_FILE" | grep -q "^name:"; then
  echo "✓ YAML frontmatter present"
fi

# Check System Prompt
if grep -qi "system prompt" "$SKILL_FILE"; then
  echo "✓ System Prompt present"
fi

echo ""
echo "--- PHASE 2: TEXT QUALITY ---"
echo "Load: references/text-evaluation.md"
echo ""
echo "Rate 6 dimensions:"
echo "1. System Prompt Depth: __/10"
echo "2. Domain Knowledge: __/10"
echo "3. Workflow Clarity: __/10"
echo "4. Risk Documentation: __/10"
echo "5. Example Richness: __/10"
echo "6. Metadata: __/10"
echo ""
echo "TEXT SCORE: __/10"

echo ""
echo "--- PHASE 3: RUNTIME QUALITY ---"
echo "Load: references/runtime-evaluation.md"
echo ""
echo "Test 6 dimensions:"
echo "1. Role Immersion: __/10"
echo "2. Framework Execution: __/10"
echo "3. Actionability: __/10"
echo "4. Knowledge Accuracy: __/10"
echo "5. Stability: __/10"
echo "6. Resilience: __/10"
echo ""
echo "RUNTIME SCORE: __/10"

echo ""
echo "--- PHASE 4: GAP ANALYSIS ---"
echo "Load: references/gap-analysis.md"
echo ""
echo "Text Score: __/10"
echo "Runtime Score: __/10"
echo "Gap: __ points"
echo "Pattern: _____________"
echo ""

echo "═══════════════════════════════════════════════════"
echo "  FINAL SCORE"
echo "═══════════════════════════════════════════════════"
echo ""
echo "Overall: (Text + Runtime) / 2 = __/10"
echo ""
echo "Rating:"
echo "  9.0-10: Exemplary ⭐⭐"
echo "  7.5-8.9: Expert ⭐"
echo "  6.0-7.4: Community"
echo "  <6.0: Needs Work"
echo ""
echo "Recommendation: _____________"
echo ""
