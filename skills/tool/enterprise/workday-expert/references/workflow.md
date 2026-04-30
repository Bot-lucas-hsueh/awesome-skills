# Standard Workflow

## 8.1 Admin Workflow

### Tenant Configuration

```
1. Initial tenant setup
   ├── Provision tenant (prod + sandbox)
   ├── Configure SSO (SAML 2.0 / OIDC with IdP)
   ├── Set up Integration System User (ISU) for API access
   └── Register OAuth 2.0 application (client credentials)

2. Core HCM Configuration
   ├── Configure Organizations (Supervisory, Matrix, Cost Center)
   ├── Set up Job Profiles and Compensation Grades
   ├── Define Pay Groups and Pay Periods
   ├── Configure Benefit Plans and Eligibility Rules
   └── Set up Document Types and E-Signatures

3. Security & Compliance
   ├── Assign security groups and roles
   ├── Configure data privacy settings (GDPR, CCPA)
   ├── Enable audit logging for sensitive data access
   └── Set up segregation of duties policies

4. Integration Setup
   ├── Configure EIB (Enterprise Interface Builder)
   ├── Set up SFTP endpoints for file-based integrations
   ├── Register web service consumers (REST/SOAP)
   └── Configure workday Studio for complex transformations
```

### API Versioning Lifecycle

```
Deprecated Version Announcement
         │
         ├─ 6 months before sunset: Warning headers in API responses
         │
         ├─ 3 months before sunset: /v1 deprecated, migration guides published
         │
         └─ Sunset date: /v1 returns 410 Gone

Migration:
/ccx/api/v1/[tenant]/workers   →  /ccx/api/v2/[tenant]/workers
/cross tenant: /ccx/api/v1/[tenant1]/workers → /ccx/api/v2/[tenant1]/workers
```

## 8.2 User Workflow

### Employee Self-Service

```
Employee logs in to Workday
         │
         ├─ View Payslip: Pay → Pay Stubs → View current period
         │
         ├─ Request Time Off: Time → Request Time Off → Submit → 
         │    Supervisor approval → Calendar auto-updated
         │
         ├─ Update Personal Info: Profile → Personal Information → Edit →
         │    Pending HR review for sensitive changes
         │
         ├─ Enroll in Benefits: Benefits → Open Enrollment →
         │    Select plans → Dependent enrollment → Confirmation
         │
         └─ Performance Review: Performance → Self-assessment →
              Complete goals → Submit for manager review
```

### Manager Workflow

```
Hiring Request (from HRBP)
         │
         ├─ Create Job Requisition: Staffing → Create Requisition →
         │    Position details → Salary range → Hiring manager
         │
         ├─ Post to Job Board: Workday Recruiting integration
         │
         ├─ Review Applicants: Inbox → Applicant Review →
         │    Scorecard → Schedule interview → Offer letter
         │
         ├─ Onboarding: New hire activated →
         │    Workday onboarding tasks → Day 1 checklist
         │
         └─ Performance: Team performance cycle →
              Goal setting → Mid-year check → Annual review
```

## 8.3 Integration Workflow

### REST API: OAuth 2.0 Client Credentials

```python
import requests
import json

TENANT = "your-tenant-name"
CLIENT_ID = "your-client-id"
CLIENT_SECRET = "your-client-secret"
AUTH_URL = f"https://wd3-impl-services1.workday.com/ccx/oauth2/{TENANT}/token"

# Step 1: Get token
auth_response = requests.post(
    AUTH_URL,
    data={
        "grant_type": "client_credentials",
        "client_id": CLIENT_ID,
        "client_secret": CLIENT_SECRET
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)
token = auth_response.json()["access_token"]

# Step 2: Get workers
headers = {"Authorization": f"Bearer {token}", "Accept": "application/json"}
workers_response = requests.get(
    f"https://wd3-impl-services1.workday.com/ccx/api/v1/{TENANT}/workers?limit=50",
    headers=headers
)
workers = workers_response.json()["data"]
for w in workers:
    print(f"{w['descriptor']} - {w['primary_work_email']}")
```

### Inbound EIB: Load Workers from External System

```
1. Create Integration System: "External HR to Workday"
2. Create Web Service Consumer: Point to source system's WSDL
3. Create Integration Cloud:
   ├── Source: Web Service Consumer
   └── Destination: Workday (supervisory organization)
4. Transform:
   ├── Map External Employee ID → Worker ID
   ├── Map Source fields → Workday datatypes
   └── Use WD for null handling: wd:Worker/wd:Worker_Data/wd:Employment_Data/wd:Worker_Type = "Contingent_Worker_Type"
5. Schedule: Daily at 2:00 AM (off-peak)
6. Error Handling: Redirect error files to /errors/ with timestamp
7. Validation Report: Email summary to integration team
```

### Webhook / Change Event Integration

```json
// Workday Outbound Delivered Change Events (Webhook)
POST https://your-webhook-endpoint.com/workday/events

Headers:
  Authorization: Bearer YOUR_WEBHOOK_SECRET
  Content-Type: application/json
  X-Workday-Signature: sha256=abc123...

Body:
{
  "eventType": "worker.created",
  "eventOrigin": "HCM_Suite/WD",
  "eventSchemaVersion": "1.0",
  "eventId": "evt-abc123",
  "eventTimestamp": "2026-03-19T10:30:00Z",
  "payload": {
    "worker": {
      "WID": "1a2b3c4d...",
      "Employee_ID": "EMP001234",
      "Legal_Name": {
        "Formatted_Name": "Jane Doe"
      },
      "Primary_Work_Email": "jane.doe@company.com"
    }
  }
}
```

### Cross-Tenant Integration (Interac)

```
Tenant A (Acme Corp) → Tenant B (Subsidiary Inc)
         │
         ├─ Outbound from Tenant A: Create Workday Connection in Tenant B
         │   Configure: Tenant B ISU credentials + endpoint
         │
         ├─ Create Integration System in Tenant A: "HCM Data to Subsidiary"
         │   Outbound Web Service → "Tenant B" target
         │
         ├─ Grant Tenant A ISU access in Tenant B:
         │   Security → Register External System → Acme Corp ISU
         │
         └─ Data flow: Worker changes in Tenant A →
              EIB Outbound → Transform → REST call to Tenant B →
              Tenant B inbound EIB loads data
```
