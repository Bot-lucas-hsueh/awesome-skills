# Scenario Examples

## 9.1 Centralized Application Logging

**User:** "Our microservices are generating logs in different formats across 12 servers. How do we centralize them in ELK?"

**Expert:**
> **Solution:**
>
> 1. Deploy **Filebeat** on each server as a DaemonSet (Kubernetes) or service
> 2. Configure multiline handling for stack traces
> 3. Add `add_host_metadata`, `add_cloud_metadata` processors
> 4. Ship directly to Logstash or Elasticsearch via Fleet
>
> ```yaml
> # filebeat.yml
> filebeat.inputs:
>   - type: log
>     enabled: true
>     paths:
>       - /var/log/myapp/*.log
>     multiline.type: pattern
>     multiline.pattern: '^\d{4}-\d{2}-\d{2}'
>     multiline.negate: true
>     multiline.match: after
>     fields:
>       service: myapp
>       environment: production
>     fields_under_root: true
>
> processors:
>   - add_host_metadata:
>       when.not.contains.tags: forwarded
>   - add_cloud_metadata: ~
>   - add_docker_metadata: ~
>
> output.logstash:
>   hosts: ["logstash.example.com:5044"]
> ```

## 9.2 Observability: Correlating Logs, Metrics, and Traces

**User:** "How do we correlate APM traces with logs and infrastructure metrics in the ELK stack?"

**Expert:**
> **Solution with Elastic Agent and APM:**
>
> 1. Deploy **Elastic Agent** via Fleet for unified data collection
> 2. Enable **APM Server** integration for distributed tracing
> 3. Use `service.transaction.id` and `trace.id` fields to link spans to logs
> 4. Enable **Logs app** correlation with APM in Kibana
>
> ```json
> // Log format with trace correlation
> {
>   "message": "Request processed",
>   "service.name": "order-service",
>   "trace.id": "abc123",
>   "transaction.id": "xyz789",
>   "span.id": "spn456",
>   "event.duration": 145
> }
> ```
>
> **Kibana Correlation:** Open Logs app, click "Correlate" on a log entry to see the APM trace timeline and host metrics.

## 9.3 Security: Threat Detection with SIEM

**User:** "How do we use ELK for security monitoring and threat detection?"

