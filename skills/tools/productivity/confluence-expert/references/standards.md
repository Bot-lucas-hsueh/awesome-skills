# Standards & Reference

## 7.1 Official Documentation

- [Confluence Cloud Documentation](https://support.atlassian.com/confluence-cloud/)
- [Confluence Data Center Docs](https://confluence.atlassian.com/enterprise/)
- [REST API v2](https://developer.atlassian.com/cloud/confluence/rest/)
- [Confluence Storage Format](https://developer.atlassian.com/cloud/confluence/storage-format/)
- [Confluence Connect (Apps)](https://developer.atlassian.com/cloud/confluence/crowd/)
- [Confluence Content Types](https://confluence.atlassian.com/doc/confluence-content-models-360889165.html)
- [Space Blueprints](https://confluence.atlassian.com/doc/space-blueprints-984790486.html)
- [Page Templates](https://confluence.atlassian.com/doc/page-templates-724765066.html)
- [Confluence Automation](https://confluence.atlassian.com/doc/automations-755376261.html)
- [Macro Reference](https://confluence.atlassian.com/doc/macro-reference-134387.html)
- [Atlassian Forge](https://developer.atlassian.com/cloud/forge/)

## 7.2 Configuration Reference

### API Authentication

```python
import requests
from requests.auth import HTTPBasicAuth
import json

# Basic Auth (deprecated, use API tokens)
BASIC_AUTH = HTTPBasicAuth('email@example.com', 'API_TOKEN')

# API Token Auth
import base64
api_token = base64.b64encode(b'email@example.com:API_TOKEN').decode('ascii')
HEADERS = {
    'Authorization': f'Basic {api_token}',
    'Content-Type': 'application/json',
    'Accept': 'application/json'
}

BASE_URL = 'https://your-domain.atlassian.net/wiki/rest/api'

# OAuth 2.0 (3LO)
# Use atlassian-python-api library
from atlassian import Confluence

confluence = Confluence(
    url='https://your-domain.atlassian.net/wiki',
    username='email@example.com',
    password='API_TOKEN',
    cloud=True
)
```

### Space and Page Operations

```python
# Create a space
space = confluence.create_space(
    key='TEAM',
    name='Engineering Team',
    description='Documentation for the engineering team',
    privately_accessible=True
)

# Create a page
page = confluence.create_page(
    space='TEAM',
    title='API Documentation',
    body='''<h1>API Documentation</h1>
<p>Welcome to our API documentation.</p>
<ac:structured-macro ac:name="code" ac:schema-version="1">
  <ac:parameter ac:name="language">python</ac:parameter>
  <ac:plain-text-body>import requests</ac:plain-text-body>
</ac:structured-macro>''',
    parent_id=None,  # Root page
    type='page'
)

# Update a page
confluence.update_page(
    page_id='PAGE_ID',
    title='Updated API Documentation',
    body='<p>Updated content here.</p>'
)

# Get page with labels
page = confluence.get_page_by_title(
    space='TEAM',
    title='API Documentation',
    expand='metadata.labels'
)

# Add labels
confluence.set_page_labels(
    page_id='PAGE_ID',
    labels=['api', 'documentation', 'engineering']
)
```

### Advanced Page Operations

```python
# Add page comment
confluence.add_comment(
    page_id='PAGE_ID',
    text='Great documentation! Could you add more examples?'
)

# Attach file
confluence.attach_file(
    '/path/to/file.pdf',
    page_id='PAGE_ID',
    name='documentation.pdf',
    content_type='application/pdf'
)

# Get page children (nested)
children = confluence.get_page_children('PAGE_ID')

# Get page descendants (all levels)
descendants = confluence.get_page_descendants('PAGE_ID')

# Move page to new location
confluence.move_page(
    space_key='TEAM',
    page_id='PAGE_ID',
    target_page_id='NEW_PARENT_ID',
    position='append'  # or 'above', 'below'
)

# Copy page (including children)
confluence.copy_page(
    space_key='TEAM',
    page_id='PAGE_ID',
    target_space_key='TEAM',
    target_title='Copy of API Documentation',
    copy_attachments=True,
    copy_labels=True
)
```

### Search Operations

```python
# Basic search
results = confluence.cql(
    'siteSearch~"api documentation" AND space=TEAM AND type=page'
)

# Advanced CQL search
from datetime import datetime

search_results = confluence.cql(
    'type=page AND space=TEAM '
    'AND (title~"API" OR text~"REST") '
    'AND label=documentation '
    'AND created>=2024-01-01 '
    'ORDER BY created DESC',
    limit=50,
    expand='body.storage,metadata.labels'
)

# Search with context
for result in search_results:
    print(f"{result['title']} - {result['excerpt']}")

# Get search suggestions
suggestions = confluence.get_content_suggestions(
    query='api',
    space_key='TEAM',
    limit=10
)
```

### Storage Format Macros

```python
# Info box
INFO_BOX = '''<ac:structured-macro ac:name="info">
  <ac:rich-text-body>
    <p>This is an informational note.</p>
  </ac:rich-text-body>
</ac:structured-macro>'''

# Warning box
WARNING = '''<ac:structured-macro ac:name="warning">
  <ac:rich-text-body>
    <p>Please backup your data before proceeding.</p>
  </ac:rich-text-body>
</ac:structured-macro>'''

# Expand/collapse
EXPAND = '''<ac:structured-macro ac:name="expand">
  <ac:parameter ac:name="title">Click to expand</ac:parameter>
  <ac:rich-text-body>
    <p>Hidden content goes here.</p>
  </ac:rich-text-body>
</ac:structured-macro>'''

# Panel with custom styling
PANEL = '''<ac:structured-macro ac:name="panel">
  <ac:parameter ac:name="borderStyle">solid</ac:parameter>
  <ac:parameter ac:name="borderColor">#0066cc</ac:parameter>
  <ac:parameter ac:name="bgColor">#f0f5ff</ac:parameter>
  <ac:rich-text-body>
    <p>Styled content panel.</p>
  </ac:rich-text-body>
</ac:structured-macro>'''

# Code block with syntax highlighting
CODE_BLOCK = '''<ac:structured-macro ac:name="code">
  <ac:parameter ac:name="language">python</ac:parameter>
  <ac:parameter ac:name="linenumbers">true</ac:parameter>
  <ac:parameter ac:name="theme">Midnight</ac:parameter>
  <ac:plain-text-body>def hello():
    print("Hello, World!")</ac:plain-text-body>
</ac:structured-macro>'''

# Table of contents
TOC = '''<ac:structured-macro ac:name="toc">
  <ac:parameter ac:name="printable">true</ac:parameter>
  <ac:parameter ac:name="style">square</ac:parameter>
  <ac:parameter ac:name="maxLevel">3</ac:parameter>
  <ac:parameter ac:name="minLevel">1</ac:parameter>
  <ac:parameter ac:name="exclude">Quick Links</ac:parameter>
  <ac:parameter ac:name="include">.*</ac:parameter>
</ac:structured-macro>'''
```

## 7.3 CQL Reference

| Clause | Example | Description |
|--------|---------|-------------|
| `type` | `type=page` | Content type |
| `space` | `space=TEAM` | Space key |
| `title` | `title~"API"` | Title search |
| `text` | `text~"documentation"` | Full-text search |
| `siteSearch` | `siteSearch~"search term"` | Search all spaces |
| `label` | `label in ("api", "guide")` | Label filter |
| `created` | `created>=2024-01-01` | Creation date |
| `modified` | `modified<now-30d` | Modification date |
| `creator` | `creator=currentUser()` | Created by |
| `parent` | `parent=PAGE_ID` | Child of page |
| `ancestor` | `ancestor=PAGE_ID` | Descendant of page |

### CQL Functions

| Function | Example |
|----------|---------|
| `now()` | `modified>now-7d` |
| `currentUser()` | `creator=currentUser()` |
| `membersOf()` | `assignee IN membersOf("team-name")` |
| `CONTAINS()` | `text CONTAINS "confluence"` |

## 7.4 Permissions and Restrictions

```python
# Add page restriction
confluence.set_page_restriction(
    page_id='PAGE_ID',
    restrictions={
        'update': {
            'user': ['user1@company.com'],
            'group': []
        },
        'read': {
            'user': [],
            'group': ['engineering-team']
        }
    }
)

# Remove restrictions
confluence.remove_page_restriction(
    page_id='PAGE_ID',
    operation_type='update'
)

# Copy permissions from parent
confluence.set_inherit_permissions(
    page_id='PAGE_ID',
    inherit=True
)
```

## 7.5 Automation Rules

```json
{
  "name": "Auto-label new API docs",
  "trigger": {
    "event": "page_created",
    "conditions": [
      {
        "condition": "title_contains",
        "value": "API"
      }
    ]
  },
  "action": {
    "action": "add_label",
    "label": "api-documentation"
  },
  "run": "as_specific_user",
  "enabled": true
}
```
