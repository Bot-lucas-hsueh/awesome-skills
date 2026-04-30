# Workflow Builder Guide

> Complete guide to Slack's no-code automation platform.

---

## Overview

Workflow Builder allows users to automate routine tasks without writing code. Available on all paid plans.

```
┌─────────────────────────────────────────────────────────────┐
│                    WORKFLOW BUILDER                          │
├─────────────────────────────────────────────────────────────┤
│                                                              │
│  TRIGGER → STEP 1 → STEP 2 → ... → FINAL ACTION             │
│                                                              │
│  Triggers:          Steps:             Actions:               │
│  • Shortcut         • Send message     • Create channel       │
│  • Scheduled        • Collect form     • Add to channel       │
│  • Webhook          • Add reaction     • External webhook     │
│  • Event            • Wait for       • Send email           │
│    reaction         • Custom step      • Update canvas        │
│                                                              │
└─────────────────────────────────────────────────────────────┘
```

---

## Triggers

### 1. Shortcut
User-initiated from shortcuts menu or message actions.

**Configuration:**
```yaml
trigger:
  type: shortcut
  name: "Create Support Ticket"
  location: 
    - global_shortcuts  # Lightning bolt menu
    - message_shortcuts # Message "..." menu
```

### 2. Scheduled
Time-based triggers (cron-like).

**Configuration:**
```yaml
trigger:
  type: scheduled
  frequency: 
    type: daily
    time: "09:00"
    timezone: "America/Los_Angeles"
    days: [monday, tuesday, wednesday, thursday, friday]
  
  # Alternative: weekly
  frequency:
    type: weekly
    day: monday
    time: "10:00"
    
  # Alternative: once
  frequency:
    type: once
    datetime: "2024-12-25T09:00:00"
```

### 3. Webhook
External systems trigger workflows.

```yaml
trigger:
  type: webhook
  name: "Deploy Completed"
  
# Generated webhook URL:
# https://hooks.slack.com/workflows/T00000000/000000000/XXXXXXXXXXXXXXXXXXXXXXXX
```

**Usage:**
```bash
curl -X POST https://hooks.slack.com/workflows/T000/000/XXX \
  -H "Content-Type: application/json" \
  -d '{
    "service": "api",
    "version": "1.2.3",
    "environment": "production",
    "status": "success"
  }'
```

### 4. Event-Based
React to Slack events.

```yaml
trigger:
  type: event
  event: reaction_added
  conditions:
    reaction: "ticket"
    channel: ["C123456", "C789012"]
```

**Supported Events:**
| Event | Description |
|-------|-------------|
| `reaction_added` | Specific emoji reaction |
| `user_joined_channel` | New member joins |
| `file_shared` | File uploaded |
| `emoji_changed` | Custom emoji added |

---

## Built-in Steps

### Send a Message

```yaml
step:
  type: send_message
  channel: "#deployments"
  message: |
    🚀 *Deployment Started*
    
    *Service:* {{trigger.service}}
    *Version:* {{trigger.version}}
    *By:* {{trigger.user}}
  
  # Include button to take action
  buttons:
    - text: "View Logs"
      url: "https://logs.company.com/{{trigger.service}}"
    - text: "Rollback"
      action: "rollback_deploy"
```

### Collect Information (Form)

```yaml
step:
  type: form
  title: "Bug Report"
  fields:
    - name: title
      type: short_text
      label: "Bug Title"
      required: true
      
    - name: severity
      type: dropdown
      label: "Severity"
      options:
        - "Critical - Service Down"
        - "High - Major Feature Broken"
        - "Medium - Workaround Exists"
        - "Low - Cosmetic"
      required: true
      
    - name: description
      type: paragraph
      label: "Description"
      placeholder: "Describe the bug..."
      required: true
      
    - name: screenshots
      type: file
      label: "Screenshots"
      required: false
```

### Add to Channel

```yaml
step:
  type: add_to_channel
  user: "{{form.submitter}}"
  channel: "#incident-{{trigger.incident_id}}"
```

### Send Email

```yaml
step:
  type: send_email
  to: ["{{form.assignee_email}}", "oncall@company.com"]
  subject: "[URGENT] {{form.severity}}: {{form.title}}"
  body: |
    A new bug report has been submitted:
    
    {{form.description}}
    
    View in Slack: {{workflow.message_permalink}}
```

### Update Canvas

```yaml
step:
  type: update_canvas
  canvas: "C1234567890"
  content: |
    ## Meeting Notes - {{current_date}}
    
    {{form.notes}}
    
    ### Action Items
    {{form.action_items}}
```

---

## Custom Steps (Developer)

### Creating Custom Steps

Custom steps extend Workflow Builder with code.

