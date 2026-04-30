# Standard Workflow

## 8.1 Admin Workflow

### Initial Setup

```
1. Account Configuration
   ├── Configure brand (logo, colors, URL, support email)
   ├── Set up multiple brands (Enterprise)
   ├── Configure authentication (SSO via SAML/OIDC)
   └── Set up API token access

2. User & Organization Setup
   ├── Import users via CSV or API
   ├── Set up organizations (companies)
   ├── Configure organization fields
   ├── Map user fields from CRM (Salesforce, HubSpot)
   └── Set up user segments

3. Ticket & Channel Configuration
   ├── Configure email channels (forward to support@)
   ├── Set up web widget (Classic ormess Web Widget)
   ├── Configure Facebook/Twitter/WhatsApp integrations
   ├── Set up Talk (phone) and Guide (knowledge base)
   └── Configure SLA policies per brand

4. Workflow Automation
   ├── Build triggers (event-driven)
   ├── Build automations (time-based)
   ├── Build macros (response templates)
   ├── Configure dynamic content (i18n)
   └── Set up SLAs and escalations
```

### ZAF App Development Workflow

```
1. Scaffold app
   zcli apps:create my-app
   cd my-app

2. Configure manifest.json
   {
     "name": "Ticket Context Panel",
     "author": { "name": "Your Team" },
     "location": { "support": { "ticket_sidebar": null } }
   }

3. Develop
   ├── Write frontend (vanilla JS, React, or Handlebars)
   ├── Access ticket data via ZAFClient
   │   const client = ZAFClient.init();
   │   const ticket = await client.get('ticket');
   │
   └── Use secure server-side for API keys

4. Test locally
   zcli apps:server
   → Enable "development mode" in Zendesk

5. Package & upload
   zcli apps:package
   zcli apps:publish
```

## 8.2 User Workflow

### End-User Support Flow

```
Customer submits request
         │
         ├─ Via email: forward@company.zendesk.com
         │   → Ticket created, auto-assigned via routing rules
         │
         ├─ Via web widget: Embedded form on website
         │   → Ticket created, pre-filled with user context
         │
         ├─ Via Chat: Real-time agent conversation
         │   → Chat escalated to ticket on request
         │
         └─ Via Talk: Phone call
              → Call ticket created, auto-IVR routing

Agent receives ticket in queue
         │
         ├─ View: Inbox / My tickets / Team view
         │
         ├─ Actions:
         │   ├── Reply via email/chat
         │   ├── Add internal note
         │   ├── Change status (Open → Pending → Solved)
         │   ├── Assign to colleague
         │   ├── Merge duplicate tickets
         │   └── Apply macro
         │
         └─ Resolution:
              Ticket solved → auto-survey (CSAT)
              → Customer satisfaction rating
              → Feedback collected
```

### Manager Escalation Flow

```
Ticket SLA breach warning (75% of SLA elapsed)
         │
         ├─ Trigger: SLA warning notification
         │   Email to assignee + manager
         │   Add note: "SLA breach warning"
         │
         ├─ SLA breach at 100%
         │   Ticket priority escalated automatically
         │   Trigger: Escalate to supervisor
         │   Email to team lead
         │
         └─ Manager review:
              If > 3 tickets overdue → team queue audit
              If systemic issue → escalate to Product/BE team
              Create linked Problem ticket (Zendesk Explore)
```

## 8.3 Integration Workflow

### REST API — OAuth 2.0

```python
import requests
from datetime import datetime, timedelta

class ZendeskClient:
    def __init__(self, subdomain, client_id, client_secret, email):
        self.subdomain = subdomain
        self.client_id = client_id
        self.client_secret = client_secret
        self.email = email
        self.base_url = f"https://{subdomain}.zendesk.com/api/v2"
        self._token = None
        self._token_expires = 0
    
    def get_token(self):
        if datetime.now().timestamp() < self._token_expires - 60:
            return self._token
        
        url = f"https://{self.subdomain}.zendesk.com/oauth/tokens"
        payload = {
            "grant_type": "client_credentials",
            "client_id": self.client_id,
            "client_secret": self.client_secret
        }
        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        data = resp.json()
        self._token = data["access_token"]
        self._token_expires = datetime.now().timestamp() + data["expires_in"]
        return self._token
    
    def request(self, method, path, **kwargs):
        token = self.get_token()
        headers = kwargs.pop("headers", {})
        headers["Authorization"] = f"Bearer {token}"
        headers["Content-Type"] = "application/json"
        resp = requests.request(
            method,
            f"{self.base_url}{path}",
            headers=headers,
            **kwargs
        )
        resp.raise_for_status()
        return resp

# Usage
zd = ZendeskClient("yoursubdomain", "client_id", "client_secret", "admin@company.com")
tickets = zd.request("GET", "/tickets.json?per_page=25").json()["tickets"]
```

### Webhook Integration (Zendesk Events → External)

```json
// Trigger → Webhook: "On ticket update, notify Slack"
{
  "webhook": {
    "name": "Notify Slack on High Priority Tickets",
    "status": "active",
    "endpoint": "https://hooks.slack.com/services/XXX/YYY/ZZZ",
    "http_method": "POST",
    "request_format": "json",
    "authentication": {
      "type": "api_key",
      "name": "X-Webhook-Token",
      "value": "your-webhook-secret"
    }
  }
}

// Payload sent to Slack:
{
  "ticket": {
    "id": 12345,
    "subject": "Critical: Payment gateway down",
    "status": "open",
    "priority": "urgent",
    "requester": {
      "name": "Jane Smith",
      "email": "jane@company.com"
    },
    "created_at": "2026-03-19T10:30:00Z"
  }
}
```

### Sunshine Events (Profile & Object Sync)

```javascript
// Send user event to Sunshine
// POST https://yoursubdomain.zendesk.com/api/v2/sunshine/events

const event = {
  type: "user.event",
  source: "your-app",
  instance_id: "user-12345",
  properties: {
    event_type: "plan_upgraded",
    plan: "enterprise",
    previous_plan: "growth",
    mrr_change: 500
  }
};

// Create/Update custom object (e.g., Contract)
const contract = {
  data: {
    type: "contract",
    id: "contract-001",
    attributes: {
      account_name: "Acme Corp",
      mrr: 5000,
      seats: 100,
      renewal_date: "2027-03-19",
      csm_name: "John Doe"
    }
  }
};

// POST /api/v2/sunshine/objects/contracts
```

### Salesforce → Zendesk Integration

```
1. Install "Zendesk for Salesforce" from Marketplace
2. Configure in Zendesk Admin → Integrations → Salesforce
3. Set sync direction:
   ├── Salesforce → Zendesk: Accounts, Contacts, Cases
   └── Zendesk → Salesforce: Tickets, Satisfaction Ratings

4. Field mapping:
   Salesforce Account.Industry → Zendesk Organization custom field
   Salesforce Contact.Email → Zendesk User.email
   Salesforce Case.Priority → Zendesk Ticket.priority

5. Trigger: "New Salesforce Case" → Create Zendesk Ticket
   Trigger: "Zendesk Ticket Solved" → Update Salesforce Case status
```

### ZAPIAlerts / Data Export via SFTP

```
1. Configure data export in Admin → Settings → Data & Privacy
2. Set up nightly incremental export:
   ├── Tickets (full + incremental)
   ├── Users
   ├── Organizations
   ├── Comments
   └── Satisfaction ratings
3. Export delivered to SFTP: /zendesk/exports/
4. Schedule: Nightly at 2:00 AM UTC
5. Retention: 30 days on SFTP, archive to S3 after
```
