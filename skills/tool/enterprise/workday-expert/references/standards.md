# Standards & Reference

## 7.1 Official Documentation

- [Workday Community](https://community.workday.com/)
- [Workday Human Capital Management Guides](https://doc.workday.com/)
- [Workday Web Services (REST API)](https://community.workday.com/document/78351)
- [Workday Studio / EIB Documentation](https://community.workday.com/file/17616)
- [Workday Adaptive Planning API](https://integration.workday.com/)
- [WorkdayPrism Analytics Docs](https://community.workday.com/node/198671)
- [WD-Keep API Reference](https://community.workday.com/author/wd-keep.html)

## 7.2 Configuration Reference

### Tenant-Specific Setup

| Item | Location | Notes |
|------|----------|-------|
| Tenant ID | `https://wd3-impl-services1.workday.com/ccx/api/v1/[tenant]` | Found in Workday URL |
| API Versioning | `/ccx/api/v1/[tenant]/[version]` | Use `v2`, `v3`, `v36.0` etc. |
| OAuth 2.0 | Authorization Server: `/ccx/oauth2/[tenant]/token` | Client Credentials or JWT |
| Sandbox | Append `-sb` to tenant ID | `tenant-sb` |

### Workday Roles & Security

| Role | Scope | Assigned To |
|------|-------|-------------|
| `System Implementer` | Full tenant config | Integration architects |
| `Integration System User` | API-only access | Service accounts |
| `Payroll Manager` | Payroll data | Payroll team |
| `HR Partner` | Worker data by business org | HR Business Partners |
| `Benefits Administrator` | Benefits domain | Benefits team |

### Business Process Framework

```
BP Configuration Fields:
├── Initiator              → Who can start the process
├── Actors                 → Assignees (supervisor, specific role, group)
├── Approval Chain         → Sequential or parallel stages
├── Conditions             → Routing logic (xpATH expressions)
├── Due Date / SLA         → Escalation timers
├── Request Participant    → Optional watchers
└── Events                 → On Complete, On Cancel, On Exception
```

### EIB (Enterprise Interface Builder)

| Component | Purpose |
|-----------|---------|
| Integration System | Defines inbound/outbound direction |
| Integration Cloud | Web Service, File (SFTP/Local/Workday) |
| Web Service Consumer | Invoke external REST/SOAP APIs |
| Workday Studio | Complex transformations (XSLT 2.0) |
| Template | Data format (CSV, XML, Fixed-width) |

## 7.3 Common Tasks

### Worker Data via REST API

```bash
# OAuth 2.0: Get Access Token
curl -X POST https://wd3-impl-services1.workday.com/ccx/oauth2/[tenant]/token \
  -H "Content-Type: application/x-www-form-urlencoded" \
  -d "grant_type=client_credentials&client_id=WD_CLIENT&client_secret=WD_SECRET"

# Get Worker by WID
curl -X GET "https://wd3-impl-services1.workday.com/ccx/api/v1/[tenant]/workers/[WID]" \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Accept: application/json"

# Get Workers (paginated)
GET /ccx/api/v1/[tenant]/workers?limit=100&offset=0&sort=workerNumber
```

### Business Process Condition (XPATH)

```xml
<!-- Spend: Expense Report Approval Condition -->
<wd:Condition>
    <wd:XPATH>wd:Total_Amount >= 1000 and wd:Payment_Type != "Personal Funds"</wd:XPATH>
</wd:wd:Condition>

<!-- HR: Manager Change Approval -->
<wd:Condition>
    <wd:XPATH>wd:Current_Management_Level_Above_Change > 3</wd:XPATH>
</wd:Condition>
```

### Tenant-Tagged Values

```
Common Tags:
wd:Worker_Reference/wd:ID[@wd:type='WID']     → Primary key (WID)
wd:Worker_Reference/wd:ID[@wd:type='Employee_ID'] → EMP001234
wd:Supervisory_Organization_Reference/wd:ID[@wd:type='Organization_ID']
wd:Business_Title
wd:Legal_Name
wd:Primary_Work_Email
wd:Date_of_Birth
wd:Effective_Shared_Start_Date
```

## 7.4 Version & Platform Compatibility

| Workday Release | Version Code | Release Date |
|-----------------|-------------|--------------|
| 2024 R1 | v40.0 | Jan 2024 |
| 2024 R2 | v41.0 | May 2024 |
| 2025 R1 | v42.0 | Jan 2025 |
| 2025 R2 | v43.0 | May 2025 |
| 2026 R1 | v44.0 | Jan 2026 |
| Current (March 2026) | **v44.0 / 2026 R1** | Current |

| Feature | Minimum Version | Notes |
|---------|----------------|-------|
| REST API v2 | v30.0+ | Recommended over v1 |
| JSON API responses | v33.0+ | Default from this version |
| JWT Bearer Auth | v34.0+ | Preferred over OAuth v1 |
| Workday Payroll | v30.0+ | Cloud payroll modules |
| Prism Analytics | v35.0+ | Adaptive Analytics |
| Skills Cloud | v38.0+ | AI-powered skills matching |
| HCM Atom Feed | v1.0+ | Legacy, use REST v2+ |

> **Note:** Workday releases twice yearly (January + May). API version matches release number. Always pin integration to specific API version in production.
