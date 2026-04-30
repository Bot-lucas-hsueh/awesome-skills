# yaml Example

```
# Automation 1: Auto-assign to sprint owner
trigger:
  - type: issueCreated
    filter: 
      state: { name: "Ready" }
actions:
  - type: updateIssue
    assignTo: "{{project.owner}}"

# Automation 2: Notify Slack when priority set to urgent
trigger:
  - type: issuePriorityChanged
    to: 0  # Urgent
actions:
  - type: createComment
    content: "🔴 This issue is now urgent. Please address immediately."
  - type: sendNotification
    channel: "#engineering"

# Automation 3: Move completed issues to Done
trigger:
  - type: issueStateChanged
    to: { name: "Completed" }
actions:
  - type: updateIssue
    state: { name: "Done" }

# Automation 4: Auto-label by project
trigger:
  - type: issueCreated
    filter:
      project: { name: "Mobile App" }
actions:
  - type: addLabel
    label: "mobile"
```
