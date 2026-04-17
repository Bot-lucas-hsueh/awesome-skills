# Gerrit Permission Management — Glossary

## Core Gerrit Concepts

### Access Control

**Access Right / Permission** — A capability granted to a group on a specific ref pattern (e.g., `submit`, `push`, `read`). Examples: `refs/heads/main read`, `refs/for/refs/heads/main push`.

**Category** — The type of access right. Categories include `read`, `write`, `push`, `create`, `delete`, `forge identity`, `submit`, `label-*`, `upload`, `pushSignedTag`, `pushTag`.

**Submit** — The permission required to merge a change into a branch. Distinct from code review labels.

**Push** — Permission to push commits directly to a branch without a code review (not recommended for protected branches).

**Force Push** — Permission to overwrite branch history with `git push --force`. Should be restricted or disabled on main/release branches.

**Read** — Permission to fetch and view a branch or project. Controls visibility.

**Create** — Permission to create new branches matching a pattern.

**Delete** — Permission to delete branches matching a pattern.

**forge identity** — Permission to claim another user's identity in commit authorship. Should be restricted to CI service accounts only.

**label-* / Label Permission** — Permission to vote with a specific label (e.g., `label-Code-Review`, `label-Verified`, `label-Security-Review`).

**Submit Rule** — A Prolog predicate that determines when a change is eligible for submission based on conditions (e.g., minimum code review score).

**Submit Filter** — A Prolog predicate that can modify or approve a submit operation based on dynamic conditions.

### Refs (References)

**refs/heads/\<branch\>** — The namespace for branch heads (e.g., `refs/heads/main`, `refs/heads/develop`).

**refs/for/\<branch\>** — The magic ref namespace for pushing changes for review. `git push origin HEAD:refs/for/main` creates a new change on the main branch.

**refs/meta/config** — The branch containing the project's access rules and submit rules in `project.config` format. Modifying this ref changes project permissions.

**refs/meta/audit** — Used for audit log tracking of permission changes.

