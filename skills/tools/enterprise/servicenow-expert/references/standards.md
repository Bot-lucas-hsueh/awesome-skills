# Standards & Reference

## 7.1 Official Documentation

- [ServiceNow Product Documentation](https://docs.servicenow.com/)
- [ServiceNow Developer Docs](https://developer.servicenow.com/)
- [Now Platform App Engine Studio](https://docs.servicenow.com/csh?product=apps_and_features&topicname=apps-and-features&language=en_US)
- [ServiceNow Community](https://www.servicenow.com/community/)
- [ServiceNow Knowledge Base](https://www.servicenow.com/content/servicenow-lifecycle/docs-kb.html)
- [Glide System Properties](https://docs.servicenow.com/csh?product=sys_properties_concepts)

## 7.2 Configuration Reference

### ACLs (Access Control Lists)

| Field | Value | Notes |
|-------|-------|-------|
| Type | `access` | Read/write/execute control |
| Operation | `read/write` | Applies to table records |
| Script | `gs.hasRole('itil')` | Role-based enforcement |
| Condition | `active=true` | Declarative ACL option |

### Flow Designer

```
Trigger Types:
├── Record            → When a record is created/updated/deleted
├── Schedule          → Cron-based Recurrence (e.g., Daily 9am)
├── Inbound Email     → Email actions on certain addresses
├── Application Event → Publish/subscribe within an app
└── Async HTTP        → Outbound REST response callback
```

### Business Rules

| Field | Value |
|-------|-------|
| Table | `incident` |
| When | `before/after/async` |
| Order | 100 (lower = earlier) |
| Filter Condition | `active=true^state=2` |

### UI Actions

```
Client-side:  g_form.setValue('state', 2); g_servicecatalog.submit('...');
Server-side:  current.state = 2; current.update();
```

### Roles & Groups

| Role | Purpose | Assigned To |
|------|---------|-------------|
| `itil` | Basic ITSM user | Incident Resolvers |
| `sn_incident.write` | Create/update incidents | Tier 1 Support |
| `admin` | Full system access | System Administrators |
| `import_admin` | Data import | Integration admins |

## 7.3 Common Tasks

### Incident Creation via Script Include

```javascript
var inc = new GlideRecord('incident');
inc.initialize();
inc.short_description = 'VPN connectivity failure';
inc.description = 'User unable to connect to corporate VPN after update';
inc.caller_id = gs.getUserID();
inc.assignment_group = 'Network Operations';
inc.category = 'network';
inc.priority = 2;
inc.urgency = 2;
inc.impact = 2;
var sysId = inc.insert();
gs.info('Created incident: ' + sysId);
```

### Approval Workflow via Flow Designer

1. Trigger: `When record is updated` on `sysApproval_approver` where `state = requested`
2. Action: `Get Related Records` → find manager from `sys_user` record
3. Action: `Create Approval` → assigned to manager
4. If approved → `Update Record` state=approved
5. If rejected → `Notify Requester` via email

### SLA Configuration

| SLA Field | Example Value |
|-----------|---------------|
| Duration | 4 hours (P2), 8 hours (P3) |
| Start Condition | `active=true^state!=7^state!=8` |
| Pause Condition | `state=3` (Awaiting User Info) |
| Restart Condition | User responds |

## 7.4 Version & Platform Compatibility

| ServiceNow Release | Code Name | End of Mainstream Support |
|--------------------|-----------|--------------------------|
| Quebec | Utah + earlier | Ended |
| Rome | Washington + earlier | Ended |
| San Diego | Tokyo + earlier | Ended |
| Tokyo | Vancouver + earlier | Ended |
| Vancouver | Washington DC | Apr 2026 |
| Washington DC | Xanadu | Apr 2027 |
| Xanadu | (next) | Pending |

| Feature | Minimum Version |
|---------|----------------|
| Flow Designer | Jakarta+ |
| App Engine Studio | Orlando+ |
| Predictive Intelligence | Madrid+ |
| Now Assist (AI) | Vancouver+ |
| Integration Hub | Istanbul+ |
| Flow Logic: Parallel Branch | Paris+ |

> **Note:** Always check [ServiceNow version matrix](https://docs.servicenow.com/) for specific feature availability by release.