**Expert:**
> **Elastic Security Setup:**
>
> 1. Enable **Security app** in Kibana (replaces SIEM app in 8.x)
> 2. Enable **Elastic Agent** integration policies for:
>    - **Endpoint Security** (Windows Defender, macOS)
>    - **Network** (Zeek, Suricata, DNS logs)
>    - **System** (Auditbeat, Linux auditd)
> 3. Use prebuilt **detection rules** from Elastic Security
> 4. Create custom rules with EQL queries
>
> ```json
> // EQL sequence detection for lateral movement
> sequence by host.id, source.ip max spans between 2m
>   [ authentication where event.action == "logon" and event.outcome == "success" ]
>   [ network where event.action == "connection" and destination.port in (3389, 22, 445) ]
> ```
>
> **Reference:** [Elastic Security documentation](https://www.elastic.co/guide/en/security/current/index.html)

## 9.4 Performance: Hot-Warm-Cold Architecture

**User:** "We have 10TB of log data daily and can't afford all-flash storage. How do we tier it?"

**Expert:**
> **Hot-Warm-Cold Setup:**
>
> ```ruby
> # pipeline.conf with index routing
> input { beats { port => 5044 } }
>
> output {
>   if [@metadata][tier] == "hot" {
>     elasticsearch {
>       hosts => ["hot-node:9200"]
>       index => "logs-%{[@metadata][log_type]}-hot-%{+YYYY.MM.dd}"
>     }
>   }
>   if [@metadata][tier] == "warm" {
>     elasticsearch {
>       hosts => ["warm-node:9200"]
>       index => "logs-%{[@metadata][log_type]}-warm-%{+YYYY.MM.dd}"
>     }
>   }
> }
> ```
>
> **Index lifecycle policy:**
> - **Hot**: 0-7 days (50GB shard or 7-day rollover)
> - **Warm**: 7-30 days (read-only, force merge)
> - **Cold**: 30-90 days (searchable snapshots, reduced replica count)
> - **Delete**: >90 days
>
> ```json
> PUT _ilm/policy/hot-warm-delete
> {
>   "policy": {
>     "phases": {
>       "hot": {
>         "min_age": "0ms",
>         "actions": {
>           "rollover": { "max_age": "7d", "max_primary_shard_size": "50gb" },
>           "set_priority": 100
>         }
>       },
>       "warm": {
>         "min_age": "7d",
>         "actions": {
>           "set_priority": 50,
>           "shrink": { "number_of_shards": 1 },
>           "forcemerge": { "max_num_segments": 1 }
>         }
>       },
>       "cold": {
>         "min_age": "30d",
>         "actions": {
>           "set_priority": 0,
>           "allocate": { "number_of_replicas": 0 }
>         }
>       },
>       "delete": {
>         "min_age": "90d",
>         "actions": { "delete": {} }
>       }
>     }
>   }
> }
> ```

## 9.5 Troubleshooting: High JVM Memory Pressure

**User:** "Our Elasticsearch nodes are hitting high JVM memory pressure (>85%) constantly. How do we diagnose?"

**Expert:**
> **Diagnosis Steps:**
>
> 1. **Check current heap usage:**
> ```
> GET _nodes/stats/jvm?filter_path=nodes.*.jvm.mem.heap_used_in_bytes,nodes.*.jvm.mem.heap_max_in_bytes
> ```
>
> 2. **Identify large indices/shards:**
> ```
> GET _cat/shards?v&h=index,shard,prirep,state,store.size,docs,heap.size
> GET _cat/indices?v&h=index,docs.count,store.size,pri,rep,health
> ```
>
> 3. **Common causes:**
>    - **Too many shards per node** (rule: < 20 shards per GB heap)
>    - **Large fielddata** from high-cardinality keywords
>    - **Heavy aggregations** on unfiltered queries
>    - **Fielddata circuit breaker** tripping
>
> 4. **Remediation:**
> ```bash
> # Reduce shard count by merging indices
> POST /old-index/_shrink/target-index

> # Clear fielddata cache
> POST _cache/clear?fielddata=true

> # Increase heap (but keep < 32GB for compressed oops)
> -Xms16g -Xmx16g

> # Monitor circuit breaker
> GET _cluster/stats?filter_path=circuit_breaker*
> ```
>
> **Reference:** [JVM settings documentation](https://www.elastic.co/guide/en/elasticsearch/reference/current/jvm.html)

## 9.6 Data Pipeline: Kafka to Elasticsearch

**User:** "How do we stream data reliably from Kafka into Elasticsearch with exactly-once semantics?"

**Expert:**
> **Logstash Kafka Input with Dead Letter Queue:**
>
> ```ruby
> input {
>   kafka {
>     bootstrap_servers => "kafka1:9092,kafka2:9092"
>     topics => ["events", "transactions"]
>     group_id => "logstash-consumers"
>     offset_reset => "earliest"
>     enable_auto_commit => false
>     consumer_threads => 4
>     max_poll_records => "500"
>     decorate_events => true
>     codec => json
>   }
> }
>
> filter {
>   mutate {
>     add_field => { "[@metadata][kafka_partition]" => "%{[@metadata][kafka_partition]}" }
>     add_field => { "[@metadata][kafka_offset]" => "%{[@metadata][kafka_offset]}" }
>   }
> }
>
> output {
>   elasticsearch {
>     hosts => ["es1:9200", "es2:9200"]
>     index => "kafka-events-%{+YYYY.MM.dd}"
>     action => "create"
>     pipeline => "enrichment-pipeline"
>     retry_on_conflict => 3
>   }
>
>   dead_letter_queue {
>     path => "/var/lib/logstash/dead_letter_queue"
>     commit_offsets => true
>   }
> }
> ```
>
> **Dead Letter Queue handling:**
> ```bash
> # Inspect DLQ
> ls /var/lib/logstash/dead_letter_queue/

> # Reprocess from DLQ
> bin/logstash -f dlq-pipeline.conf
> ```
