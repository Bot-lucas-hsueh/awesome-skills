#!/bin/bash
#
# Security audit for Gerrit permission configurations
# Usage: ./audit-permissions.sh [--repo <repo>] | [--manifest <file>] | [--all] [--strict]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_NAME=""
MANIFEST_FILE=""
SHOW_ALL=false
STRICT_MODE=false
REPORT_FILE=""
GERRIT_HOST=${GERRIT_HOST:-"localhost"}
GERRIT_WEB_PORT=${GERRIT_WEB_PORT:-"8080"}
GERRIT_USER=${GERRIT_USER:-"admin"}

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
BOLD='\033[1m'
NC='\033[0m'

# Counters
CRITICAL=0
WARNING=0
INFO=0
PASSED=0

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; ((WARNING++)); }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; ((CRITICAL++)); }
log_debug() { echo -e "${BLUE}[DEBUG]${NC} $1"; }
log_pass() { echo -e "${GREEN}[PASS]${NC} $1"; ((PASSED++)); }
log_audit() { echo -e "${CYAN}[AUDIT]${NC} $1"; ((INFO++)); }

show_help() {
    cat << EOF
Security Audit for Gerrit Permissions

Usage: $0 [options]

Options:
  --repo <name>           Audit specific repository
  --manifest <file>       Audit all repos in manifest
  --all                   Audit all repositories
  --strict                Strict mode (treat warnings as errors)
  --report <file>         Generate audit report file
  --help                  Show this help

Audit Checks:
  - Master branch protection
  - Direct push restrictions
  - Code review requirements
  - Group permission overlap
  - Anonymous access
  - Overly permissive settings

Examples:
  # Audit all repos
  $0 --all

  # Strict audit with report
  $0 --all --strict --report audit-report.json

EOF
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --repo)
            REPO_NAME="$2"
            shift 2
            ;;
        --manifest)
            MANIFEST_FILE="$2"
            shift 2
            ;;
        --all)
            SHOW_ALL=true
            shift
            ;;
        --strict)
            STRICT_MODE=true
            shift
            ;;
        --report)
            REPORT_FILE="$2"
            shift 2
            ;;
        --help)
            show_help
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Get permissions
get_permissions() {
    local repo="$1"
    curl -s -X GET \
        "http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a/projects/$(echo -n "$repo" | jq -sRr @uri)/access/" \
        --user "${GERRIT_USER}" 2>&1 | sed 's/^[)]}]//'
}

# Get all projects
get_all_projects() {
    curl -s -X GET \
        "http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a/projects/?type=CODE" \
        --user "${GERRIT_USER}" 2>&1 | sed 's/^[)]}]//' | jq -r 'keys[]' 2>/dev/null || echo ""
}

# Get projects from manifest
get_manifest_projects() {
    local manifest="$1"
    grep -o 'name="[^"]*"' "$manifest" | sed 's/name="//g' | sed 's/"//g' | sort -u
}

