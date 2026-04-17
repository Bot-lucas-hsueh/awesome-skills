# Glossary

## 9.1 Pipeline Terminology

| Term | Definition |
|------|-------------|
| **Workflow** | Automated process defined in `.yml` file in `.github/workflows/` |
| **Job** | Set of steps that run on the same runner |
| **Step** | Individual task (run command or action) within a job |
| **Action** | Reusable unit of automation |
| **Runner** | Server that executes jobs (GitHub-hosted or self-hosted) |
| **Artifact** | Files created by a workflow (via `actions/upload-artifact`) |
| **Cache** | Saved dependencies to speed up future runs |

## 9.2 Trigger Types

| Trigger | Description |
|---------|-------------|
| `push` | Code pushed to branch/tag |
| `pull_request` | PR opened, updated, or merged |
| `schedule` | Cron-based timing |
| `workflow_dispatch` | Manual trigger via UI/API |
| `repository_dispatch` | External trigger via API |
| `release` | Published release |
| `workflow_call` | Called from another workflow |

## 9.3 Context Objects

| Context | Description |
|---------|-------------|
| `github` | Workflow run info (event, sha, ref, repo) |
| `env` | Environment variables set in workflow |
| `steps` | Outputs from previous steps |
| `matrix` | Matrix strategy values |
| `needs` | Outputs from dependent jobs |
| `inputs` | Inputs from workflow_dispatch |
| `secrets` | Available secrets |

## 9.4 Runner Types

| Runner | Description |
|--------|-------------|
| `ubuntu-latest` | Ubuntu 22.04 |
| `windows-latest` | Windows Server 2022 |
| `macos-latest` | macOS 13 |
| `self-hosted` | Custom runner infrastructure |

## 9.5 Action Types

| Type | Description |
|------|-------------|
| **JavaScript** | Runs Node.js, faster startup |
| **Docker** | Container-based, isolation |
| **Composite** | Combines multiple steps |

## 9.6 Key Concepts

- **Dependabot**: Auto-update dependencies and actions
- **Concurrency**: Control parallel runs
- **Required checks**: Branch protection rules
- **Environment**: Deployment targets with protection rules
- **Artifact retention**: Default 90 days