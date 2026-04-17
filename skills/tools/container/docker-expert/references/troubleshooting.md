# Troubleshooting

## 8.1 Container Build Failures

### "no such file or directory" Error

**Symptoms:** Build fails with `COPY failed: file not found` or `no such file or directory`

**Common Causes:**

| Cause | Diagnosis | Fix |
|-------|-----------|-----|
| Wrong build context | Check where you're running `docker build` | Use `-f path/to/Dockerfile` with correct context |
| File not in context | `ls` the file in context directory | Ensure file exists in build context |
| .dockerignore too aggressive | Check `.dockerignore` | Exclude only necessary files |
| Path case sensitivity | Linux vs Windows paths | Match exact case |

**Debug Steps:**
```bash
# View build context sent to Docker
docker build --progress=plain .
# Look for: "Sending build context to Docker daemon X MB"

# Check what files are in context
docker build -f Dockerfile . --no-cache 2>&1 | grep -E "COPY|ADD"

# Verify file exists
docker run --rm -v $(pwd):/workspace alpine ls -la /workspace
```

### "Step failed" in RUN Command

**Symptoms:** `The command '/bin/sh -c npm install' returned a non-zero code: 1`

**Diagnosis:**
```bash
# Run with verbose output
docker build --progress=plain .

# Check specific layer by adding && echo "success"
RUN npm install 2>&1 || (echo "=== ERROR OUTPUT ===" && cat /tmp/npm-debug.log 2>/dev/null || true)
```

**Common Solutions:**

| Error | Cause | Fix |
|-------|-------|-----|
| EACCES permission | Running as root in base image | Add `USER node` before npm |
| Network timeout | Slow build network | Add `RUN npm config set registry` |
| Memory limit | OOM during build | Increase Docker desktop memory |
| Missing deps | package-lock.json mismatch | Clear cache: `docker builder prune` |

### Layer Caching Issues

**Symptoms:** Build is slow, caches aren't being used

**Solution:**
```dockerfile
# BAD: Changes invalidate everything
COPY . .
RUN npm install

# GOOD: Dependencies cached separately
COPY package*.json ./
RUN npm ci
COPY . .
```

## 8.2 Runtime Issues

### Container Exits Immediately

**Diagnosis:**
```bash
# Check exit code
docker ps -a
docker inspect <container> --format='{{.State.ExitCode}}'

# View logs
docker logs <container>
docker logs <container> --tail 100
```

**Common Causes:**

| Exit Code | Meaning | Fix |
|-----------|---------|-----|
| 0 | Exited normally | Check CMD/ENTRYPOINT |
| 1 | Application error | Check logs for errors |
| 125 | Docker daemon error | Check dockerd logs |
| 126 | CMD not executable | Fix file permissions |
| 127 | CMD not found | Verify PATH |

### "Connection Refused" in Container

**Symptoms:** `dial tcp: connection refused` when container tries to connect

**Diagnosis:**
```bash
# Check if port is listening in container
docker exec <container> netstat -tlnp
docker exec <container> ss -tlnp

# Check from host
docker port <container>

# Test locally in container
docker exec <container> curl localhost:8080
```

**Solutions:**
- Ensure app binds to `0.0.0.0` not `127.0.0.1`
- Verify `EXPOSE` matches actual port
- Check app started before health check

### "Permission Denied" Errors

**Symptoms:** Cannot write to volume or directory

**Diagnosis:**
```bash
docker exec <container> ls -la /app/data
docker exec <container> id
```

**Solutions:**
```dockerfile
# Fix ownership in Dockerfile
COPY --chown=appuser:appuser . .
USER appuser

# Or fix at runtime
docker run -v $(pwd):/data:z app
```

## 8.3 Networking Issues

### DNS Resolution Fails

**Symptoms:** `Could not resolve host: database`

**Diagnosis:**
```bash
# Check DNS config
docker exec <container> cat /etc/resolv.conf

# Test DNS
docker exec <container> nslookup database
docker exec <container> getent hosts database
```

**Solution:**
```bash
# Add DNS server
docker run --dns 8.8.8.8 myapp

# Or in compose
services:
  app:
    dns:
      - 8.8.8.8
```

### Can't Reach Other Containers

**Symptoms:** Containers can't communicate in same compose file

**Diagnosis:**
```bash
# Check network
docker network inspect myapp_default

# Check DNS entries
docker exec <container> cat /etc/hosts
```

**Solution:**
```yaml
services:
  app:
    networks:
      - mynetwork
  db:
    networks:
      - mynetwork

networks:
  mynetwork:
    driver: bridge
```

## 8.4 Image Size Issues

### Large Image Size

**Diagnosis:**
```bash
docker image ls
docker history myimage
dive myimage
```

**Solutions:**
- Use Alpine base: `FROM node:20-alpine`
- Multi-stage builds
- Combine RUN commands: `RUN apt-get update && apt-get install -y ... && rm -rf /var/lib/apt/lists/*`
- Use `.dockerignore`
- Clean up in same layer

## 8.5 Security Issues

### Secrets in Image

**Diagnosis:**
```bash
# Check for secrets in layers
docker history myimage

# Scan for secrets
docker run --rm -v $(pwd):/workspace aquasec/trivy config /workspace
```

**Solution:**
- Use Docker BuildKit secrets
- Use docker-compose secrets
- Never bake secrets in Dockerfile

### Running as Root

**Diagnosis:**
```bash
docker exec <container> id
```

**Solution:**
```dockerfile
FROM node:20-alpine
RUN addgroup -g 1000 appgroup && adduser -u 1000 -G appgroup -s /bin/sh -D appuser
USER appuser
```

## 8.6 Health Check Issues

### Health Check Always Failing

**Diagnosis:**
```bash
docker inspect --format='{{.State.Health}}' <container>
```

**Solutions:**
```dockerfile
# Make health check more tolerant
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Or for Alpine without curl
HEALTHCHECK --interval=30s --timeout=10s --start-period=60s --retries=3 \
  CMD wget -qO- http://localhost:8080/health || exit 1
```