```typescript
// manifest.ts (Next-gen Slack platform)
import { Manifest } from "slack-manifest";

export default Manifest({
  name: "Custom Steps Demo",
  description: "Demonstrates custom workflow steps",
  icon: "assets/icon.png",
  
  workflows: [CreateIssueWorkflow],
  
  outgoingDomains: ["api.github.com"],
  
  botScopes: [
    "commands",
    "chat:write",
    "chat:write.public"
  ]
});
```

### Custom Step Definition

```typescript
// workflows/create_issue.ts
import { DefineWorkflow, Schema } from "deno-slack-sdk/mod.ts";
import { CreateIssueFunction } from "../functions/create_issue.ts";

const CreateIssueWorkflow = DefineWorkflow({
  callback_id: "create_github_issue",
  title: "Create GitHub Issue",
  description: "Creates a GitHub issue from Slack",
  input_parameters: {
    properties: {
      interactivity: { type: Schema.slack.types.interactivity },
      channel: { type: Schema.slack.types.channel_id }
    },
    required: ["interactivity", "channel"]
  }
});

// Open form for input
const formData = CreateIssueWorkflow.addStep(
  Schema.slack.functions.OpenForm,
  {
    title: "Create GitHub Issue",
    interactivity: CreateIssueWorkflow.inputs.interactivity,
    submit_label: "Create Issue",
    fields: {
      elements: [
        {
          name: "title",
          title: "Issue Title",
          type: Schema.types.string
        },
        {
          name: "body",
          title: "Description",
          type: Schema.types.string,
          long: true
        },
        {
          name: "labels",
          title: "Labels",
          type: Schema.types.array,
          items: { type: Schema.types.string }
        }
      ],
      required: ["title", "body"]
    }
  }
);

// Execute custom function
const issue = CreateIssueWorkflow.addStep(CreateIssueFunction, {
  title: formData.outputs.fields.title,
  body: formData.outputs.fields.body,
  labels: formData.outputs.fields.labels
});

// Post result to channel
CreateIssueWorkflow.addStep(Schema.slack.functions.SendMessage, {
  channel_id: CreateIssueWorkflow.inputs.channel,
  message: `GitHub issue created: ${issue.outputs.url}`
});

export default CreateIssueWorkflow;
```

### Custom Function Implementation

```typescript
// functions/create_issue.ts
import { DefineFunction, Schema, SlackFunction } from "deno-slack-sdk/mod.ts";

export const CreateIssueFunction = DefineFunction({
  callback_id: "create_github_issue",
  title: "Create GitHub Issue",
  description: "Creates an issue in GitHub repository",
  source_file: "functions/create_issue.ts",
  input_parameters: {
    properties: {
      title: { type: Schema.types.string },
      body: { type: Schema.types.string },
      labels: { 
        type: Schema.types.array,
        items: { type: Schema.types.string }
      }
    },
    required: ["title", "body"]
  },
  output_parameters: {
    properties: {
      url: { type: Schema.types.string },
      number: { type: Schema.types.integer }
    },
    required: ["url", "number"]
  }
});

export default SlackFunction(
  CreateIssueFunction,
  async ({ inputs, env }) => {
    const response = await fetch(
      "https://api.github.com/repos/owner/repo/issues",
      {
        method: "POST",
        headers: {
          "Authorization": `Bearer ${env.GITHUB_TOKEN}`,
          "Accept": "application/vnd.github.v3+json",
          "Content-Type": "application/json"
        },
        body: JSON.stringify({
          title: inputs.title,
          body: inputs.body,
          labels: inputs.labels || []
        })
      }
    );
    
    const data = await response.json();
    
    return {
      outputs: {
        url: data.html_url,
        number: data.number
      }
    };
  }
);
```

---

## AI Workflow Builder (2024+)

### Natural Language Workflow Creation

```
User: "Create a workflow that sends a daily standup reminder 
       at 9am and collects responses"

Slack AI: Generates workflow with:
  - Scheduled trigger (daily, 9am)
  - Send message step (standup prompt)
  - Form step (collect updates)
  - Send message step (post to channel)
```

### AI-Powered Summarization Step

```yaml
step:
  type: ai_summarize
  source: "#engineering"
  timeframe: "24h"
  output_format: "bullet_points"
  destination: "#engineering-updates"
```

---

## Best Practices

### 1. Naming Conventions
```
Workflow Name: [Team] - [Action] - [Context]
Example: "Engineering - Deploy Notification - Production"

Variable Names: lowercase_with_underscores
Example: "incident_severity", "ticket_assignee"
```

### 2. Error Handling
- Always add fallback messages
- Use conditional logic for edge cases
- Test with various input types

### 3. Performance
- Limit workflow complexity (max 100 steps)
- Use batch operations where possible
- Avoid infinite loops

### 4. Security
- Store sensitive data in environment variables
- Validate webhook payloads
- Use least-privilege permissions
