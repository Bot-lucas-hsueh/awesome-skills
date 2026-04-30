# Standards & Reference

## 7.1 Official Documentation

- [Slack API Documentation](https://api.slack.com/docs)
- [Slack App Documentation](https://api.slack.com/start)
- [Block Kit Builder](https://api.slack.com/block-kit)
- [Message Formatting](https://api.slack.com/reference/surfaces/formatting)
- [Web API Methods](https://api.slack.com/methods)
- [Events API](https://api.slack.com/events-api)
- [Interactivity & Shortcuts](https://api.slack.com/interactivity)
- [OAuth & Permissions](https://api.slack.com/authentication)
- [Rate Limits](https://api.slack.com/rate-limits)

## 7.2 Configuration Reference

### App Manifest (appmanifest.json)

```json
{
  "_metadata": {
    "major_version": 2,
    "minor_version": 0
  },
  "display_information": {
    "name": "Team Productivity Bot",
    "description": "Automates team workflows and notifications",
    "background_color": "#4A154B"
  },
  "features": {
    "app_home": {
      "home_tab_enabled": true,
      "messages_tab_enabled": true
    },
    "bot_user": {
      "display_name": "TeamBot",
      "always_online": true
    },
    "slash_commands": [
      {
        "command": "/standup",
        "url": "https://example.com/slack/standup",
        "description": "Submit daily standup",
        "usage_hint": "[yesterday] [today] [blockers]"
      }
    ]
  },
  "oauth_config": {
    "redirect_urls": ["https://example.com/slack/oauth"],
    "scopes": {
      "bot": [
        "chat:write",
        "commands",
        "im:read",
        "im:write",
        "im:history",
        "channels:read",
        "groups:read",
        "users:read"
      ]
    }
  }
}
```

### Environment Variables

```bash
# .env.example
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_SIGNING_SECRET=your-signing-secret
SLACK_APP_TOKEN=xapp-your-app-token
SLACK_TEAM_ID=T0123456789

# Optional
LOG_LEVEL=debug
DB_URL=postgresql://localhost:5432/slackbot
REDIS_URL=redis://localhost:6379
```

### Permissions Scopes

| Scope | Description | Usage |
|-------|-------------|-------|
| `chat:write` | Send messages | Post messages to channels |
| `commands` | Slash commands | Handle `/` commands |
| `im:read` | Read DMs | Access direct messages |
| `im:history` | Message history | Read DM history |
| `channels:read` | List channels | Browse public channels |
| `groups:read` | List private channels | Access private channels |
| `users:read` | Get user info | Display user details |

## 7.3 Common Commands & Workflows

### Web API Methods

| Method | Endpoint | Purpose |
|--------|----------|---------|
| `chat.postMessage` | POST /chat.postMessage | Send message |
| `chat.postEphemeral` | POST /chat.postEphemeral | Send ephemeral message |
| `conversations.list` | GET /conversations.list | List channels |
| `users.list` | GET /users.list | List workspace users |
| `views.publish` | POST /views.publish | Update Home tab |
| `chat.scheduleMessage` | POST /chat.scheduleMessage | Schedule message |

### Message Payload Examples

```json
// Block Kit Message
{
  "channel": "C0123456789",
  "text": "New task assigned",
  "blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*New Task Assigned*\n:clipboard: <https://notion.so/task-123|Task: Review PR>"
      },
      "accessory": {
        "type": "button",
        "text": { "type": "plain_text", "text": "View" },
        "action_id": "view_task",
        "value": "task-123"
      }
    },
    {
      "type": "context",
      "elements": [
        { "type": "mrkdwn", "text": "Assigned to: <@U012345>|Alice | Due: Tomorrow" }
      ]
    }
  ]
}
```

### Slash Command Handler

```javascript
// Express.js handler
app.post('/slack/standup', async (req, res) => {
  const { user_id, text, channel_id, trigger_id } = req.body;
  
  // Parse command
  const [yesterday, today, blockers] = text.split('|');
  
  // Store standup data
  await db.standups.create({
    userId: user_id,
    yesterday: yesterday?.trim(),
    today: today?.trim(),
    blockers: blockers?.trim(),
    date: new Date()
  });
  
  // Open modal
  const result = await client.views.open({
    trigger_id: trigger_id,
    view: {
      type: "modal",
      title: { "type": "plain_text", "text": "Standup Submitted" },
      blocks: [
        { "type": "section", "text": { "type": "mrkdwn", "text": "✅ Standup recorded!" } }
      ]
    }
  });
  
  res.send('');
});
```

## 7.4 Version & Platform Compatibility

| Platform | Status | Notes |
|----------|--------|-------|
| Slack Desktop | Current | Full features |
| Slack Mobile | Current | Limited interactivity |
| Slack API v2 | Current | OAuth v2, granular scopes |
| Bolt Framework | v1.x | Official Node.js framework |
| Block Kit | Current | Rich message UI |

| Feature | Free | Pro | Business+ |
|---------|------|-----|-----------|
| Message history | 90 days | Unlimited | Unlimited |
| Apps/Integrations | 10 | Unlimited | Unlimited |
| Custom emojis | Unlimited | Unlimited | Unlimited |
| SCIM API | No | No | Yes |
| Session duration | 90 days | 1 year | 5 years |

### Rate Limits

```
Tier 1 (major methods): 20 req/min per token
Tier 2 (conversations.*): 100 req/min per workspace  
Tier 3 (chat.postMessage): 1 req/sec per channel
Tier 4 (views.*): 20 req/min per workspace

Exponential backoff:
- Initial: 1 second
- Max retries: 3
- Jitter: random(0, 1000ms)
```
