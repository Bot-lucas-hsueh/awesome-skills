## 10. Common Pitfalls & Anti-Patterns

| # | Anti-Pattern| Severity| Quick Fix|
|---|----------------------|-----------------|---------------------|
| 1 | **No resource limits** | 🔴 High | Always set requests/limits |
| 2 | **Running as root** | 🔴 High | Add securityContext |
| 3 | **No health checks** | 🔴 High | Add liveness/readiness probes |
| 4 | **Latest tag** | 🔴 High | Use specific version tags |
| 5 | **No RBAC** | 🔴 High | Implement RBAC |
| 6 | **No network policy** | 🟡 Medium | Add NetworkPolicy |
| 7 | **Secrets in manifests** | 🔴 High | Use SealedSecrets/external secrets |

