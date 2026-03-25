#!/bin/bash
# Quick skill evaluation script
# Usage: ./quick-eval.sh path/to/SKILL.md

SKILL_FILE="$1"

if [[ ! -f "$SKILL_FILE" ]]; then
  echo "Usage: $0 path/to/SKILL.md"
  exit 1
fi

echo "═══════════════════════════════════════"
echo "  QUICK SKILL EVALUATION"
echo "═══════════════════════════════════════"
echo ""

# Check 1: YAML Frontmatter
echo "□ YAML Frontmatter"
if head -20 "$SKILL_FILE" | grep -q "^---"; then
  echo "  ✓ Present"
else
  echo "  ✗ Missing"
fi

# Check 2: Name field
if head -20 "$SKILL_FILE" | grep -q "^name:"; then
  NAME=$(head -20 "$SKILL_FILE" | grep "^name:" | cut -d: -f2 | tr -d ' ')
  echo "  ✓ Name: $NAME"
else
  echo "  ✗ Missing name"
fi

# Check 3: Description field
if head -20 "$SKILL_FILE" | grep -q "^description:"; then
  DESC_LEN=$(head -20 "$SKILL_FILE" | grep "^description:" | wc -c)
  if [[ $DESC_LEN -lt 300 ]]; then
    echo "  ✓ Description: $DESC_LEN chars (good)"
  else
    echo "  ⚠ Description: $DESC_LEN chars (consider shortening)"
  fi
else
  echo "  ✗ Missing description"
fi

# Check 4: System Prompt
echo ""
echo "□ System Prompt"
if grep -q "## System Prompt\|# System Prompt" "$SKILL_FILE"; then
  SP_LINES=$(grep -A 50 "System Prompt" "$SKILL_FILE" | head -20 | wc -l)
  echo "  ✓ Present (~$SP_LINES lines)"
else
  echo "  ✗ Missing"
fi

# Check 5: Examples
echo ""
echo "□ Examples"
EXAMPLE_COUNT=$(grep -c "## Example\|### Example" "$SKILL_FILE" || echo "0")
if [[ $EXAMPLE_COUNT -gt 0 ]]; then
  echo "  ✓ $EXAMPLE_COUNT example sections"
else
  echo "  ✗ No examples found"
fi

# Check 6: File size
echo ""
echo "□ File Size"
LINES=$(wc -l < "$SKILL_FILE")
if [[ $LINES -lt 150 ]]; then
  echo "  ✓ Lite tier: $LINES lines"
elif [[ $LINES -lt 400 ]]; then
  echo "  ✓ Standard tier: $LINES lines"
elif [[ $LINES -lt 800 ]]; then
  echo "  ✓ Enterprise tier: $LINES lines"
else
  echo "  ⚠ Large file: $LINES lines (consider splitting)"
fi

# Estimate score
echo ""
echo "═══════════════════════════════════════"
echo "  ESTIMATED TIER"
echo "═══════════════════════════════════════"

if [[ $LINES -lt 150 && $EXAMPLE_COUNT -ge 2 ]]; then
  echo "  → Lite (5.0-6.5)"
elif [[ $LINES -lt 400 && $EXAMPLE_COUNT -ge 3 ]]; then
  echo "  → Standard (6.5-8.0)"
elif [[ $LINES -lt 800 ]]; then
  echo "  → Enterprise (8.0-9.5)"
else
  echo "  → Needs Review"
fi

echo ""
echo "For detailed evaluation, load:"
echo "  references/quality-rubric.md"
