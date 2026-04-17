# Troubleshooting

## 8.1 Common Failures

### Job Failures

| Error | Cause | Solution |
|-------|-------|----------|
| `runner not found` | No runner with matching tags | Add runner or modify tags |
| `script failure` | Non-zero exit code | Check script output, add error handling |
| `timeout` | Job exceeded max execution time | Increase timeout or optimize |
| `mount volume failed` | Docker executor permission issue | Check volume paths |

### Git Problems

| Issue | Fix |
|-------|-----|
| Shallow clone | Use `GIT_DEPTH` variable |
| Submodules | Add `GIT_SUBMODULE_STRATEGY` |
| Large repos | Use `GIT_STRATEGY: fetch` with `GIT_DEPTH` |

### Network Issues

```yaml
retry:
  max: 2
  when:
    - runner_system_failure
    - stuck_or_timeout_failure

job:
  script:
    - !reference [.retry, script]
```

## 8.2 Debugging

### Enable Debug

```yaml
variables:
  CI_DEBUG_TRACE: "true"
```

### Debug Script

```yaml
debug:
  script:
    - echo "Debug: $(env)"
    - whoami
    - pwd
    - ls -la
```

### Using GitLab UI

- View job log with ANSI colors
- Use "Retry" for failed jobs
- Check "Clean up" for stuck jobs

## 8.3 Secrets & Variables

### CI/CD Variables

| Variable | Description |
|----------|-------------|
| `CI_JOB_TOKEN` | Token for API access |
| `CI_PIPELINE_URL` | Current pipeline URL |
| `CI_COMMIT_SHA` | Current commit SHA |
| `CI_REGISTRY_IMAGE` | Container registry image |

### Troubleshooting Secrets

| Problem | Fix |
|---------|-----|
| Variable not found | Check scope (project/group) |
| Masked output | Add to masking pattern |
| Not available in job | Check `rules:` or `needs:` |

## 8.4 Runner Issues

### Check Runner Status

```bash
gitlab-runner verify
gitlab-runner list
```

### Common Runner Problems

- Runner offline: Check service/agent status
- No matching tags: Review job tag requirements
- Executor issues: Verify Docker/system setup

### Self-Hosted Runner Registration

```bash
gitlab-runner register \
  --url https://gitlab.com \
  --token "REGISTRATION_TOKEN" \
  --executor docker \
  --docker-image docker:20.10.16 \
  --description "docker-runner"
```