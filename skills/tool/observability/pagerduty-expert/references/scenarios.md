# Scenario Examples

## 9.1 Incident Escalation Scenarios

### Scenario: Cascading Database Failure

**User:** "Our primary database is showing connection timeouts and we're getting PagerDuty alerts every 30 seconds. Multiple services are affected."

**Expert:**
> **Immediate Response:**
>
> 1. **Acknowledge and Silence** (prevent alert fatigue)
>    ```bash
>    # Acknowledge the storm of alerts
>    pd-cli incidents bulk-acknowledge \
>      --filter "service=database AND status=triggered"
>    
>    # Create a maintenance window
>    pd-cli maintenance-windows create \
>      --service DATABASE_SERVICE_ID \
>      --start "2024-01-15T14:00:00Z" \
>      --end "2024-01-15T15:00:00Z" \
>      --description "Database failover in progress"
>    ```
>
> 2. **Identify Root Service**
>    - Check PagerDuty Service Map for dependency chain
>    - Database → API Layer → Frontend
>    - Focus remediation on database first
>
> 3. **Escalate Appropriately**
>    ```bash
>    # If database team needs help, page them directly
>    pd-cli incidents create \
>      --title "DBA assistance needed: Primary DB failover" \
>      --service DATABASE_SERVICE_ID \
>      --priority P1 \
>      --assignee DBA_SCHEDULE_ID
>    ```
>
> 4. **Update Stakeholders**
>    - Post to Statuspage: "Database Performance Issue - Investigating"
>    - Notify #incidents channel with estimated resolution

### Scenario: After-Hours Security Alert

**User:** "We received a PagerDuty alert for suspicious login activity. The on-call engineer isn't responding."

**Expert:**
> **Escalation Procedure:**
>
> ```bash
> # 1. Page again with high urgency
> pd-cli incidents update INCIDENT_ID \
>   --urgency high \
>   --note "Second page - no response from primary on-call"
>
> # 2. Escalate to secondary responder
> pd-cli incidents escalate INCIDENT_ID \
>   --escalation-policy PLATFORM_ESCALATION_ID
>
> # 3. If still no response after 10 minutes, page manager
> pd-cli incidents create \
>   --title "URGENT: Security incident - no on-call response" \
>   --service security-alerts \
>   --priority P1 \
>   --assignee SECURITY_MANAGER_ID
> ```
>
> **Security Incident Protocol:**
> - Do NOT resolve without security team review
> - Preserve logs: `pd-cli incidents get INCIDENT_ID --show-logs`
> - Document all actions taken for compliance

### Scenario: Third-Party API Outage

**User:** "Stripe's API is down and we're getting alerts about payment failures. How do we handle this?"

**Expert:**
> **Third-Party Integration Failure Response:**
>
> 1. **Create Maintenance Window** (stops alert noise)
>    ```bash
>    pd-cli maintenance-windows create \
>      --service payment-service \
>      --start "2024-01-15T14:30:00Z" \
>      --duration 120 \
>      --description "Stripe API outage - maintenance window"
>    ```
>
> 2. **Implement Circuit Breaker**
>    - Configure your application to fail gracefully
>    - Queue payments for retry when Stripe recovers
>
> 3. **Monitor for Recovery**
>    ```bash
>    # Create a recovery check alert
>    pd-cli services create-alert-rule PAYMENT_SERVICE_ID \
>      --condition "stripe_api_status == healthy" \
>      --action notify
>    ```
>
> 4. **Post-Mortem Actions**
>    - Document third-party dependencies in PagerDuty
>    - Set up statuspage.io monitoring for Stripe
>    - Review circuit breaker configuration

## 9.2 Multi-Environment Setups

### Scenario: Different Escalation Paths per Environment

**User:** "We have dev, staging, and production environments. How should we configure different escalation policies?"

**Expert:**
> **Environment-Based Routing:**
>
> | Environment | Response Time | Escalation | Stakeholders |
> |-------------|---------------|------------|--------------|
> | Production  | 15 min        | 3 levels   | VP Engineering, CTO |
> | Staging     | 2 hours       | 1 level    | Team Lead |
> | Development | Next business | 0 (email)  | Developer |
>
> **Implementation:**
> ```yaml
> # Production - 24/7 coverage
> resource "pagerduty_escalation_policy" "production" {
>   name = "Production Escalation"
>   rule {
>     assignment { type = "schedule"; id = pagerduty_schedule.prod_oncall.id }
>     delay = 0
>   }
>   rule {
>     assignment { type = "user"; id = pagerduty_user.sre_lead.id }
>     delay = 15
>   }
>   rule {
>     assignment { type = "user"; id = pagerduty_user.vp_engineering.id }
>     delay = 30
>   }
> }
>
> # Staging - Business hours only
> resource "pagerduty_schedule" "staging_oncall" {
>   name      = "Staging On-Call"
>   time_zone = "America/Los_Angeles"
>   
>   layer {
>     name            = "Weekday Coverage"
>     start           = "2024-01-01T09:00:00-08:00"
>     rotation_turns  = 1
>     rotation_length = 7
>     users           = [pagerduty_user.developer.id]
>     
>     restriction {
>       type           = "daily_restriction"
>       start_time_of_day = "09:00:00"
>       end_time_of_day   = "18:00:00"
>       start_day_of_week = 1  # Monday
>       end_day_of_week   = 5  # Friday
>     }
>   }
> }
> ```

