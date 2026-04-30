# Cloudflare Security Reference

## DDoS Protection

### Network-Layer (L3/4)
- **Capacity**: 187 Tbps
- **Detection**: <3 seconds automatic detection
- **Mitigation**: Anycast-based dispersion + challenge/response
- **Protocols**: TCP, UDP, ICMP, GRE

### Application-Layer (L7)
- HTTP flood protection
- Slowloris defense
- Challenge passage (Managed Challenge, JS Challenge, Interactive)
- Custom rules for specific attack patterns

### DDoS Protection Levels
| Level | Action | Use Case |
|-------|--------|----------|
| High | Challenge all non-whitelisted | Under attack |
| Medium | Challenge suspicious | Default for free |
| Low | Challenge only threatening | Enterprise sites |
| Essentially Off | Monitor only | Testing |

## Web Application Firewall (WAF)

### Managed Rulesets
1. **Cloudflare Managed Ruleset** - 500+ rules
2. **OWASP Core Rule Set** - Industry standard
3. **Exposed Credentials Check** - Breached credential detection
4. **IP Reputation** - Known threat actors

### Custom Rules (Expression Builder)
```
# Block specific countries
(ip.geoip.country eq "XX")

# Rate limiting
(cf.threat_score > 50)

# Bot detection
(cf.bot_management.score lt 10)

# Method filtering
(http.request.method eq "POST" and http.request.uri.path eq "/admin")
```

## Zero Trust Security

### Access Policies

#### Authentication Methods
- **Identity Providers**: Okta, Azure AD, Google, GitHub, etc.
- **One-time PIN**: Email-based authentication
- **Service Tokens**: API access authentication

#### Device Posture
| Check | Description |
|-------|-------------|
| Disk Encryption | Verify FileVault/BitLocker |
| OS Version | Minimum version requirement |
| Firewall | Ensure enabled |
| Colocation | Require specific network location |
| Serial Number | Managed device list |

### Gateway Policies

#### DNS Filtering
```
Block: malware, phishing, adult_content, gambling
Allow: corporate domains
Override: custom block page
```

#### Network Firewall
- Egress filtering by IP/Port
- Protocol inspection
- Geo-blocking

#### HTTP Inspection
- TLS decryption (optional)
- Content categorization
- File type blocking
- Upload scanning

## SSL/TLS Configuration

### Encryption Modes
| Mode | Description | Security |
|------|-------------|----------|
| Off | No HTTPS | ❌ |
| Flexible | HTTPS to CF, HTTP to origin | ⚠️ |
| Full | HTTPS both ways (any cert) | ✅ |
| Full (Strict) | HTTPS with valid cert | ✅✅ |

### TLS Version Control
- Minimum TLS 1.2 (recommended)
- TLS 1.3 for best performance
- Automatic HTTPS rewrites

### Post-Quantum Cryptography

#### Current Status (2024-2025)
- **ML-KEM-768/1024**: Key exchange
- **ML-DSA-65/87**: Digital signatures
- **Hybrid mode**: X25519 + Kyber
- **Coverage**: TLS 1.3, IPsec, MASQUE

#### Migration Timeline
```
2024: Hybrid PQC available
2025: Default for all traffic
2030: NIST mandate deadline
```

## Bot Management

### Detection Signals
- **Browser integrity check**
- **JavaScript fingerprinting**
- **ML-based behavioral analysis**
- **Known bot signatures**

### Bot Scores
| Score | Classification | Action |
|-------|----------------|--------|
| 1-10 | Definitely automated | Block/Challenge |
| 11-29 | Likely automated | Challenge |
| 30-99 | Likely human | Allow |
| 100 | Verified human | Allow + Cache |

### Verified Bots
- Search engines (Google, Bing)
- Social media crawlers
- Monitoring services
- Partner integrations

## Data Loss Prevention (DLP)

### Built-in Detectors
- Credit card numbers (Luhn validation)
- Social Security Numbers
- API keys and secrets
- Source code patterns

### Custom Detectors
```yaml
# Regex-based detection
pattern: "[A-Z]{2}-\d{5}-[A-Z]{2}"
confidence: high
context: employee_id
```

### Response Actions
- Block
- Allow with log
- Redact
- Notify admin

## Security Event Logging

### Logpush Destinations
- S3-compatible storage
- Datadog
- Splunk
- Google Cloud Storage
- Azure Blob

### Log Types
- HTTP requests
- Firewall events
- DNS queries
- Access authentication
- Gateway activity

### SIEM Integration
```bash
# Splunk HEC example
curl -X POST https://splunk.example.com:8088/services/collector/event \
  -H "Authorization: Splunk <token>" \
  -d '{"event": {"action": "block", "source": "waf"}}'
```

## Compliance Certifications

### Global Standards
- **SOC 2 Type II**
- **ISO 27001/27017/27018**
- **PCI DSS Level 1**
- **GDPR compliant**
- **HIPAA eligible**

### Regional
- **EU Cloud Code of Conduct**
- **UK Cyber Essentials Plus**
- **Australian IRAP**

## Incident Response

### Security Contact
- security@cloudflare.com
- HackerOne bug bounty program
- PGP key available

### DDoS Response Playbook
1. Enable "Under Attack" mode
2. Review Security Events
3. Adjust firewall rules
4. Contact support if >10 Gbps
5. Document attack vectors

### Forensics
- Request logs via API
- Export Security Events
- Preserve evidence before TTL expires
