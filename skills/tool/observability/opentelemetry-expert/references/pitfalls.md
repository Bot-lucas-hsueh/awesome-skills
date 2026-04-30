# Common Pitfalls & Anti-Patterns

## 10.1 Instrumentation Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Creating spans inside hot paths** | High | Use sampling, avoid span creation in tight loops |
| 2 | **Sensitive data in span attributes** | High | Redact with processor or filter |
| 3 | **Span names not matching conventions** | Medium | Use `{operation_name}` pattern |
| 4 | **Not handling context propagation errors** | Medium | Always check for nil span |
| 5 | **Over-instrumenting with 100+ spans/request** | Medium | Aggregate related operations |
| 6 | **Creating new tracer instances per request** | High | Use singleton or dependency injection |
| 7 | **Not setting span status on errors** | Medium | Use `span.SetStatus(codes.Error)` |
| 8 | **Missing `span.End()` calls** | High | Use `defer span.End()` or spanscope |

## 10.2 Collector Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| No memory limiter | OOM crashes | Add `memory_limiter` processor |
| Unbounded sending queue | Memory exhaustion | Set `queue_size` limits |
| Single-threaded exporters | Throughput bottleneck | Configure `num_consumers` |
| No retry configuration | Lost data on transient errors | Add `retry_on_failure` |
| Too many processors | Performance degradation | Pipeline depth optimization |
| No health check endpoint | Hard to monitor | Add `health_check` extension |

## 10.3 Configuration Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Insecure transport in prod | Data exposure | Enable TLS everywhere |
| No compression | High network usage | Enable gzip compression |
| Wrong compression type | Compatibility issues | Match exporter/collector |
| Missing resource attributes | Poor correlation | Configure `resource` processor |
| Environment variables in config | Security risk | Use secrets management |
| Hardcoded endpoints | Rigidity | Use environment variable substitution |

## 10.4 Sampling Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| 100% sampling in production | Cost explosion | Use <10% head sampling |
| No error sampling | Missing incident traces | Always sample ERROR status |
| No tail sampling config | Too much noise | Configure `tail_sampling` |
| Sampling before enrichment | Missing context | Enrich before sampling decision |
| Fixed rate for all services | Unbalanced sampling | Per-service sampling rates |
| `decision_wait: 0s` | Performance issues | Set minimum 5-10s window |

## 10.5 Propagation Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Wrong propagator format | Broken traces | Match context format (W3C, B3) |
| Missing propagator registration | Silent failure | Register all needed propagators |
| Propagating too much context | Size bloat | Filter baggage entries |
| Not handling missing context | NullPointer errors | Check for nil before propagation |
| Propagating secrets in baggage | Security risk | Use separate secure channel |

## 10.6 Performance Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Synchronous exporting | Latency increase | Use batch processors |
| No batching | High overhead | Configure `batch` processor |
| Expensive attributes on spans | Storage bloat | Use low-cardinality values |
| Recording stack traces | Memory usage | Use 1% sampling for errors |
| Large baggage payloads | Network overhead | Limit baggage size |

## 10.7 Best Practices

1. **Always use W3C TraceContext** for cross-service propagation
2. **Name spans with `{operation}` pattern** (e.g., `POST /users`)
3. **Add semantic convention attributes** for each signal type
4. **Use resource attributes** to identify service, environment, version
5. **Implement tail-based sampling** for production traces
6. **Export metrics via OTLP** for trace-metric correlation
7. **Use batch processors** with appropriate batch sizes
8. **Enable health check extension** for Kubernetes probes
9. **Configure retry with exponential backoff** for all exporters
10. **Use Kubernetes operator** for declarative management
11. **Redact PII/secrets** before exporting
12. **Use library instrumentation** for common frameworks
13. **Monitor the collector itself** (built-in metrics on :8888)
14. **Set appropriate TTL** for in-memory queues
15. **Test sampling configuration** with production load patterns

## 10.8 Security Considerations

| Concern | Mitigation |
|---------|------------|
| Sensitive data in traces | Use `transform` processor to redact |
| TLS certificates | Use cert-manager for rotation |
| Secret management | Use Kubernetes secrets or Vault |
| Network policies | Restrict collector ingress/egress |
| Collector RBAC | Use read-only mode where possible |
| Audit logging | Enable OTel internal metrics |
