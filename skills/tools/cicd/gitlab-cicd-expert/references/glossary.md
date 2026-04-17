# Glossary

## 9.1 Pipeline Terminology

| Term | Definition |
|------|-------------|
| **Pipeline** | Collection of jobs organized into stages |
| **Job** | Atomic unit of execution (script + config) |
| **Stage** | Group of jobs that run in parallel |
| **Runner** | Agent that executes jobs |
| **Artifact** | Files passed between jobs |
| **Cache** | Stored dependencies for speed |
| **Environment** | Deployment target with variables |

## 9.2 Job Keywords

| Keyword | Description |
|---------|-------------|
| `script` | Commands to run |
| `image` | Docker image for job |
| `stage` | Pipeline stage |
| `tags` | Runner selection |
| `needs` | DAG dependencies |
| `rules` | Conditional execution |
| `only/except` | Branch/tag filters |
| `artifacts` | Output files |
| `cache` | Dependency cache |
| `services` | Sidecar containers |

## 9.3 Triggers

| Trigger | Description |
|---------|-------------|
| `push` | Code pushed to branch |
| `merge_request` | MR opened/updated |
| `schedule` | Cron timing |
| `web` | Manual trigger |
| `api` | API trigger |
| `tag` | Tag created |

## 9.4 Runner Types

| Executor | Use Case |
|----------|----------|
| `docker` | Containerized builds |
| `docker+machine` | Auto-scaling Docker |
| `shell` | Direct execution |
| `ssh` | Remote execution |
| `kubernetes` | K8s pods |
| `virtualbox` | VM-based |

## 9.5 Key Features

- ** DAG (Directed Acyclic Graph)**: Use `needs:` for non-sequential jobs
- **Matrix**: Run jobs with multiple values
- **Include**: Reuse pipeline configurations
- **Child pipelines**: Trigger from parent
- **Auto DevOps**: Automatic build/test/deploy
- **Review Apps**: Temporary deployments for MRs