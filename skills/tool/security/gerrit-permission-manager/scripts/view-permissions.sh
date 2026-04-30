#!/bin/bash
#
# View current permission configuration for Gerrit repositories
# Usage: ./view-permissions.sh --repo <repo-name> | --all | --manifest <manifest.xml>

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_NAME=""
MANIFEST_FILE=""
SHOW_ALL=false
OUTPUT_FORMAT="table"  # table, json, yaml
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
log_debug() { echo -e "${BLUE}[DEBUG]${NC} $1"; }

show_help() {
    cat << EOF
View Gerrit Repository Permissions

Usage: $0 [options]

Options:
  --repo <name>           View specific repository permissions
  --manifest <file>       View permissions for all repos in manifest
  --all                   View all repositories
  --format <format>       Output format: table, json, yaml (default: table)
  --export <file>         Export to file
  --help                  Show this help

Examples:
  # View single repo permissions
  $0 --repo myproject

  # View all repos in manifest
  $0 --manifest default.xml

  # Export to JSON
  $0 --all --format json --export permissions.json

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
        --format)
            OUTPUT_FORMAT="$2"
            shift 2
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

# Get permissions for a single repo
get_repo_permissions() {
    local repo="$1"
    
    log_debug "Fetching permissions for: $repo"
    
    local response=$(curl -s -X GET \
        "http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a/projects/$(echo -n "$repo" | jq -sRr @uri)/access/" \
        --user "${GERRIT_USER}" 2>&1)
    
    # Remove Gerrit's anti-XSS prefix
    response=$(echo "$response" | sed 's/^[)]}]//')
    
    if [[ -z "$response" ]] || [[ "$response" == "null" ]]; then
        echo "{}"
    else
        echo "$response"
    fi
}

# Get list of all projects
get_all_projects() {
    local response=$(curl -s -X GET \
        "http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a/projects/?type=CODE" \
        --user "${GERRIT_USER}" 2>&1 | sed 's/^[)]}]//')
    
    echo "$response" | jq -r 'keys[]' 2>/dev/null || echo ""
}

# Get projects from manifest
get_manifest_projects() {
    local manifest="$1"
    
    if [[ ! -f "$manifest" ]]; then
        log_error "Manifest file not found: $manifest"
        exit 1
    fi
    
    # Parse XML to extract project names
    grep -o 'name="[^"]*"' "$manifest" | sed 's/name="//g' | sed 's/"//g' | sort -u
}

# Format output as table
format_table() {
    local data="$1"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════════"
    echo "                    PERMISSION CONFIGURATION"
    echo "═══════════════════════════════════════════════════════════════════"
    echo ""
    
    # Parse and display permissions
    echo "$data" | jq -r '
        to_entries[] |
        "Repository: \(.key)
        ─────────────────────────────────────────────────────────────────
        " +
        (.value | to_entries | map(
            "  Branch: \(.key)
            " + (.value | to_entries | map(
                "    \(.key): \(.value | if type == "array" then join(", ") else . end)"
            ) | join("
            "))
        ) | join("
        ")) +
        "
        "
    '
}

# Format output as JSON
format_json() {
    local data="$1"
    echo "$data" | jq '.'
}

# Format output as YAML
format_yaml() {
    local data="$1"
    
    # Convert JSON to YAML-like format
    echo "$data" | jq -r '
        to_entries[] |
        "\(.key):" +
        (.value | to_entries | map(
            "
  \(.key):" +
            (.value | to_entries | map(
                "
    \(.key): \(.value | if type == "array" then "[" + join(", ") + "]" else . end)"
            ) | join(""))
        ) | join("")) +
        "
"
    '
}

# Display summary statistics
show_summary() {
    local data="$1"
    
    echo ""
    echo "═══════════════════════════════════════════════════════════════════"
    echo "                      SUMMARY STATISTICS"
    echo "═══════════════════════════════════════════════════════════════════"
    echo ""
    
    local total_repos=$(echo "$data" | jq 'length')
    local total_branches=$(echo "$data" | jq '[.[] | length] | add')
    
    echo "  Total Repositories: $total_repos"
    echo "  Total Branch Rules: $total_branches"
    echo ""
    
    # Count permissions by type
    echo "  Permission Distribution:"
    echo "$data" | jq -r '
        [.[].[] | keys] | flatten | group_by(.) | map({key: .[0], count: length}) | sort_by(-.count) | .[] |
        "    \(.key): \(.count)"
    '
    echo ""
}

# Main execution
main() {
    local all_permissions="{}"
    local repos=""
    
    # Determine which repos to process
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
    
    if [[ -z "$repos" ]]; then
        log_error "No repositories found"
        exit 1
    fi
    
    log_info "Fetching permissions for repositories..."
    
    # Collect permissions for all repos
    for repo in $repos; do
        [[ -z "$repo" ]] && continue
        
        log_debug "Processing: $repo"
        local perms=$(get_repo_permissions "$repo")
        
        if [[ "$perms" != "{}" ]]; then
            all_permissions=$(echo "$all_permissions" | jq --arg repo "$repo" --argjson perms "$perms" '. + {($repo): $perms}')
        fi
    done
    
    # Output based on format
    case "$OUTPUT_FORMAT" in
        json)
            if [[ -n "$EXPORT_FILE" ]]; then
                echo "$all_permissions" | jq '.' > "$EXPORT_FILE"
                log_info "Exported to: $EXPORT_FILE"
            else
                format_json "$all_permissions"
            fi
            ;;
        yaml)
            if [[ -n "$EXPORT_FILE" ]]; then
                format_yaml "$all_permissions" > "$EXPORT_FILE"
                log_info "Exported to: $EXPORT_FILE"
            else
                format_yaml "$all_permissions"
            fi
            ;;
        table|*)
            format_table "$all_permissions"
            show_summary "$all_permissions"
            ;;
    esac
}

main
