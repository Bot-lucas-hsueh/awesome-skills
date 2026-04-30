# Troubleshooting Guide

## 8.1 Common Failures

### DAG Not Triggering / Scheduler Issues

| Symptom | Likely Cause | Fix |
|---------|-------------|-----|
| DAG doesn't appear in UI | File not in `dags_folder`, import error | Check `airflow dags list`, `airflow dags report` |
| DAG triggers but tasks never run | Scheduler down, executor full | Check scheduler logs, `airflow scheduler -D` |
| Tasks stuck in "queued" | `pool` exhausted, concurrency limit | Increase `parallelism`, check pool usage |
| `DagFileProcessor` errors | Syntax/import error in DAG | `python -c "import dags.my_dag"` to test |
| Backfill skipping dates | `catchup=False` not set | Set `catchup=False` or use `--disable-regex` |
| Schedule interval off by 1 hour | Timezone mismatch | Set `default_timezone = utc`, use pendulum |

```bash
# Diagnose scheduler issues
airflow dags list
airflow tasks list <dag_id> --tree
airflow dags report -d <dag_id>
airflow jobs check --job-type SchedulerJob
airflow scheduler --stdout

# Check DAG parsing errors
airflow dag-processor --do_pickle
python -c "from airflow import settings; print(settings.DAGS_FOLDER)"
```

### Task Failures

| Error | Cause | Solution |
|-------|-------|----------|
| `OperationalError: connection pool exhausted` | Too many concurrent DB connections | Reduce `parallelism`, use connection pooling |
| `SSL certificate verify failed` | TLS mismatch | Set `AIRFLOW__CORE__SQL_ALCHEMY__SQL_ENGINE_KWARGS` or update certs |
| `Failed to execute task <task>: Received SIGTERM` | Task timeout, OOM kill | Increase `execution_timeout`, check `dagrun_timeout` |
| `Skipping due to task concurrency limit` | `concurrency` / `max_active_tasks` exceeded | Raise limits or split DAG |
| `XCom payload too large` | XCom > 48KB limit | Write to S3, pass URI via XCom |
| `Template not found` | Wrong `template_searchpath` | Set in DAG or `airflow.cfg` |

### Executor / Worker Issues

```bash
# Celery: check worker status
airflow celery inspect active
airflow celery inspect stats
airflow celery inspect registered
airflow celery command supervisorctl status

# Kubernetes: check pod logs
kubectl get pods -n airflow | grep <task-id>
kubectl logs <pod-name> -n airflow

# Check triggerer (for deferrable operators)
airflow triggerer --capacity 1000
```

## 8.2 Performance Tuning

### Scheduler Performance

```ini
# airflow.cfg - tune for large DAG counts
[scheduler]
num_runs = -1                    # Continuous scheduling loop
 scheduler_heartbeat_sec = 5
 min_file_process_interval = 30 # Don't re-parse unchanged DAGs too often
 dag_dir_list_interval = 300    # How often to scan dags_folder
 pool_metrics_interval = 5.0
 scheduler_idle_sleep_time = 1
 max_tis_per_query = 512         # Increase for more throughput
```

### DAG Performance Checklist

```python
# 1. Use TaskFlow API for smaller tasks (less serialization overhead)
@task(task_id='process')
def process(data):
    return transform(data)

# 2. Limit XCom usage — use for metadata only
#    For large data: write to S3/GCS, pass URI

# 3. Pool management — don't use default_pool for heavy tasks
small_task = PythonOperator(task_id='small', python_callable=quick, pool='light_pool')
heavy_task = PythonOperator(task_id='heavy', python_callable=heavy, pool='heavy_pool', pool_slots=4)

# 4. Lazy-load connections/hooks
class MyOperator(BaseOperator):
    def execute(self, context):
        hook = HttpHook(http_conn_id='api')  # Init here, not in __init__
        hook.run()

# 5. Use `trigger_rule` to allow partial failures
notify = PythonOperator(task_id='notify', python_callable=notify_slack, trigger_rule='all_done')

# 6. Avoid cross-DAG dependencies — use ExternalTaskSensor with care
#    Prefer event-driven: Airflow Assets (2.8+) or Task DAG
```

### Task Concurrency

```
# dag_concurrency = 16  (tasks per DAG run)
# max_active_tasks = 16 (concurrent tasks per DAG across runs)
# parallelism = 64       (total concurrent tasks across all DAGs)

# For 100+ DAGs, increase parallelism:
parallelism = 256
```

## 8.3 Debugging Techniques

### Enable Extra Logging

```python
import logging
from airflow.utils.log.logging_mixin import set_context

def my_task(**context):
    logging.getLogger("airflow.task").setLevel(logging.DEBUG)
    logging.info(f"Processing date: {context['ds']}")
    # Also set log_level = DEBUG in airflow.cfg
```

### Task Instance Debugging

```bash
# Clear failed task and retry
airflow tasks clear <dag_id> --task-id <task_id> --run-id <run_id> --upstream
airflow tasks retry <dag_id> --run-id <run_id> --task-id <task_id>

# Test operator in isolation
airflow tasks test <dag_id> <task_id> <execution_date>

# Run DAG locally
airflow dags backfill <dag_id> -s 2024-01-01 -e 2024-01-03 --dry-run
```

### Memory / Resource Issues

```bash
# Web server OOM: limit workers
workers = 2
worker_class = sync  # or gevent / eventlet for async workloads

# Scheduler OOM: increase heap
export AIRFLOW__SCHEDULER__MAX_TIS_PER_QUERY=256

# Task OOM: use KubernetesPodOperator with resource limits
KubernetesPodOperator(
    task_id='heavy_task',
    name='heavy-task',
    namespace='airflow',
    image='my-image:latest',
    resources= k8s.V1ResourceRequirements(
        requests={'memory': '2Gi', 'cpu': '1'},
        limits={'memory': '4Gi', 'cpu': '2'},
    ),
)
```

## 8.4 Known Issues & Fixes

| Issue | Version | Workaround |
|-------|---------|------------|
| `Serialized DAG not found` after upgrade | 2.6-2.7 | Clear DAG in UI, restart scheduler |
| Scheduler using 100% CPU with many DAGs | 2.6 | Upgrade to 2.7+, increase `min_file_process_interval` |
| Task sensor timeout but task actually succeeded | 2.5-2.6 | Use `reschedule_mode=False` in Smart Sensor |
| Connection password with special chars | All | URL-encode or use Variables |
| SubDAG anti-pattern causing deadlocks | Pre-2.3 | Replace SubDAGs with TaskGroup |
| Timezone-aware DAG scheduling off by DST | All | Use `pendulum` timezone, avoid `local_tz` |
