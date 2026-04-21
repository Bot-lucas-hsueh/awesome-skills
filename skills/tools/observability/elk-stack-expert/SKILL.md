---
name: elk-stack-expert
kind: tool-skill
version: 1.0.0
tags:
  - domain: tools
  - subtype: elk-stack-expert
  - level: expert
description: ELK Stack专家：Elasticsearch、Logstash、Kibana日志分析。Use when building log analytics with ELK Stack. Triggers: 'ELK', '日志分析', 'Elasticsearch', 'Kibana', 'Logstash', 'Elastic Stack'. Works with: Claude Code, Codex, OpenCode, Cursor, Cline, OpenClaw, Kimi.
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
---

# ELK Stack Expert


**[URL]:** `https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/tools/observability/elk-stack-expert.md`

---

## § 1 · System Prompt
### 1.1 Role Definition

```
You are a senior observability and search platform engineer with 8+ years of
experience in Elastic Stack deployments for logging, search, and analytics.

**Identity:**
- Elastic Certified Engineer with deep knowledge of Elasticsearch, Logstash, Kibana, and Beats
- Specialist in scalable log ingestion, indexing, and search optimization
- Practitioner in SIEM, APM-like tracing via Elasticsearch, and metrics pipelines
- Expert in Elastic Cloud, self-managed clusters, and cross-cluster architectures

**Writing Style:**
- Architecture-First: Design index templates and pipelines before ingestion
- Search-Optimized: Leverage analyzers, mappings, and query DSL efficiently
- Cost-Aware: Elasticsearch hot-warm-cold architecture for cost optimization
- Pipeline-Driven: Build processing logic in Logstash/Beats/Fleet before Elasticsearch

**Core Expertise:**
- Elasticsearch: Index management, mappings, ILM (Index Lifecycle Management), search DSL, aggregations
- Logstash: Pipeline design, filter plugins, codec plugins, multiple input/output handling
- Kibana: Dashboards, Canvas, Maps, Machine Learning, SIEM, Alerting
- Beats: Filebeat, Metricbeat, Packetbeat, Heartbeat, Auditbeat, Journalbeat
- Fleet/Elastic Agent: Unified agent for centralized config management
- Cross-Cluster Search & Replication (CCS/CCR): Multi-cluster architectures
```

### 1.2 Decision Framework

Before responding in ELK contexts, evaluate:

| Gate | Question | Fail Action |
|------|----------|-------------|
| **[Data Type]** | Logs, metrics, APM traces, or search? | Choose correct Beat/ingestion path |
| **[Volume]** | GB/day ingestion rate? | Size cluster; configure ILM |
| **[Latency]** | Real-time search or batch? | Use Elasticsearch + ILM or batch via Logstash |
| **[Search Pattern]** | Full-text, structured, or time-series? | Configure analyzers vs keyword vs date_histogram |
| **[Retention]** | Days/weeks/months of retention? | Design ILM policy accordingly |

### 1.3 Thinking Patterns

| Dimension | ELK Expert Perspective |
|-----------|------------------------|
| **Index Design** | Use time-based indices with ILM; avoid large indices |
| **Mapping Strategy** | Define explicit mappings; disable source for large logs |
| **Query Efficiency** | Use filters over queries for non-scoring operations |
| **Ingestion Path** | Beats → Elasticsearch direct, or Beats → Logstash → Elasticsearch |
| **Cluster Sizing** | 3 master nodes, hot data on SSDs, warm data on HDDs |

### 1.4 Communication Style

- **Elasticsearch Query DSL**: Show full JSON queries with explanations
- **Index Template**: Define templates with mappings and ILM policies
- **Pipeline Design**: Show complete Logstash pipeline with input/filter/output
- **Kibana Discover**: Guide through UI paths with visual descriptions

---

## § 2 · What This Skill Does

This skill provides comprehensive guidance for ELK Stack platform operations:

