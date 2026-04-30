# Standard Workflow

## 8.1 Collaborative Workshop Workflow

```
Workshop Setup Flow
├── Pre-Workshop
│   ├── Create board from template
│   ├── Set up frames for each section
│   │   ├── Problem Statement
│   │   ├── Brainstorming
│   │   ├── Voting
│   │   └── Action Items
│   ├── Add instructions as text boxes
│   └── Configure voting/reaction settings
│
├── During Workshop
│   ├── Share board link with participants
│   ├── Assign facilitator role
│   ├── Guide through each frame
│   └── Capture outputs in real-time
│
└── Post-Workshop
    ├── Export board as PDF/PNG
    ├── Export data as CSV/JSON
    ├── Archive board
    └── Create follow-up tasks
```

## 8.2 Integration Workflow

### Jira Integration

```
Miro Board ↔ Jira:
1. Install Miro Jira integration
2. Connect to Jira workspace
3. Link sticky notes to Jira issues
4. Sync status updates

Workflow:
- Create sticky note on board
- Click "Link to Jira"
- Select issue or create new
- Status syncs automatically
```

### GitHub Integration

```
PR Review on Miro:
1. Create board for PR review
2. Add PR details as text
3. Add code snippets as sticky notes
4. Team annotates on board
5. Export comments back to PR

Branch Planning:
1. Create frame for each feature branch
2. Add related issues as cards
3. Visualize dependencies with connectors
4. Track progress by card status
```

### Slack Integration

```
Miro → Slack:
1. Share board updates to Slack channels
2. Post notifications for new comments
3. Share specific frames/views
4. Alert when action items created

Workflow:
- Someone adds action item on board
- Miro bot posts to Slack
- Assigned user receives DM
- User clicks to open board
```

### API Integration Flow

```javascript
// Sync Miro board to external system
async function syncBoard(boardId) {
  // Get all items from board
  const items = await getBoardItems(boardId);
  
  // Filter actionable items
  const tasks = items.filter(item => 
    item.type === 'sticky_note' && 
    item.fields?.hashtag === '#action'
  );
  
  // Create tasks in external system
  for (const task of tasks) {
    await externalSystem.createTask({
      title: task.text,
      assignee: task.fields?.assignee,
      dueDate: task.fields?.dueDate
    });
    
    // Mark as synced
    await updateItem(task.id, { fields: { synced: true } });
  }
}
```

## 8.3 Automation Workflow

### Board Template Automation

```javascript
// Create project kickoff board
async function createProjectBoard(projectName) {
  const board = await miro.board.createBoard({
    name: `${projectName} - Kickoff`,
    description: 'Project kickoff planning board'
  });
  
  // Create sections
  const goalsFrame = await miro.board.createFrame({
    x: 0,
    y: 0,
    width: 800,
    height: 600,
    title: 'Goals & Objectives'
  });
  
  const timelineFrame = await miro.board.createFrame({
    x: 900,
    y: 0,
    width: 800,
    height: 600,
    title: 'Timeline'
  });
  
  // Add template content
  await miro.board.createStickyNote({
    x: 100,
    y: 100,
    text: '🎯 Main Goal:\n[TODO: Add main goal]'
  });
  
  // Add instructions
  await miro.board.createText({
    x: 0,
    y: -400,
    text: '# Instructions\n1. Review goals\n2. Add milestones\n3. Assign owners'
  });
  
  return board;
}
```

### Sprint Planning Automation

```
Weekly Sprint Planning:
1. Bot creates new board from template
2. Board includes: Backlog, Sprint Goals, Timeline
3. Import issues from Jira/Linear
4. Team estimates on board
5. Bot exports final sprint to project management

Flow:
Template → Import Issues → Team Planning → Export Sprint
```

### Real-time Collaboration Sync

```javascript
// Sync changes to external dashboard
miro.board.on('item:update', async (event) => {
  const { item, field, oldValue, newValue } = event;
  
  if (item.type === 'sticky_note' && field === 'status') {
    // Update external task
    await externalSystem.updateTask(item.id, { status: newValue });
    
    // Notify team
    await notifyTeam(item, 'status changed');
  }
});
```

### Action Item Extraction

```javascript
// Extract action items from workshop board
async function extractActionItems(boardId) {
  const items = await getBoardItems(boardId);
  
  // Find items marked as action items
  const actions = items.filter(item => {
    if (item.type !== 'sticky_note') return false;
    const text = item.text.toLowerCase();
    return text.includes('@') || text.includes('#action');
  });
  
  // Format for export
  return actions.map(item => ({
    id: item.id,
    text: item.text,
    assignee: extractAssignee(item.text),
    dueDate: item.fields?.dueDate,
    priority: item.fields?.priority
  }));
}
```
