# Standards & Reference

## 7.1 Official Documentation

- [HashiCorp Vault Documentation](https://developer.hashicorp.com/vault/docs)
- [Vault API Reference](https://developer.hashicorp.com/vault/api)
- [Vault Configuration Reference](https://developer.hashicorp.com/vault/docs/configuration)
- [Vault Policies](https://developer.hashicorp.com/vault/docs/concepts/policies)
- [Vault Secrets Engines](https://developer.hashicorp.com/vault/docs/secrets)
- [Vault Authentication](https://developer.hashicorp.com/vault/docs/auth)
- [Vault Best Practices](https://developer.hashicorp.com/vault/tutorials/operations)
- [Vault Upgrade Guides](https://developer.hashicorp.com/vault/docs/upgrades)

## 7.2 Configuration Reference

### storage stanza (raft backend)

```hcl
storage "raft" {
  path = "/var/opt/vault/data"
  node_id = "vault_node_1"

  retry_join {
    leader_api_addr = "https://vault1.internal:8200"
  }
  retry_join {
    leader_api_addr = "https://vault2.internal:8200"
  }
}
```

### listener stanza

```hcl
listener "tcp" {
  address         = "[::]:8200"
  cluster_address = "[::]:8201"
  tls_cert_file   = "/etc/vault/tls/server.crt"
  tls_key_file    = "/etc/vault/tls/server.key"
  telemetry {
    unauthenticated_metrics_access = false
  }
}
```

### HA cluster

```hcl
storage "raft" {
  path = "/var/opt/vault/data"
  node_id = "node_2"
  retry_join {
    leader_api_addr = "https://vault1.internal:8200"
  }
}

cluster_addr = "https://vault_node2.internal:8201"

listener "tcp" {
  address         = "[::]:8200"
  cluster_address = "[::]:8201"
  tls_cert_file   = "/etc/vault/tls/server.crt"
  tls_key_file    = "/etc/vault/tls/server.key"
}
```

### Auth Methods (vault.hcl)

```hcl
# Enable Kubernetes auth at install time
api_addr = "https://vault.internal:8200"
cluster_addr = "https://vault.internal:8201"

storage "raft" {
  path = "/var/opt/vault/data"
}

listener "tcp" {
  address = "[::]:8200"
  cluster_address = "[::]:8201"
  tls_cert_file = "/etc/vault/tls/server.crt"
  tls_key_file  = "/etc/vault/tls/server.key"
}

disable_mlock = true
```

### Secrets Engines

| Engine | Path | Use Case |
|--------|------|----------|
| kv-v2 | `secret/` | Generic key-value |
| pki | `pki/` | Certificate management |
| aws | `aws/` | AWS credentials |
| database | `database/` | Dynamic DB credentials |
| transit | `transit/` | Encryption as a service |
| ssh | `ssh/` | SSH certificate authority |
| identity | `identity/` | Entity management |

### Policy Example

```hcl
path "secret/data/apps/*" {
  capabilities = ["read", "list"]
}

path "secret/metadata/*" {
  capabilities = ["list"]
}

path "database/creds/readonly-* {
  capabilities = ["read"]
}

path "pki/issue/*" {
  capabilities = ["update"]
}
```

## 7.3 Common Commands

### Server & Init

```bash
vault server -config=/etc/vault.d/vault.hcl
vault operator init                          # Initialize (5 key shares, 3 key threshold)
vault operator init -key-shares=7 -key-threshold=4
vault operator unseal <unseal-key>
vault operator unseal -migrate               # Key migration
vault operator raft snapshot save backup.snap
vault operator raft snapshot restore backup.snap
vault status
```

### KV Secrets Engine

```bash
vault kv put secret/myapp/database username="app" password="secret123"
vault kv get secret/myapp/database
vault kv get -field=password secret/myapp/database
vault kv put secret/myapp/config '{"key": "value"}'
vault kv put secret/myapp/db url="postgres://localhost:5432"
vault kv delete secret/myapp/database
vault kv list secret/
vault kv list secret/myapp/
vault kv get -version=3 secret/myapp/database     # Read version 3
vault kv rollback -version=2 secret/myapp/database
vault kv destroy -version=2 secret/myapp/database
vault kv metadata put -max-versions=10 secret/myapp
vault kv metadata put -delete-version-after=30d secret/myapp
vault kv patch secret/myapp/database password="newpass"
```

### Auth Methods

```bash
vault auth enable kubernetes
vault auth enable aws
vault auth enable userpass
vault auth enable ldap
vault auth enable approle
vault auth enable cert
vault auth enable oidc
vault auth list
vault auth tune -default-lease-ttl=1h auth/kubernetes/
vault write auth/kubernetes/config token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" kubernetes_host="https://$KUBERNETES_PORT_443_TCP_ADDR:443" kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
vault write auth/approle/role/myapp \
    secret_id_ttl=10m \
    token_num_uses=0 \
    token_ttl=20m \
    token_max_ttl=30m \
    secret_id_num_uses=0
vault write auth/approle/role/myapp policies="myapp-policy"
vault read auth/approle/role/myapp/role-id
vault write -f auth/approle/role/myapp/secret-id
vault login -method=approle role_id=<role_id> secret_id=<secret_id>
vault login -method=kubernetes role=myapp
vault token create -policy=myapp-policy -ttl=1h
vault token revoke <token>
vault token lookup
```

### Secrets Engines

```bash
# Enable engines
vault secrets enable -path=aws aws
vault secrets enable -path=database database
vault secrets enable -path=pki pki
vault secrets enable -path=transit transit
vault secrets enable -path=secret kv-v2
vault secrets disable aws
vault secrets list

# AWS
vault write aws/config/root \
    access_key=AKIA... \
    secret_key="..." \
    region=us-east-1
vault write aws/roleset/myapp \
    arn=arn:aws:iam::123456789:role/myapp \
    credential_type=iam_user \
    policy_document=@policy.json
vault read aws/creds/myapp
vault write -f aws/creds/myapp          # Generate dynamic credentials
vault write aws/roles/myapp \
    secret_key_arn=arn:aws:kms:us-east-1:123456789:key/... \
    key_name=myapp-key

# Database
vault write database/config/myapp \
    plugin_name=postgresql-database-plugin \
    connection_url="postgresql://{{username}}:{{password}}@localhost:5432/myapp" \
    username="vault-admin" \
    password="vault-admin-password" \
    allowed_roles="readonly,readwrite"
vault write database/roles/readonly \
    db_name=myapp \
    creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
    default_ttl=1h \
    max_ttl=24h
vault read database/creds/readonly
vault lease renew database/creds/readonly/<lease-id>
vault lease revoke database/creds/readonly/<lease-id>

# PKI
vault secrets tune -max-lease-ttl=87600h pki
vault write pki/root/generate/internal \
    common_name="My Internal CA" \
    ttl=87600h
vault write pki/roles/myapp \
    allowed_domains="myapp.internal" \
    allow_subdomains=true \
    max_ttl=72h
vault write pki/issue/myapp common_name="db.myapp.internal"
vault write pki/config/urls \
    issuing_certificates="https://vault.internal:8200/v1/pki/ca" \
    crl_distribution_points="https://vault.internal:8200/v1/pki/crl"

# Transit
vault write transit/keys/myapp-key
vault write transit/encrypt/myapp-key plaintext=$(echo -n "secret data" | base64)
vault write transit/decrypt/myapp-key ciphertext="vault:v1:..."
vault write transit/rewrap/myapp-key ciphertext="vault:v1:..."   # Re-encrypt with new key version
vault write transit/rotate/myapp-key                           # Rotate key version
vault transit keys list
```

### Policy Management

```bash
vault policy list
vault policy read myapp-policy
vault policy write myapp-policy /tmp/policy.hcl
vault policy fmt /tmp/policy.hcl       # Format policy
vault policy delete myapp-policy
```

### Audit

```bash
vault audit enable file file_path=/var/log/vault/audit.log
vault audit enable file file_path=/var/log/vault/audit.log log_raw=true
vault audit list
vault audit disable file
```

### Namespaces (Enterprise)

```bash
vault namespace create security
vault namespace list
vault namespace lookup security
vault token create -namespace=security -policy=default
VAULT_NAMESPACE=security vault secrets enable -path=secret kv-v2
```

## 7.4 Version Compatibility

| Vault Version | Status | EOL Date | Key Changes |
|---------------|--------|----------|-------------|
| 1.18.x | Current | ~2026 | MCP server, PKI improvements |
| 1.17.x | Supported | ~2026 | Secrets Sync, events |
| 1.16.x | Supported | ~2025 | Protobuf events, Audit improvements |
| 1.15.x | LTS | ~2027 | DR replication, User lockout |
| 1.14.x | LTS | ~2026 | Control groups, KMIP |
| 1.13.x | Security updates only | ~2025 | Ent snap exports |
| 1.12.x | EOL | - | Transform secrets engine GA |

| Client | Min Vault | Notes |
|--------|-----------|-------|
| Vault CLI | Same minor version | CLI auto-negotiates API |
| vault-sdk-go | 1.11+ | Semantic versioning |
| terraform-provider-vault | 1.14+ recommended | Check CHANGELOG |

| Feature | Min Version | Enterprise |
|---------|-------------|------------|
| KV v2 | 0.10+ | - |
| Transit rewrap | 0.9+ | - |
| Namespace | 0.11+ | Required |
| Control Groups | 1.14+ | Required |
| Performance Replication | 1.9+ | Required |
| Secrets Sync | 1.17+ | Required |
