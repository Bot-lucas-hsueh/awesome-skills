# Cloudflare Implementation Examples

## Example 1: Edge API with D1 Database

### Use Case
Build a globally distributed REST API with SQLite database at the edge.

### Architecture
```
User Request → Cloudflare Edge → Worker → D1 Database
                    ↓                              ↓
               Cache Response              Regional replica
```

### Implementation

**wrangler.toml:**
```toml
name = "api-service"
main = "src/index.ts"
compatibility_date = "2024-01-01"

[[d1_databases]]
binding = "DB"
database_name = "production-api"
database_id = "your-database-id"
```

**src/index.ts:**
```typescript
export interface Env {
  DB: D1Database;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    const path = url.pathname;
    
    // CORS headers
    const corsHeaders = {
      'Access-Control-Allow-Origin': '*',
      'Access-Control-Allow-Methods': 'GET, POST, PUT, DELETE, OPTIONS',
      'Content-Type': 'application/json'
    };
    
    if (request.method === 'OPTIONS') {
      return new Response(null, { headers: corsHeaders });
    }
    
    try {
      // GET /users
      if (path === '/users' && request.method === 'GET') {
        const { results } = await env.DB.prepare(
          "SELECT * FROM users LIMIT 100"
        ).all();
        return Response.json({ users: results }, { headers: corsHeaders });
      }
      
      // GET /users/:id
      const userMatch = path.match(/^\/users\/(\d+)$/);
      if (userMatch && request.method === 'GET') {
        const userId = userMatch[1];
        const user = await env.DB.prepare(
          "SELECT * FROM users WHERE id = ?"
        ).bind(userId).first();
        
        if (!user) {
          return Response.json({ error: 'Not found' }, { 
            status: 404, 
            headers: corsHeaders 
          });
        }
        return Response.json({ user }, { headers: corsHeaders });
      }
      
      // POST /users
      if (path === '/users' && request.method === 'POST') {
        const body = await request.json() as { name: string; email: string };
        const result = await env.DB.prepare(
          "INSERT INTO users (name, email, created_at) VALUES (?, ?, datetime('now')) RETURNING *"
        ).bind(body.name, body.email).first();
        
        return Response.json({ user: result }, { 
          status: 201, 
          headers: corsHeaders 
        });
      }
      
      return Response.json({ error: 'Not found' }, { 
        status: 404, 
        headers: corsHeaders 
      });
      
    } catch (error) {
      return Response.json({ error: 'Internal server error' }, { 
        status: 500, 
        headers: corsHeaders 
      });
    }
  }
};
```

**Database Schema (migrations/0001_initial.sql):**
```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  email TEXT UNIQUE NOT NULL,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE INDEX idx_users_email ON users(email);
```

---

## Example 2: AI-Powered Search with Vectorize

### Use Case
Semantic document search using embeddings and vector similarity.

### Architecture
```
Document → Workers AI (embeddings) → Vectorize → Store
                              ↓
Query → Workers AI (embeddings) → Vectorize (search) → Results
```

### Implementation

**wrangler.toml:**
```toml
name = "semantic-search"
main = "src/index.ts"

[ai]
binding = "AI"

[[vectorize]]
binding = "VECTORIZE"
index_name = "documents"
```

