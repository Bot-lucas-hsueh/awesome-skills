# Glossary

## Core Airflow Concepts

### DAG (Directed Acyclic Graph)
A collection of tasks with defined dependencies, representing a workflow. Airflow schedules and executes tasks following the DAG structure. DAGs must be acyclic — no loops allowed.

### Task
A unit of work in a DAG. Types include: `PythonOperator`, `BashOperator`, `Sensor`, `SubDagOperator`, `KubernetesPodOperator`. Tasks define the actual work via a `python_callable` or `bash_command`.

### Operator
A template for a Task. Defines what gets done. Categories:
- **Action Operators**: perform an action (PythonOperator, BashOperator)
- **Transfer Operators**: move data between systems (S3ToRedshiftOperator)
- **Sensor Operators**: wait for a condition (FileSensor, HttpSensor)

### TaskInstance
A specific run of a task within a DAG run, with state (queued, running, success, failed, skipped).

### DAG Run
An execution instance of a DAG at a specific `execution_date`. A DAG can have multiple concurrent runs unless `max_active_runs` limits it.

### Execution Date
The logical date/time a DAG run represents. Not necessarily the wall-clock time of execution. Follows the `schedule_interval`.

### Schedule Interval
Defines how often a DAG runs. Accepts cron expressions (`0 3 * * *`), timedelta objects, or custom `Timetable` objects. Use `@daily`, `@hourly`, or `None` for manual-only.

### XCom (Cross-Communication)
Mechanism for tasks to share data. XComs are stored in the metadata database and have a 48KB size limit. For large data, write to external storage (S3) and pass the URI.

### Trigger Rule
Defines when a task should run based on upstream task states. Options: `all_success` (default), `all_failed`, `all_done`, `one_success`, `one_failed`, `none_failed`, `none_skipped`, `always`.

### Pool
A named collection of slots that limits concurrent task execution. Use pools to prevent resource exhaustion. Each task can consume 1 or more slots.

### SLA (Service Level Agreement)
A deadline for task/DAG completion. If missed, Airflow sends an email alert. Defined via `sla` parameter on DAG.

### Variable
Airflow's key-value store for DAG configuration and secrets. Accessible via `Airflow Variables` UI and `airflow.models.Variable` API.

### Connection
A saved credential/configuration for an external system. Stored in metadata DB, accessed via `BaseHook.get_connection()`.

### Sensor
A special operator that runs until a condition is met (file exists, API returns success, external DAG completes). Use `mode='reschedule'` to free worker slots while waiting.

### TaskGroup
A way to visually group tasks in the Airflow UI without affecting execution logic. Preferred over deprecated SubDAG pattern.

### Deferrable Operator
An operator that can suspend itself and free the worker slot when waiting for an external event. Uses the Triggerer service instead of a persistent Celery worker slot. Examples: `TimeSensorAsync`, `HttpSensorAsync`.

### Asset (Airflow 2.8+)
A named reference to data (file, database table, etc.) that DAGs can listen to for triggering. Enables event-driven scheduling independent of time-based intervals.

### Catchup
When `catchup=True`, the scheduler creates DAG runs for all missed intervals since `start_date`. For production, `catchup=False` is almost always correct.

### Backfill
Running historical DAG runs for past dates. Use `airflow dags backfill` CLI command. Be careful with resource-intensive DAGs.

### Serialized DAG
Airflow serializes DAG definitions to JSON and stores them in the database. This allows the Web server and workers to load DAGs without parsing Python files. Use `airflow dags reserialize` after changes.

### TaskFlow API
A decorator-based API (`@task`) introduced in Airflow 2.0 that simplifies task authoring, automatic XCom handling, and type hinting. Preferred over traditional operator approach.

## Executors

| Term | Definition |
|------|------------|
| **SequentialExecutor** | Default, single-threaded. Runs one task at a time. For dev only. |
| **LocalExecutor** | Parallel task execution on a single machine using multiprocessing. |
| **CeleryExecutor** | Distributed executor using Celery as the task queue, Redis as broker. |
| **KubernetesExecutor** | Creates a new Kubernetes pod per task instance. Maximum isolation. |
| **CeleryKubernetesExecutor** | Hybrid — Celery for queuing, Kubernetes for execution. |
| **DebugExecutor** | Used with `airflow debug task` for interactive debugging. |

## CLI Commands Reference

| Command | Purpose |
|---------|---------|
| `airflow dags list` | List all DAGs |
| `airflow tasks list <dag>` --tree | Show task hierarchy |
| `airflow tasks test <dag> <task> <date>` | Test single task |
| `airflow dags backfill <dag>` -s -e | Run historical DAG runs |
| `airflow dags reserialize` | Refresh serialized DAGs |
| `airflow connections add <id>` --conn-* | Create a connection |
| `airflow variables set <key> <value>` | Set a variable |
| `airflow scheduler -D` | Restart scheduler daemon |
| `airflow sync-perm` | Sync Airflow permissions (FAB) |
