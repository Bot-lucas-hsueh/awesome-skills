# Datadog Log Management Reference

> Comprehensive guide to log collection, processing, and analysis

---

## Log Collection Methods

### Agent-Based Collection

**File Tailing:**
```yaml
# datadog.yaml
logs:
  enabled: true
  configs:
    - type: file
      path: /var/log/app/*.log
      service: payment-api
      source: python
      tags:
        - env:production
        - team:payments
      
    - type: file
      path: /var/log/nginx/access.log
      service: nginx
      source: nginx
      log_processing_rules:
        - type: exclude_at_match
          name: exclude_health_checks
          pattern: 'GET /health'
```

**Docker Integration:**
```yaml
logs:
  enabled: true
  container_collect_all: true
  
  # Or label-based selection
  container_collect_all: false
```

```bash
# Docker labels for log configuration
docker run -l "com.datadoghq.ad.logs=[{\"source\": \"python\", \"service\": \"my-app\"}]" my-image
```

### API Ingestion
```bash
# Direct log submission
curl -X POST "https://http-intake.logs.datadoghq.com/v1/input" \
  -H "Content-Type: application/json" \
  -H "DD-API-KEY: ${DD_API_KEY}" \
  -d '{
    "message": "User login successful",
    "service": "auth-service",
    "ddsource": "custom",
    "ddtags": "env:production,user_id:12345",
    "hostname": "auth-server-01"
  }'
```

### Cloud Provider Forwarding

**AWS S3 Forwarding:**
```hcl
resource "aws_lambda_function" "datadog_log_forwarder" {
  function_name = "datadog-log-forwarder"
  runtime       = "python3.9"
  handler       = "lambda_function.lambda_handler"
  
  environment {
    variables = {
      DD_API_KEY = var.datadog_api_key
      DD_SITE    = "datadoghq.com"
    }
  }
}

resource "aws_s3_bucket_notification" "logs" {
  bucket = aws_s3_bucket.logs.id
  
  lambda_function {
    lambda_function_arn = aws_lambda_function.datadog_log_forwarder.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "logs/"
  }
}
```

---

## Log Processing

### Grok Parsing
```yaml
# Custom parsing rule
- type: grok
  name: parse_custom_app_logs
  pattern: '%{TIMESTAMP_ISO8601:timestamp} %{LOGLEVEL:level} %{DATA:logger} - %{GREEDYDATA:message}'
  source: message
  
  # Extracted attributes will be:
  # - timestamp: 2024-01-15T10:30:00Z
  # - level: ERROR
  # - logger: payment.processor
  # - message: Payment failed for order #12345
```

### Pipeline Configuration
```yaml
# Log pipeline via API
name: "Payment Service Pipeline"
filter:
  query: "source:python service:payment-api"

processors:
  - type: grok-parser
    name: "Parse Application Logs"
    source: message
    grok:
      match_rules: |
        payment %{TIMESTAMP_ISO8601:timestamp} %{WORD:level} Payment %{WORD:status} for order %{NUMBER:order_id}, amount: %{NUMBER:amount:float}
  
  - type: status-remapper
    name: "Map Log Level"
    sources:
      - level
  
  - type: date-remapper
    name: "Map Timestamp"
    sources:
      - timestamp
  
  - type: attribute-remapper
    name: "Remap Order ID"
    sources:
      - order_id
    target: order.id
    target_type: attribute
  
  - type: arithmetic-processor
    name: "Calculate in Cents"
    expression: "amount * 100"
    target: amount_cents
    replace_missing: false
```

### Sensitive Data Scanning
```yaml
# Built-in scanning rules
- type: sensitive_data_scanner
  name: "Credit Card Detection"
  pattern: "\\b4[0-9]{12}(?:[0-9]{3})?\\b"
  replacement: "[CREDIT_CARD_REDACTED]"
  
- type: sensitive_data_scanner
  name: "SSN Detection"
  pattern: "\\b\\d{3}-\\d{2}-\\d{4}\\b"
  replacement: "[SSN_REDACTED]"
  
- type: sensitive_data_scanner
  name: "API Key Detection"
  pattern: "(api[_-]?key[\\s]*[:=][\\s]*)([a-zA-Z0-9]{32,})"
  replacement: "$1[API_KEY_REDACTED]"
```

---

## Log Metrics

### Generate Metrics from Logs
```hcl
resource "datadog_logs_metric" "payment_errors" {
  name = "payment.errors.count"
  
  compute {
    aggregation_type = "count"
  }
  
  filter {
    query = "service:payment-api status:error"
  }
  
  group_by {
    path     = "order.type"
    tag_name = "order_type"
  }
  
  group_by {
    path     = "customer.tier"
    tag_name = "customer_tier"
  }
}

resource "datadog_logs_metric" "response_time" {
  name = "api.response.duration"
  
  compute {
    aggregation_type = "distribution"
    path             = "duration"
  }
  
  filter {
    query = "source:nginx"
  }
}
```

