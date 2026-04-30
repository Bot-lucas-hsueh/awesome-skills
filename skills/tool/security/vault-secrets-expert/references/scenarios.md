# Scenario Examples

## 9.1 Kubernetes Application

**User:** "Integrate Vault with Kubernetes application"

**Vault Expert:**
> **Setup:**
>
> ```bash
> # 1. Enable Kubernetes auth on Vault
> vault auth enable kubernetes
>
> # 2. Create policy for the app
> cat > myapp-policy.hcl << 'EOF'
> path "secret/data/myapp/*" {
>     capabilities = ["read"]
> }
> path "database/creds/myapp-db" {
>     capabilities = ["read"]
> }
> EOF
> vault policy write myapp myapp-policy.hcl
>
> # 3. Create Kubernetes role
> vault write auth/kubernetes/role/myapp \
>     bound_service_account_names=myapp-sa \
>     bound_service_account_namespaces=default \
>     policies=myapp \
>     ttl=24h
> ```
>
> **Application Code (Python):**
>
> ```python
> import hvac
>
> client = hvac.Client()
>
> # Read database credentials (auto-rotated)
> db_creds = client.secrets.database.generate_credentials(
>     name='myapp-db'
> )
>
> # Read config
> config = client.secrets.kv.v2.read_secret_version(
>     path='myapp/config',
>     mount_point='secret'
> )
> ```

## 9.2 CI/CD Pipeline

**User:** "Use Vault in CI/CD pipeline"

**Vault Expert:**
> **GitHub Actions:**
>
> ```yaml
> name: Deploy
> on: [push]
> jobs:
>   deploy:
>     runs-on: ubuntu-latest
>     steps:
>       - uses: actions/checkout@v4
>
>       - name: Authenticate to Vault
>         uses: hashicorp/vault-action@v2
>         with:
>           url: https://vault.mycompany.com
>           method: github
>           github-token: ${{ secrets.GITHUB_TOKEN }}
>           secrets: |
>             secret/data/ci/myapp AWS_ACCESS_KEY_ID | AWS_ACCESS_KEY_ID ;
>             secret/data/ci/myapp AWS_SECRET_ACCESS_KEY | AWS_SECRET_ACCESS_KEY ;
>             secret/data/ci/myapp DOCKER_USERNAME | DOCKER_USERNAME ;
>             secret/data/ci/myapp DOCKER_PASSWORD | DOCKER_PASSWORD ;
>
>       - name: Deploy
>         run: ./deploy.sh
> ```

## 9.3 Certificate Automation

**User:** "Automate TLS certificate management"

**Vault Expert:**
> **Setup PKI:**
>
> ```bash
> # Enable and configure PKI
> vault secrets enable pki
> vault secrets tune -max-lease-ttl=8760h pki
>
> # Generate internal CA
> vault write pki/root/generate/internal \
>     common_name="MyCompany Internal CA" \
>     ttl=87600h
>
> # Create intermediate CA
> vault secrets enable -path=pki_int pki
> vault write pki_int/intermediate/generate/internal \
>     common_name="MyApp Intermediate CA" \
>     | vault pki_intermediate_setIssuer -
>
> # Create role
> vault write pki_int/roles/myapp \
>     allowed_domains=myapp.internal \
>     allow_subdomains=true \
>     max_ttl=72h \
>     ttl=24h
>
> # Issue certificate
> vault write pki_int/issue/myapp \
>     common_name=api.myapp.internal
> ```
>
> **Certificate Renewal Script:**
>
> ```bash
> #!/bin/bash
> CERT=$(vault write -field=certificate pki_int/issue/myapp \
>     common_name=api.myapp.internal \
>     ttl=24h)
>
> PRIVATE_KEY=$(vault write -field=private_key pki_int/issue/myapp \
>     common_name=api.myapp.internal \
>     ttl=24h)
>
> echo "$CERT" | sudo tee /etc/ssl/certs/myapp.crt
> echo "$PRIVATE_KEY" | sudo tee /etc/ssl/private/myapp.key
> sudo systemctl reload nginx
> ```
