#!/usr/bin/env bash
# validate.sh — Validate SKILL.md against agentskills spec
# Usage: ./validate.sh path/to/SKILL.md
# Exit code: 0 = pass, 1 = fail

set -euo pipefail

SKILL_FILE="${1:-}"
ERRORS=0
WARNINGS=0

RED='\033[0;31m'; YELLOW='\033[1;33m'; GREEN='\033[0;32m'; NC='\033[0m'

fail()  { echo -e "${RED}  ✗ $1${NC}"; ERRORS=$((ERRORS+1)); }
warn()  { echo -e "${YELLOW}  ⚠ $1${NC}"; WARNINGS=$((WARNINGS+1)); }
pass()  { echo -e "${GREEN}  ✓ $1${NC}"; }

if [[ -z "$SKILL_FILE" || ! -f "$SKILL_FILE" ]]; then
  echo "Usage: $0 path/to/SKILL.md"
  exit 1
fi

SKILL_DIR=$(dirname "$SKILL_FILE")
DIR_NAME=$(basename "$SKILL_DIR")

echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  SKILL VALIDATION — agentskills spec"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "File: $SKILL_FILE"
echo ""

# ── 1. Frontmatter ─────────────────────────────────────────────────────────
echo "[ Frontmatter ]"

FIRST_LINE=$(head -1 "$SKILL_FILE")
if [[ "$FIRST_LINE" != "---" ]]; then
  fail "File must begin with '---'"
else
  FM_END=$(awk '/^---$/{if(NR>1){print NR; exit}}' "$SKILL_FILE")
  if [[ -z "$FM_END" ]]; then
    fail "Frontmatter closing '---' not found"
  else
    pass "Frontmatter delimiters present (lines 1–${FM_END})"
    FRONTMATTER=$(sed -n "2,$((FM_END-1))p" "$SKILL_FILE")
  fi
fi

# ── 2. Required: name ───────────────────────────────────────────────────────
echo ""
echo "[ name field ]"

NAME=$(echo "$FRONTMATTER" | grep "^name:" | head -1 | sed 's/^name:[[:space:]]*//' | tr -d '"'"'" )

if [[ -z "$NAME" ]]; then
  fail "Required field 'name' is missing"
else
  # Must match directory name
  if [[ "$NAME" != "$DIR_NAME" ]]; then
    fail "name '$NAME' does not match directory name '$DIR_NAME'"
  else
    pass "name matches directory: $NAME"
  fi

  # Lowercase letters, numbers, hyphens only
  if ! echo "$NAME" | grep -qE '^[a-z0-9-]+$'; then
    fail "name contains invalid characters (allowed: a-z, 0-9, -)"
  else
    pass "name characters valid"
  fi

  # No leading/trailing hyphens
  if echo "$NAME" | grep -qE '^-|-$'; then
    fail "name must not start or end with a hyphen"
  else
    pass "name has no leading/trailing hyphens"
  fi

  # No consecutive hyphens
  if echo "$NAME" | grep -q '\-\-'; then
    fail "name must not contain consecutive hyphens (--)"
  else
    pass "name has no consecutive hyphens"
  fi

  # Length check
  NAME_LEN=${#NAME}
  if [[ $NAME_LEN -gt 64 ]]; then
    fail "name is $NAME_LEN chars (max 64)"
  else
    pass "name length: $NAME_LEN/64"
  fi
fi

# ── 3. Required: description ────────────────────────────────────────────────
echo ""
echo "[ description field ]"

if ! echo "$FRONTMATTER" | grep -q "^description:"; then
  fail "Required field 'description' is missing"
else
  # Extract multi-line description value
  DESC=$(awk '/^description:/{found=1; sub(/^description:[[:space:]]*/,""); print; next}
              found && /^  /{print; next}
              found{exit}' "$SKILL_FILE" | tr -d "'" | sed 's/^>//' | xargs)
  DESC_LEN=$(echo -n "$DESC" | wc -c)

  if [[ $DESC_LEN -eq 0 ]]; then
    fail "description is empty"
  elif [[ $DESC_LEN -gt 1024 ]]; then
    fail "description is $DESC_LEN chars (max 1024)"
  elif [[ $DESC_LEN -lt 50 ]]; then
    warn "description is very short ($DESC_LEN chars) — consider expanding"
  else
    pass "description length: $DESC_LEN/1024"
  fi
fi

# ── 4. Optional fields — no unknown top-level keys ─────────────────────────
echo ""
echo "[ Optional fields ]"

ALLOWED_KEYS="name|description|license|compatibility|metadata|allowed-tools"
BAD_KEYS=$(echo "$FRONTMATTER" | grep -E "^[a-z]" | grep -vE "^($ALLOWED_KEYS):" | cut -d: -f1)

if [[ -n "$BAD_KEYS" ]]; then
  while IFS= read -r key; do
    warn "Non-spec top-level field: '$key' (move to metadata:)"
  done <<< "$BAD_KEYS"
else
  pass "No non-spec top-level fields"
fi

# ── 5. File size ────────────────────────────────────────────────────────────
echo ""
echo "[ Progressive disclosure ]"

LINES=$(wc -l < "$SKILL_FILE")
if [[ $LINES -gt 500 ]]; then
  fail "SKILL.md is $LINES lines (hard limit: 500; recommended: ≤ 300)"
elif [[ $LINES -gt 300 ]]; then
  warn "SKILL.md is $LINES lines (recommended ≤ 300; move details to references/)"
else
  pass "SKILL.md line count: $LINES ✓"
fi

if [[ -d "$SKILL_DIR/references" ]]; then
  REF_COUNT=$(find "$SKILL_DIR/references" -name "*.md" | wc -l)
  pass "references/ directory present ($REF_COUNT .md files)"
else
  warn "No references/ directory — consider progressive disclosure for larger skills"
fi

# ── 6. System Prompt check ─────────────────────────────────────────────────
echo ""
echo "[ Content structure ]"

if grep -qi "§ 1\|## § 1\|system prompt\|# System Prompt" "$SKILL_FILE"; then
  pass "System Prompt section found"
else
  warn "No System Prompt (§1) found — worth 20% of quality score"
fi

HAS_11=$(grep -c "§ 1\.1\|1\.1 " "$SKILL_FILE" || true)
HAS_12=$(grep -c "§ 1\.2\|1\.2 " "$SKILL_FILE" || true)
HAS_13=$(grep -c "§ 1\.3\|1\.3 " "$SKILL_FILE" || true)
[[ $HAS_11 -gt 0 ]] && pass "§1.1 Identity found" || warn "§1.1 Identity missing"
[[ $HAS_12 -gt 0 ]] && pass "§1.2 Decision Framework found" || warn "§1.2 Decision Framework missing"
[[ $HAS_13 -gt 0 ]] && pass "§1.3 Thinking Patterns found" || warn "§1.3 Thinking Patterns missing"

# ── Summary ─────────────────────────────────────────────────────────────────
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo "  RESULT"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"

if [[ $ERRORS -eq 0 && $WARNINGS -eq 0 ]]; then
  echo -e "${GREEN}  PASS — No issues found${NC}"
  exit 0
elif [[ $ERRORS -eq 0 ]]; then
  echo -e "${YELLOW}  PASS (with warnings) — $WARNINGS warning(s)${NC}"
  exit 0
else
  echo -e "${RED}  FAIL — $ERRORS error(s), $WARNINGS warning(s)${NC}"
  exit 1
fi
