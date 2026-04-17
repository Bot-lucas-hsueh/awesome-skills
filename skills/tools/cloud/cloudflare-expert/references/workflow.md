# Troubleshooting Guide

## 8.1 Common Cloudflare Errors and Fixes

### 8.1.1 DNS Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `ERR_CONNECTION_REFUSED` | Origin not reachable | Check origin server, firewall |
| `ERR_NAME_NOT_RESOLVED` | DNS not propagated | Check DNS settings, wait for propagation |
| `ERR_SSL_VERSION_INTERFERENCE` | SSL handshake failed | Check SSL mode, origin cert |
| `Error 520** | Origin returned invalid/empty response | Check origin server logs |
| `Error 521** | Cloudflare cannot reach origin | Check origin firewall, Cloudflare IPs |
| `Error 522** | Connection timed out | Check origin connectivity, firewall |
| `Error 523** | Origin unreachable | Check origin is online |
| `Error 524** | Origin timeout | Check origin application, increase timeout |

### 8.1.2 SSL/TLS Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `ERR_SSL_PROTOCOL_ERROR` | TLS handshake failed | Check SSL mode, cipher compatibility |
| `SSL_ERROR_NO_CYPHER_OVERLAP` | No matching cipher | Enable modern ciphers |
| `MOZILLA_PKIX_ERROR_MITM_DETECTED` | MITM proxy detected | Check corporate proxy |
| `Invalid CSR** | Certificate signing request invalid | Regenerate CSR |
| `Too Many Requests** | Rate limited | Wait, check API usage |

### 8.1.3 Worker Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `Worker CPU time limit exceeded` | Script used too much CPU | Optimize code, reduce complexity |
| `Worker exceeded memory limit` | Script used >128MB | Optimize memory usage |
| `Worker invocation rate limit` | Too many concurrent workers | Queue requests |
| `Workers runtime error` | Uncaught exception | Check worker logs |

### 8.1.4 Cache Errors

| Error Code | Meaning | Fix |
|------------|---------|-----|
| `Cache MISS` | Page not in cache | Normal for first request |
| `Cache BYPASS` | Bypass cache header set | Check cache headers |
| `Stale content** | Origin down, serving stale | Normal during origin issues |

## 8.2 Diagnostic Tools

### 8.2.1 Cloudflare Diagnostics

| Tool | Purpose |
|------|---------|
| **Cloudflare Radar** | Global traffic and performance insights |
| **dig command** | Check DNS resolution |
| **Traceroute/MTR** | Path analysis to origin |
| **SSL Lab's SSL Test** | SSL configuration check |
| **Cloudflare Check** | Propagation and SSL status |

### 8.2.2 Diagnostic Commands

```bash
# DNS lookup with Cloudflare
dig example.com +short

# Check Cloudflare IPs
dig +short cloudflare.com A

# Trace route to origin
traceroute origin.example.com

# Test SSL configuration
openssl s_client -connect example.com:443 -tls1_3

# Check cache status headers
curl -I https://example.com

# Purge specific file via API
curl -X POST "https://api.cloudflare.com/client/v4/zones/{zone_id}/purge_cache" \
  -H "Authorization: Bearer {token}" \
  -H "Content-Type: application/json" \
  --data '{"files":["https://example.com/style.css"]}'
```

### 8.2.3 Cloudflare Analytics

```bash
# Get zone analytics via API
curl "https://api.cloudflare.com/client/v4/zones/{zone_id}/analytics/dashboard" \
  -H "Authorization: Bearer {token}"

# Get worker metrics
curl "https://api.cloudflare.com/client/v4/accounts/{account_id}/workers/analytics" \
  -H "Authorization: Bearer {token}"
```

## 8.3 Common Debugging Workflows

### 8.3.1 "Site Not Loading" Debug

```
1. Check Cloudflare Status (dash.cloudflare.com)
2. Use cloudflarediag.com for DNS check
3. Temporarily disable proxy (grey cloud)
4. Check origin server directly
5. Review Firewall Events log
6. Check SSL/TLS mode
7. Verify DNS records are correct
```

### 8.3.2 "SSL Certificate Error" Debug

```
1. Verify origin certificate is valid and not expired
2. Check SSL/TLS mode is Full or Full (strict)
3. Ensure origin uses valid hostname
4. Check for mixed content issues
5. Use SSL Lab's SSL Test for diagnostics
6. Verify CAA records if set
```

### 8.3.3 "Slow Performance" Debug

```
1. Check Cloudflare Analytics for traffic patterns
2. Enable caching for static assets
3. Review Cache Hit Ratio
4. Check for uncached dynamic content
5. Enable Polish and Mirage for images
6. Consider enabling HTTP/2 or HTTP/3
7. Review Workers performance
```

## 8.4 Cloudflare API Debugging

### 8.4.1 Common API Errors

| Status Code | Meaning | Fix |
|-------------|---------|-----|
| `400` | Bad Request | Check request body, parameters |
| `401` | Unauthorized | Verify API token |
| `403` | Forbidden | Check permissions, zone access |
| `429` | Rate Limited | Back off, respect headers |
| `500` | Server Error | Retry, contact support |

### 8.4.2 Verify API Token

```bash
# Test API token
curl -H "Authorization: Bearer {token}" \
  "https://api.cloudflare.com/client/v4/user/tokens/verify"

# Response should include:
# {"result": {"status": "active"}, ...}
```

## 8.5 Zero Trust Troubleshooting

### 8.5.1 Access Policy Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Cannot access application | Policy blocking | Review Access policies |
| Infinite redirect | IdP misconfiguration | Check IdP settings |
| Certificate error | mTLS not configured | Add client certificate |
| Session expires quickly | Short session duration | Adjust session settings |

### 8.5.2 WARP Client Issues

| Issue | Fix |
|-------|-----|
| Cannot connect | Check network, reinstall WARP |
| DNS leaks | Verify DNS settings in WARP |
| Split tunnel issues | Configure split tunnel routes |
| Authentication loops | Clear WARP cache, re-authenticate |

## 8.6 Support Resources

### 8.6.1 Cloudflare Support Tiers

| Plan | Support | SLA |
|------|---------|-----|
| **Free** | Community, docs | No SLA |
| **Pro** | Email support | 24hr response |
| **Business** | Email + chat | 4hr response |
| **Enterprise** | Dedicated support | Custom SLA |

### 8.6.2 Getting Help

1. **Cloudflare Community** — community.cloudflare.com
2. **Developer Docs** — developers.cloudflare.com
3. **Cloudflare Blog** — blog.cloudflare.com
4. **Support Ticket** — Create via dashboard (Pro+)
5. **Enterprise Support** — Dedicated team

### 8.6.3 Status Pages

- [Cloudflare Status](https://www.cloudflarestatus.com/)
- [Cloudflare History](https://www.cloudflarestatus.com/history)
