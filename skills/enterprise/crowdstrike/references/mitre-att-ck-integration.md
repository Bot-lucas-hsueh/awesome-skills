## 6. MITRE ATT&CK Integration

```
TACTIC MAPPING TO FALCON CAPABILITIES:
┌────────────────────┬────────────────────────────────────────────────────────┐
│ Initial Access     │ Falcon Prevent (phishing, drive-by compromise)         │
│ Execution          │ IOA behavioral detection, PowerShell monitoring        │
│ Persistence        │ Startup folder, registry, WMI event monitoring         │
│ Privilege Escal    │ UAC bypass, token impersonation detection              │
│ Defense Evasion    │ AMSI tampering, rootkit detection, process hollowing   │
│ Credential Access  │ Identity Protection, Kerberoasting detection           │
│ Discovery          │ System/network enumeration behavioral analytics        │
│ Lateral Movement   │ RDP, PsExec, WMI, SMB monitoring                       │
│ Collection         │ Data staging, clipboard monitoring                     │
│ C2                 │ Network traffic analysis, DNS tunneling detection      │
│ Exfiltration       │ Data loss prevention, cloud activity monitoring        │
│ Impact             │ Ransomware protection, backup tampering detection      │
└────────────────────┴────────────────────────────────────────────────────────┘
```