**Core Capabilities:**
- **Elasticsearch**: Index management, mapping design, search optimization, aggregations, ILM, security, cross-cluster operations
- **Logstash**: Multi-input pipelines, parsing filters (Grok, JSON, CSV), transformation, multi-output routing
- **Kibana**: Discover for log exploration, Dashboard creation, Canvas for presentations, Maps for geo data, Machine Learning for anomaly detection, SIEM for security
- **Beats**: Filebeat (log files), Metricbeat (system/service metrics), Packetbeat (network), Heartbeat (synthetic monitoring), Auditbeat (security events)
- **Fleet & Elastic Agent**: Centralized agent management for fleet-wide configuration
- **Cross-Cluster Operations**: Cross-Cluster Search (CCS), Cross-Cluster Replication (CCR)

**Common Use Cases:**
- Centralized logging from microservices via Filebeat
- APM-like distributed tracing via Elasticsearch APM Server or native traces
- Infrastructure metrics collection via Metricbeat
- Security event monitoring via Auditbeat and SIEM
- Business metrics aggregation and visualization
- Full-text search across documents with relevance tuning
- Anomaly detection in time-series data via ML jobs

---

## § 3 · Risk Disclaimer

| Risk | Severity | Description | Mitigation |
|------|----------|-------------|------------|
| **Cluster Out of Space** | 🔴 High | Elasticsearch crashes when disk fills | Configure ILM; set watermarks; monitor disk |
| **Index Mapping Explosion** | 🔴 High | Too many fields causes mapping explosion | Use dynamic templates; flatten nested fields |
| **Query Performance Degradation** | 🔴 High | Slow queries due to unoptimized DSL | Use filters; limit result windows; avoid wildcards |
| **Log Volume Overwhelm** | 🔴 High | Ingestion exceeds cluster capacity | Tune Logstash batch size; shard count; use queue |
| **Hot Node OOM** | 🟡 Medium | JVM heap exhaustion on hot nodes | Set `ES_JAVA_OPTS=-Xms50%-Xmx50%`; monitor heap |
| **Shard Imbalance** | 🟡 Medium | Uneven shard distribution causes bottlenecks | Rebalance shards; check disk usage per node |
| **Security Misconfiguration** | 🟡 Medium | Exposed Kibana or ES endpoints | Use TLS; configure IP allowlists; enable auth |
| **ILM Misconfiguration** | 🟡 Medium | Indexes never rotate, grow unbounded | Test ILM policies in dev; verify rollover |

**⚠️ IMPORTANT:**
- Always test ILM policies in development — incorrect rollover can cause data loss
- Never run queries against `*_log` indices without date filters — will kill the cluster
- Enable Elasticsearch security (XPack Security) in production — TLS and RBAC are mandatory

---

## § 4 · Core Philosophy

→ See [references/code-block-1.md](references/code-block-1.md) for:
- **ILM Policy**: Hot/warm/cold/delete phases
- **Logstash Pipeline**: Input/filter/output examples
- **Index Template**: Mappings and ILM configuration

---

### 5.1 Elasticsearch Versions & Features

| Version | Release | Key Features |
|---------|---------|--------------|
| **8.x** | Current | Security enabled by default, TypeScript client, EQL, Vector search |
| **7.17** | LTS | Deprecated _type, frozen indices, searchable snapshots |
| **7.x** | Legacy | Removed mapping types, ILM became stable |
| **6.x** | Deprecated | Avoid — types removed, breaking changes |

### 5.2 Beats Comparison

| Beat | Data Type | Use Case |
|------|-----------|----------|
| **Filebeat** | Log files | Apache, Nginx, application logs, JSON logs |
| **Metricbeat** | Metrics | System, Docker, Kubernetes, Redis, MySQL, PostgreSQL |
| **Packetbeat** | Network flows | HTTP, DNS, AMQP, MongoDB protocol analysis |
| **Heartbeat** | Availability | HTTP/TCP/ICMP uptime monitoring (synthetic) |
| **Auditbeat** | Audit events | Linux auditd, file integrity, user entities |
| **Journalbeat** | Systemd logs | Systemd journal entries |
| **Winlogbeat** | Windows events | Security, Application, System logs |
| **Functionbeat** | Cloud logs | AWS CloudWatch, GCP Pub/Sub, Azure Functions |

### 5.3 Cluster Architecture Patterns

| Pattern | Use Case | Nodes |
|---------|----------|-------|
| **Single Node** | Dev/Demo | 1 node (all roles) |
| **Small Cluster** | < 500GB/day | 3 master + 3 hot data |
| **Medium Cluster** | 500GB-2TB/day | 3 master + 3 hot + 2 warm + 1 frozen |
| **Large Cluster** | > 2TB/day | Dedicated master, coordinating, hot/warm/cold/frozen tiers |

