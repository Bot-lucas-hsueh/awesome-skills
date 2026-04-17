# Standards & Reference

## 7.1 Official Documentation

- [Cloudflare Documentation](https://developers.cloudflare.com/) — Full documentation for all Cloudflare products
- [Cloudflare Radar](https://radar.cloudflare.com/) — Internet traffic and security insights
- [Cloudflare Design Docs](https://blog.cloudflare.com/) — Architecture and engineering blog
- [Cloudflare Workers Docs](https://developers.cloudflare.com/workers/) — Serverless platform
- [Cloudflare R2 Docs](https://developers.cloudflare.com/r2/) — Object storage (S3-compatible)
- [Cloudflare D1 Docs](https://developers.cloudflare.com/d1/) — SQLite database
- [Cloudflare WAF Documentation](https://developers.cloudflare.com/waf/) — Web Application Firewall
- [Zero Trust Documentation](https://developers.cloudflare.com/cloudflare-one/) — Zero Trust Network Access
- [Cloudflare Community Forum](https://community.cloudflare.com/) — Community support

## 7.2 DNS Best Practices

### 7.2.1 DNS Record Types and Usage

| Record Type | Purpose | Common TTL |
|-------------|---------|------------|
| **A** | IPv4 address for hostname | 300-3600s |
| **AAAA** | IPv6 address for hostname | 300-3600s |
| **CNAME** | Alias to another domain | 300-3600s |
| **MX** | Mail server priority | 3600-86400s |
| **TXT** | SPF, DKIM, domain verification | 3600-86400s |
| **NS** | Nameserver delegation | 86400s |
| **SOA** | Start of Authority | 86400s |
| **SRV** | Service location | 3600s |
| **CAA** | Certification Authority Authorization | 86400s |

### 7.2.2 Cloudflare Proxy Settings

| Setting | Behavior | Use Case |
|---------|----------|----------|
| **DNS only (grey cloud)** | Direct connection, no protection | Systems requiring direct IP |
| **Proxied (orange cloud)** | Traffic through Cloudflare | Websites, web apps |
| **Stale content** | Serve cached content if origin down | High availability |

### 7.2.3 Recommended TTLs

| Record Type | TTL | Rationale |
|------------|-----|-----------|
| **A (static site)** | 86400 (24h) | Rarely changes |
| **A (load balancer)** | 300 (5min) | Ability to failover quickly |
| **CNAME (CDN)** | 300 (5min) | Cache invalidation |
| **MX** | 86400 (24h) | Low priority records |
| **TXT/SPF** | 3600 (1h) | Email verification |

## 7.3 Cloudflare Plans Comparison

### 7.3.1 Plan Features

| Feature | Free | Pro | Business | Enterprise |
|---------|------|-----|----------|------------|
| **SSL** | Full | Full | Full | Full |
| **CDN** | Basic | Advanced | Advanced | Enterprise |
| **WAF rules** | 5 | 25 | 100+ | Unlimited |
| **DDoS protection** | L3/L4 | L3/L4 | L3/L4 | L3/L4/L7 |
| **Rate limiting** | - | 10 rules | 100 rules | Custom |
| **Workers (requests/day)** | 100,000 | 1,000,000 | 10,000,000 | Unlimited |
| **Bandwidth** | Unlimited | Unlimited | Unlimited | Unlimited |

### 7.3.2 SSL/TLS Modes

| Mode | Security | Compatibility |
|------|----------|---------------|
| **Off (not secure)** | None | Legacy systems only |
| **Flexible** | Partial | Not recommended |
| **Full** | Encrypted both sides | Default for most |
| **Full (strict)** | Encrypted + origin cert | Production |
| **Origin Server** | Origin-only encryption | Internal services |

## 7.4 WAF and Security Best Practices

### 7.4.1 OWASP Top 10 Protection

Cloudflare WAF includes rulesets for:
1. SQL Injection
2. XSS (Cross-Site Scripting)
3. Local File Inclusion
4. Remote File Inclusion
5. Command Injection

### 7.4.2 Rate Limiting Rules

```json
{
  "description": "Block excessive requests",
  "expression": "(http.request.uri.path contains \"/api/\")",
  "ratelimit": {
    "requests_per_period": 100,
    "period": 60,
    "response_code": 429,
    "action": "block",
    "mitigation_timeout": 300
  }
}
```

### 7.4.3 Security Headers

| Header | Recommended Value |
|--------|-------------------|
| **Strict-Transport-Security** | `max-age=31536000; includeSubDomains; preload` |
| **X-Content-Type-Options** | `nosniff` |
| **X-Frame-Options** | `SAMEORIGIN` |
| **Referrer-Policy** | `strict-origin-when-cross-origin` |
| **Permissions-Policy** | `geolocation=(self)` |

## 7.5 Cloudflare Workers Architecture

### 7.5.1 Workers vs Pages

| Feature | Workers | Pages |
|---------|---------|-------|
| **Runtime** | V8 isolates | V8 + Edge runtime |
| **Use case** | API, middleware, compute | Static sites, SSR |
| **Cold start** | <5ms | <200ms |
| **Pricing** | Requests + CPU time | Bandwidth + builds |

### 7.5.2 Workers KV vs D1 vs Durable Objects

| Product | Type | Use Case | Consistency |
|---------|------|----------|-------------|
| **Workers KV** | Key-Value Store | Caching, config | Eventually consistent |
| **D1** | SQLite Database | Relational data | Strong consistency |
| **Durable Objects** | Stateful Objects | Real-time, coordination | Strong consistency |

## 7.6 Zone and Domain Management

### 7.6.1 Cloudflare API Base URL

```
https://api.cloudflare.com/client/v4
```

### 7.6.2 Common API Endpoints

| Endpoint | Method | Purpose |
|----------|--------|---------|
| `/zones` | GET/POST | List/create zones |
| `/zones/{zone_id}/dns_records` | GET/POST | Manage DNS records |
| `/zones/{zone_id}/purge_cache` | POST | Purge cache |
| `/zones/{zone_id}/firewall/rules` | GET/POST | Firewall rules |
| `/accounts/{account_id}/workers/scripts` | GET/POST | Workers scripts |
