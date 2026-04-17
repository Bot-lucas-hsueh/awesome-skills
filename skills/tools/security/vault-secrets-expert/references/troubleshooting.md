# Troubleshooting Guide

## 8.1 Authentication Issues

### Token Expired

**Problem:** Received "permission denied" or "permission denied" errors.

**Diagnosis:**
```bash
# Check current token
vault token lookup

# Verify token capabilities
vault token capabilities secret/data/myapp

# Check expiration
vault token lookup | grep "expire_time"
```

**Fix:**
```bash
# Renew token (if allowed)
vault token renew

# Or re-authenticate
vault login -method=approle role_id=xxx secret_id=xxx
```

### Auth Method Not Working

**Problem:** Cannot authenticate with configured auth method.

**Diagnosis:**
```bash
# Check auth method is enabled
vault auth list

# Check auth method config
vault read auth/kubernetes/config

# Test JWT token
vault write auth/kubernetes/login jwt=xxx role=myapp
```

## 8.2 Secrets Not Found

### Path Not Found

**Problem:** Error reading secret - "permission denied" or "path not found".

**Diagnosis:**
```bash
# Check if secret engine exists
vault secrets list

# Check secret path
vault kv list secret/

# Verify policy
vault policy read myapp-policy
```

**Fix:**
```hcl
# Fix policy to allow access
path "secret/data/myapp/*" {
  capabilities = ["read"]
}
```

### Wrong Namespace

**Problem:** Secret exists but cannot be accessed.

**Fix:**
```bash
# List namespaces
vault namespace list

# Use correct namespace
export VAULT_NAMESPACE=ns_name
vault kv get secret/myapp
```

## 8.3 Seal/Unseal Issues

### Vault Sealed

**Problem:** Vault sealed after restart.

**Diagnosis:**
```bash
vault status
# Shows: Sealed: true
```

**Fix:**
```bash
# Unseal with key shares (Shamir)
vault operator unseal <key1>
vault operator unseal <key2>
vault operator unseal <key3>

# Check seal status
vault status
# Should show: Sealed: false
```

### Auto-Unseal Not Working

**Fix:**
```bash
# Check seal configuration
vault read sys/seal

# For AWS KMS auto-unseal:
vault write sys/seal aws-kms key_id=xxx

# Verify
vault status
```

## 8.4 Performance Issues

### Slow Reads

**Problem:** Vault reads are slow.

**Diagnosis:**
```bash
# Check latency
time vault kv get secret/myapp

# Check storage backend
vault status | grep Storage
```

**Fix:**
- Use faster storage backend
- Enable caching
- Check network latency

### High Memory Usage

**Fix:**
```bash
# Check memory
vault status | grep "Used Memory"

# Limit max_request_stack
vault write sys/config request-handling max_request_stack_size=1024
```

## 8.5 Replication Issues

### Replication Not Working

**Diagnosis:**
```bash
# Check replication status
vault status | grep "Replication"

# Check performance replication
vault read sys/replication/status
```

**Fix:**
- Verify network connectivity between nodes
- Check same storage backend
- Ensure proper TLS certificates

## 8.6 Dynamic Secrets Issues

### Database Credentials Not Rotating

**Problem:** Database credentials not being revoked.

**Fix:**
```bash
# Manually revoke lease
vault lease revoke database/creds/myapp/<lease_id>

# Check leases
vault list sys/leases/lookup/database/creds/myapp
```

### Lease Expired

**Problem:** Application fails when lease expires.

**Fix:**
```javascript
// In application code:
// 1. Track lease expiration
// 2. Renew before expiry
// 3. Re-fetch credentials on expiry
const lease = await client.secret.database.creds('myapp-role');
setTimeout(async () => {
  await renew(lease.LeaseID);
}, lease.TTL * 1000 - 60000);
```

## 8.7 Policy Issues

### Permission Denied Despite Policy

**Diagnosis:**
```bash
# Check token policies
vault token lookup | grep policies

# Check effective policy
vault token capabilities secret/data/myapp

# Test policy
vault policy read myapp
```

**Fix:**
```hcl
# Update policy
vault policy write myapp - <<EOF
path "secret/data/myapp/*" {
  capabilities = ["read", "list"]
}
EOF
```
