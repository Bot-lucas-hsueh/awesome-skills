## §4 · Examples (Detailed)

### §4.1 Example: Major Incident Automation

**Context:** Design automated major incident response for critical (P1) incidents.

**Requirements:**
- Auto-trigger when incident priority = 1
- Create war room (MS Teams)
- Notify stakeholders via multiple channels
- Generate status page update
- Schedule bridge call

**Solution:**

```yaml
Flow: Major Incident Response Automation
Trigger: Incident record updated, Priority = 1

Actions:
  1. Validate Major Incident:
     - Check if already flagged as major
     - Verify incident category qualifies
  
  2. Create Major Incident Record:
     - Copy incident details
     - Set MI status = "Active"
     - Generate MI number
  
  3. Create War Room:
     - Integration Hub: Microsoft Teams spoke
     - Create channel: "INC-[number]-War-Room"
     - Add members: On-call team, managers, executives
     - Post initial incident summary
  
  4. Multi-Channel Notification:
     - Email: Executive leadership
     - SMS: On-call engineers (Twilio spoke)
     - Slack: #incidents channel
     - Status page: Post initial update
  
  5. Schedule Bridge Call:
     - Office 365 spoke: Create meeting
     - Add all stakeholders
     - Include bridge details in notifications
  
  6. Create Child Tasks:
     - Technical investigation
     - Communication management
     - Stakeholder updates (recurring every 15 min)

Error Handling:
  - Log all integration failures
  - Create retry tasks for failed notifications
  - Alert integration admin on 3rd failure
  - Maintain manual fallback procedures
```

**Implementation Script:**
```javascript
// Business Rule: Trigger Major Incident Flow
(function executeRule(current, previous) {
    // Only on priority change to 1
    if (current.priority != '1' || previous.priority == '1') {
        return;
    }
    
    // Check if already major incident
    if (current.major_incident) {
        return;
    }
    
    // Mark as major incident
    current.major_incident = true;
    current.major_incident_state = 'active';
    
    // Start Flow
    var flow = new sn_flow.Flow();
    var inputs = {
        'incident_id': current.sys_id.toString(),
        'incident_number': current.number.toString(),
        'short_description': current.short_description.toString(),
        'caller_id': current.caller_id.toString()
    };
    
    flow.startFlow('major_incident_response', inputs);
    
})(current, previous);
```

**Outcome:**
- Major incident response time: 5 min → 30 seconds
- Stakeholder notification: 100% coverage
- Mean time to war room: 2 minutes
- Executive visibility: Real-time dashboard

---

### §4.2 Example: Employee Onboarding Workflow

**Context:** End-to-end onboarding spanning HR, IT, Security, Facilities.

**Solution:**

```yaml
Flow: Employee Onboarding Orchestrator
Trigger: HR Case "New Hire" created

Parallel Branches:

  Branch A - IT Provisioning:
    - Create AD account (Integration Hub: Active Directory)
    - Assign laptop (Asset Management)
    - Setup email/calendar (Office 365)
    - Grant system access (based on role)
    - Notify manager when complete
  
  Branch B - Security Clearance:
    - Create Security case
    - Background check verification
    - Security training assignment
    - Badge creation request
    - Update employee record
  
  Branch C - Facilities:
    - Create Facilities request
    - Assign workspace
    - Parking pass allocation
    - Welcome kit preparation
  
  Branch D - HR Tasks:
    - Send welcome email
    - Schedule orientation
    - Collect documentation

Join & Completion:
  - Wait for all branches
  - Send completion notification to manager
  - Schedule first day calendar invite
  - Schedule 30/60/90 day check-ins
  - Queue onboarding survey
```

**Role-Based Asset Assignment:**
```javascript
// Script Include: Onboarding Automation
var OnboardingAutomation = Class.create();
OnboardingAutomation.prototype = {
    initialize: function() {},
    
    getRoleAssets: function(role) {
        var assetMap = {
            'Developer': ['Laptop-Dev', 'Monitor-Dual', 'Keyboard-Mechanical'],
            'Sales': ['Laptop-Standard', 'Headset-Noise-Canceling'],
            'Executive': ['Laptop-Premium', 'Monitor-UltraWide', 'Docking-Station'],
            'Designer': ['Laptop-Design', 'Tablet-Stylus', 'Monitor-Color']
        };
        return assetMap[role] || ['Laptop-Standard'];
    },
    
    assignAssets: function(employeeId, role) {
        var assets = this.getRoleAssets(role);
        assets.forEach(function(asset) {
            var req = new GlideRecord('sc_req_item');
            req.initialize();
            req.cat_item = this.getCatalogItem(asset);
            req.requested_for = employeeId;
            req.insert();
        }, this);
    },
    
    type: 'OnboardingAutomation'
};
```

**Outcome:**
- Onboarding time: 5 days → 2 days
- Manual tasks reduced: 80%
- New hire satisfaction: 4.6/5
- IT provisioning errors: -90%

---

