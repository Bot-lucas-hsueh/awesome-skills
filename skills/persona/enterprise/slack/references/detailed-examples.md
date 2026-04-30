## §4 Detailed Examples

### Example 1: Building a Standup Bot with Bolt for Python

**Scenario:** Engineering team wants automated daily standup collection.

```python
import os
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# Initialize app with environment tokens
app = App(token=os.environ["SLACK_BOT_TOKEN"])

# Slash command: /standup triggers modal
@app.command("/standup")
def handle_standup_command(ack, body, client):
    ack()
    
    # Open modal for standup input
    client.views_open(
        trigger_id=body["trigger_id"],
        view={
            "type": "modal",
            "callback_id": "standup_submission",
            "title": {"type": "plain_text", "text": "Daily Standup"},
            "blocks": [
                {
                    "type": "input",
                    "block_id": "yesterday",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "input"
                    },
                    "label": {"type": "plain_text", "text": "What did you do yesterday?"}
                },
                {
                    "type": "input",
                    "block_id": "today",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "input"
                    },
                    "label": {"type": "plain_text", "text": "What will you do today?"}
                },
                {
                    "type": "input",
                    "block_id": "blockers",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "input"
                    },
                    "label": {"type": "plain_text", "text": "Any blockers?"},
                    "optional": True
                }
            ],
            "submit": {"type": "plain_text", "text": "Submit"}
        }
    )

# Handle modal submission
@app.view("standup_submission")
def handle_standup_view(ack, body, client):
    ack()
    
    user = body["user"]["id"]
    values = body["view"]["state"]["values"]
    
    yesterday = values["yesterday"]["input"]["value"]
    today = values["today"]["input"]["value"]
    blockers = values["blockers"]["input"].get("value", "None")
    
    # Post formatted standup to channel
    standup_channel = os.environ["STANDUP_CHANNEL_ID"]
    
    client.chat_postMessage(
        channel=standup_channel,
        blocks=[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"*<@{user}>'s Standup*"
                }
            },
            {
                "type": "section",
                "fields": [
                    {"type": "mrkdwn", "text": f"*Yesterday:*\n{yesterday}"},
                    {"type": "mrkdwn", "text": f"*Today:*\n{today}"},
                    {"type": "mrkdwn", "text": f"*Blockers:*\n{blockers}"}
                ]
            },
            {"type": "divider"}
        ]
    )

if __name__ == "__main__":
    handler = SocketModeHandler(app, os.environ["SLACK_APP_TOKEN"])
    handler.start()
```

**Key Learnings:**
- Use modals for structured data collection
- Socket Mode eliminates need for public URL
- Block Kit creates rich, formatted messages
- Store channel IDs in environment variables

---

### Example 2: Enterprise Grid Architecture for Global Company

**Scenario:** 10,000+ employee company needs multi-region Slack setup.

```
┌────────────────────────────────────────────────────────────────┐
│                    ENTERPRISE GRID                              │
│                                                                 │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐│
│  │  US Workspace   │  │  EU Workspace   │  │  APAC Workspace ││
│  │  slack-us.company│  │  slack-eu.company│  │ slack-apac.company│
│  │                 │  │                 │  │                 ││
│  │  #general-us    │  │  #general-eu    │  │  #general-apac  ││
│  │  #eng-sf        │  │  #eng-berlin    │  │  #eng-sydney    ││
│  │  #sales-amer    │  │  #sales-emea    │  │  #sales-apac    ││
│  └─────────────────┘  └─────────────────┘  └─────────────────┘│
│           │                    │                    │           │
│           └────────────────────┼────────────────────┘           │
│                                │                                │
│                    ┌───────────┴───────────┐                    │
│                    │   SHARED CHANNELS     │                    │
│                    │                       │                    │
│                    │  #company-announcements│                    │
│                    │  #product-updates      │                    │
│                    │  #security-incidents   │                    │
│                    │  #exec-questions       │                    │
│                    └───────────────────────┘                    │
└────────────────────────────────────────────────────────────────┘
```

**Implementation:**