# Audit checks
audit_repo() {
    local repo="$1"
    local perms="$2"
    local findings="[]"
    
    echo ""
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "  Repository: ${BOLD}$repo${NC}"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo ""
    
    # Check 1: Master branch protection
    log_audit "Checking master/main branch protection..."
    
    local master_perms=$(echo "$perms" | jq '.["refs/heads/master"] // .["refs/heads/main"] // empty')
    
    if [[ -z "$master_perms" ]] || [[ "$master_perms" == "null" ]]; then
        log_warn "  No master/main branch permissions defined"
        findings=$(echo "$findings" | jq --arg repo "$repo" --arg check "master_protection" \
            '. + [{"repo": $repo, "level": "warning", "check": $check, "message": "No master/main branch permissions defined"}]')
    else
        # Check if submit is restricted
        local submit_groups=$(echo "$master_perms" | jq '.submit // empty')
        if [[ -z "$submit_groups" ]] || [[ "$submit_groups" == "null" ]]; then
            log_error "  CRITICAL: master/main branch has no submit restrictions!"
            findings=$(echo "$findings" | jq --arg repo "$repo" --arg check "master_submit" \
                '. + [{"repo": $repo, "level": "critical", "check": $check, "message": "master/main branch has no submit restrictions"}]')
        else
            log_pass "  master/main branch has submit restrictions"
        fi
        
        # Check for code review requirements
        local has_code_review=$(echo "$master_perms" | jq 'has("label-Code-Review")')
        if [[ "$has_code_review" != "true" ]]; then
            log_warn "  master/main branch has no code review requirements"
            findings=$(echo "$findings" | jq --arg repo "$repo" --arg check "master_code_review" \
                '. + [{"repo": $repo, "level": "warning", "check": $check, "message": "master/main branch has no code review requirements"}]')
        else
            log_pass "  master/main branch requires code review"
        fi
    fi
    
    # Check 2: Anonymous access
    log_audit "Checking anonymous access..."
    
    local has_anonymous=$(echo "$perms" | jq '.. | strings | select(. == "Anonymous Users")')
    if [[ -n "$has_anonymous" ]]; then
        log_warn "  Anonymous access is granted"
        findings=$(echo "$findings" | jq --arg repo "$repo" --arg check "anonymous_access" \
            '. + [{"repo": $repo, "level": "info", "check": $check, "message": "Anonymous access is granted"}]')
    else
        log_pass "  No anonymous access"
    fi
    
    # Check 3: Overly permissive groups
    log_audit "Checking for overly permissive groups..."
    
    local all_groups=$(echo "$perms" | jq -r '[.. | strings | select(contains(" "))] | unique | .[]')
    
    if echo "$all_groups" | grep -qi "admin"; then
        log_warn "  Admin groups found in permissions"
        findings=$(echo "$findings" | jq --arg repo "$repo" --arg check "admin_groups" \
            '. + [{"repo": $repo, "level": "warning", "check": $check, "message": "Admin groups found in permissions"}]')
    fi
    
    # Check 4: Feature branch protection
    log_audit "Checking feature branch configuration..."
    
    local has_feature_branches=$(echo "$perms" | jq 'keys[] | select(contains("feature"))')
    if [[ -n "$has_feature_branches" ]]; then
        log_pass "  Feature branches configured"
    fi
    
    # Check 5: Block force push
    log_audit "Checking force push protection..."
    
    # Note: Gerrit handles this differently, check for push permissions
    local push_force=$(echo "$perms" | jq '.. | objects | select(has("push")) | .push')
    if [[ -n "$push_force" ]]; then
        log_info "  Push permissions configured (verify force push is blocked in UI)"
    fi
    
    # Check 6: Separation of duties
    log_audit "Checking separation of duties..."
    
    local submit_groups=$(echo "$perms" | jq '[.. | .submit? // empty | if type == "array" then .[] else . end] | unique')
    local review_groups=$(echo "$perms" | jq '[.. | .["label-Code-Review"]? // empty | if type == "array" then .[] else . end] | unique')
    
    if [[ "$submit_groups" == "$review_groups" ]]; then
        log_warn "  Same groups can submit and review - consider separation"
        findings=$(echo "$findings" | jq --arg repo "$repo" --arg check "separation_of_duties" \
            '. + [{"repo": $repo, "level": "info", "check": $check, "message": "Same groups can submit and review"}]')
    else
        log_pass "  Separation of duties maintained"
    fi
    
    echo ""
    echo "$findings"
}

# Generate audit report
generate_report() {
    local all_findings="$1"
    
    cat << EOF
{
  "audit_date": "$(date -u +"%Y-%m-%dT%H:%M:%SZ")",
  "gerrit_host": "${GERRIT_HOST}:${GERRIT_WEB_PORT}",
  "summary": {
    "critical": $CRITICAL,
    "warnings": $WARNING,
    "info": $INFO,
    "passed": $PASSED
  },
  "score": $(calculate_score),
  "findings": $all_findings
}
EOF
}

