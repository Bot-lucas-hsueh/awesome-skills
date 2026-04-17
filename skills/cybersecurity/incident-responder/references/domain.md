## § 6 · Domain Knowledge

### 6.1 MITRE ATT&CK Framework

| Tactic | Common Techniques | Detection |
|--------|-------------------|-----------|
| **Initial Access** | Phishing, exploits | Email security, vulnerability management |
| **Execution** | PowerShell, WMI | Script blocking, command logging |
| **Persistence** | Registry run keys, services | Persistence hunting, autoruns |
| **Defense Evasion** | Process injection, obfuscation | Behavioral detection, memory scanning |
| **Credential Access** | Mimikatz, keylogging | Credential guard, monitoring |
| **Exfiltration** | C2 channels, cloud storage | DLP, network monitoring |

### 6.2 Evidence Collection Priority

| Priority | Evidence Type | Volatility |
|----------|---------------|------------|
| **1** | Memory (RAM) | Highest |
| **2** | Network connections | High |
| **3** | Running processes | High |
| **4** | Disk (full image) | Low |
| **5** | Logs (system, network) | Low |

### 6.3 Ransomware Response Playbook

1. **Isolate**: Disconnect affected systems from network
2. **Identify**: Determine ransomware variant (ID Ransomware)
3. **Assess**: Check for decryption tools (NoMoreRansom)
4. **Preserve**: Forensic imaging before any recovery
5. **Notify**: Law enforcement, cyber insurance
6. **Recover**: Restore from clean backups (verify first)
7. **Harden**: Patch, improve monitoring, user training

---
