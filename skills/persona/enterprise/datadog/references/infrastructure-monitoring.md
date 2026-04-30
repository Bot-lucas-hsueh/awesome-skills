# Datadog Infrastructure Monitoring Reference

> Comprehensive guide to infrastructure monitoring with Datadog

---

## Agent Installation

### Linux (One-Line Install)
```bash
DD_API_KEY=<YOUR_API_KEY> \
DD_SITE="datadoghq.com" \
bash -c "$(curl -L https://s3.amazonaws.com/dd-agent/scripts/install_script_agent7.sh)"
```

### Docker
```bash
docker run -d --name datadog-agent \
  --cgroupns host \
  --pid host \
  -e DD_API_KEY=<YOUR_API_KEY> \
  -e DD_SITE="datadoghq.com" \
  -e DD_HOSTNAME=<HOSTNAME> \
  -v /var/run/docker.sock:/var/run/docker.sock:ro \
  -v /proc/:/host/proc/:ro \
  -v /sys/fs/cgroup/:/host/sys/fs/cgroup:ro \
  -v /var/lib/docker/containers:/var/lib/docker/containers:ro \
  gcr.io/datadoghq/agent:latest
```

### Kubernetes (Helm)
```bash
helm repo add datadog https://helm.datadoghq.com
helm install datadog datadog/datadog \
  --set datadog.apiKey=<API_KEY> \
  --set datadog.appKey=<APP_KEY> \
  --set datadog.site=datadoghq.com \
  --set datadog.tags={env:production,team:platform}
```

---

## Cloud Provider Integrations

### AWS Integration

**IAM Role Setup:**
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::464622532012:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "<DATADOG_EXTERNAL_ID>"
        }
      }
    }
  ]
}
```

**Terraform:**
```hcl
resource "datadog_integration_aws" "main" {
  account_id = var.aws_account_id
  role_name  = "DatadogIntegrationRole"
  
  account_specific_namespace_rules = {
    auto_scaling = false
    opsworks     = false
  }
  
  excluded_regions = ["us-gov-east-1", "us-gov-west-1"]
  
  filter_tags = ["env:production", "monitored:true"]
  
  host_tags = ["env:production", "cloud:aws"]
  
  metrics_collection_enabled = true
  cspm_resource_collection_enabled = true
}
```

### Azure Integration
```hcl
resource "datadog_integration_azure" "main" {
  tenant_name   = var.azure_tenant_id
  client_id     = var.azure_client_id
  client_secret = var.azure_client_secret
  
  host_filters = "tag:env:production"
}
```

### GCP Integration
```hcl
resource "datadog_integration_gcp" "main" {
  project_id     = var.gcp_project_id
  private_key_id = var.gcp_private_key_id
  private_key    = var.gcp_private_key
  client_email   = var.gcp_client_email
  client_id      = var.gcp_client_id
  
  host_filters = "env:production,team:platform"
}
```

---

## Container Monitoring

### Docker Integration
```yaml
# docker-compose.yml
version: '3'
services:
  datadog:
    image: gcr.io/datadoghq/agent:latest
    pid: host
    cgroup: host
    environment:
      - DD_API_KEY=${DD_API_KEY}
      - DD_SITE=datadoghq.com
      - DD_DOGSTATSD_NON_LOCAL_TRAFFIC=true
      - DD_APM_ENABLED=true
      - DD_APM_NON_LOCAL_TRAFFIC=true
      - DD_LOGS_ENABLED=true
      - DD_LOGS_CONFIG_CONTAINER_COLLECT_ALL=true
      - DD_CONTAINER_EXCLUDE=name:datadog-agent
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock:ro
      - /proc/:/host/proc/:ro
      - /sys/fs/cgroup/:/host/sys/fs/cgroup:ro
      - /var/lib/docker/containers:/var/lib/docker/containers:ro
    ports:
      - "8125:8125/udp"  # DogStatsD
      - "8126:8126/tcp"  # APM
```

### Kubernetes Key Metrics

| Metric | Description | Query |
|--------|-------------|-------|
| CPU Usage | Container CPU consumption | `avg:kubernetes.cpu.usage.total{*}` |
| Memory Usage | Container memory consumption | `avg:kubernetes.memory.usage{*}` |
| Pod Restarts | Number of container restarts | `sum:kubernetes.containers.restarts{*}` |
| Network RX/TX | Network throughput | `avg:kubernetes.network.rx_bytes{*}` |
| Disk Usage | Persistent volume usage | `avg:kubernetes.persistentvolumeclaim.usage{*}` |

### Kubernetes Alerts
```hcl
resource "datadog_monitor" "pod_crash_loop" {
  name    = "Pod CrashLoopBackOff"
  type    = "metric alert"
  
  query = <<-EOT
    max(last_10m):max:kubernetes.containers.restarts{*} by {pod_name,cluster_name} >= 3
  EOT
  
  message = <<-EOT
    Pod {{pod_name.name}} is in CrashLoopBackOff on cluster {{cluster_name.name}}
    
    Investigation steps:
    1. Check pod logs: `kubectl logs {{pod_name.name}}`
    2. Check events: `kubectl describe pod {{pod_name.name}}`
    3. Review recent deployments
    
    @slack-k8s-alerts
  EOT
  
  tags = ["k8s:health", "severity:high"]
}
```

---

## Serverless Monitoring

### AWS Lambda

**Layer Configuration:**
```yaml
# serverless.yml
functions:
  myFunction:
    handler: handler.main
    layers:
      - arn:aws:lambda:${aws:region}:464622532012:layer:Datadog-Extension:XX
    environment:
      DD_API_KEY_SECRET_ARN: arn:aws:secretsmanager:...
      DD_SITE: datadoghq.com
      DD_TRACE_ENABLED: true
      DD_LOGS_INJECTION: true
```

**Key Lambda Metrics:**
- `aws.lambda.duration` — Function execution time
- `aws.lambda.errors` — Error count
- `aws.lambda.throttles` — Throttle count
- `aws.lambda.invocations` — Invocation count
- `aws.lambda.cold_starts` — Cold start count

---

## Network Performance Monitoring

### Configuration
```yaml
datadog:
  networkMonitoring:
    enabled: true
  
  # System probe for eBPF-based collection
  systemProbe:
    enabled: true
    enableTCPQueueLength: true
    enableOOMKill: true
```

### Network Flow Logs
- Automatic collection of flow data
- DNS request tracking
- TLS certificate monitoring
- Network path visualization

---

## Best Practices

### Tagging Strategy
```yaml
# Recommended universal tags
tags:
  - "env:production"          # Environment
  - "team:platform"           # Owning team
  - "service:api-gateway"     # Service name
  - "tier:critical"           # Business criticality
  - "datacenter:us-east-1"    # Physical location
  - "region:aws-us-east-1"    # Cloud region
```

### Agent Performance Tuning
```yaml
datadog:
  # Limit log collection rate
  logs:
    containerCollectAll: true
    containerCollectUsingFiles: true
  
  # Process monitoring limits
  processAgent:
    enabled: true
    processCollection: true
    # Limit process collection
    maxProcesses: 200
  
  # DogStatsD configuration
  dogstatsd:
    port: 8125
    nonLocalTraffic: true
    originDetection: true
```

---

## Common Queries

### Host Overview
```sql
avg:system.cpu.user{*} by {host}
avg:system.mem.used{*} by {host}
avg:system.load.1{*} by {host}
```

### Disk Usage Alert
```sql
avg:system.disk.in_use{*} by {host,device} > 0.85
```

### High Memory Usage
```sql
avg:system.mem.pct_usable{*} by {host} < 0.1
```
