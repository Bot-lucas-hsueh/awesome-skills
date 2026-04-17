## § 8 · Scenario Examples

### Scenario 1: Greenfield Falcon Deployment
**Context**: 5,000-employee company with no EDR, wants comprehensive endpoint security.

**Expert Response:**

**Phase 1: Foundation (Weeks 1-2)**
```
Deployment Strategy:
├── Week 1: Ring 0 (50 IT devices)
│   └── Validate sensor stability, policy effectiveness
├── Week 2: Ring 1 (500 non-critical endpoints)
│   └── Monitor for compatibility issues, tune policies
├── Week 3: Ring 2 (2,000 standard users)
│   └── Scale deployment, establish support procedures
├── Week 4: Ring 3 (2,450 remaining + servers)
│   └── Complete coverage, server-specific policies
```

**Key Configurations:**
- Prevention Policy: Aggressive ML + Exploit protection
- Detection Policy: Enable all behavioral IOAs
- Update Rings: 4 rings (24h-96h observation periods)
- OverWatch: Full Elite tier for 24/7 hunting

**Success Metrics:**
- 100% sensor coverage by Week 4
- Zero critical compatibility issues
- <0.1% false positive rate
- First OverWatch detection within 48 hours

### Scenario 2: July 2024 Incident Preparedness
**Context**: CISO wants assurance against vendor update failures.

**Expert Response:**

**Risk Mitigation Framework:**
```yaml
update_governance:
  staged_rollout:
    ring_0:
      scope: internal_it
      size: 50_devices
      observation: 24_hours
      rollback_trigger: ">0.1% issues"
    ring_1:
      scope: non_critical
      size: 5_percent
      observation: 48_hours
      rollback_trigger: ">0.05% issues"
    ring_2:
      scope: standard_users
      size: 25_percent
      observation: 72_hours
    ring_3:
      scope: critical_systems
      size: remaining
      observation: 96_hours
  
  emergency_procedures:
    automated:
      - sensor_health_monitoring
      - crash_rate_alerts
      - automatic_deployment_halt
    manual:
      - emergency_rollback_runbook
      - bitlocker_recovery_procedures
      - alternative_protection_activation
  
  business_continuity:
    - air_gapped_recovery_workstations
    - offline_backup_validation
    - manual_ir_procedures
    - vendor_escalation_contacts
```

### Scenario 3: Cloud-Native Security Transformation
**Context**: Company migrating to AWS/Azure with containerized workloads.

**Expert Response:**

**CNAPP Architecture:**
```
Multi-Cloud Security Stack:
├── Falcon Horizon (CSPM)
│   ├── AWS Security Hub integration
│   ├── Azure Security Center connector
│   ├── CIS benchmarks (Level 1 & 2)
│   └── Custom IOMs for organizational policies
├── Falcon Cloud Workload (CWP)
│   ├── EKS/AKS admission controller
│   ├── Container image scanning
│   ├── Runtime protection
│   └── Serverless function monitoring
├── Falcon Identity (CIEM)
│   ├── Cross-cloud entitlement visibility
│   ├── Least privilege recommendations
│   └── Anomalous access detection
└── Shift-Left Security
    ├── Terraform/IaC scanning
    ├── GitHub Actions integration
    ├── SCA and SBOM generation
    └── Developer security training
```

### Scenario 4: Insider Threat Investigation
**Context**: Suspicious data access patterns from privileged admin.

**Expert Response:**

**Investigation Workflow:**
```powershell
# Identity-focused Event Search queries

# Query 1: Unusual data access volume
event_simpleName=SensitiveDataAccess 
| eval TimeBin=round(_time/3600)
| stats count, sum(DataVolumeMB) as TotalMB by UserName, TimeBin
| eventstats avg(TotalMB) as AvgMB, stdev(TotalMB) as StdevMB by UserName
| eval IsAnomaly=if(TotalMB > (AvgMB + 3*StdevMB), 1, 0)
| where IsAnomaly=1

# Query 2: Off-hours privileged access
event_simpleName=UserLogon 
| eval Hour=strftime(_time, "%H")
| eval IsOffHours=if(Hour < 6 OR Hour > 22, 1, 0)
| where IsOffHours=1 AND UserIsAdmin=1
| stats count by UserName, ComputerName, Hour
| where count > 3

# Query 3: Lateral movement indicators
event_simpleName=RemoteResponse 
| search TargetHostName!=ComputerName
| stats count, values(TargetHostName) as AccessedHosts by UserName
| where count > 5
```

**Response Actions:**
1. Immediate suspension of suspect account
2. Forensic preservation of relevant systems
3. HR and Legal notification per policy
4. Comprehensive audit of data accessed
5. Enhanced monitoring for related accounts


