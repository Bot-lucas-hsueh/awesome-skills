# Scenario Examples

## 9.1 IT Service Management Scenarios

> **Note:** Workday is primarily HCM/Finance focused, but integrates with ITSM for employee-facing workflows.

### Scenario: IT Ticket Creation from Workday Profile

> **User:** "When an employee updates their phone number in Workday, we want to auto-create an IT ticket to update their AD phone."

**Expert:**
> **Flow: Workday → ServiceNow via REST API:**
>
> 1. **Workday:** Configure Business Process on Worker Data change
>    ```
>    Trigger: Workday → Business Process: "Update Personal Contact Info"
>        Step: If Work_Phone changes → Invoke Web Service
>    ```
>
> 2. **Workday EIB Outbound:**
>    ```xml
>    <wd:Integration_System>IT_Profile_Sync_Outbound</wd:Integration_System>
>    <wd:Operation>Notify_IT</wd:Operation>
>    <wd:Worker_Reference>
>      <wd:ID wd:type="Employee_ID">{Employee_ID}</wd:ID>
>    </wd:Worker_Reference>
>    <wd:New_Work_Phone>{New_Phone}</wd:New_Work_Phone>
>    <wd:Change_Date>{Current_Date}</wd:Change_Date>
>    ```
>
> 3. **ServiceNow:** Inbound REST endpoint receives payload
>    ```javascript
>    // Scripted REST Resource: POST /api/x_hr/workday-profile-update
>    var data = request.body.data;
>    var inc = new GlideRecord('incident');
>    inc.initialize();
>    inc.short_description = 'AD Phone Update - Employee: ' + data.worker_id;
>    inc.description = 'Update corporate phone for ' + data.worker_id + 
>                      ' from AD to: ' + data.new_phone;
>    inc.category = 'security';
>    inc.subcategory = 'active_directory';
>    inc.assignment_group = 'Identity Management';
>    inc.insert();
>    ```

## 9.2 HR & Finance Workflows

### Scenario: Offboarding Automation

> **User:** "When an employee is terminated, we need to revoke access across 15 systems automatically."

**Expert:**
> **Offboarding Workflow:**
>
> ```
> Terminate Action in Workday
>         │
>         ├─ BP: "Terminate Employee"
>         │    └─ Last Day = termination_date
>         │
>         ├─ Day = termination_date - 1:
>         │    Flow Designer in ServiceNow (triggered by WD EIB):
>         │        ├─ Create "Offboarding" task group
>         │        ├─ Parallel tasks:
>         │        │   ├─ Revoke AD account (PowerShell via MID)
>         │        │   ├─ Disable VPN access
>         │        │   ├─ Revoke Okta/SAML access
>         │        │   ├─ Remove from distribution lists
>         │        │   ├─ Revoke AWS IAM roles
>         │        │   ├─ Forward emails to manager
>         │        │   ├─ Disable Slack/Teams account
>         │        │   ├─ Revoke badge access
>         │        │   └─ Calendar: Decline all meetings
>         │        │
>         │        └─ Notify HR + Manager on each task completion
>         │
>         └─ Day = termination_date + 1:
>              Send offboarding confirmation to HR
>              Mark all tasks complete
>              Archive worker record in Workday
> ```
>
> **Workday BP Configuration:**
> ```
> Initiator: HR Specialist
> Stage 1: HR Approval (1 day SLA)
>   Actor: Direct Manager
> Stage 2: IT Offboarding (Automated)
>   Condition: termination_date <= CURRENT_DATE + 1
>   Action: Invoke EIB Outbound "Terminate_Employee_Events"
> Stage 3: Payroll Finalization
>   Actor: Payroll Processor
>   Action: Process final paycheck + PTO payout
> Stage 4: Compliance Hold
>   Condition: if manager needs 30-day doc retention
>   Hold: Document access for 30 days post-termination
> ```

### Scenario: Compensation Planning Cycle

> **User:** "Walk me through the annual merit increase cycle from Workday."

**Expert:**
> **Merit Increase Workflow:**
>
> ```
> Jan 1: Compensation Analyst configures cycle
>   ├── Create Compensation Review Template
>   ├── Set budget % (e.g., 4% for merit pool)
>   ├── Configure matrix: Performance Rating → Increase %
>   │       Exceeds Expectations → 5-7%
>   │       Meets Expectations → 3-5%
>   │       Needs Improvement → 0-2%
>   └── Assign to HR Business Partners
>
> Jan 15: Managers receive review tasks
>   ├── View current salary + compa-ratio
>   ├── Enter proposed increase per employee
>   ├── Add justification notes
>   └── Submit for HR review
>
> Feb 1: HRBP Review
>   ├── Approve/modify proposed increases
>   ├── Flag outliers (compa-ratio > 1.1 or < 0.85)
>   └── Check against salary bands
>
> Feb 15: Compensation Approval
>   ├── VP/CHRO final approval
>   └── Budget reconciliation
>
> Mar 1: Payroll Execution
>   ├── Load increases to Payroll
>   ├── Effective_Date = Mar 1
>   ├── Retro pay processing for Jan-Feb period
>   └── Manager notification of finalized increases
> ```

