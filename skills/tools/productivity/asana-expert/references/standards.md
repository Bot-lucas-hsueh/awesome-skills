# Standards & Reference

## 7.1 Official Documentation

- [Asana Developer Docs](https://developers.asana.com/docs)
- [API Reference](https://developers.asana.com/reference)
- [OAuth 2.0 Guide](https://developers.asana.com/docs/oauth)
- [Asana Connect](https://app.asana.com/-/oauth_authorize)
- [Patron API](https://developers.asana.com/docs/personal-access-token)
- [Webhook Events](https://developers.asana.com/docs/webhook-events)
- [Asana Search](https://developers.asana.com/docs/search-73)
- [Asana Status Page](https://www.asana.com/free/status)
- [Rate Limits](https://developers.asana.com/docs/rate-limits)
- [Bulk APIs](https://developers.asana.com/docs/bulk)
- [Batch Requests](https://developers.asana.com/docs/batch-requests)

## 7.2 Configuration Reference

### Authentication

```python
import asana

# Personal Access Token
client = asana.Client.access_token('YOUR_PAT')

# OAuth 2.0
from urllib.parse import urlencode
auth_url = 'https://app.asana.com/-/oauth_authorize?' + urlencode({
    'client_id': 'CLIENT_ID',
    'redirect_uri': 'https://yourapp.com/callback',
    'response_type': 'code',
    'scope': 'default'
})

# Exchange code for token
import requests
response = requests.post('https://app.asana.com/-/oauth_token', data={
    'grant_type': 'authorization_code',
    'client_id': 'CLIENT_ID',
    'client_secret': 'CLIENT_SECRET',
    'redirect_uri': 'https://yourapp.com/callback',
    'code': authorization_code
})
access_token = response.json()['access_token']
```

### Project Configuration

```python
# Create a project
project = client.projects.create({
    'name': 'Q1 Product Launch',
    'workspace': 'WORKSPACE_GID',
    'notes': 'Launch campaign for Q1 2024',
    'default_view': 'list',
    'is_public': False,
    'color': 'dark-pink',
    'icon': 'goal',
    'due_date': '2024-03-31',
    'start_on': '2024-01-01'
})

# Add custom fields
custom_field = client.custom_fields.create({
    'name': 'Priority',
    'type': 'enum',
    'enum_options': [
        {'name': 'High', 'color': 'red'},
        {'name': 'Medium', 'color': 'yellow'},
        {'name': 'Low', 'color': 'green'}
    ],
    'workspace': 'WORKSPACE_GID'
})

# Create task with custom fields
task = client.tasks.create({
    'name': 'Design landing page',
    'projects': [project['gid']],
    'assignee': 'user@company.com',
    'due_on': '2024-02-15',
    'custom_fields': [
        {'gid': custom_field['gid'], 'enum_value': {'gid': high_priority_gid}}
    ],
    'notes': 'Design specs: https://figma.com/...',
    'followers': ['user@company.com']
})
```

### Webhook Configuration

```python
# Register a webhook
webhook = client.webhooks.create({
    'resource': project['gid'],
    'target': 'https://yourapp.com/asana/webhook',
    'filters': [
        {
            'action': 'changed',
            'fields': ['name', 'completed'],
            'resource_type': 'task'
        }
    ]
})

# Verify webhook signature
import hmac
import hashlib

def verify_webhook(request):
    signature = request.headers.get('X-Hook-Signature', '')
    body = request.get_data(as_text=True)
    secret = 'WEBHOOK_SECRET'
    expected = hmac.new(
        secret.encode(),
        body.encode(),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(signature, expected)
```

## 7.3 Common Commands

### Task Operations

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET /tasks/{task_gid}` | Retrieve task | Get task details |
| `POST /tasks` | Create task | Create new task |
| `PUT /tasks/{task_gid}` | Update task | Modify task |
| `DELETE /tasks/{task_gid}` | Delete task | Remove task |
| `POST /tasks/{task_gid}/subtasks` | Add subtask | Create subtask |
| `POST /tasks/{task_gid}/addFollowers` | Add followers | Add watchers |
| `POST /tasks/{task_gid}/stories` | Add comment | Add story |
| `GET /tasks/{task_gid}/subtasks` | List subtasks | Get subtasks |
| `POST /tasks/{task_gid}/duplicate` | Duplicate | Copy task |

### Project Operations

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET /projects/{project_gid}` | Get project | Retrieve project |
| `POST /projects` | Create project | Create new project |
| `POST /projects/{gid}/addMembers` | Add members | Add team members |
| `GET /projects/{gid}/tasks` | Project tasks | Get all tasks |
| `POST /projects/{gid}/sections` | Create section | Add section |

### Search

```python
# Search tasks
results = client.search.tasks_for_workspace(
    'WORKSPACE_GID',
    {
        'text': 'landing page',
        'projects': ['PROJECT_GID'],
        'assignee': 'me',
        'completed': False,
        'due_on.after': 'today',
        'sort_by': 'due_on',
        'opt_fields': 'name,due_on,assignee.name,custom_fields'
    }
)

# Advanced search
tasks = client.tasks.search({
    'workspace': 'WORKSPACE_GID',
    'filters': [
        {
            'field': 'due_on',
            'op': 'is_less_than',
            'value': '2024-03-01'
        },
        {
            'field': 'custom_fields.Priority',
            'op': 'is_not',
            'value': 'Low'
        }
    ]
})
```

## 7.4 Field Reference

### Task Fields

| Field | Type | Description |
|-------|------|-------------|
| `name` | string | Task name |
| `notes` | string | Task description |
| `completed` | boolean | Completion status |
| `assignee` | User | Assigned user |
| `assignee.name` | string | Assignee display name |
| `due_on` | string | Due date (YYYY-MM-DD) |
| `start_on` | string | Start date |
| `due_at` | string | Due datetime |
| `memberships` | array | Project/section membership |
| `custom_fields` | array | Custom field values |
| `followers` | array | Task followers |
| `projects` | array | Projects containing task |
| `parent` | Task | Parent task (for subtasks) |
| `tags` | array | Tags applied to task |
| `num_subtasks` | integer | Count of subtasks |
| `approval_status` | string | Approval status |
| `liked` | boolean | Whether liked |

### Custom Field Types

| Type | Options | Example |
|------|---------|---------|
| `text` | none | Free-form text |
| `number` | `precision` | Decimal value |
| `enum` | `enum_options` | Dropdown choice |
| `date` | none | Date value |
| `people` | none | User reference |
| `tracker` | none | Progress tracker |
| `formula` | computed | Calculated value |

## 7.5 Pagination and Filtering

```python
# Pagination with collection limit
tasks = client.tasks.get_tasks(
    {'workspace': 'WORKSPACE_GID', 'limit': 100},
    opt_pretty=True
)

# Get all pages automatically
all_tasks = list(client.tasks.get_tasks(
    {'workspace': 'WORKSPACE_GID', 'limit': 100},
    items_per_page=100
))

# Using next_page token
def get_all_tasks():
    tasks = []
    result = client.tasks.get_tasks({'workspace': 'WORKSPACE_GID'})
    while result:
        tasks.extend(result.data)
        result = result.next_page()
    return tasks

# Filtering with opt_fields
tasks = client.tasks.get_tasks({
    'project': 'PROJECT_GID',
    'completed': False,
    'opt_fields': 'name,due_on,assignee.email,tags.name'
})
```

## 7.6 Batch Operations

```python
# Batch request
batch_response = client.batch.create({
    'data': [
        {
            'method': 'GET',
            'relative_path': '/tasks/123'
        },
        {
            'method': 'PUT',
            'relative_path': '/tasks/456',
            'data': {'completed': True}
        },
        {
            'method': 'POST',
            'relative_path': '/tasks',
            'data': {'name': 'New Task', 'projects': ['PROJECT_GID']}
        }
    ]
})

# Handle responses
for result in batch_response['data']:
    if 'body' in result:
        print(result['body'])
```

## 7.7 Asana Connect Scopes

| Scope | Access |
|-------|--------|
| `default` | Read/write access to most resources |
| `basic` | Read access to profiles, no write |
| `openid` | OpenID Connect user info |
| `email` | User email address |
| `profile` | User profile photo and name |
| `workspace` | Workspace membership info |
| `task:assignees` | Ability to assign/unassign tasks |
| `project:read` | Read project membership |
