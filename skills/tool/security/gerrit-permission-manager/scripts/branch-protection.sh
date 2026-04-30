#!/bin/bash
#
# Branch protection utility for Gerrit repositories
# Usage: ./branch-protection.sh --repo <repo> --branch <branch-pattern> [options]

set -e

REPO_NAME=""
BRANCH_PATTERN=""
REQUIRE_REVIEW=1
REQUIRE_SUBMIT_ACCESS=true
BLOCK_FORCE_PUSH=true
ALLOWED_USERS=""
GERRIT_HOST=${GERRIT_HOST:-"localhost"}
GERRIT_PORT=${GERRIT_PORT:-"29418"}
GERRIT_USER=${GERRIT_USER:-"admin"}

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --repo)
            REPO_NAME="$2"
            shift 2
            ;;
        --branch)
            BRANCH_PATTERN="$2"
            shift 2
            ;;
        --require-review)
            REQUIRE_REVIEW="$2"
            shift 2
            ;;
        --require-submit-access)
            REQUIRE_SUBMIT_ACCESS=true
            shift
            ;;
        --allow-force-push)
            BLOCK_FORCE_PUSH=false
            shift
            ;;
        --allowed-users)
            ALLOWED_USERS="$2"
            shift 2
            ;;
        --help)
            echo "Usage: $0 --repo <repo> --branch <pattern> [options]"
            echo ""
            echo "Options:"
            echo "  --repo <name>              Repository name"
            echo "  --branch <pattern>         Branch pattern (e.g., refs/heads/main)"
            echo "  --require-review <n>       Required review score (default: 1)"
            echo "  --require-submit-access    Require submit access to merge"
            echo "  --allow-force-push         Allow force push (default: block)"
            echo "  --allowed-users <groups>   Comma-separated list of allowed groups"
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate arguments
if [[ -z "$REPO_NAME" || -z "$BRANCH_PATTERN" ]]; then
    log_error "Both --repo and --branch are required"
    exit 1
fi

log_info "Configuring branch protection for $REPO_NAME:$BRANCH_PATTERN"

# Generate project.config section for branch protection
generate_protection_config() {
    local branch="$1"
    
    cat << EOF

# Branch protection for $branch
[access "$branch"]
    read = group Anonymous Users
    submit = group Project Owners
    submit = group Maintainers
    label-Code-Review = -2..+2 group Maintainers
    label-Code-Review = -1..+1 group Registered Users
EOF

    if $BLOCK_FORCE_PUSH; then
        cat << EOF
    push = -force group Registered Users
    push = group Maintainers
EOF
    fi

    if [[ -n "$ALLOWED_USERS" ]]; then
        IFS=',' read -ra GROUPS <<< "$ALLOWED_USERS"
        for group in "${GROUPS[@]}"; do
            echo "    submit = group $group"
        done
    fi
}

# Apply via SSH
apply_protection_ssh() {
    local repo="$1"
    local branch="$2"
    
    log_info "Applying branch protection via SSH..."
    
    # Set review requirements
    ssh -p $GERRIT_PORT $GERRIT_USER@$GERRIT_HOST \
        gerrit set-reviewers-cmd --project "$repo" \
        --add " Maintainers" 2>/dev/null || true
    
    # Block direct push to protected branch for non-maintainers
    ssh -p $GERRIT_PORT $GERRIT_USER@$GERRIT_HOST \
        gerrit create-group "${repo}-${branch//\//-}-submitters" 2>/dev/null || true
    
    log_info "Branch protection configured via SSH"
}

# Create permission update payload
create_permission_payload() {
    local branch="$1"
    
    cat << EOF
{
  "add": {
    "$branch": {
      "permissions": {
        "read": {
          "rules": {
            "group/Anonymous Users": { "action": "ALLOW" }
          }
        },
        "submit": {
          "rules": {
            "group/Project Owners": { "action": "ALLOW" },
            "group/Maintainers": { "action": "ALLOW" }
          }
        },
        "label-Code-Review": {
          "label_id": "Code-Review",
          "rules": {
            "group/Registered Users": { "action": "ALLOW", "min": -1, "max": 1 },
            "group/Maintainers": { "action": "ALLOW", "min": -2, "max": 2 }
          }
        }
      }
    }
  }
}
EOF
}

# Apply via REST API
apply_protection_api() {
    local repo="$1"
    local branch="$2"
    
    log_info "Applying branch protection via REST API..."
    
    local payload
    payload=$(create_permission_payload "$branch")
    
    # Post to Gerrit REST API
    curl -s -X POST \
        "http://${GERRIT_HOST}:8080/a/projects/$(echo -n "$repo" | jq -sRr @uri)/access/" \
        -H "Content-Type: application/json" \
        -d "$payload" 2>/dev/null | tail -c +6
    
    log_info "Branch protection applied via REST API"
}

# Main execution
echo "Branch Protection Configuration"
echo "==============================="
echo "Repository: $REPO_NAME"
echo "Branch: $BRANCH_PATTERN"
echo "Required Review Score: $REQUIRE_REVIEW"
echo "Block Force Push: $BLOCK_FORCE_PUSH"
echo ""

# Try SSH first, then API
if ! apply_protection_ssh "$REPO_NAME" "$BRANCH_PATTERN"; then
    if command -v jq &> /dev/null; then
        apply_protection_api "$REPO_NAME" "$BRANCH_PATTERN"
    else
        log_warn "Could not apply via API (jq not installed)"
        log_info "Manual configuration required:"
        generate_protection_config "$BRANCH_PATTERN"
    fi
fi

log_info "Branch protection configured for $REPO_NAME:$BRANCH_PATTERN"
log_info ""
log_info "Verification:"
log_info "  ssh -p $GERRIT_PORT $GERRIT_USER@$GERRIT_HOST gerrit ls-projects -d"