```json
// Organization settings (admin API)
{
  "enterprise": {
    "name": "Acme Corporation",
    "default_workspace": "acme-primary",
    "data_residency": {
      "us": "aws-us-east-1",
      "eu": "aws-eu-west-1",
      "apac": "aws-ap-southeast-1"
    },
    "security": {
      "sso": {
        "provider": "okta",
        "enforced": true
      },
      "dlp": {
        "enabled": true,
        "patterns": ["credit_card", "ssn", "api_key"]
      },
      "retention": {
        "messages": "indefinite",
        "files": "7_years"
      }
    }
  }
}
```

**Governance Rules:**
1. **Channel Naming:** `#region-function-topic` (e.g., `#us-eng-kubernetes`)
2. **Shared Channels:** Only for cross-region collaboration
3. **Local Decisions:** Keep in regional workspaces
4. **Global Announcements:** Use `#company-announcements` (read-only for most)

---

### Example 3: Incident Response Workflow with Workflow Builder

**Scenario:** Automated incident management with Slack workflows.

```yaml
# Workflow Definition (conceptual)
workflow:
  name: "Incident Response"
  trigger:
    type: shortcut
    name: "Declare Incident"
  
  steps:
    - name: "Collect Incident Details"
      type: form
      fields:
        - name: severity
          type: select
          options: [P1-Critical, P2-High, P3-Medium, P4-Low]
        - name: description
          type: textarea
        - name: affected_services
          type: multi_select
          options: [API, Web, Mobile, Database]
    
    - name: "Create Incident Channel"
      type: custom_step
      webhook: https://api.company.com/slack/create-incident-channel
      inputs:
        severity: "{{step1.severity}}"
        description: "{{step1.description}}"
    
    - name: "Notify On-Call Engineer"
      type: message
      channel: "{{step2.channel_id}}"
      content: |
        🚨 *{{step1.severity}} Incident Declared*
        
        *Description:* {{step1.description}}
        *Affected:* {{step1.affected_services}}
        *Channel:* <#{{step2.channel_id}}>
        
        cc: <!subteam^on-call-engineers>
    
    - name: "Create Jira Ticket"
      type: connector
      app: jira
      action: create_issue
      project: INC
      summary: "{{step1.description}}"
      priority: "{{step1.severity}}"
    
    - name: "Post to Status Page"
      type: webhook
      url: https://status.company.com/api/incidents
      method: POST
      body:
        status: "investigating"
        message: "We are investigating an issue with {{step1.affected_services}}"
```

**Post-Incident Actions:**
```python
# Custom step: Archive incident channel after 7 days
import time
from datetime import datetime, timedelta

def archive_incident_channel(channel_id, severity, resolved_at):
    """Schedule channel archival after cooling period"""
    
    cooling_periods = {
        "P1-Critical": 30,  # days
        "P2-High": 14,
        "P3-Medium": 7,
        "P4-Low": 3
    }
    
    days = cooling_periods.get(severity, 7)
    archive_date = resolved_at + timedelta(days=days)
    
    # Schedule via workflow
    return {
        "action": "schedule_archival",
        "channel_id": channel_id,
        "archive_date": archive_date.isoformat(),
        "reason": f"Incident resolved, cooling period: {days} days"
    }
```

---

### Example 4: AI-Powered Knowledge Base with Slack AI

**Scenario:** Engineering team uses Slack AI to surface institutional knowledge.

```javascript
// Slack AI Integration Pattern
class SlackKnowledgeBase {
  
  async findRelatedDiscussions(query, channel) {
    // Use Slack AI search to find relevant conversations
    const searchResults = await this.slack.search.messages({
      query: query,
      sort: "timestamp",
      sort_dir: "desc",
      count: 10
    });
    
    // Use AI to summarize findings
    const summary = await this.slack.ai.summarize({
      messages: searchResults.matches,
      format: "bullet_points"
    });
    
    return {
      answer: summary.answer,
      sources: searchResults.matches.map(m => ({
        channel: m.channel.name,
        timestamp: m.ts,
        permalink: m.permalink
      }))
    };
  }
  
  async generateChannelRecap(channelId, days = 7) {
    // Generate AI summary of channel activity
    const recap = await this.slack.ai.recap({
      channel: channelId,
      since: Date.now() - (days * 24 * 60 * 60 * 1000)
    });
    
    return {
      summary: recap.summary,
      action_items: recap.action_items,
      decisions: recap.decisions,
      participants: recap.participants
    };
  }
}

// Usage in Workflow
app.event("app_mention", async ({ event, client }) => {
  const question = event.text.replace(/<@\w+>/, "").trim();
  
  const kb = new SlackKnowledgeBase(client);
  const result = await kb.findRelatedDiscussions(
    question, 
    event.channel
  );
  
  await client.chat.postMessage({
    channel: event.channel,
    thread_ts: event.thread_ts || event.ts,
    blocks: [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: `*Answer:*\n${result.answer}`
        }
      },
      {
        type": "context",
        elements: [
          {
            type: "mrkdwn",
            text: `*Sources:* ${result.sources.map(s => 
              `<${s.permalink}|${s.channel}>`
            ).join(", ")}`
          }
        ]
      }
    ]
  });
});
```

