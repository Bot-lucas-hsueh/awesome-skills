# Scenario Examples

## 9.1 Sprint Planning Automation

**User:** "How do we automatically create sprint tasks from our backlog?"

**Expert:**
> **Solution:**
>
> ```python
> def sprint_planning(client, backlog_project_gid, sprint_project_gid, capacity_hours=40):
>     # Get incomplete backlog tasks
>     backlog_tasks = client.tasks.get_tasks({
>         'project': backlog_project_gid,
>         'completed': False,
>         'opt_fields': 'name,custom_fields.Estimate'
>     })
>
>     # Get team capacity
>     team_members = client.team_members.find_by_team('TEAM_GID')
>
>     # Sort by priority and estimate
>     sorted_tasks = sorted(
>         backlog_tasks,
>         key=lambda t: (
>             -t.get('custom_fields', [{}])[0].get('number_value', 0),
>             t.get('name')
>         )
>     )
>
>     # Assign tasks based on capacity
>     assigned_tasks = []
>     member_index = 0
>
>     for task in sorted_tasks:
>         estimate = task.get('custom_fields', [{}])[0].get('number_value', 1)
>
>         if estimate <= capacity_hours:
>             # Assign to team member
>             member = team_members[member_index % len(team_members)]
>             client.tasks.update(task['gid'], {
>                 'assignee': member['user']['gid']
>             })
>
>             # Move to sprint project
>             client.tasks.addProject(task['gid'], {
>                 'project': sprint_project_gid,
>                 'insert_before': None
>             })
>
>             capacity_hours -= estimate
>             assigned_tasks.append(task)
>
>             if capacity_hours <= 0:
>                 member_index += 1
>                 capacity_hours = 40
>
>     return assigned_tasks
> ```

## 9.2 Automated Status Reports

**User:** "How do we generate weekly status reports automatically?"

**Expert:**
> **Solution:**
>
> ```python
> from datetime import datetime, timedelta

> def generate_weekly_report(client, workspace_gid):
>     today = datetime.now()
>     week_ago = today - timedelta(days=7)
>
>     # Get my tasks completed this week
>     completed_tasks = client.tasks.search({
>         'workspace': workspace_gid,
>         'assignee': 'me',
>         'completed_at.after': week_ago.strftime('%Y-%m-%d'),
>         'completed': True,
>         'opt_fields': 'name,completed_at,projects.name,custom_fields.Status'
>     })
>
>     # Get in-progress tasks
>     in_progress = client.tasks.search({
>         'workspace': workspace_gid,
>         'assignee': 'me',
>         'completed': False,
>         'due_on.after': today.strftime('%Y-%m-%d'),
>         'opt_fields': 'name,due_on,custom_fields.Status'
>     })
>
>     # Generate report
>     report = f"""
> Weekly Status Report - {today.strftime('%Y-%m-%d')}
> ================================================
>
> Completed ({len(list(completed_tasks))} tasks):
> """
>     for task in list(completed_tasks)[:10]:
>         report += f"- {task['name']}\n"
>
>     report += f"""
>
> In Progress ({len(list(in_progress))} tasks):
> """
>     for task in list(in_progress)[:5]:
>         report += f"- {task['name']} (due: {task['due_on']})\n"
>
>     return report

> # Post report to a task comment
> report_task_gid = 'REPORT_TASK_GID'
> report = generate_weekly_report(client, 'WORKSPACE_GID')
> client.stories.create({
>     'task': report_task_gid,
>     'text': report,
>     'is_pinned': True
> })
> ```

## 9.3 Cross-Project Dependency Tracking

**User:** "We have dependencies across 5 projects. How do we track blockers?"

**Expert:**
> **Solution:**
>
> ```python
> def find_blocked_work(client, workspace_gid):
>     # Find all tasks that depend on incomplete tasks
>     blocked_tasks = []
>
>     # Search for tasks mentioning dependencies
>     tasks = client.tasks.search({
>         'workspace': workspace_gid,
>         'completed': False,
>         'opt_fields': 'name,notes,projects.name,dependents'
>     })
>
>     for task in tasks:
>         # Check for blocking dependencies
>         for dep in task.get('dependencies', []):
>             blocker = client.tasks.find_by_id(dep['gid'])
>             if not blocker.get('completed'):
>                 blocked_tasks.append({
>                     'blocked_task': task,
>                     'blocker': blocker,
>                     'blocker_due': blocker.get('due_on')
>                 })
>
>     # Group by blocker
>     blockers = {}
>     for item in blocked_tasks:
>         blocker_gid = item['blocker']['gid']
>         if blocker_gid not in blockers:
>             blockers[blocker_gid] = {
>                 'blocker': item['blocker'],
>                 'blocked': []
>             }
>         blockers[blocker_gid]['blocked'].append(item['blocked_task'])
>
>     return blockers

> def create_blocker_report(client, workspace_gid):
>     blockers = find_blocked_work(client, workspace_gid)
>
>     report = "# Dependency Blockers Report\n\n"
>
>     for blocker_gid, data in blockers.items():
>         blocker = data['blocker']
>         blocked = data['blocked']
>
>         report += f"## {blocker['name']}\n"
>         report += f"Due: {blocker.get('due_on', 'Not set')}\n"
>         report += f"Blocked tasks ({len(blocked)}):\n"
>
>         for task in blocked:
>             project = task['projects'][0]['name'] if task.get('projects') else 'No project'
>             report += f"- [{project}] {task['name']}\n"
>
>         report += "\n"
>
>     return report
> ```

## 9.4 Resource Allocation Tracking

**User:** "How do we track team capacity and workload distribution?"

