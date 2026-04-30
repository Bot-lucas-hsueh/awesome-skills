# Scenario Examples

## 9.1 Team Workflows

### Scenario: Daily Standup Automation

**User:** "How do I build a standup bot that collects updates?"

**Expert:**
> **Standup Bot Implementation:**
>
> 1. **Command Definition:**
>    `/standup [yesterday|today|blockers]`
>
> 2. **Modal Form:**
>    ```javascript
>    {
>      type: "modal",
>      title: { type: "plain_text", text: "Daily Standup" },
>      submit: { type: "plain_text", text: "Submit" },
>      blocks: [
>        {
>          type: "input",
>          block_id: "yesterday",
>          label: { type: "plain_text", text: "What did you do yesterday?" },
>          element: { type: "plain_text_input", multiline: true }
>        },
>        {
>          type: "input",
>          block_id: "today",
>          label: { type: "plain_text", text: "What will you do today?" },
>          element: { type: "plain_text_input", multiline: true }
>        },
>        {
>          type: "input",
>          block_id: "blockers",
>          label: { type: "plain_text", text: "Any blockers?" },
>          element: { type: "plain_text_input", multiline: true }
>        }
>      ]
>    }
>    ```
>
> 3. **Daily Digest:**
>    - Collect all standups from database
>    - Format into channel message
>    - Post at configured time

### Scenario: On-Call Alerting

**User:** "How do I set up PagerDuty integration with Slack?"

**Expert:**
> **On-Call Integration:**
>
> 1. **Alert Channel Setup:**
>    - Create #incidents channel
>    - Configure PagerDuty Slack integration
>    - Set up escalation policies
>
> 2. **Bot Workflow:**
>    ```
>    PagerDuty Trigger
>    ├─ PD webhook → Bot endpoint
>    ├─ Parse incident details
>    ├─ Post to #incidents
>    ├─ DM on-call engineer
>    └─ Track acknowledgment time
>    ```
>
> 3. **Incident Commands:**
>    - `/incident create [title]` - Open new incident
>    - `/incident ack [id]` - Acknowledge
>    - `/incident resolve [id]` - Resolve incident
>    - `/incident update [id]` - Post update

## 9.2 Automation Scenarios

### Workflow Builder Patterns

```
New Employee Onboarding Workflow:
Trigger: User added to #new-hires channel
├─ Send welcome DM with onboarding checklist
├─ Post introduction to #general
├─ Schedule 1-week follow-up
└─ Add to relevant team channels

Checklist:
- [ ] Dev environment setup
- [ ] Tool access granted
- [ ] Team introductions scheduled
- [ ] 30-day review scheduled
```

### Notification Templates

```javascript
// GitHub PR notification
const prNotification = {
  blocks: [
    {
      type: "header",
      text: { type: "plain_text", text: "🔀 New PR Ready for Review" }
    },
    {
      type: "section",
      fields: [
        { type: "mrkdwn", text: "*Author:*\n<@U123>|Alice" },
        { type: "mrkdwn", text: "*Branch:*\nfeature/auth" }
      ]
    },
    {
      type: "section",
      text: {
        type: "mrkdwn",
        text: "*<https://github.com/org/repo/pull/123|PR-123: Add authentication module>*"
      }
    },
    {
      type: "actions",
      elements: [
        { type: "button", text: { type: "plain_text", text: "Review PR" }, url: "https://github.com/..." },
        { type: "button", text: { type: "plain_text", text: "Approve" }, action_id: "approve_pr" }
      ]
    }
  ]
};

// Deployment notification
const deploymentNotification = {
  blocks: [
    {
      type: "section",
      text: { type: "mrkdwn", text: ":rocket: *Deploying to Production*" }
    },
    {
      type: "context",
      elements: [
        { type: "mrkdwn", text: "Version: 2.1.0 | By: <@U456>|Bob | Time: 3:00 PM" }
      ]
    },
    {
      type: "section",
      fields: [
        { type: "mrkdwn", text: "*Changes:*\n• Feature A\n• Bug fix #123" }
      ]
    }
  ]
};
```

### Scheduled Reports

```javascript
// Weekly summary (Every Monday 9 AM)
schedule.scheduleJob('0 9 * * 1', async () => {
  const stats = await getWeeklyStats();
  
  await client.chat.postMessage({
    channel: 'C0123456789',
    text: 'Weekly Team Summary',
    blocks: [
      { type: "header", text: { type: "plain_text", text: "📊 Weekly Summary" } },
      { type: "section", fields: [
        { type: "mrkdwn", text: `*Tasks Completed:*\n${stats.completed}` },
        { type: "mrkdwn", text: `*PRs Merged:*\n${stats.prsMerged}` }
      ]},
      { type: "divider" },
      { type: "section", text: { type: "mrkdwn", text: `*Top Contributors:*\n${stats.topContributors}` } }
    ]
  });
});
```

## 9.3 DevOps Workflows

### CI/CD Pipeline Integration

```
GitHub Actions → Slack:
1. push to main → Notify #deployments
2. PR created → Notify #pr-reviews
3. PR merged → Start deployment
4. Deployment started → Track progress
5. Deployment success/failure → Notify team

Workflow:
on:
  push:
    branches: [main]

jobs:
  deploy:
    steps:
      - name: Notify Slack
        uses: slackapi/slack-github-action@v1
        with:
          channel-id: 'C0123456789'
          payload: |
            {
              "text": "Deploying to production...",
              "blocks": [...]
            }
```

### Incident Response Bot

```
Incident Created:
/incident create "Database outage"
├─ Create dedicated channel #incident-YYYY-MM-DD
├─ Add incident commander
├─ Set status to "Active"
├─ Start timer
└─ Post incident template

During Incident:
- /incident update "Identified root cause: disk full"
- /incident post "Working on solution"
- /incident post "Applying fix now"

Incident Resolved:
/incident resolve
├─ Post summary
├─ Calculate duration
├─ Create post-mortem task
├─ Archive channel
└─ Send metrics to #incidents
```

### Deployment Checklist

```javascript
const deploymentChecklist = {
  blocks: [
    {
      type: "section",
      text: { type: "mrkdwn", text: "🚀 *Production Deployment Checklist*" }
    },
    {
      type: "actions",
      elements: [
        { type: "button", text: { type: "plain_text", text: "✅ DB Migration" }, action_id: "check_db" },
        { type: "button", text: { type: "plain_text", text: "✅ Tests Pass" }, action_id: "check_tests" },
        { type: "button", text: { type: "plain_text", text: "✅ Staging Verified" }, action_id: "check_staging" }
      ]
    },
    {
      type: "actions",
      elements: [
        { type: "button", text: { type: "plain_text", text: "Deploy Now" }, style: "primary", action_id: "deploy" },
        { type: "button", text: { type: "plain_text", text: "Cancel" }, action_id: "cancel" }
      ]
    }
  ]
};
```

### Monitoring Alerts

```
Alert Levels:

P1 (Critical):
- Immediate Slack notification
- DM to on-call engineer
- Create incident channel
- Phone call escalation

P2 (High):
- Post to #alerts
- DM to team lead
- Create tracking ticket

P3 (Medium):
- Post to #monitoring
- Daily summary digest

Alert Message Format:
🔴 *[P1]* Service: payments-api | Error rate: 45% | Duration: 5min
   └─ <Link to dashboards>
   └─ <Link to logs>
```
