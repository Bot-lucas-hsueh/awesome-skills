# Examples

## 10.1 Cloudflare CLI (wrangler) Commands

### 10.1.1 Workers Setup

```bash
# Install wrangler
npm install -g wrangler

# Login to Cloudflare
wrangler login

# Create new worker project
wrangler generate my-worker

# Create worker from scratch
wrangler init my-worker

# Preview worker locally
wrangler dev

# Deploy worker to production
wrangler deploy

# List workers
wrangler deployments list
```

### 10.1.2 Workers Script Examples

```javascript
// Basic HTTP handler
export default {
  async fetch(request) {
    return new Response('Hello World!', {
      headers: { 'Content-Type': 'text/plain' }
    });
  }
};

// Fetch from origin with caching
export default {
  async fetch(request, env) {
    const cache = caches.default;
    let response = await cache.match(request);
    
    if (!response) {
      response = await fetch(request);
      response = new Response(response.body, response);
      response.headers.append('Cache-Control', 'max-age=3600');
      await cache.put(request, response.clone());
    }
    
    return response;
  }
};

// API proxy with rate limiting
export default {
  async fetch(request, env) {
    const ip = request.headers.get('CF-Connecting-IP');
    const key = `rate_limit:${ip}`;
    const count = await env.KV.get(key);
    
    if (count && parseInt(count) > 100) {
      return new Response('Rate limit exceeded', { status: 429 });
    }
    
    await env.KV.put(key, String((parseInt(count) || 0) + 1), {
      expirationTtl: 60
    });
    
    return fetch('https://api.example.com' + new URL(request.url).pathname, {
      headers: { 'Authorization': `Bearer ${env.API_TOKEN}` }
    });
  }
};
```

### 10.1.3 D1 Database Commands

```bash
# Create D1 database
wrangler d1 create my-database

# Create table
wrangler d1 execute my-database --command="
  CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE
  )
"

# Insert data
wrangler d1 execute my-database --command="
  INSERT INTO users (name, email) VALUES ('John', 'john@example.com')
"

# Query data
wrangler d1 execute my-database --command="SELECT * FROM users"

# Prepare statement with binding
wrangler d1 execute my-database \
  --command="SELECT * FROM users WHERE email = ?" \
  --bind "john@example.com"
```

### 10.1.4 R2 Storage Commands

```bash
# List buckets
wrangler r2 bucket list

# Create bucket
wrangler r2 bucket create my-bucket

# Upload file
wrangler r2 object put my-file.txt --bucket=my-bucket < my-file.txt

# List objects
wrangler r2 object list --bucket=my-bucket

# Get object
wrangler r2 object get my-bucket/my-file.txt -o downloaded.txt
```

## 10.2 DNS Management

### 10.2.1 Common DNS Records via API

```bash
# Get zone ID
curl -X GET "https://api.cloudflare.com/client/v4/zones?name=example.com" \
  -H "Authorization: Bearer {token}"

# Create A record
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{
    "type": "A",
    "name": "www",
    "content": "192.0.2.1",
    "ttl": 300,
    "proxied": true
  }'

# Create CNAME record
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{
    "type": "CNAME",
    "name": "api",
    "content": "example.com",
    "ttl": 300,
    "proxied": true
  }'

# Create MX record
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{
    "type": "MX",
    "name": "@",
    "content": "mail.example.com",
    "priority": 10,
    "ttl": 3600
  }'
```

### 10.2.2 DNS Configuration Examples

| Record Type | Name | Content | Proxy |
|------------|------|---------|-------|
| A | @ | 192.0.2.1 | Proxied |
| A | www | 192.0.2.1 | Proxied |
| AAAA | @ | 2001:db8::1 | DNS only |
| CNAME | api | example.com | Proxied |
| MX | @ | mail.example.com | DNS only |
| TXT | @ | v=spf1 include:_spf.example.com ~all | DNS only |
| CAA | @ | 0 issue "letsencrypt.org" | DNS only |

## 10.3 Firewall Rules

### 10.3.1 Common Firewall Rules via API

```bash
# Block specific IP
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{
    "filter": {
      "expression": "ip.src == 192.0.2.1"
    },
    "action": "block"
  }'

# Challenge bad bots
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{
    "filter": {
      "expression": "cf.threat_score > 30"
    },
    "action": "challenge"
  }'

# Allow specific country
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/firewall/rules" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{
    "filter": {
      "expression": "not (ip.geoip.country in {'US' 'CA' 'GB'})"
    },
    "action": "js_challenge"
  }'
```

### 10.3.2 Rate Limiting Rules

```json
{
  "description": "API rate limit",
  "expression": "(http.request.uri.path contains \"/api/\")",
  "ratelimit": {
    "requests_per_period": 100,
    "period": 60,
    "response_code": 429,
    "action": "block",
    "bypass_url_pattern": ""
  }
}
```

## 10.4 Page Rules (Deprecated - Use Workers)

```javascript
// Equivalent Worker for Page Rules
export default {
  async fetch(request, env) {
    const url = new URL(request.url);
    
    // Always use HTTPS
    if (url.protocol === 'http:') {
      url.protocol = 'https:';
      return Response.redirect(url.toString(), 301);
    }
    
    // Forward www to root
    if (url.hostname.startsWith('www.')) {
      url.hostname = url.hostname.replace('www.', '');
      return Response.redirect(url.toString(), 301);
    }
    
    return fetch(request);
  }
};
```

## 10.5 Cache Configuration

### 10.5.1 Cache API via Workers

```javascript
// Cache API response
export default {
  async fetch(request, env) {
    const cacheKey = new Request(request.url, request);
    const cache = caches.default;
    
    const cached = await cache.match(cacheKey);
    if (cached) {
      return cached;
    }
    
    const response = await fetch(request);
    if (response.ok) {
      const newResponse = new Response(response.body, response);
      newResponse.headers.set('Cache-Control', 'public, max-age=86400');
      await cache.put(cacheKey, newResponse.clone());
      return newResponse;
    }
    
    return response;
  }
};
```

### 10.5.2 Cache Purge via API

```bash
# Purge all cache
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{"purge_everything": true}'

# Purge specific files
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{"files": [
    "https://example.com/style.css",
    "https://example.com/script.js"
  ]}'

# Purge by tag
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{"tags": ["product-page", "homepage"]}'
```

## 10.6 Load Balancer Configuration

### 10.6.1 Health Check Configuration

```json
{
  "monitor": {
    "type": "http",
    "interval": 60,
    "timeout": 30,
    "retries": 3,
    "method": "GET",
    "path": "/health",
    "header": {
      "Host": ["example.com"]
    },
    "expected_body": "healthy",
    "expected_codes": ["200"]
  }
}
```

## 10.7 wrangler.toml Examples

```toml
name = "my-worker"
main = "src/index.js"
compatibility_date = "2024-01-01"

[env.production]
name = "my-worker-prod"

[[kv_namespaces]]
binding = "CACHE"
id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

[[d1_databases]]
binding = "DB"
database_name = "my-database"
database_id = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"

[[r2_buckets]]
binding = "BUCKET"
bucket_name = "my-bucket"
```