### §4.3 Example: Custom Vendor Management App

**Context:** Build scoped application for vendor onboarding, performance, risk.

**Data Model:**
```yaml
Application: Vendor Management (x_vendor_mgmt)

Tables:
  Vendor:
    - name (string, required)
    - vendor_id (auto-number)
    - status (choice: Prospect, Active, Suspended, Terminated)
    - category (choice: Software, Hardware, Services, Consulting)
    - primary_contact (reference: Contact)
    - contract_value (currency)
    - risk_rating (choice: Low, Medium, High, Critical)
    - onboarding_date (date)
    - last_assessment_date (date)

  Vendor Assessment:
    - vendor (reference: Vendor)
    - assessment_date (date)
    - assessor (reference: User)
    - security_score (integer 1-10)
    - financial_score (integer 1-10)
    - operational_score (integer 1-10)
    - overall_score (calculated)
    - findings (html)
    - remediation_plan (html)

  Vendor Contract:
    - vendor (reference: Vendor)
    - contract_number (string)
    - start_date (date)
    - end_date (date)
    - value (currency)
    - renewal_reminder (boolean)
    - documents (attachment)
```

**Flows:**
```yaml
1. Vendor Onboarding Flow:
   Trigger: Vendor status changed to "Active"
   Actions:
     - Create assessment task
     - Notify procurement team
     - Add to vendor portal
     - Schedule 90-day review

2. Risk Assessment Reminder:
   Schedule: Weekly
   Actions:
     - Find vendors with assessment > 365 days old
     - Create assessment tasks
     - Email vendor managers

3. Contract Renewal Alert:
   Trigger: 90 days before end_date
   Actions:
     - Create renewal task
     - Notify contract owner
     - Update vendor status to "Renewal Pending"
```

**UI Builder Pages:**
```yaml
Vendor Portal:
  - Header: Vendor logo, status badge, risk indicator
  - Tabs:
    - Overview: Summary fields, key metrics
    - Assessments: Related list with scores
    - Contracts: Related list with renewal status
    - Performance: Charts (trend analysis)
  - Actions:
    - Request Assessment
    - Upload Documents
    - View Compliance Report

Vendor Manager Dashboard:
  - KPI Cards:
    - Total Active Vendors
    - High Risk Vendors
    - Contracts Expiring Soon
    - Pending Assessments
  - Charts:
    - Vendors by Category
    - Risk Rating Distribution
    - Assessment Trend (6 months)
  - Lists:
    - Vendors Requiring Action
    - Overdue Assessments
```

**Integration:**
```javascript
// External vendor data sync
var VendorSync = Class.create();
VendorSync.prototype = {
    initialize: function() {},
    
    syncFromDunBradstreet: function(vendorId) {
        var vendor = new GlideRecord('x_vendor_mgmt_vendor');
        if (!vendor.get(vendorId)) return;
        
        // Call D&B API via Integration Hub
        var action = new sn_integrationhub.Action('dun_bradstreet');
        var result = action.run('get_company_info', {
            'company_name': vendor.name.toString()
        });
        
        // Update vendor with D&B data
        vendor.duns_number = result.duns;
        vendor.credit_rating = result.credit_rating;
        vendor.annual_revenue = result.revenue;
        vendor.employee_count = result.employees;
        vendor.update();
    },
    
    type: 'VendorSync'
};
```

**Outcome:**
- Vendor onboarding: 30 days → 10 days
- Assessment completion: 95%
- High-risk vendor visibility: 100%
- Contract renewal on-time: 98%

---

### §4.4 Example: Enterprise Integration Architecture

**Context:** Connect ServiceNow with SAP, Salesforce, Workday, Azure AD.

**Architecture:**
```
┌─────────────────────────────────────────────────────────────────┐
│                    INTEGRATION ARCHITECTURE                      │
├─────────────────────────────────────────────────────────────────┤
│                                                                  │
│   ┌─────────────┐  ┌─────────────┐  ┌─────────────────────────┐ │
│   │     SAP     │  │  Salesforce │  │       Workday           │ │
│   │    (ERP)    │  │    (CRM)    │  │       (HR)              │ │
│   └──────┬──────┘  └──────┬──────┘  └───────────┬─────────────┘ │
│          │                │                       │              │
│   ┌──────┴────────────────┴───────────────────────┴──────┐      │
│   │              INTEGRATION HUB (Middleware)            │      │
│   │  • Spokes: SAP, Salesforce, Workday, Azure AD       │      │
│   │  • Flows: 50+ integration workflows                  │      │
│   │  • APIs: REST, SOAP, OData                          │      │
│   └────────────────────────┬─────────────────────────────┘      │
│                            │                                     │
│   ┌────────────────────────┴─────────────────────────────┐      │
│   │                    SERVICENOW                        │      │
│   │  • CMDB (system of record for IT)                   │      │
│   │  • ITSM (incidents, changes, requests)              │      │
│   │  • ITOM (events, discovery, mapping)                │      │
│   │  • HRSD (employee services)                         │      │
│   └──────────────────────────────────────────────────────┘      │
│                                                                  │
└─────────────────────────────────────────────────────────────────┘
```

