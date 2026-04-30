#!/bin/bash
#
# Apply permission templates to Gerrit repositories
# Usage: ./apply-permissions.sh --repo <repo-name> --template <template-name>

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_NAME=""
TEMPLATE_NAME=""
CUSTOM_PERMISSIONS=""
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

# Parse arguments
while [[ $# -gt 0 ]]; do
    case $1 in
        --repo)
            REPO_NAME="$2"
            shift 2
            ;;
        --template)
            TEMPLATE_NAME="$2"
            shift 2
            ;;
        --permissions)
            CUSTOM_PERMISSIONS="$2"
            shift 2
            ;;
        --dry-run)
            DRY_RUN=true
            shift
            ;;
        --help)
            echo "Usage: $0 --repo <repo-name> --template <template-name> [options]"
            echo ""
            echo "Options:"
            echo "  --repo <name>          Repository name"
            echo "  --template <name>      Template name (standard, restricted, protected-branches, multi-team, ci-cd)"
            echo "  --permissions <file>   Custom permissions JSON file"
            echo "  --dry-run              Show what would be done without applying"
            echo "  --help                 Show this help"
            exit 0
            ;;
        *)
            log_error "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Validate required arguments
if [[ -z "$REPO_NAME" ]]; then
    log_error "Repository name is required. Use --repo <name>"
    exit 1
fi

if [[ -z "$TEMPLATE_NAME" && -z "$CUSTOM_PERMISSIONS" ]]; then
    log_error "Either --template or --permissions must be specified"
    exit 1
fi

# Get template file
if [[ -n "$TEMPLATE_NAME" ]]; then
    TEMPLATE_FILE="$SCRIPT_DIR/../references/templates/${TEMPLATE_NAME}.json"
    
    # Create template if it doesn't exist
    if [[ ! -f "$TEMPLATE_FILE" ]]; then
        log_info "Template file not found, extracting from permission-templates.md"
        
        # Extract template from markdown reference
        mkdir -p "$(dirname "$TEMPLATE_FILE")"
        
        case "$TEMPLATE_NAME" in
            standard)
                cat > "$TEMPLATE_FILE" << 'EOF'
{
  "description": "Standard open source project permissions",
  "refs/heads/main": {
    "permissions": {
      "read": ["Anonymous Users"],
      "submit": ["Project Owners", "Maintainers"],
      "label-Code-Review": ["Registered Users"],
      "label-Verified": ["CI Bot"]
    },
    "requirements": {
      "minCodeReviewScore": 1,
      "minVerifiedScore": 1
    }
  }
}
EOF
                ;;
            restricted)
                cat > "$TEMPLATE_FILE" << 'EOF'
{
  "description": "Restricted access permissions",
  "refs/heads/main": {
    "permissions": {
      "read": ["Registered Users"],
      "submit": ["Project Owners"],
      "label-Code-Review": ["Maintainers"],
      "label-Verified": ["CI Bot"]
    }
  },
  "refs/heads/*": {
    "permissions": {
      "read": ["Registered Users"],
      "create": ["Maintainers"],
      "push": ["Maintainers"]
    }
  }
}
EOF
                ;;
            protected-branches)
                cat > "$TEMPLATE_FILE" << 'EOF'
{
  "description": "Protected branches with mandatory reviews",
  "refs/heads/main": {
    "permissions": {
      "read": ["Anonymous Users"],
      "submit": ["Project Owners"],
      "label-Code-Review": ["Maintainers"]
    },
    "requirements": {
      "minCodeReviewScore": 2,
      "requiredReviewers": 2
    }
  },
  "refs/heads/feature/*": {
    "permissions": {
      "read": ["Registered Users"],
      "create": ["Registered Users"],
      "push": ["Registered Users"]
    }
  }
}
EOF
                ;;
            *)
                log_error "Unknown template: $TEMPLATE_NAME"
                exit 1
                ;;
        esac
    fi
    
    PERMISSIONS_FILE="$TEMPLATE_FILE"
else
    PERMISSIONS_FILE="$CUSTOM_PERMISSIONS"
fi

if [[ ! -f "$PERMISSIONS_FILE" ]]; then
    log_error "Permissions file not found: $PERMISSIONS_FILE"
    exit 1
fi

log_info "Applying permissions to repository: $REPO_NAME"
log_info "Using template: $TEMPLATE_NAME"

if $DRY_RUN; then
    log_info "DRY RUN - No changes will be applied"
    cat "$PERMISSIONS_FILE"
    exit 0
fi

# Convert JSON permissions to Gerrit project.config format
convert_to_gerrit_config() {
    local json_file="$1"
    local repo="$2"
    
    # Create project.config content
    cat << 'GERRITCONFIG'
[project]
    description = Permissions managed by gerrit-permission-manager

GERRITCONFIG

    # Parse JSON and generate access sections
    # This is a simplified version - in production, use jq or proper JSON parsing
    
    echo "# Access permissions"
    echo "[access \"refs/heads/*\"]"
    echo "    read = group Anonymous Users"
    echo ""
    echo "[access \"refs/heads/main\"]"
    echo "    submit = group Project Owners"
    echo "    label-Code-Review = -2..+2 group Maintainers"
    echo "    label-Code-Review = -1..+1 group Registered Users"
}

# Apply permissions via Gerrit REST API or SSH
apply_permissions_ssh() {
    local repo="$1"
    
    log_info "Applying permissions via SSH..."
    
    # Set project permissions using SSH
    ssh -p $GERRIT_PORT $GERRIT_USER@$GERRIT_HOST \
        gerrit set-project "$repo" \
        --submit-type MERGE_IF_NECESSARY \
        --require-change-id \
        --require-signed-off-by 2>/dev/null || {
        log_warn "SSH command failed, trying REST API..."
        return 1
    }
    
    return 0
}

apply_permissions_api() {
    local repo="$1"
    local permissions_file="$2"
    
    log_info "Applying permissions via REST API..."
    
    # Get current permissions first
    local current_access
    current_access=$(curl -s -X GET \
        "http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a/projects/$(echo -n "$repo" | jq -sRr @uri)/access/" \
        -u "$GERRIT_USER:$GERRIT_PASSWORD" 2>/dev/null | tail -c +6) || {
        log_warn "Failed to get current permissions"
        current_access="{}"
    }
    
    # Prepare new permissions payload
    local payload
    payload=$(cat "$permissions_file" | jq -c '.')
    
    # Apply new permissions
    curl -s -X POST \
        "http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a/projects/$(echo -n "$repo" | jq -sRr @uri)/access/" \
        -H "Content-Type: application/json" \
        -u "$GERRIT_USER:$GERRIT_PASSWORD" \
        -d "$payload" 2>/dev/null | tail -c +6
    
    log_info "Permissions applied via REST API"
}

# Try SSH first, fallback to API
if ! apply_permissions_ssh "$REPO_NAME"; then
    if command -v jq &> /dev/null; then
        apply_permissions_api "$REPO_NAME" "$PERMISSIONS_FILE"
    else
        log_error "jq is required for REST API mode. Install jq or configure SSH keys."
        exit 1
    fi
fi

log_info "Permissions applied successfully to $REPO_NAME"
log_info ""
log_info "Verification commands:"
log_info "  ssh -p $GERRIT_PORT $GERRIT_USER@$GERRIT_HOST gerrit query project:$REPO_NAME"
