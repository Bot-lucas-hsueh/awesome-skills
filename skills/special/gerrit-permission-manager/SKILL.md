---
name: gerrit-permission-manager
display_name: Gerrit Permission Manager / Gerrit权限管理专家
author: neo.ai
version: 1.0.0
difficulty: expert
category: special
tags: [gerrit, permissions, code-review, access-control, devops]
platforms: [opencode, openclaw, claude, cursor, codex, cline, kimi]
description: >
  Expert manager for Gerrit multi-repository and multi-branch permission configurations.
  Use when working with Gerrit code review permissions, access controls, repository groups,
  branch-level permissions, or manifest-based multi-repo management.
  Triggers: "gerrit permissions", "repo groups", "branch protection", "Gerrit access control".
  Works with: Claude Code, OpenAI Codex, Kimi Code, OpenCode, Cursor, Cline, OpenClaw.
---

# Gerrit Permission Manager

Manage complex permission structures across multiple Gerrit repositories and branches.

## Capabilities

1. **Multi-Repository Permission Management** - Batch configure permissions across repository groups
2. **Branch-Level Access Control** - Fine-grained permissions per branch pattern
3. **Manifest Repository Management** - Create and maintain manifest files for repo tool
4. **Permission Templates** - Reusable permission configurations for common patterns (standard, restricted, protected-branches, multi-team, git-flow)
5. **Bulk Operations** - Apply changes across multiple repos/branches efficiently
6. **Permission Viewing & Export** - View, export permissions in multiple formats (table, JSON, YAML)
7. **Statistics & Analytics** - Analyze permission usage, group references, security coverage
8. **Security Auditing** - Automated security checks with scoring and compliance reporting
9. **Drift Detection** - Compare repositories and detect configuration drift from templates

## Quick Start

### Create Manifest Repository

```bash
# Create manifest repo for managing 10+ repositories
./scripts/create-manifest-repo.sh <manifest-name> <repo-list-file>
```

### Apply Permission Template

```bash
# Apply standard permissions to a repository
./scripts/apply-permissions.sh --repo <repo-name> --template <template-name>
```

### Bulk Permission Update

```bash
# Update permissions across multiple repos
./scripts/bulk-update.sh --manifest <manifest.xml> --permission-file <permissions.json>
```

### View Permissions

```bash
# View permissions for all repositories
./scripts/view-permissions.sh --all

# Export to JSON
./scripts/view-permissions.sh --all --format json --export perms.json
```

### Security Audit

```bash
# Run security audit on all repos
./scripts/audit-permissions.sh --all

# Check compliance with scoring
./scripts/audit-permissions.sh --all --strict --report audit.json
```

### Statistics & Analytics

```bash
# Get permission statistics
./scripts/stats-permissions.sh --all

# Compare two repositories
./scripts/compare-permissions.sh --source repo1 --target repo2

# Check drift from template
./scripts/compare-permissions.sh --check-drift myrepo --template git-flow
```

## Permission Templates

See [references/permission-templates.md](references/permission-templates.md) for predefined templates:
- `standard` - Standard open source project permissions
- `restricted` - Restricted access, limited submitters
- `protected-branches` - Main branch protection with review requirements
- `multi-team` - Multiple team access with different levels
- `git-flow` - Git Flow workflow with branch-based permissions (see Git Flow section below)

## Core Workflows

### 1. Setup New Repository Group

```bash
# 1. Create manifest repository
./scripts/create-manifest-repo.sh my-project-manifest repos.txt

# 2. Define permission structure
# Edit references/permissions.json

# 3. Apply to all repos in manifest
./scripts/bulk-update.sh --manifest my-project-manifest/default.xml
```

### 2. Add Branch Protection

```bash
# Protect main/master branches
./scripts/branch-protection.sh --repo <repo> --branch "refs/heads/main" \
  --require-review 2 --require-submit-access
```

### 3. Grant Team Access

```bash
# Grant team access to repository group
./scripts/grant-team-access.sh --manifest <manifest> --team <team-name> --access-level <level>
```

## Configuration Format

### Manifest File (repo tool)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<manifest>
  <remote name="origin" fetch="http://localhost:8080/" />
  <default remote="origin" revision="main" />
  
  <project path="repo1" name="repo1" />
  <project path="repo2" name="repo2" />
  <!-- ... more repos -->
</manifest>
```

### Permissions JSON

```json
{
  "refs/heads/main": {
    "read": ["Registered Users"],
    "submit": ["Project Owners", "Maintainers"],
    "label-Code-Review": {
      "-2..+2": ["Maintainers"],
      "-1..+1": ["Registered Users"]
    }
  },
  "refs/heads/develop": {
    "submit": ["Developers", "Maintainers"]
  }
}
```

## Gerrit REST API Integration

Use provided scripts to interact with Gerrit REST API:

```bash
# List all projects
./scripts/gerrit-api.sh GET /projects/

