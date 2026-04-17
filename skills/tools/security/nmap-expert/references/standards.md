# Standards & Reference

## 7.1 Official Documentation

- [nmap.org Official Site](https://nmap.org/)
- [Nmap Documentation](https://nmap.org/book/man.html)
- [Nmap Reference Guide](https://nmap.org/docs.html)
- [Nmap OS Detection](https://nmap.org/book/osdetect.html)
- [Nmap NSE Documentation](https://nmap.org/nsedoc/)
- [Nmap Output Formats](https://nmap.org/book/output-formats.html)
- [Zenmap GUI Documentation](https://nmap.org/zenmap/)
- [Nmap Port Scanning Basics](https://nmap.org/book/man-port-scanning-basics.html)

## 7.2 Configuration Reference

### Timing Templates

```bash
# T0-T5: Aggressiveness (higher = faster but noisier)
# T0-T2: IDS evasion, slow scans
# T3: Default, balanced
# T4-T5: Fast, reliable networks only

# Timing flags
-T0    Paranoid (IDS evasion, 5 min between packets)
-T1    Sneaky (IDS evasion, 15 sec between packets)  
-T2    Polite (low bandwidth, 0.4 sec between packets)
-T3    Normal (default, parallel scans)
-T4    Aggressive (fast, assumes good network)
-T5    Insane (very fast, may miss open ports)
```

### Timing Template Parameters

```bash
# Equivalent manual settings for -T4
--max-rtt-timeout 1250ms
--min-rtt-timeout 100ms
--initial-rtt-timeout 500ms
--max-retries 6
--scan-delay 0ms
--max-scan-delay 10ms

# Example: Custom timing for unstable network
nmap -T4 --max-rtt-timeout 2000ms --initial-rtt-timeout 1000ms \
     --max-retries 3 --max-scan-delay 50ms target
```

### Output Format Options

```bash
# Multiple output formats
-oA basename     # All formats (nmap, xml, grepable)
-oN file.nmap    # Normal output (readable)
-oX file.xml     # XML output (for parsing)
-oG file.gnmap   # Grepable output (grep-friendly)
-oS file.scrip   # Script kiddie output (l337 speak)

# Example: Multiple formats
nmap -sV -oA scan_results target.com
# Creates: scan_results.nmap, scan_results.xml, scan_results.gnmap

# Verbosity options
-v               # Increase verbosity (-v, -vv, -vvv)
-d [1-9]         # Debugging (more = verbose debugging)
--reason         # Show why port is in state
--open           # Only show open ports
```

### Script Scan Configuration

```bash
# Script categories
nmap --script <category> target
# Categories: auth, broadcast, brute, default, discovery, dos, exploit, 
#             external, fuzzer, intrusive, malware, safe, version, vuln

# Example: Default scripts (runs with -sC)
nmap -sC target.com

# Specific scripts
nmap --script=http-enum,http-title target.com

# Script arguments
nmap --script=smb-brute --script-args userdb=users.txt,passdb=pass.txt target

# Script timing (slower = more thorough)
nmap --script-timeout 30m target  # Timeout for all scripts
nmap --max-script-trace-time 5m target
```

## 7.3 Common Commands

| Command | Description |
|---------|-------------|
| `nmap -sT target` | TCP connect scan (full handshake) |
| `nmap -sS target` | SYN scan (half-open, requires root) |
| `nmap -sU target` | UDP scan (slow, high false negatives) |
| `nmap -sV target` | Version detection |
| `nmap -O target` | OS detection |
| `nmap -A target` | Aggressive (OS, version, scripts, traceroute) |
| `nmap -sC target` | Default scripts |
| `nmap -p- target` | Scan all 65535 ports |
| `nmap -F target` | Fast scan (top 100 ports) |
| `nmap -Pn target` | No ping (skip host discovery) |
| `nmap --top-ports 1000 target` | Scan top 100 most common ports |

### Essential Scan Types

```bash
# Host discovery
nmap -sn 10.0.0.0/24           # Ping sweep (no port scan)
nmap -PS 80,443 target         # TCP SYN ping (ports 80,443)
nmap -PA 3389 target           # TCP ACK ping
nmap -PU 53 target             # UDP ping

# Port scanning
nmap -sS -p 22,80,443 target   # SYN scan specific ports
nmap -sT -p 1-1000 target     # TCP connect scan port range
nmap -sU -p 53,123,161 target  # UDP scan specific ports

# Service/Version detection
nmap -sV --version-intensity 5 target  # Version detection (0-9)
nmap -sV --version-light target       # Light version scan
nmap -sV --version-all target         # Intensity 9, exhaustive

# OS detection
nmap -O target                  # OS detection
nmap -O --osscan-guess target   # Aggressive OS guessing
nmap -A target                  # Aggressive (OS + version + scripts + traceroute)
```

### Port Specification Syntax

```bash
-p 22                   # Single port
-p 22,80,443            # Multiple specific ports
-p 1-1000               # Range of ports
-p-                     # All ports (1-65535)
-p U:53,T:80            # UDP port 53, TCP port 80
-p 80,100-200           # Port 80 plus range 100-200
--top-ports 100         # Top 100 most common ports
--exclude-ports 9100    # Exclude specific ports (printer detection)
```

## 7.4 Version Compatibility

| nmap Version | Status | Notable Features |
|-------------|--------|------------------|
| 7.95 | Current | New scripts, IPv6 improvements |
| 7.94 | Current | Performance improvements |
| 7.92-7.93 | Supported | SSL/TLS script updates |
| 7.80-7.91 | Supported | Major performance gains |
| 7.60-7.70 | Legacy | NSE Lua improvements |
| 6.x | Legacy | Some scripts still relevant |

### Platform Support

| Platform | Notes |
|----------|-------|
| Linux | Native, best performance |
| macOS | Native via Homebrew `brew install nmap` |
| Windows | Official installer, requires admin for SYN scan |
| FreeBSD | Native package |
| Raspberry Pi | Native package |

### Windows vs Unix Differences

```bash
# Windows: SYN scan requires Npcap/WinPcap
# Without: Falls back to TCP connect (-sT)
# Note: nmap --privilege on Windows = SYN scan

# Unix/Linux: Requires root for SYN scan
sudo nmap -sS target.com
sudo nmap -sU target.com
```

## 7.5 Use Cases

| Use Case | Command | Output |
|----------|---------|--------|
| Quick port check | `nmap -sT -F target` | Top 100 ports |
| Full port scan | `nmap -sS -p- -T4 target` | All ports, fast |
| Service enumeration | `nmap -sV target` | Version info |
| OS fingerprinting | `nmap -O target` | OS guess |
| Aggressive scan | `nmap -A target` | Everything |
| Firewall detection | `nmap -sA target` | ACK scan for firewall mapping |
| Stealth scan | `nmap -sS -T2 target` | IDS evasion |
| Vulnerability scan | `nmap --script vuln target` | Security checks |
| Network inventory | `nmap -O -sV -oA inventory target` | Full discovery |
| Web enumeration | `nmap --script http-enum target` | Web directories |
