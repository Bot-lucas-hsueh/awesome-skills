# Standard Workflow

## 8.1 Reconnaissance & Enumeration Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: Host Discovery                                          │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 1. Ping sweep (if authorized)                                   │
│    nmap -sn 10.0.0.0/24 -oG ping_sweep.gnmap                   │
│                                                                  │
│ 2. No ping (skip discovery)                                      │
│    nmap -Pn 10.0.0.0/24 - used when hosts block ICMP           │
│                                                                  │
│ 3. Multi-method discovery                                       │
│    nmap -sn -PE -PP -PS21,22,23,25,80,443,3389 \              │
│         -PA80,443,3389 -PU53,123,161 \                         │
│         10.0.0.0/24                                            │
│                                                                  │
│ 4. Review discovered hosts                                       │
│    grep "Up" ping_sweep.gnmap | cut -d' ' -f2                  │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: Port Scanning                                            │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ Quick scan (if time constrained):                               │
│    nmap -sS -T4 -F target                                       │
│                                                                  │
│ Standard scan:                                                  │
│    nmap -sS -sV -T4 --top-ports 1000 target                   │
│                                                                  │
│ Full scan (comprehensive):                                      │
│    nmap -sS -sV -O -p- -T4 target                              │
│                                                                  │
│ UDP scan (runs in parallel):                                    │
│    nmap -sU -sV --top-ports 100 target                         │
│    (Note: UDP takes much longer, consider -T5)                   │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 3: Service & Vulnerability Detection                       │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ 1. Version detection                                             │
│    nmap -sV --version-intensity 5 target                       │
│                                                                  │
│ 2. OS detection (if network allows)                            │
│    nmap -O --osscan-guess target                               │
│                                                                  │
│ 3. Default scripts                                              │
│    nmap -sC target                                             │
│                                                                  │
│ 4. Vulnerability scripts                                        │
│    nmap --script vuln,exploit target                           │
│                                                                  │
│ 5. Specific service enumeration                                 │
│    nmap --script=banner,http-enum,ssl-cert target              │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

### Enumeration Checklist

```markdown
:clipboard: Enumeration targets:

- [ ] Web servers (80, 443, 8080, 8443)
- [ ] SSH (22)
- [ ] RDP (3389)
- [ ] SMB (445, 139)
- [ ] FTP (21)
- [ ] DNS (53)
- [ ] Email (25, 110, 143, 993, 995)
- [ ] Databases (1433, 1521, 3306, 5432, 27017)
- [ ] Middleware (8080, 8443, 9000)
- [ ] Cloud services (5000, 7000)
- [ ] Version control (22 for git, 9418 for git protocol)
- [ ] Management (443 for WinRM, 5985/5986 for WinRM)
```

## 8.2 Scanning Methodology

### Tiered Scanning Approach

```
┌────────────────────────────────────────────────────────────┐
│ TIER 1: Rapid Discovery (5-10 minutes)                      │
├────────────────────────────────────────────────────────────┤
│ nmap -sS -sV -T4 -oA tier1_scan target                   │
│ - Top 1000 ports                                          │
│ - Version detection                                        │
│ - Default scripts                                          │
│ Purpose: Quick overview, identify obvious targets         │
└────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌────────────────────────────────────────────────────────────┐
│ TIER 2: Comprehensive Scan (30-60 minutes)                 │
├────────────────────────────────────────────────────────────┤
│ nmap -sS -sV -O -p- -T3 -oA tier2_full target            │
│ - All ports                                                │
│ - Version detection                                        │
│ - OS detection                                             │
│ - Script scan on interesting services                     │
│ Purpose: Find everything, deep enumeration                │
└────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌────────────────────────────────────────────────────────────┐
│ TIER 3: Targeted Deep Dive (varies)                         │
├────────────────────────────────────────────────────────────┤
│ nmap -sV --script=discovery,version,intrusive \           │
│      -p 22,80,443,445,3306,5432 target                  │
│ Purpose: Deep scan specific high-value services           │
└────────────────────────────────────────────────────────────┘
```

