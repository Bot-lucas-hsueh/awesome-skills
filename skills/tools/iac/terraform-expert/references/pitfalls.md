## 10. Common Pitfalls & Anti-Patterns

| # | Anti-Pattern| Severity| Quick Fix|
|---|----------------------|-----------------|---------------------|
| 1 | **Hardcoded values** | 🔴 High | Use variables |
| 2 | **Local state** | 🔴 High | Use remote backend |
| 3 | **No state locking** | 🔴 High | Add DynamoDB locking |
| 4 | **Monolithic main.tf** | 🟡 Medium | Create modules |
| 5 | **No formatting** | 🟡 Medium | Run terraform fmt |
| 6 | **Manual terraform destroy** | 🔴 High | Use CI/CD with approval |

