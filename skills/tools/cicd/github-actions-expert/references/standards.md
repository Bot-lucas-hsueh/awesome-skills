# Standards & Reference

## 7.1 Official Documentation

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Workflow Syntax Reference](https://docs.github.com/en/actions/using-workflows/workflow-syntax-for-github-actions)
- [Expression Syntax](https://docs.github.com/en/actions/learn-github-actions/expressions)
- [Context Reference](https://docs.github.com/en/actions/learn-github-actions/contexts)
- [Actions Marketplace](https://github.com/marketplace?type=actions)

## 7.2 Workflow Syntax

### Triggers

```yaml
on:
  push:
    branches: [main, develop]
    paths:
      - 'src/**'
      - 'package.json'
    tags:
      - 'v*'
  pull_request:
    branches: [main]
    types: [opened, synchronize, closed]
  schedule:
    - cron: '0 2 * * *'
  workflow_dispatch:
    inputs:
      environment:
        type: choice
        options: [staging, production]
```

### Job Configuration

```yaml
jobs:
  build:
    runs-on: ubuntu-latest
    timeout-minutes: 30
    continue-on-error: false
    outputs:
      version: ${{ steps.version.outputs.version }}
    steps:
      - id: version
        run: echo "version=1.0.0" >> $GITHUB_OUTPUT
```

### Matrix Strategy

```yaml
strategy:
  fail-fast: false
  matrix:
    node: [16, 18, 20]
    os: [ubuntu-latest, windows-latest]
    include:
      - node: 20
        os: ubuntu-latest
        coverage: true
```

## 7.3 Best Practices

| Practice | Description |
|----------|-------------|
| **Pin versions** | Use `@v4` not `@latest` for actions |
| **Add timeout** | Prevent stuck builds with `timeout-minutes` |
| **Cache dependencies** | Use built-in cache in setup actions |
| **Fail fast** | Lint before tests, unit before integration |
| **Use environments** | Protect production deployments |

## 7.4 Permissions

```yaml
permissions:
  contents: read
  actions: read
  statuses: read
  deployments: write
  security-events: write
```

Minimum required permissions for typical workflows. Use [permissions calculator](https://docs.github.com/en/actions/security-guides/automatic-token-authentication#permissions-for-the-github_token).