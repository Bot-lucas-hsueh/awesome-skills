# Standards & Reference

## 7.1 Official Documentation

- [Miro Developer Documentation](https://developers.miro.com/docs)
- [Miro Web SDK Reference](https://dev.miro.com/docs)
- [Miro REST API](https://miro.com/app/settings/user-profile/apps/api-scopes)
- [Miro Platform Overview](https://miro.com/platform)
- [Miro Web Plugin SDK](https://www.npmjs.com/package/@mirohq/websdk-types)
- [Miro App Authorization](https://dev.miro.com/docs/authentication)
- [Miro Widgets Reference](https://dev.miro.com/docs/widgets-overview)
- [Miro Board API](https://dev.miro.com/docs/boards-api)

## 7.2 Configuration Reference

### App Manifest (manifest.json)

```json
{
  "name": "Team Productivity Plugin",
  "version": "1.0.0",
  "description": "Automates team workflows on Miro boards",
  "sdkVersion": "2.0",
  "appMode": "app",
  "permissions": [
    "board:read",
    "board:write",
    "board:content:read",
    "board:content:write"
  ],
  "locales": ["en-US", "es-ES"],
  "features": {
    "core": {
      "autoboard": false,
      "editableBoard": true
    },
    "topBar": {
      "name": "Productivity Tools",
      "icon": "./assets/icon.svg"
    }
  },
  "dataSources": {
    "miro": ["boards"]
  }
}
```

### Web SDK Configuration

```javascript
import { create, BoardSidePanel } from '@mirohq/websdk-ui';

const miro = create({
  board: {
    read: true,
    write: true
  }
});

// Initialize app
async function init() {
  const board = await miro.board.get();
  const widgets = await board.widgets.get();
  return { board, widgets };
}
```

### REST API Configuration

```bash
# Environment Setup
MIRO_CLIENT_ID=your_client_id
MIRO_CLIENT_SECRET=your_client_secret
MIRO_REDIRECT_URI=https://your-app.com/callback

# OAuth Flow
# 1. Authorization URL
https://miro.com/oauth/authorize?response_type=code&client_id=${MIRO_CLIENT_ID}&redirect_uri=${MIRO_REDIRECT_URI}

# 2. Token Exchange
curl -X POST https://api.miro.com/v1/oauth/token \
  -H "Content-Type: application/json" \
  -d '{"grant_type": "authorization_code", "code": "...", "client_id": "...", "client_secret": "..."}"
```

### Widget Configuration

```javascript
// Create sticky note
const stickyNote = await miro.board.createStickyNote({
  x: 0,
  y: 0,
  rotation: 0,
  width: 200,
  text: 'New Task',
  fields: {
    customField: 'value'
  }
});

// Create shape
const shape = await miro.board.createShape({
  x: 200,
  y: 0,
  width: 150,
  height: 100,
  shape: 'rectangle',
  style: {
    fillColor: '#ffffff',
    borderColor: '#000000'
  }
});

// Create connector
const connector = await miro.board.createConnector({
  startWidgetId: stickyNote.id,
  endWidgetId: shape.id,
  startSide: 'right',
  endSide: 'left',
  style: {
    color: '#000000',
    width: 2
  }
});
```

## 7.3 Common Commands & Operations

### REST API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v2/boards` | GET | List boards |
| `/v2/boards/{id}` | GET | Get board details |
| `/v2/boards/{id}/items` | GET | Get board items |
| `/v2/boards/{id}/items` | POST | Create item |
| `/v2/boards/{id}/items/{item_id}` | PATCH | Update item |
| `/v2/boards/{id}/items/{item_id}` | DELETE | Delete item |

### Widget Types

| Type | Class | Description |
|------|-------|-------------|
| Sticky Note | `StickyNote` | Colored notes |
| Shape | `Shape` | Rectangles, circles, etc. |
| Text | `Text` | Plain text blocks |
| Card | `Card` | Trello-like cards |
| Frame | `Frame` | Container for organizing |
| Connector | `Connector` | Lines connecting items |
| Image | `Image` | Uploaded images |
| Embed | `Embed` | Embedded content |

## 7.4 Version & Platform Compatibility

| Platform | Status | Notes |
|----------|--------|-------|
| Miro Web | Current | Full functionality |
| Miro Desktop | Current | Windows/macOS |
| Miro Mobile | Current | Limited editing |
| Web SDK | v2.x | Current stable |
| REST API | v2 | Current stable |

| Plan | Boards | Members | History |
|------|--------|---------|---------|
| Free | 3 | 3 | 7 days |
| Starter | Unlimited | 10 | 90 days |
| Business | Unlimited | Unlimited | Unlimited |
| Enterprise | Unlimited | Unlimited | Unlimited |

### Rate Limits

```
REST API:
- 200 requests per minute per team
- 50 requests per minute per app instance

Web SDK:
- No explicit limits but be reasonable
- Batch operations when possible

Retry with exponential backoff:
- Initial: 1 second
- Max retries: 3
```
