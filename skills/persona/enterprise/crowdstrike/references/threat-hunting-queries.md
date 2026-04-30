# CrowdStrike Falcon Threat Hunting Queries Reference

## Overview
This reference provides Event Search queries for proactive threat hunting across the Falcon platform. All queries use CrowdStrike Query Language (CQL).

---

## Table of Contents
1. [Initial Access Detection](#initial-access-detection)
2. [Execution Monitoring](#execution-monitoring)
3. [Persistence Detection](#persistence-detection)
4. [Privilege Escalation](#privilege-escalation)
5. [Defense Evasion](#defense-evasion)
6. [Credential Access](#credential-access)
7. [Discovery](#discovery)
8. [Lateral Movement](#lateral-movement)
9. [Collection](#collection)
10. [Command and Control](#command-and-control)
11. [Exfiltration](#exfiltration)
12. [Impact](#impact)

---

## Initial Access Detection

### Suspicious Office Document Execution
```spl
// Detects Office applications spawning suspicious child processes
// MITRE ATT&CK: T1566.001 - Phishing: Spearphishing Attachment

event_simpleName=ProcessRollup2 
| search ParentBaseFileName IN ("winword.exe", "excel.exe", "powerpnt.exe", "outlook.exe")
| where FileName IN ("powershell.exe", "cmd.exe", "wscript.exe", "cscript.exe", "mshta.exe", "regsvr32.exe", "rundll32.exe")
| eval RiskScore=case(
    FileName=="powershell.exe", 100,
    FileName=="cmd.exe", 80,
    FileName=="mshta.exe", 90,
    true(), 70
)
| stats count, values(CommandLine) as Commands, max(RiskScore) as MaxRisk 
    by ComputerName, UserName, ParentBaseFileName, FileName
| where count > 0
| sort - MaxRisk
```

### Suspicious Browser Downloads
```spl
// Detects executable downloads from browsers
// MITRE ATT&CK: T1189 - Drive-by Compromise

event_simpleName=ProcessRollup2 
| search ParentBaseFileName IN ("chrome.exe", "firefox.exe", "iexplore.exe", "msedge.exe", "opera.exe")
| where FileName IN (".exe", ".dll", ".bat", ".ps1", ".vbs", ".js", ".hta")
| eval SuspiciousPath=if(match(FilePath, "(?i)\\\\(temp|downloads|desktop|documents)\\\\"), 1, 0)
| where SuspiciousPath=1
| stats count, values(FilePath) as Paths, values(CommandLine) as Commands 
    by ComputerName, UserName, FileName
| sort - count
```

---

## Execution Monitoring

### Encoded PowerShell Commands
```spl
// Detects PowerShell with encoding/obfuscation
// MITRE ATT&CK: T1059.001 - PowerShell

event_simpleName=ProcessRollup2 FileName=powershell.exe
| eval CommandLine=lower(CommandLine)
| search (
    CommandLine="*encodedcommand*" 
    OR CommandLine="*enc*" 
    OR CommandLine="*bypass*"
    OR CommandLine="*noprofile*"
    OR CommandLine="*windowstyle*hidden*"
    OR CommandLine="*command*"
    OR CommandLine="*downloadstring*"
    OR CommandLine="*invoke-expression*"
    OR CommandLine="*iex*"
    OR CommandLine="*frombase64string*"
)
| eval EncodingLevel=case(
    match(CommandLine, "encodedcommand|frombase64string"), "High",
    match(CommandLine, "downloadstring|invoke-expression|iex"), "Medium",
    match(CommandLine, "bypass|windowstyle"), "Low",
    true(), "Unknown"
)
| stats count, values(CommandLine) as Commands by ComputerName, UserName, EncodingLevel
| sort - count
```

### Living Off The Land Binaries (LOLBins)
```spl
// Detects suspicious use of legitimate system tools
// MITRE ATT&CK: T1218 - System Binary Proxy Execution

event_simpleName=ProcessRollup2
| where FileName IN ("certutil.exe", "regsvr32.exe", "mshta.exe", "rundll32.exe", 
                     "wmic.exe", "cscript.exe", "wscript.exe", "bitsadmin.exe",
                     "certoc.exe", "installutil.exe", "msbuild.exe")
| eval SuspiciousIndicator=case(
    match(CommandLine, "(?i)urlcache|split|f|decode"), "CertUtil Download",
    match(CommandLine, "(?i)script|scrobj"), "Regsvr32 Script",
    match(CommandLine, "(?i)javascript|vbscript"), "MSHTA Script",
    match(CommandLine, "(?i)http"), "Network Call",
    true(), "Other"
)
| stats count, values(CommandLine) as Commands by ComputerName, UserName, FileName, SuspiciousIndicator
| where count > 0
| sort - count
```

---

## Persistence Detection

### Registry Run Keys Modification
```spl
// Detects persistence via registry run keys
// MITRE ATT&CK: T1547.001 - Registry Run Keys

event_simpleName=AsepValueUpdate
| search RegObjectName IN ("*\\Software\\Microsoft\\Windows\\CurrentVersion\\Run*",
                           "*\\Software\\Microsoft\\Windows\\CurrentVersion\\RunOnce*",
                           "*\\SOFTWARE\\Wow6432Node\\Microsoft\\Windows\\CurrentVersion\\Run*")
| eval Suspicious=if(match(RegValueName, "(?i)update|system|windows|svchost"), 1, 0)
| stats count, values(RegValueName) as RegistryValues, values(RegStringValue) as Values 
    by ComputerName, UserName, RegObjectName
| sort - Suspicious, - count
```

### Scheduled Task Creation
```spl
// Detects suspicious scheduled task creation
// MITRE ATT&CK: T1053.005 - Scheduled Task/Job

event_simpleName=ScheduledTaskInfo
| eval SuspiciousAction=case(
    match(TaskExecCommand, "(?i)powershell|cmd|wscript|cscript"), "Script Execution",
    match(TaskExecCommand, "(?i)\\\\\\\\|http"), "Remote Execution",
    match(TaskExecCommand, "(?i)temp|appdata|programdata"), "Suspicious Path",
    true(), "Normal"
)
| where SuspiciousAction != "Normal"
| stats count, values(TaskExecCommand) as Commands, values(TaskName) as TaskNames 
    by ComputerName, UserName, SuspiciousAction
| sort - count
```

### WMI Event Subscription
```spl
// Detects WMI persistence mechanisms
// MITRE ATT&CK: T1546.003 - WMI Event Subscription

event_simpleName=WmiEventSubscription
| eval Suspicious=case(
    match(CommandLine, "(?i)activescript|commandlineeventconsumer"), "ActiveScript Consumer",
    match(CommandLine, "(?i)persistence|backdoor"), "Persistence Keyword",
    true(), "Normal"
)
| where Suspicious != "Normal"
| stats count by ComputerName, UserName, CommandLine, Suspicious
```

---

## Privilege Escalation

### UAC Bypass Attempts
```spl
// Detects User Account Control bypass techniques
// MITRE ATT&CK: T1548.002 - Bypass User Account Control

event_simpleName=ProcessRollup2
| search (FileName="computerdefaults.exe" OR FileName="fodhelper.exe" OR 
          FileName="slui.exe" OR FileName="dism.exe")
| eval UACBypassTechnique=case(
    FileName=="computerdefaults.exe", "ComputerDefaults",
    FileName=="fodhelper.exe", "Fodhelper",
    FileName=="slui.exe", "SLUI",
    true(), "Other"
)
| stats count by ComputerName, UserName, UACBypassTechnique, CommandLine
```

### Token Impersonation
```spl
// Detects suspicious token manipulation
// MITRE ATT&CK: T1134 - Access Token Manipulation

event_simpleName=ProcessRollup2
| search CommandLine="*runas*" OR CommandLine="*netonly*" OR CommandLine="*/savecred*"
| eval Technique=case(
    match(CommandLine, "(?i)runas.*savecred"), "Credential Saving",
    match(CommandLine, "(?i)runas.*netonly"), "Network Only Token",
    true(), "Other RunAs"
)
| stats count by ComputerName, UserName, Technique, CommandLine
```

---

## Defense Evasion

### AMSI Bypass Attempts
```spl
// Detects Anti-Malware Scan Interface bypass
// MITRE ATT&CK: T1562.001 - Disable or Modify Tools

event_simpleName IN (ProcessRollup2, ScriptControlScanTelemetry)
| eval AMSIBypass=case(
    match(CommandLine, "(?i)amsi"), "AMSI Reference",
    match(CommandLine, "(?i)system\\.management\\.automation"), "Automation Assembly",
    match(CommandLine, "(?i)amsiinitfailed"), "AMSI Init Failed",
    true(), "No Bypass"
)
| where AMSIBypass != "No Bypass"
| stats count by ComputerName, UserName, AMSIBypass, CommandLine
```

### Process Injection
```spl
// Detects potential process injection
// MITRE ATT&CK: T1055 - Process Injection

event_simpleName=ProcessRollup2
| where FileName IN ("powershell.exe", "cmd.exe", "wscript.exe")
| search CommandLine="*invoke-mimikatz*" OR CommandLine="*reflective*" OR 
         CommandLine="*inject*" OR CommandLine="*proginject*"
| stats count by ComputerName, UserName, FileName, CommandLine
```

---

## Credential Access

### LSASS Access Attempts
```spl
// Detects attempts to access LSASS memory
// MITRE ATT&CK: T1003.001 - LSASS Memory

event_simpleName=SensitiveProcessAccess
| search TargetProcessId_decimal=lsass.exe
| eval SuspiciousCaller=case(
    match(CallStackModuleNames, "(?i)mimikatz|sekurlsa|pypykatz"), "Known Tool",
    match(CallStackModuleNames, "(?i)dbghelp|dbgcore"), "Debugging API",
    true(), "Unknown"
)
| stats count by ComputerName, UserName, SourceProcessId_decimal, SuspiciousCaller
```

### Kerberoasting Detection
```spl
// Detects potential Kerberoasting activity
// MITRE ATT&CK: T1558.003 - Kerberoasting

event_simpleName=KerberosTicket
| where TicketType="TGS"
| where EncryptionType IN ("RC4-HMAC", "DES-CBC-MD5", "DES-CBC-CRC")
| eval IsServiceAccount=if(match(ServiceName, "\\$"), 0, 1)
| where IsServiceAccount=1
| stats count, dc(ServiceName) as UniqueServices by ComputerName, UserName, SourceIP
| where count > 5
| sort - count
```

### SAM Database Access
```spl
// Detects SAM database access attempts
// MITRE ATT&CK: T1003.002 - Security Account Manager

event_simpleName=ProcessRollup2
| search FilePath="*\\Windows\\System32\\config\\SAM" OR 
         CommandLine="*\\sam*" OR CommandLine="*\\security*"
| where FileName IN ("reg.exe", "vssadmin.exe", "diskshadow.exe")
| stats count by ComputerName, UserName, FileName, CommandLine
```

---

## Discovery

### Network Scanning
```spl
// Detects internal network scanning
// MITRE ATT&CK: T1046 - Network Service Scanning

event_simpleName=NetworkConnectIP4
| eval TimeBin=round(_time/60)
| stats dc(RemoteAddressIP4) as UniqueTargets, count as TotalConnections 
    by ComputerName, UserName, TimeBin
| where UniqueTargets > 50
| eval ScanRate=TotalConnections/UniqueTargets
| where ScanRate > 2
| sort - UniqueTargets
```

### System Information Discovery
```spl
// Detects system reconnaissance
// MITRE ATT&CK: T1082 - System Information Discovery

event_simpleName=ProcessRollup2
| where FileName IN ("systeminfo.exe", "hostname.exe", "whoami.exe", 
                     "net.exe", "ipconfig.exe", "tasklist.exe")
| eval ReconType=case(
    FileName=="systeminfo.exe", "System Details",
    FileName=="whoami.exe", "User Context",
    FileName=="net.exe", "Network/Account Info",
    FileName=="ipconfig.exe", "Network Config",
    true(), "Other"
)
| stats count, dc(ReconType) as ReconVariety by ComputerName, UserName
| where ReconVariety >= 3
| sort - count
```

---

## Lateral Movement

### Remote Service Creation
```spln// Detects suspicious remote service creation
// MITRE ATT&CK: T1021.002 - Remote Services: SMB/Windows Admin Shares

event_simpleName=ServiceCreation
| eval SuspiciousPath=case(
    match(ImageFileName, "(?i)\\\\\\\\.*\\\admin\\\$"), "Admin Share",
    match(ImageFileName, "(?i)\\\\\\\\.*\\\c\\\$"), "C$ Share",
    match(ImageFileName, "(?i)temp|appdata"), "User Temp",
    true(), "Normal"
)
| where SuspiciousPath != "Normal"
| stats count by ComputerName, UserName, ImageFileName, SuspiciousPath
```

### PSExec Usage
```spl
// Detects PsExec and similar remote execution tools
// MITRE ATT&CK: T1569.002 - System Services: Service Execution

event_simpleName=ProcessRollup2
| search FileName="psexec.exe" OR FileName="psexec64.exe" OR 
         CommandLine="*psexec*" OR CommandLine="*-accepteula*"
| eval UsageType=case(
    match(CommandLine, "(?i)-s"), "System Context",
    match(CommandLine, "(?i)\\\\\\\\"), "Remote Execution",
    true(), "Local"
)
| stats count by ComputerName, UserName, UsageType, CommandLine
```

### WMI Remote Execution
```spl
// Detects remote WMI execution
// MITRE ATT&CK: T1047 - Windows Management Instrumentation

event_simpleName=ProcessRollup2 FileName=wmic.exe
| search CommandLine="*/node*" OR CommandLine="*process call create*"
| eval RemoteTarget=if(match(CommandLine, "(?i)/node:\\s*(\\\\\S+|\d+\\.\d+\\.\d+\\.\d+)"), 
                       replace(CommandLine, ".*/node:\\s*(\\\\\S+|\d+\\.\d+\\.\d+\\.\d+).*", "\\1"), 
                       "Unknown")
| stats count by ComputerName, UserName, RemoteTarget, CommandLine
```

---

## Collection

### Clipboard Monitoring
```spl
// Detects clipboard access (potential credential harvesting)
// MITRE ATT&CK: T1115 - Clipboard Data

event_simpleName=ClipboardOperation
| eval SensitiveContent=case(
    match(ClipboardData, "(?i)password|pwd|pass"), "Password",
    match(ClipboardData, "(?i)token|api.?key|secret"), "Token/Key",
    match(ClipboardData, "\\b\\d{4}[\s-]?\\d{4}[\s-]?\\d{4}[\s-]?\\d{4}\\b"), "Credit Card",
    true(), "Other"
)
| stats count by ComputerName, UserName, SensitiveContent
| where SensitiveContent != "Other"
```

### Screen Capture
```spl
// Detects screen capture activity
// MITRE ATT&CK: T1113 - Screen Capture

event_simpleName=ProcessRollup2
| where FileName IN ("psr.exe", "screenshot.exe", "snippingtool.exe", 
                     "greenshot.exe", "sharex.exe", "lightshot.exe")
| eval ToolType=if(match(FilePath, "(?i)system32|syswow64"), "Built-in", "Third-party")
| stats count by ComputerName, UserName, FileName, ToolType
```

---

## Command and Control

### DNS Tunneling Detection
```spl
// Detects potential DNS tunneling
// MITRE ATT&CK: T1071.004 - Application Layer Protocol: DNS

event_simpleName=DnsRequest
| eval DomainLength=len(QueryName)
| eval SubdomainCount=len(replace(QueryName, "[^\\.]", ""))
| eval Entropy=length(replace(QueryName, "(.)\\1+", "\\1"))
| where DomainLength > 50 OR SubdomainCount > 4
| stats count, avg(DomainLength) as AvgLength, dc(QueryName) as UniqueDomains 
    by ComputerName, DomainResolved
| where count > 20
| sort - count
```

### Suspicious Network Connections
```spl
// Detects connections to suspicious ports
// MITRE ATT&CK: T1071 - Application Layer Protocol

event_simpleName=NetworkConnectIP4
| where RemotePort IN (4444, 5555, 6666, 7777, 8888, 9999, 12345, 31337)
| eval KnownTool=case(
    RemotePort=4444, "Metasploit Default",
    RemotePort=5555, "Android ADB/Alternative",
    RemotePort=31337, "Back Orifice/Elite",
    true(), "Other Suspicious"
)
| stats count by ComputerName, UserName, RemoteAddressIP4, RemotePort, KnownTool
```

### Beaconing Detection
```spl
// Detects regular beaconing patterns (potential C2)
// MITRE ATT&CK: T1071 - Command and Control

event_simpleName=NetworkConnectIP4
| eval TimeBin=round(_time/300)
| stats count, stdev(_time) as TimeVariance, min(_time) as FirstSeen, max(_time) as LastSeen 
    by ComputerName, UserName, RemoteAddressIP4, RemotePort
| eval Duration=LastSeen-FirstSeen
| eval Interval=Duration/count
| where count > 10 AND TimeVariance < 300 AND Interval BETWEEN (30, 600)
| sort - count
```

---

## Exfiltration

### Large Data Transfers
```spl
// Detects large outbound data transfers
// MITRE ATT&CK: T1041 - Exfiltration Over C2 Channel

event_simpleName=NetworkReceiveAcceptIP4
| eval TimeBin=round(_time/3600)
| stats sum(ConnectionSize) as TotalBytes by ComputerName, UserName, RemoteAddressIP4, TimeBin
| eval TotalMB=TotalBytes/1024/1024
| where TotalMB > 100
| sort - TotalMB
```

### Cloud Storage Upload
```spl
// Detects uploads to cloud storage
// MITRE ATT&CK: T1567 - Exfiltration Over Web Service

event_simpleName=NetworkConnectIP4
| search RemoteAddressIP4 IN ("13.107.42.14", "52.96.0.0/14", 
                              "142.250.0.0/15", "172.217.0.0/16")
| eval CloudService=case(
    match(DNSName, "(?i)onedrive|sharepoint|office"), "Microsoft",
    match(DNSName, "(?i)drive.google|docs.google|storage.google"), "Google Drive",
    match(DNSName, "(?i)dropbox"), "Dropbox",
    match(DNSName, "(?i)box.com"), "Box",
    true(), "Other"
)
| stats count by ComputerName, UserName, CloudService, DNSName
```

---

## Impact

### Ransomware Indicators
```spl
// Detects potential ransomware activity
// MITRE ATT&CK: T1486 - Data Encrypted for Impact

event_simpleName=ProcessRollup2
| where FileName IN ("vssadmin.exe", "wbadmin.exe", "bcdedit.exe")
| search CommandLine="*delete*" OR CommandLine="*shadows*" OR 
         CommandLine="*recoveryenabled*no*" OR CommandLine="*ignoreallfailures*"
| eval RansomwarePrep=case(
    match(CommandLine, "(?i)shadow.*delete"), "Shadow Copy Deletion",
    match(CommandLine, "(?i)recoveryenabled.*no"), "Recovery Disable",
    true(), "Other"
)
| stats count by ComputerName, UserName, RansomwarePrep, CommandLine
```

### Mass File Modification
```spl
// Detects mass file modifications (potential encryption)
// MITRE ATT&CK: T1486 - Data Encrypted for Impact

event_simpleName=FileOpenInfo
| eval TimeBin=round(_time/60)
| eval SuspiciousExt=if(match(FileName, "\\.(encrypted|locked|crypto|vault|evil)$"), 1, 0)
| stats count, sum(SuspiciousExt) as SuspiciousFiles by ComputerName, UserName, TimeBin
| where count > 100 OR SuspiciousFiles > 0
| eval EncryptionLikelihood=if(SuspiciousFiles > 0, "High", if(count > 500, "Medium", "Low"))
| sort - SuspiciousFiles, - count
```

---

## Advanced Hunting Techniques

### Anomaly Detection - User Behavior
```spl
// Detects anomalous user activity
// Baseline: Normal activity patterns per user

event_simpleName=ProcessRollup2
| eval Hour=strftime(_time, "%H")
| eval DayOfWeek=strftime(_time, "%A")
| eval IsOffHours=if(Hour < 6 OR Hour > 20, 1, 0)
| eval IsWeekend=if(DayOfWeek IN ("Saturday", "Sunday"), 1, 0)

// Calculate user baseline
| eventstats avg(count) as AvgExecs, stdev(count) as StdevExecs by UserName
| where count > (AvgExecs + 3*StdevExecs)
| eval AnomalyScore=(count - AvgExecs) / StdevExecs
| where AnomalyScore > 3
| sort - AnomalyScore
```

### Lateral Movement Chain
```spl
// Detects lateral movement sequences
// Tracks user activity across multiple systems

event_simpleName=UserLogon
| eval TimeBin=round(_time/300)
| stats dc(ComputerName) as UniqueSystems, values(ComputerName) as Systems 
    by UserName, TimeBin
| where UniqueSystems > 3
| sort - UniqueSystems
```

### Persistence Check
```spl
// Comprehensive persistence detection
// MITRE ATT&CK: T1547 - Boot or Logon Autostart Execution

event_simpleName IN (AsepValueUpdate, ScheduledTaskInfo, ServiceCreation, 
                     RegKeySecurityDecrease, DriverLoad)
| eval PersistenceType=case(
    event_simpleName="AsepValueUpdate", "Registry ASEP",
    event_simpleName="ScheduledTaskInfo", "Scheduled Task",
    event_simpleName="ServiceCreation", "Windows Service",
    event_simpleName="DriverLoad", "Driver Load",
    true(), "Other"
)
| stats count by ComputerName, UserName, PersistenceType, count
| sort - count
```

---

## Query Optimization Tips

### Performance Best Practices
1. **Use specific event types** rather than wildcards
2. **Filter early** with `where` before stats
3. **Limit time ranges** for initial exploration
4. **Use `head`** for testing large result sets
5. **Leverage indexed fields** like `ComputerName`, `UserName`

### Common Patterns
```spl
// Time-based bucketing
| eval TimeBin=round(_time/3600)  // Hourly
| eval TimeBin=round(_time/86400) // Daily

// Statistical analysis
| eventstats avg(field) as Avg, stdev(field) as Stdev by group
| where field > (Avg + 3*Stdev)

// String manipulation
| eval LowerCommand=lower(CommandLine)
| eval CleanPath=replace(FilePath, "\\\\", "/")

// Conditional evaluation
| eval RiskScore=case(condition1, 100, condition2, 80, true(), 50)
```

---

## References

### MITRE ATT&CK Mapping
- [MITRE ATT&CK Framework](https://attack.mitre.org/)
- [CrowdStrike ATT&CK Coverage](https://www.crowdstrike.com/resources/guides/crowdstrike-mitre-attack/)

### Documentation
- [CrowdStrike Query Language Guide](https://falcon.crowdstrike.com/documentation/page/query-language)
- [Event Search Documentation](https://falcon.crowdstrike.com/documentation/page/event-search)

### Community Resources
- [Falcon Queries GitHub](https://github.com/CrowdStrike/falcon-queries)
- [Falcon Community](https://community.crowdstrike.com/)

---

*Version: 1.0*
*Last Updated: 2026-03-21*