# Get project access
./scripts/gerrit-api.sh GET /projects/myproject/access/

# Set project access
./scripts/gerrit-api.sh POST /projects/myproject/access/ --data @permissions.json
```

## SSH Commands

```bash
# Create group
ssh -p 29418 admin@localhost gerrit create-group developers

# Add member to group
ssh -p 29418 admin@localhost gerrit set-members --add user@example.com developers

# List groups
ssh -p 29418 admin@localhost gerrit ls-groups
```

## Git Flow Workflow

Git Flow is a branching model that provides a robust framework for managing larger projects. This skill includes a complete Git Flow permission template.

### Branch Structure

```
master/main (production)
    ↑
develop (integration)
    ↑
feature/* → release/* → hotfix/*
```

### Permission Roles

| Role | master | develop | feature/* | release/* | hotfix/* |
|------|--------|---------|-----------|-----------|----------|
| **Project Owners** | Submit, Push | Submit, Push | All | All | All |
| **Release Managers** | Submit (2+ reviews) | Submit | - | Submit, Create | Submit, Create |
| **Team Leads** | - | Submit (1+ review) | Submit, Create, Push | - | Create |
| **Developers** | - | Push | Create, Push | - | - |
| **CI Bot** | Verify | Verify | Verify | Verify | Verify |

### Apply Git Flow Permissions

```bash
# Apply Git Flow template to a repository
./scripts/apply-permissions.sh --repo myproject --template git-flow

# Apply to all repos in manifest
./scripts/bulk-update.sh --manifest my-manifest/default.xml --template git-flow
```

### Git Flow Workflow Commands

```bash
# 1. Start a new feature
repo start feature/login --all

# 2. Work on feature and push for review
git push origin HEAD:refs/for/develop

# 3. When feature is done, merge to develop
# (Through Gerrit UI with Team Lead approval)

# 4. Create release branch (Release Manager only)
git checkout -b release/v1.2.0 develop
git push origin release/v1.2.0

# 5. After release testing, merge to master
git checkout master
git merge --no-ff release/v1.2.0
git push origin HEAD:refs/for/master

# 6. Create hotfix (for production issues)
git checkout -b hotfix/critical-fix master
git push origin HEAD:refs/for/master
```

### Protected Branches Rules

- **master**: Requires 2 code reviews from Release Managers or Project Owners
- **develop**: Requires 1 code review from Team Leads or above
- **release/***: Requires 2 code reviews, only Release Managers can create/merge
- **hotfix/***: Requires 1 code review, can be created by Team Leads in emergencies
- **feature/***: Developers have full control, no restrictions

See [references/git-flow.md](references/git-flow.md) for detailed workflow documentation.

## Permission Auditing & Statistics

### View Current Permissions

```bash
# View single repository permissions
./scripts/view-permissions.sh --repo myproject

# View all repositories in table format
./scripts/view-permissions.sh --all

# Export to JSON
./scripts/view-permissions.sh --all --format json --export permissions.json

# View from manifest
./scripts/view-permissions.sh --manifest default.xml --format yaml
```

### Permission Statistics

```bash
# Get statistics for all repositories
./scripts/stats-permissions.sh --all

# Statistics for specific manifest
./scripts/stats-permissions.sh --manifest default.xml

# Export statistics
./scripts/stats-permissions.sh --all --export stats.json
```

**Statistics include:**
- Total repositories and branch rules
- Unique groups count
- Most complex repositories
- Permission type distribution
- Most referenced groups
- Security coverage metrics

### Security Audit

```bash
# Basic audit
./scripts/audit-permissions.sh --all

# Strict mode (exit on warnings)
./scripts/audit-permissions.sh --all --strict

# Generate audit report
./scripts/audit-permissions.sh --all --report audit-report.json

# Audit specific repository
./scripts/audit-permissions.sh --repo myproject
```

**Audit Checks:**
- ✅ Master branch protection
- ✅ Code review requirements
- ✅ Anonymous access detection
- ✅ Overly permissive groups
- ✅ Separation of duties
- ✅ Force push protection

**Security Score:** 0-100 rating based on findings

## Troubleshooting

### Permission Denied

```bash
# Check current permissions
ssh -p 29418 admin@localhost gerrit query --current-patch-set project:myproject
```

### Manifest Sync Issues

```bash
# Re-sync all repos
repo forall -c 'git fetch origin'
```
