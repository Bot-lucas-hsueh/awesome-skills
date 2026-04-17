## 10. Common Pitfalls & Anti-Patterns

### 🔴 High Severity

**Anti-Pattern 1: Secrets in Environment Variables

```markdown
❌ BAD: ENV vars in Docker Compose
  DB_PASSWORD=prod-password-123
  AWS_SECRET_KEY=AKIAIOSFODNN7EXAMPLE
  # Visible in: kubectl describe pod, docker inspect, CloudTrail logs,
  # CI/CD logs if printed, and any code that calls os.environ.items()

✅ GOOD: Dynamic secrets via Vault or AWS Secrets Manager
  - vault read aws/creds/app-role → ephemeral credentials, auto-expire after 1h
  - Kubernetes External Secrets Operator → sync from Secrets Manager to K8s Secret
  - Never store secrets in env vars, ConfigMaps, Docker images, or git
```

**Anti-Pattern 2: Running Containers as Root

```markdown
❌ BAD: Default Dockerfile with no USER directive
  FROM node:20
  COPY . .
  CMD ["node", "server.js"]  # Runs as root (UID 0)
  # Container escape vulnerability → attacker becomes host root

✅ GOOD: Explicit non-root user
  FROM node:20-alpine
  RUN addgroup -g 1001 -S nodejs && adduser -S -u 1001 -G nodejs nodejs
  USER nodejs
  COPY --chown=nodejs:nodejs . .
  CMD ["node", "server.js"]
  # Enforce with OPA: runAsNonRoot: true in pod security context
```

**Anti-Pattern 3: Trusting JWT Expiry for Revocation

```markdown
❌ BAD: Assuming expired JWTs are automatically invalid for revocation
  # User is compromised; you want to revoke their access immediately
  # But their JWT has 15 minutes remaining
  # → Attacker continues to access the API for 15 more minutes

✅ GOOD: Maintain a token revocation list (Redis with TTL)
  # On logout or compromise detection:
  redis.setex(f"revoked:{jti}", token_ttl_seconds, "1")
  # On every request:
  if redis.get(f"revoked:{payload.jti}"):
      raise HTTPException(401, "Token revoked")
```

### 🟡 Medium Severity

**Anti-Pattern 4: Using MD5/SHA1 for Password Hashing / 用 MD5/SHA1 哈希密码**

```markdown
❌ BAD: SHA-256 or MD5 for passwords (fast hash = crackable)
  password_hash = hashlib.sha256(password.encode()).hexdigest()
  # GPU can try 10 billion SHA-256 hashes/second → 8-char password cracked in minutes

✅ GOOD: Argon2 (OWASP recommended, 2026)
  from argon2 import PasswordHasher
  ph = PasswordHasher(time_cost=2, memory_cost=65536, parallelism=2)
  hash = ph.hash(password)
  ph.verify(hash, user_input)  # Raises VerifyMismatchError if wrong
  # GPU can try ~100 Argon2 hashes/second → same password takes 100M× longer
```

**Anti-Pattern 5: Verbose Error Messages in Production

```markdown
❌ BAD: Exposing stack traces and internal paths to users
  {"error": "psycopg2.OperationalError: FATAL: database 'users' does not exist
              File '/app/database.py', line 45 in connect()
              connection string: postgresql://admin:P@ssw0rd@db-prod:5432/users"}
  # Reveals: DB host, port, username, password, file paths, tech stack

✅ GOOD: Generic error to client, detailed log internally
  # Client receives:
  {"error": {"code": "INTERNAL_ERROR", "message": "An error occurred. Request ID: req-xyz"}}
  # Internal structured log includes full stack trace + context for debugging
  logger.error("DB connection failed", exc_info=True, extra={"request_id": req_id})
```

---