**refs/tags/** — The namespace for tags. Permissions here control who can create/push tags.

**refs/heads/releases/\*** — Branch pattern for release branches.

**refs/heads/feature/\*** — Branch pattern for feature branches.

**refs/heads/hotfix/\*** — Branch pattern for hotfix branches.

### Code Review

**Change** — A unit of review in Gerrit. Created by pushing to `refs/for/<branch>`. Also called a "patch set" stack.

**Patch Set** — A new version of a change. Created by amending or rebasing and pushing again.

**Code-Review Label** — The default label (`-2..+2`) for code quality review. `-2` blocks submission, `+2` indicates approval.

**Verified Label** — Default label (`-1..+1`) for CI/build system verification. `-1` blocks submission when enforced.

**+2 / -2 Vote** — A strong approval or strong rejection. Only users with `label-Code-Review -2..+2` permission can give these votes.

**+1 / -1 Vote** — A weak approval or suggestion. Registered users typically have this.

**Abandon** — Marking a change as no longer intended to be merged.

**Restore** — Reactivating an abandoned change.

**Draft** — A change not visible to reviewers until explicitly published.

### Groups

**Account Group** — A named collection of users. Groups are the primary vehicle for granting permissions.

**UUID (Group UUID)** — The globally unique identifier for a group. Used in `project.config` instead of group names to avoid ambiguity.

**Owner Group** — The group that can modify a project's access rules. The project owner group.

**Internal Groups** — Groups managed within Gerrit (e.g., `Registered Users`, `Project Owners`).

**External Groups** — Groups managed in an external system (LDAP, OAuth) and synchronized to Gerrit.

**Registered Users** — Built-in group containing every user with a Gerrit account. Useful as a catch-all for broad permissions.

**Anonymous Users** — Built-in group for unauthenticated access. Used for public read-only projects.

**All-Projects** — The parent project whose access rules are inherited by all other projects.

### Projects

**Project** — A Git repository managed by Gerrit. The top-level container for code and access rules.

**Project Config** — The file (`project.config`) in `refs/meta/config` that stores access rules for a project.

**Inheritance** — Child projects can inherit access rules from their parent project via the `inherit` setting.

**All-Projects** — The root project in Gerrit. Access rules set here apply to every project unless overridden.

**Child Project** — A project that inherits from a parent project.

**Parent Project** — A project from which a child project inherits access rules.

### Manifests (repo tool)

**Manifest Repository** — A Git repository containing `default.xml` that defines which projects to check out and their branches.

**default.xml** — The manifest file in repo format specifying project paths, remotes, and revision assignments.

**Remote** — In a manifest, the fetch URL for a group of projects.

**Project Element** — An entry in `default.xml` mapping a repository name to a checkout path and optional revision.

### SSH & REST API

**Gerrit SSH** — Gerrit's command-line interface over SSH on port 29418. Commands like `gerrit set-members`, `gerrit ls-groups`.

**Gerrit REST API** — HTTP API for programmatic access to Gerrit (projects, changes, accounts, groups).

**HTTP Password** — A generated password for authenticating with the Gerrit REST API over HTTPS.

**SSH Key** — A public key registered to a Gerrit account for SSH authentication.

**Review SSH Command** — `gerrit review` — command to vote on a change, approve, or add comments.

**Stream Events** — `gerrit stream-events` — real-time event stream for hooks and integrations.

### Security & Compliance

**Force Push** — A push that overwrites the remote branch history. Dangerous on main branches; should be restricted.

**Non-Forkable Workflow** — A setup where direct pushes are blocked; all changes must go through review. Provides an auditable change trail.

**Code Owner** — A file (`OWNERS`) designating who can approve changes to specific paths. Enforced via submit rules.

**Drift Detection** — Comparing actual repository permissions against a defined baseline template to identify unauthorized changes.

**Security Audit** — Automated checks for common security misconfigurations (anonymous read, force push, overly broad groups).

**Security Score** — A 0-100 rating of a project's permission configuration based on security audit findings.

**Separation of Duties** — Principle ensuring no single role has all permissions (e.g., developers cannot approve their own changes).

**SLSA Compliance** — Supply-chain security framework. Gerrit's non-forkable review model supports SLSA Level 2-3.

### Workflows

**Git Flow** — A branching model with `main` (production), `develop` (integration), `feature/*`, `release/*`, and `hotfix/*` branches.

**Fork Workflow** — A model where contributors work in personal forks and submit changes via pull requests.

**Non-Fork / Direct-Write Workflow** — A model where all developers push to shared branches with review requirements. Gerrit's native mode.

**Branch Protection** — A configuration that blocks direct pushes to certain branches, requiring all changes to go through code review.

**Minimum Reviewer Count** — A submit rule requirement for a specific number of approvals before a change can be submitted.

**Expedited Review** — An accelerated approval process for hotfixes, typically requiring fewer reviews.

### Configuration Files

**project.config** — The configuration file in `refs/meta/config` storing access rules, label definitions, and project settings.

**groups** — A file in `refs/meta/config` listing which groups own specific access blocks.

**rules.pl** — A Prolog file in `refs/meta/config` defining submit rules.

**gerrit.config** — The server configuration file controlling Gerrit's global settings.

**etc/secure.config** — Sensitive server settings (database passwords, LDAP bind credentials).

**gerrit_site/** — The root directory of a Gerrit installation.

### Common Permission Patterns

**Standard OSS** — Public read, restricted submit. Suitable for open-source projects.

**Restricted** — Registered users only, tight submit controls. For internal or sensitive projects.

**Protected Branches** — Multiple reviewer requirements, code owner approval. For production branches.

**Multi-Team** — Team-specific branches with cross-team read. For large organizations.

**Git Flow** — Branch-role matrix matching the Git Flow branching strategy.

**CI-Optimized** — CI bot verification required, service accounts with minimal permissions.

### Related Tools

**repo tool** — Google's multi-repository management tool. Uses manifest XML files to synchronize many Git repositories.

**repo sync** — Command to synchronize all repositories defined in a manifest.

**repo start** — Create and start a new branch across all or selected projects.

**repo forall** — Run a shell command across all repositories in a manifest.

**Jenkins Gerrit Trigger** — Plugin that triggers builds on code review events.

**Zuul** — OpenStack's CI/CD gating system that integrates with Gerrit.