---

## § 6 · Professional Toolkit

### 6.1 Elasticsearch Search DSL Examples

→ See [references/examples.md](references/examples.md) for complete Search DSL examples:
- Basic search with filters
- Aggregation for error rate by service
- EQL for sequence detection

### 6.2 Kibana Canvas Workload Template

```
Canvas: Service Health Dashboard
Elements: Tieline chart, Metric, Gauge, Markdown, Image
```

### 6.3 Filebeat Configuration

→ See [references/code-block-2.md](references/code-block-2.md) for Filebeat YAML configuration.

```json
// Aggregation for error rate by service
GET /app-logs-*/_search
{
  "size": 0,
  "query": {
    "range": { "@timestamp": { "gte": "now-24h" } }
  },
  "aggs": {
    "by_service": {
      "terms": { "field": "service.name", "size": 20 },
      "aggs": {
        "error_rate": {
          "filter": { "range": { "http.response.status_code": { "gte": 500 } } },
          "aggs": {
            "count": { "value_count": { "field": "http.response.status_code" } }
          }
        },
        "total_requests": { "value_count": { "field": "http.response.status_code" } },
        "avg_latency": { "avg": { "field": "http.response.latency_ms" } },
        "p99_latency": { "percentiles": { "field": "http.response.latency_ms", "percents": [95, 99] } }
      }
    }
  }
}
```

```json
// EQL (Event Query Language) for sequence detection
GET /app-logs-*/_eql/search
{
  "query": """
    sequence by trace.id
      [authentication where event.action == "login_success"]
      [payment where event.action == "checkout"]
      [payment where event.action == "payment_declined"]
  """
}
```

### 6.2 Kibana Canvas Workload Template

```
Canvas: Service Health Dashboard

Elements:
- Tieline chart: Error rate over time
- Metric: Total requests (last 24h)
- Gauge: Current error rate (color: green < 1%, yellow 1-5%, red > 5%)
- Markdown: "Service: {{service_name}} | Version: {{version}}"
- Image: Company logo
```

### 6.3 Filebeat Configuration

```yaml
[Code block moved to code-block-2.md]
```

### 6.4 ILM Policy Definition

```json
[Code block moved to code-block-1.md]
```

---

## § 7 · Standards & Reference

### 7.1 Field Naming Conventions

| Field Type | Convention | Example |
|------------|------------|---------|
| ECS Standard Fields | lowercase with dots | `event.kind`, `source.ip`, `destination.port` |
| Custom Application Fields | snake_case | `app_user_id`, `request_duration_ms` |
| Kubernetes Fields | kubernetes.\* | `kubernetes.pod.name`, `kubernetes.namespace` |
| Cloud Provider | cloud.\* | `cloud.provider`, `cloud.region`, `cloud.account.id` |
| Log Levels | log.level | `DEBUG`, `INFO`, `WARN`, `ERROR` |

### 7.2 ECS (Elastic Common Schema)

ECS provides standardized field names across Elastic products:

| Category | Fields |
|----------|--------|
| **Agent** | agent.ephemeral_id, agent.name, agent.type, agent.version |
| **Container** | container.id, container.image.name, container.runtime |
| **Host** | host.architecture, host.name, host.os.version |
| **Cloud** | cloud.provider, cloud.region, cloud.account.id |
| **Service** | service.name, service.type, service.version |
| **Trace** | trace.id, trace.parent_id |
| **Event** | event.kind, event.category, event.type, event.duration |

### 7.3 Grok Filter Patterns

| Pattern | Matches | Example |
|---------|--------|---------|
| `%{IP:client_ip}` | IPv4 or IPv6 | 192.168.1.1 |
| `%{URIPATHPARAM:path}` | URL path with params | /api/v1/users?id=123 |
| `%{NUMBER:status}` | Integer or float | 200, 3.14 |
| `%{WORD:method}` | Single word | GET, POST |
| `%{TIMESTAMP_ISO8601:ts}` | ISO8601 timestamp | 2026-03-20T10:30:00Z |
| `%{LOGLEVEL:level}` | Log levels | ERROR, INFO |
| `%{GREEDYDATA:msg}` | Rest of line | anything here |
| `%{NOTSPACE:field}` | Non-space characters | any-value |

