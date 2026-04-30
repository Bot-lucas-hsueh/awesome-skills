# KV Secrets Engine & Policy Examples

## KV Secrets Engine

```bash
# Enable KV v2 secrets engine
vault secrets enable -path=secret kv-v2

# Write a secret
vault kv put secret/myapp database username=admin password=secret123

# Read a secret
vault kv get secret/myapp

# Read specific version
vault kv get -version=3 secret/myapp

# List secrets
vault kv list secret/

# Delete (soft delete)
vault kv delete secret/myapp

# Permanently delete
vault kv destroy -versions=3 secret/myapp

# Update metadata
vault kv metadata put -max-versions=10 secret/myapp

# Check version info
vault kv metadata get secret/myapp
```

## Policy Examples

```hcl
# Read-only policy for an application
path "secret/data/app/*" {
  capabilities = ["read"]
}

# Read-write policy
path "secret/data/app/*" {
  capabilities = ["read", "list"]
}

# Admin policy
path "secret/*" {
  capabilities = ["create", "read", "update", "delete", "list"]
}

# Database credentials policy
path "database/creds/*" {
  capabilities = ["read"]
}

# Kubernetes auth policy example
path "auth/kubernetes/role/myapp" {
  capabilities = ["read"]
}
```
