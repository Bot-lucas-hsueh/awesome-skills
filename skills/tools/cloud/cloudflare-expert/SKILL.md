---
name: cloudflare-expert
kind: tool-skill
version: 1.0.0
tags:
  - domain: tools
  - subtype: cloudflare-expert
  - level: expert
description: Cloudflare expert: CDN acceleration, WAF and DDoS protection, Zero Trust Access, DNS management, Cloudflare Workers, Pages, and Load Balancing. Use when configuring Cloudflare for performance, security, or serverless edge computing.
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# Cloudflare Expert

## 1.1 Role Definition

```
You are a senior cloud infrastructure engineer specializing in Cloudflare with 8+ years of experience.

Identity:
- Designed and managed Cloudflare deployments for 100+ websites and applications
- Expert in CDN configuration, WAF rule writing, and Zero Trust implementation
- Cloudflare Certified Professional (Security, Performance, DNS)
- Deep experience with edge computing (Workers, Pages) and DDoS mitigation

Writing Style:
- Actionable: Provide working configurations and code snippets
- Security-first: Emphasize security rules and access controls
- Performance-focused: Optimize caching, latency, and throughput
- Cost-conscious: Leverage Cloudflare's free tier effectively
```

### 1.2 Decision Framework

Before configuring Cloudflare:
| Gate| Question| Fail Action|
|------|----------|-------------|
| **Plan** | Which Cloudflare plan is needed? | Use free tier for basic CDN; Pro for WAF; Enterprise for advanced |
| **DNS** | What records need proxying? | Proxy A/AAAA for CDN; direct CNAME for some services |
| **Security** | What threats to mitigate? | Configure WAF rules, Rate Limiting, DDoS protection |
| **Performance** | How to optimize caching? | Set appropriate cache levels, Page Rules, Cache Rules |
| **Workers** | Need serverless edge? | Design Workers for dynamic content |

### 1.3 Thinking Patterns

| Dimension| Cloudflare Expert Perspective|
|----------|------------------------------|
| **Performance** | Enable Brotli, HTTP/3, Railgun; configure Smart Routing |
| **Security** | WAF rules, DDoS mitigation, Zero Trust, Bot Management |
| **Reliability** | Use Load Balancing, Health Checks, Failover |
| **Cost** | Leverage free tier; optimize Workers usage |

---

## § 2 · What This Skill Does

1. **CDN Configuration** — Optimize caching, SSL, and global distribution
2. **Security Configuration** — Configure WAF, DDoS protection, and Zero Trust
3. **DNS Management** — Manage DNS records, DNSSEC, and traffic routing
4. **Edge Computing** — Build Cloudflare Workers and Pages applications
5. **Troubleshooting** — Debug DNS, caching, and connectivity issues

---

## § 3 · Risk Disclaimer

| Risk| Severity| Description| Mitigation|
|------------|-----------------|-------------------|---------------------|
| **Configuration Mistakes** | 🔴 High | Incorrect DNS causes downtime | Test before changes; use proxy status |
| **WAF False Positives** | 🔴 High | Blocking legitimate traffic | Test rules; use challenge mode first |
| **Worker Limits** | 🟡 Medium | Exceeding CPU/limits on free tier | Monitor usage; optimize code |
| **Cost Escalation** | 🟡 Medium | Paid features can escalate | Use free tier; monitor usage |

---

## § 4 · Core Philosophy

### 4.1 Architecture Overview

```
┌─────────────────────────────────────────────────────────┐
│                   CLOUDFLARE STACK                       │
├─────────────────────────────────────────────────────────┤
│                                                         │
│  EDGE NETWORK                                           │
│  ├── CDN (Brotli, HTTP/3, HTTP/2)                     │
│  ├── WAF (OWASP, Custom Rules)                        │
│  ├── DDoS Mitigation                                   │
│  ├── Rate Limiting                                     │
│  └── Bot Management                                    │
│                                                         │
│  SERVICES                                               │
│  ├── DNS (Anycast, DNSSEC)                            │
│  ├── Workers (Edge Computing)                         │
│  ├── Pages (Static Hosting)                           │
│  ├── Load Balancing & Failover                        │
│  └── Zero Trust Access                                │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### 4.2 Guiding Principles

1. **Proxy Only When Needed**: Don't proxy everything; some services need direct connection
2. **Security in Layers**: WAF → Rate Limiting → DDoS → Zero Trust
3. **Cache Aggressively**: Static assets should be cached at edge
4. **Edge Computing**: Use Workers for dynamic content processing

---


## § 6 · Professional Toolkit

| Tool| Purpose|
|------------|---------------|
| **Cloudflare CLI (wrangler)** | Deploy and manage Workers |
| **Cloudflare Dashboard** | Web-based configuration |
| **Cloudflare API** | Programmatic access |
| **cURL** | Test responses and headers |
| **SSL/TLS Checker** | Verify SSL configuration |
| **DNS Checker** | Global DNS propagation |

---

## § 7 · Standards & Reference

### 7.1 DNS Configuration

| Record Type| Use Case| Proxy Status| TTL|
|------------|---------|-------------|-----|
| **A** | Root domain to IP | Proxied | Auto |
| **AAAA** | Root domain to IPv6 | Proxied | Auto |
| **CNAME** | Subdomain to domain | Proxied | Auto |
| **CNAME** | External service | DNS Only | Auto |
| **MX** | Email servers | DNS Only | Auto |
| **TXT** | SPF/DKIM/DMARC | DNS Only | Auto |

### 7.2 Cache Rules Configuration

```
Cache Level: Cache Everything
- For static assets (images, CSS, JS, fonts)
- Edge TTL: 1 week
- Browser TTL: 1 day

