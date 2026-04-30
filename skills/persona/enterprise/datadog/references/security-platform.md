# Datadog Security Platform Reference

> Comprehensive guide to Cloud Security Posture Management (CSPM), Cloud Workload Protection (CWP/CWPP), and Cloud SIEM

---

## Cloud Security Posture Management (CSPM)

### AWS CSPM Setup

**IAM Policy:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudtrail:DescribeTrails",
        "cloudtrail:GetTrailStatus",
        "cloudtrail:GetEventSelectors",
        "config:Get*",
        "config:Describe*",
        "config:List*",
        "ec2:Describe*",
        "iam:Get*",
        "iam:List*",
        "kms:List*",
        "kms:Describe*",
        "logs:Describe*",
        "s3:GetBucket*",
        "s3:ListBucket",
        "sns:List*",
        "sqs:List*"
      ],
      "Resource": "*"
    }
  ]
}
```

**Terraform Configuration:**
```hcl
resource "datadog_integration_aws" "main" {
  account_id = var.aws_account_id
  role_name  = "DatadogIntegrationRole"
  
  cspm_resource_collection_enabled = true
  security_scanning_enabled        = true
}

# Enable compliance frameworks
resource "datadog_security_monitoring_default_rule" "cis_aws" {
  case {
    status        = "high"
    condition     = "a > 0"
    notifications = ["@security-team@company.com"]
  }
  
  enabled = true
}
```

### CSPM Rules

**Custom Rule Definition:**
```hcl
resource "datadog_security_monitoring_rule" "s3_public_access" {
  name        = "S3 Bucket Public Access"
  description = "Detects S3 buckets with public read/write access"
  enabled     = true
  type        = "configuration"
  
  query {
    query = <<-EOT
      source:cspm 
      @resource_type:aws_s3_bucket 
      @policy.name: "S3 Block Public Access"
    EOT
    
    group_by_fields = ["@resource", "@account_id"]
  }
  
  case {
    name      = "Public S3 Bucket Detected"
    status    = "high"
    condition = "a > 0"
    notifications = [
      "@security-oncall",
      "@slack-security-alerts"
    ]
  }
  
  options {
    detection_method    = "threshold"
    evaluation_window   = 86400
    keep_alive          = 604800
    max_signal_duration = 604800
  }
  
  tags = [
    "framework:cis",
    "framework:aws-foundations",
    "severity:high",
    "resource:s3"
  ]
}
```

### Compliance Frameworks

| Framework | Coverage | Description |
|-----------|----------|-------------|
| CIS AWS Foundations | 100% | Center for Internet Security benchmarks |
| CIS Azure Foundations | 100% | Azure-specific security controls |
| CIS GCP Foundations | 100% | GCP-specific security controls |
| PCI DSS | Partial | Payment card industry compliance |
| HIPAA | Partial | Healthcare data protection |
| SOC 2 | Partial | Service organization controls |
| GDPR | Partial | Data privacy regulations |

---

## Cloud Workload Protection (CWPP/CWS)

### Agent Configuration
```yaml
# datadog.yaml
security_agent:
  enabled: true
  
  runtime:
    enabled: true
    
    # Syscall monitoring
    syscall_monitor:
      enabled: true
    
    # Network detection
    network_detection:
      enabled: true
    
    # Anomaly detection
    anomaly_detection:
      enabled: true
      
  compliance:
    enabled: true
    
    # Check intervals
    check_interval: 20m
```

### Kubernetes Deployment
```yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  name: datadog-agent
  namespace: datadog
spec:
  template:
    spec:
      containers:
        - name: agent
          image: gcr.io/datadoghq/agent:latest
          env:
            - name: DD_SECURITY_AGENT_ENABLED
              value: "true"
            - name: DD_RUNTIME_SECURITY_CONFIG_ENABLED
              value: "true"
            - name: DD_COMPLIANCE_CONFIG_ENABLED
              value: "true"
          securityContext:
            capabilities:
              add:
                - SYS_ADMIN
                - SYS_RESOURCE
                - SYS_PTRACE
                - NET_ADMIN
                - NET_BROADCAST
                - NET_RAW
                - IPC_LOCK
                - CHOWN
          volumeMounts:
            - name: sys-kernel-debug
              mountPath: /sys/kernel/debug
            - name: etc-passwd
              mountPath: /etc/passwd
            - name: etc-group
              mountPath: /etc/group
      volumes:
        - name: sys-kernel-debug
          hostPath:
            path: /sys/kernel/debug
        - name: etc-passwd
          hostPath:
            path: /etc/passwd
        - name: etc-group
          hostPath:
            path: /etc/group
