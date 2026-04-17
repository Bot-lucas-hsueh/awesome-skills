# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Shards exceeding 50GB** | High | Implement ILM with rollover at 50GB |
| 2 | **Too many shards per node** | High | Target <20 shards per GB heap |
| 3 | **Mapping explosions** | High | Use dynamic templates with keyword type for IDs |
| 4 | **Searching across too many indices** | Medium | Use index aliases with date math pattern |
| 5 | **Ignoring circuit breakers** | High | Pre-size queries, use `track_total_hits: false` when possible |
| 6 | **Running Elasticsearch as root** | High | Always run as non-root user |
| 7 | **No ILM policy** | Medium | Define lifecycle management from day one |
| 8 | **Sending unstructured logs** | Medium | Standardize on JSON/ECS format |
| 9 | **Missing rollover alias setup** | Medium | Use `is_write_index: true` on write alias |
| 10 | **Not monitoring the monitoring** | Medium | Monitor disk, heap, CPU of ES cluster itself |

## 10.2 Indexing Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| `refresh_interval: -1` on write-heavy index | Data not visible until explicit refresh | Use `_refresh?wait_for=true` only when needed |
| Bulk indexing without backpressure | Memory exhaustion, 429 errors | Implement exponential backoff in client |
| Not using pipelined bulk requests | Reduced throughput | Enable `piped` bulk format |
| Sending single-document bulks | Maximum overhead | Batch 1000-5000 docs per bulk |
| Ignoring 409 conflict responses | Data loss potential | Use versioning or optimistic concurrency |

## 10.3 Query Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| `match_all` with high `from`/`size` | Deep pagination memory issues | Use `search_after` for deep pagination |
| Aggregating on `text` fields | Uses fielddata, very slow | Use `.keyword` subfield or fix mapping |
| Wildcard at start of query | Forces full scan | Use prefix queries or autocomplete |
| High cardinality terms aggregation | OOM on large cardinalities | Use `composite` aggregation with pagination |
| `script` in filter context | Cannot use cache | Use `script` only in `must`/`should` |

## 10.4 Best Practices

1. **Use Index Lifecycle Management (ILM)** from the start
2. **Prefer keyword fields** over text for filtering and aggregations
3. **Keep shard size between 10-50GB** for optimal search performance
4. **Use the ILP (Ingest Node Pipeline)** for document enrichment
5. **Configure circuit breakers** to prevent OOM
6. **Use cross-cluster search** for multi-tenant or federated searches
7. **Enable TLS everywhere** in production
8. **Use API keys over basic auth** for programmatic access
9. **Implement snapshot lifecycle management** (SLM) for backups
10. **Follow ECS (Elastic Common Schema)** for field naming consistency

## 10.5 Logstash Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Single-threaded filter | Low throughput | Increase `pipeline.workers` and `pipeline.batch.size` |
| Complex Ruby in filter | CPU bottleneck | Use native filters, reserve Ruby for complex logic |
| No Dead Letter Queue | Lost events on failures | Always configure DLQ in production |
| Using `file` input in production | Inefficient, loses state | Use Beats or Kafka as input |
| Not cleaning up old data | Disk space exhaustion | Set retention policies, use ILM |
| Debug logging in production | Performance degradation | Set `log.level: info` in production |

## 10.6 Kibana Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Too many visualizations per dashboard | Slow load times | Split into multiple dashboards |
| Long date ranges on large indices | Timeout errors | Use narrower time ranges or apply filters |
| Canvas with live data | Performance issues | Use refresh intervals appropriately |
| Saving sensitive data in dashboards | Security risk | Use encrypted saved objects |
| Not pinning time filter | Confusion across users | Pin frequently used time ranges |

## 10.7 Security Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Security disabled in production | Data exposure | Always enable security |
| Admin role for application service accounts | Privilege escalation | Use minimal required roles |
| Storing credentials in plaintext configs | Credential theft | Use keystore or secrets management |
| No IP allowlisting | Unauthorized access | Configure `xpack.security.transport.filter.allowlist` |
| Sharing API keys across services | Audit trail loss | One key per service with descriptive name |
| Not rotating credentials | Long-term exposure | Rotate API keys every 90 days |

## 10.8 Capacity Planning Mistakes

| Mistake | Impact | Prevention |
|---------|--------|------------|
| Not planning for index replica overhead | Underestimated storage | Plan 2-3x primary size for replicas |
| Ignoring mapping overhead | Out of memory | Small field mappings, disable `_source` when safe |
| Single hot node with many warm nodes | Write bottleneck | Distribute hot nodes based on write volume |
| Not leaving headroom for snapshots | Disk full on backup | Keep 20% disk free for snapshots |
| Ignoring document churn rate | Write throttling | Model ingestion rate and shard allocation |
