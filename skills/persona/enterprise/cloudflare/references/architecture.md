# Cloudflare Architecture Reference

## Network Architecture

### Global Edge Network
- **330+ cities** across **125+ countries**
- **95% of Internet users** within **50ms** of a Cloudflare data center
- **78+ million HTTP requests/second** processing capacity
- Anycast network routing for automatic traffic optimization

### Points of Presence (PoP) Structure
```
┌─────────────────────────────────────────────────────────────┐
│                     CLOUDFLARE EDGE                         │
├─────────────────────────────────────────────────────────────┤
│  ┌─────────┐  ┌─────────┐  ┌─────────┐  ┌─────────┐        │
│  │  PoP 1  │  │  PoP 2  │  │  PoP 3  │  │  PoP N  │        │
│  │ (City)  │  │ (City)  │  │ (City)  │  │ (City)  │        │
│  ├─────────┤  ├─────────┤  ├─────────┤  ├─────────┤        │
│  │• CDN    │  │• CDN    │  │• CDN    │  │• CDN    │        │
│  │• WAF    │  │• WAF    │  │• WAF    │  │• WAF    │        │
│  │• Workers│  │• Workers│  │• Workers│  │• Workers│        │
│  │• GPU    │  │• GPU    │  │• GPU    │  │• GPU    │        │
│  │ (AI)    │  │ (AI)    │  │ (AI)    │  │ (AI)    │        │
│  └─────────┘  └─────────┘  └─────────┘  └─────────┘        │
└─────────────────────────────────────────────────────────────┘
                            │
                    ┌───────┴───────┐
                    │   CENTRAL     │
                    │   CORE DCs    │
                    └───────────────┘
```

## Security Architecture

### Defense Layers
1. **Edge DDoS Protection** - 187 Tbps network capacity
2. **WAF** - OWASP Core Rule Set + Cloudflare-managed rules
3. **Bot Management** - ML-based detection
4. **Zero Trust** - Identity-aware access controls

### Post-Quantum Cryptography (2024-2025)
- **ML-KEM** (Kyber) key encapsulation
- **ML-DSA** (Dilithium) digital signatures
- **Hybrid mode**: Classical + PQC running in parallel
- **X25519Kyber768** for TLS 1.3
- Full SASE platform coverage

## Developer Platform Stack

### Compute
| Service | Use Case | Latency |
|---------|----------|---------|
| Workers | Serverless functions | <1ms cold start |
| Durable Objects | Stateful coordination | Regional |
| Pages | JAMstack hosting | Global edge |

### Storage
| Service | Type | Best For |
|---------|------|----------|
| KV | Key-value | Configuration, session data |
| D1 | SQL (SQLite) | Relational data |
| R2 | Object storage | Large files, backups |
| Durable Objects | Strong consistency | State management |
| Vectorize | Vector DB | AI/ML embeddings |

### AI/ML Platform
```
┌────────────────────────────────────────────┐
│           WORKERS AI STACK                 │
├────────────────────────────────────────────┤
│  Models: Llama, Mistral, Stable Diffusion  │
│  GPUs: 180+ cities globally                │
│  Inference: Serverless, pay-per-use        │
├────────────────────────────────────────────┤
│           VECTORIZE                        │
│  - 5M vectors per index                    │
│  - 31ms median query latency               │
│  - Cosine/Euclidean metrics                │
├────────────────────────────────────────────┤
│           AI GATEWAY                       │
│  - Rate limiting                           │
│  - Caching                                 │
│  - Model fallback                          │
│  - Persistent logs                         │
└────────────────────────────────────────────┘
```

## Zero Trust Architecture (Cloudflare One)

### Components
```
                    ┌─────────────────┐
                    │   User/Device   │
                    │  (WARP Client)  │
                    └────────┬────────┘
                             │
                    ┌────────▼────────┐
                    │  Cloudflare     │
                    │     Edge        │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
┌───────▼───────┐  ┌────────▼────────┐  ┌────────▼────────┐
│    Access     │  │     Gateway     │  │     Tunnel      │
│  (Identity)   │  │ (SWG/DNS/Network)│  │   (cloudflared) │
└───────┬───────┘  └────────┬────────┘  └────────┬────────┘
        │                    │                    │
        └────────────────────┼────────────────────┘
                             │
                    ┌────────▼────────┐
                    │  Applications   │
                    │  (SaaS/Private) │
                    └─────────────────┘
```

### Identity Providers
- Okta, Azure AD, Google Workspace
- Generic OIDC/SAML 2.0
- One-time PINs
- Device certificates

## Performance Optimization Patterns

### Caching Strategy
```
Browser Cache → CDN Edge Cache → Origin Shield → Origin
     (TTL)          (TTL)           (TTL)        (Source)
```

### Smart Placement (Workers)
- **Standard**: Run at edge (closest to user)
- **Smart Placement**: Run near data source for backend-heavy workloads

## Deployment Patterns

### Blue-Green with Workers
```javascript
// Canary deployment based on headers
default: {
  async fetch(request, env) {
    const version = request.headers.get('CF-Version') || 'stable';
    
    if (version === 'beta') {
      return env.BETA_WORKER.fetch(request);
    }
    
    // A/B testing: 10% to new version
    const cookie = request.headers.get('Cookie');
    if (cookie?.includes('version=new') || Math.random() < 0.1) {
      return env.NEW_WORKER.fetch(request);
    }
    
    return env.STABLE_WORKER.fetch(request);
  }
}
```

### Multi-Region D1
```
Primary D1 (US-East) ──► Read Replicas (EU, APAC)
       │
       └──► Async replication to R2 for analytics
```

## Observability Stack

### Built-in Metrics
- **Workers Analytics**: CPU time, duration, errors
- **AI Gateway**: Request volume, token usage, latency
- **Real User Monitoring (RUM)**: Core Web Vitals

### Log Destinations
- Datadog, Splunk, AWS S3, Google Cloud Storage
- R2 (zero egress cost)
- Webhooks

## Cost Optimization

### Egress Cost Comparison
| Service | Egress Cost |
|---------|-------------|
| AWS S3 | $0.09/GB |
| Google Cloud | $0.08-0.12/GB |
| Azure Blob | $0.08-0.15/GB |
| **Cloudflare R2** | **$0** |

### Workers Pricing Tiers
| Tier | CPU Time | Requests |
|------|----------|----------|
| Free | 10ms/req | 100K/day |
| Paid | 50ms/req | 10M included |
| Enterprise | Custom | Custom |
