# Common Pitfalls & Anti-Patterns

## 10.1 Query Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **`rate()` without `by` clause** | High | Always use `by` to group by relevant labels |
| 2 | **`sum(rate(...))` without grouping** | High | Use `sum by (label) (rate(...))` |
| 3 | **`histogram_quantile` without `by (le)`** | High | Must include `le` in `by` clause |
| 4 | **`topk()` without recording rule** | Medium | Use recording rules for complex topk |
| 5 | **Nested `rate()` calls** | Medium | Simplify: `rate(a)` not `rate(rate(a))` |
| 6 | **`count()` on gauge without aggregation** | Medium | Use `sum(count()) by (label)` |
| 7 | **Using `irate()` for slow queries** | Medium | Use `rate()` for dashboards, `irate()` only for spikes |
| 8 | **`on()` without `group_left/group_right`** | High | Specify many-to-one matching explicitly |

## 10.2 Label Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Label cardinality growing unbounded | Memory exhaustion | Limit label values, remove user IDs |
| Label name typos | Silent failures | Use consistent naming conventions |
| Using dynamic URLs as label values | Cardinality explosion | Hash or bucket the values |
| Missing critical labels | Poor correlation | Always include service, instance, job |
| Overlapping label sets | Query confusion | Use consistent label schemas |

## 10.3 Alerting Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| `for: 0m` on volatile metrics | Alert storms | Set appropriate `for` duration |
| Not grouping alerts | Too many notifications | Group by service, severity |
| No runbook links | Slow response | Always add `runbook_url` annotation |
| Alerting on raw counters | False positives | Use `rate()` to normalize |
| No `NoData` handling | Silent failures | Add `absent()` alerts |
| Hardcoded thresholds | Brittleness | Use SLO-based thresholds |
| No repeat interval tuning | Alert fatigue | Set `repeat_interval` appropriately |

## 10.4 Scrape Configuration Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Too many scrape targets per job | Load imbalance | Split into multiple jobs |
| Scrape interval too short | High cardinality | Use 15s-60s for most metrics |
| Missing `honor_labels: true` | Label conflicts | Configure appropriately |
| No target relabeling | Poor labels | Add metadata via relabeling |
| Using `file_sd` in Kubernetes | Stale targets | Use native Kubernetes SD |

## 10.5 Recording Rules Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| No recording rules for dashboards | Slow queries | Pre-compute expensive aggregations |
| Recording rule name too long | Truncation | Keep names <190 characters |
| Not grouping by instance | Loss of detail | Include critical dimensions |
| Inconsistent naming | Confusion | Follow `{level}:{metric}:{aggregation}` |
| No group for recording rules | Evaluation issues | Always use named groups |

## 10.6 Storage Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Retention too long locally | Disk exhaustion | Use remote write to object storage |
| Too many shards | Memory pressure | Right-size based on samples/sec |
| No compaction configured | Slow queries | Configure appropriate block duration |
| Not using WAL compression | Disk I/O | Enable `--storage.tsdb.wal-compression` |
| Remote write queue full | Data loss | Tune `queue_config` parameters |

## 10.7 Best Practices

1. **Use recording rules** for all dashboard queries that take >1 second
2. **Name recording rules**: `{type}:{metric}:{aggregation}` (e.g., `job:http_requests_total:rate5m`)
3. **Scrape at 15s** for critical metrics, **30s-60s** for most others
4. **Keep cardinality bounded**: <100 unique values per label
5. **Use `rate()`** for counters, **`increase()`** for totals over intervals
6. **Always use `by`/`without`** to control grouping dimensions
7. **Set `for: 5m`** on alerting rules to avoid flapping
8. **Use `histogram_quantile`** with `_bucket` suffix, not `_sum` or `_count`
9. **Alert on SLIs**, not raw metrics (e.g., error rate, not error count)
10. **Add `runbook_url`** annotation to all production alerts
11. **Use `absent()`** queries to detect missing metrics
12. **Remote write to long-term storage** after 2-15 days local retention
13. **Monitor Prometheus itself** with its built-in metrics
14. **Use `group_left()`** carefully when doing vector matching
15. **Test PromQL queries** in the UI before creating alerts

## 10.8 Kubernetes Operator Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Wrong `ServiceMonitor` namespace | Targets not discovered | Match target namespace |
| Missing `podMonitorSelector` | PodMonitors not picked up | Configure selector |
| Overly broad scrape intervals | High load | Set appropriate intervals |
| Not using `PodMonitor` for sidecars | Missing metrics | Use PodMonitor for sidecar patterns |
| Ignoring `thanos.io/pod-monitor` annotation | Manual configuration | Use annotation-based discovery |
