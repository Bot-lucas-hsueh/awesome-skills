# Glossary

## Core Concepts

| Term | Definition |
|------|------------|
| **DAG** | Directed Acyclic Graph - workflow definition |
| **Task** | Single unit of work |
| **Operator** | Template for task execution |
| **Sensor** | Task that waits for condition |
| **XCom** | Cross-task communication |

## Operators

| Term | Definition |
|------|------------|
| **BashOperator** | Execute shell command |
| **PythonOperator** | Execute Python function |
| **BigQueryOperator** | Run BigQuery queries |
| **KubernetesPodOperator** | Run pod in K8s |
| **VirtualOperator** | Placeholder/skip task |

## Execution

| Term | Definition |
|------|------------|
| **DagRun** | Instance of DAG execution |
| **TaskInstance** | Instance of task execution |
| **Execution Date** | Logical timestamp for run |
| **Logical Date** | Same as execution date |

## Scheduling

| Term | Definition |
|------|------------|
| **Cron** | Schedule expression |
| **Timetable** | Custom schedule logic |
| **Catchup** | Backfill missed runs |
| **Backfill** | Historical runs |

## Monitoring

| Term | Definition |
|------|------------|
| **Airflow UI** | Web interface |
| **Metadb** | Metadata database |
| **Flower** | Celery monitoring |
| **StatsD** | Metrics collection |

## Executors

| Term | Definition |
|------|------------|
| **LocalExecutor** | Single machine parallel |
| **CeleryExecutor** | Distributed workers |
| **KubernetesExecutor** | K8s pod per task |
| **SequentialExecutor** | One task at a time |