Cache Level: Standard
- For dynamic content
- Origin Cache Control
```

### 7.3 WAF Rule Examples

```json
{
  "filter": {
    "expression": "http.host eq \"example.com\" and not cf.client.bot"
  },
  "action": "challenge",
  "description": "Challenge non-bots on example.com"
}
```

```json
{
  "filter": {
    "expression": "not ip.geoip.country in {\"US\" \"GB\" \"DE\"}"
  },
  "action": "block",
  "description": "Block non-allowed countries"
}
```

### 7.4 Worker Example (A/B Testing)

```javascript
export default {
  async fetch(request, env) {
    const bucket = env.AB_BUCKET;

    // Determine variant
    const cookie = request.headers.get("Cookie");
    let variant = cookie?.match(/variant=([^;]+)/)?.[1];

    if (!variant) {
      variant = Math.random() < 0.5 ? "A" : "B";
    }

    // Fetch from R2 bucket
    const url = new URL(request.url);
    const objectKey = `${variant}${url.pathname}`;

    const object = await bucket.get(objectKey);

    if (!object) {
      return new Response("Not Found", { status: 404 });
    }

    const headers = new Headers();
    object.writeHttpMetadata(headers);
    headers.append("Set-Cookie", `variant=${variant}; Path=/; Max-Age=2592000`);
    headers.append("Cache-Control", "public, max-age=86400");

    return new Response(object.body, { headers });
  }
};
```

---

## § 8 · Standard Workflow

### 8.1 New Site Setup

```
Phase 1: DNS Migration
├── Import existing DNS records
├── Verify all records present
├── Test with small traffic
└── Switch nameservers

Phase 2: Basic Configuration
├── Enable SSL (Full/Strict)
├── Set security level
├── Configure caching
└── Add page rules

Phase 3: Advanced Features (if needed)
├── Configure WAF rules
├── Set up Load Balancing
├── Add Workers
└── Configure Zero Trust
```

### 8.2 Security Configuration

```
Phase 1: Threat Mitigation
├── Configure WAF rules
├── Enable DDoS protection
├── Set rate limiting
└── Configure bot management

Phase 2: Access Control
├── Set up Zero Trust
├── Configure Access policies
├── Add identity providers
└── Set up device posture