**src/index.ts:**
```typescript
export interface Env {
  AI: Ai;
  VECTORIZE: VectorizeIndex;
  R2: R2Bucket;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    
    // Index document
    if (url.pathname === '/index' && request.method === 'POST') {
      const { id, content, metadata } = await request.json() as {
        id: string;
        content: string;
        metadata: Record<string, string>;
      };
      
      // Generate embeddings
      const embeddings = await env.AI.run(
        '@cf/baai/bge-base-en-v1.5',
        { text: [content] }
      );
      
      // Store in vector database
      await env.VECTORIZE.upsert([{
        id,
        values: embeddings.data[0],
        metadata
      }]);
      
      return Response.json({ success: true, id });
    }
    
    // Search documents
    if (url.pathname === '/search' && request.method === 'GET') {
      const query = url.searchParams.get('q');
      if (!query) {
        return Response.json({ error: 'Query required' }, { status: 400 });
      }
      
      // Generate query embedding
      const queryEmbedding = await env.AI.run(
        '@cf/baai/bge-base-en-v1.5',
        { text: [query] }
      );
      
      // Search vectors
      const results = await env.VECTORIZE.query(queryEmbedding.data[0], {
        topK: 5,
        returnMetadata: true
      });
      
      return Response.json({
        query,
        results: results.matches.map(match => ({
          id: match.id,
          score: match.score,
          metadata: match.metadata
        }))
      });
    }
    
    return new Response('Not found', { status: 404 });
  }
};
```

---

## Example 3: Zero Trust Internal Application

### Use Case
Secure internal admin dashboard with identity-aware access.

### Architecture
```
Admin User → Cloudflare Access (Okta) → Tunnel → Internal App
                ↓
         Policy Check (group: admins)
```

### Implementation

**1. Cloudflare Tunnel Setup:**
```bash
# Install cloudflared
brew install cloudflare/cloudflare/cloudflared

# Authenticate
cloudflared tunnel login

# Create tunnel
cloudflared tunnel create admin-dashboard

# Route traffic
cloudflared tunnel route dns admin-dashboard admin.company.com
```

**2. Tunnel Configuration (~/.cloudflared/config.yml):**
```yaml
tunnel: <tunnel-id>
credentials-file: ~/.cloudflared/<tunnel-id>.json

ingress:
  - hostname: admin.company.com
    service: http://localhost:3000
    originRequest:
      connectTimeout: 30s
      tlsVerify: false
  - service: http_status:404
```

**3. Access Policy (Terraform):**
```hcl
resource "cloudflare_access_application" "admin_dashboard" {
  account_id                = var.account_id
  name                      = "Admin Dashboard"
  domain                    = "admin.company.com"
  session_duration          = "24h"
  auto_redirect_to_identity = true
}

resource "cloudflare_access_policy" "admin_policy" {
  application_id = cloudflare_access_application.admin_dashboard.id
  account_id     = var.account_id
  name           = "Admin Access"
  decision       = "allow"
  precedence     = 1

  include {
    group = [cloudflare_access_group.admins.id]
  }

  require {
    email_domain = ["company.com"]
  }
}
```

---

## Example 4: Real-time Image Processing Pipeline

### Use Case
Upload, process, and serve optimized images using R2 and Workers.

### Architecture
```
Upload → Worker → R2 (raw) → Worker (transform) → R2 (processed)
                                              ↓
                                         Cache + Serve
```

### Implementation

