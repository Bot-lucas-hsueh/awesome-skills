#!/bin/bash
# Skill Auto-Scorer
# Automatically calculate metrics and scores for skills
#
# Usage: ./skill-scorer.sh path/to/SKILL.md

SKILL_FILE="$1"

if [ -z "$SKILL_FILE" ]; then
    echo "Usage: $0 path/to/SKILL.md"
    exit 1
fi

if [ ! -f "$SKILL_FILE" ]; then
    echo "Error: File not found: $SKILL_FILE"
    exit 1
fi

echo "================================"
echo "Skill Auto-Scorer"
echo "================================"
echo ""
echo "File: $SKILL_FILE"
echo ""

# === STRUCTURAL METRICS ===
echo "--- Structural Metrics ---"

# Total lines
TOTAL_LINES=$(wc -l < "$SKILL_FILE")
echo "Total Lines: $TOTAL_LINES"

# Section count
SECTION_COUNT=$(grep -c "^## [0-9]\+\." "$SKILL_FILE")
echo "H2 Sections: $SECTION_COUNT/16"

# Check section numbering
MISSING_SECTIONS=0
for i in {1..16}; do
    if ! grep -q "^## $i\." "$SKILL_FILE"; then
        MISSING_SECTIONS=$((MISSING_SECTIONS + 1))
        echo "  ⚠ Missing: Section $i"
    fi
done

if [ $MISSING_SECTIONS -eq 0 ]; then
    echo "  ✅ All 16 sections present"
fi

# === CONTENT DENSITY METRICS ===
echo ""
echo "--- Content Density (SDI) ---"

# Count tables (lines starting with |)
TABLE_LINES=$(grep -c "^|" "$SKILL_FILE" 2>/dev/null || echo "0")
TABLE_COUNT=$((TABLE_LINES / 3))  # Approximate: 3 lines per table row
echo "Tables: ~$TABLE_COUNT"

# Count code blocks
CODE_BLOCKS=$(grep -c "^\`\`\`" "$SKILL_FILE" 2>/dev/null || echo "0")
CODE_BLOCK_COUNT=$((CODE_BLOCKS / 2))  # Opening + closing
echo "Code Blocks: $CODE_BLOCK_COUNT"

# Count lists
LIST_ITEMS=$(grep -c "^- " "$SKILL_FILE" 2>/dev/null || echo "0")
echo "List Items: $LIST_ITEMS"

# Calculate SDI
if [ $TOTAL_LINES -gt 0 ]; then
    SDI=$(echo "scale=2; ($TABLE_COUNT * 3 + $CODE_BLOCK_COUNT * 2 + $LIST_ITEMS * 1) / ($TOTAL_LINES / 100)" | bc 2>/dev/null || echo "N/A")
    echo ""
    echo "Structure Density Index (SDI): $SDI"
    
    if [ "$SDI" != "N/A" ]; then
        if (( $(echo "$SDI >= 3.0" | bc -l) )); then
            echo "  ✅ Exceptional (> 3.0)"
        elif (( $(echo "$SDI >= 2.0" | bc -l) )); then
            echo "  ✅ Excellent (2.0-3.0)"
        elif (( $(echo "$SDI >= 1.0" | bc -l) )); then
            echo "  ⚠ Good (1.0-2.0)"
        else
            echo "  ❌ Needs Work (< 1.0)"
        fi
    fi
fi

# === YAML METADATA ===
echo ""
echo "--- YAML Metadata ---"

# Check for required fields
REQUIRED_FIELDS=("name:" "display_name:" "author:" "version:" "category:" "tags:" "platforms:" "description:")
MISSING_FIELDS=0

for field in "${REQUIRED_FIELDS[@]}"; do
    if ! grep -q "^$field" "$SKILL_FILE"; then
        echo "  ⚠ Missing field: $field"
        MISSING_FIELDS=$((MISSING_FIELDS + 1))
    fi
done

if [ $MISSING_FIELDS -eq 0 ]; then
    echo "  ✅ All 9 metadata fields present"
fi

# Description length
DESC_LENGTH=$(sed -n '/^description:/,/^---$/p' "$SKILL_FILE" | grep -v "^---$" | wc -c)
if [ $DESC_LENGTH -gt 263 ]; then
    echo "  ⚠ Description too long: $DESC_LENGTH chars (max 263)"
