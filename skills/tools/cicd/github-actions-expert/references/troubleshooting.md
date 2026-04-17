# Troubleshooting

## 8.1 Common Failures

### Build Failures

| Error | Cause | Solution |
|-------|-------|----------|
| `No such file or directory` | Wrong working directory | Add `working-directory` or `cd` |
| `command not found` | Tool not installed | Add setup step or install in before_script |
| `permission denied` | File not executable | Add `chmod +x` step |
| `module not found` | Dependencies not installed | Add install step |

### Checkout Issues

| Issue | Fix |
|-------|-----|
| Large repo slow checkout | Use `fetch-depth: 1` for shallow clone |
| Submodules not fetched | Add `fetch-depth: 0` and `submodules: recursive` |
| LFS files not retrieved | Add `lfs: true` to checkout action |

### Network Issues

```yaml
- name: Retry with timeout
  uses: nick-invision/retry@v2
  with:
    timeout_minutes: 5
    max_attempts: 3
    command: npm ci
```

## 8.2 Debugging

### Enable Debug Logging

1. Add `ACTIONS_RUNNER_DEBUG: true` to repository secrets
2. Add `ACTIONS_STEP_DEBUG: true` to repository secrets

### Interactive Debugging

```yaml
- name: Debug shell
  run: |
    echo "Debug info"
    env | sort
    ls -la
```

### Re-run Failed Jobs

- Use "Re-run all failed jobs" in Actions UI
- Use `gh run rerun` CLI command

## 8.3 Secrets Management

### Accessing Secrets

```yaml
steps:
  - name: Use secret
    env:
      API_KEY: ${{ secrets.API_KEY }}
    run: echo "Using $API_KEY"
```

### Masking Sensitive Data

```yaml
- name: Mask secret
  run: echo "::add-mask::$SECRET_VALUE"
```

### Troubleshooting Secret Issues

| Problem | Cause | Fix |
|---------|-------|-----|
| Secret empty | Not set in repo settings | Add to repository secrets |
| Secret not available | Wrong scope | Use organization secrets |
| Permission denied | Workflow not approved | Require approval for external PRs |

## 8.4 Cache Debugging

```yaml
- name: Cache debugging
  run: |
    echo "Cache key: ${{ hashFiles('**/package-lock.json') }}"
    ls -la ${{ steps.cache.outputs.cache-path }}
```

### Cache Not Restored

- Verify cache key matches
- Check if cache was created successfully
- Ensure cache action version supports your runner