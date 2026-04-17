# Standard Workflow

## 8.1 Getting Started

```
Phase 1: API Access Setup
├── Create Asana developer account
├── Register an application
├── Generate Personal Access Token (for testing)
├── Configure OAuth 2.0 (for production apps)
└── Install client library (pip install asana)

Phase 2: Basic Operations
├── List workspaces and projects
├── Retrieve team structure
├── Create your first task
├── Add comments and attachments
└── Test webhook endpoints

Phase 3: Integration Development
├── Map your data model to Asana concepts
├── Implement pagination for large datasets
├── Add error handling and retries
├── Set up webhook processing
└── Build caching layer

Phase 4: Production Deployment
├── Implement rate limit handling
├── Add proper authentication flow
├── Set up monitoring and logging
├── Document API usage patterns
└── Plan for Asana API changes
```

## 8.2 Common Workflows

### Task Lifecycle Management

1. **Create task** with all required fields
2. **Set custom fields** and dependencies
3. **Add subtasks** for breakdown
4. **Assign to team members**
5. **Set up due dates and reminders**
6. **Add followers** for visibility
7. **Track progress** via status updates
8. **Complete and archive**

### Project Setup

```python
# Create a complete project structure
def setup_project(client, workspace_gid, team_gid):
    # Create project
    project = client.projects.create({
        'name': 'Website Redesign',
        'workspace': workspace_gid,
        'team': team_gid,
        'default_view': 'board',
        'start_on': '2024-01-15',
        'due_date': '2024-03-31'
    })

    # Create sections
    sections = ['Backlog', 'In Progress', 'Review', 'Done']
    section_gids = {}
    for name in sections:
        section = client.sections.create({
            'name': name,
            'project': project['gid']
        })
        section_gids[name] = section['gid']

    # Create template tasks
    tasks = [
        {'name': 'Design mockups', 'section': 'Backlog', 'assignee': 'designer@co.com'},
        {'name': 'Frontend development', 'section': 'Backlog', 'depends_on': 'Design mockups'},
        {'name': 'Backend integration', 'section': 'Backlog'},
        {'name': 'QA testing', 'section': 'Backlog'},
        {'name': 'Deployment', 'section': 'Backlog'}
    ]

    for task_spec in tasks:
        task = client.tasks.create({
            'name': task_spec['name'],
            'projects': [project['gid']],
            'assignee': task_spec.get('assignee')
        })

    return project
```

### Automated Sprint Management

```python
def create_sprint(client, project_gid, sprint_name, start_date, end_date):
    # Create sprint project
    sprint_project = client.projects.create({
        'name': f'Sprint: {sprint_name}',
        'workspace': 'WORKSPACE_GID',
        'start_on': start_date,
        'due_date': end_date
    })

    # Link to parent project
    parent_project = client.projects.find_by_id(project_gid)
    # Note: Asana doesn't support subprojects directly
    # Use tags or custom fields to link

    return sprint_project

def move_tasks_to_sprint(client, task_gids, sprint_project_gid):
    # Batch move tasks to sprint
    for task_gid in task_gids:
        client.tasks.addProject(task_gid, {
            'project': sprint_project_gid,
            'insert_after': None,
            'insert_before': None
        })
```

### Daily Standup Automation

```python
def get_yesterday_completed(client, user_gid, date):
    yesterday = datetime.strptime(date, '%Y-%m-%d') - timedelta(days=1)
    yesterday_str = yesterday.strftime('%Y-%m-%d')

    tasks = client.tasks.search({
        'workspace': 'WORKSPACE_GID',
        'assignee': user_gid,
        'completed_at.after': yesterday_str,
        'completed_at.before': date,
        'opt_fields': 'name,completed_at,projects.name'
    })

    return list(tasks)

def get_blocked_tasks(client, user_gid):
    blocked = client.tasks.search({
        'workspace': 'WORKSPACE_GID',
        'assignee': user_gid,
        'completed': False,
        'subtasks': 'any'
    })

    return [
        task for task in blocked
        if any(subtask.get('completed') == False for subtask in task.get('subtasks', []))
    ]
```

