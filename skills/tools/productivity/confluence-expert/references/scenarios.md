# Scenario Examples

## 9.1 Engineering Wiki with Auto-Labeling

**User:** "How do we automatically label documentation based on content?"

**Expert:**
> **Solution with Confluence Automation:**
>
> 1. Create automation rule for new pages
> 2. Add conditions to check page title/content
> 3. Apply labels based on matching criteria
>
> ```python
> def auto_label_pages(confluence, space_key):
>     # Get all unlabeled pages
>     pages = confluence.get_all_pages(
>         space=space_key,
>         expand='metadata.labels'
>     )
>
>     for page in pages:
>         labels = [l['name'] for l in page['metadata']['labels']['results']
>                   if l.get('name')]
>
>         # Determine labels based on content
>         new_labels = determine_labels(page['title'], page['body']['storage']['value'])
>
>         # Add new labels
>         for label in new_labels:
>             if label not in labels:
>                 confluence.add_label(page_id=page['id'], label=label)
>
> def determine_labels(title, body):
>     labels = []
>     content = (title + ' ' + body).lower()
>
>     # Auto-label based on keywords
>     if 'api' in content:
>         labels.append('api')
>     if 'tutorial' in content or 'guide' in content:
>         labels.append('guide')
>     if 'architecture' in content or 'design' in content:
>         labels.append('architecture')
>     if 'runbook' in content or 'incident' in content:
>         labels.append('operations')
>     if 'setup' in content or 'install' in content:
>         labels.append('onboarding')
>
>     return labels
> ```
>
> **Confluence Automation Rule (UI Configuration):**
> - **Trigger:** Page created or modified
> - **Condition:** Space equals TEAM
> - **Condition:** Title contains "API"
> - **Action:** Add label "api-documentation"

## 9.2 API Documentation Sync

**User:** "How do we sync OpenAPI specs with Confluence pages?"

**Expert:**
> **Solution:**
>
> ```python
> import yaml
> from pathlib import Path

> def sync_openapi_to_confluence(confluence, space_key, openapi_path):
>     with open(openapi_path) as f:
>         spec = yaml.safe_load(f) if openapi_path.endswith('.yaml') else json.load(f)
>
>     # Create or update API index page
>     api_index = f'''
> <h1>API Documentation - {spec.get('info', {}).get('title', 'API')}</h1>
> <p>Version: {spec.get('info', {}).get('version', '1.0')}</p>
> <p>{spec.get('info', {}).get('description', '')}</p>
>
> <h2>Endpoints</h2>
> <ac:structured-macro ac:name="toc">
>   <ac:parameter ac:name="printable">true</ac:parameter>
> </ac:structured-macro>
> '''
>
>     # Create/update API index
>     index_page = confluence.get_page_by_title(space_key, 'API Reference')
>
>     if index_page:
>         confluence.update_page(index_page['id'], body=api_index)
>         index_id = index_page['id']
>     else:
>         new_page = confluence.create_page(space_key, 'API Reference', api_index)
>         index_id = new_page['id']
>
>     # Create page for each tag
>     paths_by_tag = group_by_tag(spec.get('paths', {}))
>
>     for tag, paths in paths_by_tag.items():
>         tag_page_body = f'<h1>{tag.title()} API</h1>\n'
>
>         for path, methods in paths.items():
>             for method, details in methods.items():
>                 if method.upper() not in ['GET', 'POST', 'PUT', 'DELETE', 'PATCH']:
>                     continue
>
>                 endpoint_page = create_endpoint_page(
>                     confluence, space_key, tag, path, method, details
>                 )
>
>                 tag_page_body += f'''
> <h2>{method.upper()} {path}</h2>
> <p>{details.get('summary', '')}</p>
> <p><ac:link><ri:page ri:content-title="{endpoint_page['title']}"/></ac:link></p>
> '''
>
>         # Create/update tag page
>         tag_page = confluence.get_page_by_title(space_key, f'{tag.title()} API')
>         if tag_page:
>             confluence.update_page(tag_page['id'], body=tag_page_body)
>         else:
>             confluence.create_page(space_key, f'{tag.title()} API', tag_page_body, index_id)

> def create_endpoint_page(confluence, space_key, tag, path, method, details):
>     title = f'{method.upper()} {path} - {tag}'
>
>     params_table = ''
> if details.get('parameters'):
>     params_table = '''
> <table>
> <tr><th>Name</th><th>In</th><th>Type</th><th>Required</th><th>Description</th></tr>
> '''
>     for param in details['parameters']:
>         params_table += f'''<tr>
> <td>{param.get('name', '')}</td>
> <td>{param.get('in', '')}</td>
> <td>{param.get('schema', {}).get('type', '')}</td>
> <td>{'Yes' if param.get('required') else 'No'}</td>
> <td>{param.get('description', '')}</td>
> </tr>'''
>     params_table += '</table>'''

>     body = f'''
> <h1>{method.upper()} {path}</h1>
> <p><strong>Summary:</strong> {details.get('summary', '')}</p>
> <p><strong>Description:</strong> {details.get('description', '')}</p>
>
> <h2>Request</h2>
> {params_table}
>
> <h2>Request Body</h2>
> <ac:structured-macro ac:name="code">
>   <ac:parameter ac:name="language">json</ac:parameter>
>   <ac:plain-text-body>{json.dumps(details.get('requestBody', {}).get('content', {}).get('application/json', {}).get('schema', {}), indent=2)}</ac:plain-text-body>
> </ac:structured-macro>
>
> <h2>Responses</h2>
> '''
>
>     for code, response in details.get('responses', {}).items():
>         body += f'''
> <h3>{code}</h3>
> <p>{response.get('description', '')}</p>
> '''
>
>     return confluence.create_page(space_key, title, body)

> def group_by_tag(paths):
>     grouped = {}
>     for path, methods in paths.items():
>         for method, details in methods.items():
>             tags = details.get('tags', ['uncategorized'])
>             tag = tags[0]
>             if tag not in grouped:
>                 grouped[tag] = {}
>             grouped[tag][path] = grouped[tag].get(path, {})
>             grouped[tag][path][method] = details
>     return grouped
> ```

