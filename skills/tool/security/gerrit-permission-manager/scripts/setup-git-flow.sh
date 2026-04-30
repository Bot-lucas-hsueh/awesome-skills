#!/bin/bash
#
# Setup Git Flow workflow for a Gerrit repository
# Usage: ./setup-git-flow.sh --repo <repo-name> [--create-groups] [--apply-permissions]

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_NAME=""
CREATE_GROUPS=false
APPLY_PERMISSIONS=false
DRY_RUN=false

GERRIT_HOST=${GERRIT_HOST:-"localhost"}
GERRIT_PORT=${GERRIT_PORT:-"29418"}
GERRIT_WEB_PORT=${GERRIT_WEB_PORT:-"8080"}
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

# Show help
show_help() {
    cat << EOF
Git Flow Setup Script

Usage: $0 --repo <repo-name> [options]

Options:
  --repo <name>           Repository name (required)
  --create-groups         Create Git Flow groups in Gerrit
  --apply-permissions     Apply Git Flow permission template
  --dry-run               Show what would be done without executing
  --help                  Show this help

Environment Variables:
  GERRIT_HOST             Gerrit hostname (default: localhost)
  GERRIT_WEB_PORT         Gerrit HTTP port (default: 8080)
  GERRIT_USER             Gerrit admin username (default: admin)

Examples:
  # Setup Git Flow for repository
  $0 --repo myproject --create-groups --apply-permissions

  # Preview changes
  $0 --repo myproject --create-groups --dry-run

EOF
}

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --repo)
            REPO_NAME="$2"
            shift 2
            ;;
        --create-groups)
            CREATE_GROUPS=true
            shift
            ;;
        --apply-permissions)
            APPLY_PERMISSIONS=true
            shift
            ;;
        --dry-run)
            DRY_RUN=true
            shift
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

# Validate arguments
if [[ -z "$REPO_NAME" ]]; then
    log_error "Repository name is required. Use --repo <name>"
    exit 1
fi

if ! $CREATE_GROUPS && ! $APPLY_PERMISSIONS; then
    log_error "At least one of --create-groups or --apply-permissions must be specified"
    exit 1
fi

log_info "Setting up Git Flow for repository: $REPO_NAME"

# Create Git Flow groups
create_groups() {
    log_info "Creating Git Flow groups..."
    
    local groups=(
        "Project Owners"
        "Release Managers"
        "Team Leads"
        "Developers"
        "CI Bot"
    )
    
    for group in "${groups[@]}"; do
        local group_url=$(echo "$group" | sed 's/ /+/g')
        
        if $DRY_RUN; then
            log_info "[DRY-RUN] Would create group: $group"
        else
            # Create group via REST API
            local response=$(curl -s -X PUT \
                "http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a/groups/${group_url}" \
                --user "${GERRIT_USER}" \
                -H "Content-Type: application/json" \
                -d "{\"description\":\"Git Flow: ${group}\",\"visible_to_all\":true}" 2>&1)
            
            if [[ "$response" == *")]}'"* ]]; then
                log_info "✓ Created group: $group"
            elif [[ "$response" == *"already exists"* ]]; then
                log_warn "Group already exists: $group"
            else
                log_error "Failed to create group: $group"
                log_debug "Response: $response"
            fi
        fi
    done
}

# Apply Git Flow permissions
apply_permissions() {
    log_info "Applying Git Flow permissions..."
    
    if $DRY_RUN; then
        log_info "[DRY-RUN] Would apply git-flow template to $REPO_NAME"
        cat << EOF

Permission Structure:

master (Production)
  - Read: All users
  - Submit: Project Owners, Release Managers (requires 2 reviews)
  - Push: Project Owners only

develop (Integration)
  - Read: Registered users
  - Submit: Project Owners, Release Managers, Team Leads (requires 1 review)
  - Push: Team Leads and above

feature/* branches
  - Read: Registered users
  - Create: Developers, Team Leads
  - Push: Developers, Team Leads
  - Submit: Team Leads, Release Managers

release/* branches
  - Read: Registered users
  - Create: Release Managers, Project Owners
  - Push: Release Managers, Project Owners
  - Submit: Release Managers, Project Owners (requires 2 reviews)

hotfix/* branches
  - Read: Registered users
  - Create: Release Managers, Project Owners, Team Leads (emergency)
  - Push: Release Managers, Project Owners
  - Submit: Release Managers, Project Owners (requires 1 review)

EOF
    else
        # Apply the git-flow template
        "$SCRIPT_DIR/apply-permissions.sh" --repo "$REPO_NAME" --template git-flow
        
        if [[ $? -eq 0 ]]; then
            log_info "✓ Git Flow permissions applied successfully"
        else
            log_error "Failed to apply Git Flow permissions"
            exit 1
        fi
    fi
}

# Create develop branch if not exists
create_develop_branch() {
    log_info "Checking develop branch..."
    
    # Check if develop branch exists
    local branches=$(curl -s -X GET \
        "http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a/projects/${REPO_NAME}/branches/" \
        --user "${GERRIT_USER}" 2>&1 | sed 's/^[)]}]//' | jq -r '.[].ref' 2>/dev/null || echo "")
    
    if [[ "$branches" == *"refs/heads/develop"* ]]; then
        log_info "develop branch already exists"
    else
        log_info "Creating develop branch from master..."
        
        if $DRY_RUN; then
            log_info "[DRY-RUN] Would create develop branch"
        else
            # Create develop branch via REST API
            local response=$(curl -s -X PUT \
                "http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a/projects/${REPO_NAME}/branches/develop" \
                --user "${GERRIT_USER}" \
                -H "Content-Type: application/json" \
                -d '{"revision":"refs/heads/master"}' 2>&1)
            
            if [[ "$response" == *")]}'"* ]] || [[ "$response" == *"created"* ]]; then
                log_info "✓ Created develop branch"
            else
                log_warn "Could not create develop branch (may already exist)"
            fi
        fi
    fi
}

# Main execution
main() {
    echo "======================================="
    echo "Git Flow Setup for: $REPO_NAME"
    echo "======================================="
    echo ""
    
    if $DRY_RUN; then
        log_warn "DRY RUN MODE - No changes will be made"
        echo ""
    fi
    
    # Create groups if requested
    if $CREATE_GROUPS; then
        create_groups
        echo ""
    fi
    
    # Create develop branch
    create_develop_branch
    echo ""
    
    # Apply permissions if requested
    if $APPLY_PERMISSIONS; then
        apply_permissions
        echo ""
    fi
    
    # Summary
    echo "======================================="
    log_info "Git Flow setup complete!"
    echo "======================================="
    echo ""
    echo "Next steps:"
    echo ""
    echo "1. Add members to groups:"
    echo "   ssh -p ${GERRIT_PORT} ${GERRIT_USER}@${GERRIT_HOST} gerrit set-members --add <user> 'Release Managers'"
    echo ""
    echo "2. Verify permissions:"
    echo "   ${SCRIPT_DIR}/gerrit-api.sh GET /projects/${REPO_NAME}/access/"
    echo ""
    echo "3. Start using Git Flow:"
    echo "   repo start feature/my-feature --all"
    echo ""
    echo "See references/git-flow.md for complete workflow documentation"
    echo ""
}

# Run main
main
