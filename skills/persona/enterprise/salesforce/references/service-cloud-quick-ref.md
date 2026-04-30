# Service Cloud Quick Reference

## Core Service Objects

| Object | Purpose | Key Relationships |
|--------|---------|-------------------|
| **Case** | Customer support tickets | Account, Contact, Asset, Entitlement |
| **Solution** | Knowledge articles | Category, Status, IsReviewed |
| **Entitlement** | Support contracts | Account, Asset, ContractLineItem |
| **Milestone** | SLA tracking | Entitlement, Case, Target/Actual dates |
| **Asset** | Customer products | Account, Contact, Product2 |
| **Work Order** | Field service jobs | Account, Asset, Case, ServiceAppointment |

## Case Management

### Case Lifecycle
```
New → Working → Escalated → Closed
        ↓           ↓
   Assignment    Notification
   Rules         (Manager)
```

### Assignment Rules
```java
Criteria Priority:
1. Account.Support_Tier__c = "Enterprise"
2. Case.Origin = "Phone" AND Priority = "High"
3. Product Category = "Critical"
4. Default Queue
```

### Escalation Rules
```
Criteria: Priority = High AND Status != Closed
         AND Age > 4 hours
Action: 
  - Email: Support Manager
  - Reassign: Escalation Queue
  - Field Update: IsEscalated = true
```

## Omni-Channel

### Routing Configuration
```
Service Channel (Cases) 
    → Routing Config (Priority, Model)
        → Presence Config (Status, Capacity)
            → Queue
                → Agent
```

### Routing Models
| Model | Use Case |
|-------|----------|
| **Most Available** | Distribute evenly |
| **Least Active** | Balanced workload |
| **Skill-Based** | Expert matching |

### Presence Statuses
```yaml
Available:
  - Online: Ready for work
  - Busy: On call/meeting
  
Unavailable:
  - Break: Lunch/coffee
  - Training: Learning time
  - Meeting: Internal meetings
```

## Knowledge Management

### Article Lifecycle
```
Draft → Review → Published → Archived
  ↓       ↓         ↓           ↓
Author  SME      Public    Outdated
```

### Data Categories
```
Product Line
├── Product A
├── Product B
└── Product C

Topic
├── Installation
├── Troubleshooting
├── How-To
└── FAQ
```

### Article Types
- **FAQ** - Common questions
- **How-To** - Step-by-step guides
- **Troubleshooting** - Problem resolution
- **Reference** - Technical documentation

## Einstein for Service

### Features
| Feature | Description |
|---------|-------------|
| **Case Classification** | Auto-categorize incoming cases |
| **Case Wrap-Up** | Auto-summarize case resolution |
| **Reply Recommendations** | Suggest response based on knowledge |
| **Article Recommendations** | Surface relevant articles |
| **Einstein Bots** | Automated chat handling |
| **Agentforce** | Autonomous service agents |

### Einstein Bot Setup
```
Dialog Flow:
  Welcome → Intent Recognition
              ↓
    ┌─────────┼─────────┐
    ↓         ↓         ↓
 Order    Support   General
 Status     ↓        Info
            ↓
     ┌──────┴──────┐
     ↓             ↓
  Knowledge    Create Case
   Article        Handoff
```

## Field Service

### Key Objects
- **Work Order** - Job to be done
- **Work Order Line Item** - Specific tasks
- **Service Appointment** - Scheduled time slot
- **Service Resource** - Technician
- **Operating Hours** - Availability
- **Territory** - Geographic area

### Scheduling
```
Scheduling Policy → Service Objectives → Resource Availability
         ↓
    Gantt Optimizer
         ↓
  Optimized Schedule
```

## Service Analytics

### Key Metrics
| Metric | Formula | Target |
|--------|---------|--------|
| **First Response Time** | Time to first agent response | < 1 hour |
| **Resolution Time** | Case open to close | < 24 hours |
| **CSAT** | Customer satisfaction score | > 90% |
| **First Contact Resolution** | Resolved on first interaction | > 70% |
| **Agent Utilization** | % of time on productive work | 75-85% |

---

> **Tip**: Use Service Cloud Voice for CTI integration with telephony