```

### CWS Detection Rules

**Default Rule Categories:**
- **Container Escape** — Detects container breakout attempts
- **Credential Access** — Detects credential dumping
- **Defense Evasion** — Detects process hiding
- **Discovery** — Detects system reconnaissance
- **Execution** — Detects unauthorized code execution
- **Impact** — Detects ransomware and data destruction
- **Initial Access** — Detects exploitation attempts
- **Lateral Movement** — Detects network propagation
- **Persistence** — Detects backdoor installation
- **Privilege Escalation** — Detects permission elevation

**Custom Detection Rule:**
```hcl
resource "datadog_security_monitoring_rule" "suspicious_container_exec" {
  name        = "Suspicious Container Execution"
  description = "Detects execution of suspicious binaries in containers"
  enabled     = true
  type        = "workload_security"
  
  agent_rule {
    agent_rule_id = "suspicious_container_exec"
    expression    = <<-EOT
      exec.file.path in ["/bin/bash", "/bin/sh", "/bin/dash"] &&
      exec.args_flags contains "-c" &&
      (
        exec.args contains "curl" ||
        exec.args contains "wget" ||
        exec.args contains "nc -e" ||
        exec.args contains "bash -i" ||
        exec.args contains "sh -i"
      ) &&
      container.id != ""
    EOT
  }
  
  case {
    name      = "Suspicious Container Activity"
    status    = "high"
    condition = "a > 0"
    notifications = ["@security-team"]
  }
  
  tags = [
    "tactic:execution",
    "technique:command_and_scripting_interpreter",
    "severity:high",
    "resource:container"
  ]
}
```

---

## Cloud SIEM

### Log Sources

**AWS CloudTrail:**
```hcl
resource "datadog_integration_aws_log_collection" "cloudtrail" {
  account_id = var.aws_account_id
  services   = ["cloudtrail"]
}
```

**Azure Activity Logs:**
```hcl
resource "datadog_integration_azure_log_collection" "activity" {
  tenant_name = var.azure_tenant_id
  client_id   = var.azure_client_id
  
  custom_log_collection = [
    "ActivityLogs"
  ]
}
```

**GCP Audit Logs:**
```hcl
resource "datadog_integration_gcp_sts" "audit" {
  project_id     = var.gcp_project_id
  client_email   = var.gcp_client_email
  
  automute       = true
  is_cspm_enabled = true
}
```

### SIEM Detection Rules

**Brute Force Detection:**
```hcl
resource "datadog_security_monitoring_rule" "aws_brute_force" {
  name        = "AWS Console Brute Force"
  description = "Detects multiple failed login attempts to AWS Console"
  enabled     = true
  
  query {
    query = <<-EOT
      source:cloudtrail 
      @eventName:ConsoleLogin 
      @error.message:*Failed*
    EOT
    
    group_by_fields = ["@userIdentity.userName", "@sourceIPAddress"]
  }
  
  case {
    name      = "Potential Brute Force"
    status    = "medium"
    condition = "a > 5"
    notifications = ["@security-oncall"]
  }
  
  options {
    detection_method    = "threshold"
    evaluation_window   = 300
    keep_alive          = 3600
    max_signal_duration = 86400
  }
  
  tags = [
    "tactic:credential_access",
    "technique:brute_force",
    "framework:mitre_attack"
  ]
}
```

**Privilege Escalation:**
```hcl
resource "datadog_security_monitoring_rule" "privilege_escalation" {
  name        = "IAM Policy Change"
  description = "Detects changes to IAM policies"
  enabled     = true
  
  query {
    query = <<-EOT
      source:cloudtrail 
      @eventName:(PutUserPolicy|PutRolePolicy|AttachUserPolicy|AttachRolePolicy|CreateAccessKey)
    EOT
    
    group_by_fields = ["@userIdentity.userName", "@eventName"]
  }
  
  case {
    name      = "IAM Policy Modified"
    status    = "high"
    condition = "a > 0"
    notifications = [
      "@security-oncall",
      "@slack-security-alerts"
    ]
  }
  
  tags = ["tactic:privilege_escalation", "resource:iam"]
}
```

**Data Exfiltration:**
```hcl
resource "datadog_security_monitoring_rule" "data_exfil" {
  name        = "Large Data Transfer"
  description = "Detects large data transfers outside organization"
  enabled     = true
  
  query {
    query = <<-EOT
      source:cloudtrail 
      @eventName:(GetObject|Download) 
      @bytes:>104857600
    EOT
    
    group_by_fields = ["@userIdentity.userName", "@sourceIPAddress"]
  }
  
  case {
    name      = "Potential Data Exfiltration"
    status    = "high"
    condition = "a > 10"
    notifications = ["@security-incident-response"]
  }
  
  tags = ["tactic:exfiltration", "severity:critical"]
}
```

---

## Application Security Management (ASM)

### Enable ASM
```yaml
datadog:
  apm:
    enabled: true
    
  asm:
    enabled: true
    
    # Threat detection modes
    threats:
      # SQL Injection
      sql_injection: true
      # Command Injection
      command_injection: true
      # XSS
      xss: true
      # SSRF
      ssrf: true
      # LFI/RFI
      lfi_rfi: true
