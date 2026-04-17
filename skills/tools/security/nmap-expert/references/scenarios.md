# Scenario Examples

## 9.1 CTF & Training Scenarios

### Quick Network Assessment for CTF

**User:** "I need to assess a CTF target - what's the fastest way?"

**Expert:**
> **CTF Quick Scan Workflow:**
>
> **Step 1: Fast discovery scan**
> ```bash
> nmap -sS -T5 -oA ctf_quick target
> # 15-second scan of top 100 ports
> ```
>
> **Step 2: Aggressive scan on interesting hosts**
> ```bash
> nmap -A -T4 -p- target -oA ctf_full
> # All ports, OS, scripts, traceroute
> ```
>
> **Step 3: Targeted script scan**
> ```bash
> # Web enumeration
> nmap --script=http-enum,http-title,http-headers -p 80,443,8080 target
>
> # SMB enumeration
> nmap --script=smb-enum*,smb-os-discovery -p 139,445 target
>
> # DNS enumeration  
> nmap --script=dns-zone-transfer,dns-enum -p 53 target
>
> # SSL/TLS analysis
> nmap --script=ssl-cert,ssl-enum-ciphers -p 443 target
> ```
>
> **Step 4: Vulnerability check**
> ```bash
> nmap --script=vuln target -oA ctf_vulns
> ```

### Practice Lab Setup

**User:** "How do I scan my home lab safely?"

**Expert:**
> **Home Lab Scanning:**
>
> **Network diagram:**
> ```
> Kali Linux (attacker) ---- Switch ---- VulnHub VMs
>     192.168.1.100              192.168.1.10-20
> ```
>
> **Scan commands:**
> ```bash
> # 1. Discover all hosts
> nmap -sn 192.168.1.0/24 -oA lab_discovery
> 
> # 2. Quick scan discovered hosts
> nmap -sS -sV -T4 192.168.1.10,15,20 -oA lab_services
> 
> # 3. Enumerate specific service
> nmap --script=default,vuln -p 80,443,3306 192.168.1.15 -oA web_enum
> 
> # 4. Save results
> # Import to Metasploit
> msf> db_import lab_full.xml
> ```

## 9.2 Bug Bounty & Pentest Workflows

### External Network Reconnaissance

**User:** "How do I do external recon for a bug bounty target?"

**Expert:**
> **Bug Bounty Recon Workflow:**
>
> **Step 1: Host discovery (external)**
> ```bash
> # DNS enumeration
> nmap --script=dns-zone-transfer,dns-brute -p 53 ns.target.com
>
> # Find live hosts via various methods
> nmap -Pn -T4 --script=dns-discovery target.com -oA dns_recon
> ```
>
> **Step 2: Web footprinting**
> ```bash
> # Scan for web services
> nmap -p 80,443,8080,8443 target.com -oA web_scan
>
> # Web server enumeration
> nmap --script=http-enum,http-title,http-headers,http-robots.txt \
>      -p 80,443,8080,8443 target.com
>
> # SSL/TLS analysis
> nmap --script=ssl-cert,ssl-enum-ciphers,ssl-known-key \
>      -p 443 target.com
> ```
>
> **Step 3: Service enumeration**
> ```bash
> # Common external services
> nmap -sV -p 22,25,53,110,143,465,587,993,995 target.com
>
> # Identify cloud services
> nmap --script=http-cloudflare* -p 80,443 target.com
> ```
>
> **Step 4: Passive/alternative recon (before active scan)**
> ```bash
> # WHOIS
> nmap --script=http-robtex-reverse-ip,whois* target.com
>
> # Certificate transparency
> nmap --script=ssl-cert,http-headers target.com
> ```

### Internal Network Penetration Test

**User:** "What's the workflow for an internal network pentest?"