### Scenario: Region-Based Failover

**User:** "We run in US-East and EU-West. How do we route incidents to the correct regional team?"

**Expert:**
> **Multi-Region On-Call Strategy:**
>
> ```bash
> # EU-West on-call
> pd-cli schedules create \
>   --name "EU-West Infrastructure On-Call" \
>   --time-zone "Europe/London" \
>   --users USER_ID_1,USER_ID_2 \
>   --handoff-time "10:00"
>
> # US-East on-call
> pd-cli schedules create \
>   --name "US-East Infrastructure On-Call" \
>   --time-zone "America/New_York" \
>   --users USER_ID_3,USER_ID_4 \
>   --handoff-time "10:00"
>
> # Configure routing based on alert labels
> # Prometheus alert with region label
> alert: HighLatencyByRegion
> expr: histogram_quantile(0.99, http_request_duration_seconds_bucket) > 2
> labels:
>   severity: warning
>   region: "{{ $labels.region }}"
> annotations:
>   summary: "High latency in {{ $labels.region }}"
>
> # Alertmanager routes by region
> route:
>   - match:
>       region: eu-west
>     receiver: 'pagerduty-eu-west'
>   - match:
>       region: us-east
>     receiver: 'pagerduty-us-east'
> ```

## 9.3 Disaster Recovery

### Scenario: Complete On-Call System Failure

**User:** "What happens if PagerDuty itself goes down? How do we ensure we can still respond to incidents?"

**Expert:**
> **DR Strategy for PagerDuty Outage:**
>
> **1. Backup Communication Channels**
> ```yaml
> # Configure multiple notification channels
> resource "pagerduty_user" "engineer" {
>   name  = "John Engineer"
>   email = "john@company.com"
>   
>   job_title = "Senior SRE"
>   
>   # Multiple contact methods
>   contact_method {
>     type    = "phone_contact_method"
>     address = "+14155551234"
>     label   = "Mobile"
>   }
>   
>   contact_method {
>     type    = "email"
>     address = "john@company.com"
>     label   = "Work Email"
>   }
>   
>   # Backup: SMS to alternate number
>   contact_method {
>     type    = "sms_contact_method"
>     address = "+14155555678"
>     label   = "Backup SMS"
>   }
> }
> ```
>
> **2. Slack-Based Fallback**
> - Create #incident-response channel
> - Configure Slack alerts via PagerDuty
> - If PagerDuty fails, manually post to Slack
>
> **3. Manual Escalation Runbook**
> ```
> PagerDuty Outage Procedure:
> 1. Check status.pagerduty.com
> 2. If confirmed outage:
>    - Post to #incidents: "PagerDuty outage confirmed"
>    - Use backup phone tree (stored in 1Password)
>    - IT contacts on-call manager directly
> 3. Continue incident response via Slack
> 4. Document all actions manually
> 5. When PagerDuty recovers, create incidents retroactively
> ```
>
> **4. Regular Testing**
> ```bash
> # Quarterly DR test
> # 1. Simulate PagerDuty outage
> # 2. Verify backup notification works
> # 3. Document response time
> # 4. Update runbook with lessons learned
> ```

### Scenario: Data Recovery After Accidental Deletion

**User:** "We accidentally deleted critical escalation policies. How do we recover?"

**Expert:**
> **Recovery Options:**
>
> **1. Terraform State Recovery**
> ```bash
> # If using Terraform, restore from state
> terraform state pull > backup.tfstate
    
> # Identify deleted resources
> terraform state list | grep -i escalation
    
> # Recreate from code
> terraform apply
> ```
>
> **2. PagerDuty Support**
> - Contact PagerDuty support immediately
> - Request "Resource Recovery" within 30-day window
> - Provide: Team IDs, deleted resource names, approximate deletion time
>
> **3. Configuration Backup Strategy**
> ```yaml
> # Schedule daily backups
> resource "null_resource" "pd_config_backup" {
>   triggers = {
>     always_run = timestamp()
>   }
>   
>   provisioner "local-exec" {
>     command = <<-EOT
>       curl -s "https://api.pagerduty.com/services" \
>         -H "Authorization: Token token=${var.pagerduty_api_key}" \
>         > "backups/services-$(date +%Y%m%d).json"
>       
>       curl -s "https://api.pagerduty.com/escalation_policies" \
>         -H "Authorization: Token token=${var.pagerduty_api_key}" \
>         > "backups/escalation-policies-$(date +%Y%m%d).json"
>     EOT
>   }
> }
> ```
