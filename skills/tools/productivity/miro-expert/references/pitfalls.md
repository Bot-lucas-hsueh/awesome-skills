# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | **Unorganized boards** | Medium | Use frames to organize sections |
| 2 | **No naming conventions** | Medium | Establish board/item naming standards |
| 3 | **Overcrowded boards** | Medium | Split into multiple boards |
| 4 | **Ignoring templates** | Low | Use templates for consistency |
| 5 | **Manual data sync** | High | Automate with API integrations |
| 6 | **No board archiving** | Low | Archive completed boards |
| 7 | **Too many shapes** | Low | Keep it simple, use sticky notes |
| 8 | **Missing instructions** | Medium | Add setup instructions on board |

### Anti-Pattern: Disorganized Brainstorming

```
Anti-Pattern:
Board with 50 sticky notes, no organization
Random placement, hard to read

Solution:
- Create frames before brainstorming
- One frame per category
- Use color coding
- Group related items
- Add voting after silent phase
```

## 10.2 Anti-Patterns

### 1. Using Boards as File Storage

```
Anti-Pattern:
- Uploading PDFs, spreadsheets to board
- Storing documents in sticky notes
- No visual planning, just file dump

Problem: Hard to find, doesn't leverage visual collaboration

Solution:
- Use Miro for visual collaboration
- Link to external documents
- Use board for planning, docs for details
```

### 2. No Collaboration Guidelines

```
Anti-Pattern:
- Everyone editing at once
- No clear facilitator
- Editing conflicts
- Chaos

Solution:
- Assign facilitator role
- Use timeboxing
- Define contribution guidelines
- Use "Present" mode for focus
```

### 3. Over-Engineering Diagrams

```
Anti-Pattern:
- Perfect alignment required
- 20+ colors for diagram
- Complex shapes everywhere

Problem: Takes too long, less engaging

Solution:
- Use simple sticky notes and shapes
- Good enough is good enough
- Speed over polish
```

### 4. No Clear Outcome

```
Anti-Pattern:
- Meeting without agenda
- Board created but no goal
- Discussion goes nowhere

Solution:
- Define success criteria upfront
- Capture action items separately
- End with clear next steps
```

### 5. Stale Content

```
Anti-Pattern:
- Old boards never archived
- Outdated information stays
- Wrong versions of truth

Solution:
- Set board expiration reminders
- Archive completed boards
- Regular board audits
- Use board status indicators
```

## 10.3 Integration Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| No caching for API calls | Rate limit errors | Cache responses |
| Polling too frequently | Performance issues | Use webhooks |
| Syncing everything | Data inconsistencies | Sync only actionable items |
| No error handling | Silent failures | Log and alert |
| Bidirectional sync loops | Infinite loops | One-way sync or debounce |

## 10.4 Performance Anti-Patterns

```javascript
// BAD: Getting all items every update
async function syncBoard() {
  const items = await board.getItems(); // Gets ALL items
  for (const item of items) {
    await syncToExternal(item);
  }
}

// GOOD: Only get changed items
async function syncBoard(lastSync) {
  const items = await board.getItems({
    modifiedAfter: lastSync
  });
  // Now only syncs changed items
}

// BAD: Creating items one by one
for (const task of tasks) {
  await miro.board.createStickyNote(task);
}

// GOOD: Batch operations
await miro.board.bulkCreateStickyNotes(tasks);

// BAD: No pagination handling
const items = await board.getItems(); // May be truncated

// GOOD: Handle pagination
let cursor;
do {
  const result = await board.getItems({ cursor });
  items.push(...result.data);
  cursor = result.cursor;
} while (cursor);
```

## 10.5 Web SDK Anti-Patterns

```javascript
// BAD: No cleanup
app.configure(({ addClickHandler }) => {
  addClickHandler('button', () => {
    // Creates new listener every click
  });
});

// GOOD: Proper cleanup
let cleanup;
app.configure(({ addClickHandler, addDestroyHandler }) => {
  const handler = () => processClick();
  addClickHandler('button', handler);
  addDestroyHandler(() => removeClickHandler('button', handler));
});

// BAD: Accessing DOM directly
document.querySelector('.my-class').style.display = 'none';

// GOOD: Use Miro UI components
import { Button } from '@mirohq/websdk-ui';
const button = new Button({ label: 'Click me' });
button.onClick(() => handleClick());
```
