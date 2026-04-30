# Standard Workflow

## 8.1 Getting Started

```
Phase 1: Environment Setup
├── Create Atlassian account
├── Generate API token
├── Install confluence-client library
├── Set up authentication
└── Verify API access

Phase 2: Space Organization
├── Identify required spaces
├── Design space structure
├── Create space blueprints
├── Set up space permissions
└── Configure space settings

Phase 3: Content Architecture
├── Define content types (docs, how-tos, policies)
├── Create page templates
├── Establish naming conventions
├── Set up label taxonomy
└── Build navigation structure

Phase 4: Content Migration
├── Export existing content
├── Transform to Confluence format
├── Map to new space structure
├── Import with relationships preserved
└── Verify and link content
```

## 8.2 Common Workflows

### Documentation Site Setup

```python
def setup_documentation_space(confluence, space_key, team_name):
    # Create space
    space = confluence.create_space(
        key=space_key,
        name=f'{team_name} Documentation',
        description=f'Central documentation for {team_name}',
        private=True
    )

    # Create root pages
    root_pages = {
        'Home': 'Welcome to {team_name} documentation',
        'Getting Started': 'Onboarding guide and prerequisites',
        'API Reference': 'API documentation and examples',
        'Guides': 'Step-by-step how-to guides',
        'Architecture': 'System design and architecture docs',
        'Runbooks': 'Operational runbooks and procedures'
    }

    page_ids = {}
    for title, description in root_pages.items():
        page = confluence.create_page(
            space=space_key,
            title=title,
            body=f'<p>{description}</p>',
            type='page'
        )
        page_ids[title] = page['id']

    # Create page templates
    templates = {
        'API Endpoint': '''<h1>API Endpoint</h1>
<p><strong>Endpoint:</strong> [Paste endpoint URL]</p>
<p><strong>Method:</strong> GET/POST/PUT/DELETE</p>
<h2>Description</h2>
<p>[Describe what this endpoint does]</p>
<h2>Parameters</h2>
<p>[List parameters]</p>
<h2>Response</h2>
<p>[Document response format]</p>''',

        'Runbook': '''<h1>Runbook: [Title]</h1>
<p><strong>Severity:</strong> [P1/P2/P3/P4]</p>
<p><strong>Last Updated:</strong> {date}</p>
<h2>Overview</h2>
<p>[Brief description of this runbook]</p>
<h2>Prerequisites</h2>
<ul>
<li>[ ] Access to production environment</li>
<li>[ ] Notify team of maintenance</li>
</ul>
<h2>Procedure</h2>
<ol>
<li>[Step 1]</li>
<li>[Step 2]</li>
</ol>
<h2>Rollback</h2>
<p>[How to rollback if something goes wrong]</p>'''
    }

    for name, template in templates.items():
        confluence.create_page(
            space=space_key,
            title=f'Template: {name}',
            body=template.format(date=datetime.now().strftime('%Y-%m-%d')),
            parent_id=page_ids['Home']
        )

    return page_ids
```

### Automated Documentation Updates

```python
def update_api_documentation(confluence, space_key, api_data):
    # Check if page exists
    existing = confluence.get_page_by_title(space_key, api_data['title'])

    if existing:
        # Update existing page
        confluence.update_page(
            page_id=existing['id'],
            title=api_data['title'],
            body=api_data['content']
        )
        page_id = existing['id']
    else:
        # Create new page
        page = confluence.create_page(
            space=space_key,
            title=api_data['title'],
            body=api_data['content'],
            parent_id=get_api_index_page()
        )
        page_id = page['id']

    # Update API index
    update_api_index(confluence, space_key, api_data, page_id)

    return page_id

def generate_release_notes(confluence, space_key, version, changes):
    body = f'''
<h1>Release Notes - Version {version}</h1>
<p><strong>Release Date:</strong> {datetime.now().strftime('%Y-%m-%d')}</p>

<h2>New Features</h2>
'''
    for feature in changes.get('new', []):
        body += f'<li>{feature}</li>'

    body += '''
<h2>Bug Fixes</h2>
'''
    for fix in changes.get('fixed', []):
        body += f'<li>{fix}</li>'

    body += '''
<h2>Breaking Changes</h2>
'''
    for breaking in changes.get('breaking', []):
        body += f'<li>{breaking}</li>'

    return confluence.create_page(
        space=space_key,
        title=f'Release Notes - {version}',
        body=body,
        parent_id=get_releases_page()
    )
```

### Content Migration

