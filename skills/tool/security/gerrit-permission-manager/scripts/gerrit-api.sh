#!/bin/bash
#
# Gerrit REST API helper script
# Usage: ./gerrit-api.sh <method> <endpoint> [options]

set -e

GERRIT_HOST=${GERRIT_HOST:-"localhost"}
GERRIT_WEB_PORT=${GERRIT_WEB_PORT:-"8080"}
GERRIT_USER=${GERRIT_USER:-"admin"}
GERRIT_PASSWORD=${GERRIT_PASSWORD:-"secret"}

METHOD=""
ENDPOINT=""
DATA=""
VERBOSE=false

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

log_info() { echo -e "${GREEN}[INFO]${NC} $1"; }
log_warn() { echo -e "${YELLOW}[WARN]${NC} $1"; }
log_error() { echo -e "${RED}[ERROR]${NC} $1"; }

# Show help
show_help() {
    cat << EOF
Gerrit REST API Helper

Usage: $0 <method> <endpoint> [options]

Methods: GET, POST, PUT, DELETE

Endpoints:
  /projects/                     List all projects
  /projects/{name}/              Get project info
  /projects/{name}/access/       Get/set project access
  /groups/                       List all groups
  /groups/{name}/                Get group info
  /accounts/                     List accounts
  /config/version/               Get Gerrit version

Options:
  --data <json>       JSON data for POST/PUT requests
  --data @file        Read JSON data from file
  -v, --verbose       Verbose output
  --help              Show this help

Environment Variables:
  GERRIT_HOST         Gerrit hostname (default: localhost)
  GERRIT_WEB_PORT     Gerrit HTTP port (default: 8080)
  GERRIT_USER         Gerrit username (default: admin)
  GERRIT_PASSWORD     Gerrit password

Examples:
  $0 GET /projects/
  $0 GET /projects/myrepo/access/
  $0 POST /projects/myrepo/access/ --data @permissions.json
  $0 GET /groups/
  $0 PUT /config/server/preferences --data '{"theme":"NIGHT"}'

EOF
}

# Parse arguments
if [[ $# -lt 2 ]]; then
    show_help
    exit 1
fi

METHOD="$1"
ENDPOINT="$2"
shift 2

while [[ $# -gt 0 ]]; do
    case $1 in
        --data)
            DATA="$2"
            shift 2
            ;;
        -v|--verbose)
            VERBOSE=true
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

# Build URL
URL="http://${GERRIT_HOST}:${GERRIT_WEB_PORT}/a${ENDPOINT}"

# Build curl command
CURL_OPTS="-s"
if $VERBOSE; then
    CURL_OPTS="-v"
fi

# Prepare data
if [[ -n "$DATA" ]]; then
    if [[ "$DATA" == @* ]]; then
        # Read from file
        DATA_FILE="${DATA#@}"
        if [[ ! -f "$DATA_FILE" ]]; then
            log_error "Data file not found: $DATA_FILE"
            exit 1
        fi
        CURL_DATA="--data-binary @$DATA_FILE"
    else
        # Inline JSON
        CURL_DATA="--data '$DATA'"
    fi
fi

# Execute request
log_info "${METHOD} ${URL}"

RESPONSE=$(curl $CURL_OPTS \
    -X "$METHOD" \
    -H "Content-Type: application/json" \
    -u "$GERRIT_USER:$GERRIT_PASSWORD" \
    ${CURL_DATA:-} \
    "$URL" 2>&1)

# Gerrit returns JSON with )]}' prefix for security
CLEAN_RESPONSE=$(echo "$RESPONSE" | sed 's/^[)]}]//' )

# Check if response is JSON
if echo "$CLEAN_RESPONSE" | jq -e . > /dev/null 2>&1; then
    # Pretty print JSON
    echo "$CLEAN_RESPONSE" | jq '.'
else
    echo "$CLEAN_RESPONSE"
fi
