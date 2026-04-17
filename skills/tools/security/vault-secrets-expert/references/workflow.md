# Standard Workflow

## 8.1 Vault Setup Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ Phase 1: Initial Server Setup                                   │
│                                                                 │
│  1. Install Vault binary                                        │
│     curl -fsSL https://releases.hashicorp.com/vault/1.18.0/... │
│                                                                 │
│  2. Create vault user & directories                             │
│     useradd -r vault                                            │
│     mkdir -p /var/opt/vault/{data,logs,config}                  │
│     chown -R vault:vault /var/opt/vault                        │
│                                                                 │
│  3. Write vault.hcl config                                      │
│     storage raft, listener tcp, telemetry                       │
│     tls (cert/key), cluster_addr for HA                         │
│                                                                 │
│  4. Write systemd unit file                                     │
│     ExecStart=vault server -config=/etc/vault.d/                │
│     Restart=always, User=vault                                  │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Phase 2: Cluster Formation (HA / DR)                            │
│                                                                 │
│  1. Start first node, run vault operator init                   │
│     vault operator init -key-shares=5 -key-threshold=3          │
│     -> Get 5 unseal keys (store in Vault, Shamir)               │
│     -> Get initial root token                                   │
│                                                                 │
│  2. Unseal all nodes                                            │
│     vault operator unseal <key1> (repeat 3 times per node)      │
│                                                                 │
│  3. Join additional nodes via retry_join                        │
│     Check: vault operator members                               │
│                                                                 │
│  4. Verify cluster health                                       │
│     vault status                                                │
│     curl -s https://vault:8200/v1/sys/health?standbyok=true     │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Phase 3: Production Hardening                                   │
│                                                                 │
│  1. Enable audit logging                                        │
│     vault audit enable file file_path=/var/log/vault/audit.log  │
│     vault audit enable file log_raw=true                        │
│                                                                 │
│  2. Configure TLS (must for production)                         │
│     listener.tls_cert_file, listener.tls_key_file               │
│                                                                 │
│  3. Enable required auth methods                               │
│     vault auth enable kubernetes                                │
│     vault auth enable approle                                   │
│     vault auth enable aws                                       │
│                                                                 │
│  4. Enable secrets engines                                      │
│     vault secrets enable -path=secret -description="App secrets" kv-v2
│     vault secrets enable -path=pki pki                         │
│     vault secrets enable -path=aws aws                          │
│                                                                 │
│  5. Create admin and app policies                               │
│     vault policy write admin-policy admin.hcl                   │
│     vault policy write myapp-policy myapp.hcl                   │
│                                                                 │
│  6. Configure Kubernetes auth                                   │
│     vault write auth/kubernetes/config                          │
│       token_reviewer_jwt=...                                    │
│       kubernetes_host=...                                       │
│       kubernetes_ca_cert=@ca.crt                                │
│                                                                 │
│  7. Create AppRole for each service                             │
│     vault write auth/approle/role/myapp                         │
│       policies=myapp-policy                                     │
│       token_ttl=1h                                              │
│                                                                 │
│  8. Generate root CA for PKI                                    │
│     vault write pki/root/generate/internal ttl=87600h ...       │
└─────────────────────────────────────────────────────────────────┘
```

## 8.2 Secrets Management Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ Step 1: Design Secrets Structure                                │
│                                                                 │
│  secret/                                                         │
│  ├── apps/           <- per-app namespace                      │
│  │   ├── myapp/                                               │
│  │   │   ├── database      (DB credentials)                   │
│  │   │   ├── api-keys      (external API keys)                │
│  │   │   └── config        (JSON config, certs)                │
│  │   └── otherapp/                                             │
│  ├── infra/          <- infrastructure secrets                 │
│  │   ├── tls/                                               │
│  │   └── backup-credentials/                                  │
│  └── shared/         <- cross-team shared secrets              │
│      └── registry-creds/                                       │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Step 2: Create Policies (principle of least privilege)          │
│                                                                 │
│  myapp-policy.hcl:                                              │
│  path "secret/data/apps/myapp/*" {                              │
│    capabilities = ["read"]                                      │
│  }                                                              │
│  path "secret/metadata/apps/myapp/*" {                          │
│    capabilities = ["list"]                                      │
│  }                                                              │
│  path "database/creds/myapp-*" {                                 │
│    capabilities = ["read"]                                      │
│  }                                                              │
│  path "pki/issue/myapp" {                                       │
│    capabilities = ["update"]                                    │
│  }                                                              │
│  path "auth/approle/role/myapp/role-id" {                        │
│    capabilities = ["read"]                                       │
│  }                                                              │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Step 3: Write & Read Secrets                                    │
│                                                                 │
│  Write secrets (admin/CI only):                                 │
│  vault kv put secret/apps/myapp/database \                      │
│    host="db.internal" \                                         │
│    port="5432" \                                               │
│    username="myapp" \                                          │
│    password="$(openssl rand -base64 32)"                        │
│                                                                 │
│  Write config (JSON):                                           │
│  vault kv put secret/apps/myapp/config \                        │
│    config_json='{"log_level":"info","timeout_ms":5000}'         │
│                                                                 │
│  Read in application:                                           │
│  VAULT_ADDR=https://vault.internal:8200 \                       │
│  VAULT_TOKEN="$(vault kv get -field=token secret/apps/myapp/svc)" \
│  DB_PASS=$(vault kv get -field=password secret/apps/myapp/database)
│                                                                 │
│  Read via Kubernetes auth (preferred):                          │
│  VAULT_ADDR=https://vault.internal:8200                        │
│  vault kv get secret/apps/myapp/database   # uses mounted SA token
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Step 4: Secret Rotation                                         │
│                                                                 │
│  1. Update secret:                                              │
│     vault kv put secret/apps/myapp/database password="newpass"  │
│                                                                 │
│  2. Set metadata for retention:                                  │
│     vault kv metadata put \                                     │
│       -max-versions=10 \                                       │
│       -delete-version-after=90d \                               │
│       secret/apps/myapp/database                                │
│                                                                 │
│  3. For DB credentials, revoke old lease:                        │
│     vault lease revoke database/creds/myapp/<lease-id>          │
│                                                                 │
│  4. Verify application picked up new secret:                     │
│     Check app logs / health endpoint                            │
└─────────────────────────────────────────────────────────────────┘
```