## 9.3 Support Ticketing Workflows

### Scenario: Benefits Enrollment Support

> **User:** "Open enrollment is next month. How do we route benefits questions to the right team?"

**Expert:**
> **Benefits Support Routing:**
>
> ```
> Employee submits question via Workday
>   │
>   ├─ Category detection (NLP or form):
>   │   ├─ "medical" or "health plan" → Benefits: Medical
>   │   ├─ "401k" or "retirement" → Benefits: Retirement
>   │   ├─ "dental" or "vision" → Benefits: Dental/Vision
>   │   ├─ "HSA" or "FSA" → Benefits: Accounts (HSA/FSA)
>   │   └─ "COBRA" or "terminated" → Benefits: COBRA/Continuation
>   │
>   ├─ Tier 1 (Benefits SSC):
>   │   FAQ lookup (Knowledge Base)
>   │   If not resolved → escalate to Tier 2
>   │
>   ├─ Tier 2 (Benefits Specialists):
>   │   Direct data correction in Workday
>   │   Life event corrections
>   │   Plan design questions
>   │
>   └─ Tier 3 (Carriers/Brokers):
>       Complex claims or coverage disputes
>       Carrier contact information auto-populated
> ```
>
> **Workday Communities Setup:**
> ```
> Create Communities Group: "Benefits Support Center"
> Configure BP: "Benefits Inquiry"
>   ├── Category dropdown (custom fields)
>   ├── Urgency (High = near enrollment deadline)
>   ├── Attach relevant plan documents (auto-attached by category)
>   └── SLA: 24h response for Tier 1, 4h for escalated
> ```

### Scenario: Payroll Discrepancy Resolution

> **User:** "An employee says their paycheck is wrong. How do we trace and fix it?"

**Expert:**
> **Payroll Dispute Resolution:**
>
> ```
> Employee reports discrepancy
>         │
>         ├─ Step 1: HR verifies in Workday
>         │   ├── Check Pay Group → Pay Period
>         │   ├── Review Payslip Components:
>         │   │   Base Pay: correct?
>         │   │   Overtime: any missing hours?
>         │   │   Deductions: correct plans?
>         │   │   Taxes: withholding correct?
>         │   └── One-time payments: included?
>         │
>         ├─ Step 2: Time tracking verification
>         │   ├── Punch clock → Time off requests
>         │   ├── Holiday pay applied?
>         │   └── Correct pay rule group?
>         │
>         ├─ Step 3: If Workday data correct:
>         │   Redirect to Payroll Processor (ADP/Paychex/Paycom)
>         │   Pull pay register comparison
>         │
>         └─ Step 4: If correction needed:
>             ├── Correct in Workday
>             ├── Generate supplemental run (if mid-period)
>             ├── Or adjust in next pay period
>             └── Document in case management record
> ```

### Scenario: Performance Review Cycle Automation

> **User:** "We have a semi-annual review process. How do we automate reminders and escalations?"

**Expert:**
> **Performance Review BP Automation:**
>
> ```
> T-30 Days: Cycle Initiated
>   System creates review periods for all active employees
>   Managers receive "Open Review Period" task
>
> T-21 Days: Self-Assessment Reminder
>   Email to employee: "Complete your self-assessment"
>   If not done → escalate to manager
>
> T-14 Days: Manager Assessment Window Opens
>   BP assigns task to direct manager
>   Include: Self-assessment summary (read-only)
>   Include: Goals from last cycle
>   Include: 360 feedback (if configured)
>
> T-7 Days: Reminder to Manager
>   Inbox notification: "Your team's reviews are 50% complete"
>   Dashboard: List of incomplete reviews
>
> T-1 Day: Escalation to Skip-Level
>   If manager < 25% complete → notify skip-level manager
>
> T+0 (Due Date): Lock Submissions
>   BP closes review window
>   Incomplete reviews flagged to HR
>
> T+7 Days: Calibration Sessions
>   HR creates calibration meeting agenda in Workday
>   Rating distribution charts auto-generated
>
> T+14 Days: Final Ratings Published
>   Employee notified: "Your review is ready"
>   Compensation changes effective (if merit cycle)
> ```
