# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Pitfall | Severity | Quick Fix |
|---|---------|----------|-----------|
| 1 | **Global ACL blocking scoped app access** | 🔴 High | Use `current.canRead()` or scope-specific ACLs |
| 2 | **Circular business rule dependencies** | 🔴 High | Set `current.setWorkflow(false)` before update |
| 3 | **Storing secrets in system properties (plaintext)** | 🔴 High | Use Credentials Store or Encrypted Text fields |
| 4 | **Missing ACL on reference fields** | 🔴 High | Explicitly set ACLs on `x_*.u_field.reference` |
| 5 | **Update set pollution (mixing unrelated changes)** | 🔴 High | One ticket per update set; tag with change ID |
| 6 | **Client-side GlideRecord in `onSubmit`** | 🟡 Medium | Use `gs.getUser()` server-side; avoid async GlideRecord |
| 7 | **No GlideSystemGuard on `gs.sleep()` in production** | 🟡 Medium | Remove `gs.sleep()`; use scheduled jobs instead |
| 8 | **Disabling ACL logs for performance** | 🟡 Medium | Keep ACL logging ON in dev; tune query performance |
| 9 | **Scope creep in scoped apps** | 🟡 Medium | Pin app scope; use proper application cross-scope access |
| 10 | **Forgetting `current.update()` after `current.setValue()`** | 🟡 Medium | Always call `.update()` or use `.updateMultiple()` batch |

### ACL Issues — Specific Cases

```javascript
// BAD: Role check without consideringelevated privileges
(function runScript(ctrl, req) {
    if (!gs.hasRole('itil')) return false; // Blocks read for users with elevated ACL
})(acl, request);

// BETTER: Check field-level write ACL separately
(function runScript(ctrl, req) {
    if (!gs.hasRole('itil') && !gs.hasRole('admin')) return false;
    if (current.state == 7) return false; // No writes on closed records
})(acl, request);
```

### Circular Dependencies

```javascript
// BAD: Business Rule A updates incident → triggers BR B → BR B updates incident → triggers BR A
// BR A (on incident, after update):
current.u_last_updated_by = gs.getUserName();
current.update(); // ← triggers BR B!

// FIX: Guard with a skip flag
(function BR_A(current, previous) {
    if (current.u_skip_br_a) return;
    current.u_last_updated_by = gs.getUserName();
    current.u_skip_br_b = true;
    current.update();
    current.u_skip_br_b = false;
})(current, previous);
```

## 10.2 Performance & Configuration Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **GlideRecord in loops (N+1 query problem)** | 🔴 High | Use `addJoin()` or `glideAggregate()` |
| 2 | **Display business rules on large tables** | 🔴 High | Disable `runscript=true`; use calculated fields |
| 3 | **Missing indexes on filter fields** | 🔴 High | Add index on high-cardinality filter columns |
| 4 | **Synchronous REST calls in UI action** | 🔴 High | Use async ` SNC.Networking` or flow subflow |
| 5 | **Overly broad `sysparm_query=*` returns** | 🟡 Medium | Paginate; use `sysparm_limit`, `sysparm_offset` |
| 6 | **No caching on reference qualifiers** | 🟡 Medium | Use `getRefRecord()` + cache; or `glide.ignore.user` |
| 7 | **Large load scripts without transaction guards** | 🟡 Medium | Batch in chunks of 1000; use `glide.limit.iteration` |
| 8 | **Hardcoded instance URLs in scripts** | 🟡 Medium | Use `gs.getProperty('glide.servlet.uri')` |
| 9 | **MID Server polling too frequently (< 30s)** | 🟡 Medium | Set minimum 30s poll interval; batch processing |
| 10 | **Unused flows/布雷ak-tips left enabled** | 🟡 Medium | Audit and disable deprecated flows quarterly |

### N+1 Query Problem

```javascript
// BAD: Query inside loop
var gr = new GlideRecord('incident');
gr.addQuery('active', true);
gr.query();
while (gr.next()) {
    var user = new GlideRecord('sys_user');
    user.get(gr.caller_id);
    gs.info(user.name); // Each iteration = new query
}

// GOOD: Join upfront
var ga = new GlideAggregate('incident', 'caller_id.name');
ga.addQuery('active', true);
ga.addAggregate('COUNT');
ga.groupBy('caller_id');
ga.query();
while (ga.next()) {
    gs.info(ga.caller_id.name + ': ' + ga.getAggregate('COUNT'));
}
```

### Missing Index Example

```javascript
// Query: INC0001234 - slow on large tables
gr.addQuery('assignment_group', 'Network Operations');
gr.addQuery('state', '!=', '7');
gr.addQuery('active', 'true');
gr.addQuery('opened_at', '>', startOfMonth);

// DIAGNOSE: Check Explain Plan
// gs.debugSQL = true;
// Run query → check Execution plan in DevTools

// FIX: Add index via "Tables & Columns" or:
var idx = new GlideIndex('incident');
idx.addColumn('assignment_group');
idx.addColumn('state');
idx.addColumn('active');
idx.create();

// Verify: System Diagnostics → Database → Indexes → Find unused
```

### Async REST in UI Action

```javascript
// BAD: Blocks UI for up to 30 seconds
var r = new sn_ws.RESTMessageV2();
r.invoke(); // synchronous!

// GOOD: Use REST Message in Flow Designer with Async HTTP
// OR in script: use background script with g_synchronous = false
// OR use: new sn_ws.RESTMessageV2().executeAsync();
(function() {
    var r = new sn_ws.RESTMessageV2();
    r.setHttpMethod('POST');
    r.setEndpoint('https://api.example.com/notify');
    r.setRequestBody(JSON.stringify({id: current.sys_id}));
    var handle = r.executeAsync();
    // Returns immediately; handle.getStatusCode() later in scheduled job
})();
```
