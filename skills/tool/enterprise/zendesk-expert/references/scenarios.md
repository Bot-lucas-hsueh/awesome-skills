# Scenario Examples

## 9.1 IT Service Management Scenarios

### Scenario: Multi-Brand Support Routing

> **User:** "We have 3 product brands with different support teams. How do we route tickets automatically?"

**Expert:**
> **Multi-Brand Routing:**
>
> 1. **Set up 3 brands** in Admin → Brands
>    ```
>    Brand A: brand-a.com → support-brand-a@company.com
>    Brand B: brand-b.com → support-brand-b@company.com
>    Brand C: brand-c.com → support-brand-c@company.com
>    ```
>
> 2. **Configure email routing** (via forwarding rules):
>    ```
>    forward: support@brand-a.com → brand_a_tickets@company.zendesk.com
>    ```
>
> 3. **Trigger for brand assignment:**
>    ```javascript
>    // Trigger: "Auto-assign brand from requester domain"
>    {
>      "title": "Route to Brand A",
>      "active": true,
>      "conditions": {
>        "all": [
>          { "field": "requester.email", "operator": "contains", "value": "@brand-a.com" }
>        ]
>      },
>      "actions": [
>        { "field": "brand_id", "value": "123456" },
>        { "field": "group_id", "value": "111111" },
>        { "field": "tags", "value": "brand-a" }
>      ]
>    }
>    ```
>
> 4. **Custom fields** per brand:
>    ```
>    Ticket Form: Brand A Support (fields: Product, License Key)
>    Ticket Form: Brand B Support (fields: Store ID, Platform)
>    Ticket Form: Brand C Support (fields: Account ID, Region)
>    ```

### Scenario: ServiceNow ↔ Zendesk Integration

> **User:** "We use ServiceNow for IT operations and Zendesk for end-user support. How do we sync incidents?"

**Expert:**
> **ServiceNow ↔ Zendesk Integration:**
>
> ```
> Zendesk (End-User Support)
>         │
>         ├─ User reports issue → Ticket created in Zendesk
>         │
>         ├─ Trigger: If category = "IT Infrastructure" → Create ServiceNow Incident
>         │
>         └─ Webhook → ServiceNow REST API:
>              POST /api/now/table/incident
>              {
>                "short_description": "{{ticket.subject}}",
>                "description": "{{ticket.description}}",
>                "urgency": "2",
>                "caller_id": "{{ticket.requester.email}}"
>              }
>
> ServiceNow (IT Operations)
>         │
>         ├─ Incident created, assigned to IT ops team
>         ├─ Resolved in ServiceNow
>         │
>         └─ Webhook back to Zendesk:
>              PUT /api/v2/tickets/{{zendesk_ticket_id}}.json
>              {
>                "ticket": {
>                  "status": "solved",
>                  "comment": {
>                    "body": "Resolved by IT Ops. Incident INC0012345"
>                  }
>                }
>              }
> ```
>
> **Security Consideration:**
> ```
> Zendesk → ServiceNow: Use OAuth 2.0 (client credentials grant)
> ServiceNow → Zendesk: Use API token + Basic Auth
> Whitelist IPs on both sides
> Log all cross-system updates
> ```

## 9.2 HR/Finance Workflows

### Scenario: Employee Helpdesk Ticketing

> **User:** "We're using Zendesk for our internal IT helpdesk. How do we handle HR requests separately?"

**Expert:**
> **Internal IT + HR Ticketing:**
>
> ```
> Employee submits request
>         │
>         ├─ Type: IT Issue
>         │   → Route to IT Support group
>         │   → SLA: P1 = 1h, P2 = 4h, P3 = 8h
>         │
>         ├─ Type: HR Request
>         │   → Route to HR Service group
>         │   → Category dropdown: Benefits, Payroll, Policy, Leave
>         │   → SLA: General = 48h, Urgent = 8h
>         │
>         └─ Type: Facilities
>              → Route to Facilities group
>              → Category: Office, Equipment, Safety
>
> Ticket Form: "Internal IT Helpdesk"
>   ├── Category (dropdown): Hardware, Software, Access, Network
>   ├── Urgency (dropdown): Critical, Normal, Low
>   ├── Asset Tag (text): Optional
>   └── Business Justification (textarea): Required for Access requests
>
> Auto-assign rules:
>   Category = "Active Directory Access" → IT Security team
>   Category = "Laptop Request" → IT Procurement
>   Category = "Payroll Question" → HR Shared Services
> ```

### Scenario: Expense Reimbursement Tracking

> **User:** "How do we route expense reimbursement requests from Zendesk to our finance system?"

**Expert:**
> **Expense Reimbursement Flow:**
>
> 1. **User submits expense ticket:**
>    ```
>    Subject: "Reimbursement request - Client dinner"
>    Category: Finance
>    Subcategory: Expense Report
>    Attachments: receipts.pdf (required)
>    Amount: $127.50
>    ```
>
> 2. **Trigger: Route to Finance queue:**
>    ```javascript
>    // Trigger: "Route expense requests"
>    {
>      "conditions": {
>        "all": [
>          { "field": "ticket:custom_field_123456", "operator": "is", "value": "expense" },
>          { "field": "ticket:status", "operator": "is", "value": "new" }
>        ]
>      },
>      "actions": [
>        { "field": "group_id", "value": "finance_support_group" },
>        { "field": "sla_policy_id", "value": "finance_sla" },
>        { "field": "tags", "value": "expense-pending" }
>      ]
>    }
>    ```
>
> 3. **Finance agent reviews:**
>    - Verifies receipts attached
>    - Checks policy compliance (meal limit $100/person)
>    - If approved → forward to Concur/Expensify API
>    - Mark ticket "Solved" with reference number
>
> 4. **Webhook on solve:** POST to Concur API
>    ```json
>    {
>      "expense_report": {
>        "employee_id": "{{ticket.requester.external_id}}",
>        "amount": "{{ticket.custom_field_amount}}",
>        "category": "meals",
>        "submitted_date": "{{ticket.created_at}}"
>      }
>    }
>    ```