**SAP Asset Sync:**
```javascript
var SAPAssetImport = Class.create();
SAPAssetImport.prototype = {
    initialize: function() {},
    
    transform: function(source, target, map, log, isUpdate) {
        // Map SAP fields to CMDB
        target.name = source.sap_asset_name;
        target.asset_tag = source.sap_asset_id;
        target.serial_number = source.sap_serial;
        target.model_id = this.findOrCreateModel(source.sap_model);
        target.owned_by = this.findUser(source.sap_cost_center);
        target.install_status = this.mapStatus(source.sap_status);
        return true;
    },
    
    mapStatus: function(sapStatus) {
        var statusMap = {
            'ACTIVE': '1',
            'INACTIVE': '6',
            'RETIRED': '7',
            'MAINTENANCE': '3'
        };
        return statusMap[sapStatus] || '6';
    },
    
    type: 'SAPAssetImport'
};
```

**Workday Employee Sync:**
```javascript
var EmployeeSync = Class.create();
EmployeeSync.prototype = {
    initialize: function() {},
    
    execute: function() {
        var action = new sn_integrationhub.Action('workday');
        var employees = action.run('get_employees', {
            'modified_since': gs.daysAgo(1)
        });
        
        employees.forEach(function(emp) {
            this.syncEmployee(emp);
        }, this);
    },
    
    syncEmployee: function(empData) {
        var user = new GlideRecord('sys_user');
        if (user.get('employee_number', empData.employee_id)) {
            user.email = empData.email;
            user.department = this.findDepartment(empData.dept_code);
            user.manager = this.findManager(empData.manager_id);
            user.update();
        } else {
            user.initialize();
            user.user_name = empData.email;
            user.first_name = empData.first_name;
            user.last_name = empData.last_name;
            user.email = empData.email;
            user.employee_number = empData.employee_id;
            user.insert();
        }
    },
    
    type: 'EmployeeSync'
};
```

**Outcome:**
- 15+ systems integrated
- 99.5% sync success rate
- Real-time employee provisioning
- Single source of truth for IT assets
- 40% reduction in manual data entry

---

### §4.5 Example: CMDB Cleanup & Optimization

**Context:** Optimize 500K+ CI CMDB with performance issues, duplicates, stale data.

**Phase 1: Assessment:**
```sql
-- Identify duplicate CIs by serial number
SELECT serial_number, COUNT(*) as count
FROM cmdb_ci
WHERE serial_number IS NOT NULL
GROUP BY serial_number
HAVING COUNT(*) > 1;

-- Find stale CIs (no updates in 1 year)
SELECT sys_class_name, COUNT(*)
FROM cmdb_ci
WHERE sys_updated_on < DATEADD(year, -1, GETDATE())
  AND operational_status = '1'
GROUP BY sys_class_name;
```

**Phase 2: Cleanup Script:**
```javascript
var CMBDCleanup = Class.create();
CMBDCleanup.prototype = {
    initialize: function() {
        this.batchSize = 1000;
        this.log = [];
    },
    
    mergeDuplicates: function() {
        var dupQuery = new GlideAggregate('cmdb_ci');
        dupQuery.groupBy('serial_number');
        dupQuery.addHaving('COUNT', '>', 1);
        dupQuery.query();
        
        while (dupQuery.next()) {
            var serial = dupQuery.serial_number;
            this.mergeCIsBySerial(serial);
        }
    },
    
    mergeCIsBySerial: function(serial) {
        var gr = new GlideRecord('cmdb_ci');
        gr.addQuery('serial_number', serial);
        gr.orderBy('sys_created_on');
        gr.query();
        
        if (gr.next()) {
            var masterId = gr.sys_id;
            while (gr.next()) {
                this.redirectRelationships(gr.sys_id, masterId);
                gr.deleteRecord();
            }
        }
    },
    
    archiveStaleCIs: function(daysOld) {
        var gr = new GlideRecord('cmdb_ci');
        gr.addQuery('sys_updated_on', '<', gs.daysAgo(daysOld));
        gr.addQuery('operational_status', '!=', '7');
        gr.setLimit(this.batchSize);
        gr.query();
        
        while (gr.next()) {
            gr.operational_status = '7';  // Retired
            gr.update();
        }
    },
    
    type: 'CMBDCleanup'
};
```

**Phase 3: Maintenance Schedule:**
```yaml
Daily:
  - Duplicate detection report
  - Orphaned CI cleanup
  
Weekly:
  - Stale CI identification
  - Data quality score calculation
  
Monthly:
  - Full reconciliation with discovery
  - Certification campaign
```

**Outcome:**
- CMDB size: 500K → 320K (36% reduction)
- Query performance: 3s → 200ms
- Service mapping accuracy: 75% → 95%
- Duplicate records: 45K → 0
- Data quality score: 68% → 92%

---