# Calculate security score
calculate_score() {
    local total=$((CRITICAL + WARNING + INFO + PASSED))
    if [[ $total -eq 0 ]]; then
        echo "100"
        return
    fi
    
    # Critical = -10, Warning = -5, Info = -1, Pass = +2
    local score=$((100 + PASSED * 2 - CRITICAL * 10 - WARNING * 5 - INFO))
    if [[ $score -lt 0 ]]; then
        score=0
    fi
    echo "$score"
}

# Display summary
display_summary() {
    local score=$(calculate_score)
    
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════════╗"
    echo "║                    AUDIT SUMMARY                                  ║"
    echo "╚═══════════════════════════════════════════════════════════════════╝"
    echo ""
    printf "  ${BOLD}%-20s${NC} %d\n" "Critical Issues:" "$CRITICAL"
    printf "  ${BOLD}%-20s${NC} %d\n" "Warnings:" "$WARNING"
    printf "  ${BOLD}%-20s${NC} %d\n" "Informational:" "$INFO"
    printf "  ${BOLD}%-20s${NC} %d\n" "Passed Checks:" "$PASSED"
    echo ""
    
    # Display score with color
    if [[ $score -ge 80 ]]; then
        echo -e "  ${BOLD}Security Score:${NC} ${GREEN}$score/100${NC} ✅ GOOD"
    elif [[ $score -ge 60 ]]; then
        echo -e "  ${BOLD}Security Score:${NC} ${YELLOW}$score/100${NC} ⚠️  MODERATE"
    else
        echo -e "  ${BOLD}Security Score:${NC} ${RED}$score/100${NC} ❌ POOR"
    fi
    echo ""
    
    if [[ $CRITICAL -gt 0 ]]; then
        echo -e "  ${RED}ACTION REQUIRED:${NC} Critical security issues found!"
        echo "  Run with --strict to enforce compliance."
    elif [[ $WARNING -gt 0 ]]; then
        echo -e "  ${YELLOW}RECOMMENDATION:${NC} Address warnings to improve security posture."
    else
        echo -e "  ${GREEN}STATUS:${NC} All security checks passed!"
    fi
    echo ""
}

# Main execution
main() {
    local repos=""
    local all_findings="[]"
    
    # Determine repos
    if [[ -n "$REPO_NAME" ]]; then
        repos="$REPO_NAME"
    elif [[ -n "$MANIFEST_FILE" ]]; then
        repos=$(get_manifest_projects "$MANIFEST_FILE")
    elif $SHOW_ALL; then
        repos=$(get_all_projects)
    else
        log_error "Must specify --repo, --manifest, or --all"
        exit 1
    fi
    
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════════╗"
    echo "║           GERRIT PERMISSION SECURITY AUDIT                        ║"
    echo "╚═══════════════════════════════════════════════════════════════════╝"
    echo ""
    echo "  Gerrit: ${GERRIT_HOST}:${GERRIT_WEB_PORT}"
    echo "  Mode: $(if $STRICT_MODE; then echo "STRICT"; else echo "NORMAL"; fi)"
    echo "  Repositories: $(echo "$repos" | wc -w)"
    echo ""
    
    for repo in $repos; do
        [[ -z "$repo" ]] && continue
        
        local perms=$(get_permissions "$repo")
        if [[ "$perms" != "null" ]] && [[ -n "$perms" ]]; then
            local findings=$(audit_repo "$repo" "$perms")
            all_findings=$(echo "$all_findings" | jq --argjson findings "$findings" '. + $findings')
        fi
    done
    
    display_summary
    
    if [[ -n "$REPORT_FILE" ]]; then
        generate_report "$all_findings" > "$REPORT_FILE"
        log_info "Audit report saved to: $REPORT_FILE"
    fi
    
    # Exit with error in strict mode if issues found
    if $STRICT_MODE && [[ $CRITICAL -gt 0 || $WARNING -gt 0 ]]; then
        exit 1
    fi
}

main