## 9.3 Support Ticketing Workflows

### Scenario: Intelligent Triage with Zendesk AI

> **User:** "We get 1000 tickets a day. How do we auto-categorize and route them?"

**Expert:**
> **AI-Powered Triage:**
>
> 1. **Enable Intelligent Triage** (Zendesk AI, Enterprise+):
>    ```
>    Admin → AI → Intelligent Triage
>    → Select: Category, Group, Priority prediction
>    → Minimum confidence: 70%
>    ```
>
> 2. **Train the model:**
>    ```
>    → Use last 6 months of historical tickets
>    → Each category: 100+ labeled examples minimum
>    → Review predictions weekly for the first month
>    ```
>
> 3. **Automation based on AI predictions:**
>    ```
>    Trigger: "AI Category Prediction"
>    Conditions:
>      - AI Confidence ≥ 70% → Auto-assign
>      - AI Confidence < 70% → Flag for human review (add tag: "needs-review")
>    ```
>
> 4. **Fallback rules for edge cases:**
>    ```
>    if subject contains "refund" → Category: Billing
>    if subject contains "bug" OR "broken" → Priority: High
>    if requester.plan = "Enterprise" → Priority: High, Group: Enterprise Support
>    if requester.csat < 3.0 (last 3 tickets) → Priority: High
>    ```

### Scenario: CSAT Follow-Up Automation

> **User:** "We want to send a survey only when tickets are solved and wait 24h before following up."

**Expert:**
> **CSAT Automation:**
>
> ```
> Ticket Solved
>         │
>         ├─ Trigger: Ticket status → "Solved"
>         │   Action: Schedule webhook after 24 hours
>         │   → Send CSAT survey via email
>         │
>         └─ 24 hours later:
>              Survey email sent
>              Requester responds (Good/Bad)
>
>              ├─ Good (CSAT ≥ 4):
>              │   → No action needed
>              │
>              └─ Bad (CSAT ≤ 3) OR No response:
>                   Trigger: "CSAT Follow-Up"
>                   Action 1: Add tag "csat-followup"
>                   Action 2: Assign to original agent
>                   Action 3: Send second survey via macro
>
>                   If still no response after 48h:
>                       → Escalate to team lead
>                       → Create internal note with context
> ```
>
> **Trigger Configuration:**
> ```javascript
> // Trigger: "Schedule CSAT follow-up"
> {
>   "title": "Schedule CSAT follow-up",
>   "active": true,
>   "conditions": {
>     "all": [
>       { "field": "ticket:status", "operator": "is", "value": "solved" }
>     ]
>   },
>   "actions": [
>     { "field": "notification_survey", "value": "send_after_24h" }
>   ]
> }
>
> // Trigger: "CSAT low score escalation"
> {
>   "title": "CSAT low score escalation",
>   "active": true,
>   "conditions": {
>     "all": [
>       { "field": "ticket:satisfaction", "operator": "is_not", "value": "good" },
>       { "field": "ticket:status", "operator": "is", "value": "solved" }
>     ]
>   },
>   "actions": [
>     { "field": "group_id", "value": "team_lead_group" },
>     { "field": "tags", "value": "csat-escalated" },
>     { "field": "subject", "value": "[CSAT Follow-up Needed] {{ticket.subject}}" }
>   ]
> }
> ```

### Scenario: Merge Duplicate Tickets

> **User:** "We often get the same issue reported by multiple customers. How do we handle this efficiently?"

**Expert:**
> **Duplicate Detection & Merge Workflow:**
>
> 1. **Identify duplicates via Trigger:**
>    ```
>    Trigger: "Flag potential duplicates"
>    Condition: Subject similarity > 80% + same product tag
>    Action: Add tag "potential-duplicate"
>    ```
>
> 2. **Agent workflow:**
>    ```
>    Agent sees ticket tagged "potential-duplicate"
>         │
>         ├─ Searches knowledge base for similar resolved tickets
>         │   Search: "{{ticket.subject}}" in Guide
>         │
>         ├─ If match found:
>         │   Reply with solution article link
>         │   If user confirms solved → close as "Solved"
>         │
>         └─ If genuinely duplicate:
>              Merge into master ticket:
>              /api/v2/tickets/{master_id}/merge
>              {
>                "source_ticket_id": "{{ticket.id}}",
>                "target_ticket_id": "{master_ticket_id}"
>              }
>              → All comments from source merged into master
>              → Source ticket marked "Merged: {master_id}"
>              → Requester notified of master ticket link
>    ```
>
> 3. **Mass merge via API (outage scenarios):**
>    ```python
>    # Find tickets created during outage window with similar patterns
>    params = {
>        "query": "tags:outage type:ticket status:open created>[2026-03-19T00:00:00Z]"
>    }
>    tickets = zd.request("GET", "/search.json", params=params).json()["results"]
>    
>    # Keep first as master, merge rest
>    master = tickets[0]["id"]
>    for t in tickets[1:]:
>        requests.post(
>            f"{zd.base_url}/tickets/{master}/merge.json",
>            json={"source_ticket_id": t["id"]},
>            auth=zd.auth
>        )
>        print(f"Merged ticket {t['id']} into {master}")
>    ```
