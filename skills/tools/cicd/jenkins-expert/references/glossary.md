# Glossary

## 9.1 Pipeline Terminology

| Term | Definition |
|------|-------------|
| **Pipeline** | CD process as code in Jenkinsfile |
| **Jenkinsfile** | Version-controlled pipeline definition |
| **Stage** | Logical grouping of steps |
| **Step** | Single task/action |
| **Node** | Machine that executes pipeline |
| **Agent** | Distributed execution environment |
| **Executor** | Slot for running builds |
| **Workspace** | Filesystem location for build |
| **Artifact** | Files preserved from build |

## 9.2 Pipeline Types

| Type | Description |
|------|-------------|
| **Declarative** | Newer, structured, enforced syntax |
| **Scripted** | Older, Groovy-based, flexible |
| **Freestyle** | UI-based configuration |
| **Matrix** | Multi-configuration project |

## 9.3 Key Concepts

| Concept | Description |
|---------|-------------|
| **Agent** | Where to run (any, label, docker) |
| **Environment** | Key-value variables |
| **Options** | Pipeline-level settings |
| **Parameters** | User-provided inputs |
| **Triggers** | What starts the build |
| **Post** | Post-build actions |
| **when** | Conditional stage execution |

## 9.4 Common Steps

| Step | Description |
|------|-------------|
| `sh` | Execute shell command |
| `bat` | Execute Windows batch |
| `echo` | Print message |
| `dir` | Change directory |
| `withCredentials` | Access secured credentials |
| `withEnv` | Set environment variables |
| `archiveArtifacts` | Save build output |
| `junit` | Publish test results |

## 9.5 Agent Types

| Type | Description |
|------|-------------|
| **Built-in Node** | Master controller |
| **Permanent Agent** | Dedicated machine |
| **Cloud Agent** | Dynamic (Kubernetes, Docker) |
| **SSH Agent** | Remote via SSH |
| **Docker Agent** | Container-based |

## 9.6 Plugins

- **Pipeline**: Core pipeline support
- **Blue Ocean**: Modern UI
- **Git**: Source control
- **Maven Integration**: Maven builds
- **Docker Pipeline**: Docker builds
- **Kubernetes**: K8s orchestration
- **Credentials Binding**: Secure variables