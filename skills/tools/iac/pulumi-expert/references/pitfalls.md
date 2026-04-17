# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Prevention |
|---|---------|----------|------------|
| 1 | Hardcoding resource names | 🔴 High | Use config + naming conventions |
| 2 | Not using stacks | 🔴 High | Separate dev/staging/prod |
| 3 | Storing secrets in code | 🔴 High | Use `pulumi config --secret` |
| 4 | Not reviewing preview | 🔴 High | Always `pulumi preview` |
| 5 | Ignoring dependencies | 🟡 Medium | Use proper resource dependencies |
| 6 | Manual state changes | 🔴 High | Only modify via Pulumi |

## 10.2 Anti-Patterns

### Resource Naming

```typescript
// BAD: Hardcoded names
const bucket = new aws.s3.Bucket("my-app-bucket");

// GOOD: Dynamic naming
const config = new pulumi.Config();
const env = config.require("environment");
const bucket = new aws.s3.Bucket(`${env}-app-bucket`);
```

### Secret Management

```typescript
// BAD: Hardcoded secrets
const password = "my-secret-password";

// GOOD: From config (encrypted)
const password = config.requireSecret("db-password");

// Or with secret()
const dbPassword = config.require("db-password");
```

## 10.3 State Management

| Issue | Solution |
|-------|----------|
| Accidental deletion | Use `protect: true` |
| State drift | Run `pulumi refresh` |
| State lock | Use `pulumi login --local` or backend |
| Corruption | Use `pulumi history` to rollback |

## 10.4 Best Practices

```
Project Structure:
□ One stack per environment
□ Modularize by component
□ Use shared config
□ Document stacks

Security:
□ Encrypt secrets
□ Use least privilege IAM
□ Rotate credentials
□ Audit access

Performance:
□ Use resource options for dependencies
□ Parallel resource creation
□ Enable stack references
□ Cache dependencies
```