**Expert:**
> **Solution:**
>
> ```python
> def analyze_team_workload(client, team_gid):
>     # Get all team members
>     members = client.team_members.find_by_team(team_gid)
>
>     workload = []
>     for member in members:
>         user = member['user']
>
>         # Get active tasks
>         tasks = client.tasks.search({
>             'workspace': 'WORKSPACE_GID',
>             'assignee': user['gid'],
>             'completed': False,
>             'opt_fields': 'name,due_on,custom_fields'
>         })
>
>         # Calculate estimated hours
>         total_estimate = sum(
>             t.get('custom_fields', [{}])[0].get('number_value', 0)
>             for t in tasks
>         )
>
>         # Count overdue tasks
>         overdue = [t for t in tasks if t.get('due_on') < today_str]
>
>         workload.append({
>             'member': user['name'],
>             'email': user['email'],
>             'active_tasks': len(list(tasks)),
>             'estimated_hours': total_estimate,
>             'overdue_tasks': len(overdue),
>             'tasks': list(tasks)[:5]  # Top 5
>         })
>
>     return workload

> def rebalance_work(client, team_gid):
>     workload = analyze_team_workload(client, team_gid)
>
>     # Find overloaded and underloaded members
>     avg_load = sum(m['estimated_hours'] for m in workload) / len(workload)
>
>     overloaded = [m for m in workload if m['estimated_hours'] > avg_load * 1.2]
>     underloaded = [m for m in workload if m['estimated_hours'] < avg_load * 0.8]
>
>     suggestions = []
>     for light in underloaded:
>         for heavy in overloaded:
>             if suggestions:
>                 break
>             suggestions.append({
>                 'from': heavy['member'],
>                 'to': light['member'],
>                 'reason': f"Move tasks from overloaded ({heavy['estimated_hours']}h) to underloaded ({light['estimated_hours']}h)"
>             })
>
>     return suggestions
> ```

## 9.5 Time-Off Coordination

**User:** "How do we automatically notify teams when members are out?"

**Expert:**
> **Solution:**
>
> ```python
> def check_team_availability(client, team_gid, start_date, end_date):
>     # Get team members
>     members = client.team_members.find_by_team(team_gid)
>
>     unavailable = []
>     available = []
>
>     for member in members:
>         user = member['user']
>
>         # Look for tasks due during absence
>         tasks_during_absence = client.tasks.search({
>             'workspace': 'WORKSPACE_GID',
>             'assignee': user['gid'],
>             'due_on.after': start_date,
>             'due_on.before': end_date,
>             'completed': False
>         })
>
>         tasks_list = list(tasks_during_absence)
>
>         if tasks_list:
>             unavailable.append({
>                 'user': user,
>                 'tasks': tasks_list,
>                 'needs_coverage': True
>             })
>         else:
>             available.append(user)
>
>     return {
>         'needs_coverage': unavailable,
>         'available': available
>     }

> def reassign_tasks_for_absence(client, user_gid, backup_user_gid, start_date, end_date):
>     # Get tasks due during absence
>     tasks = client.tasks.search({
>         'workspace': 'WORKSPACE_GID',
>         'assignee': user_gid,
>         'due_on.after': start_date,
>         'due_on.before': end_date,
>         'completed': False
>     })
>
>     # Batch reassign
>     reassigned = []
>     for task in tasks:
>         # Update assignee
>         client.tasks.update(task['gid'], {
>             'assignee': backup_user_gid
>         })
>
>         # Add comment
>         client.stories.create({
>             'task': task['gid'],
>             'text': f'Task reassigned due to planned absence ({start_date} - {end_date})'
>         })
>
>         reassigned.append(task['gid'])
>
>     return reassigned
> ```

## 9.6 Automated Meeting Notes

**User:** "How do we auto-generate meeting agendas from task comments?"

**Expert:**
> **Solution:**
>
> ```python
> def generate_meeting_agenda(client, project_gid, meeting_date):
>     # Find tasks with recent comments
>     tasks = client.tasks.get_tasks({
>         'project': project_gid,
>         'opt_fields': 'name,stories,custom_fields'
>     })
>
>     agenda_items = []
>
>     for task in tasks:
>         # Check for discussion items in comments
>         for story in task.get('stories', []):
>             if story.get('type') == 'comment':
>                 text = story.get('text', '')
>                 if 'discuss:' in text.lower() or 'agenda:' in text.lower():
>                     agenda_items.append({
>                         'task': task,
>                         'discussion_point': text,
>                         'commenter': story.get('created_by', {}).get('name')
>                     })
>
>     # Group by priority from custom fields
>     agenda_items.sort(
>         key=lambda x: x['task'].get('custom_fields', [{}])[0].get('name', 'Medium')
>     )
>
>     # Generate agenda
>     agenda = f"# Meeting Agenda - {meeting_date}\n\n"
>
>     for item in agenda_items:
>         agenda += f"## {item['task']['name']}\n"
>         agenda += f"{item['discussion_point']}\n"
>         agenda += f"- Raised by: {item['commenter']}\n\n"
>
>     return agenda

> def create_meeting_task(client, project_gid, agenda):
>     # Create meeting task with agenda as notes
>     meeting = client.tasks.create({
>         'name': 'Weekly Team Sync',
>         'projects': [project_gid],
>         'notes': agenda,
>         'start_on': today_str,
>         'due_on': today_str
>     })
>
>     # Pin the task
>     client.stories.create({
>         'task': meeting['gid'],
>         'text': 'Meeting agenda generated from team tasks',
>         'is_pinned': True
>     })
>
>     return meeting
> ```
