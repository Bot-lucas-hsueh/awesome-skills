# Cloudflare CLI Reference (Wrangler)

## Installation & Setup

```bash
# Install Wrangler
npm install -g wrangler

# Authenticate
wrangler login

# Check version
wrangler --version

# Update Wrangler
npm update -g wrangler
```

## Project Management

### Initialize Project
```bash
# Interactive setup
wrangler init my-project

# Specific template
wrangler init --template cloudflare/workers-sdk/templates/worker-rust

# Skip questions (defaults)
wrangler init --yes
```

### Configuration (wrangler.toml / wrangler.jsonc)
```toml
name = "my-worker"
main = "src/index.ts"
compatibility_date = "2024-01-01"
compatibility_flags = ["nodejs_compat"]

# Environment variables
[vars]
API_URL = "https://api.example.com"
ENVIRONMENT = "production"

# Secrets (not committed)
# wrangler secret put API_KEY

# KV namespace
[[kv_namespaces]]
binding = "CACHE"
id = "xxx"

# D1 database
[[d1_databases]]
binding = "DB"
database_name = "production"
database_id = "xxx"

# R2 bucket
[[r2_buckets]]
binding = "STORAGE"
bucket_name = "assets"

# Durable Objects
[[durable_objects.bindings]]
name = "RATE_LIMITER"
class_name = "RateLimiter"

# Migrations
[[migrations]]
tag = "v1"
new_classes = ["RateLimiter"]
```

## Development

### Local Development
```bash
# Start dev server (hot reload)
wrangler dev

# Custom port
wrangler dev --port 8787

# Local mode (no remote resources)
wrangler dev --local

# Remote mode (uses actual Cloudflare resources)
wrangler dev --remote
```

### Testing
```bash
# Run Vitest tests
wrangler vitest

# Single run
wrangler vitest run
```

## Deployment

### Deploy
```bash
# Deploy to production
wrangler deploy

# Deploy specific environment
wrangler deploy --env staging

# Dry run
wrangler deploy --dry-run

# Include source maps
wrangler deploy --sourcemap
```

### Version Management
```bash
# List deployments
wrangler versions list

# View specific version
wrangler versions view <version-id>

# Delete version
wrangler versions delete <version-id>

# Gradual deployment (canary)
wrangler deploy --gradual 10%  # 10% traffic initially
```

## Secrets Management

```bash
# Set secret
wrangler secret put SECRET_NAME

# Set secret for specific env
wrangler secret put SECRET_NAME --env production

# List secrets
wrangler secret list

# Delete secret
wrangler secret delete SECRET_NAME

# Bulk secrets from file
wrangler secret bulk ./secrets.json
```

## KV Commands

```bash
# Create namespace
wrangler kv:namespace create "CACHE"

# List namespaces
wrangler kv:namespace list

# Delete namespace
wrangler kv:namespace delete --namespace-id xxx

# Write key
wrangler kv:key put --namespace-id xxx "key" "value"

# Write from file
wrangler kv:key put --namespace-id xxx "config" --path ./config.json

# Bulk upload
wrangler kv:bulk put --namespace-id xxx ./keys.json

# Read key
wrangler kv:key get --namespace-id xxx "key"

# Delete key
wrangler kv:key delete --namespace-id xxx "key"

# List keys
wrangler kv:key list --namespace-id xxx --limit 100
```

## D1 Commands

```bash
# Create database
wrangler d1 create my-database

# List databases
wrangler d1 list

# Delete database
wrangler d1 delete my-database

# Execute SQL
wrangler d1 execute my-database --command "SELECT * FROM users"

# Execute from file
wrangler d1 execute my-database --file ./schema.sql

# Local development
wrangler d1 execute my-database --local --file ./seed.sql

# Create migration
wrangler d1 migrations create my-database add_users_table

# Apply migrations
wrangler d1 migrations apply my-database

# Apply locally
wrangler d1 migrations apply my-database --local
```

## R2 Commands

```bash
# Create bucket
wrangler r2 bucket create my-bucket

# List buckets
wrangler r2 bucket list

# Delete bucket
wrangler r2 bucket delete my-bucket

# Upload object
wrangler r2 object put my-bucket/file.txt --file ./file.txt

# Upload with metadata
wrangler r2 object put my-bucket/file.txt --file ./file.txt \
  --content-type "text/plain" \
  --custom-metadata "key=value"

# Download object
wrangler r2 object get my-bucket/file.txt --file ./downloaded.txt

# Delete object
wrangler r2 object delete my-bucket/file.txt

# List objects
wrangler r2 object list my-bucket --prefix "uploads/"
```

## Vectorize Commands

```bash
# Create index
wrangler vectorize create my-index --dimensions=768 --metric=cosine

# List indexes
wrangler vectorize list

# Delete index
wrangler vectorize delete my-index

# Insert vectors
wrangler vectorize insert my-index ./vectors.json

# Query index
wrangler vectorize query my-index --vector "[0.1, 0.2, ...]"

# Get index info
wrangler vectorize info my-index
```

## Tail (Live Logs)

```bash
# Stream logs
wrangler tail

# Filter by status
wrangler tail --status error

# Filter by method
wrangler tail --method POST

# Filter by IP
wrangler tail --ip 1.2.3.4

# JSON format
wrangler tail --format json

# Historical (last hour)
wrangler tail --since 1h
```

## Cloudflared (Tunnel)

```bash
# Install
brew install cloudflare/cloudflare/cloudflared

# Authenticate
cloudflared tunnel login

# Create tunnel
cloudflared tunnel create my-tunnel

# Route DNS
cloudflared tunnel route dns my-tunnel tunnel.example.com

# Run tunnel
cloudflared tunnel run my-tunnel

# Run with config
cloudflared tunnel --config ~/.cloudflared/config.yml run my-tunnel

# List tunnels
cloudflared tunnel list

# Delete tunnel
cloudflared tunnel delete my-tunnel
```

### Tunnel Config (config.yml)
```yaml
tunnel: <tunnel-id>
credentials-file: ~/.cloudflared/<tunnel-id>.json

ingress:
  - hostname: api.example.com
    service: http://localhost:3000
    originRequest:
      connectTimeout: 30s
      noTLSVerify: false
      
  - hostname: *.example.com
    service: http://localhost:8080
    
  - service: http_status:404

# Logging
logfile: /var/log/cloudflared.log
loglevel: info

# HA configuration
retries: 5
grace-period: 30s
```

## AI Commands

```bash
# List models
wrangler ai models list

# Run inference
wrangler ai run @cf/meta/llama-3.1-8b-instruct \
  '{"prompt": "Hello, how are you?"}'

# Run with image
wrangler ai run @cf/stabilityai/stable-diffusion-xl-base-1.0 \
  '{"prompt": "a cat in space"}' --output ./output.png
```

## Troubleshooting

```bash
# Check config
wrangler config

# Whoami
wrangler whoami

# Invalidate cache
wrangler publish --invalidate

# Debug mode
WRANGLER_LOG=debug wrangler deploy

# Check compatibility
wrangler deployments status
```
