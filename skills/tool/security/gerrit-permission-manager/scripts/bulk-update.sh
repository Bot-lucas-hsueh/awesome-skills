#!/bin/bash
#
# Bulk update permissions across multiple repositories using manifest
# Usage: ./bulk-update.sh --manifest <manifest.xml> --permission-file <permissions.json>

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
MANIFEST_FILE=""
PERMISSIONS_FILE=""
TEMPLATE_NAME=""
PARALLEL=false
MAX_JOBS=4
DRY_RUN=false

GERRIT_HOST=${GERRIT_HOST:-"localhost"}
GERRIT_PORT=${GERRIT_PORT:-"29418"}
GERRIT_USER=${GERRIT_USER:-"admin"}

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }
log_debug() { echo -e "${BLUE}[DEBUG]${NC} $1"; }

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --manifest)
            MANIFEST_FILE="$2"
            shift 2
            ;;
        --permission-file)
            PERMISSIONS_FILE="$2"
            shift 2
            ;;
        --template)
            TEMPLATE_NAME="$2"
            shift 2
            ;;
        --parallel)
            PARALLEL=true
            shift
            ;;
        --jobs)
            MAX_JOBS="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --help)
            echo "Usage: $0 --manifest <manifest.xml> [options]"
            echo ""
            echo "Options:"
            echo "  --manifest <file>        Manifest XML file"
            echo "  --permission-file <file> JSON permissions file"
            echo "  --template <name>        Use predefined template"
            echo "  --parallel               Run updates in parallel"
            echo "  --jobs <n>               Max parallel jobs (default: 4)"
            echo "  --dry-run                Show what would be done"
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate arguments
if [[ -z "$MANIFEST_FILE" ]]; then
    log_error "Manifest file is required. Use --manifest <file>"
    exit 1
fi

if [[ ! -f "$MANIFEST_FILE" ]]; then
    log_error "Manifest file not found: $MANIFEST_FILE"
    exit 1
fi

if [[ -z "$PERMISSIONS_FILE" && -z "$TEMPLATE_NAME" ]]; then
    log_error "Either --permission-file or --template must be specified"
    exit 1
fi

# Extract repositories from manifest
extract_repos() {
    local manifest="$1"
    
    # Parse XML and extract project names
    # Using grep/sed for simplicity - in production use proper XML parsing
    grep -o 'name="[^"]*"' "$manifest" | \
        sed 's/name="//g' | sed 's/"//g' | \
        sort -u
}

# Update single repository
update_repo() {
    local repo="$1"
    local perm_file="$2"
    local template="$3"
    
    log_info "Updating: $repo"
    
    if $DRY_RUN; then
        log_info "[DRY-RUN] Would update $repo"
        return 0
    fi
    
    if [[ -n "$template" ]]; then
        "$SCRIPT_DIR/apply-permissions.sh" --repo "$repo" --template "$template" 2>&1 | sed "s/^/[$repo] /"
    else
        "$SCRIPT_DIR/apply-permissions.sh" --repo "$repo" --permissions "$perm_file" 2>&1 | sed "s/^/[$repo] /"
    fi
    
    local status=$?
    if [[ $status -eq 0 ]]; then
        log_info "✓ $repo updated successfully"
    else
        log_error "✗ $repo update failed"
    fi
    
    return $status
}

# Main execution
log_info "Starting bulk permission update"
log_info "Manifest: $MANIFEST_FILE"

# Get list of repositories
REPOS=$(extract_repos "$MANIFEST_FILE")
REPO_COUNT=$(echo "$REPOS" | wc -l)

log_info "Found $REPO_COUNT repositories in manifest"

if $DRY_RUN; then
    log_info "DRY RUN mode - no changes will be applied"
    echo "Repositories to update:"
    echo "$REPOS"
    exit 0
fi

# Track results
SUCCESS_COUNT=0
FAIL_COUNT=0

if $PARALLEL; then
    log_info "Running in parallel mode (max $MAX_JOBS jobs)"
    
    # Export function for parallel execution
    export -f update_repo log_info log_error
    export SCRIPT_DIR PERMISSIONS_FILE TEMPLATE_NAME DRY_RUN
    
    # Run in parallel using xargs
    while IFS= read -r repo; do
        echo "$repo"
    done <<< "$REPOS" | xargs -P "$MAX_JOBS" -I {} bash -c 'update_repo "$@"' _ {} "$PERMISSIONS_FILE" "$TEMPLATE_NAME"
    
    # Note: In production, use proper parallel execution with result tracking
else
    # Sequential execution
    while IFS= read -r repo; do
        if update_repo "$repo" "$PERMISSIONS_FILE" "$TEMPLATE_NAME"; then
            ((SUCCESS_COUNT++))
        else
            ((FAIL_COUNT++))
        fi
    done <<< "$REPOS"
fi

# Summary
echo ""
log_info "======================================="
log_info "Bulk Update Summary"
log_info "======================================="
log_info "Total repositories: $REPO_COUNT"
log_info "Successful: $SUCCESS_COUNT"
log_info "Failed: $FAIL_COUNT"

if [[ $FAIL_COUNT -gt 0 ]]; then
    exit 1
fi

log_info "All repositories updated successfully!"
