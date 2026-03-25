#!/bin/bash
# Quick text quality check
# Usage: ./quick-text-check.sh path/to/SKILL.md

SKILL_FILE="$1"

if [[ ! -f "$SKILL_FILE" ]]; then
  echo "Usage: $0 path/to/SKILL.md"
  exit 1
fi

echo "Quick Text Quality Check"
echo "========================"
echo ""

SCORE=0
MAX=10

# Check 1: YAML frontmatter (2 points)
if head -20 "$SKILL_FILE" | grep -q "^name:"; then
  echo "✓ Has name field"
  SCORE=$((SCORE + 1))
fi

if head -20 "$SKILL_FILE" | grep -q "^description:"; then
  echo "✓ Has description field"
  SCORE=$((SCORE + 1))
fi

# Check 2: System Prompt (2 points)
if grep -qi "system prompt" "$SKILL_FILE"; then
  SP_LINES=$(grep -A 20 "system prompt" "$SKILL_FILE" 2>/dev/null | wc -l)
  if [[ $SP_LINES -gt 5 ]]; then
    echo "✓ System Prompt substantive ($SP_LINES lines)"
    SCORE=$((SCORE + 2))
  else
    echo "⚠ System Prompt minimal ($SP_LINES lines)"
    SCORE=$((SCORE + 1))
  fi
else
  echo "✗ No System Prompt found"
fi

# Check 3: Examples (2 points)
EXAMPLES=$(grep -c "^###\|^##.*[Ee]xample" "$SKILL_FILE" 2>/dev/null || echo "0")
if [[ $EXAMPLES -ge 3 ]]; then
  echo "✓ Multiple examples ($EXAMPLES)"
  SCORE=$((SCORE + 2))
elif [[ $EXAMPLES -ge 1 ]]; then
  echo "⚠ Few examples ($EXAMPLES)"
  SCORE=$((SCORE + 1))
else
  echo "✗ No examples found"
fi

# Check 4: Risk/Anti-patterns (2 points)
if grep -qi "risk\|anti-pattern\|pitfall\|limitation" "$SKILL_FILE"; then
  echo "✓ Risk awareness present"
  SCORE=$((SCORE + 2))
else
  echo "✗ No risk documentation"
fi

# Check 5: File size (2 points)
LINES=$(wc -l < "$SKILL_FILE")
if [[ $LINES -lt 800 && $LINES -gt 50 ]]; then
  echo "✓ Appropriate size ($LINES lines)"
  SCORE=$((SCORE + 2))
else
  echo "⚠ Unusual size ($LINES lines)"
  SCORE=$((SCORE + 1))
fi

echo ""
echo "Score: $SCORE/$MAX"
echo ""

if [[ $SCORE -ge 8 ]]; then
  echo "✅ Good text quality"
elif [[ $SCORE -ge 6 ]]; then
  echo "⚠️  Acceptable with improvements"
else
  echo "❌ Needs significant work"
fi
