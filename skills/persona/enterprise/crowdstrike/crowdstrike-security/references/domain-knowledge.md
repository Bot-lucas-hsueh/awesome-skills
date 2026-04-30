# CrowdStrike Domain Knowledge Reference

> Deep technical reference for CrowdStrike Falcon platform. Load when asked about platform internals, detection engines, or advanced capabilities.

---

## §1 Falcon Platform Architecture

### 1.1 Sensor Architecture

| Layer | Component | Function |
|-------|-----------|----------|
| Kernel | `csagent.sys` (Win), `falcond` (macOS/Linux) | System call interception, behavior monitoring |
| User Space | Sensor agent | Process tracking, network telemetry, policy enforcement |
| Cloud Bridge | HTTPS/TLS to Falcon backend | Event streaming, command retrieval, config updates |

**Key Properties:**
- Kernel-level visibility without rootkit-level access
- CPU overhead < 1% (typical); memory < 40MB
- No signature definitions on endpoint—all analysis in cloud
- Automatic sensor updates without reboot

### 1.2 Threat Graph

```
CrowdStrike Cloud
┌─────────────────────────────────────────────────────────┐
│  TRILLION+ events/week processed                        │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐        │
│  │ Smart      │  │ ML/AI      │  │ Global     │        │
│  │ Filtering  │→ │ Correlation│→ │ Threat     │        │
│  │ (99% data  │  │ Engine     │  │ Intel      │        │
│  │  reduction)│  │            │  │ (Falcon X) │        │
│  └────────────┘  └────────────┘  └────────────┘        │
│        ↓              ↓              ↓                 │
│  ┌─────────────────────────────────────────┐           │
│  │ Real-time IOA Detection & Blocking     │           │
│  └─────────────────────────────────────────┘           │
└─────────────────────────────────────────────────────────┘
         ↑ Real-time event stream from sensors
         ↓ Cloud config, policy, IOC updates to sensors
```

### 1.3 Smart Filtering Pipeline

```
Raw Endpoint Events (billions/hour)
        ↓
┌─────────────────────────────┐
│ Smart Filtering (on-sensor)│  99% data reduction
│ - Deduplication             │  before cloud transmission
│ - Whitelist suppression     │
│ - Threshold filtering       │
└─────────────────────────────┘
        ↓ (~1% of raw events)
┌─────────────────────────────┐
│ Cloud Analytics            │
│ - ML behavioral models     │
│ - IOC correlation          │
│ - Anomaly detection        │
└─────────────────────────────┘
        ↓
┌─────────────────────────────┐
│ Threat Graph                │  Real-time graph of
│ - Campaign tracking         │  adversary activity
│ - Attribution               │  across customers
└─────────────────────────────┘
```

---

## §2 Detection Paradigm: IOA vs IOC

### 2.1 Indicator of Attack (IOA)

**What it detects:** Intent and technique—*what the adversary is trying to accomplish*

| IOA Category | Example Behaviors |
|--------------|-------------------|
| Execution | Code injection, process hollowing, parent-child anomaly |
| Persistence | Registry modification, scheduled task creation, service installation |
| Lateral Movement | WMI remote execution, RDP enumeration, SMB lateral tool transfer |
| Exfiltration | Unusual DNS tunnels, large encrypted outbound flows |

**Advantages:**
- Catches zero-day, never-seen-before malware
- Stops attack at early stage (kill chain)
- Adversary cannot "change hash" to evade

### 2.2 Indicator of Compromise (IOC)

**What it detects:** Evidence of known bad—*what the adversary left behind*

| IOC Type | Example |
|----------|---------|
| File Hash | SHA256 of known malware样本 |
| Domain/IP | C2 infrastructure from threat intel |
| Registry Key | Known malware persistence location |
| Mutex | Named mutex used by specific ransomware |

**Use cases:**
- Threat intelligence enrichment (Falcon X)
- Retro-hunt across historical data
- Block known-bad infrastructure

### 2.3 Falcon Detection Stack

