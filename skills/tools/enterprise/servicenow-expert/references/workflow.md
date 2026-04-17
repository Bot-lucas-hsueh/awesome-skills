# Standard Workflow

## 8.1 Admin Workflow

### Initial Instance Setup

```
1. Instance provisioning (dev/test/prod)
2. Configure MID Server (for on-prem integrations)
3. Set up LDAP/SSO authentication
4. Enable required plugins (ITSM, HR, CSM, etc.)
5. Configure Glenn Charts → Enable "Glide Chart" plugin
6. Import baseline data: Reference tables, CMDB
7. Define email servers and notification rules
8. Set up SLA schedules and business hours
9. Configure domain separation (if multi-tenant)
10. Role assignment and group structure
```

### Development Lifecycle

```
Phase 1: Studio/IDE Development
├── Create application in Studio or IDE plugin
├── Write Business Rules, Script Includes, ACLs
├── Unit test with `gs.info()` and background scripts
└── Commit to source control (Git via VS Code plugin)

Phase 2: CI/CD Pipeline
├── Automated unit tests via jest-sn十八 / GlideUnitTestRunner
├── Migration Sets or Update Sets to move between instances
└── Git Integration (Paris+): clone → commit → deploy

Phase 3: Promotion
├── dev → test (via update set or Git)
├── test → stage (regression testing)
└── stage → prod (controlled deployment window)
```

## 8.2 User Workflow

### Incident Management (ITIL)

```
User reports issue
    │
    ├─ Portal / Service Catalog request
    │
    ├─ Incident created (auto-assigned via Assignment Rules)
    │   ├── P1 → Manager notification
    │   ├── P2-P3 → Assignment group routing
    │   └── P4-P5 → Self-service resolution
    │
    ├─ Resolution work in progress (state=In Progress)
    │   ├── Work notes (internal)
    │   ├── Journal entries (audit trail)
    │   └── CI lookup via CMDB
    │
    ├─ SLA breach warning at 75% elapsed
    │
    └─ Resolution & closure
        ├── State → Resolved (awaiting confirmation)
        └── State → Closed
```

### Change Management

```
Standard Change:
RFC submitted → CAB review (auto/not required based on risk) → Approved → 
Implementation → Post-change review → Closed

Normal Change:
RFC submitted → CAB approval required → Risk assessment → 
Scheduled blackout window → Implementation → Post-change review → Closed

Emergency Change:
Express CAB (2 approvers) → Immediate implementation → 
Post-implementation review within 72h → Closed
```

## 8.3 Integration Workflow

### REST API Integration

```javascript
// Outbound REST message using Script Include
var r = new sn_ws.RESTMessageV2();
r.setHttpMethod('POST');
r.setEndpoint('https://your-system.com/api/v1/incidents');
r.setRequestHeader('Authorization', 'Bearer ' + gs.getProperty('api.token'));
r.setRequestHeader('Content-Type', 'application/json');

var body = {
    short_description: current.short_description,
    caller: current.caller_id.getDisplayValue(),
    priority: current.priority.getDisplayValue(),
    sys_id: current.sys_id + ''
};

r.setRequestBody(JSON.stringify(body));
var response = r.execute();
var httpStatus = response.getStatusCode();
var responseBody = JSON.parse(response.getBody());
```

### Inbound REST (Scripted REST API)

```javascript
// Scripted REST Resource: /api/x_itsm/incident_sync
(function process(/\* RESTAPIRequest\*/ request, /\* RESTAPIResponse\*/ response) {
    var data = request.body.data;
    
    var inc = new GlideRecord('incident');
    inc.initialize();
    inc.short_description = data.short_description;
    inc.description = data.description;
    inc.caller_id = data.caller_sys_id;
    inc.priority = data.priority;
    var sysId = inc.insert();
    
    response.setStatus(201);
    response.setBody({ sys_id: sysId, status: 'created' });
})(request, response);
```

### Webhook / Flow Integration Hub

```
Trigger: Record Created on incident (state = -1)
    │
    ├─ Integration Hub Spoke: Microsoft Teams
    │   └── Post message: "New incident: [short_description]"
    │
    ├─ Integration Hub Spoke: Slack
    │   └── Send notification to #it-ops channel
    │
    └─ Integration Hub Spoke: ServiceNow ITSM
        └── Cross-scope record creation
```

### Table API (OAuth 2.0)

```bash
# Step 1: Get OAuth token
curl -X POST https://INSTANCE.service-now.com/oauth_token.do \
  -d "grant_type=password" \
  -d "client_id=OAUTH_CLIENT_ID" \
  -d "client_secret=OAUTH_CLIENT_SECRET" \
  -d "username=admin" \
  -d "password=admin_password"

# Step 2: Use token for table API
curl -X GET https://INSTANCE.service-now.com/api/now/table/incident \
  -H "Authorization: Bearer ACCESS_TOKEN" \
  -H "Accept: application/json"
```
