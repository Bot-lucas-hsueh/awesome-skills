# Standard Workflow

## 8.1 Project Management Workflow

```
Project Creation Flow
├── 1. Create Project Database
│   ├── Define schema (Status, Priority, Due Date, Assignee)
│   ├── Set up views (Board, Calendar, Timeline, Gallery)
│   └── Configure filters for team views
│
├── 2. Create Project Page
│   ├── Overview section with goals
│   ├── Link to project database
│   ├── Team directory
│   └── Resources section
│
├── 3. Set Up Recurring Tasks
│   ├── Weekly team sync template
│   ├── Sprint planning template
│   ├── Daily standup format
│   └── Monthly review template
│
└── 4. Automate Notifications
    ├── Task due tomorrow → Slack alert
    ├── Task overdue → Email reminder
    └── New project page → Team notification
```

## 8.2 Integration Workflow

### Slack Integration

```
Notion Actions in Slack:
/notion create "New task" → Creates page in inbox
/notion search [query] → Returns matching pages
/notion link [URL] → Saves to Notion

Slack → Notion:
1. Slack message with @notion-bot
2. Reaction with 📝 to save to Notion
3. Slash command to create task
```

### GitHub Integration

```
PR Opened:
1. GitHub action triggers Notion API
2. Create/update issue page in project
3. Link PR to related tasks
4. Update task status to "In Review"

PR Merged:
1. Update task status to "Complete"
2. Move to completed section
3. Notify team in Slack
```

### Calendar Integration

```
Notion → Google Calendar / Outlook:
1. Connect calendar to Notion
2. Database date properties sync automatically
3. Events appear in Notion calendar view

Calendar → Notion Tasks:
1. Meeting ends → Create follow-up task
2. Task due today appears in daily agenda
3. Overdue items highlighted
```

### Zapier/Make Integration

```yaml
Trigger: Notion Database Item Created
Action: Send Slack message
Message: "New task: {{title}} assigned to {{assignee}}"

Trigger: Row updated in Notion
Action: Create calendar event
Event: "Follow-up: {{task_name}}"

Trigger: Due date approached
Action: Send email reminder
Email: "Task '{{name}}' due tomorrow"
```

## 8.3 Automation Workflow

### Task Lifecycle Automation

```
Trigger: New task created in "Tasks" database
├─ Set default status: "Not Started"
├─ Set created date: auto
├─ Assign to creator
└─ Send confirmation to creator

Trigger: Due date = today
├─ Change status: "Due Today"
├─ Add tag: "urgent"
└─ Send Slack notification

Trigger: Status changed to "Complete"
├─ Set completion date
├─ Move to "Completed" section
└─ Archival after 30 days
```

### Team Workflows

```
Daily Standup Notion Page:
├─ Created: Daily at 8:00 AM (template)
├─ Contains: Yesterday, Today, Blockers
├─ Team members fill in
└─ Auto-archive after 7 days

Weekly Review:
├─ Created: Monday 9:00 AM
├─ Filter: Tasks completed this week
├─ Filter: Overdue tasks
├─ Team notes section
└─ Linked to sprint database
```

### Content Pipeline

```
Content Database:
├─ Status: Draft → Review → Approved → Published
├─ Author property
├─ Reviewer property
├─ Publish date
├─ Category (multi-select)
└─ Word count (formula)

Automation:
Draft Created → Notify editor
Review Requested → Assign reviewer
Review Complete → Move to Approved
Publish Date = Today → Move to Published
```
