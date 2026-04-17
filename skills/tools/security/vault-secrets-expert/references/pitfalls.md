# Common Pitfalls & Anti-Patterns

## 10.1 Common Mistakes

| # | Mistake | Severity | Impact | Quick Fix |
|---|---------|----------|--------|-----------|
| 1 | **Not using TLS in production** | 🔴 Critical | All secrets transmitted in clear text | Use `listener "tcp" { tls_cert_file = "..." tls_key_file = "..." }` |
| 2 | **Root token never revoked** | 🔴 Critical | Excessive blast radius if leaked | `vault token revoke -self` from root token; use periodic tokens instead |
| 3 | **Unseal keys stored together** | 🔴 Critical | Single point of failure for Shamir | Use Vault Transit auto-unseal or distribute keys across separate HSMs/teams |
| 4 | **Policies too broad (`*` wildcards)** | 🔴 High | Principle of least privilege violated | Be explicit: `path "secret/data/apps/myapp/{{identity.entity.name}}" { capabilities = ["read"] }` |
| 5 | **KV v1 vs v2 confusion** | 🔴 High | `/v1/secret/foo` vs `/v1/secret/data/foo` | Use KV v2 consistently; check version: `vault kv get -version=1 secret/mykey` |
| 6 | **Dynamic secrets with infinite TTL** | 🔴 High | Leaked creds valid forever | Always set `default_ttl` and `max_ttl` on database/AWS roles |
| 7 | **No audit logging** | 🔴 High | No compliance trail, no forensics | `vault audit enable file file_path=/var/log/vault/audit.log` |
| 8 | **Secrets in environment variables** | 🟡 Medium | Visible in `ps aux`, container logs | Use Vault Agent sidecar or secret injection via file with restricted permissions |
| 9 | **Ignoring lease TTLs** | 🟡 Medium | Revoked creds still work if not tracked | Set short TTLs; implement lease renewal/revocation logic |
| 10 | **Single-region Vault** | 🟡 Medium | Region outage = secret outage | Use Performance Replication (Enterprise) or multi-region storage |
| 11 | **No snapshot backups** | 🔴 High | No recovery path from data loss | `vault operator raft snapshot save` daily + before upgrades |
| 12 | **Using default mlock behavior** | 🟡 Medium | `mlock: false` on swap-enabled systems leaks secrets to disk | `disable_mlock = false` (or handle swap properly) |

### Unseal Key Anti-Patterns

```bash
# BAD: All 5 keys with same ops team
# -> Single compromised team = all keys compromised

# GOOD: Shamir split
# - 1 key: HSM/Key Management (never touches human hands)
# - 2 keys: Security team (individual, stored in separate HSMs)
# - 2 keys: Ops team (individual, different locations)
# Threshold: 3 (any 3 of 5)

# BETTER: Auto-unseal with cloud KMS
# AWS: vault write transit/config aws_kms_key_id=...
# GCP: vault write transit/config gcp_kms_key_id=...
# -> No manual unseal needed after restart
```

### Policy Anti-Patterns

```hcl
# BAD: Wildcard on everything
path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# BAD: Read-only but still allows listing all secrets
path "secret/*" {
  capabilities = ["read", "list"]   # Can enumerate all secrets
}

# BAD: Template-free policy for all entities
path "secret/data/apps/{{entity.name}}" {
  capabilities = ["read"]
}
# If entity.name is empty or forged, this fails silently

# GOOD: Specific path, explicit capabilities
path "secret/data/apps/payment-service/db" {
  capabilities = ["read"]
}

# GOOD: Use role-id based policies for AppRole
path "secret/data/apps/myapp/{{role_id}}" {
  capabilities = ["read"]
}
```

## 10.2 Anti-Patterns

### Anti-Pattern 1: Static Secrets in Code

```go
// BAD: Secret hardcoded
password := "super-secret-password"
url := "postgres://user:super-secret-password@db:5432"

// BAD: Secret in config file committed to repo
db_password: "super-secret-password"
```

**Fix:** Fetch from Vault at runtime using AppRole or Kubernetes auth:
```go
// GOOD
secret, _ := client.Logical().Read("secret/data/apps/myapp/db")
password := secret.Data["data"].(map[string]interface{})["password"].(string)
```

---

### Anti-Pattern 2: Long-Lived Tokens

```bash
# BAD: Token valid for 1 year
vault token create -ttl=8760h -policy=myapp
```

