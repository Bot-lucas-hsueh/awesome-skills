# CrowdStrike Workflows & Scenarios Reference

> Complete workflows and real-world scenarios for CrowdStrike Falcon operations. Load when asked about procedures, incident response, or threat hunting playbooks.

---

## §1 Threat Hunting Workflow

### 1.1 Hypothesis-Driven Hunting Model

```
┌──────────────────────────────────────────────────────────────────────┐
│                    CROWDSTRIKE THREAT HUNTING CYCLE                │
├──────────────────────────────────────────────────────────────────────┤
│                                                                      │
│   ┌───────────────┐    ┌───────────────┐    ┌───────────────┐     │
│   │ HUNT          │───→│ INVESTIGATE   │───→│ VALIDATE      │     │
│   │ (Hypothesis)  │    │ (Data Search) │    │ (Confirm)     │     │
│   └───────────────┘    └───────────────┘    └───────────────┘     │
│          ↑                                              │           │
│          │         ┌───────────────┐                   │           │
│          └─────────│ DOCUMENT     │───────────────────┘           │
│                    │ & FEEDBACK   │                               │
│                    └───────────────┘                               │
└──────────────────────────────────────────────────────────────────────┘
```

### 1.2 Hunting Methodology Steps

| Step | Action | Tool | Output |
|------|--------|------|--------|
| 1 | Form hypothesis based on intel, MITRE, anomalies | N/A | Documented hypothesis |
| 2 | Identify relevant data sources | Event Search | Data source list |
| 3 | Execute hunt queries | Event Search / Falcon UI | Raw findings |
| 4 | Analyze patterns, cluster behaviors | Manual + Falcon Spotlight | Anomaly list |
| 5 | Validate with additional data | RTR, memory forensics | Confirmed threat or FP |
| 6 | Contain if confirmed | Falcon console, RTR | Host isolated |
| 7 | Document and share IOCs | Falcon X, Falcon UI | Hunt report, updated detections |

### 1.3 Common Hunting Hypotheses

| Category | Hypothesis Template | Example Query Trigger |
|---------|--------------------|-----------------------|
| Execution | "Adversary may have executed via [technique]" | PowerShell from Office, LOLBins |
| Persistence | "Adversary may have established [mechanism]" | New scheduled task, registry Run key |
| C2 | "Adversary may be using [protocol] for C2" | Long DNS queries, HTTPS to non-standard ports |
| Lateral | "Adversary may have moved laterally via [method]" | SMB from workstation to server |
| Exfil | "Adversary may be exfiltrating via [channel]" | Large outbound to new destination |

---

## §2 Incident Response Playbook

### 2.1 Falcon-Specific IR Lifecycle

```
┌─────────────────────────────────────────────────────────────────────┐
│ DETECTION → TRIAGE → CONTAINMENT → ERADICATION → RECOVERY → LESSONS│
│     ↓           ↓            ↓              ↓           ↓            ↓
│  Falcon      Falcon UI   Falcon RTR   Falcon    Falcon    Update
│  Prevent     + OverWatch + Fusion    Prevent   Restore   Detections
│  + Insight   Severity   SOAR        + Manual  Backups   + Intel
└─────────────────────────────────────────────────────────────────────┘
```

### 2.2 Severity Classification

| Severity | Definition | SLA | Example |
|----------|-----------|-----|---------|
| CRITICAL | Active breach, ransomware, APT | Immediate (< 5 min) | Mass encryption, data exfil in progress |
| HIGH | Confirmed malware, lateral movement | 15 min | Rootkit, credential theft, C2 active |
| MEDIUM | Suspicious activity, potential threat | 1 hour | Novel technique, privilege escalation attempt |
| LOW | Informational, likely FP | 4 hours | Minor policy violation, unusual but benign |

### 2.3 Containment Playbook

**Step 1: Network Containment (Immediate)**
```
Falcon Console → Hosts → Select Host → Actions → Network Containment
```
- Isolates host from network while sensor remains active
- SSH/RDP access via Falcon RTR still works
- Auto-removes after 24h unless extended

**Step 2: Process Termination**
```
Falcon UI → Processes → Select Malicious Process → Kill Process
OR
RTR: kill <pid>
```

**Step 3: Persistence Removal**
```
RTR: rm /path/to/payload.exe
RTR: reg delete "HKLM\...\SuspiciousKey" /f
RTR: netsh advfirewall firewall delete rule name="malicious rule"
```

**Step 4: Host Remediation**
```
RTR: execute /tmp/remediation_script.sh
OR
Falcon Complete: Request analyst-led remediation
```

