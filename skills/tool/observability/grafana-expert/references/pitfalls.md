# Common Pitfalls & Anti-Patterns

## 10.1 Dashboard Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|--------------|----------|-----------|
| 1 | **Queries without `$__range` or `$__interval`** | High | Use auto variables for dynamic ranges |
| 2 | **Hardcoded datasource UIDs** | Medium | Use datasource variables |
| 3 | **Too many panels per dashboard** | Medium | Split into multiple linked dashboards |
| 4 | **No templating variables** | Medium | Add environment/service filters |
| 5 | **Missing time range context** | Medium | Add annotations for releases/deploys |
| 6 | **Using tabs for different datasources** | Low | Use mixed datasource |
| 7 | **No dashboard description** | Low | Document purpose and ownership |
| 8 | **Overly complex mixed queries** | Medium | Split into separate panels |

## 10.2 Query Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| `*` in label matchers | Very slow | Use specific label filters |
| `rate()` without recording rules | High cardinality | Use pre-aggregated recording rules |
| Large `topk()` without limit | Hidden cardinality | Limit to top 10-20 |
| `histogram_quantile` without `by (le)` | Aggregation error | Always include `by (le, ...)` |
| Using `__name__` regex without anchoring | Multiple metrics matched | Anchor both ends: `^metric_name$` |
| Nested subselections | Query complexity | Use recording rules |
| `without()` removing critical labels | Lost context | Keep essential labels |

## 10.3 Alerting Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Alert fires immediately (`for: 0m`) | Alert storms | Set minimum `for` duration |
| No `NoData` handling | Missing alerts | Configure `noDataState` |
| `OR` without priority | Confusing routing | Use nested `AND`/`OR` carefully |
| Too many annotations | Clutter | Keep to summary + runbook link |
| Testing in production | Alert spam | Test in staging first |
| Alerting on raw data | Noise | Use recording rules for complex queries |
| No deduplication | Repeated alerts | Group by alertname + labels |

## 10.4 Provisioning Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Storing secrets in YAML | Security risk | Use environment variables |
| `disableDeletion: true` forever | Orphaned objects | Enable deletion after migration |
| Manual changes + provisioning | Configuration drift | GitOps-only approach |
| Not pinning plugin versions | Breaking changes | Pin to specific versions |
| Large dashboard JSONs | Hard to review | Split by panel type |
| Missing `orgId` in multi-tenant | Wrong org | Always specify orgId |

## 10.5 Performance Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Large time ranges on busy dashboards | Timeouts | Limit to 7 days or use downsampling |
| Too many datasources per panel | Slow rendering | Consolidate or use recording rules |
| Real-time refresh on large datasets | High load | Use longer intervals |
| Histogram panels on high-cardinality data | Browser OOM | Reduce bucket count |
| Canvas with many data points | Rendering lag | Sample or aggregate |

## 10.6 Security Anti-Patterns

| Anti-Pattern | Impact | Solution |
|--------------|--------|----------|
| Admin token for apps | Privilege escalation | Use viewer API key |
| Default admin credentials | Unauthorized access | Disable default admin |
| Public dashboards without scoping | Data leakage | Use `hideAlerts` and `hideControls` |
| Sharing dashboard links publicly | Information disclosure | Require authentication |
| SQL datasource with write access | SQL injection risk | Use read-only user |
| Storing passwords in grafana.ini | Hard to rotate | Use grafana.ini secrets |

## 10.7 Best Practices

1. **Use recording rules** for frequently-queried complex aggregations
2. **Name dashboards consistently**: `{team}-{service}-{view}`
3. **Tag dashboards** for organization and filtering
4. **Document SLIs/SLOs** in dashboard descriptions
5. **Link related dashboards** using panel links
6. **Pin important dashboards** to home dashboard
7. **Use folders** for team ownership and access control
8. **Set dashboard cache TTL** appropriately
9. **Export and version control** all dashboards
10. **Use annotations** for deployments, incidents, config changes
11. **Test alert rules** with preview before saving
12. **Rotate API keys** every 90 days
13. **Use RBAC** for fine-grained permissions
14. **Monitor Grafana itself** (builtin dashboard)
15. **Use library panels** for shared visualization patterns
