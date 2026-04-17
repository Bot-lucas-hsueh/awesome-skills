# Standards & Reference

## 7.1 Official Documentation

- [Notion Help Center](https://www.notion.so/help)
- [Notion API Documentation](https://developers.notion.com)
- [Notion Integrations](https://www.notion.so/integrations)
- [Notion Templates](https://www.notion.so/templates)
- [Block Types Reference](https://developers.notion.com/reference/block-type)
- [Property Values](https://developers.notion.com/reference/property-value)
- [Database Schema](https://developers.notion.com/docs/database)
- [Permissions & Access](https://www.notion.so/help/different-levels-of-permissions)

## 7.2 Configuration Reference

### Notion API Setup

```json
{
  "notion": {
    "auth": "secret_xxxxxxxxxxxxxxxxxxxx",
    "version": "2022-02-22"
  }
}
```

### Integration Configuration

```yaml
# Notion API Client Setup
integration:
  name: "Team Workspace Bot"
  capabilities:
    - read_content
    - update_content
    - insert_content
    - query_database
  workspace:
    id: "workspace_id_here"
    name: "Engineering Team"
```

### Database Schema Examples

**Project Tracker Database:**

```json
{
  "Name": { "title": {} },
  "Status": { "select": { "options": ["Active", "Paused", "Completed"] } },
  "Priority": { "select": { "options": ["Critical", "High", "Medium", "Low"] } },
  "Deadline": { "date": {} },
  "Assignee": { "people": [] },
  "Tags": { "multi_select": { "options": ["frontend", "backend", "design"] } },
  "Progress": { "number": { "format": "percent" } },
  "Related": { "relation": { "database_id": "other_db_id" } }
}
```

**Task Management Database:**

```json
{
  "Task": { "title": {} },
  "Done": { "checkbox": {} },
  "Due": { "date": {} },
  "Assigned": { "people": [] },
  "Status": { 
    "status": { 
      "options": [
        { "name": "Not started", "color": "gray" },
        { "name": "In progress", "color": "blue" },
        { "name": "Complete", "color": "green" }
      ]
    }
  },
  "Estimate": { "number": { "format": "hours" } },
  "Priority": { "select": { "options": ["P1", "P2", "P3"] } }
}
```

## 7.3 Common Commands & Operations

### API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/v1/databases/{id}/query` | POST | Query database with filters |
| `/v1/pages` | POST | Create new page |
| `/v1/pages/{id}` | PATCH | Update page properties |
| `/v1/blocks/{id}/children` | GET | Get page content |
| `/v1/search` | POST | Search pages and databases |

### Query Filters

```json
{
  "filter": {
    "property": "Status",
    "select": { "equals": "Active" }
  },
  "sorts": [
    { "property": "Deadline", "direction": "ascending" }
  ],
  "page_size": 100
}
```

### Filter Operators

| Property Type | Operators |
|--------------|-----------|
| Select | equals, does_not_equal |
| Multi-select | contains, does_not_contain |
| Date | equals, before, after, is_empty |
| Number | equals, greater_than, less_than |
| Checkbox | equals |
| Text | contains, does_not_contain, starts_with |

## 7.4 Version & Platform Compatibility

| Platform | Status | Notes |
|----------|--------|-------|
| Notion Web | Current | Full functionality |
| Notion Desktop (macOS/Windows) | Current | Offline support |
| Notion Mobile (iOS/Android) | Current | Limited views |
| Notion API | v2022-02-22 | Stable, breaking changes quarterly |

| Feature | Free | Plus | Business | Enterprise |
|---------|------|------|----------|------------|
| API requests | 100/min | 100/min | 250/min | Custom |
| Blocks per page | Unlimited | Unlimited | Unlimited | Unlimited |
| Shared workspaces | 5 guests | Unlimited | Unlimited | Unlimited |
| Version history | 7 days | 30 days | 90 days | Unlimited |
| API | No | Yes | Yes | Yes |

### Rate Limits

```
Free/Plus: 3 requests/second
Business: 5 requests/second  
Enterprise: Custom limits
Retry: Exponential backoff (1s, 2s, 4s, 8s...)
```
