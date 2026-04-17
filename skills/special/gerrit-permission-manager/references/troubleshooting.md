# Gerrit Permission Troubleshooting

## Authentication & Authorization Failures

### Permission Denied on Push

**Symptom:** `remote: ERROR: permission denied` when pushing to a branch.

**Diagnosis:**
```bash
# Check current user
ssh -p 29418 admin@host gerrit gsql --format JSON -c \
  "SELECT preferred_email FROM accounts WHERE account_id IN
   (SELECT account_id FROM account_external_ids WHERE external_id = 'gerrit:username')"

# List group memberships
ssh -p 29418 admin@host gerrit ls-groups --member username@domain

# View effective access for the project
ssh -p 29418 admin@host gerrit stream-events 2>/dev/null | head -1 &
# Or use the access viewer in the Web UI under Projects > Access > View Inherited
```

**Common causes and fixes:**

| Cause | Fix |
|-------|-----|
| User not in the right group | Add to correct group: `gerrit set-members --add user@domain GroupName` |
| Group not granted permission on branch | Add permission for the group on the specific `refs/heads/<branch>` ref |
| Branch pattern too narrow | Change `refs/heads/main` to `refs/heads/*` or `refs/heads/releases/*` |
| Permission inherited from parent project | Check parent project's `project.config`; use `refs/meta/config` to override |
| Anonymous access blocked | Change `read` from `Anonymous Users` to `Registered Users` |
| IP-based Gerrit authorization | Check `gerrit.config` `auth.http` or `auth.git` settings |

**Force-push denial:**
```bash
# Check if force-push is blocked on the branch
ssh -p 29418 admin@host gerrit ls-groups -r project-name refs/heads/main

# If force-push was accidentally granted, revoke it:
# In Gerrit UI: Projects > Access > Edit > Remove "Force Push" from the group
# Or via ssh:
ssh -p 29418 admin@host gerrit set-project-access --project project-name \
  --remove 'refs/heads/main push' GroupName
```

### Cannot Submit / Merge a Change

**Symptom:** Change shows "Could not merge" or user cannot click Submit.

**Diagnosis:**
```bash
# Check what permissions are blocking submit
ssh -p 29418 admin@host gerrit gsql --format JSON -c \
  "SELECT * FROM account_groups WHERE name LIKE '%Owner%'"

# Check label scores required
ssh -p 29418 admin@host gerrit gerrit query --current-patch-set \
  project:myproject topic:myfeature

# Verify user's groups
ssh -p 29418 admin@host gerrit ls-groups --member user@domain
```

**Common causes:**

| Cause | Fix |
|-------|-----|
| Missing `submit` permission | Add `submit` to the user's group on the target branch |
| Required label score not met | Get required reviewers to vote; check `minCodeReviewScore` rule |
| Code owner approval required | Ensure code owner file (`OWNERS`) exists and approvers have voted |
| Submit rule (prolog) blocking | Check `refs/meta/config` submit rules; review `rules.pl` |
| Closed change | Reopen the change or create a new one |
| Same change already merged | Rebase on latest and resubmit |

### Cannot Create Branch

**Symptom:** `remote: ERROR: insufficient permission to create branch`.

**Fix:**
```bash
# Grant create permission
ssh -p 29418 admin@host gerrit set-project-access \
  --project myproject --add 'refs/heads/* create' Developers
```

If the pattern is `refs/heads/release/*`, grant on that specific ref:
```bash
ssh -p 29418 admin@host gerrit set-project-access \
  --project myproject --add 'refs/heads/release/* create' ReleaseManagers
```

### -2 / -1 Votes Blocking Submission

**Fix workflow:**
1. Address review comments — make changes and push a new patch set
2. Request reviewer to change their vote to 0 or +1
3. If vote is from CI bot on stale code, re-trigger CI
4. Project Owners can override in emergencies:
```bash
# Override (bypass code review) — Project Owner only
ssh -p 29418 admin@host gerrit review --project myproject \
  --message "Emergency bypass" --ready-for-submit \
  --submit Change-Id
```

## Group Management Issues

### Group Not Found or Empty

**Symptom:** Permission added but group shows 0 members or does not exist.

**Diagnosis:**
```bash
# List all groups
ssh -p 29418 admin@host gerrit ls-groups

# Check group UUID
ssh -p 29418 admin@host gerrit ls-groups -v group-name

# Verify group UUID in project.config matches UUID from ls-groups
```

**Common causes:**
- Group created in UI but not yet visible — wait ~30 seconds for replication
- UUID mismatch between project.config and actual group
- Group in parent project but not inherited — check `inherit` flag

### Removing User from Group Not Effective

**Cause:** Gerrit caches authentication. Changes take effect on next login.

**Immediate effect:**
```bash
# Force account cache invalidation
ssh -p 29418 admin@host gerrit flush-caches --cache accounts
ssh -p 29418 admin@host gerrit flush-caches --cache groups

# For service accounts, kill the session
ssh -p 29418 admin@host gerrit set-account --remove-account user@domain
```