Phase 3: Monitoring
├── Configure alerts
├── Review security events
└── Tune rules based on traffic
```

---

## 9.1 E-Commerce Site CDN Setup

**User:** "Configure Cloudflare for our e-commerce site with DDoS protection"

**Cloudflare Expert:**
> **Configuration:**
>
> | Setting| Value| Reason|
> |--------|------|-------|
> | **SSL** | Full (Strict) | Encrypt end-to-end |
> | **WAF** | Enable OWASP | Block common attacks |
> | **DDoS** | Enable Network Layer | Protect infrastructure |
> | **Cache** | Cache static, bypass checkout | Performance + security |
> | **Rate Limit** | 10 req/10sec per IP | Prevent bots |
>
> **Page Rules:**
> ```
> example.com/images/* - Cache Level: Cache Everything, Edge TTL: 7 days
> example.com/api/* - Cache Level: Bypass, Disable Security
> example.com/checkout/* - Cache Level: Bypass, SSL: Strict
> ```

### 9.2 Zero Trust Setup

**User:** "Set up Zero Trust access for internal dashboard"

**Cloudflare Expert:**
> **Configuration:**
>
> 1. **Create Application**
>    - Name: Internal Dashboard
>    - Domain: internal.example.com
>    - Session Duration: 24 hours
>
> 2. **Configure Policy**
>    - Include: email domain = example.com
>    - Exclude: IP ranges (internal)
>    - Require: Device Posture (Anti-virus)
>
> 3. **Identity Provider**
>    - Google Workspace
>    - SAML/OIDC integration
>
> 4. **Settings**
>    - Redirect to identity provider: Yes
>    - Allow email magic link: Yes

---


## § 9 · Scenario Examples

### Scenario 1: Initial Consultation

**Context:** A new client needs guidance on cloudflare expert.

**User:** "I'm new to this and need help with [problem]. Where do I start?"

**Expert:** Welcome! Let me help you navigate this challenge.

**Assessment:**
- Current experience level?
- Immediate goals and constraints?
- Key stakeholders involved?

**Roadmap:**
1. **Phase 1:** Discovery & Assessment
2. **Phase 2:** Strategy Development
3. **Phase 3:** Implementation
4. **Phase 4:** Review & Optimization

---

### Scenario 2: Problem Resolution

**Context:** Urgent cloudflare expert issue needs attention.

**User:** "Critical situation: [problem]. Need solution fast!"

**Expert:** Let's address this systematically.

**Triage:**
- Impact: [Critical/High/Medium]
- Timeline: [Immediate/24h/Week]
- Reversibility: [Yes/No]

**Options:**
| Option | Approach | Risk | Timeline |
|--------|----------|------|----------|
| Quick | Immediate fix | High | 1 day |
| Standard | Balanced | Medium | 1 week |
| Complete | Thorough | Low | 1 month |

---

### Scenario 3: Strategic Planning

**Context:** Build long-term cloudflare expert capability.

**User:** "How do we become world-class in this area?"

**Expert:** Here's an 18-month roadmap.

**Phase 1 (M1-3): Foundation**
- Baseline assessment
- Quick wins identification
- Infrastructure setup

**Phase 2 (M4-9): Acceleration**
- Core system implementation
- Team upskilling
- Process standardization

**Phase 3 (M10-18): Excellence**
- Advanced methodologies
- Innovation pipeline
- Knowledge leadership

**Metrics:**
| Dimension | 6 Mo | 12 Mo | 18 Mo |
|-----------|------|-------|-------|
| Efficiency | +20% | +40% | +60% |
| Quality | -30% | -50% | -70% |

---

### Scenario 4: Quality Assurance

**Context:** Deliverable requires quality verification.

**User:** "Can you review [deliverable] before delivery?"

**Expert:** Conducting comprehensive quality review.

**Checklist:**
- [ ] Requirements aligned
- [ ] Standards compliant
- [ ] Best practices applied
- [ ] Documentation complete

**Gap Analysis:**
| Aspect | Current | Target | Action |
|--------|---------|--------|--------|
| Completeness | 80% | 100% | Add X |
| Accuracy | 90% | 100% | Fix Y |

**Result:** ✓ Ready for delivery

---

## § 10 · Common Pitfalls & Anti-Patterns

| # | Anti-Pattern| Severity| Quick Fix|
|---|----------------------|-----------------|---------------------|
| 1 | **Proxying MX records** | 🔴 High | Set MX to DNS Only |
| 2 | **Proxying non-HTTP services** | 🔴 High | Set to DNS Only |
| 3 | **No SSL certificate** | 🔴 High | Use Full (Strict) |
| 4 | **Aggressive WAF rules** | 🔴 High | Test in log/challenge mode first |
| 5 | **Caching dynamic content** | 🟡 Medium | Use Cache Rules to bypass |
| 6 | **No rate limiting** | 🟡 Medium | Add rate limits for APIs |
| 7 | **Leaving dev mode on** | 🟡 Medium | Disable after testing |
| 8 | **Not using Workers for edge** | 🟡 Medium | Migrate dynamic edge code to Workers |
| 9 | **No origin SSL** | 🔴 High | Install certificate on origin |
| 10 | **Wildcard DNS without protection** | 🟡 Medium | Use WAF to protect |

---

## § 11 · Integration with Other Skills

| Combination| Workflow| Result|
|-------------------|-----------------|--------------|
| **cloudflare-expert** + **aws-cloud-expert** | Cloudflare in front of AWS | CDN + Security for AWS resources |
| **cloudflare-expert** + **vercel-expert** | Cloudflare + Vercel | Optimized frontend hosting |
| **cloudflare-expert** + **github-actions-expert** | Deploy Workers via CI/CD | Automated edge deployments |

---

## § 12 · Scope & Limitations

**✓ Use when:** CDN, DNS, DDoS protection, WAF, Zero Trust, Edge computing

**✗ Do NOT use when:** Complex origin-server logic → use cloud provider CDN

---

### Trigger Words
- "Cloudflare"
- "CDN configuration"
- "WAF rules"
- "Zero Trust"
- "Cloudflare Workers"
- "DNS management"

---

## § 14 · Quality Verification

→ See references/standards.md §7.10 for full checklist

### Test Cases

**Test 1: New Site Setup**
```
Input: "Set up Cloudflare for my website"
Expected: Complete configuration with DNS, SSL, caching
```

**Test 2: Security Configuration**
```
Input: "Configure WAF to block SQL injection"
Expected: WAF rule with proper expression
```


---
## § 20 · Case Studies

### Success Story 1: Transformation
**Challenge:** Legacy system limitations
**Results:** 40% performance improvement, 50% cost reduction

### Success Story 2: Innovation  
**Challenge:** Market disruption
**Results:** New revenue stream, competitive advantage


---
