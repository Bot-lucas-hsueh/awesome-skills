# Daily ETL DAG with Idempotency

TaskFlow API with idempotent load (upsert) pattern.

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task
from airflow.providers.postgres.operators.postgres import PostgresOperator

default_args = {
    'owner': 'data-engineer',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
}

@dag(default_args=default_args, schedule_interval='0 2 * * *',
     start_date=datetime(2024, 1, 1), catchup=False)
def daily_etl():

    @task
    def extract(logical_date: datetime):
        date_str = logical_date.strftime('%Y-%m-%d')
        data = api.fetch_orders(date=date_str)
        return data  # TaskFlow auto-XComs this

    @task
    def transform(data: list):
        return [{'id': o['id'], 'amount': o['total'],
                 'date': o['created_at'], 'processed': True}
                for o in data]

    @task
    def load(orders: list):
        # Idempotent: INSERT ON CONFLICT UPDATE
        for order in orders:
            warehouse.upsert('orders', order, key='id')

    load(transform(extract()))

# Key decisions:
# - catchup=False prevents backfilling on restart
# - upsert makes load idempotent (safe to re-run)
# - XCom data kept minimal (list of dicts, not raw API response)
```
