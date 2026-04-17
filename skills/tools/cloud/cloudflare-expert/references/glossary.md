# Glossary

## DNS & Network

| Term | Definition |
|------|------------|
| **Zone** | Domain namespace managed by Cloudflare |
| **Proxy Status** | DNS-only (grey cloud) vs Proxied (orange cloud) |
| **Anycast** | Multiple data centers serving same IP |
| **NS** | Nameserver delegation |
| **CNAME Flattening** | Resolve CNAME to A at root domain |
| **DNSSEC** | DNS signing for authenticity |

## SSL/TLS

| Term | Definition |
|------|------------|
| **Full (strict)** | Encrypted end-to-end with valid cert |
| **Full** | Encrypted, no origin cert validation |
| **Flexible** | HTTPS between user and Cloudflare only |
| **Origin Server** | Encryption at origin only |
| **Authenticated Origin Pulls** | Verify Cloudflare as client |
| **Custom Certificate** | Upload your own SSL |

## Performance

| Term | Definition |
|------|------------|
| **Argo Smart Routing** | Route via less congested paths |
| **Railgun** | Compression for dynamic content |
| **Brotli** | Compression algorithm |
| **HTTP/2** | Multiplexed connections |
| **HTTP/3** | QUIC-based protocol |
| **Early Hints** | Preload hints before response |

## Security

| Term | Definition |
|------|------------|
| **WAF** | Web Application Firewall |
| **Rate Limiting** | Request throttling |
| **Bot Fight Mode** | Challenge suspicious bots |
| **Challenge** | Browser challenge page |
| **JS Challenge** | JavaScript verification |
| **Cloudflare DDoS** | Layer 3/4/7 protection |
| **IP Reputation** | Threat score database |

## Workers & Edge

| Term | Definition |
|------|------------|
| **Workers** | Serverless JavaScript execution |
| **Durable Objects** | Stateful edge computing |
| **Workers KV** | Key-value storage at edge |
| **D1** | SQLite at edge |
| **R2** | S3-compatible object storage |
| **Pages** | Static site hosting |

## Access & Zero Trust

| Term | Definition |
|------|------------|
| **Access** | Zero Trust network access |
| **Tunnel** | Secure connection to origin |
| **Gateway** | Secure web gateway |
| **WARP** | Client for Zero Trust |
| **IdP** | Identity Provider |

## Analytics & Logs

| Term | Definition |
|------|------------|
| **Firewall Events** | Blocked/threat requests |
| **Analytics** | Traffic, bandwidth, requests |
| **Logs** | HTTP request logs |
| **Heartbeat** | Origin health monitoring |

## Caching

| Term | Definition |
|------|------------|
| **Cache Level** | Cache behavior settings |
| **Edge Cache TTL** | Time at Cloudflare |
| **Browser Cache TTL** | Time in browser |
| **Cache Tag** | Custom purge identifiers |
| **Surrogate Key** | Cache grouping |