# Scenario Examples

## 9.1 Team Workflows

### Scenario: Team Wiki Management

**User:** "How should we structure our team wiki in Notion?"

**Expert:**
> **Team Wiki Structure:**
>
> ```
> Team Wiki
> ├── Getting Started
> │   ├── Onboarding Checklist
> │   ├── Tools & Access
> │   └── Team Norms
> ├── Engineering
> │   ├── Architecture Docs
> │   ├── Runbooks
> │   └── API Documentation
> ├── Product
> │   ├── Roadmap
> │   ├── PRDs
> │   └── Meeting Notes
> └── Design
>     ├── Style Guide
>     ├── Component Library
>     └── Design Reviews
> ```
>
> **Best Practices:**
> - Use templates for consistency
> - Link related pages with `@` mentions
> - Keep pages focused, split long pages

### Scenario: OKR Tracking

**User:** "How do we track OKRs in Notion?"

**Expert:**
> **OKR Database Structure:**
>
> 1. **Objective Database:**
>    - Title (objective name)
>    - Quarter (select: Q1 2024, etc.)
>    - Owner (person)
>    - Status (progress percentage)
>    - Linked Key Results (relation)
>
> 2. **Key Results Database:**
>    - Title
>    - Objective (relation)
>    - Target value
>    - Current value
>    - Unit (%, $, count)
>
> 3. **Weekly Check-in Database:**
>    - Date
>    - Key Result (relation)
>    - Notes
>    - Confidence (1-10)

## 9.2 Automation Scenarios

### Notion Database Queries

```json
// Query: Tasks due this week
{
  "filter": {
    "and": [
      { "property": "Status", "status": { "does_not_equal": "Complete" } },
      { "property": "Due", "date": { "this_week": {} } }
    ]
  },
  "sorts": [{ "property": "Due", "direction": "ascending" }]
}

// Query: Overdue tasks
{
  "filter": {
    "and": [
      { "property": "Due", "date": { "before": "today" } },
      { "property": "Status", "status": { "does_not_equal": "Complete" } }
    ]
  }
}

// Query: High priority items
{
  "filter": {
    "or": [
      { "property": "Priority", "select": { "equals": "Critical" } },
      { "property": "Priority", "select": { "equals": "High" } }
    ]
  }
}
```

### Formula Examples

```javascript
// Progress calculation
prop("Done") / prop("Total") * 100

// Status label
if(prop("Due") < now(), "🔴 Overdue", 
  if(prop("Due") < now() + 604800000, "🟡 Due Soon", "🟢 On Track"))

// Assignee initials
slice(prop("Assignee").name, 0, 2)

// Time until due
if(empty(prop("Due")), "No due date",
  format(dateBetween(prop("Due"), now())) + " days left")
```

### Workflow Automations

**Content Publishing Pipeline:**
```
Trigger: Status changes to "Ready for Review"
├─ Notify reviewer via Slack
├─ Set review deadline (3 days)
├─ Create review checklist page
└─ Add to "Needs Review" dashboard

Trigger: All reviews complete
├─ Change status to "Approved"
├─ Move to published section
├─ Notify author
└─ Add to newsletter database
```

**Project Health Dashboard:**
```
Trigger: Weekly (every Monday 9 AM)
├─ Query all active projects
├─ Calculate overdue task count
├─ Calculate upcoming deadlines (7 days)
├─ Generate summary report
└─ Post to #project-updates channel
```

## 9.3 DevOps Workflows

### Incident Response Wiki

```
Incident Page Template:
├─ Incident ID
├─ Severity (P1-P4)
├─ Status (Active, Investigating, Resolved)
├─ Timeline (created, updated)
├─ Impact Assessment
├─ Root Cause
├─ Action Items
├─ Lessons Learned
└─ Related Incidents

Automation:
P1 Incident Created:
├─ Create dedicated incident page
├─ Create incident channel in Slack
├─ Assign incident commander
├─ Set SLA timer
└─ Notify on-call team

Incident Resolved:
├─ Archive incident page
├─ Create post-mortem task
├─ Update incident metrics
└─ Share summary in #incidents channel
```

### On-Call Rotation Management

```
On-Call Database:
├─ Engineer (person)
├─ Start Date
├─ End Date
├─ Shift (primary, backup)
├─ On Call Now? (formula)
└─ Escalation Contact

Automation:
On-Call Changed:
├─ Update Slack status
├─ Notify team of new on-call
├─ Update emergency contact list
└─ Set calendar reminder (24h before)
```

### Deployment Notes

```
Deployment Page:
├─ Version
├─ Date/Time
├─ Deployed By
├─ Environment
├─ Changes (relation to commits)
├─ Rollback Plan
├─ Verification Steps
├─ Sign-off
└─ Post-deployment Tasks

Deployment Checklist:
- [ ] Code reviewed
- [ ] Tests passing
- [ ] Staging verified
- [ ] Database migrations ready
- [ ] Rollback plan documented
- [ ] Monitoring alerts configured
- [ ] Communication sent
```