### 2.4 Host Recovery Steps

| Phase | Action | Tool/Method |
|-------|--------|-------------|
| Validate | Confirm no active threats | Event Search: confirm no C2, no persistence re-established |
| Clean | Rebuild or restore from snapshot | Falcon RTR or IT orchestration |
| Re-onboard | Reinstall sensor if needed | Falcon installer |
| Monitor | 72-hour enhanced monitoring | OverWatch escalation for 72h |
| Document | Record IOCs, timeline, lessons | Falcon case notes + external report |

---

## §3 Scenario Examples

### Scenario 1: APT Detection via PowerShell + Macro Chain

**Trigger:** OverWatch alert — PowerShell spawning from Microsoft Excel with suspicious command line.

**Falcon UI Investigation:**
1. Navigate to Hosts → select affected endpoint
2. Review process timeline for `excel.exe → powershell.exe`
3. Identify full command line with encoded content

**Event Search Query:**
```powershell
event_simpleName=ProcessRollup2
| search FileName="*powershell*" ParentBaseFileName="*excel*"
| eval decoded=base64_decode(split(CommandLine, "-enc")[1])
| table _time, ComputerName, UserName, ParentBaseFileName, CommandLine, decoded
```

**Findings:**
- Excel macro spawned PowerShell with base64-encoded command
- PowerShell downloaded payload from `malicious-c2[.]xyz`
- C2 domain registered 2 hours before attack

**Response:**
| Action | Method | Time |
|--------|--------|------|
| Network isolate host | Falcon Console | T+2min |
| Kill malicious processes | Falcon UI | T+3min |
| Collect forensic snapshot | Falcon RTR memdump | T+5min |
| Hunt for IOCs enterprise-wide | Event Search | T+10min |
| Block C2 domain in firewall | Falcon Prevent policy | T+12min |
| Report to OverWatch | Falcon UI → Share | T+15min |

**IOCs Extracted:**
```
Domain: malicious-c2[.]xyz
SHA256: abc123...def456 (dropper)
SHA256: fed789...ghi012 (payload)
IP: 198.51.100[.]42
Tactic: T1059.001 (PowerShell), T1105 (Ingress Tool Transfer)
```

---

### Scenario 2: Ransomware Outbreak — 1-10-60 Response

**Trigger:** Falcon Insight alert — Mass file encryption detected on file server.

**Timeline:**
| Time | Action | Mechanism |
|------|--------|-----------|
| T+0s | Alert fires: `RansomwareBehavioralNotification` | ML behavioral detection |
| T+15s | Auto-isolation of 12 affected hosts | Falcon Fusion SOAR automation |
| T+45s | Analyst confirms: LockBit 3.0 variant | Falcon X malware analysis |
| T+2min | Kill encryption processes across all hosts | RTR batch script |
| T+5min | Block C2 domains and TOR exit nodes | Falcon Prevent policy |
| T+15min | Isolate unaffected critical assets | Falcon Console |
| T+30min | Begin recovery from immutable backups | IT + Falcon Complete |
| T+2hr | All critical services restored | - |
| T+4hr | Full enterprise scan for residual threat | Event Search sweep |

**Key Decisions:**
- **Did NOT pay ransom** — Falcon X had decryptor available
- **Immediately isolated** — prevented spread to backup infrastructure
- **OverWatch engaged** — confirmed no nation-state involvement (pure eCrime)

**Post-Incident:**
- Added custom IOA for LockBit TTPs (volume shadow deletion, .txt ransom note pattern)
- Tightened backup isolation policy
- Conducted company-wide phishing simulation
- Updated server prevention policy to "aggressive" mode

---

### Scenario 3: Supply Chain Compromise (SolarWinds-Style)

**Trigger:** Threat intel — APT actor using software update mechanism for initial access.

**Hunting Query:**
```powershell
# Hunt for suspicious software update activity
event_simpleName IN (ProcessRollup2, NetworkAccessLog)
| search (FileName="*updater*" OR FileName="*update*" OR ImageFileName="*update*")
AND (RemoteAddress IN (source("malicious-ip-list"))
     OR RemoteAddressType="External")
| stats values(CommandLine) as commands, count
  by ComputerName, UserName, FileName, RemoteAddress
| where count > 5
```

**Investigation Steps:**
1. Identify all hosts running affected software → `HostSearch`
2. Query for network connections to malicious C2 IPs → `NetworkAccessLog`
3. Check for DLL sideloading patterns → `ModuleLoad`
4. Review process tree of update service → `ProcessTree`
5. Extract memory for forensic analysis → `RTR memdump`

