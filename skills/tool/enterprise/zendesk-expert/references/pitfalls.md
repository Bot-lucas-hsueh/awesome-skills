# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Pitfall | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **Using email address as requester instead of user ID** | 🔴 High | Always look up or create user by email first, then use `requester_id` |
| 2 | **Exposing API token in client-side JavaScript (ZAF app)** | 🔴 High | All API calls must go through secure server-side proxy |
| 3 | **Not respecting API rate limits (700 req/min)** | 🔴 High | Implement exponential backoff; batch requests |
| 4 | **Hardcoding agent/group IDs in triggers** | 🟡 Medium | Use dynamic conditions (role-based, tag-based) |
| 5 | **Creating infinite trigger loops** | 🔴 High | Never trigger on changes caused by your own trigger |
| 6 | **Deleting users with open tickets** | 🔴 High | Close/merge tickets first; use "suspended" instead |
| 7 | **Not sanitizing user input in custom fields** | 🟡 Medium | Escape HTML in ticket comments from external sources |
| 8 | **Ignoring locale in datetime handling** | 🟡 Medium | Always use ISO 8601 timestamps; specify timezone |
| 9 | **Confusing trigger vs automation conditions** | 🟡 Medium | Triggers: event-based; Automations: time-based |
| 10 | **Overusing macros (copy-paste replies)** | 🟡 Medium | Personalize with dynamic content placeholders |

### API Token Security

```javascript
// BAD: Exposed in client-side ZAF app
const response = await fetch(
  `https://yoursubdomain.zendesk.com/api/v2/tickets.json`,
  {
    headers: {
      "Authorization": "Basic " + btoa("token:abc123SUPERSECRET")
    }
  }
);
// Token visible in browser network tab!

// GOOD: Use ZAFClient for client-side access
const client = ZAFClient.init();
const ticket = await client.get('ticket');

// GOOD: Server-side proxy for admin operations
// app/src/routes/proxy.js (Express)
app.post('/api/proxy/tickets', async (req, res) => {
  // Server-side token (never exposed to client)
  const zd = new ZendeskClient(process.env.ZD_SUBDOMAIN, process.env.ZD_TOKEN);
  const result = await zd.createTicket(req.body);
  res.json(result);
});
```

### Infinite Loop Prevention

```javascript
// BAD: Trigger A → updates ticket → Trigger B → updates ticket → Trigger A...
// Trigger A: "On public comment → add tag"
//   Action: "Add comment from agent"
// Trigger B: "On tag added → add internal note"
//   Action: "Add comment" (creates a new comment!)
// → Loop! Every comment triggers both triggers

// FIX: Use tags to break the cycle
// Trigger A: "On public comment → add tag 'agent-replied'"
//   Conditions: ticket does not have tag "agent-replied"
//   Action: Add tag "agent-replied"

// Trigger B: "On tag 'agent-replied' → add internal note"
//   Conditions: ticket has tag "agent-replied"
//   Action: Add internal note (not public comment)
//   Action: Remove tag "agent-replied"  // Break the cycle
```

## 10.2 Performance & Configuration Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Single large ZAF app doing too many API calls** | 🔴 High | Use `ZAFClient.invoke()` batching; cache data |
| 2 | **No pagination on large ticket exports** | 🔴 High | Use cursor pagination; chunk in 100s |
| 3 | **Syncing all tickets in real-time (webhook floods)** | 🟡 Medium | Use webhook filters; batch events server-side |
| 4 | **Thousands of tags (tag explosion)** | 🟡 Medium | Audit and remove unused tags quarterly; use max 50 tags/ticket |
| 5 | **Complex nested views with many conditions** | 🟡 Medium | Simplify: use tags instead of field conditions |
| 6 | **Slow macros (loading external data)** | 🟡 Medium | Pre-fetch data; cache CRM lookups |
| 7 | **Not archiving old resolved tickets** | 🟡 Medium | Enable auto-archive for tickets > 90 days solved |
| 8 | **Unbounded custom field growth** | 🟡 Medium | Review custom fields bi-annually; remove unused |
| 9 | **No monitoring on webhook delivery failures** | 🟡 Medium | Set up alerting on webhook 4xx/5xx responses |
| 10 | **Stale ZAF app dependencies (security vulnerabilities)** | 🟡 Medium | Update ZAF SDK quarterly; audit npm packages |

### ZAF Client Batching

```javascript
// BAD: Multiple sequential API calls (slow)
const client = ZAFClient.init();
const ticket = await client.get('ticket');
const user = await client.get('ticket.requester');
const org = await client.get('ticket.organization');
const fields = await client.get('ticket.customFields:162345');

