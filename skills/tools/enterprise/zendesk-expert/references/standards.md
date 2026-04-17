# Standards & Reference

## 7.1 Official Documentation

- [Zendesk Developer Docs](https://developer.zendesk.com/)
- [Zendesk REST API Reference](https://developer.zendesk.com/api-reference/)
- [Zendesk Guide / Help Center](https://www.zendesk.com/product/guidelines/)
- [Zendesk Sunshine API](https://developer.zendesk.com/documentation/sunshine/)
- [Zendesk Apps Framework (ZAF)](https://developer.zendesk.com/apps-fundamentals/)
- [Zendesk Marketplace](https://www.zendesk.com/marketplace/)
- [Zendesk API Rate Limits & Pagination](https://developer.zendesk.com/api-reference/ticketing/rest/)
- [Zendesk Support Admin Guide](https://support.zendesk.com/hc/en-us/articles/4408827472794)

## 7.2 Configuration Reference

### Roles & Access

| Role | Permissions | Assigned To |
|------|-------------|-------------|
| `Agent` | View/respond to assigned tickets | Tier 1 Support |
| `Light Agent` | View-only on tickets | Stakeholders |
| `Admin` | Full config access | Team Leads, Admins |
| `Billing Admin` | Billing & subscription | Finance |
| `Super Admin` | Account-wide + SSO | IT/Platform Admin |

### Views (Ticket Routing)

```javascript
// View Definition: "High Priority Unassigned"
{
  "name": "High Priority Unassigned",
  "conditions": {
    "all": [
      { "field": "priority", "operator": "is", "value": "high" },
      { "field": "status", "operator": "less_than", "value": "solved" }
    ],
    "any": [
      { "field": "assignee_id", "operator": "is", "value": "null" }
    ]
  },
  "sort": {
    "field": "created_at",
    "order": "desc"
  },
  "group": "Support Tier 1"
}
```

### SLA Policies

| SLA Field | Value | Notes |
|-----------|-------|-------|
| First Reply Time | 4h (Business hours) | P1: 1h, P2: 4h, P3: 8h |
| Next Reply Time | 8h (Business hours) | For P1/P2 only |
| Resolution Time | 24h (Calendar) | P1: 4h, P2: 24h, P3: 72h |
| Target | Business hours | Define in Admin → Business Hours |

### Trigger Conditions (Common)

| Field | Operator | Value |
|-------|----------|-------|
| `ticket.status` | `is` | `open` |
| `ticket.priority` | `is` | `urgent` |
| `ticket.is_public` | `is` | `true` |
| `ticket.requester.languages` | `is` | `en` |
| `ticket.tags` | `contains` | `enterprise` |
| `ticket.assignee.role` | `is` | `admin` |

## 7.3 Common Tasks

### Create Ticket via API

```bash
curl -X POST https://yoursubdomain.zendesk.com/api/v2/tickets.json \
  -H "Content-Type: application/json" \
  -u "your_email/token:your_api_token" \
  -d '{
    "ticket": {
      "subject": "Cannot login to dashboard",
      "comment": {
        "body": "Getting 403 error when accessing the main dashboard"
      },
      "priority": "high",
      "requester_id": 12345,
      "tags": ["login", "authentication"],
      "custom_fields": [
        { "id": 360001234567, "value": "enterprise" }
      ]
    }
  }'
```

### Search API

```bash
# Find tickets with specific criteria
curl "https://yoursubdomain.zendesk.com/api/v2/search.json?query=type:ticket status:open priority:high" \
  -u "your_email/token:your_api_token"

# Find user by email
curl "https://yoursubdomain.zendesk.com/api/v2/users/search.json?query=email:user@example.com" \
  -u "your_email/token:your_api_token"
```

### Bulk Update via API

```python
import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth("agent@company.com/token", "your_api_token")
headers = {"Content-Type": "application/json"}

# Find tickets to update
search_url = "https://yoursubdomain.zendesk.com/api/v2/search.json"
params = {"query": "tags:needs_review type:ticket status:open"}

response = requests.get(search_url, auth=auth, params=params)
tickets = response.json()["results"]

# Bulk update
for ticket in tickets:
    update_url = f"https://yoursubdomain.zendesk.com/api/v2/tickets/{ticket['id']}.json"
    payload = {
        "ticket": {
            "tags": ["reviewed"],
            "status": "pending"
        }
    }
    requests.put(update_url, json=payload, auth=auth, headers=headers)
```

## 7.4 Version & Platform Compatibility

| Zendesk Product | Version/Release | Notes |
|-----------------|-----------------|-------|
| Support | Enterprise Suite | Advanced features, data center locations |
| Explore | Explore Professional / Enterprise | Analytics and reporting |
| Sunshine | General Availability | Customer object platform |
| Chat (formerly Zopin) | v4.0 | Messaging and live chat |
| Sell | CRM Suite | Sales automation |
| Guide | Enterprise | Knowledge base and self-service |

| API Version | Status | Sunset Date |
|-------------|--------|-------------|
| API v1 | **Deprecated** | Ended Nov 2025 |
| API v2 | **Current** | Active |
| Sunshine API | **Current** | Active |

| Feature | Minimum Plan | Notes |
|---------|-------------|-------|
| Multiple ticket forms | Suite Team+ | For multilingual support |
| SLA policies | Suite Team+ | Per-brand SLA |
| Light Agent role | Suite Growth+ | View-only access |
| Custom roles & groups | Suite Professional+ | Fine-grained permissions |
| Audit logs (90 days) | Suite Team+ | Enterprise: 1 year |
| Data center locations | Enterprise | US/EU/AU/JP |
| Advanced AI (Intelligent Triage) | Suite Enterprise+ | Zendesk AI features |
