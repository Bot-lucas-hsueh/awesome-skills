# Standards & Reference

## 7.1 Official Documentation

- [Apache Airflow Documentation](https://airflow.apache.org/docs/apache-airflow/stable/)
- [Airflow Core Concepts](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/index.html)
- [Operators Reference](https://airflow.apache.org/docs/apache-airflow/stable/_api/airflow/operators/index.html)
- [Airflow REST API](https://airflow.apache.org/docs/apache-airflow/stable/stable-rest-api-ref.html)
- [Airflow UI / DAG Views](https://airflow.apache.org/docs/apache-airflow/stable/ui.html)
- [Kubernetes Executor](https://airflow.apache.org/docs/apache-airflow/stable/kubernetes.html)
- [Celery Executor](https://airflow.apache.org/docs/apache-airflow/stable/celery.html)
- [Amazon MWAA](https://docs.aws.amazon.com/mwaa/latest/userguide/what-is-mwaa.html)
- [Astro (Astronomer) Runtime](https://docs.astronomer.io/astro/runtime-release-notes)
- [Airflow Plugins](https://airflow.apache.org/docs/apache-airflow/stable/plugins.html)
- [Timetables (Custom Scheduling)](https://airflow.apache.org/docs/apache-airflow/stable/authoring-and-scheduling/timetable.html)
- [XCom Deep Dive](https://airflow.apache.org/docs/apache-airflow/stable/core-concepts/xcom.html)

## 7.2 Architecture Patterns

### Executors

| Executor | Use Case | Pros | Cons |
|----------|----------|------|------|
| **SequentialExecutor** | Local dev / minimal | Zero setup | No parallelism |
| **LocalExecutor** | Single-node prod | Parallel tasks, simple | No horizontal scale |
| **CeleryExecutor** | Multi-node prod | Horizontal scale, queue-based | Needs Redis/Celery |
| **KubernetesExecutor** | Cloud-native / containerized | Per-task pods, isolation | Complexity |
| **CeleryKubernetesExecutor** | Hybrid | Best of both worlds | Very complex |

### DAG Architecture Patterns

```
Pattern 1: Linear ETL
  extract → validate → transform → load → notify

Pattern 2: Branching / Conditional
  start → [check_type] → A_path (type=api) / B_path (type=db)
                        ↓                    ↓
                     done                 done

Pattern 3: SubDAG / TaskGroup (parallel work)
  parent_dag:
    task_group_1[load_dim_customers, load_dim_products, load_dim_orders]
    aggregation → reporting

Pattern 4: Sensor → Action
  wait_for_file (FileSensor) → process_file → cleanup

Pattern 5: Dynamic Task Mapping
  process_order(subtask_id="{{ task_instance.task_id }}")
  # or
  process_region(region="{{ params.region }}")
```

## 7.3 DAG Authoring Standards

### Minimal Production DAG

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.models import Variable
from airflow.utils.task_group import TaskGroup

default_args = {
    'owner': 'data-platform',
    'depends_on_past': False,
    'wait_for_downstream': False,
    'email': ['data-alerts@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(minutes=30),
    'pool': 'default_pool',
}

with DAG(
    dag_id='etl_orders_daily',
    default_args=default_args,
    description='Daily order ETL pipeline',
    schedule_interval='0 3 * * *',       # 3 AM UTC daily
    start_date=datetime(2024, 1, 1),
    end_date=None,
    catchup=False,                          # Never catch up on backfills by default
    max_active_runs=1,                      # One run at a time
    max_active_tasks=16,
    dagrun_timeout=timedelta(hours=2),
    tags=['etl', 'orders', 'daily'],
    params={
        'env': 'prod',
        'batch_size': 10000,
    },
) as dag:

    extract = PythonOperator(
        task_id='extract_orders',
        python_callable=extract_orders,
        op_kwargs={
            'batch_size': '{{ params.batch_size }}',
        },
        retries=1,
    )

    validate = BashOperator(
        task_id='validate_data_quality',
        bash_command='python scripts/validate.py {{ ti.task_id }}',
        env={'AIRFLOW_CTX_DAG_ID': '{{ dag.dag_id }}'},
    )

    transform = PythonOperator(
        task_id='transform_orders',
        python_callable=transform_orders,
    )

    load = PythonOperator(
        task_id='load_to_warehouse',
        python_callable=load_to_warehouse,
    )

    notify = PythonOperator(
        task_id='notify_completion',
        python_callable=send_slack_notification,
        trigger_rule='all_done',  # Always run, even on failure
    )

    extract >> validate >> transform >> load >> notify
```

### Sensor Pattern

```python
from airflow.sensors.filesystem import FileSensor
from airflow.sensors.external_task import ExternalTaskSensor
from airflow.sensors.sql import SqlSensor
from airflow.sensors.base import BaseSensorOperator

# File arrival
wait_for_orders = FileSensor(
    task_id='wait_for_orders_file',
    filepath='/data/incoming/orders_{{ ds_nodash }}.csv',
    poke_interval=300,      # Check every 5 min
    timeout=3600 * 6,       # Timeout after 6 hours
    mode='poke',            # 'poke' or 'reschedule'
)

# Wait for upstream DAG
wait_for_dag = ExternalTaskSensor(
    task_id='wait_for_extract_dag',
    external_dag_id='extract_pipeline',
    external_task_id=None,  # Wait for entire DAG
    execution_delta=timedelta(hours=1),
    poke_interval=300,
    timeout=3600 * 2,
    mode='poke',
)

# Custom sensor
class NewRecordSensor(BaseSensorOperator):
    def poke(self, context):
        session = settings.Session()
        last_run = session.query(Log).filter(
            Log.dag_id == self.dag_id,
            Log.task_id == self.task_id,
            Log.state == 'success'
        ).order_by(Log.execution_date.desc()).first()
        return last_run is not None
```

### XCom Patterns

```python
# Push via return value
def extract(**context):
    data = api.fetch('/orders', date=context['ds'])
    return data  # Automatically pushed to XCom

def load(**context):
    data = context['ti'].xcom_pull(task_ids='extract')
    warehouse.bulk_insert('orders', data)

# Push/pull explicitly
context['ti'].xcom_push(key='order_count', value=count)
count = context['ti'].xcom_pull(task_ids='extract', key='order_count')

# Large payloads: use object storage instead of XCom
def extract(**context):
    data = api.fetch_large_dataset()
    # Write to S3, pass URI via XCom
    s3_uri = write_to_s3(data, prefix='staging/orders')
    context['ti'].xcom_push(key='s3_uri', value=s3_uri)
```

## 7.4 Configuration Reference

### airflow.cfg (Production Defaults)

```ini
[core]
dags_folder = /usr/local/airflow/dags
base_log_folder = /usr/local/airflow/logs
executor = CeleryExecutor
parallelism = 64
dag_concurrency = 16
max_active_runs_per_dag = 3
load_examples = False
default_timezone = utc
default_pool_slots = 128

[database]
sql_alchemy_conn = postgresql+psycopg2://airflow:password@postgres:5432/airflow
sql_engine_kwargs = {"pool_pre_ping": true, "pool_recycle": 3600}

[webserver]
web_server_host = 0.0.0.0
web_server_port = 8080
base_url = http://airflow.example.com
web_server_worker_timeout = 120
workers = 4
worker_refresh_batch_size = 1
worker_refresh_interval = 6000

[celery]
celery_app_name = airflow.executors.celery_executor
broker_url = redis://redis:6379/0
result_backend = db+postgresql://airflow:password@postgres:5432/airflow
celery_concurrency = 16
task_adoption_editor_timeout = 300
task_revoke_editor_timeout = 600

[celery_broker_transport_options]
master_name = mymaster

[scheduler]
job_heartbeat_sec = 5
scheduler_heartbeat_sec = 5
num_runs = -1
scheduler_idle_sleep_time = 1
min_file_process_interval = 30
dag_dir_list_interval = 300
print_stats_interval = 30
pool_metrics_interval = 5.0
scheduler_health_check_threshold = 30

[logging]
base_log_folder = /usr/local/airflow/logs
remote_logging = True
remote_log_conn_id = s3_conn
remote_base_log_folder = s3://airflow-logs/
logging_level = INFO
fab_logging_level = WARN
worker_log_server_port = 8793

[api]
auth_backends = airflow.api.auth.backend.basic_auth

[metrics]
statsd_on = True
statsd_host = statsd
statsd_port = 8125
statsd_prefix = airflow
```

## 7.5 Connection Management

```python
# Via Airflow UI / CLI
airflow connections add 'postgres_warehouse' \
    --conn-type 'postgresql' \
    --conn-host 'warehouse.example.com' \
    --conn-port 5432 \
    --conn-schema 'analytics' \
    --conn-login 'airflow_ro' \
    --conn-password 'secret'

# Via Variables for secrets
airflow variables set snowflake_account 'xy12345.us-east-1'

# In DAG
from airflow.hooks.base import BaseHook

def my_task():
    conn = BaseHook.get_connection('postgres_warehouse')
    engine = create_engine(f"postgresql://{conn.login}:{conn.password}@{conn.host}/{conn.schema}")
```

## 7.6 Version Compatibility

| Version | Status | Python | Key Features |
|---------|--------|--------|--------------|
| 2.0.x | EOL | 3.6+ | TaskFlow API, Dr. Elephant deprecation |
| 2.2.x | EOL | 3.7+ | Deferrable operators, custom timetables |
| 2.3.x | EOL | 3.7+ | DAG processor, improved asset events |
| 2.4.x | EOL | 3.7+ | Task group improvements, conditional DAGs |
| 2.5.x | EOL | 3.7+ | Smart sensors (EOL), DAG triggers |
| 2.6.x | EOL | 3.8+ | Triggerer, deferrable sensors, backfill fixes |
| 2.7.x | Security | 3.8+ | Task log grouping, SLA improvements |
| 2.8.x | Stable | 3.8+ | Assets (DAG triggers), deferrable sensors stable |
| 2.9.x | Stable | 3.8+ | Event-based scheduling, custom operators |
| 2.10.x | Latest | 3.8+ | Per-operator resources, dataset URI refs |
