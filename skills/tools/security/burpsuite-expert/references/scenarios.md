# Scenario Examples

## 9.1 CTF & Training Scenarios

### Setting Up a Lab Environment

**User:** "I want to practice web app testing - where do I start?"

**Expert:**
> **Recommended Training Platforms:**
>
> 1. **OWASP WebGoat** - `java -jar webgoat-server-2023.4.jar`
>    - Start: `http://localhost:8080/WebGoat`
>    - Configure Burp proxy: `127.0.0.1:8080`
>
> 2. **DVWA (Damn Vulnerable Web App)**
>    - Docker: `docker run -d -p 80:80 vulnerables/web-dvwa`
>    - Set Burp proxy for browser
>
> 3. **Juice Shop** - `docker run -p 3000:3000 bkimminich/juice-shop`
>    - Modern vulnerabilities, gamified challenges
>
> 4. **PortSwigger Academy Labs**
>    - Built-in browser with proxy pre-configured
>    - Walkthrough guides available

**Workflow:**
```bash
# 1. Configure browser proxy
about:preferences -> Network Settings -> Manual proxy
  HTTP Proxy: 127.0.0.1
  Port: 8080
  Check: Use this proxy for all protocols

# 2. Install Burp's CA cert (for HTTPS testing)
# In Burp: Proxy -> Options -> Import/export CA certificate
# Install in browser: Settings -> Certificates -> Authorities

# 3. Practice workflow
- Intercept: Proxy -> Intercept ON
- Modify: Change parameters in request
- Forward: Send modified request
- Analyze: Check response for changes
```

### Learning SQL Injection

**User:** "How do I practice SQL injection detection with Burp?"

**Expert:**
> **Lab: PortSwigger SQL Injection Lab**
>
> 1. Navigate to SQL injection lab in browser
> 2. Burp intercepts the request
> 3. Example request:
>    ```http
>    GET /filter?category=Gifts HTTP/1.1
>    Host: vulnerable-site.com
>    ```
> 4. Send to Repeater (Ctrl+R)
> 5. Test payloads:
>    - `Gifts' OR '1'='1` (classic OR)
>    - `Gifts' UNION SELECT NULL--` (UNION-based)
>    - `Gifts' WAITFOR DELAY '00:00:05'--` (time-based blind)
> 6. Use Intruder for batch testing:
>    - Add positions around the parameter
>    - Load SQL injection wordlist
>    - Analyze responses for differences

## 9.2 Bug Bounty Workflow

### Reconnaissance-First Approach

**User:** "How do I efficiently test bug bounty targets with Burp?"

**Expert:**
> **Bug Bounty Workflow:**
>
> 1. **Scope Definition**
>    - Download BB scope (HackerOne, Bugcrowd)
>    - Configure Burp Project scope
>
> 2. **Passive Recon**
>    - Browse all in-scope domains
>    - Let passive scan run
>    - Use `site:target.com` Google dorking
>
> 3. **Active Crawling**
>    - Spider all discovered paths
>    - Use Discover Content for fuzzing
>    - Map API endpoints
>
> 4. **Targeted Testing**
>    ```markdown
>    | Endpoint Type | Testing Focus |
>    |--------------|---------------|
>    | /api/* | Auth bypasses, IDOR |
>    | /admin/* | Auth bypass, path traversal |
>    | /upload/* | File upload vulnerabilities |
>    | /search?q= | XSS, SQLi, SSRF |
>    | /redirect?url= | Open redirect |
>    | /graphql | GraphQL injection, introspection |
>    ```
>
> 5. **Automation**
>    - Use Burp Scanner for initial sweep
>    - Manual testing for high-value targets
>    - Note: Some programs prohibit active scanning - check rules!

### Authentication Testing Workflow

**User:** "How do I test authentication mechanisms thoroughly?"

**Expert:**
> **Authentication Testing Checklist:**
>
> ```markdown
> 1. Login Function
>    - SQL injection: admin'--
>    - Password brute force (Intruder)
>    - Username enumeration
>    - Missing rate limiting
>
> 2. Session Management
>    - Cookie attributes (HttpOnly, Secure, SameSite)
>    - Session fixation
>    - Session prediction (use Sequencer)
>    - Logout functionality
>
> 3. Password Features
>    - Password reset token predictability
>    - Forgot password email injection
>    - Weak password policies
>
> 4. Multi-Factor Auth
>    - 2FA bypass techniques
>    - OTP prediction
>    - Session persistence after 2FA
>
> 5. OAuth/SAML
>    - Redirect URI validation
>    - Token manipulation
>    - State parameter checking
> ```

## 9.3 Compliance Scanning (PCI-DSS, etc.)

### PCI-DSS Web Application Testing

**User:** "How do I document findings for PCI-DSS compliance?"

**Expert:**
> **PCI-DSS Requirement 6.6 Compliance Workflow:**
>
> 1. **Pre-Assessment**
>    - Confirm in-scope applications (cardholder data environment)
>    - Get written authorization
>    - Define scope boundaries
>
> 2. **Testing Scope**
>    ```markdown
>    In-scope for PCI:
>    - https://shop.target.com (accepts cards)
>    - https://checkout.target.com (payment page)
>    - https://myaccount.target.com (stored cards)
>    ```
>
> 3. **PCI-Specific Testing**
>    - OWASP Top 10 coverage
>    - CWE/SANS Top 25
>    - Specific PCI requirements:
>      - 3.4: Cardholder data encryption
>      - 4.2: PAN protection in transit
>      - 6.5: Common coding vulnerabilities
>
> 4. **Report Mapping**
>    ```markdown
>    | Finding | CWE ID | PCI Req | CVSS | Remediation |
>    |---------|--------|---------|------|-------------|
>    | SQL Injection | CWE-89 | 6.5.1 | 9.8 | Parametrize queries |
>    | XSS Stored | CWE-79 | 6.5.7 | 8.1 | Output encoding |
>    | CSRF | CWE-352 | 6.5.9 | 6.5 | Anti-CSRF tokens |
>    ```
>
> 5. **Remediation Validation**
>    - Retest after fixes deployed
>    - Document evidence of remediation
>    - Update scan date in ROC

### Enterprise Penetration Test Report Structure

```markdown
# Executive Summary
- Engagement overview
- Scope: 5 applications tested
- Total vulnerabilities: 12 (2 Critical, 4 High, 6 Medium)
- Overall risk rating: HIGH

# Methodology
- OWASP Testing Guide v4.2
- PTES Framework
- Black-box approach

# Findings Detail

## CRITICAL: SQL Injection in /api/users/search
**Description:** The search parameter is vulnerable to SQL injection...
**Impact:** Attacker can extract entire database, including cardholder data...
**Steps to Reproduce:**
1. Navigate to https://app.target.com/dashboard
2. Open Burp Suite proxy
3. Locate search request...
**Remediation:** Implement parameterized queries...
**CVSS 3.1:** 9.8 (CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H)

# Appendices
- Burp scan results (XML export)
- HTTP request/response samples
- Scope confirmation
```