### Log-Based Alerts
```hcl
resource "datadog_monitor" "error_spike" {
  name = "Payment Error Spike"
  type = "log alert"
  
  query = <<-EOT
    logs("service:payment-api status:error").index("main").rollup("count").last("5m") > 50
  EOT
  
  thresholds {
    critical = 50
    warning  = 20
  }
  
  message = <<-EOT
    Error spike detected in payment service
    
    Error count: {{value}} in last 5 minutes
    
    View logs: https://app.datadoghq.com/logs?query=service:payment-api%20status:error
    
    @pagerduty-payments-oncall
  EOT
}
```

---

## Log Storage & Retention

### Indexes
```hcl
resource "datadog_logs_index" "production" {
  name = "production"
  
  filter {
    query = "env:production"
  }
  
  daily_limit = 1000000000  # 1TB
  
  exclusion_filter {
    name       = "Exclude Debug Logs"
    is_enabled = true
    filter {
      query       = "status:debug"
      sample_rate = 1.0
    }
  }
  
  exclusion_filter {
    name       = "Sample Verbose Logs"
    is_enabled = true
    filter {
      query       = "source:access_log"
      sample_rate = 0.1  # Keep 10%
    }
  }
}
```

### Archives
```hcl
resource "datadog_logs_archive" "s3_archive" {
  name = "S3 Archive"
  
  query = "*"
  
  s3_archive {
    bucket     = aws_s3_bucket.logs_archive.bucket
    path       = "/logs"
    account_id = data.aws_caller_identity.current.account_id
    role_name  = aws_iam_role.datadog_archive.name
  }
  
  include_tags = true
  tags = ["env:production", "compliance:required"]
  
  rehydration_tags = ["team:security"]
}
```

---

## Log Analytics

### Log Explorer Queries
```sql
-- Basic search
service:payment-api status:error

-- Structured query
@order.amount:>1000 @customer.tier:premium status:error

-- Time range
service:nginx @http.status_code:500 -@path:/health

-- Aggregation
source:nginx | count by @http.status_code

-- Top list
service:api | top @endpoint by count

-- Timeseries
service:payment-api status:error | timeseries count
```

### Pattern Analysis
```sql
-- Find common error patterns
service:payment-api status:error | patterns

-- Cluster similar logs
source:application status:error | cluster
```

---

## Best Practices

### Log Format Recommendation
```json
{
  "timestamp": "2024-01-15T10:30:00Z",
  "level": "ERROR",
  "message": "Payment processing failed",
  "service": "payment-api",
  "dd": {
    "trace_id": "123456789",
    "span_id": "987654321"
  },
  "attributes": {
    "order_id": "order-12345",
    "customer_id": "cust-67890",
    "amount": 99.99,
    "currency": "USD",
    "payment_method": "credit_card",
    "error": {
      "type": "PaymentDeclined",
      "code": "INSUFFICIENT_FUNDS",
      "message": "Card declined by issuer"
    }
  }
}
```

### Logging Levels Guide
| Level | Usage | Retention |
|-------|-------|-----------|
| DEBUG | Development troubleshooting | 7 days |
| INFO | Normal operations | 30 days |
| WARN | Unexpected but handled | 90 days |
| ERROR | Failures requiring attention | 1 year |
| CRITICAL | System-wide issues | 1 year |

### Cost Optimization
1. **Sampling** — Exclude or sample verbose logs
2. **Filtering** — Drop DEBUG logs in production
3. **Metrics Generation** — Convert high-volume logs to metrics
4. **Archiving** — Move old logs to S3
5. **Rehydration** — Only restore when needed

---

## Integration with APM

### Log-Trace Correlation
```python
import logging
from ddtrace import tracer

# Configure trace injection
from ddtrace.logging import format as dd_format

logging.basicConfig(
    format=dd_format,
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Logs will automatically include:
# - dd.trace_id
# - dd.span_id
# - dd.service
# - dd.env
# - dd.version

def process_order(order_id):
    logger.info(f"Processing order {order_id}")
    # Log appears in Datadog correlated with current trace
```

### Log Facets for Traces
```yaml
# Configure facets in Datadog UI
facets:
  - name: "Trace ID"
    path: "dd.trace_id"
    type: string
  
  - name: "Span ID"
    path: "dd.span_id"
    type: string
  
  - name: "Service"
    path: "dd.service"
    type: string
```