```python
def migrate_content(confluence, source_data, space_key, parent_page_id=None):
    migrated = []

    for item in source_data:
        # Create page with migrated content
        page = confluence.create_page(
            space=space_key,
            title=item['title'],
            body=convert_to_storage_format(item['content']),
            parent_id=parent_page_id,
            type='page'
        )

        # Copy labels
        if item.get('labels'):
            confluence.set_page_labels(
                page_id=page['id'],
                labels=item['labels']
            )

        # Copy attachments
        if item.get('attachments'):
            for attachment in item['attachments']:
                confluence.attach_file(
                    attachment['path'],
                    page_id=page['id'],
                    name=attachment['name']
                )

        # Recurse for children
        if item.get('children'):
            migrate_content(
                confluence,
                item['children'],
                space_key,
                page['id']
            )

        migrated.append({'original': item['id'], 'new': page['id']})

    return migrated

def convert_to_storage_format(content):
    # Convert Markdown to Confluence storage format
    # This is a simplified example
    import re

    # Headers
    content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)

    # Code blocks
    content = re.sub(
        r'```(\w+)?\n(.*?)```',
        r'<ac:structured-macro ac:name="code"><ac:parameter ac:name="language">\1</ac:parameter><ac:plain-text-body>\2</ac:plain-text-body></ac:structured-macro>',
        content,
        flags=re.DOTALL
    )

    # Paragraphs
    content = f'<p>{content}</p>'

    return content
```

## 8.3 Space Blueprint Templates

```python
# Create a Team Space
team_space_blueprint = {
    'key': 'team',
    'name': 'Team Space',
    'description': 'For team collaboration and documentation',
    'sections': [
        {'key': 'home', 'title': 'Home'},
        {'key': 'meetings', 'title': 'Meeting Notes'},
        {'key': 'docs', 'title': 'Team Documents'}
    ]
}

# Create a Project Space
project_space_blueprint = {
    'key': 'project',
    'name': 'Project Space',
    'description': 'For project management and tracking',
    'sections': [
        {'key': 'overview', 'title': 'Project Overview'},
        {'key': 'planning', 'title': 'Planning & Backlog'},
        {'key': 'releases', 'title': 'Releases'},
        {'key': 'retrospectives', 'title': 'Retrospectives'}
    ]
}
```

## 8.4 Page Template Examples

### Architecture Decision Record (ADR)

```python
ADR_TEMPLATE = '''<h1>ADR-{number}: {title}</h1>
<table>
<tr><th><strong>Status</strong></th><td>{status}</td></tr>
<tr><th><strong>Date</strong></td><td>{date}</td></tr>
<tr><th><strong>Deciders</strong></td><td>{deciders}</td></tr>
</table>

<h2>Context</h2>
<p>{context}</p>

<h2>Decision</h2>
<p>{decision}</p>

<h2>Consequences</h2>
<h3>Positive</h3>
<ul>{positive_consequences}</ul>
<h3>Negative</h3>
<ul>{negative_consequences}</ul>

<h2>Related Documents</h2>
<ul>{related_docs}</ul>
'''
```

### Incident Post-Mortem

```python
POSTMORTEM_TEMPLATE = '''<h1>Incident Post-Mortem: {title}</h1>

<table>
<tr><th><strong>Date</strong></th><td>{date}</td></tr>
<tr><th><strong>Duration</strong></td><td>{duration}</td></tr>
<tr><th><strong>Severity</strong></td><td>{severity}</td></tr>
<tr><th><strong>Status</strong></td><td>{status}</td></tr>
</table>

<h2>Summary</h2>
<p>{summary}</p>

<h2>Impact</h2>
<ul>
<li>Users affected: {users_affected}</li>
<li>Revenue impact: {revenue_impact}</li>
</ul>

<h2>Root Cause</h2>
<p>{root_cause}</p>

<h2>Timeline</h2>
{timeline}

<h2>What Went Well</h2>
<ul>{went_well}</ul>

<h2>What Went Poorly</h2>
<ul>{went_poorly}</ul>

<h2>Action Items</h2>
<table>
<tr><th>Action</th><th>Owner</th><th>Due Date</th></tr>
{action_items}
</table>
'''
```

## 8.5 Testing Workflow

```bash
# Test API connectivity
curl -u email@example.com:TOKEN \
  "https://your-domain.atlassian.net/wiki/rest/api/space"

# Get space info
curl -u email@example.com:TOKEN \
  "https://your-domain.atlassian.net/wiki/rest/api/space/SPACE_KEY"

# Create a test page
curl -u email@example.com:TOKEN \
  -X POST \
  -H "Content-Type: application/json" \
  -d '{"type":"page","title":"Test Page","space":{"key":"SPACE_KEY"},"body":{"storage":{"value":"<p>Test</p>","representation":"storage"}}}' \
  "https://your-domain.atlassian.net/wiki/rest/api/content"

# Search content
curl -u email@example.com:TOKEN \
  "https://your-domain.atlassian.net/wiki/rest/api/content/search?cql=space=SPACE_KEY AND type=page"
```
