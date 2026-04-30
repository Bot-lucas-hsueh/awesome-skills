# Dynamic DAG with Multiple Destinations

Dynamic Task Mapping for syncing multiple tables.

```python
from airflow.decorators import dag, task
from airflow.providers.google.cloud.transfers.mysql_to_gcs import MySQLToGCSOperator
from airflow.providers.google.cloud.transfers.gcs_to_bigquery import GCSToBigQueryOperator

@dag(schedule_interval='@daily', start_date=datetime(2024, 1, 1))
def sync_mysql_to_bigquery():

    @task
    def get_table_list():
        return [
            {'table': 'orders', 'partition': 'order_date'},
            {'table': 'customers', 'partition': 'created_at'},
            {'table': 'products', 'partition': None},
        ]

    @task
    def extract_to_gcs(table_config: dict):
        return MySQLToGCSOperator(
            task_id=f"extract_{table_config['table']}",
            mysql_conn_id='mysql-prod',
            sql=f"SELECT * FROM {table_config['table']}",
            bucket='my-bucket',
            filename=f"raw/{table_config['table']}/{{{{ ds }}}}/{table_config['table']}.json",
            export_format='json',
        ).execute(context={})

    tables = get_table_list()
    extract_to_gcs.expand(table_config=tables)

# Alternative: Use a single DAG with for loop over table_list
# and dynamic task mapping for each table.

# Key points:
# - Dynamic Task Mapping creates tasks at runtime
# - expand() fans out tasks based on input data
# - Each mapped task gets unique task_id
```
