# ServiceNow ITSM Deep Dive

## Overview
IT Service Management (ITSM) is ServiceNow's flagship product, powering IT workflows for 85% of Fortune 500 companies.

## Core Modules

### Incident Management
**Purpose:** Restore normal service operation as quickly as possible

**Key Concepts:**
- **Priority Matrix:** Impact × Urgency = Priority (1-5)
- **Major Incidents:** P1 incidents requiring special handling
- **SLAs:** Response and resolution time commitments
- **Incident State Flow:** New → In Progress → Resolved → Closed

**Best Practices:**
1. Use assignment rules to auto-route based on category
2. Implement major incident process for P1s
3. Enable self-service via Virtual Agent
4. Track mean time to resolve (MTTR)

### Problem Management
**Purpose:** Eliminate root causes of incidents

**Key Concepts:**
- **Root Cause Analysis:** 5 Whys, Fishbone diagrams
- **Known Error Database:** Documented workarounds
- **Problem State:** Draft → Root Cause Analysis → Fix in Progress → Closed

### Change Management
**Purpose:** Control the lifecycle of changes

**Change Types:**
| Type | Risk Level | Approval Required | Timeline |
|------|------------|-------------------|----------|
| Standard | Low | Pre-approved | Hours |
| Normal | Medium-High | CAB | Days-Weeks |
| Emergency | High | ECAB | Immediate |

**Risk Calculator:**
```
Risk Score = Impact (1-3) × Probability (1-3)
Score 1-3: Low Risk (Auto-approved if Standard)
Score 4-6: Medium Risk (Manager approval)
Score 7-9: High Risk (CAB required)
```

### Request Management
**Purpose:** Fulfill service requests efficiently

**Service Catalog:**
- Item categories: Hardware, Software, Access, Services
- Fulfillment workflows per item
- Approval matrices
- Asset integration

## Configuration

### Assignment Rules
```javascript
// Example: Route by category and location
if (current.category == 'Network' && current.location == 'EMEA') {
    current.assignment_group = 'Network EMEA';
}
```

### SLA Definitions
- **Response SLA:** Time to acknowledge/assign
- **Resolution SLA:** Time to resolve/close
- **Pause Conditions:** Awaiting user, vendor, change

### Workflow
```yaml
Incident Workflow:
  New:
    - Auto-assign based on rules
    - Send notification to assignee
  
  In Progress:
    - Track work notes
    - Update stakeholders
  
  Resolved:
    - Require resolution notes
    - Calculate resolution time
    - Send satisfaction survey
  
  Closed:
    - Archive after retention period
```

## Integration Points
- CMDB: CI relationships
- Asset Management: Hardware/software tracking
- Knowledge Management: Solution suggestions
- Virtual Agent: Self-service creation
