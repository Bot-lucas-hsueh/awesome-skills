## §5 · Gotchas & Anti-Patterns

### #SN1: Business Rule Recursion
```javascript
// BAD: Recursive update loop
(function executeRule(current, previous) {
    current.priority = '1';
    current.update();  // Triggers another update!
})(current, previous);

// GOOD: Recursion guard
(function executeRule(current, previous) {
    if (current.isActionAborted()) return;
    if (!current.isNewRecord()) return;
    current.priority = '1';  // Don't call update() in Before rules
})(current, previous);
```

### #SN2: GlideRecord in Loops (N+1 Problem)
```javascript
// BAD: Query inside loop
while (inc.next()) {
    var user = new GlideRecord('sys_user');  // N queries!
    user.get(inc.caller_id);
}

// GOOD: Single query with map
var users = {};
var userGR = new GlideRecord('sys_user');
userGR.query();
while (userGR.next()) {
    users[userGR.sys_id] = userGR.name;
}
while (inc.next()) {
    gs.info(users[inc.caller_id]);
}
```

### #SN3: Hardcoded Values
```javascript
// BAD: Brittle across instances
if (current.category == 'Hardware') {
    current.assignment_group = '8a4f7e2f1b303000...';  // Hardcoded!
}

// GOOD: Dynamic lookup
var grpName = gs.getProperty('hardware.assignment_group');
var grp = new GlideRecord('sys_user_group');
if (grp.get('name', grpName)) {
    current.assignment_group = grp.sys_id;
}
```

### #SN4: Ignoring ACLs
```javascript
// BAD: Bypasses security
var inc = new GlideRecord('incident');
inc.query();  // User sees everything

// GOOD: ACL-aware
var inc = new GlideRecordSecure('incident');
inc.query();  // Respects security model
```

### #SN5: Global Scope Abuse
```javascript
// BAD: Everything in global
Global: MyScriptInclude, my_business_rule

// GOOD: Scoped applications
Application: x_vendor_mgmt
- x_vendor_mgmt.vendor
- x_vendor_mgmt.VendorUtils
```

---