## 8.3 OAuth Implementation

```python
# Flask OAuth flow example
from flask import Flask, redirect, request, session
import asana

app = Flask(__name__)
app.secret_key = 'SECRET_KEY'

CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
REDIRECT_URI = 'https://yourapp.com/oauth/callback'

@app.route('/login')
def login():
    auth_url = f'https://app.asana.com/-/oauth_authorize?' \
               f'client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}' \
               f'&response_type=code&scope=default'
    return redirect(auth_url)

@app.route('/oauth/callback')
def oauth_callback():
    code = request.args.get('code')
    token_url = 'https://app.asana.com/-/oauth_token'

    response = requests.post(token_url, data={
        'grant_type': 'authorization_code',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'code': code
    })

    token_data = response.json()
    access_token = token_data['access_token']

    # Store token and create client
    session['access_token'] = access_token
    client = asana.Client.access_token(access_token)
    me = client.users.me()

    return f"Logged in as {me['name']}"

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
```

## 8.4 Webhook Processing

```python
# Flask webhook handler
from flask import Flask, request, jsonify
import hmac
import hashlib

app = Flask(__name__)

WEBHOOK_SECRET = 'YOUR_WEBHOOK_SECRET'

@app.route('/webhook', methods=['POST'])
def handle_webhook():
    # Verify signature
    signature = request.headers.get('X-Hook-Signature', '')
    body = request.get_data(as_text=True)

    expected = hmac.new(
        WEBHOOK_SECRET.encode(),
        body.encode(),
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(signature, expected):
        return 'Invalid signature', 401

    # Process events
    events = request.json['events']
    for event in events:
        resource = event['resource']
        action = event['action']

        if resource['resource_type'] == 'task':
            handle_task_change(action, resource)
        elif resource['resource_type'] == 'story':
            handle_story_change(action, resource)

    return jsonify({'ok': True})

def handle_task_change(action, resource):
    print(f"Task {action}: {resource['gid']}")

def handle_story_change(action, resource):
    print(f"Story {action}: {resource['gid']}")

# Sync webhook with Asana
@app.route('/webhook/handshake', methods=['GET'])
def webhook_handshake():
    challenge = request.args.get('webhook', {}).get('challenge')
    return jsonify({'webhook': {'challenge': challenge}})
```

## 8.5 Rate Limit Handling

```python
import time
import requests
from ratelimit import limits, sleep_and_retry

@sleep_and_retry
@limits(calls=1500, period=60)  # Asana's rate limit
def asana_api_call(func, *args, **kwargs):
    try:
        return func(*args, **kwargs)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 429:
            retry_after = int(e.response.headers.get('Retry-After', 60))
            print(f"Rate limited. Waiting {retry_after}s")
            time.sleep(retry_after)
            return func(*args, **kwargs)
        raise

# Usage with retry logic
def create_task_with_retry(client, task_data, max_retries=3):
    for attempt in range(max_retries):
        try:
            return asana_api_call(client.tasks.create, task_data)
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                time.sleep(2 ** attempt)  # Exponential backoff
            else:
                raise
    raise Exception("Max retries exceeded")
```

## 8.6 Testing Workflow

```bash
# Test API connectivity
curl -H "Authorization: Bearer $ASANA_PAT" \
  "https://app.asana.com/api/1.0/users/me"

# Test task creation
curl -X POST -H "Authorization: Bearer $ASANA_PAT" \
  -H "Content-Type: application/json" \
  -d '{"data":{"name":"Test Task","projects":["PROJECT_GID"]}}' \
  "https://app.asana.com/api/1.0/tasks"

# Test webhook endpoint
ngrok http 5000
# Use ngrok URL for webhook target
```