**Falcon Spotlight Integration:**
- Flag all known vulnerable versions of affected software
- Prioritize patching based on network exposure
- Monitor for exploit attempts targeting unpatched systems

---

### Scenario 4: Insider Threat — Credential Abuse

**Trigger:** HR alert — IT admin with recent termination notice accessed sensitive database.

**Falcon Query:**
```powershell
# Detect privileged account anomalous access
event_simpleName=ProcessRollup2
| search UserName="*jsmith*"
| search (CommandLine="*mysql*" OR CommandLine="*psql*" OR CommandLine="*sqlplus*")
| eval timestamp=strftime(_time, "%Y-%m-%d %H:%M:%S")
| table timestamp, ComputerName, UserName, CommandLine, TargetFileName
| sort - timestamp
```

**Additional Queries:**
```powershell
# Unusual data access volume
event_simpleName IN (FileCreate, DnsRequest)
| search UserName="*jsmith*"
| stats sum(FileSize) as total_bytes, dc(DomainName) as unique_dest
  by ComputerName, UserName
| where total_bytes > 100000000 OR unique_dest > 100

# Access outside normal working hours
event_simpleName=ProcessRollup2
| search UserName="*jsmith*"
| eval hour=extract("^\\d{4}-\\d{2}-\\d{2} (\\d{2})", _time)
| search hour<6 OR hour>22
| table _time, ComputerName, UserName, FileName, CommandLine
```

**Findings:**
- Admin accessed production database at 3:00 AM
- Downloaded 50GB of customer records to USB-attached drive
- File transfer detected via `FileCreate` + removable media policy

**Response:**
- Immediate credential revocation (via Azure AD + Falcon Complete)
- Evidence preservation for legal team
- Escalation to Legal, HR, and Executive team
- Law enforcement notification (depending on data sensitivity)

---

### Scenario 5: Cloud Workload Protection — Container Escape

**Trigger:** Falcon container security alert — Abnormal namespace activity in Kubernetes pod.

**Falcon Query:**
```powershell
# Detect container escape indicators
event_simpleName IN (ProcessRollup2, NetworkAccessLog)
| search CommandLine="*nsenter*" OR CommandLine="*crictl*" OR CommandLine="*docker*exec*"
| search ComputerName="*k8s*" OR ComputerName="*container*"
| stats count by ComputerName, UserName, CommandLine, ImageFileName
| sort - count
```

**Kubernetes Audit Log Correlation:**
- Identify which container attempted namespace entry
- Review Kubernetes API server logs for RBAC abuse
- Check for `hostPID` or `hostNetwork` privilege escalation

**Container-Specific Response:**
1. Isolate compromised pod → `kubectl get pod <name> -o json | jq '.spec.nodeName'`
2. Kill malicious container process via RTR on node
3. Block malicious image across cluster → Falcon container policy
4. Review admission controller logs → Falcon admission control alerts
5. Redeploy pods from verified image registry

---

## §4 Anti-Patterns & Fixes

| Anti-Pattern | Symptom | Falcon Fix |
|-------------|---------|-----------|
| Over-exclusion | High prevention bypass rate | Quarterly exclusion review; prefer ML exclusions |
| Alert fatigue | OverWatch reports ignored | Custom dashboard with severity filtering |
| Prevention-only | Missed dwell time indicators | Enable Falcon Insight detection alongside prevention |
| Static policies | Breach despite policies configured | Monthly policy review driven by threat intel |
| Ignoring OverWatch | APT missed for 30+ days | Mandatory 4-hour SLA for OverWatch report review |
| Legacy AV mindset | Signature-only reliance | Enable full behavioral + ML prevention |
| No IR plan | Dwell time 45+ days | Document and test Falcon IR playbooks quarterly |
| Siloed SOC | Hunting + SOC disconnected | Integrated dashboards, shared Falcon case management |

---

## §5 1-10-60 Framework Implementation

| Phase | Target | How Falcon Enables It |
|-------|--------|----------------------|
| **Detect** | 1 minute | ML behavioral detection, Smart Filtering, OverWatch |
| **Investigate** | 10 minutes | Event Search, process timeline, IOC enrichment via Falcon X |
| **Remediate** | 60 minutes | Network containment, RTR, Fusion SOAR, Falcon Complete |

**Falcon X IOC Enrichment:**
```powershell
# Enrich IOCs automatically via Falcon X API
# POST /falconx/entities/submissions/v1
{
  "samples": [
    {"sha256": "<suspect_hash>"},
    {"sample_url": "https://malicious-site.com/payload.exe"}
  ],
  "action": "all"
}
```
