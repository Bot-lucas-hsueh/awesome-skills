# Standard Workflow

## 8.1 Reconnaissance & Enumeration Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: Passive Reconnaissance                                  │
├─────────────────────────────────────────────────────────────────┤
│ 1. Configure Burp proxy with upstream if needed                  │
│ 2. Set scope - include only authorized targets                   │
│ 3. Enable "Do not send items to history" for off-scope          │
│ 4. Browse target application manually                            │
│ 5. Use Burp's Target > Site map for crawl starting point        │
│ 6. Right-click host -> "Spider from here"                        │
│ 7. Review discovered URLs, parameters, hidden forms              │
│    - Check Engagement Tools > Analyze Target                     │
│    - Review Site map for interesting paths                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: Active Enumeration                                      │
├─────────────────────────────────────────────────────────────────┤
│ 1. Run Burp Scanner (Professional)                               │
│    - Passive scan runs continuously                              │
│    - Schedule active scan during off-peak                        │
│ 2. Use Target > Discover Content                                 │
│    - Directory brute forcing                                     │
│    - File extension enumeration                                  │
│ 3. Identify:                                                     │
│    - Authentication endpoints                                    │
│    - Admin panels                                                │
│    - API endpoints (/api/v1, /rest, /graphql)                   │
│    - File upload points                                          │
│    - Parameterized URLs                                         │
│ 4. Document all discovered endpoints                             │
└─────────────────────────────────────────────────────────────────┘
```

## 8.2 Scanning Methodology

### Web Application Testing Methodology

```
Step 1: Baseline Traffic Capture
├── Browse application with proxy intercept ON
├── Capture all requests/responses
├── Enable "Intercept client requests" for key requests
└── Review raw traffic for hidden headers/values

Step 2: Passive Scanning
├── Continue browsing while Burp passively scans
├── Review: Proxy > HTTP History > Filter by issues
├── Check Scanner > Queue for passive findings
└── Export passive scan results

Step 3: Crawl & Discovery
├── Target > Spider: Full application crawl
├── Target > Discover Content: Brute force dirs/files
├── Review Site map > Filter by content type
└── Identify: login, admin, api, file upload pages

Step 4: Active Scanning (with permission!)
├── Right-click branch -> "Actively scan this branch"
├── Configure scan: 
│   ├── Remove certain insert points (IDs, tokens)
│   ├── Exclude Form Submission for critical actions
│   └── Set rate limit to avoid DoS
├── Monitor: Scanner > Results queue
└── Review findings by severity

Step 5: Targeted Testing
├── Repeater: Manual testing of specific endpoints
├── Intruder: Parameter fuzzing, credential stuffing
├── Decoder: Base64, URL encoding, hex conversion
└── Sequencer: Token randomness analysis
```

### Scope Definition Best Practice

```markdown
IN SCOPE:
  ^https?://target\.com/.*
  ^https?://api\.target\.com/.*
  ^https?://staging\.target\.com/.*

OUT OF SCOPE:
  ^https?://target\.com/logout.*
  ^https?://target\.com/privacy.*
  ^https?://target\.com/terms.*
  \.png$\|\.jpg$\|\.gif$\|\.css$\|\.js$
```

## 8.3 Reporting Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ REPORTING PHEDULE                                               │
├─────────────────────────────────────────────────────────────────┤
│ DAILY:                                                          │
│ - Sync findings with team (Burp sync or report share)           │
│ - Update issue tracker with new findings                        │
│ - Mark duplicates/false positives                               │
│                                                                  │
│ WEEKLY:                                                         │
│ - Review all findings for accuracy                               │
│ - Update severity if new context discovered                      │
│ - Draft weekly status summary                                   │
│                                                                  │
│ END OF ENGAGEMENT:                                              │
│ - Generate final report                                          │
│ - Review with client                                            │
│ - Provide remediation guidance                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Report Generation (Burp Professional)

```markdown
1. Scanner > Reported Items
2. Filter by scope, severity, type
3. Select items to include
4. Click "Report selected issues"
5. Configure:
   - Format: HTML, PDF, DOCX, XML
   - Include: Executive summary, remediation, screenshots
   - Exclude: Informational, low severity (as needed)
6. Custom template if available
```

### Custom Report Template Structure

```markdown
# Vulnerability Report Template

## Executive Summary
- Total findings: X Critical, Y High, Z Medium, N Low
- Overall risk assessment
- Top priorities

## Methodology
- Testing scope
- Tools used
- Timeline

## Findings (by severity)
### CRITICAL
- Title, Description, Steps to Reproduce
- Impact, Evidence (burp screenshot)
- Remediation, References

### HIGH
... (same structure)

## Appendices
- Raw scan output
- Traffic logs
- Scope confirmation
```

### Issue Tracker Integration

| Tool | Integration Method |
|------|-------------------|
| JIRA | Burp Enterprise: webhook or API sync |
| Linear | Export to CSV, manual import |
| GitHub Issues | Burp Extension: github-issue-creator |
| DefectDojo | API import/export |
| Custom DB | XML/JSON export, custom script |

### Remediation Tracking

```markdown
| Finding | Status | Assigned To | Due Date | Verified |
|---------|--------|-------------|----------|----------|
| SQL Injection in /api/search | Open | Dev Team | 2024-02-01 | No |
| XSS in comment field | In Progress | Frontend | 2024-01-30 | No |
| CSRF on admin forms | Remediated | DevOps | 2024-01-25 | Yes |
```
