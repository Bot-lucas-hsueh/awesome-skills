# Glide API Reference

## GlideRecord

### CRUD Operations

```javascript
// CREATE
var gr = new GlideRecord('incident');
gr.initialize();
gr.short_description = 'Sample incident';
gr.caller_id = gs.getUserID();
var sysId = gr.insert();

// READ
var gr = new GlideRecord('incident');
gr.addQuery('active', true);
gr.addQuery('priority', '<=', 2);
gr.orderByDesc('sys_created_on');
gr.setLimit(100);
gr.query();

while (gr.next()) {
    gs.info(gr.number + ': ' + gr.short_description);
}

// UPDATE
var gr = new GlideRecord('incident');
if (gr.get('number', 'INC0010001')) {
    gr.state = 6; // Resolved
    gr.update();
}

// DELETE
var gr = new GlideRecord('incident');
if (gr.get('number', 'INC0010001')) {
    gr.deleteRecord();
}
```

### Query Operators
| Operator | Description | Example |
|----------|-------------|---------|
| `=` | Equals | `addQuery('state', '=', 2)` |
| `!=` | Not equals | `addQuery('state', '!=', 7)` |
| `<` | Less than | `addQuery('priority', '<', 3)` |
| `>` | Greater than | `addQuery('opened_at', '>', gs.daysAgo(7))` |
| `IN` | In list | `addQuery('state', 'IN', '1,2,3')` |
| `CONTAINS` | Contains text | `addQuery('short_description', 'CONTAINS', 'error')` |
| `STARTSWITH` | Starts with | `addQuery('number', 'STARTSWITH', 'INC')` |

### Performance Methods
```javascript
gr.setWorkflow(false);      // Skip business rules
gr.autoSysFields(false);    // Skip audit fields
gr.setForceUpdate(true);    // Force update even if no changes
gr.setLimit(1000);          // Limit results
```

## GlideRecordSecure
ACL-aware version of GlideRecord:
```javascript
var gr = new GlideRecordSecure('incident');
gr.query();  // Only returns records user can read
```

## GlideSystem (gs)

### User & Session
```javascript
gs.getUserID();           // Current user sys_id
gs.getUserName();         // Username
gs.getUserDisplayName();  // Full name
gs.hasRole('itil');       // Check role
gs.getUser().isMemberOf('Group Name');
```

### Dates
```javascript
gs.now();                 // Current datetime
gs.today();               // Current date
gs.daysAgo(7);            // Date 7 days ago
gs.hoursAgo(24);          // Datetime 24 hours ago
gs.addDays('2024-01-01', 30);  // Add days to date
```

### Logging
```javascript
gs.info('Information message');
gs.warn('Warning message');
gs.error('Error message');
gs.debug('Debug message');  // Only in debug mode
```

### Properties
```javascript
var value = gs.getProperty('custom.property.name', 'default');
gs.setProperty('custom.property.name', 'value');
```

## GlideDateTime
```javascript
var gdt = new GlideDateTime();
gdt.addDays(7);
gdt.addHours(-2);
gdt.addMinutes(30);

var dateStr = gdt.getDisplayValue();  // Formatted date
var internal = gdt.getValue();         // Internal format
```

## GlideDuration
```javascript
var dur = new GlideDuration();
dur.setMilliseconds(86400000);  // 1 day

var display = dur.getDisplayValue();  // "1 Day"
```

## Script Include Pattern
```javascript
var MyUtils = Class.create();
MyUtils.prototype = {
    initialize: function() {
        this.tableName = 'incident';
    },
    
    findByNumber: function(number) {
        var gr = new GlideRecord(this.tableName);
        if (gr.get('number', number)) {
            return gr;
        }
        return null;
    },
    
    type: 'MyUtils'
};
```

## Business Rule Template
```javascript
(function executeRule(current, previous /*null when async*/) {
    // Add your code here
    
})(current, previous);
```

## Client Script (onChange)
```javascript
function onChange(control, oldValue, newValue, isLoading) {
    if (isLoading || newValue == '') {
        return;
    }
    
    g_form.setValue('field_name', 'value');
    g_form.showFieldMsg('field_name', 'Message', 'info');
}
```

## UI Action (Server-side)
```javascript
// Condition
current.state == 1 && gs.hasRole('itil');

// Script
current.state = 2;  // In Progress
current.assigned_to = gs.getUserID();
current.update();
gs.addInfoMessage('Incident assigned to you');
action.setRedirectURL(current);
```