**Best Practices:**
- Always cite sources with permalinks
- Use threads to keep knowledge organized
- Pin AI-generated summaries to channels
- Regular recaps for high-activity channels

---

### Example 5: Slack Connect for External Collaboration

**Scenario:** Vendor collaboration using Slack Connect with security controls.

```python
# Slack Connect Management Script
from slack_sdk import WebClient

class SlackConnectManager:
    def __init__(self, token):
        self.client = WebClient(token=token)
    
    def create_secure_connect_channel(self, name, partner_emails, data_classification):
        """
        Create Slack Connect channel with security policies
        """
        # Determine retention based on classification
        retention_days = {
            "public": 90,
            "internal": 365,
            "confidential": 30,
            "restricted": 7
        }.get(data_classification, 90)
        
        # Create channel
        channel = self.client.conversations_create(
            name=f"ext-{name}",
            is_private=True
        )
        channel_id = channel["channel"]["id"]
        
        # Set topic with security notice
        self.client.conversations_setTopic(
            channel=channel_id,
            topic=f"🔒 {data_classification.upper()} | External collaboration | "
                  f"Auto-archive after {retention_days} days of inactivity"
        )
        
        # Invite external users via Slack Connect
        for email in partner_emails:
            self.client.conversations_inviteShared(
                channel=channel_id,
                emails=[email],
                message="Welcome to our secure collaboration space"
            )
        
        # Set up retention policy
        self._configure_retention(channel_id, retention_days)
        
        # Post welcome message with guidelines
        self.client.chat_postMessage(
            channel=channel_id,
            blocks=[
                {
                    "type": "header",
                    "text": {
                        "type": "plain_text",
                        "text": "🔒 Secure Collaboration Channel"
                    }
                },
                {
                    "type": "section",
                    "text": {
                        "type": "mrkdwn",
                        "text": (
                            f"*Data Classification:* {data_classification.upper()}\n"
                            f"*Retention:* {retention_days} days\n\n"
                            "*Guidelines:*\n"
                            "• No credentials or secrets\n"
                            "• Share files via approved links only\n"
                            "• Escalate security concerns to #security"
                        )
                    }
                }
            ]
        )
        
        return channel_id
    
    def audit_connect_channels(self):
        """
        Generate audit report of all Slack Connect channels
        """
        channels = self.client.conversations_list(
            types="private_channel",
            exclude_archived=True
        )
        
        connect_channels = []
        for channel in channels["channels"]:
            if channel["name"].startswith("ext-"):
                info = self.client.conversations_info(channel=channel["id"])
                connect_channels.append({
                    "name": channel["name"],
                    "created": channel["created"],
                    "num_members": channel["num_members"],
                    "is_shared": info["channel"].get("is_shared", False),
                    "shared_team_ids": info["channel"].get("shared_team_ids", [])
                })
        
        return connect_channels

# Usage
manager = SlackConnectManager(os.environ["SLACK_ADMIN_TOKEN"])

# Create vendor channel
vendor_channel = manager.create_secure_connect_channel(
    name="acme-corp-integration",
    partner_emails=["contact@acme-corp.com", "dev@acme-corp.com"],
    data_classification="confidential"
)

# Generate audit report
audit_report = manager.audit_connect_channels()
print(f"Active Slack Connect channels: {len(audit_report)}")
```

**Security Checklist:**
- [ ] Verify external domain before inviting
- [ ] Set appropriate retention policies
- [ ] Enable DLP for sensitive content
- [ ] Regular access reviews
- [ ] Auto-archive inactive channels

---