**src/index.ts:**
```typescript
export interface Env {
  R2_RAW: R2Bucket;
  R2_PROCESSED: R2Bucket;
  AI: Ai;
}

export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    const url = new URL(request.url);
    
    // Upload endpoint
    if (url.pathname === '/upload' && request.method === 'POST') {
      const formData = await request.formData();
      const file = formData.get('image') as File;
      
      if (!file || !file.type.startsWith('image/')) {
        return Response.json({ error: 'Invalid image' }, { status: 400 });
      }
      
      const id = crypto.randomUUID();
      const key = `uploads/${id}`;
      
      // Store original
      await env.R2_RAW.put(key, file.stream(), {
        httpMetadata: { contentType: file.type },
        customMetadata: { originalName: file.name }
      });
      
      // Process asynchronously (could use Queues)
      const imageBuffer = await file.arrayBuffer();
      const processed = await env.AI.run(
        '@cf/microsoft/resnet-50',
        { image: [...new Uint8Array(imageBuffer)] }
      );
      
      return Response.json({
        id,
        url: `/image/${id}`,
        classification: processed
      });
    }
    
    // Serve image with transformations
    const imageMatch = url.pathname.match(/^\/image\/(\w+)$/);
    if (imageMatch) {
      const id = imageMatch[1];
      const width = url.searchParams.get('w');
      const format = url.searchParams.get('format') || 'webp';
      
      // Check cache first
      const cacheKey = new Request(`https://cache/${id}?w=${width}&f=${format}`);
      const cache = caches.default;
      let response = await cache.match(cacheKey);
      
      if (!response) {
        // Fetch from R2
        const object = await env.R2_PROCESSED.get(`processed/${id}`);
        
        if (!object) {
          return new Response('Not found', { status: 404 });
        }
        
        response = new Response(object.body, {
          headers: {
            'Content-Type': `image/${format}`,
            'Cache-Control': 'public, max-age=31536000',
            'CDN-Cache-Control': 'max-age=31536000'
          }
        });
        
        // Cache for 1 year (immutable content)
        await cache.put(cacheKey, response.clone());
      }
      
      return response;
    }
    
    return new Response('Not found', { status: 404 });
  }
};
```

---

## Example 5: Distributed Rate Limiter

### Use Case
Global rate limiting using Durable Objects for coordination.

### Implementation

**src/rateLimiter.ts:**
```typescript
export class RateLimiter {
  private state: DurableObjectState;
  private requests: Map<string, number[]> = new Map();
  
  constructor(state: DurableObjectState) {
    this.state = state;
  }
  
  async fetch(request: Request): Promise<Response> {
    const url = new URL(request.url);
    const clientId = url.searchParams.get('client') || 'default';
    const limit = parseInt(url.searchParams.get('limit') || '100');
    const windowMs = parseInt(url.searchParams.get('window') || '60000');
    
    const now = Date.now();
    const windowStart = now - windowMs;
    
    // Get existing requests for this client
    let timestamps = this.requests.get(clientId) || [];
    
    // Remove old requests outside window
    timestamps = timestamps.filter(ts => ts > windowStart);
    
    // Check limit
    if (timestamps.length >= limit) {
      const retryAfter = Math.ceil((timestamps[0] + windowMs - now) / 1000);
      return new Response('Rate limit exceeded', {
        status: 429,
        headers: {
          'X-RateLimit-Limit': limit.toString(),
          'X-RateLimit-Remaining': '0',
          'X-RateLimit-Reset': (timestamps[0] + windowMs).toString(),
          'Retry-After': retryAfter.toString()
        }
      });
    }
    
    // Add current request
    timestamps.push(now);
    this.requests.set(clientId, timestamps);
    
    // Persist state
    await this.state.storage.put(`requests:${clientId}`, timestamps);
    
    return new Response('OK', {
      headers: {
        'X-RateLimit-Limit': limit.toString(),
        'X-RateLimit-Remaining': (limit - timestamps.length).toString(),
        'X-RateLimit-Reset': (now + windowMs).toString()
      }
    });
  }
}
```

**wrangler.toml:**
```toml
[[durable_objects.bindings]]
name = "RATE_LIMITER"
class_name = "RateLimiter"

[[migrations]]
tag = "v1"
new_classes = ["RateLimiter"]
```

**Usage in Worker:**
```typescript
export default {
  async fetch(request: Request, env: Env): Promise<Response> {
    // Get rate limiter instance (by IP or API key)
    const clientId = request.headers.get('CF-Connecting-IP') || 'anonymous';
    const limiterId = env.RATE_LIMITER.idFromName(clientId);
    const limiter = env.RATE_LIMITER.get(limiterId);
    
    // Check rate limit
    const check = await limiter.fetch(
      `http://internal/check?client=${clientId}&limit=100&window=60000`
    );
    
    if (check.status === 429) {
      return new Response('Too many requests', { 
        status: 429,
        headers: Object.fromEntries(check.headers)
      });
    }
    
    // Process request
    return new Response('Success');
  }
};
```
