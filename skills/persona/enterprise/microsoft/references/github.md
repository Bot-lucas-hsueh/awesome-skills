# GitHub Platform Reference

## Platform Overview

### Key Metrics (2025)
| Metric | Value |
|--------|-------|
| Developers | 100M+ |
| Repositories | 420M+ |
| Organizations | 4M+ |
| Countries | 200+ |

### GitHub Copilot
| Metric | Value |
|--------|-------|
| Total Users | 15M+ |
| Paid Subscribers | 4.7M+ |
| Fortune 100 Adoption | 90% |
| Languages Supported | 30+ |

## GitHub Products

### Free Tier
- Unlimited public/private repos
- 2,000 Actions minutes/month
- 500MB Packages storage
- Community support

### GitHub Team ($4/user/month)
- Everything in Free
- 3,000 Actions minutes/month
- 2GB Packages storage
- Advanced collaboration tools
- Code review assignments

### GitHub Enterprise ($21/user/month)
- Everything in Team
- 50,000 Actions minutes/month
- 50GB Packages storage
- SAML/SSO
- Advanced security
- Audit logs
- Priority support

## GitHub Actions

### Workflow Structure
```yaml
name: CI/CD Pipeline
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'
      - name: Install dependencies
        run: npm ci
      - name: Run tests
        run: npm test
```

### Runners
| Type | Specs | Cost |
|------|-------|------|
| Ubuntu | 2-core, 7GB RAM | $0.008/min |
| Windows | 2-core, 7GB RAM | $0.016/min |
| macOS | 3-core, 14GB RAM | $0.08/min |
| Larger runners | Up to 64-core | Custom pricing |

## GitHub Copilot Technical Details

### Model
- Base: OpenAI Codex
- Fine-tuned for code completion
- Supports 30+ programming languages

### IDE Support
| IDE | Extension |
|-----|-----------|
| VS Code | Built-in |
| Visual Studio | Official extension |
| JetBrains IDEs | Official plugin |
| Neovim | Community plugin |

### Privacy
- Code snippets may be used for training (optional opt-out)
- Enterprise version offers isolated instances
- No retention of sensitive data

## GitHub Advanced Security

### Features
| Feature | Description |
|---------|-------------|
| Code Scanning | Static analysis (CodeQL) |
| Secret Scanning | Detect leaked credentials |
| Dependency Review | Vulnerability alerts |
| Security Advisories | Responsible disclosure |

### CodeQL
- Semantic code analysis
- Custom queries
- CI/CD integration
- 100+ built-in queries

### Secret Scanning
- 100+ token types
- Partner patterns
- Custom patterns (Enterprise)
- Push protection

## GitHub API

### REST API v3
```http
GET https://api.github.com/repos/microsoft/vscode
Authorization: Bearer {token}
```

### GraphQL API v4
```graphql
query {
  repository(owner: "microsoft", name: "vscode") {
    stargazerCount
    forkCount
    issues(states: OPEN) {
      totalCount
    }
  }
}
```

### Rate Limits
| Authentication | Limit |
|----------------|-------|
| Unauthenticated | 60/hour |
| Authenticated | 5,000/hour |
| GitHub App | 15,000/hour |

---

**Last Updated**: 2026-03-21