## 8.3 Dynamic Secrets Workflow

```
┌─────────────────────────────────────────────────────────────────┐
│ AWS Dynamic Secrets                                             │
│                                                                 │
│  1. Enable and configure AWS secrets engine                     │
│     vault secrets enable -path=aws aws                          │
│     vault write aws/config/root \                               │
│       access_key=AKIA... \                                     │
│       secret_key="..." \                                       │
│       region=us-east-1                                          │
│                                                                 │
│  2. Create a Vault role (maps to IAM role)                      │
│     vault write aws/roles/myapp-role \                          │
│       arn=arn:aws:iam::123456789:role/myapp-ecs-task \          │
│       credential_type=iam_user \                                │
│       policy_document=@aws-policy.json                          │
│                                                                 │
│  3. Generate credentials (app calls this at startup)           │
│     vault read aws/creds/myapp-role                             │
│     -> Returns access_key, secret_key, security_token           │
│                                                                 │
│  4. Application uses credentials, Vault auto-revokes at TTL     │
│     vault write -f aws/creds/myapp-role  # Manual generation    │
│                                                                 │
│  5. Clean up stale IAM users:                                   │
│     vault write aws/config/lease \                              │
│       lease=1h \                                               │
│       lease_max=24h                                            │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Database Dynamic Secrets                                        │
│                                                                 │
│  1. Enable database secrets engine                              │
│     vault secrets enable -path=database database                 │
│                                                                 │
│  2. Configure database connection                               │
│     vault write database/config/myapp-postgres \                │
│       plugin_name=postgresql-database-plugin \                  │
│       connection_url="postgresql://{{username}}:{{password}}@db:5432" \
│       username="vault-admin" \                                  │
│       password="vault-admin-pass" \                             │
│       allowed_roles="readonly,readwrite"                         │
│                                                                 │
│  3. Create database role (defines what DB user Vault creates)   │
│     vault write database/roles/readonly \                       │
│       db_name=myapp-postgres \                                  │
│       creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT SELECT ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
│       default_ttl=1h \                                          │
│       max_ttl=24h                                               │
│                                                                 │
│     vault write database/roles/readwrite \                      │
│       db_name=myapp-postgres \                                  │
│       creation_statements="CREATE ROLE \"{{name}}\" WITH LOGIN PASSWORD '{{password}}' VALID UNTIL '{{expiration}}'; GRANT SELECT, INSERT, UPDATE, DELETE ON ALL TABLES IN SCHEMA public TO \"{{name}}\";" \
│       default_ttl=1h \                                          │
│       max_ttl=8h                                                │
│                                                                 │
│  4. Application requests credentials                            │
│     vault read database/creds/readonly                           │
│     -> Returns username, password, lease_id, lease_duration     │
│                                                                 │
│  5. Application uses credentials, Vault creates DB user per lease
│     When lease expires: vault auto-revokes and drops DB user    │
│                                                                 │
│  6. Dynamic root credential (initial DB setup only)            │
│     vault read database/creds/myapp-postgres                    │
│     Store in Vault kv for Vault's own access to DB             │
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ PKI Certificates                                                │
│                                                                 │
│  1. Configure CA                                                │
│     vault secrets enable -path=pki pki                          │
│     vault secrets tune -max-lease-ttl=87600h pki               │
│     vault write pki/root/generate/internal \                    │
│       common_name="internal.example.com" \                     │
│       ttl=87600h                                                │
│                                                                 │
│  2. Create role for issuance                                   │
│     vault write pki/roles/myapp \                               │
│       allowed_domains="myapp.internal" \                        │
│       allow_subdomains=true \                                   │
│       allow_any_name=false \                                    │
│       enforce_hostnames=true \                                  │
│       max_ttl=72h \                                             │
│       generate_lease=true                                       │
│                                                                 │
│  3. Issue certificate on demand                                 │
│     vault write pki/issue/myapp \                               │
│       common_name="db1.myapp.internal" \                       │
│       ttl=24h                                                   │
│     -> Returns certificate, private_key, issuing_ca, serial_number
│                                                                 │
│  4. Certificate renewal (before expiry)                         │
│     vault write pki/issue/myapp common_name="svc.myapp.internal"
│                                                                 │
│  5. CRL configuration                                           │
│     vault write pki/config/urls \                               │
│       issuing_certificates="https://vault.internal/v1/pki/ca" \
│       crl_distribution_points="https://vault.internal/v1/pki/crl"
│                                                                 │
│  6. Cross-signing for external trust (multi-cloud)             │
│     vault write pki_int/root/generate/internal ...              │
│     vault write pki_int/roles/myapp issuer_ref="intermediate-ca"
└─────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────┐
│ Transit Encryption Service                                       │
│                                                                 │
│  1. Enable transit engine                                       │
│     vault secrets enable -path=transit transit                   │
│                                                                 │
│  2. Create encryption key                                       │
│     vault write transit/keys/myapp-key \                        │
│       type=aes256-gcm96 \                                       │
│       derived=true \                                            │
│       exportable=false                                          │
│                                                                 │
│  3. Encrypt data (client-side encryption)                        │
│     vault write transit/encrypt/myapp-key \                     │
│       plaintext="$(echo -n 'sensitive data' | base64)"        │
│     -> Returns ciphertext: vault:v1:...                         │
│                                                                 │
│  4. Decrypt data                                                │
│     vault write transit/decrypt/myapp-key \                     │
│       ciphertext="vault:v1:..."                                │
│     -> Returns plaintext                                        │
│                                                                 │
│  5. Key rotation (without re-encrypting existing data)          │
│     vault write transit/keys/myapp-key rotate=true              │
│                                                                 │
│  6. Rewrap (re-encrypt old data with new key version)           │
│     vault write transit/rewrap/myapp-key \                       │
│       ciphertext="vault:v1:oldCiphertext"                      │
│     -> Returns vault:v2:... (encrypted under newest key)        │
│                                                                 │
│  7. HashiCorp Vault handles key versioning automatically        │
│     All versions stored, old data readable, new data uses latest
└─────────────────────────────────────────────────────────────────┘
```