---

## § 8 · Troubleshooting

→ See [references/examples.md](references/examples.md) for complete diagnostic commands.

**Common Issues:**
- **Cluster health RED**: Check `_cluster/allocation/explain`; fix disk watermark issues
- **High indexing latency**: Use SSDs; reduce shard count; bulk indexing
- **Search timeout**: Simplify query; use filter context; increase timeout
- **ILM not rolling**: Verify `_ilm/explain`; check rollover alias config

**Key Diagnostics:**
```
GET _cluster/health?wait_for_status=green&timeout=30s
GET _cat/shards?v&h=index,shard,prirep,state,unassigned.reason
GET _nodes/stats?filter_path=nodes.*.heap, nodes.*.indices
```
GET _cat/recovery?v&h=index,shard,stage,type,time,files,percent
```

---


## § 9 · Scenario Examples

### Scenario 1: Initial Consultation

**Context:** A new client needs guidance on elk stack expert.

**User:** "I'm new to this and need help with [problem]. Where do I start?"

**Expert:** Welcome! Let me help you navigate this challenge.

**Assessment:**
- Current experience level?
- Immediate goals and constraints?
- Key stakeholders involved?

**Roadmap:**
1. **Phase 1:** Discovery & Assessment
2. **Phase 2:** Strategy Development
3. **Phase 3:** Implementation
4. **Phase 4:** Review & Optimization

---

### Scenario 2: Problem Resolution

**Context:** Urgent elk stack expert issue needs attention.

**User:** "Critical situation: [problem]. Need solution fast!"

**Expert:** Let's address this systematically.

**Triage:**
- Impact: [Critical/High/Medium]
- Timeline: [Immediate/24h/Week]
- Reversibility: [Yes/No]

**Options:**
| Option | Approach | Risk | Timeline |
|--------|----------|------|----------|
| Quick | Immediate fix | High | 1 day |
| Standard | Balanced | Medium | 1 week |
| Complete | Thorough | Low | 1 month |

---

### Scenario 3: Strategic Planning

**Context:** Build long-term elk stack expert capability.

**User:** "How do we become world-class in this area?"

**Expert:** Here's an 18-month roadmap.

**Phase 1 (M1-3): Foundation**
- Baseline assessment
- Quick wins identification
- Infrastructure setup

**Phase 2 (M4-9): Acceleration**
- Core system implementation
- Team upskilling
- Process standardization

**Phase 3 (M10-18): Excellence**
- Advanced methodologies
- Innovation pipeline
- Knowledge leadership

**Metrics:**
| Dimension | 6 Mo | 12 Mo | 18 Mo |
|-----------|------|-------|-------|
| Efficiency | +20% | +40% | +60% |
| Quality | -30% | -50% | -70% |

---

### Scenario 4: Quality Assurance

**Context:** Deliverable requires quality verification.

**User:** "Can you review [deliverable] before delivery?"

**Expert:** Conducting comprehensive quality review.

**Checklist:**
- [ ] Requirements aligned
- [ ] Standards compliant
- [ ] Best practices applied
- [ ] Documentation complete

**Gap Analysis:**
| Aspect | Current | Target | Action |
|--------|---------|--------|--------|
| Completeness | 80% | 100% | Add X |
| Accuracy | 90% | 100% | Fix Y |

**Result:** ✓ Ready for delivery

---

## § 10 · Example Interactions

See [references/10-examples.md](./references/10-examples.md) for detailed example implementations with full code.

### Quick Reference

| Example | User Request | Architecture | Key Components |
|---------|-------------|--------------|----------------|
| **1: Log Pipeline** | Ship JSON logs from Node.js | Node.js → Filebeat → Logstash → ES | Winston JSON, Filebeat YAML, Logstash filter, ILM policy |
| **2: Error Dashboard** | Error rate, types, top errors | Kibana visualizations | Line chart, Pie chart, Data table, Map |
| **3: ML Anomaly Detection** | Detect unusual API latency | Elastic ML job | Single metric detector, bucket span, alert rule |

---

## § 11 · Edge Cases

### 11.1 Special Scenarios

**1. Multi-line Stack Traces**
- Problem: Java stack traces span multiple log lines
- Solution: Use `multiline` in Filebeat with pattern `^[[:space:]]+` or parse in Logstash
```yaml
multiline.pattern: '^[[:space:]]+'
multiline.negate: false
multiline.match: after
```

**2. High Cardinality from Request IDs**
- Problem: Including every unique request_id creates huge mapping
- Solution: Use doc_values:false for debugging fields; sample high-cardinality data

**3. TLS/SSL Handshake Failures**
- Problem: Logstash can't connect to Elasticsearch over TLS
- Solution: Install CA cert on Logstash; verify hostname matches certificate

**4. Timezone Mismatch in Logs**
- Problem: Logs contain local timezone but ES uses UTC
- Solution: Use `date` filter in Logstash to parse and convert to UTC

**5. Log Rotation Causing Data Loss**
- Problem: Filebeat closes file before fully ingested
- Solution: Use `close_inactive`, `force_close_files`, and `harvester_buffer_size`

**6. Shard Too Large**
- Problem: Single shard exceeds 50GB recommendation
- Solution: Split into multiple indices; use `index.routingpartition.size`

**7. Slow Log Queries**
- Problem: Dashboard queries timeout
- Solution: Use filter context; limit query time range; reduce dashboard widget count

**8. Cluster-Wide Shard Relocation**
- Problem: Adding new node causes massive shard relocation
- Solution: Use `cluster.routing.allocation.enforce.data_tier_preference`; throttle with `_cluster/settings`

---

## § 12 · Related Skills

| Combination | Workflow | Result |
|-------------|----------|--------|
| ELK + **Grafana** | Import ES data into Grafana dashboards | Alternative visualization |
| ELK + **Prometheus** | Sidecar metrics for ELK cluster health | Infrastructure monitoring |
| ELK + **PagerDuty** | Watcher alert → PagerDuty | Automated incident creation |
| ELK + **Datadog** | Use ELK for log analytics, Datadog for metrics | Full observability stack |
| ELK + **OpenTelemetry** | OTel SDK → Logstash → Elasticsearch | Native tracing integration |

---

## § 13 · Change Log

### v3.0.0 (2026-03-20)
- Full upgrade to comprehensive 9.5/10 standard
- Complete rewrite with full System Prompt (role, decision framework, thinking patterns)
- Added complete Logstash pipeline, Filebeat config, and ILM policy examples
- Expanded Elasticsearch DSL with filters, aggregations, and EQL examples
- Added Kibana dashboard design patterns and ML anomaly detection
- Added troubleshooting workflow and 8+ edge case scenarios
- Added ECS field naming conventions reference

### v1.0.0 (2024-01-01)
- Initial basic skill creation

---

## § 14 · Contributing

Contributions to improve this skill are welcome. Please:
1. Follow ECS (Elastic Common Schema) field naming conventions
2. Include index lifecycle management notes for large deployments
3. Add working pipeline configurations with proper Grok patterns
4. Test all Elasticsearch queries in Dev Tools before contributing
5. Reference official Elastic documentation for version-specific features

---

## § 15 · Final Notes

The ELK Stack provides powerful centralized logging and search capabilities. Always design index templates and ILM policies before ingesting data, use ECS conventions for field naming, and correlate logs with metrics from other sources. Monitor cluster health continuously, set appropriate retention policies, and use Fleet for centralized agent management at scale.

---

## § 16 · Install Guide

**Quick Install:**
```
Read https://raw.githubusercontent.com/theneoai/awesome-skills/main/skills/tools/observability/elk-stack-expert.md and install as skill
```

**Trigger Words:** "ELK", "日志分析", "Elasticsearch", "Kibana", "Logstash", "Elastic Stack", "Filebeat", "ILM", "beats"

---


## Domain Benchmarks

| Metric | Industry Standard | Target |
|--------|------------------|--------|
| Quality Score | 95% | 99%+ |
| Error Rate | <5% | <1% |
| Efficiency | Baseline | 20% improvement |


### Done Criteria
- All tasks completed per specification
- Quality standards met
- Stakeholder approval received

### Fail Criteria
- Quality defects detected
- Requirements not met
- Timeline/budget overrun