else
    echo "  ✅ Description length: $DESC_LENGTH chars"
fi

# === QUALITY CHECKS ===
echo ""
echo "--- Quality Checks ---"

# Risk disclaimer count
RISKS=$(grep -c "^| \*\*" "$SKILL_FILE" 2>/dev/null || echo "0")
if [ $RISKS -ge 4 ]; then
    echo "  ✅ Risk entries: $RISKS (≥4)"
else
    echo "  ⚠ Risk entries: $RISKS (< 4)"
fi

# Scenario examples
SCENARIOS=$(grep -c "^### [0-9]\+\.[0-9]" "$SKILL_FILE" 2>/dev/null || echo "0")
if [ $SCENARIOS -ge 2 ]; then
    echo "  ✅ Scenario examples: $SCENARIOS (≥2)"
else
    echo "  ⚠ Scenario examples: $SCENARIOS (< 2)"
fi

# Gotchas/Anti-patterns
GOTCHAS=$(grep -c "^| [0-9]\+ | \*\*" "$SKILL_FILE" 2>/dev/null || echo "0")
if [ $GOTCHAS -ge 3 ]; then
    echo "  ✅ Gotchas: $GOTCHAS (≥3)"
else
    echo "  ⚠ Gotchas: $GOTCHAS (< 3)"
fi

# === ENTERPRISE SKILL CHECKS ===
echo ""
echo "--- Enterprise Practice Checks ---"

# Check for dual-perspective
if grep -q "For Job Seekers\|For Practitioners\|求职者\|在职者" "$SKILL_FILE"; then
    echo "  ✅ Dual-perspective detected"
else
    echo "  ℹ No dual-perspective (OK for non-enterprise skills)"
fi

# Check for three-layer architecture
if grep -q "Culture Layer\|Methodology Layer\|Tool Layer" "$SKILL_FILE"; then
    echo "  ✅ Three-layer architecture detected"
else
    echo "  ℹ No three-layer architecture (OK for non-enterprise skills)"
fi

# === CONSISTENCY CHECKS ===
echo ""
echo "--- Consistency Checks ---"

# Check for section symbol consistency (should use ## 1. not ## § 1 —)
if grep -q "^## §" "$SKILL_FILE"; then
    echo "  ❌ Found § symbol in headers (use ## 1. format)"
else
    echo "  ✅ Section symbols consistent"
fi

# Check for — vs - in headers
if grep "^## [0-9]" "$SKILL_FILE" | grep -q " — "; then
    echo "  ❌ Found em-dash (—) in H2 headers (use ## 1. Name format)"
else
    echo "  ✅ No em-dash in H2 headers"
fi

# === TOKEN BUDGET ===
echo ""
echo "--- Token Budget ---"

if [ $TOTAL_LINES -le 500 ]; then
    echo "  ✅ Body length: $TOTAL_LINES lines (≤500)"
else
    echo "  ⚠ Body length: $TOTAL_LINES lines (>500, consider references/)"
fi

# === SUMMARY ===
echo ""
echo "================================"
echo "Summary"
echo "================================"

echo "Structure: $SECTION_COUNT/16 sections"
echo "Density: SDI = $SDI"
echo "Length: $TOTAL_LINES lines"

# Estimate score based on metrics
ESTIMATED_SCORE="Unknown"
if [ "$SDI" != "N/A" ]; then
    if (( $(echo "$SDI >= 2.5" | bc -l) )) && [ $SECTION_COUNT -eq 16 ] && [ $RISKS -ge 4 ] && [ $SCENARIOS -ge 2 ]; then
        ESTIMATED_SCORE="8.5-9.5 (Expert/Exemplary)"
    elif (( $(echo "$SDI >= 2.0" | bc -l) )) && [ $SECTION_COUNT -ge 14 ] && [ $RISKS -ge 3 ]; then
        ESTIMATED_SCORE="7.0-8.4 (Expert)"
    elif [ $SECTION_COUNT -ge 12 ]; then
        ESTIMATED_SCORE="5.0-6.9 (Community)"
    else
        ESTIMATED_SCORE="<5.0 (Basic)"
    fi
fi

echo "Estimated Quality Tier: $ESTIMATED_SCORE"
echo ""
echo "For detailed scoring, see: references/standards.md §7.1"