```

**Environment Variables:**
```bash
export DD_APPSEC_ENABLED=true
export DD_APPSEC_RULES=/opt/datadog/appsec/rules.json
export DD_APPSEC_WAF_TIMEOUT=10000
```

---

## Security Dashboards

### Executive Security Dashboard
```json
{
  "title": "Security Overview - Executive",
  "widgets": [
    {
      "definition": {
        "title": "Compliance Score",
        "type": "query_value",
        "requests": [{
          "formulas": [{"formula": "compliant / total * 100"}],
          "queries": [
            {"data_source": "security_findings", 
             "query": "source:cspm status:pass", 
             "name": "compliant", "aggregator": "count"},
            {"data_source": "security_findings", 
             "query": "source:cspm", 
             "name": "total", "aggregator": "count"}
          ]
        }],
        "autoscale": false,
        "precision": 1,
        "unit": "%"
      }
    },
    {
      "definition": {
        "title": "Open Security Findings by Severity",
        "type": "toplist",
        "requests": [{
          "queries": [{
            "data_source": "security_findings",
            "query": "source:cspm @status:open",
            "name": "findings",
            "aggregator": "count"
          }],
          "formulas": [{"formula": "findings"}],
          "group_by": [{"facet": "@severity", "limit": 10}]
        }]
      }
    },
    {
      "definition": {
        "title": "SIEM Signals Over Time",
        "type": "timeseries",
        "requests": [{
          "queries": [{
            "data_source": "security_signals",
            "query": "*",
            "name": "signals"
          }],
          "formulas": [{"formula": "signals"}],
          "group_by": [{"facet": "status", "limit": 10}]
        }]
      }
    },
    {
      "definition": {
        "title": "Workload Security Detections",
        "type": "timeseries",
        "requests": [{
          "queries": [{
            "data_source": "security_signals",
            "query": "source:cws",
            "name": "detections"
          }]
        }]
      }
    }
  ],
  "layout_type": "ordered",
  "tags": ["security", "executive"]
}
```

---

## Incident Response Workflow

### Automated Response
```hcl
resource "datadog_security_monitoring_rule" "auto_response" {
  name        = "Auto-Isolate Compromised Instance"
  description = "Automatically isolate EC2 instances showing malicious behavior"
  enabled     = true
  
  query {
    query = <<-EOT
      source:cws 
      @evt.name:(exec | file) 
      @threat.tactic:(credential_access | lateral_movement)
    EOT
    
    group_by_fields = ["@host.id"]
  }
  
  case {
    name      = "Compromised Instance Detected"
    status    = "critical"
    condition = "a > 0"
    notifications = [
      "@webhook-isolate-instance",
      "@security-incident-response"
    ]
  }
  
  tags = ["auto-remediation:enabled", "severity:critical"]
}
```

### Webhook Payload
```json
{
  "alert_id": "{{alert_id}}",
  "title": "{{title}}",
  "severity": "{{severity}}",
  "host": "{{host.name}}",
  "threat": {
    "tactic": "{{threat.tactic}}",
    "technique": "{{threat.technique}}"
  },
  "remediation": {
    "action": "isolate_instance",
    "instance_id": "{{host.id}}",
    "security_group": "sg-isolated"
  }
}
```

---

## Security Metrics

| Metric | Source | Description |
|--------|--------|-------------|
| Compliance Score | CSPM | % of passing compliance checks |
| Mean Time to Detect (MTTD) | SIEM | Average time to detect threats |
| Mean Time to Respond (MTTR) | Signals | Average time to resolve signals |
| Open Findings | CSPM | Count of unremediated findings |
| Active Threats | CWS | Count of active runtime threats |
| Blocked Attacks | ASM | Count of blocked attack attempts |
