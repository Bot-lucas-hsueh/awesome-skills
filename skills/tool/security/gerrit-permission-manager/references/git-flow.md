# Git Flow Workflow Documentation

Complete guide for using Git Flow with Gerrit permission management.

## Overview

Git Flow is a branching strategy designed by Vincent Driessen that provides a robust framework for managing larger projects with scheduled release cycles.

## Branch Types

### 1. Master/Main Branch

**Purpose**: Production-ready code
**Protection Level**: Highest
**Permissions**:
- Read: All users
- Submit: Project Owners, Release Managers (requires 2 reviews)
- Push: Project Owners only
- Direct push: Blocked

**Characteristics**:
- Always deployable
- Tagged with version numbers
- Only receives merges from release/* and hotfix/* branches

### 2. Develop Branch

**Purpose**: Integration branch for features
**Protection Level**: High
**Permissions**:
- Read: All registered users
- Submit: Project Owners, Release Managers, Team Leads (requires 1 review)
- Push: Team Leads and above
- Create feature branches from here

**Characteristics**:
- Contains latest development changes
- Base for feature branches
- Collects completed features

### 3. Feature Branches

**Pattern**: `feature/*` or `feature/TICKET-description`
**Purpose**: Develop new features
**Protection Level**: Low (developer freedom)
**Permissions**:
- Read: All registered users
- Create: Developers, Team Leads
- Push: Developers, Team Leads
- Submit: Team Leads
- Delete: Creator or Team Leads

**Lifecycle**:
```bash
# Create from develop
repo start feature/ABC-123-login develop

# Develop and commit
git add .
git commit -m "ABC-123: Add user login"

# Push for code review
git push origin HEAD:refs/for/develop

# After approval, merge via Gerrit UI
# Branch can be deleted after merge
```

### 4. Release Branches

**Pattern**: `release/v{major}.{minor}.{patch}`
**Purpose**: Prepare for production release
**Protection Level**: Very High
**Permissions**:
- Read: All registered users
- Create: Release Managers, Project Owners
- Push: Release Managers, Project Owners
- Submit: Release Managers, Project Owners (requires 2 reviews)

**Lifecycle**:
```bash
# Create from develop when ready to release
git checkout -b release/v1.2.0 develop

# Only bug fixes, no new features
git commit -m "Fix: Resolve login issue"

# Push for review (strict approval required)
git push origin HEAD:refs/for/master
git push origin HEAD:refs/for/develop

# After approval:
# - Merge to master (triggers production deployment)
# - Merge back to develop
# - Tag the release on master
```

### 5. Hotfix Branches

**Pattern**: `hotfix/v{version}-{description}`
**Purpose**: Critical production fixes
**Protection Level**: High
**Permissions**:
- Read: All registered users
- Create: Release Managers, Project Owners, Team Leads (emergency)
- Push: Release Managers, Project Owners
- Submit: Release Managers, Project Owners (requires 1 review, expedited)

**Lifecycle**:
```bash
# Create from master for urgent fix
git checkout -b hotfix/v1.2.1-login-fix master

# Fix the issue
git commit -m "HOTFIX: Fix critical login bug"

# Push with high priority
git push origin HEAD:refs/for/master

# After approval:
# - Merge to master
# - Merge to develop
# - Tag emergency release
```

## Permission Groups

### Project Owners
- **Members**: Project leads, architects
- **Responsibilities**: 
  - Repository administration
  - Critical production decisions
  - Override emergencies
- **Permissions**: All actions on all branches

### Release Managers
- **Members**: Senior developers, DevOps leads
- **Responsibilities**:
  - Managing release cycles
  - Approving master merges
  - Hotfix coordination
- **Permissions**:
  - Submit to master (with 2 reviews)
  - Full control of release/* branches
  - Full control of hotfix/* branches
  - Submit to develop

### Team Leads
- **Members**: Feature team leads
- **Responsibilities**:
  - Code review
  - Feature branch management
  - Develop branch maintenance
- **Permissions**:
  - Submit to develop (with 1 review)
  - Submit feature branches
  - Create hotfix branches (emergency)

### Developers
- **Members**: Regular developers
- **Responsibilities**:
  - Feature development
  - Code review participation
  - Bug fixes
- **Permissions**:
  - Create feature branches
  - Push to feature branches
  - Push to develop (via review)

### CI Bot
- **Members**: Automated systems (Jenkins, GitLab CI, etc.)
- **Responsibilities**:
  - Automated testing
  - Build verification
- **Permissions**:
  - Read all branches
  - Label-Verified on all branches

## Code Review Requirements

### Master Branch
- **Minimum Score**: +2 Code-Review
- **Required Reviewers**: 2
- **Who can approve**: Release Managers, Project Owners
- **Additional Requirements**:
  - All tests must pass (Verified +1)
  - No unresolved comments
  - Up-to-date with target branch

### Develop Branch
- **Minimum Score**: +1 Code-Review
- **Required Reviewers**: 1
- **Who can approve**: Team Leads, Release Managers, Project Owners
- **Additional Requirements**:
  - Tests passing recommended

### Release Branches
- **Minimum Score**: +2 Code-Review
- **Required Reviewers**: 2
- **Who can approve**: Release Managers, Project Owners
- **Additional Requirements**:
  - Full test suite passing
  - QA approval
  - Documentation updated

### Hotfix Branches
- **Minimum Score**: +1 Code-Review
- **Required Reviewers**: 1
- **Who can approve**: Release Managers, Project Owners
- **Additional Requirements**:
  - Critical issue verification
  - Expedited review process

## Typical Workflow Examples

### Example 1: New Feature Development

```bash
# 1. Sync all repos
repo sync

# 2. Start feature branch
repo start feature/ABC-456-user-profile

# 3. Work on feature
cd repo1
# ... make changes ...
git add .
git commit -m "ABC-456: Add user profile page"

# 4. Push for code review
git push origin HEAD:refs/for/develop

# 5. Address review comments
# ... make fixes ...
git commit --amend
git push origin HEAD:refs/for/develop

# 6. Team Lead merges to develop via Gerrit UI

# 7. Complete and delete branch
repo prune
```

### Example 2: Release Process

```bash
# 1. Ensure develop is stable
repo sync

# 2. Create release branch (Release Manager)
repo start release/v2.0.0 develop

# 3. Stabilization period
# - Only bug fixes
# - No new features
# - QA testing

# 4. Push release to master (Release Manager)
git push origin HEAD:refs/for/master

# 5. After approval and merge, tag release
git checkout master
git pull
git tag -a v2.0.0 -m "Release version 2.0.0"
git push origin v2.0.0

# 6. Merge back to develop
git checkout develop
git merge --no-ff release/v2.0.0
git push origin develop
```

### Example 3: Hotfix Process

```bash
# 1. Create hotfix from master
git checkout master
git pull
repo start hotfix/v2.0.1-critical-fix master

# 2. Fix the issue
git commit -m "HOTFIX: Fix critical security issue"

# 3. Push with high priority
git push origin HEAD:refs/for/master

# 4. Expedited review by Release Manager

# 5. After merge, tag and deploy
git checkout master
git pull
git tag -a v2.0.1 -m "Hotfix v2.0.1"
git push origin v2.0.1

# 6. Merge to develop
git checkout develop
git merge --no-ff hotfix/v2.0.1-critical-fix
git push origin develop
```

## Best Practices

### Branch Naming Conventions

- **Features**: `feature/TICKET-123-short-description`
- **Releases**: `release/v{major}.{minor}.{patch}`
- **Hotfixes**: `hotfix/v{version}-{short-description}`

### Commit Message Guidelines

- Reference ticket: `ABC-123: Add user authentication`
- Hotfixes: `HOTFIX: Fix production crash`
- Releases: `RELEASE: Version 2.0.0`

### Review Guidelines

- All code must be reviewed before merging
- Use Gerrit's comment threads for discussions
- Resolve all comments before submitting
- Keep changes focused and small

### Emergency Procedures

When critical production issues occur:

1. **Team Lead** can create hotfix branch
2. **Release Manager** gets immediate notification
3. Expedited review (1 approval required)
4. Deploy immediately after merge
5. Post-mortem within 24 hours

## Permission Configuration

Apply Git Flow permissions using:

```bash
# Single repository
./scripts/apply-permissions.sh --repo myproject --template git-flow

# All repositories in manifest
./scripts/bulk-update.sh --manifest default.xml --template git-flow

# Verify permissions
./scripts/gerrit-api.sh GET /projects/myproject/access/
```

## Troubleshooting

### "Permission denied" on master

Ensure:
1. You have Release Manager or Project Owner role
2. Code has 2 Code-Review +2 approvals
3. All tests passing (Verified +1)

### Cannot create release branch

Only Release Managers and Project Owners can create release/* branches. Contact them to create the branch.

### Feature branch not merging

Check:
1. Branch is based on latest develop
2. All conflicts resolved
3. At least 1 Code-Review +1
4. No unresolved comments