**Expert:**
> **Internal Pentest Workflow:**
>
> **Phase 1: Network mapping**
> ```bash
> # 1. Subnet enumeration
> nmap -sn 10.0.0.0/16 -oA subnet_hosts
>
> # 2. Port scan of entire subnet (quick)
> nmap -sS -T4 -p 22,80,443,445,3389,5432,3306 \
>      --open 10.0.0.0/16 -oA quick_internal
>
> # 3. Service fingerprinting
> nmap -sV -p- --open 10.0.0.0/16 -oA services_internal
> ```
>
> **Phase 2: Targeted enumeration**
> ```bash
> # SMB enumeration
> nmap --script=smb-enum*,smb-os-discovery,smb-security-mode \
>      -p 139,445 10.0.0.0/16
>
> # MSSQL enumeration  
> nmap -p 1433 --script=ms-sql-info,ms-sql-empty-password \
>      10.0.0.0/16
>
> # SNMP enumeration
> nmap -sU -p 161 --script=snmp-info,snmp-brute \
>      10.0.0.0/16
>
> # LDAP enumeration
> nmap -p 389,636 --script=ldap-rootdse,ldap-search \
>      10.0.0.0/16
> ```
>
> **Phase 3: Vulnerability assessment**
> ```bash
> # Known exploits
> nmap --script=smb-vuln*,ms-sql-vuln* -p 445,1433 \
>      10.0.0.0/16
>
> # Weak credentials
> nmap --script=ftp-anon,ssh-brute,mysql-brute,smb-brute \
>      10.0.0.0/16
> ```

## 9.3 Compliance Scanning

### PCI-DSS Network Assessment

**User:** "How do I document nmap results for PCI-DSS?"

**Expert:**
> **PCI-DSS Requirements 11.2 & 11.3 Workflow:**
>
> **Required documentation:**
> - Network diagrams
> - All open ports and services
> - Vulnerabilities found
> - Remediation evidence
>
> **Scan documentation:**
> ```bash
> # Comprehensive scan of CDE
> nmap -sS -sV -O -p- -T4 \
>      -oA pci_scan_$(date +%Y%m%d) \
>      -e eth0 \
>      10.1.2.0/24
>
> # Script scan for common vulnerabilities
> nmap --script=vuln,exploit -p- \
>      10.1.2.0/24 -oA pci_vulns
>
> # SSL/TLS compliance check
> nmap --script=ssl-cert,ssl-enum-ciphers,ssl-known-key \
>      -p 443,8443 10.1.2.0/24
> ```
>
> **Evidence export:**
> ```bash
> # Generate timestamped reports
> DATE=$(date +%Y%m%d)
> nmap -sV -oA pci_full_$DATE 10.1.2.0/24
> 
> # Extract key findings
> grep "open" pci_full_$DATE.gnmap | sort -u > pci_open_ports_$DATE.txt
> grep -E "(CVE|MSF|SMB|SQL)" pci_vulns.gnmap > pci_critical_$DATE.txt
> ```
>
> **Remediation verification scan:**
> ```bash
> # Post-remediation scan
> nmap -sV -p 21,22,23,25,80,110,143,3306,3389,5432 \
>      10.1.2.0/24 -oA pci_recheck_$(date +%Y%m%d)
> ```

### HIPAA Security Assessment

```bash
# HIPAA-relevant scanning
nmap -sS -sV -p- -T4 -oA hipaa_assessment \
     --script=ftp-anon,ssh1-enum-algos,ssl-heartbleed,\
     mysql-enum,ms-sql-info,rdp-enum \
     10.0.0.0/24

# PHI system verification
nmap -p 445 --script=smb-enum-shares,smb-ls \
     10.0.0.0/24 -oA hipaa_file_shares

# Audit logging verification
nmap -p 389,636 --script=ldap-search \
     10.0.0.0/24 -oA hipaa_ldap
```

### Compliance Scan Schedule

```markdown
| Standard | Requirement | Recommended Scan |
|----------|------------|-----------------|
| PCI-DSS | Quarterly + after changes | Full + vuln |
| HIPAA | Annual + risk-based | Network + endpoints |
| SOC 2 | Continuous/periodic | Automation + annual |
| NIST 800-53 | As required | Varies by controls |
| ISO 27001 | Annual + after changes | Full assessment |
```

### Export for Governance Tools

```bash
# Generate reports for governance tools
nmap -sV -oX hipaa_scan.xml 10.0.0.0/24

# Nessus XML import format
# Metasploit XML import
# Qualys CSV format (via post-processing)

# Script to extract compliance-relevant data
#!/bin/bash
echo "=== COMPLIANCE SCAN REPORT ==="
echo "Date: $(date)"
echo ""
echo "=== OPEN PORTS BY HOST ==="
grep "open" scan.gnmap | awk '{print $2, $5}'
echo ""
echo "=== VULNERABLE SERVICES ==="
grep -E "(smb-vuln|ms-sql-vuln|heartbleed)" vuln_scan.gnmap
```