```
┌────────────────────────────────────────────────────────┐
│ ML-Based Detection (CrowdStrike ML Engine)           │
│ - Neural engine analyzes behavior vectors             │
│ - Continuously trained on Threat Graph data           │
│ - Catches novel attack patterns                       │
├────────────────────────────────────────────────────────┤
│ Behavioral IOA Detection (User / Kernel)              │
│ - Process behavior analysis                           │
│ - Network behavior (dns, http, tcp)                  │
│ - File system / registry behavior                    │
├────────────────────────────────────────────────────────┤
│ Signature-Based Prevention (Traditional)             │
│ - Rapid blocking of known malware                     │
│ - CrowdStrike threat intelligence feeds              │
├────────────────────────────────────────────────────────┤
│ Custom IOA / IOC (Customer)                          │
│ - Custom indicator blocking (Falcon Complete/Custom)  │
│ - Falcon Prevent / Detect policies                    │
└────────────────────────────────────────────────────────┘
```

---

## §3 Core Product Modules

### 3.1 Falcon Prevent (Next-Gen AV / EPP)

Prevention policy enforcement:
- **Malware Prevention Policy**: File-based malware blocking
- **Exploit Prevention Policy**: Memory protection, script control, payload execution
- **Ransomware Protection**: Behavioral guarding, backup interruption detection
- **Firewall Policy**: Network traffic control, application-level rules

### 3.2 Falcon Insight (EDR)

Continuous behavioral monitoring:
- Real-time event collection from all sensors
- Threat detection on process, network, file, registry, loaded DLL behavior
- Investigation timeline and process tree visualization
- IOC and IOA alert correlation

### 3.3 Falcon OverWatch (Managed Threat Hunting)

24/7 elite human threat hunters:
- Proactive hunting across customer environments
- Hypothesis-driven investigation of anomalies
- High-fidelity alerts with context (reduces false positives)
- Adversary intelligence shared across CrowdStrike customer base

### 3.4 Falcon X (Threat Intelligence)

Automated threat intelligence:
- **Automated Malware Analysis**: Sandboxing with full detonation
- **Threat Intelligence**: Curated intel from Falcon sensor telemetry
- **Premium Threat Intelligence**: Nation-state and eCrime intelligence reports
- **IOC Management**: Import/export for SIEM/SOAR integration

### 3.5 Falcon Spotlight (Vulnerability Management)

Real-time vulnerability prioritization:
- Correlates CVE exposure with active threat campaigns
- Exploitability scoring based on detected threats
- Remediation prioritization based on asset criticality

### 3.6 Falcon Complete (MDR)

End-to-end managed detection and response:
- CrowdStrike analysts handle full IR lifecycle
- Guided response playbooks
- Proactive threat hunting included

---

## §4 Event Search (Falcon Query Language)

### 4.1 Core Event Types

| event_simpleName | Description | Key Fields |
|-----------------|-------------|------------|
| `ProcessRollup2` | Process execution | `FileName`, `CommandLine`, `ParentBaseFileName`, `UserName` |
| `NetworkAccessLog**` | Network connections | `RemoteAddress`, `RemotePort`, `Protocol`, `ImageFileName` |
| `DnsRequest` | DNS queries | `DomainName`, ` ComputerName`, `UserName` |
| `FileCreate` | File creation events | `FileName`, `TargetFileName`, `FileSize` |
| `RegistryCreate` | Registry modifications | `TargetObject`, `Value`, `OperationType` |
| `ImageLoad` | DLL/module loading | `ImageFileName`, `LoadedImageName` |
| `TokenMod` | Token manipulation | `TargetProcessId`, `OperationType` |

### 4.2 Essential Hunting Queries

