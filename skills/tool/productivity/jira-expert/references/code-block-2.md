# yaml Example

```
# Rule 1: Auto-assign when story moves to "In Progress"
trigger:
  type: issue transitioned
  to: "In Progress"
conditions:
  - type: issueTypeCondition
    value: Story
  - type: assigneeCondition
    operator: NOT_SET
actions:
  - type: assignIssueAction
    value: "{{issue.assignee}}"
    # Fallback to sprint owner if no assignee
  - type: set_FIELDValue
    field: Sprint
    value: "{{sprint.current}}"

# Rule 2: Notify team when priority is set to Critical
trigger:
  type: fieldValueChanged
  field: Priority
  to: Critical
conditions:
  - type: projectCondition
    value: ENG
actions:
  - type: addLabelAction
    label: critical-priority
  - type: sendWebhookAction
    url: "https://slack.webhook/..."
    # Webhook payload for Slack notification

# Rule 3: Auto-close resolved issues after 7 days
trigger:
  type: issue transitioned
  to: Done
conditions:
  - type: issueTypeCondition
    value: Bug
actions:
  - type: transitionIssueAction
    to: Closed
    delay: 7d
```
