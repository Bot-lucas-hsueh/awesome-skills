# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Quick Fix |
|---|---------|----------|--------|-----------|
| 1 | **Running full port scan on entire network** | :red_circle: High | Network congestion, IDS alerts | Use --top-ports or limit to specific hosts |
| 2 | **SYN scan without root/sudo** | :red_circle: High | Falls back to TCP connect, slower | Use `sudo nmap` or `-sT` instead |
| 3 | **Not saving scan results** | :yellow_circle: Medium | Lost data, no audit trail | Always use `-oA filename` |
| 4 | **Scanning without host discovery on local net** | :yellow_circle: Medium | May miss hosts that block ICMP | Use `-Pn` only when needed |
| 5 | **Ignoring UDP scan results** | :yellow_circle: Medium | Miss UDP services (DNS, SNMP) | Run targeted UDP scan on known hosts |
| 6 | **Wrong timing template for network** | :yellow_circle: Medium | Missed ports, false positives | Adjust `-T` based on network reliability |
| 7 | **Not checking firewall rules first** | :yellow_circle: Medium | Scanning won't work as expected | Test connectivity to known open port |
| 8 | **Running all scripts blindly** | :yellow_circle: Medium | Network noise, crashes services | Use targeted script selection |
| 9 | **Assuming closed = filtered** | :yellow_circle: Medium | Wrong vulnerability assessment | Verify with multiple scan types |
| 10 | **Forgetting -p- for all ports** | :yellow_circle: Medium | Missing low-frequency services | Always do full port scan on targets |

### Critical Scanning Errors

```markdown
:x: WRONG - Common errors:

# Error 1: SYN scan without privileges
nmap -sS target
# Result: May silently use TCP connect, slower

# Error 2: Aggressive timing on unstable network  
nmap -T5 target
# Result: Packet loss, missed ports

# Error 3: Scanning entire class B when only /24 needed
nmap -sS -p- 10.0.0.0/16
# Result: 65,000 hosts, hours of scanning, network impact

# Error 4: No output saved
nmap target
# Result: No audit trail, can't import to tools

# Error 5: Forgetting important ports
nmap -p 80,443 target
# Result: Misses SSH (22), RDP (3389), etc.

:white_check_mark: CORRECT:

# Proper SYN scan
sudo nmap -sS target

# Adjust timing for network
nmap -T4 target     # Good LAN
nmap -T2 target     # Unreliable/WAN

# Scope properly
nmap -sS -p- -T4 10.0.0.0/28  # Only needed hosts

# Always save
nmap -sV -oA scan_results target

# Include common high-risk ports
nmap -p 22,80,443,445,1433,3306,3389 target
```

## 10.2 Anti-Patterns

### Scanning Anti-Patterns

| Anti-Pattern | Description | Impact | Correct Approach |
|-------------|-------------|--------|------------------|
| **No timing template** | Using default everywhere | Unnecessary slowness | `-T4` for LAN, `-T2` for WAN |
| **All scripts on all ports** | `nmap -sC -p-` everywhere | Network noise, crashes | Targeted scripts per service |
| **Skipping UDP** | Only scanning TCP | Miss DNS, SNMP, etc. | Add `-sU` for key UDP ports |
| **No version detection** | Basic port scan only | Miss specific vulns | Always use `-sV` |
| **Ignoring script output** | Scan but don't review | Miss findings | Read script output carefully |

### Port State Interpretation Errors

```markdown
:warning: Port state confusion:

CLOSED vs FILTERED:

nmap -sS target:445
# closed: Port closed (RST received)
# filtered: No response (firewall likely dropping)
# open: Service listening

For firewall analysis:
nmap -sA target     # ACK scan
nmap -sW target     # Window scan
nmap -sN target     # Null scan (no flags)

# Filtered vs Not filtered (for response):
nmap -sN -p 445 target
# If RST: filtered=no
# If no response: filtered=yes
```

### Output Handling Anti-Patterns

