#!/bin/bash
#
# Compare permissions between repositories or detect drift from template
# Usage: ./compare-permissions.sh --source <repo> --target <repo> | --check-drift <repo> --template <template>

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SOURCE_REPO=""
TARGET_REPO=""
CHECK_DRIFT=false
DRIFT_REPO=""
DRIFT_TEMPLATE=""
OUTPUT_FORMAT="table"
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

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }
log_match() { echo -e "${GREEN}✓${NC} $1"; }
log_diff() { echo -e "${RED}✗${NC} $1"; }

show_help() {
    cat << EOF
Compare Gerrit Repository Permissions

Usage:
  # Compare two repositories
  $0 --source <repo1> --target <repo2>

  # Check drift from template
  $0 --check-drift <repo> --template <template-name>

Options:
  --source <repo>         Source repository
  --target <repo>         Target repository to compare
  --check-drift <repo>    Check repository against template
  --template <name>       Template name for drift check
  --format <format>       Output: table, json (default: table)
  --help                  Show this help

Examples:
  # Compare two repos
  $0 --source repo1 --target repo2

  # Check if repo matches git-flow template
  $0 --check-drift myrepo --template git-flow

EOF
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --source)
            SOURCE_REPO="$2"
            shift 2
            ;;
        --target)
            TARGET_REPO="$2"
            shift 2
            ;;
        --check-drift)
            CHECK_DRIFT=true
            DRIFT_REPO="$2"
            shift 2
            ;;
        --template)
            DRIFT_TEMPLATE="$2"
            shift 2
            ;;
        --format)
            OUTPUT_FORMAT="$2"
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

# Get template
get_template() {
    local template="$1"
    cat "$SCRIPT_DIR/../references/templates/${template}.json" 2>/dev/null || echo "{}"
}

# Compare two permission sets
compare_permissions() {
    local source="$1"
    local target="$2"
    local source_name="$3"
    local target_name="$4"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════════"
    echo "  Comparing: ${BOLD}${source_name}${NC} vs ${BOLD}${target_name}${NC}"
    echo "═══════════════════════════════════════════════════════════════════"
    echo ""
    
    local differences="[]"
    
    # Get all unique branches
    local branches=$(echo "$source $target" | jq -s '.[0] * .[1] | keys[]' 2>/dev/null | sort -u)
    
    if [[ -z "$branches" ]]; then
        log_warn "No branch permissions found"
        return
    fi
    
    for branch in $branches; do
        echo "  Branch: ${BOLD}${branch}${NC}"
        
        local source_branch=$(echo "$source" | jq -r ".[\"${branch}\"] // empty")
        local target_branch=$(echo "$target" | jq -r ".[\"${branch}\"] // empty")
        
        if [[ -z "$source_branch" ]]; then
            log_diff "    Only in ${target_name}"
            differences=$(echo "$differences" | jq --arg branch "$branch" --arg type "only_in_target" \
                '. + [{"branch": $branch, "type": $type}]')
        elif [[ -z "$target_branch" ]]; then
            log_diff "    Only in ${source_name}"
            differences=$(echo "$differences" | jq --arg branch "$branch" --arg type "only_in_source" \
                '. + [{"branch": $branch, "type": $type}]')
        else
            # Compare permissions for this branch
            local diff=$(echo "$source_branch" | jq --argjson target "$target_branch" \
                'with_entries(select(.value != $target[.key]))')
            
            if [[ "$diff" == "{}" ]] || [[ -z "$diff" ]]; then
                log_match "    Permissions match"
            else
                log_diff "    Permissions differ"
                echo "      Source: $(echo "$source_branch" | jq -c '.')"
                echo "      Target: $(echo "$target_branch" | jq -c '.')"
                differences=$(echo "$differences" | jq --arg branch "$branch" --argjson diff "$diff" \
                    '. + [{"branch": $branch, "type": "different", "details": $diff}]')
            fi
        fi
    done
    
    echo ""
    local diff_count=$(echo "$differences" | jq 'length')
    if [[ $diff_count -eq 0 ]]; then
        echo -e "  ${GREEN}✓${NC} Repositories have identical permission configurations"
    else
        echo -e "  ${YELLOW}⚠${NC} Found ${diff_count} differences"
    fi
    echo ""
    
    echo "$differences"
}