```powershell
# Suspicious PowerShell execution
event_simpleName=ProcessRollup2 FileName="*powershell*" CommandLine="*"
| eval cmd=lower(CommandLine)
| search cmd="*encodedcommand*" OR cmd="*downloadstring*" OR cmd="*invoke-expression*"
| stats count by ComputerName, UserName, ParentBaseFileName, CommandLine

# Lateral movement via SMB
event_simpleName=NetworkAccessLog RemotePort=445 ImageFileName!="*explorer*"
| stats values(RemoteAddress) as target_ips, count by ComputerName, ImageFileName

# Ransomware early indicators
event_simpleName IN (ProcessRollup2, FileCreate)
| search FileName="*vssadmin*" OR CommandLine="*shadowcopy*delete*" OR CommandLine="*cipher*"
| stats values(FileName) as behaviors by ComputerName, UserName

# Credential dumping detection
event_simpleName=ProcessRollup2
| search CommandLine="*lsass*" OR CommandLine="*mimikatz*" OR CommandLine="*sam*dump*"
| stats count by ComputerName, UserName, CommandLine

# DNS exfiltration pattern
event_simpleName=DnsRequest
| stats dc(DomainName) as unique_domains, count by ComputerName, UserName
| where unique_domains > 500

# Living-off-the-land LOLBins
event_simpleName=ProcessRollup2
| search (FileName="*certutil*" OR FileName="*bitsadmin*" OR FileName="*mshta*")
AND (CommandLine="*url*" OR CommandLine="*download*" OR CommandLine="*http*")
| stats count by ComputerName, FileName, CommandLine
```

### 4.3 RTR (Real Time Response) Commands

```powershell
# Initiate RTR session
 FalconRTR.exe -hostid <host_id>

# File operations
ls /Users/*/Downloads/
cat /tmp/malicious_script.sh
rm /tmp/payload.exe

# Process investigation
ps                             # List running processes
cat /proc/<pid>/cmdline        # Process command line

# Registry analysis (Windows)
reg query "HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run"
reg query "HKLM\SYSTEM\CurrentControlSet\Services" /s | grep -i "<threat_name>"

# Memory acquisition
memdump /tmp/memory_<hostname>_<timestamp>.raw

# Network analysis
netstat -anp | grep ESTABLISHED
cat /proc/net/tcp

# Remediation
put /local/clean_script.sh /tmp/remediation.sh
execute /tmp/remediation.sh
```

---

## §5 MITRE ATT&CK Mapping

### 5.1 Falcon Coverage Matrix

| ATT&CK Tactic | Falcon Detection Method | event_simpleName |
|--------------|----------------------|-----------------|
| T1566 Phishing | Sandbox detonation, macro detection | `BehavioralProtectionNotification` |
| T1059 Command Execution | Process monitoring, script control | `ProcessRollup2`, `ScriptControl` |
| T1055 Process Injection | Memory protection, injection detection | `ModuleLoad`, `ProcessInjection` |
| T1547 Boot Autostart | Registry monitoring | `RegistryCreate`, `RegistryModify` |
| T1021 Remote Services | Network monitoring, RDP detection | `NetworkAccessLog`, `RdpSessionNotification` |
| T1484 Domain Trust | LDAP/WMI remote detection | `WmiCommand`, `LdapQuery` |
| T1070 Indicator Removal | File integrity, shadow copy detection | `FileCreate`, `VssAdminExecution` |
| T1048 Exfiltration | Network anomaly, large outbound flows | `NetworkTunnelTraffic`, `DnsRequest` |

---

## §6 Detection Tuning Best Practices

### 6.1 Prevention Policy Configuration

| Setting | Recommended | Rationale |
|---------|-------------|----------|
| Behavioral ML | **Enforce** | Primary zero-day protection |
| Local ML | **Enforce** | On-sensor, offline protection |
| Script Control | **Enforce** (PowerShell, CMD, HTA, MSI) | Blocks LOLBins |
| Exploit Protection | **Enforce** | Stops privilege escalation |
| Ransomware Guarding | **Enforce** | Behavioral blocking |
| Custom IOA | **Detect → Prevent** (after tuning) | Phase-in carefully |

### 6.2 Exclusion Best Practices

**DOs:**
- Exclude specific software with known benign behavior
- Document exclusion rationale with expiry date
- Review exclusions quarterly
- Use machine learning exclusions over file/path exclusions

**DON'Ts:**
- Exclude `%TEMP%`, `%APPDATA%`, entire user directories
- Exclude by file hash (use Falcon X IOCs instead)
- Whitelist entire software vendors

### 6.3 Detection-to-Prevention Workflow

```
1. New IOA detected → Analyst review (SOC L2)
2. Confirmed true positive → Investigate scope
3. False positive → Submit to CS support for tuning
4. True positive (new TTPs) → Add to custom prevention policy
5. High-confidence adversary behavior → Switch to prevent mode
6. Monitor for 14 days → Evaluate FP rate → Adjust
```
