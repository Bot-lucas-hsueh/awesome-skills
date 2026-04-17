# Standards & Reference

## 7.1 Official Documentation

- [Docker Engine Overview](https://docs.docker.com/engine/)
- [Dockerfile Best Practices](https://docs.docker.com/develop/develop-images/dockerfile_best-practices/)
- [Docker Build Guide](https://docs.docker.com/build/)
- [Docker Compose Reference](https://docs.docker.com/compose/compose-file/)
- [Docker Security](https://docs.docker.com/engine/security/)
- [Docker API v1.44](https://docs.docker.com/engine/api/v1.44/)

## 7.2 Architecture Patterns

### Multi-Stage Build Pattern

```dockerfile
# Build stage
FROM node:20-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci
COPY . .
RUN npm run build

# Production stage
FROM node:20-alpine
WORKDIR /app
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/node_modules ./node_modules
COPY package*.json .
USER node
CMD ["node", "dist/index.js"]
```

### Builder Pattern with Cache Optimization

```dockerfile
# Dependencies layer (changes infrequently)
FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Source code layer (changes frequently)
COPY . .
CMD ["python", "app.py"]
```

### Security Hardening Pattern

```dockerfile
FROM python:3.11-slim
RUN groupadd -r appgroup && useradd -r -g appgroup appuser
WORKDIR /app
COPY --chown=appuser:appuser . .
USER appuser
RUN chmod 500 /app/entrypoint.sh
CMD ["/app/entrypoint.sh"]
```

## 7.3 Best Practices Checklist

| Category | Requirement | Implementation |
|----------|-------------|----------------|
| **Base Image** | Use specific version tags | `FROM node:20-alpine` not `node:latest` |
| **Non-root** | Run as non-root user | `USER appuser` |
| **Layer caching** | Copy dependencies first | Separate RUN for dependencies |
| **Security** | Drop all capabilities | `security-opt: no-new-privileges:true` |
| **Health** | Include health check | `HEALTHCHECK --interval=30s ...` |
| **Secrets** | Never in Dockerfile | Use `--secret` or Docker BuildKit |
| **Output** | Multi-platform builds | `docker buildx build --platform` |

## 7.4 Configuration Reference

### Docker Compose v3 Reference

```yaml
version: '3.8'
services:
  web:
    build:
      context: .
      dockerfile: Dockerfile
      args:
        BUILD_VERSION: v1.0
    ports:
      - "8080:8080"
    environment:
      - NODE_ENV=production
      - DB_HOST=postgres
    depends_on:
      db:
        condition: service_healthy
      redis:
        condition: service_started
    healthcheck:
      test: ["CMD", "curl", "-f", "http://localhost:8080/health"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 40s
    restart: unless-stopped
    networks:
      - frontend
      - backend

networks:
  frontend:
    driver: bridge
  backend:
    driver: bridge

volumes:
  db-data:
```

### BuildKit Secrets

```dockerfile
# syntax=docker/dockerfile:1.4
FROM node:20-alpine
RUN --mount=type=secret,id=npm_token \
  NPM_TOKEN=$(cat /run/secrets/npm_token) && \
  echo "//registry.npmjs.org/:_authToken=$NPM_TOKEN" > .npmrc
```

## 7.5 Version Compatibility

| Docker Version | BuildKit | Buildx | Compose v3 |
|----------------|----------|--------|------------|
| 20.10+ | ✅ Native | ✅ Bundled | ✅ Full |
| 19.03 | ✅ Separate | ✅ Plugin | ✅ Full |
| 18.09 | ⚠️ Opt-in | ⚠️ Plugin | ⚠️ Partial |

## 7.6 Common Commands

```bash
# Build with BuildKit
DOCKER_BUILDKIT=1 docker build .

# Multi-platform build
docker buildx build --platform linux/amd64,linux/arm64 -t myapp:latest .

# Scan for vulnerabilities
docker scan myapp:latest

# Analyze image layers
dive myapp:latest

# Lint Dockerfile
hadolint Dockerfile

# Pull with all platforms
docker buildx build --platform all --push -t myapp:latest .
```