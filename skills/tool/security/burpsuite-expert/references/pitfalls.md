# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Quick Fix |
|---|---------|----------|--------|-----------|
| 1 | **Testing out-of-scope targets** | :red_circle: High | Legal/contract violation, blacklist | Always verify scope before testing |
| 2 | **Running active scan without permission** | :red_circle: High | Service disruption, data corruption | Use passive scanning first |
| 3 | **Not intercepting HTTPS properly** | :red_circle: High | Missing vulnerabilities | Install Burp CA cert correctly |
| 4 | **Submitting forms during scan** | :red_circle: High | Spam, data corruption | Exclude POST requests in scanner config |
| 5 | **Deleting/modifying data during scan** | :red_circle: High | Data loss, business impact | Use read-only testing mode |
| 6 | **Ignoring JavaScript-rendered content** | :yellow_circle: Medium | Missed API endpoints | Use Burp's JS analysis + browser access |
| 7 | **Not exporting project file** | :yellow_circle: Medium | Lost work | Regular saves + backup |
| 8 | **Skipping manual testing** | :yellow_circle: Medium | Logic flaws, IDORs missed | Combine scanner + manual testing |
| 9 | **Not configuring scope filters** | :yellow_circle: Medium | Wasted time, noise | Add regex exclusions |
| 10 | **Missing proxy chain issues** | :yellow_circle: Medium | Intermittent failures | Verify proxy settings |

### Legal & Scope Violations

**Common Errors:**
```markdown
:warning: NEVER do these:
├── Scan IPs not in scope (check WHOIS, DNS records)
├── Test mobile apps without explicit permission
├── Test API keys against production
├── Exfiltrate data beyond PoC
├── Leave backdoors or persistence
└── Share findings outside authorized team
```

**Pre-Engagement Checklist:**
```markdown
:clipboard: Required before any testing:
- [ ] Written scope document signed
- [ ] Bug bounty program rules reviewed (if applicable)
- [ ] Rate limits agreed upon
- [ ] Emergency contacts established
- [ ] Out-of-scope ranges identified
- [ ] Maximum scan intensity defined
- [ ] Blackout dates (if any) noted
```

## 10.2 Anti-Patterns

### Scanning Anti-Patterns

| Anti-Pattern | Description | Impact | Correct Approach |
|-------------|-------------|--------|------------------|
| **Noisy Scanning** | Running aggressive scans immediately | IDS alerts, IP block | Start with stealth: `-T2`, single probe |
| **Full Port Scan via Proxy** | Port scanning through Burp | Misses UDP, inefficient | Use nmap for network scanning |
| **Ignoring Passive Scan** | Only running active scans | Misses info leaks, timing issues | Enable + review passive findings |
| **Scanner-only Testing** | No manual testing | Logic flaws, business logic bugs | Always manual review critical flows |
| **Not Using Intruder Strategically** | Random fuzzing | Inefficient, misses targeted vulns | Target specific parameters |

### Incorrect Configuration Examples

```markdown
:warning: WRONG:
├── Proxy bound to 0.0.0.0 on shared network (others can intercept)
├── Intercept ON for entire engagement (misses background traffic)
├── No TLS downgrade testing configured
├── Scanner configured with aggressive insert points on prod
└── Ignoring SSL errors (misses cert issues)

:white_check_mark: CORRECT:
├── Proxy bound to 127.0.0.1 for local testing
├── Intercept OFF during reconnaissance (passive scan)
├── Enable TLS downgrade in project options
├── Conservative scan settings for production
├── Log and investigate SSL errors
```

### Reporting Anti-Patterns

| Anti-Pattern | Issue | Correct Approach |
|--------------|-------|------------------|
| Copy-paste scanner output | No context, hard to understand | Edit, prioritize, add business impact |
| High severity without PoC | Won't be fixed | Include exact request/response |
| No remediation guidance | Client can't fix | Add specific code fixes, config changes |
| Missing false positive flagging | Wasted developer time | Clearly mark suspected FP with reasoning |
| One-size-fits-all report | Not actionable | Executive + technical sections |

## 10.3 False Positive Management

### Reducing False Positives

```markdown
1. Always verify scanner findings manually
   - Check the exact request Burp sent
   - Verify the vulnerability exists
   - Confirm with different payloads

2. Use Insertion Point Options wisely:
   - Remove predictable parameters (session IDs, timestamps)
   - Set proper attack boundaries
   - Limit recursive scans

3. Common False Positives to Watch:
   - SSL certificate errors on internal sites
   - "Password autocomplete" on API endpoints
   - "Cache control" on dynamic APIs
   - Version info disclosure on internal tools
```

### Verification Checklist

```markdown
:clipboard: Before reporting any finding:
- [ ] Replicated the exact request
- [ ] Confirmed vulnerability with second payload
- [ ] Assessed actual impact (not theoretical)
- [ ] Checked if it's a known framework behavior
- [ ] Verified in scope
- [ ] Documented steps to reproduce
- [ ] Assessed if it requires user interaction
```

## 10.4 Performance & Resource Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Burp running slow | Large sitemap, too many history items | Use project files, limit history size |
| Out of memory | Scanning large application | Increase JVM heap, split scan |
| High CPU usage | Too many concurrent threads | Reduce threads in scanner options |
| Proxy timeouts | Target server overloaded | Add delay, reduce scan speed |
| Cannot intercept | Proxy not capturing | Check: intercept rules, scope, invisible proxy |

### Resource Optimization

```bash
# Increase Burp memory allocation
java -Xmx4g -jar burpsuite_pro.jar  # 4GB heap
java -Xmx8g -jar burpsuite_pro.jar  # 8GB heap

# Project file management
├── Save regularly: Ctrl+S
├── Use project file: .bup format
├── Archive old projects
└── Export findings separately
```