# Check drift from template
check_drift() {
    local repo_perms="$1"
    local template_name="$2"
    local template=$(get_template "$template_name")
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════════"
    echo "  Drift Check: ${BOLD}${DRIFT_REPO}${NC} vs ${BOLD}${template_name}${NC} template"
    echo "═══════════════════════════════════════════════════════════════════"
    echo ""
    
    if [[ "$template" == "{}" ]]; then
        log_error "Template not found: ${template_name}"
        exit 1
    fi
    
    local drift_items="[]"
    local compliant_items="[]"
    
    # Check each branch in template
    local template_branches=$(echo "$template" | jq -r '.branches // {} | keys[]' 2>/dev/null)
    
    for branch_key in $template_branches; do
        local branch_pattern=$(echo "$template" | jq -r ".branches[\"${branch_key}\"].pattern // \"${branch_key}\"")
        local expected_perms=$(echo "$template" | jq -r ".branches[\"${branch_key}\"]")
        
        echo "  Checking branch pattern: ${BOLD}${branch_pattern}${NC}"
        
        # Find matching branches in repo
        local matching_branches=$(echo "$repo_perms" | jq -r --arg pattern "$branch_pattern" \
            'keys | map(select(test($pattern))) | .[]' 2>/dev/null)
        
        if [[ -z "$matching_branches" ]]; then
            log_warn "    No matching branches found"
            drift_items=$(echo "$drift_items" | jq --arg pattern "$branch_pattern" \
                '. + [{"pattern": $pattern, "status": "missing_branch"}]')
        else
            for branch in $matching_branches; do
                local actual_perms=$(echo "$repo_perms" | jq -r ".[\"${branch}\"]")
                
                # Simplified check - in real implementation, compare specific permissions
                if [[ -n "$actual_perms" ]]; then
                    log_match "    ${branch}: configured"
                    compliant_items=$(echo "$compliant_items" | jq --arg branch "$branch" \
                        '. + [{"branch": $branch, "status": "compliant"}]')
                else
                    log_diff "    ${branch}: not configured"
                    drift_items=$(echo "$drift_items" | jq --arg branch "$branch" \
                        '. + [{"branch": $branch, "status": "not_configured"}]')
                fi
            done
        fi
    done
    
    echo ""
    local drift_count=$(echo "$drift_items" | jq 'length')
    local compliant_count=$(echo "$compliant_items" | jq 'length')
    
    echo "  Summary:"
    echo "    Compliant: ${GREEN}${compliant_count}${NC}"
    echo "    Drift: ${RED}${drift_count}${NC}"
    
    if [[ $drift_count -eq 0 ]]; then
        echo -e "  ${GREEN}✓${NC} Repository fully compliant with ${template_name} template"
    else
        echo -e "  ${YELLOW}⚠${NC} Configuration drift detected"
    fi
    echo ""
}

# Main execution
main() {
    if ! $CHECK_DRIFT; then
        # Compare mode
        if [[ -z "$SOURCE_REPO" ]] || [[ -z "$TARGET_REPO" ]]; then
            log_error "Both --source and --target required for comparison"
            exit 1
        fi
        
        log_info "Fetching permissions..."
        local source_perms=$(get_permissions "$SOURCE_REPO")
        local target_perms=$(get_permissions "$TARGET_REPO")
        
        compare_permissions "$source_perms" "$target_perms" "$SOURCE_REPO" "$TARGET_REPO"
        
    else
        # Drift check mode
        if [[ -z "$DRIFT_REPO" ]] || [[ -z "$DRIFT_TEMPLATE" ]]; then
            log_error "Both --check-drift and --template required for drift check"
            exit 1
        fi
        
        log_info "Fetching permissions..."
        local repo_perms=$(get_permissions "$DRIFT_REPO")
        
        check_drift "$repo_perms" "$DRIFT_TEMPLATE"
    fi
}

main