// GOOD: Single batched request
const client = ZAFClient.init();
const data = await client.get([
  'ticket',
  'ticket.requester',
  'ticket.organization',
  'ticket.customFields:162345'
]);
// Single round-trip to Zendesk!

// Cache frequently accessed data
const cache = {};
async function getTicketContext(ticketId) {
  const key = `ticket-${ticketId}`;
  if (cache[key]) return cache[key];
  
  const data = await client.get(['ticket', 'ticket.requester', 'ticket.organization']);
  cache[key] = data;
  
  // Invalidate after 5 minutes
  setTimeout(() => delete cache[key], 5 * 60 * 1000);
  return data;
}
```

### Pagination Best Practices

```python
# BAD: Loading all tickets at once (crashes on large accounts)
all_tickets = []
page = requests.get(f"{BASE}/tickets.json", auth=auth)
all_tickets.extend(page.json()["tickets"])
# Memory explosion with 100k+ tickets!

# GOOD: Cursor-based pagination
def fetch_all_tickets(base_url, auth, per_page=100):
    all_tickets = []
    cursor = None
    
    while True:
        params = {"per_page": per_page}
        if cursor:
            params["cursor"] = cursor
        
        resp = requests.get(
            f"{base_url}/tickets.json",
            auth=auth,
            params=params
        )
        resp.raise_for_status()
        data = resp.json()
        all_tickets.extend(data["tickets"])
        
        # Check for next page cursor
        next_page = data.get("next_page")
        if not next_page:
            break
        
        # Extract cursor from URL
        cursor = next_page.split("cursor=")[1]
        print(f"Fetched {len(all_tickets)} tickets...")
        
        # Respect rate limits
        time.sleep(0.1)
    
    return all_tickets

# Alternative: Incremental sync (only changed since last run)
def fetch_incremental(base_url, auth, last_sync):
    params = {
        "sort_by": "updated_at",
        "updated_after": last_sync.isoformat(),
        "per_page": 100
    }
    # Returns only tickets updated since last sync
    # Much faster for daily sync jobs
```

### Webhook Filter Anti-Patterns

```javascript
// BAD: No filter on webhook → receives ALL ticket events
// Webhook receives 10,000 events/day when you only need 100

// GOOD: Filter at the source
// Trigger → Webhook with conditions:
{
  "name": "High Priority Ticket Webhook",
  "endpoint": "https://your-api.com/webhook",
  "conditions": {
    "all": [
      { "field": "ticket.priority", "operator": "is", "value": "urgent" }
    ]
  },
  "actions": []
}
// Only fires on urgent tickets → 100 events/day instead of 10,000
```

### Tag Management

```python
# Audit and clean up tags quarterly
resp = requests.get(
    f"{BASE}/tags.json",
    auth=auth,
    params={"per_page": 100}
)
tags = resp.json()["tags"]

# Find tags with < 10 ticket uses (likely stale)
for tag in tags:
    count_resp = requests.get(
        f"{BASE}/search.json",
        auth=auth,
        params={"query": f"tags:{tag['name']} type:ticket"}
    )
    count = count_resp.json()["count"]
    if count < 10:
        print(f"Stale tag: {tag['name']} (used {count} times)")
        # Flag for removal

# Remove unused tags in bulk
# Admin → Manage Tags → Remove tags with no tickets
```
