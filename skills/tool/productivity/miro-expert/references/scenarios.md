# Scenario Examples

## 9.1 Team Workflows

### Scenario: Agile Retrospective Board

**User:** "How do I set up a sprint retrospective on Miro?"

**Expert:**
> **Retrospective Board Structure:**
>
> ```
> Board: Sprint 24 Retrospective
> │
> ├─ Frame: 🎯 What Went Well
> │   ├── Sticky Notes (Green)
> │   └── Team contributions
> │
> ├─ Frame: 🚧 What to Improve
> │   ├── Sticky Notes (Yellow)
> │   └── Action items
> │
> ├─ Frame: 💡 New Ideas
> │   ├── Sticky Notes (Blue)
> │   └── Brainstorm results
> │
> └─ Frame: ✅ Action Items
>     ├── Cards with owners
>     └── Due dates
> ```
>
> **Best Practices:**
> - Use different colors for each category
> - Set timer for silent brainstorming
> - Group related stickies with frames
> - Vote on top items before discussion

### Scenario: User Story Mapping

**User:** "How do I create a user story map in Miro?"

**Expert:**
> **User Story Map Structure:**
>
> ```
> Rows (Activities):
> - Discover
> - Learn
> - Register
> - Shop
> - Checkout
> - Support
>
> Columns (Releases):
> | MVP | v1.1 | v1.2 | v2.0 |
> -----------------------------------
> |     |      |      |       |
> |     |      |      |       |
>
> Cards:
> - Release MVP: Register email, Basic checkout
> - v1.1: Social login, Wishlist
> - v1.2: 1-Click checkout, Order history
> ```
>
> **Implementation:**
> 1. Create rows as horizontal swimlanes
> 2. Create frames for each release
> 3. Add cards to corresponding cells
> 4. Connect related cards across rows

## 9.2 Automation Scenarios

### Miro Board Templates

```javascript
// Retrospective template
const retrospectiveTemplate = {
  name: 'Sprint Retrospective',
  frames: [
    { title: '🎯 Went Well', color: '#00ff00', x: 0, y: 0 },
    { title: '🚧 Improve', color: '#ffff00', x: 400, y: 0 },
    { title: '💡 Ideas', color: '#00ffff', x: 800, y: 0 },
    { title: '✅ Actions', color: '#ff6600', x: 1200, y: 0 }
  ],
  instructions: [
    { text: 'Add sticky notes to each section', x: 0, y: -200 },
    { text: 'Vote on top items', x: 400, y: -200 }
  ]
};

// Create from template
async function createRetrospective(sprintName) {
  const board = await miro.board.createBoard({ name: sprintName });
  
  for (const frame of retrospectiveTemplate.frames) {
    await miro.board.createFrame({
      ...frame,
      width: 350,
      height: 500
    });
  }
  
  return board;
}
```

### Workflow Board Patterns

```
Kanban Board:
├─ To Do Column
│   └─ Sticky notes (tasks)
├─ In Progress Column
│   └─ Sticky notes with owner tag
├─ Review Column
│   └─ Cards linked to PRs
└─ Done Column
    └─ Completed items (grayed)

Implementation:
- Use frames for columns
- Sticky notes as task cards
- Color-code by priority
- Use connectors to show blockers
```

### Time Boxing Session

```javascript
// Pomodoro-style workshop timer
async function runTimeboxedSession(session) {
  const { duration, topic, participants } = session;
  
  // Create topic frame
  const frame = await miro.board.createFrame({
    x: 0, y: 0,
    title: topic,
    width: 800, height: 400
  });
  
  // Add timer widget
  const timerText = await miro.board.createText({
    x: 0, y: -250,
    text: `# Timer: ${duration} minutes`,
    style: { fontSize: 24 }
  });
  
  // Start countdown
  let remaining = duration * 60;
  const interval = setInterval(async () => {
    remaining--;
    if (remaining <= 0) {
      clearInterval(interval);
      await notifyParticipants('Time is up!');
    }
  }, 1000);
}
```

## 9.3 DevOps Workflows

### Architecture Diagram

```
Infrastructure Planning Board:
├─ Current Architecture
│   └─ Shapes showing components
│   └─ Connectors showing traffic flow
│   └─ Labels showing technologies
│
├─ Proposed Architecture
│   └─ New components highlighted
│   └─ Migration steps numbered
│
├─ Decision Log
│   └─ Cards with pros/cons
│   └─ Linked to issues
│
└─ Action Items
    └─ Owner tags
    └─ Due dates

Shapes Used:
- Rectangles: Services/applications
- Cylinders: Databases
- Circles: External services
- Arrows: Data flow
- Cloud shapes: AWS/GCP/Azure services
```

### Incident Post-Mortem Board

```
Post-Mortem Board Template:
├─ Timeline (Horizontal)
│   └─ Events with timestamps
│   └─ Color-coded by severity
│
├─ Impact Assessment
│   └─ Duration, users affected
│   └─ Cost impact
│
├─ Root Cause
│   └─ Fishbone diagram
│   └─ 5 Whys analysis
│
├─ Action Items
│   └─ Cards with owners
│   └─ Priority labels
│   └─ Due dates
│
└─ Lessons Learned
    └─ Key takeaways
    └─ Process improvements
```

### Deployment Planning

```
Release Planning Board:
├─ Scope
│   └─ Features for this release
│   └─ Dependencies highlighted
│
├─ Risk Matrix
│   └─ Likelihood vs Impact grid
│   └─ Risk cards in quadrants
│
├─ Rollback Plan
│   └─ Step-by-step cards
│   └─ Decision points
│
├─ Communication Plan
│   └─ Stakeholder notifications
│   └─ Status update times
│
└─ Sign-off Checklist
    └─ Required approvals
    └─ Checkbox items

Board Features:
- Time: Auto-updating timer
- Version: Sticky note with version
- Status: Color-coded progress
```

### Sprint Board Sync

```javascript
// Sync Miro board with project management
async function syncWithJira(boardId, jiraProject) {
  const board = await getBoard(boardId);
  
  // Get frame IDs for columns
  const frames = board.items.filter(i => i.type === 'frame');
  const columns = {
    todo: frames.find(f => f.title.includes('To Do'))?.id,
    inProgress: frames.find(f => f.title.includes('In Progress'))?.id,
    done: frames.find(f => f.title.includes('Done'))?.id
  };
  
  // Sync each column
  for (const [status, frameId] of Object.entries(columns)) {
    const items = await getFrameItems(frameId);
    
    for (const item of items) {
      if (item.type === 'card' && !item.fields?.jiraKey) {
        // Create Jira issue
        const issue = await jira.createIssue({
          summary: item.text,
          status,
          project: jiraProject
        });
        
        // Link back
        await updateItem(item.id, { 
          fields: { jiraKey: issue.key }
        });
      }
    }
  }
}
```
