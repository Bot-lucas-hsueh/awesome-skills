#!/bin/bash
#
# Statistics and analytics for Gerrit permissions
# Usage: ./stats-permissions.sh [--repo <repo>] | [--manifest <file>] | [--all]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_NAME=""
MANIFEST_FILE=""
SHOW_ALL=false
GERRIT_HOST=${GERRIT_HOST:-"localhost"}
GERRIT_WEB_PORT=${GERRIT_WEB_PORT:-"8080"}
GERRIT_USER=${GERRIT_USER:-"admin"}

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
CYAN='\033[0;36m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

show_help() {
    cat << EOF
Permission Statistics and Analytics

Usage: $0 [options]

Options:
  --repo <name>           Statistics for specific repository
  --manifest <file>       Statistics for all repos in manifest
  --all                   Statistics for all repositories
  --export <file>         Export to JSON file
  --help                  Show this help

Examples:
  # Statistics for single repo
  $0 --repo myproject

  # Statistics for all repos
  $0 --all

  # Export statistics
  $0 --all --export stats.json

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
        --export)
            EXPORT_FILE="$2"
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

# Get permissions data
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

# Analyze permissions
analyze_permissions() {
    local all_data="{}"
    local repos="$1"
    
    for repo in $repos; do
        [[ -z "$repo" ]] && continue
        local perms=$(get_permissions "$repo")
        if [[ "$perms" != "null" ]] && [[ -n "$perms" ]]; then
            all_data=$(echo "$all_data" | jq --arg repo "$repo" --argjson perms "$perms" '. + {($repo): $perms}')
        fi
    done
    
    echo "$all_data"
}

# Calculate statistics
calculate_stats() {
    local data="$1"
    
    local total_repos=$(echo "$data" | jq 'length')
    local total_branches=$(echo "$data" | jq '[.[] | keys | length] | add // 0')
    
    # Count unique groups
    local unique_groups=$(echo "$data" | jq -r '[.[].[] | values | .[] | if type == "array" then .[] else . end] | unique | length')
    
    # Most permissive branches
    local most_permissive=$(echo "$data" | jq -r '
        to_entries | map({
            repo: .key,
            branches: (.value | keys | length)
        }) | sort_by(-.branches) | .[0:5] | .[] |
        "  \(.repo): \(.branches) branches"
    ')
    
    # Permission type distribution
    local perm_distribution=$(echo "$data" | jq -r '
        [.[].[] | keys] | flatten | group_by(.) | map({key: .[0], count: length}) | sort_by(-.count) | .[] |
        "  \(.key): \(.count)"
    ')
    
    # Groups usage
    local group_usage=$(echo "$data" | jq -r '
        [.[].[] | values | .[] | if type == "array" then .[] else . end] | group_by(.) | map({key: .[0], count: length}) | sort_by(-.count) | .[0:10] | .[] |
        "  \(.key): \(.count) references"
    ')
    
    # Branch protection stats
    local protected_branches=$(echo "$data" | jq '[.[] | keys[] | select(contains("master") or contains("main") or contains("release"))] | length')
    local feature_branches=$(echo "$data" | jq '[.[] | keys[] | select(contains("feature"))] | length')
    
    cat << EOF
{
  "total_repositories": $total_repos,
  "total_branches": $total_branches,
  "unique_groups": $unique_groups,
  "protected_branches": $protected_branches,
  "feature_branches": $feature_branches,
  "most_permissive_repos": $(echo "$data" | jq '[to_entries | map({repo: .key, branches: (.value | keys | length)}) | sort_by(-.branches) | .[0:5]]'),
  "permission_distribution": $(echo "$data" | jq '[[.[].[] | keys] | flatten | group_by(.) | map({key: .[0], count: length}) | sort_by(-.count)]'),
  "group_usage": $(echo "$data" | jq '[[.[].[] | values | .[] | if type == "array" then .[] else . end] | group_by(.) | map({group: .[0], count: length}) | sort_by(-.count)]')
}
EOF
}

# Display statistics
display_stats() {
    local stats="$1"
    
    echo ""
    echo "╔═══════════════════════════════════════════════════════════════════╗"
    echo "║                 PERMISSION STATISTICS & ANALYTICS                 ║"
    echo "╚═══════════════════════════════════════════════════════════════════╝"
    echo ""
    
    local total_repos=$(echo "$stats" | jq '.total_repositories')
    local total_branches=$(echo "$stats" | jq '.total_branches')
    local unique_groups=$(echo "$stats" | jq '.unique_groups')
    local protected_branches=$(echo "$stats" | jq '.protected_branches')
    local feature_branches=$(echo "$stats" | jq '.feature_branches')
    
    echo "📊 OVERVIEW"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    printf "  %-30s %d\n" "Total Repositories:" "$total_repos"
    printf "  %-30s %d\n" "Total Branch Rules:" "$total_branches"
    printf "  %-30s %d\n" "Unique Groups:" "$unique_groups"
    printf "  %-30s %d\n" "Protected Branches:" "$protected_branches"
    printf "  %-30s %d\n" "Feature Branches:" "$feature_branches"
    echo ""
    
    echo "🏆 MOST COMPLEX REPOSITORIES (by branch count)"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "$stats" | jq -r '.most_permissive_repos[] | "  \(.repo): \(.branches) branches"'
    echo ""
    
    echo "📋 PERMISSION TYPE DISTRIBUTION"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "$stats" | jq -r '.permission_distribution[0:10] | .[] | "  \(.key): \(.count)"'
    echo ""
    
    echo "👥 TOP 10 MOST REFERENCED GROUPS"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    echo "$stats" | jq -r '.group_usage[0:10] | .[] | "  \(.group): \(.count) references"'
    echo ""
    
    # Security insights
    echo "🔒 SECURITY INSIGHTS"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    local protected_ratio=$(( protected_branches * 100 / (total_branches > 0 ? total_branches : 1) ))
    printf "  Protected Branch Coverage: %d%%\n" "$protected_ratio"
    
    if [[ $protected_ratio -lt 30 ]]; then
        echo "  ⚠️  WARNING: Low protected branch coverage"
    elif [[ $protected_ratio -lt 60 ]]; then
        echo "  ℹ️  INFO: Moderate protected branch coverage"
    else
        echo "  ✅ GOOD: High protected branch coverage"
    fi
    echo ""
    
    # Template detection
    echo "🎯 DETECTED WORKFLOW PATTERNS"
    echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
    
    local has_git_flow=false
    local has_protected=false
    
    if [[ $feature_branches -gt 0 ]]; then
        has_git_flow=true
        echo "  ✅ Git Flow workflow detected (feature branches present)"
    fi
    
    if [[ $protected_branches -gt 0 ]]; then
        has_protected=true
        echo "  ✅ Branch protection enabled"
    fi
    
    if ! $has_git_flow && ! $has_protected; then
        echo "  ⚠️  Basic permissions only - consider using templates"
    fi
    echo ""
}

# Main execution
main() {
    local repos=""
    
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
    
    log_info "Analyzing permissions..."
    
    local data=$(analyze_permissions "$repos")
    local stats=$(calculate_stats "$data")
    
    display_stats "$stats"
    
    if [[ -n "$EXPORT_FILE" ]]; then
        echo "$stats" | jq '.' > "$EXPORT_FILE"
        log_info "Statistics exported to: $EXPORT_FILE"
    fi
}

main
