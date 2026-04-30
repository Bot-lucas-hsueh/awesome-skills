# DAG Template

Production-ready DAG template with best practices.

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.providers.amazon.aws.operators.s3 import S3CopyObjectOperator
from airflow.operators.empty import EmptyOperator

default_args = {
    'owner': 'data-engineer',
    'depends_on_past': False,
    'email': ['alerts@example.com'],
    'email_on_failure': True,
    'email_on_retry': False,
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'execution_timeout': timedelta(hours=2),
}

@dag(
    dag_id='etl_orders_daily',
    default_args=default_args,
    description='Daily ETL pipeline for orders',
    schedule_interval='0 2 * * *',  # 2 AM daily
    start_date=datetime(2024, 1, 1),
    end_date=None,
    catchup=False,  # Don't backfill on restart
    max_active_runs=1,  # One run at a time
    max_active_tasks=16,  # Limit concurrent tasks
    tags=['etl', 'orders', 'daily'],
    doc_md='''
    ## Daily ETL Pipeline
    Extracts orders from source, transforms, and loads to warehouse.
    
    ### Schedule
    Runs daily at 2 AM UTC.
    
    ### Owner
    Data Engineering team
    ''',
)
def etl_orders_dag():
    
    start = EmptyOperator(task_id='start')
    end = EmptyOperator(task_id='end')
    
    @task
    def extract(logical_date: datetime):
        """Extract orders from source API."""
        date_str = logical_date.strftime('%Y-%m-%d')
        data = api.fetch_orders(date=date_str)
        return data
    
    @task
    def transform(data: list):
        """Transform raw orders."""
        return [
            {
                'id': o['id'],
                'amount': o['total'],
                'date': o['created_at'],
                'processed': True
            }
            for o in data
        ]
    
    @task
    def load(orders: list):
        """Load to warehouse (idempotent upsert)."""
        for order in orders:
            warehouse.upsert('orders', order, key='id')
    
    @task
    def notify_success(count: int):
        """Send success notification."""
        slack.notify(f'ETL completed: {count} orders processed')
    
    # DAG structure
    extracted = extract()
    transformed = transform(extracted)
    loaded = load(transformed)
    notified = notify_success(loaded)
    
    start >> extracted >> transformed >> loaded >> notified >> end

etl_orders_dag()

# Key points:
# - catchup=False prevents backfill on restart
# - max_active_runs=1 prevents overlapping runs
# - Idempotent tasks safe for re-runs
# - Use TaskFlow API for cleaner code
```