## 9.3 Meeting Notes Aggregation

**User:** "How do we auto-generate weekly team meeting summaries?"

**Expert:**
> **Solution:**
>
> ```python
> def generate_weekly_summary(confluence, space_key, week_start):
>     # Find all meeting notes from this week
>     from datetime import datetime, timedelta
>
>     week_end = (datetime.strptime(week_start, '%Y-%m-%d') +
>                 timedelta(days=7)).strftime('%Y-%m-%d')
>
>     meetings = confluence.cql(
>         f'space={space_key} AND '
>         f'type=page AND '
>         f'title~"Meeting Notes" AND '
>         f'created>={week_start} AND created<{week_end}',
>         expand='body.storage'
>     )
>
>     # Extract action items
>     action_items = []
>     discussions = []
>
>     for meeting in meetings:
>         body = meeting['body']['storage']['value']
>
>         # Parse meeting content (simplified)
>         if 'Action:' in body:
>             # Extract action items
>             lines = body.split('\n')
>             for i, line in enumerate(lines):
>                 if 'Action:' in line or line.strip().startswith('- [ ]'):
>                     action_items.append({
>                         'text': line.strip(),
>                         'source': meeting['title']
>                     })
>
>     # Generate summary
>     summary = f'''
> <h1>Weekly Meeting Summary</h1>
> <p><strong>Week:</strong> {week_start} to {week_end}</p>
> <p><strong>Meetings:</strong> {len(list(meetings))}</p>
>
> <h2>Action Items</h2>
> <table>
> <tr><th>Item</th><th>From Meeting</th><th>Status</th></tr>
> '''
>     for item in action_items:
>         summary += f'<tr><td>{item["text"]}</td><td>{item["source"]}</td><td>[ ]</td></tr>\n'
>
>     summary += '</table>'
>
>     return confluence.create_page(
>         space=space_key,
>         title=f'Weekly Summary - {week_start}',
>         body=summary
>     )
> ```

## 9.4 Sprint Retrospective Board

**User:** "How do we automatically compile sprint retrospectives?"

**Expert:**
> **Solution:**
>
> ```python
> def compile_retrospective(confluence, space_key, sprint_name, story_points):
>     # Create retrospective page
>     retro_body = f'''
> <h1>Sprint Retrospective - {sprint_name}</h1>
>
> <h2>What Went Well</h2>
> <ac:structured-macro ac:name="feedback">
>   <ac:parameter ac:name=" Anonymous">false</ac:parameter>
>   <ac:parameter ac:name="label">Went Well</ac:parameter>
> </ac:structured-macro>
>
> <h2>What Could Be Improved</h2>
> <ac:structured-macro ac:name="feedback">
>   <ac:parameter ac:name=" Anonymous">false</ac:parameter>
>   <ac:parameter ac:name="label">Improvements</ac:parameter>
> </ac:structured-macro>
>
> <h2>Action Items</h2>
> <table>
> <tr><th>Action</th><th>Owner</th><th>Priority</th></tr>
> </table>
> '''
>
>     retro_page = confluence.create_page(
>         space=space_key,
>         title=f'Retro: {sprint_name}',
>         body=retro_body
>     )
>
>     # Link to sprint data
>     sprint_data = f'''
> <h1>Sprint Metrics - {sprint_name}</h1>
>
> <h2>Velocity</h2>
> <p>Story points completed: {story_points.get("completed", 0)}</p>
> <p>Story points committed: {story_points.get("committed", 0)}</p>
>
> <h2>Cycle Time</h2>
> <p>Average: {story_points.get("avg_cycle_time", "N/A")} days</p>
>
> <h2>Retrospective</h2>
> <p><ac:link><ri:page ri:content-title="Retro: {sprint_name}"/></ac:link></p>
> '''
>
>     return confluence.create_page(
>         space=space_key,
>         title=f'Sprint Metrics: {sprint_name}',
>         body=sprint_data
>     )
> ```