### Firewall/IDS Evasion Techniques

```bash
# Fragment packets
nmap -f target                    # 8-byte fragments
nmap -f -f target                 # 16-byte fragments
nmap --mtu 24 target              # Custom MTU

# Decoy scan (requires -sS)
nmap -D decoy1,decoy2,ME target   # Hide real source
nmap -D RND:10 target            # Random decoys

# Source port manipulation
nmap -g 53 target                # Source port 53 (DNS)
nmap -g 80 target                # Source port 80 (HTTP)

# Slow scans (IDS evasion)
nmap -T0 -p 80 target            # Very slow
nmap -T1 -p 80 target            # Slow

# Zombie scan (requires zombie host)
nmap -sI zombiehost target       # Idle scan

# Data length
nmap --data-length 24 target     # Add random data
```

### Script Scan Selection

```bash
# By category
nmap --script=auth target           # Authentication testing
nmap --script=broadcast target      # Broadcast discovery
nmap --script=brute target          # Password brute force
nmap --script=default target        # Default scripts (-sC)
nmap --script=discovery target      # Service discovery
nmap --script=dos target            # DoS testing
nmap --script=exploit target        # Exploit modules
nmap --script=external target       # External services
nmap --script=fuzzer target         # Fuzzing scripts
nmap --script=intrusive target      # Aggressive/intrusive
nmap --script=malware target        # Malware detection
nmap --script=safe target           # Non-intrusive
nmap --script=version target        # Version detection
nmap --script=vuln target           # Vulnerability scanning

# Custom combinations
nmap --script=http-enum,http-title,http-headers target
nmap --script="discovery and not intrusive" target
```

## 8.3 Reporting Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ REPORTING STRUCTURE                                              │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ OUTPUT FORMATS FOR DIFFERENT AUDIENCES:                         │
│                                                                  │
│ 1. Normal output (-oN): Management, quick review                 │
│ 2. XML output (-oX): Integration, parsing                        │
│ 3. Grepable (-oG): Automation, filtering                        │
│ 4. All formats (-oA): Archive, multiple uses                    │
│                                                                  │
│ EXAMPLE:                                                         │
│ nmap -sV -sC -oA scan_results target                           │
│                                                                  │
│ FILES GENERATED:                                                 │
│ - scan_results.nmap   (human readable)                         │
│ - scan_results.xml    (importable)                             │
│ - scan_results.gnmap  (grep-able)                              │
└─────────────────────────────────────────────────────────────────┘
```

### Parsing & Automation

```bash
# Extract specific information from grepable output
grep "Ports:" targets.gnmap | grep "open" | cut -d' ' -f2

# Extract hosts with specific port open
grep "22/open" targets.gnmap | cut -d' ' -f2

# Find hosts with multiple open ports
awk -F'Ports:' '/Ports:/{print $2}' targets.gnmap | \
  awk -F',' '{if(NF>10)print}' | cut -d' ' -f2

# XML parsing with grep/sed
grep "<port>" scan.xml | grep "state=\"open\""

# Import to Metasploit
msf> db_import scan.xml
```

### Script Output Management

```bash
# Log all script output
nmap --script-args log=scripts.log target

# Silent scanning
nmap -sS -sV --script-timeout 10m target

# Script trace (debug)
nmap --script-trace -p 80 target

# Max parallelism
nmap --max-parallelism 100 target
nmap --min-parallelism 10 target

# Rate limiting
nmap --min-rate 100 target    # Min 100 packets/sec
nmap --max-rate 1000 target   # Max 1000 packets/sec
```

### Export and Import Workflow

```markdown
# Common tool integration

| Tool | Import Method | Format |
|------|--------------|--------|
| Metasploit | db_import | XML |
| Nessus | Direct XML | XML |
| Qualys | q XML | XML |
| Nmap FE | Via file | Nmap XML |
| Python | ElementTree | XML |
| Splunk | UF/HEC | JSON/XML |
```