```markdown
:x: WRONG:
nmap target > output.txt  # Loses grepable format info
cat output.nmap | grep open  # Wrong, lost structure

:white_check_mark: CORRECT:
nmap -oA scan_results target     # All formats
grep "open" scan_results.gnmap  # Grepable format
grep "<state state=\"open\"" scan_results.xml  # XML parsing
```

## 10.3 False Positive/Negative Management

### Reducing False Negatives

```markdown
:clipboard: Common reasons for missed vulnerabilities:

1. Partial port scan
   - Fix: Always scan -p- for comprehensive assessment
   - Some services on non-standard ports

2. UDP scan too fast
   - Fix: Run -sU with longer timeout
   - UDP requires retries

3. Firewall dropping packets
   - Fix: Use multiple scan types (-sS, -sT, -sA)
   - Try source port 53 or 80

4. Script timing out
   - Fix: Increase --script-timeout
   - Try individual scripts separately

5. Service detection failed
   - Fix: Increase version intensity
   - Try manual banner grab
```

### Verification Commands

```bash
# Verify port state manually
nc -zv target 80
telnet target 80
openssl s_client -connect target:443

# Check service version
curl -I http://target
ssh -v target

# UDP service verification  
nmap -sU -p 53 target --script dns-nsid
# DNS queries to verify service
```

### Port State Table

```markdown
| Scan Type | Open | Closed | Filtered |
|-----------|------|--------|----------|
| SYN (-sS) | SYN-ACK | RST | No response |
| TCP (-sT) | SYN-ACK | RST | RST or timeout |
| ACK (-sA) | RST | RST | No response |
| UDP (-sU) | ICMP port unreach | No response | No response |
| FIN (-sF) | No response | RST | No response |
| Null (-sN) | No response | RST | No response |
```

## 10.4 Legal & Scope Issues

### Critical Legal Considerations

```markdown
:warning: MUST verify before scanning:

1. Written authorization
   - Bug bounty program rules allow it
   - Signed contract for pentest
   - Scope explicitly defined

2. IP ranges verified
   - WHOIS matches scope
   - No shared infrastructure
   - Cloud provider confirm ownership

3. Rate limits agreed
   - Some targets rate limit
   - Aggressive scans may trigger blocks
   - Coordinate with target IT

4. Timing windows
   - Some orgs require off-hours scanning
   - Production systems = minimal impact
   - Coordinate maintenance windows
```

### Scope Violation Detection

```bash
# Before scanning, verify IPs belong to target:
whois 192.168.1.1 | grep -i "Organization"
# Compare with scope document

# During scan, watch for:
# - Hosts outside expected subnets
# - Unusually large response counts
# - Unexpected services (medical devices, ICS)
```

## 10.5 Performance Optimization

| Issue | Cause | Solution |
|-------|-------|----------|
| Scan taking too long | Large port range, slow network | Increase -T, reduce port range |
| Missing ports | Too fast, packet loss | Reduce -T, increase retries |
| Network congestion | Aggressive scanning | Use -T2-3, limit parallelism |
| Firewall blocking | Too many probes | Use -g (source port), slow down |
| Host unresponsive | Rate limiting | Use -Pn, increase timeout |

### Speed Optimization

```bash
# Fast scan (local network)
nmap -T5 --max-retries 2 -p- target

# Balanced scan
nmap -T4 --max-parallelism 100 target

# Stealth/slow scan
nmap -T1 --max-retries 1 --max-scan-delay 1s target

# Adaptive timing
nmap --initial-rtt-timeout 100ms target  # Fast for low latency
nmap --initial-rtt-timeout 2000ms target # Slow for high latency
```

### Parallelism Controls

```bash
--max-parallelism 1     # One probe at a time (slowest)
--min-parallelism 10    # Minimum parallel probes
--max-retries 0         # No retries (fastest, most unreliable)
--max-retries 10        # Many retries (slowest, most reliable)
--max-scan-delay 10ms   # Max delay between probes
```
