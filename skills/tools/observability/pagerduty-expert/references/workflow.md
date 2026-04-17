# Standard Workflow

## 8.1 Incident Response Workflow

```
PagerDuty Incident Lifecycle
═══════════════════════════════════════════════════════════════

[Trigger] → [Created] → [Acknowledged] → [Resolved]
     │           │            │              │
     ▼           ▼            ▼              ▼
  Alert      On-call      Engineer      Post-mortem
  fires      notified     working       scheduled
                              │
                              ▼
                         [Escalated] (if timeout)
                              │
                              ▼
                         [Auto-escalate to next level]
```

### Phase 1: Alert Triage (0-5 minutes)

1. **Assess Priority**
   - P1 (Critical): Complete service outage, data loss, security breach
   - P2 (High): Significant degradation affecting multiple users
   - P3 (Medium): Partial degradation, workaround available
   - P4 (Low): Minor issue, no immediate user impact

2. **Quick Diagnostic**
   ```bash
   # Check if related incidents exist
   pd-cli incidents list --status triggered,acknowledged \
     --service SERVICE_ID --limit 10
   
   # Verify monitoring systems
   curl -s "https://api.pagerduty.com/incidents?statuses[]=triggered" | jq '.incidents[] | {id, title, created_at}'
   ```

3. **Initial Response Actions**
   - Acknowledge if taking ownership
   - Add context note to incident
   - Page additional responders if needed

### Phase 2: Investigation (5-30 minutes)

1. **Gather Context**
   ```bash
   # Get incident timeline
   pd-cli incidents timeline INCIDENT_ID
   
   # Check related alerts
   pd-cli alerts list --incident INCIDENT_ID
   
   # View service health
   pd-cli services get SERVICE_ID --show statistics
   ```

2. **Execute Runbooks**
   ```bash
   # Trigger automated runbook
   pd-cli runbooks execute RUNBOOK_ID \
     --parameter="host=web-server-01" \
     --parameter="action=diagnose"
   ```

3. **Communicate Status**
   - Update incident with findings
   - Post to #incidents Slack channel
   - Notify stakeholders via Statuspage if customer-impacting

### Phase 3: Resolution & Post-Mortem (30-60+ minutes)

1. **Resolve Incident**
   ```bash
   pd-cli incidents update INCIDENT_ID \
     --status resolved \
     --resolution="Root cause: Database connection pool exhausted. Fixed by increasing max_connections."
   ```

2. **Schedule Post-Mortem**
   ```bash
   # Create post-mortem meeting
   pd-cli incidents schedule-postmortem INCIDENT_ID \
     --attendees="team@company.com,platform@company.com" \
     --scheduled-time="2024-01-15T14:00:00Z"
   ```

3. **Create Follow-up Items**
   - Link Jira/Linear tickets
   - Set PagerDuty task reminders
   - Update runbooks if needed

## 8.2 Integration Workflow

### Setting Up Monitoring Integration

```
Integration Setup Flow
══════════════════════

1. Create Integration in PagerDuty
   └── Copy Integration Key

2. Configure Monitoring Tool
   ├── Prometheus → Alertmanager → PagerDuty
   ├── Datadog → PagerDuty Integration
   ├── CloudWatch → SNS → PagerDuty
   └── Custom → Events API v2

3. Test Integration
   └── Send test alert

4. Configure Routing Rules
   └── Route by severity, service, team
```

### Prometheus + Alertmanager + PagerDuty

```yaml
# alertmanager.yml
global:
  resolve_timeout: 5m

route:
  group_by: ['alertname', 'cluster', 'service']
  group_wait: 30s
  group_interval: 5m
  repeat_interval: 4h
  receiver: 'pagerduty-critical'
  routes:
    - match:
        severity: critical
      receiver: 'pagerduty-critical'
      continue: true
    - match:
        severity: warning
      receiver: 'pagerduty-warning'
    - match:
        team: platform
      receiver: 'pagerduty-platform'

receivers:
  - name: 'pagerduty-critical'
    pagerduty_configs:
      - service_key: 'CRITICAL_INTEGRATION_KEY'
        severity: critical
        class: 'alert'
        component: 'prometheus'
        group: '{{ groupLabels }}'
        details:
          summary: '{{ .CommonLabels.alertname }}'
          description: '{{ .CommonAnnotations.description }}'
        urgent: true

  - name: 'pagerduty-warning'
    pagerduty_configs:
      - service_key: 'WARNING_INTEGRATION_KEY'
        severity: warning
        urgent: false
```

### ServiceNow Bidirectional Sync

```yaml
# PagerDuty → ServiceNow Integration
# 1. Install PagerDuty Integration in ServiceNow
# 2. Configure in PagerDuty:
resource "pagerduty_extension" "servicenow" {
  name = "ServiceNow Incident Sync"
  extending_service = pagerduty_service.production.id
  extension_schema = pagerduty_extension_schema.servicenow.id
  
  config = jsonencode({
    "integration_url" = "https://company.servicenow.com/api/pagerduty/incidents",
    "sync_options" = {
      "create_incident" = true
      "update_status" = true
      "sync_assignee" = true
      "sync_priority" = true
    }
  })
}
```

## 8.3 On-Call & Observability Workflow

### Weekly On-Call Handoff Process

```
Monday 10:00 AM - Weekly Handoff
═════════════════════════════════

1. Outgoing On-Call Review
   ├── Open incidents from past week
   ├── Pending action items
   └── Active escalations

2. Schedule Verification
   └── Confirm next 2 weeks coverage

3. Handoff Documentation
   ├── Post to #oncall-handoff Slack
   └── Include:
       - Current known issues
       - Watch items
       - Recent changes
       - Contact info
```

### Schedule Management

```bash
# Create override for vacation
pd-cli overrides create \
  --schedule SCHEDULE_ID \
  --user USER_ID \
  --start "2024-01-20T00:00:00Z" \
  --end "2024-01-27T00:00:00Z"

# List upcoming on-calls
pd-cli schedules oncalls SCHEDULE_ID --until 2024-02-01

# Swap on-call with teammate
pd-cli overrides swap \
  --schedule SCHEDULE_ID \
  --user-a USER_A_ID \
  --user-b USER_B_ID \
  --start "2024-01-22T09:00:00Z" \
  --end "2024-01-22T17:00:00Z"
```

### Analytics & Reporting

```bash
# Get incident metrics for week
curl "https://api.pagerduty.com/reports/incidents" \
  -H 'Authorization: Token token=API_KEY' \
  -G --data-urlencode "date_range=week" \
  --data-urlencode "timezone=America/Los_Angeles"

# Export to CSV for SLA reporting
pd-cli reports export \
  --type incidents \
  --start 2024-01-01 \
  --end 2024-01-31 \
  --format csv \
  --output weekly-sla-report.csv
```

### SLA Monitoring

```yaml
# Configure SLA policies
resource "pagerduty_service_level_objective" "response_time" {
  name        = "Critical Response SLA"
  description = "P1 incidents must be acknowledged within 15 minutes"
  service     = pagerduty_service.production.id
  
  target {
    value        = 15  # minutes
    threshold    = 0.95  # 95% compliance
    time_window  = "rolling_window"
    time_window_config {
      rolling_window_type = "weeks"
      count = 1
    }
  }
  
  metric {
    type        = "mean_time_to_acknowledge"
    from        = "created_at"
    to          = "acknowledged_at"
    groups      = [pagerduty_team.platform.id]
  }
}
```