## Manifest & Multi-Repository Issues

### repo sync Fails with Permission Errors

**Symptom:** `fatal: cannot obtain manifest` or permission denied on manifest repo.

**Fix:**
```bash
# Verify manifest project has read access for all teams
ssh -p 29418 admin@host gerrit ls-access manifest-project

# Ensure manifest repo allows repo tool's anonymous fetch
ssh -p 29418 admin@host gerrit set-project-access \
  --project manifest --add 'refs/* read' 'Registered Users'

# For repo tool specifically, ensure refs/meta/config is readable
ssh -p 29418 admin@host gerrit set-project-access \
  --project manifest --add 'refs/meta/config read' 'Manifest Admins'
```

### Manifest Remote Not Fetching All Projects

**Diagnosis:**
```bash
# Validate manifest XML syntax
repo help manifest

# Check project existence
repo info --all

# Re-verify remote fetch URL
grep -A5 'remote name="origin"' .repo/manifests/default.xml
```

**Fix:** Ensure the manifest repo grants `read` permission to all users before multi-repo operations.

### Manifest Branch Mismatch

**Symptom:** Repos checking out wrong branch or default revision not found.

**Fix:**
```xml
<!-- In manifest XML -->
<default remote="origin" revision="main" />
<!-- Instead of leaving revision empty (defaults to master) -->
```

## Drift & Configuration Issues

### Permissions Drift Across Repositories

**Symptom:** Some repos differ from the baseline template.

**Detection:**
```bash
./scripts/compare-permissions.sh --source repo1 --target repo2

# Check drift from template
./scripts/compare-permissions.sh --check-drift myrepo --template git-flow
```

**Fix:**
```bash
# Re-apply template to affected repos
./scripts/apply-permissions.sh --repo myrepo --template git-flow --force

# Bulk re-apply across manifest
./scripts/bulk-update.sh --manifest default.xml --template git-flow --force
```

### Project Inheritance Not Working

**Cause:** Child project overrides or breaks parent permissions.

**Fix:**
```bash
# Review inheritance chain
ssh -p 29418 admin@host gerrit ls-access child-project --inherited

# Reset child to inherit only
ssh -p 29418 admin@host gerrit set-project-config \
  --project child-project --inherit true
```

## API & Script Failures

### REST API Returns 403 Forbidden

**Fix:**
```bash
# Generate HTTP password for authentication
# Web UI: Settings > HTTP Password > Generate

# Use with curl
curl -s -X GET -u username:http_password \
  "http://localhost:8080/a/projects/myproject/access/"

# For SSH, verify SSH key is registered
ssh -p 29418 admin@host gerrit gsql --format JSON -c \
  "SELECT ssh_public_key FROM account_ssh_keys WHERE account_id = YOUR_ID"
```

### SSH Connection Refused or Timeout

**Fix:**
```bash
# Verify sshd is running
ssh -p 29418 admin@localhost gerrit version

# Check gerrit.config sshd listen address
grep -E "sshd.listenAddress|sshd.bindAddress" $site_path/etc/gerrit.config

# Test connectivity
nc -zv localhost 29418
```

### bulk-update.sh Script Fails on Partial Manifest

**Fix:**
```bash
# Dry run first to identify failing repos
./scripts/bulk-update.sh --manifest default.xml --dry-run --verbose

# Fix failing repos individually
./scripts/apply-permissions.sh --repo failing-repo --template git-flow

# Retry with --continue flag
./scripts/bulk-update.sh --manifest default.xml --continue
```

## Security Audit Failures

### Anonymous Read Access Flagged

**Symptom:** `audit-permissions.sh` reports anonymous access as high risk.

**Fix — for public OSS projects (acceptable risk):**
```bash
# Acknowledge risk with justification
./scripts/audit-permissions.sh --repo myproject --acknowledge \
  --reason "Public open-source project, source code is public anyway"
```

**Fix — for private projects:**
```bash
# Restrict read access
ssh -p 29418 admin@host gerrit set-project-access \
  --project myproject --remove 'refs/* read' 'Anonymous Users' \
  --add 'refs/* read' 'Registered Users'
```

### Overly Permissive Group (forge identity, push)

**Symptom:** Security score drops below threshold.

**Fix:**
```bash
# Revoke forge identity from broad groups
ssh -p 29418 admin@host gerrit set-project-access \
  --project myproject --remove 'refs/* forge identity' 'All Users'

# Grant forge identity only to service accounts
ssh -p 29418 admin@host gerrit set-project-access \
  --project myproject --add 'refs/* forge identity' 'CI Service Accounts'
```

### No Force-Push Protection on Main Branch

**Fix:**
```bash
# Remove force-push from main branch for all groups
ssh -p 29418 admin@host gerrit set-project-access \
  --project myproject --remove 'refs/heads/main force push' 'Registered Users'
ssh -p 29418 admin@host gerrit set-project-access \
  --project myproject --remove 'refs/heads/main force push' 'Anonymous Users'

# Verify
ssh -p 29418 admin@host gerrit ls-access myproject refs/heads/main
```
