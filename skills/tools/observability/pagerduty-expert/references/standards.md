# Standards & Reference

## 7.1 Official Documentation

- [PagerDuty Platform Documentation](https://developer.pagerduty.com/docs)
- [REST API Reference](https://developer.pagerduty.com/api-reference)
- [Events API v2](https://v2.developer.pagerduty.com/docs/events-api-v2)
- [ServiceNow Integration Guide](https://www.pagerduty.com/integrations/servicenow/)
- [PagerDuty Terraform Provider](https://registry.terraform.io/providers/PagerDuty/pagerduty/latest/docs)
- [PagerDuty Runbook Automation](https://www.pagerduty.com/features/runbook-automation/)

## 7.2 Configuration Reference

### Service Configuration

```yaml
# Minimal PagerDuty Service (Terraform)
resource "pagerduty_service" "production" {
  name                    = "production-api"
  description             = "Production API Service"
  auto_resolve_timeout    = 14400  # 4 hours
  acknowledgement_timeout = 1800   # 30 minutes
  
  incident_priority_urgency = "high"
  
  escalation_policy = pagerduty_escalation_policy.main.id
}

resource "pagerduty_service_dependency" "api-backend" {
  dependent_service = pagerduty_service.backend.id
  supporting_service = pagerduty_service.production.id
}
```

### Escalation Policy

```yaml
# Escalation Policy with 3 levels
resource "pagerduty_escalation_policy" "main" {
  name        = "Production Escalation Policy"
  description = "Escalates to on-call, then team lead, then manager"
  
  rule {
    assignment {
      type    = "schedule"
      id      = pagerduty_schedule.on_call.id
    }
    delay = 0  # minutes
  }
  
  rule {
    assignment {
      type    = "user"
      id      = pagerduty_user.team_lead.id
    }
    delay = 30
  }
  
  rule {
    assignment {
      type    = "user"
      id      = pagerduty_user.manager.id
    }
    delay = 60
  }
}
```

### Event Rules (Intelligent Alert Grouping)

```yaml
# Route incidents based on severity and source
resource "pagerduty_event_orchestration" "service" {
  service = pagerduty_service.production.id
  
  set {
    id = "critical"
    actions {
      priority = pagerduty_priority.critical.id
      annotate = "Critical incident routed to P1 queue"
    }
    condition {
      expression = "event.severity == 'critical' or event.custom_details.priority == 'P1'"
    }
  }
  
  set {
    id = "warning"
    actions {
      priority = pagerduty_priority.high.id
    }
    condition {
      expression = "event.severity == 'warning'"
    }
  }
}
```

### Team Structure

```yaml
resource "pagerduty_team" "platform" {
  name        = "Platform Engineering"
  description = "Core platform services team"
}

resource "pagerduty_team_membership" "lead" {
  team_id = pagerduty_team.platform.id
  user_id = pagerduty_user.team_lead.id
  role    = "manager"
}
```

## 7.3 Common Commands & API Operations

### PagerDuty REST API v2

```bash
# Create an incident via Events API
curl -X POST https://events.pagerduty.com/v2/enqueue \
  -H 'Content-Type: application/json' \
  -d '{
    "routing_key": "YOUR_INTEGRATION_KEY",
    "event_action": "trigger",
    "payload": {
      "summary": "High CPU usage on web-server-01",
      "source": "prometheus",
      "severity": "warning",
      "component": "cpu",
      "group": "host",
      "class": "high_cpu",
      "custom_details": {
        "hostname": "web-server-01",
        "cpu_usage": "92%",
        "threshold": "80%"
      }
    }
  }'

# Acknowledge an incident
curl -X PUT https://api.pagerduty.com/incidents/INCIDENT_ID \
  -H 'Authorization: Token token=YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"incident": {"type": "incident_reference", "status": "acknowledged"}}'

# Snooze an incident for 1 hour
curl -X POST https://api.pagerduty.com/incidents/INCIDENT_ID/snooze \
  -H 'Authorization: Token token=YOUR_API_TOKEN' \
  -H 'Content-Type: application/json' \
  -d '{"duration": 3600}'

# Get on-call schedule
curl -https://api.pagerduty.com/oncalls \
  -H 'Authorization: Token token=YOUR_API_TOKEN' \
  -G --data-urlencode "time_zone=America/Los_Angeles" \
  --data-urlencode "include[]=users" \
  --data-urlencode "include[]=schedules"
```

### PagerDuty CLI (pd-cli)

```bash
# Install pd-cli
npm install -g pd-cli

# Configure authentication
pd-cli configure --api-key YOUR_API_KEY

# List services
pd-cli services list

# Get incident details
pd-cli incidents get INCIDENT_ID

# Update incident priority
pd-cli incidents update INCIDENT_ID --priority P1

# Take ownership of incident
pd-cli incidents update INCIDENT_ID --assignee YOUR_USER_ID
```

## 7.4 Version Compatibility

| Component | Version | Status | Notes |
|-----------|---------|--------|-------|
| Events API v2 | 2.1 | Current | Required for new integrations |
| REST API | 2024-01-01 | Current | Latest stable release |
| Terraform Provider | 3.x | Recommended | Supports all API features |
| PagerDuty Runbook | 4.x | Current | Enhanced automation |
| Statuspage Integration | 2.x | Current | Bi-directional sync |

### Feature Support Matrix

| Feature | Starter | Standard | Professional | Enterprise |
|---------|---------|----------|--------------|------------|
| Services | 5 | 25 | Unlimited | Unlimited |
| Users | 5 | 50 | Unlimited | Unlimited |
| Event Orchestration | No | Yes | Yes | Yes |
| Analytics API | No | No | Yes | Yes |
| SLA Policies | No | Basic | Advanced | Advanced |
| Service Dependency | No | No | Yes | Yes |