## 9.5 Documentation Health Dashboard

**User:** "How do we track documentation coverage and staleness?"

**Expert:**
> **Solution:**
>
> ```python
> def generate_docs_health_report(confluence, space_key):
>     # Get all pages
>     pages = confluence.get_all_pages(space=space_key, expand='version,metadata')

>     health_data = []
>
>     for page in pages:
>         last_modified = page['version']['when']
>         days_since_update = (datetime.now() -
>                              datetime.strptime(last_modified, '%Y-%m-%d')).days

>         # Check for stale content
>         status = 'current'
>         if days_since_update > 90:
>             status = 'stale'
>         elif days_since_update > 30:
>             status = 'needs-review'

>         # Count children (for documentation depth)
>         children = confluence.get_page_children(page['id'])
>         child_count = len(children.get('results', []))

>         health_data.append({
>             'title': page['title'],
>             'last_updated': last_modified,
>             'days_old': days_since_update,
>             'status': status,
>             'depth': child_count,
>             'url': page['_links']['webui']
>         })

>     # Generate report
>     report = '''<h1>Documentation Health Report</h1>
> <p>Generated: {date}</p>
>
> <h2>Summary</h2>
> <ul>
> <li>Total pages: {total}</li>
> <li>Stale pages (>90 days): {stale}</li>
> <li>Needs review (>30 days): {needs_review}</li>
> </ul>
>
> <h2>Stale Pages</h2>
> <table>
> <tr><th>Page</th><th>Last Updated</th><th>Days Old</th></tr>
> '''.format(
>         date=datetime.now().strftime('%Y-%m-%d'),
>         total=len(health_data),
>         stale=len([p for p in health_data if p['status'] == 'stale']),
>         needs_review=len([p for p in health_data if p['status'] == 'needs-review'])
>     )

>     for page in sorted(health_data, key=lambda x: x['days_old'], reverse=True)[:20]:
>         if page['status'] != 'current':
>             report += f'''<tr>
> <td><ac:link><ri:page ri:content-title="{page['title']}"/></ac:link></td>
> <td>{page['last_updated']}</td>
> <td>{page['days_old']}</td>
> </tr>'''

>     report += '</table>'

>     return confluence.create_page(
>         space=space_key,
>         title='Documentation Health Report',
>         body=report
>     )
> ```

## 9.6 Content Approval Workflow

**User:** "How do we implement a content approval workflow in Confluence?"

**Expert:**
> **Solution with Restrictions:**
>
> ```python
> def setup_approval_workflow(confluence, page_id, reviewers):
>     # Set page to draft status
>     confluence.update_page(
>         page_id=page_id,
>         status='current',  # Draft status if using page drafts
>         title=confluence.get_page_by_id(page_id)['title']
>     )

>     # Add reviewers as watchers
>     for reviewer in reviewers:
>         confluence.add_page_as_watcher(page_id, reviewer)

>     # Add comment asking for review
>     confluence.add_comment(
>         page_id=page_id,
>         text=f'''Please review this documentation.
>
> Changes made:
> - [New section on API authentication]
> - [Updated examples]
> - [Added troubleshooting guide]
>
> @{reviewer} Please review and either:
> - Approve by clicking "Approve" if the changes are ready
> - Comment with feedback if changes are needed
>
> Thanks!'''
>     )

> def approve_page(confluence, page_id, approver):
>     # Remove restrictions (publish)
>     confluence.set_page_restriction(
>         page_id=page_id,
>         restrictions={}
>     )

>     # Add approval comment
>     confluence.add_comment(
>         page_id=page_id,
>         text=f'''Approved by @{approver}
>
> This documentation is now published and visible to all users.'''
>     )

>     # Add approved label
>     confluence.add_label(page_id=page_id, label='approved')
> ```
