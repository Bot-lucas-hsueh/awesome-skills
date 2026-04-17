# Scenario Examples

## 9.1 Basic Usage

**User:** "How do I get started with ServiceNow?"

**Expert:**
> **Getting Started:**
>
> 1. Access your ServiceNow instance
> 2. Navigate to the application
> 3. Create your first record
>
> ```javascript
> // Create incident via script
> var inc = new GlideRecord('incident');
> inc.initialize();
> inc.short_description = 'Issue description';
> inc.category = 'software';
> inc.insert();
> ```

## 9.2 Incident Management

**User:** "How do I create and manage incidents in ServiceNow?"

**Expert:**
> **Incident Workflow:**
>
> ```javascript
> // Create incident
> var inc = new GlideRecord('incident');
> inc.initialize();
> inc.short_description = 'User cannot login';
> inc.description = 'User receives error when logging in';
> inc.caller_id = '6816f79cc0a8016401c5a33be04be441'; // User sys_id
> inc.category = 'software';
> inc.subcategory = 'access';
> inc.priority = 2;
> inc.urgency = 2;
> inc.impact = 2;
> var sysId = inc.insert();
> ```

> **Update Incident:**
> ```javascript
> var inc = new GlideRecord('incident');
> inc.get('INC0012345');
> inc.state = 2; // In Progress
> inc.assigned_to = 'some_user_sys_id';
> inc.work_notes = 'Working on the issue';
> inc.update();
> ```

> **Close Incident:**
> ```javascript
> var inc = new GlideRecord('incident');
> inc.get('INC0012345');
> inc.state = 7; // Closed
> inc.resolution_notes = 'Fixed by resetting password';
> inc.update();
> ```

## 9.3 Change Management

**User:** "How do I create a change request?"

**Expert:**
> **Change Request Workflow:**
>
> ```javascript
> // Create change request
> var change = new GlideRecord('change_request');
> change.initialize();
> change.short_description = 'Upgrade database server';
> change.description = 'Upgrade production MySQL from 5.7 to 8.0';
> change.type = 'normal';
> change.risk = 'medium';
> change.category = 'database';
> change.planned_start_date = '2024-03-15 02:00:00';
> change.planned_end_date = '2024-03-15 06:00:00';
> change.insert();
> ```

## 9.4 Script Include

**User:** "How do I create a reusable script include?"

**Expert:**
> **Script Include:**
>
> ```javascript
> var MyAppUtils = Class.create();
> MyAppUtils.prototype = {
>     initialize: function() {},
>
>     getUserInfo: function(userId) {
>         var user = new GlideRecord('sys_user');
>         if (user.get(userId)) {
>             return {
>                 name: user.getDisplayValue('name'),
>                 email: user.email,
>                 department: user.department.getDisplayValue()
>             };
>         }
>         return null;
>     },
>
>     createIncident: function(shortDesc, description, callerId) {
>         var inc = new GlideRecord('incident');
>         inc.initialize();
>         inc.short_description = shortDesc;
>         inc.description = description;
>         inc.caller_id = callerId;
>         return inc.insert();
>     },
>
>     type: 'MyAppUtils'
> };
> ```

## 9.5 REST API Integration

**User:** "How do I integrate with external APIs?"

**Expert:**
> **Outbound REST:**
>
> ```javascript
> var r = new sn_ws.RESTMessageV2('External API', 'Get Tickets');
> r.setHttpMethod('GET');
> r.setEndpoint('https://api.example.com/tickets');
> r.setRequestHeader('Authorization', 'Bearer ' + gs.getProperty('api.token'));
> r.setRequestHeader('Content-Type', 'application/json');
>
> var response = r.execute();
> var status = response.getStatusCode();
> var body = response.getBody();
> ```

> **Inbound REST (Scripted REST API):**
>
> ```javascript
> (function process(/\* RESTAPIRequest\*/ request, /\* RESTAPIResponse\*/ response) {
>     var data = request.body.data;
>     
>     var inc = new GlideRecord('incident');
>     inc.initialize();
>     inc.short_description = data.short_description;
>     inc.description = data.description;
>     inc.caller_id = data.caller_email;
>     var sysId = inc.insert();
>     
>     response.setStatus(201);
>     response.setBody({ sys_id: sysId, status: 'created' });
> })(request, response);
> ```

## 9.6 Flow Designer

**User:** "How do I create a flow in ServiceNow?"

**Expert:**
> **Flow Creation:**
>
> 1. **Trigger**: Record created or updated on incident table
> 2. **Condition**: Priority = 1 (Critical)
> 3. **Actions**:
>    - Notify on-call manager via email
>    - Create task for escalation team
>    - Update assignment group
>    - Add work note

> **Flow Example (Pseudo-code):**
> ```
> When incident.priority = 1 AND incident.created
>     DO:
>       - Send Email: To = assigned_to.manager, Subject = "Critical Incident"
>       - Create Task: "Escalation Review" assigned to Security Team
>       - Update Field: assigned_group = "Tier 2 Support"
>       - Add Work Note: "Auto-escalated due to critical priority"
> ```

## 9.7 Business Rule

**User:** "How do I create a business rule?"

**Expert:**
> **Business Rule Example:**
>
> ```javascript
> // Before business rule on Incident
> (function executeRule(current, previous) {
>     // Auto-assign high priority incidents
>     if (current.priority == 1 && current.assigned_to.nil()) {
>         current.assigned_to = 'support_group';
>         current.assignment_group = 'Level 2 Support';
>     }
>     
>     // Set initial values
>     if (current.isNewRecord()) {
>         current.u_first_response_due = gs.nowDateTime();
>     }
> })(current, previous);
> ```

## 9.8 ACL (Access Control)

**User:** "How do I create an ACL?"

**Expert:**
> **ACL Example:**
>
> ```javascript
> // ACL: Read access to incident assigned to current user
> (function runScript(ctrl, req) {
>     // Allow if user is assigned to the incident
>     if (current.assigned_to == gs.getUserID()) {
>         return true;
>     }
>     
>     // Allow if user is in the assignment group
>     var gr = new GlideRecord('sys_user_grmember');
>     gr.addQuery('user', gs.getUserID());
>     gr.addQuery('group', current.assignment_group);
>     gr.query();
>     
>     return gr.getRowCount() > 0;
> })(acl, request);
> ```
