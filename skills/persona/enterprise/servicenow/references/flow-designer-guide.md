# Flow Designer Complete Guide

## Overview
Flow Designer is ServiceNow's visual workflow automation tool, replacing legacy Workflow Editor.

## Flow Types

| Type | Trigger | Use Case |
|------|---------|----------|
| **Record-Based** | Create/Update/Delete | Field automation, notifications |
| **Schedule-Based** | Timer | Batch jobs, reminders |
| **Subflow** | Called from other flows | Reusable logic |
| **Action** | Called from other apps | Integration actions |

## Core Actions

### Data Actions
- **Create Record:** Insert new record
- **Update Record:** Modify existing record
- **Get Records:** Query and iterate
- **Delete Record:** Remove records

### Notification Actions
- **Send Email:** HTML/text email
- **Send Notification:** Push/mobile
- **Create Communication:** Activity stream

### Integration Hub Actions
- **REST:** HTTP calls
- **Spoke Actions:** Pre-built integrations
- **Custom Actions:** Script-based integrations

## Best Practices

### Performance
```yaml
DO:
  - Keep flows under 50 elements
  - Use subflows for reusable logic
  - Query once, iterate (avoid loops with queries)
  - Use "Get Records" with limits

DON'T:
  - Create circular triggers
  - Query inside loops
  - Mix sync/async without reason
  - Skip error handling
```

### Error Handling
```
Every action should have:
  - Success path
  - Error path
  - Timeout handling
  - Retry logic (for integrations)
```

## Example: Approval Flow
```yaml
Flow: Change Request Approval
Trigger: Change Request state moves to Assess

Actions:
  1. Get Change Details
     - Query change_request table
     - Store in flow data
  
  2. Calculate Risk
     - If risk_score > 6: Route to CAB
     - Else: Auto-approve
  
  3. CAB Approval (if needed)
     - Create CAB meeting task
     - Wait for approval
     - Timeout: 5 business days
  
  4. Update Change State
     - Approved: Move to Authorize
     - Rejected: Move to New with notes
  
  5. Notify Stakeholders
     - Email: Change owner
     - Slack: #change-management
```

## Subflow Design
```javascript
// Input variables
inputs: {
    incident_id: {type: 'string', required: true},
    notification_type: {type: 'choice', choices: ['email', 'sms', 'slack']}
}

// Output variables
outputs: {
    notification_sent: {type: 'boolean'},
    error_message: {type: 'string'}
}
```

## Testing
1. **Test with different data:** Empty, max length, special chars
2. **Test error conditions:** Timeouts, failed integrations
3. **Test concurrency:** Multiple records triggering simultaneously
4. **Test permissions:** Run as different user roles

## Migration from Workflow Editor
- Workflows run alongside Flows (coexistence)
- Migrate gradually by workflow
- Flow Designer has more capabilities for new development
- Legacy Workflows still supported for existing automations
