#!/bin/bash
# Test skill with sample inputs
# Usage: ./test-skill.sh path/to/SKILL.md

SKILL_FILE="$1"
SKILL_NAME=$(basename $(dirname "$SKILL_FILE"))

echo "═══════════════════════════════════════"
echo "  SKILL TEST: $SKILL_NAME"
echo "═══════════════════════════════════════"
echo ""
echo "This script generates test cases for manual evaluation."
echo ""

# Extract skill type from description
DESC=$(head -30 "$SKILL_FILE" | grep "^description:" | cut -d: -f2-)
echo "Skill Description:"
echo "  $DESC"
echo ""

# Generate test cases based on skill content
echo "═══════════════════════════════════════"
echo "  SUGGESTED TEST CASES"
echo "═══════════════════════════════════════"
echo ""

echo "Test 1: BASIC USE CASE"
echo "----------------------"
echo "Use the skill for its primary purpose."
echo "Expected: Clear, actionable output in character"
echo ""

echo "Test 2: EDGE CASE"
echo "-----------------"
echo "Use with unusual but valid input."
echo "Expected: Handles gracefully or clarifies boundaries"
echo ""

echo "Test 3: MISUSE ATTEMPT"
echo "----------------------"
echo "Ask for something outside skill scope."
echo "Expected: Politely declines or redirects"
echo ""

echo "Test 4: FOLLOW-UP DEPTH"
echo "-----------------------"
echo "Ask 3 follow-up questions on same topic."
echo "Expected: Maintains context and depth"
echo ""

echo "═══════════════════════════════════════"
echo "  EVALUATION CHECKLIST"
echo "═══════════════════════════════════════"
echo ""
echo "Rate each 1-10:"
echo "□ Role Consistency: ___"
echo "□ Domain Accuracy: ___"
echo "□ Actionability: ___"
echo "□ Tone Appropriateness: ___"
echo "□ No Hallucination: ___"
echo ""
echo "Total: ___/50"
echo ""
echo "Would you use this skill again? Y/N"
