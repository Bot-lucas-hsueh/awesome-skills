# Standard Workflow

## 8.1 Bot Integration Workflow

```
Slack Bot Setup Pipeline
├── 1. Create Slack App
│   ├── Go to api.slack.com/apps
│   ├── Create new app (From scratch)
│   ├── Configure app manifest
│   └── Install to workspace
│
├── 2. Configure Permissions
│   ├── Add OAuth scopes
│   ├── Request from workspace
│   └── Get bot token
│
├── 3. Enable Features
│   ├── Enable Slash Commands
│   ├── Enable Interactivity
│   ├── Enable Event Subscriptions
│   └── Configure Home tab
│
├── 4. Develop Webhook Handler
│   ├── Set request URL in Slack settings
│   ├── Verify signing secret
│   ├── Handle events
│   └── Respond within 3 seconds
│
└── 5. Deploy & Monitor
    ├── Deploy to HTTPS endpoint
    ├── Monitor logs
    └── Handle errors gracefully
```

## 8.2 Event Handling Workflow

### Event Subscription Flow

```
Slack Event Received
├─ Verify request signature
├─ Check URL verification challenge
├─ Parse event payload
├─ Route to handler
│   ├─ message.channels
│   ├─ app_mention
│   ├─ reaction_added
│   └─ view_submission
└─ Acknowledge (200 OK)
```

### Common Event Handlers

```javascript
// Message event handler
app.message('help', async ({ message, say }) => {
  await say({
    blocks: [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: "*Available Commands:*\n• `/standup` - Submit daily standup\n• `/tasks` - View your tasks\n• `/status` - Set your status"
        }
      }
    ]
  });
});

// App mention handler
app.event('app_mention', async ({ event, client }) => {
  await client.chat.postMessage({
    channel: event.channel,
    text: `Hi <@${event.user}>! How can I help?`
  });
});

// Reaction handler
app.event('reaction_added', async ({ event, client }) => {
  if (event.reaction === 'white_check_mark') {
    // Task completed
    await updateTaskStatus(event.item.ts);
  }
});
```

### Modal Workflow

```
Open Modal:
1. User clicks button / triggers action
2. Bot receives interaction payload
3. Bot calls views.open with modal definition
4. Slack displays modal to user

Submit Modal:
1. User fills form and clicks Submit
2. Bot receives view_submission event
3. Bot validates input
4. Bot processes data
5. Bot calls views.update or returns errors
```

## 8.3 Automation Workflow

### Notification Workflows

```
GitHub PR Merged → Slack Notification:
1. GitHub webhook fires on PR merge
2. Bot receives webhook at /webhooks/github
3. Bot formats message with PR details
4. Bot posts to #deployments channel
5. Bot threads with deployment checklist

Deployment Status Update:
1. CI/CD pipeline sends status
2. Bot receives webhook
3. Bot updates deployment thread
4. Bot notifies team if failed
5. Bot creates incident ticket if needed
```

### Standup Bot Flow

```
Daily 9:00 AM:
1. Bot sends DM to all team members
2. DM contains interactive form
3. User submits standup
4. Bot collects and formats
5. Bot posts summary to #standups channel

Flow:
DM → Interactive Form → Submit → 
  ├─ Store in database
  ├─ Post to channel
  └─ Send confirmation
```

### Task Management Integration

```
Slack ↔ Jira/Linear/Notion Integration:

Create Task from Slack:
1. User sends: `/task "Fix login bug" @jira ENG-123`
2. Bot parses command
3. Bot updates Jira
4. Bot confirms in Slack

Status Updates:
1. Issue status changes in Jira
2. Webhook triggers bot
3. Bot posts update to assigned user
4. User can transition from Slack
```

### Scheduled Reminders

```javascript
// Schedule daily reminder
const schedule = require('node-schedule');

schedule.scheduleJob('0 9 * * 1-5', async () => {
  const channel = await client.conversations.list();
  const standupChannel = channel.channels.find(c => c.name === 'standups');
  
  await client.chat.postMessage({
    channel: standupChannel.id,
    text: "Good morning! Don't forget to submit your standup.",
    blocks: [
      {
        type: "section",
        text: {
          type: "mrkdwn",
          text: "Good morning team! :sunny:\n\nIt's standup time. Use /standup to share your updates."
        }
      }
    ]
  });
});
```

### Approval Workflows

```
Expense Approval Flow:
1. User submits expense via /expense command
2. Bot creates approval request
3. Manager receives DM notification
4. Manager approves/rejects via buttons
5. Bot notifies user of decision
6. Bot routes to finance if approved

Flow:
/expense → Modal → Submit → 
  ├─ DM Manager
  ├─ Await approval
  ├─ Process decision
  └─ Notify employee
```