**Fix:** Use short-lived tokens with automatic renewal:
```bash
# GOOD: Short TTL, renew before expiry
vault token create -ttl=1h -policy=myapp
# App renews before 1h expires using lease renewal API
```

Or use AppRole which is designed for machine auth:
```bash
# GOOD: AppRole with short token_ttl
vault write auth/approle/role/myapp \
  token_ttl=20m \
  token_max_ttl=1h \
  secret_id_ttl=10m
```

---

### Anti-Pattern 3: No Secret Rotation Strategy

```bash
# BAD: Static DB password set once, never rotated
vault kv put secret/app/db password="original-password-123"
# 5 years later: same password, never changed
```

**Fix:** Dynamic secrets (per-lease unique credentials) or scheduled rotation:
```bash
# GOOD: Dynamic credentials
vault read database/creds/myapp-readonly
# Each call returns different credentials

# GOOD: Rotation via cron/Vault Agent
# policy.hcl
path "secret/data/apps/myapp/db" {
  capabilities = ["update"]
}
# Rotate monthly: vault kv put secret/data/apps/myapp/db password="$(openssl rand -base64 32)"
```

---

### Anti-Pattern 4: Overly Permissive Policies

```hcl
# BAD: Admin policy for every app
path "*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# BAD: Policy grants more than needed
path "secret/data/*" {
  capabilities = ["read", "update"]  # App only reads, no updates
}
```

**Fix:** One policy per app, minimum capabilities:
```hcl
# GOOD
path "secret/data/apps/myapp/database" {
  capabilities = ["read"]
}
path "secret/metadata/apps/myapp/database" {
  capabilities = ["list"]
}
```

---

### Anti-Pattern 5: Exposing Vault Token to Containers Without Scoping

```yaml
# BAD: Pod gets cluster-admin Vault token
serviceAccount: vault-sa  # bound to admin policy
```

**Fix:** Use service account namespacing + Vault role binding:
```yaml
# GOOD: Tightly bound service account
# vault write auth/kubernetes/role/myapp \
#   bound_service_account_names=myapp-sa \
#   bound_service_account_namespaces=production \
#   policies=myapp-readonly \
#   ttl=24h
```

---

### Anti-Pattern 6: Manual Secret Injection via CI/CD

```bash
# BAD: CI reads secrets and sets env vars (leaked to build logs)
export DB_PASSWORD=$(vault kv get -field=password secret/app/db)
docker run -e DB_PASSWORD=$DB_PASSWORD ...
# -> Password visible in CI logs
```

**Fix:** Use Vault Agent Injector or build-time secret injection with cleanup:
```bash
# GOOD: Vault Agent sidecar injects at runtime (not build)
# annotation on pod: vault.hashicorp.com/agent-inject: "true"
# annotation: vault.hashicorp.com/role: "myapp"
# No env vars needed, secrets mounted as files

# GOOD: If CI must use secrets, use one-time tokens
VAULT_TOKEN=$(vault token create -policy=ci-policy -ttl=10m -field=token)
vault kv get -field=password secret/ci/db
vault token revoke $VAULT_TOKEN
```

---

### Anti-Pattern 7: Using KV v1 in 2024+

```bash
# BAD: v1 doesn't support versioning, metadata, check-and-set
vault write secret/myapp/config '{"key":"value"}'
vault write secret/myapp/config '{"key":"newvalue"}"  # Overwrites, no history
```

**Fix:** Use KV v2:
```bash
# GOOD: v2 with versioning
vault secrets enable -path=secret kv-v2
vault kv put secret/myapp/config key="value"
vault kv put secret/myapp/config key="newvalue"
vault kv get -version=1 secret/myapp/config  # Read old version
vault kv metadata put -max-versions=10 secret/myapp/config
```

---

### Anti-Pattern 8: No Monitoring on Lease Expiration

```go
// BAD: Credential fetched, lease_id ignored
creds, _ := client.DatabaseCredentials("myapp")
db.Connect(creds.Username, creds.Password)
// Lease expires, DB password revoked, app fails with auth errors
```

**Fix:** Track and renew leases:
```go
// GOOD: Renew lease, handle expiration
creds, err := client.Databases().Credentials("myapp", "myapp-role")
if err != nil {
    // Handle error
}

// Start renewal goroutine
go func() {
    for {
        client.Sys().Renewal(creds.LeaseID, 30*time.Second)
    }
}()

// Handle expiration: re-fetch credentials when TTL expires
<-time.After(time.Duration(creds.TTL) * time.Second)
creds, _ = client.Databases().Credentials("myapp", "myapp-role")
```
