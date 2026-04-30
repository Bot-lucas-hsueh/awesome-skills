## § 8 · Scenario Examples

### Example 1: Ransomware Attack Response

**Context**: Organization hit with Conti ransomware, 500 servers encrypted.

**Response**:
```
Hour 0: Detection
├── Ransom note discovered on file servers
├── IR team activated, legal notified
├── Network segmentation initiated

Hour 2: Containment
├── Isolate all affected systems
├── Preserve forensic images of critical servers
├── Identify backup systems (air-gapped, intact)

Hour 6: Investigation
├── Initial access: Phishing email 3 days ago
├── Lateral movement: RDP with compromised creds
├── Persistence: Registry run keys
├── Scope: 500 servers, no evidence of data theft

Day 2: Recovery
├── Rebuild from clean golden images
├── Restore data from offline backups
├── Reset all domain credentials
├── Deploy EDR to all endpoints

Post-Incident:
├── Executive briefing completed
├── FBI notified
├── Security awareness training enhanced
├── RDP access removed, MFA enforced
```

---

### Example 2: Data Exfiltration Investigation

**Context**: Alert on large data transfer to unknown cloud storage.

**Investigation**:
```
Detection:
├── DLP alert: 50GB uploaded to personal Dropbox
├── User: Marketing manager account

Analysis:
├── Account had suspicious login from foreign IP
├── Phishing email found in deleted items
├── No malware detected (credential theft only)
├── Data: Customer PII and financial records

Response:
├── Account disabled immediately
├── Dropbox legal request for data deletion
├── Affected customers notified (GDPR/CCPA)
├── Credit monitoring offered
├── Phishing simulation for all users
```

---

### Example 3: Insider Threat Investigation

**Context**: Suspicious database queries by employee leaving for competitor.

**Investigation**:
```
Indicators:
├── Employee resigned, going to competitor
├── Unusual after-hours database access
├── Large CSV exports from customer database

Forensics:
├── Database audit logs analyzed
├── Email communications reviewed (legal hold)
├── USB device usage examined

Findings:
├── 10,000 customer records exported
├── Evidence of intent (email to personal account)

Actions:
├── Law enforcement notified
├── Civil litigation initiated
├── Access revoked
├── Data loss assessment for customers
```

---

### Example 4: Nation-State APT Investigation

**Context**: Advanced persistent threat detected in government contractor network.

**Response**:
```
Characteristics:
├── Custom malware (no AV signatures)
├── Living-off-the-land techniques
├── Long dwell time (6+ months undetected)
├── Target: Defense project files

Investigation:
├── Memory forensics reveals sophisticated implant
├── C2 infrastructure analysis (attribution clues)
├── Lateral movement mapping
├── Data staging identification

Coordination:
├── FBI and DHS notified
├── Threat intelligence sharing (ISAC)
├── Counter-intelligence briefing
├── Network rebuild from scratch
```

---

### Example 5: Supply Chain Attack Response

**Context**: Compromised software vendor, backdoor in legitimate update.

**Response**:
```
Scope:
├── 1000+ customers received backdoored update
├── Backdoor active for 3 months

Investigation:
├── Identify all affected systems
├── Timeline of backdoor activity
├── Determine data access potential

Containment:
├── Emergency patch from vendor
├── Mass deployment to all endpoints
├── Enhanced monitoring for IOCs
├── Threat hunting for related activity

Communication:
├── Customer notification
├── CISA advisory
├── Media response
```

---
