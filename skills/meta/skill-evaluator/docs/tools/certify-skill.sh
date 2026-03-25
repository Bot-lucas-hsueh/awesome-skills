#!/bin/bash
# Full certification test for production skills
# Usage: ./certify-skill.sh path/to/SKILL.md

SKILL_FILE="$1"

if [[ ! -f "$SKILL_FILE" ]]; then
  echo "Usage: $0 path/to/SKILL.md"
  echo ""
  echo "This script runs the full certification suite:"
  echo "- Quick evaluation"
  echo "- Standard runtime test"
  echo "- Deep stress test"
  echo "- Adversarial testing"
  echo ""
  echo "Total time: 2-3 hours"
  echo "Use for: Production-critical skills only"
  exit 1
fi

SKILL_NAME=$(basename $(dirname "$SKILL_FILE"))
CERTIFICATION_DATE=$(date +%Y-%m-%d)
CERTIFICATION_ID="CERT-$(date +%s)"

echo "═══════════════════════════════════════════════════════════"
echo "  SKILL CERTIFICATION TEST"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "Skill: $SKILL_NAME"
echo "Date: $CERTIFICATION_DATE"
echo "ID: $CERTIFICATION_ID"
echo ""
echo "⚠️  This is a comprehensive 2-3 hour test"
echo "   Ensure you have uninterrupted time"
echo ""
read -p "Press Enter to begin or Ctrl+C to cancel..."
echo ""

# Create certification directory
CERT_DIR="certifications/$SKILL_NAME-$CERTIFICATION_DATE"
mkdir -p "$CERT_DIR"

echo "Certification artifacts will be saved to: $CERT_DIR"
echo ""

# Phase 1: Quick Evaluation
echo "═══════════════════════════════════════════════════════════"
echo "PHASE 1: QUICK EVALUATION (5 minutes)"
echo "═══════════════════════════════════════════════════════════"
echo ""
./scripts/quick-eval.sh "$SKILL_FILE" | tee "$CERT_DIR/01-quick-eval.txt"
echo ""
read -p "Phase 1 complete. Press Enter to continue..."

# Phase 2: Text Quality Review
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "PHASE 2: TEXT QUALITY REVIEW (15 minutes)"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "Refer to: references/text-evaluation.md"
echo ""
echo "Rate 6 dimensions:"
echo "1. System Prompt Depth: __/10"
echo "2. Domain Knowledge: __/10"
echo "3. Workflow Clarity: __/10"
echo "4. Risk Documentation: __/10"
echo "5. Example Richness: __/10"
echo "6. Metadata Completeness: __/10"
echo ""
echo "Text Score = weighted average"
echo "Record in: $CERT_DIR/02-text-quality.txt"
echo ""
read -p "Complete text review and press Enter..."

# Phase 3: Standard Runtime
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "PHASE 3: STANDARD RUNTIME TEST (20 minutes)"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "Refer to: references/runtime-evaluation.md"
echo ""
echo "Test 6 dimensions:"
echo "1. Role Immersion: __/10"
echo "2. Framework Execution: __/10"
echo "3. Output Actionability: __/10"
echo "4. Knowledge Accuracy: __/10"
echo "5. Long-Conversation Stability: __/10"
echo "6. Resilience: __/10"
echo ""
echo "Runtime Score = weighted average"
echo "Record in: $CERT_DIR/03-runtime-test.txt"
echo ""
read -p "Complete runtime test and press Enter..."

# Phase 4: Deep Testing
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "PHASE 4: DEEP STRESS TEST (40 minutes)"
echo "═══════════════════════════════════════════════════════════"
echo ""
./scripts/deep-test.sh "$SKILL_FILE" quick | tee "$CERT_DIR/04-deep-test.txt"
echo ""
read -p "Phase 4 complete. Press Enter to continue..."

# Phase 5: Adversarial Testing
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "PHASE 5: ADVERSARIAL TESTING (60 minutes)"
echo "═══════════════════════════════════════════════════════════"
echo ""
./scripts/adversarial-test.sh "$SKILL_FILE" | tee "$CERT_DIR/05-adversarial.txt"
echo ""
read -p "Phase 5 complete. Press Enter for final report..."

# Generate Final Report
echo ""
echo "═══════════════════════════════════════════════════════════"
echo "CERTIFICATION REPORT"
echo "═══════════════════════════════════════════════════════════"
echo ""
echo "Certification ID: $CERTIFICATION_ID"
echo "Skill: $SKILL_NAME"
echo "Date: $CERTIFICATION_DATE"
echo ""
echo "SCORES:"
echo "--------"
echo ""
echo "Text Quality:        __/10"
echo "Runtime Quality:     __/10"
echo "Deep Test:           __/10 (bonus)"
echo "Adversarial:         __/10 (bonus)"
echo ""
echo "GAP ANALYSIS:"
echo "-------------"
echo "Text - Runtime Gap: __ points"
echo "Pattern: _____________"
echo ""
echo "CERTIFICATION STATUS:"
echo "---------------------"
echo ""
echo "□ CERTIFIED (9.0+ overall, all dimensions 7.5+)"
echo "□ CONDITIONAL (8.0+ overall, minor improvements needed)"
echo "□ NOT CERTIFIED (<8.0 or any dimension <6.0)"
echo ""
echo "Artifacts saved in: $CERT_DIR/"
echo ""
echo "═══════════════════════════════════════════════════════════"

# Create summary file
cat > "$CERT_DIR/CERTIFICATION-SUMMARY.txt" << EOF
SKILL CERTIFICATION SUMMARY
============================

Skill: $SKILL_NAME
Date: $CERTIFICATION_DATE
ID: $CERTIFICATION_ID

RESULTS:
--------
Text Quality:        __/10
Runtime Quality:     __/10
Deep Test:           __/10
Adversarial:         __/10

FINAL SCORE:         __/10

STATUS:              [ ] CERTIFIED / [ ] CONDITIONAL / [ ] NOT CERTIFIED

REVIEWER:            ________________
SIGNATURE:           ________________
DATE:                ________________

NOTES:
------


RECOMMENDATIONS:
----------------


NEXT REVIEW DATE:    ________________
EOF

echo "Summary template created: $CERT_DIR/CERTIFICATION-SUMMARY.txt"
echo ""
echo "Complete the summary and archive for audit trail."
