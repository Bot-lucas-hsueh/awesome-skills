# Example DAGs

## 10.1 Data Pipeline Examples

### Multi-Branch ETL with Quality Gates

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator, BranchPythonOperator
from airflow.operators.empty import EmptyOperator
from airflow.operators.postgres_operator import PostgresOperator
from airflow.sensors.external_task import ExternalTaskSensor

default_args = {
    'owner': 'data-engineer',
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    'order_etl_pipeline',
    default_args=default_args,
    schedule_interval='0 4 * * *',
    start_date=datetime(2024, 1, 1),
    catchup=False,
) as dag:

    start = EmptyOperator(task_id='start')

    wait_extract = ExternalTaskSensor(
        task_id='wait_for_extract',
        external_dag_id='source_extract_pipeline',
        external_task_id=None,
        execution_delta=timedelta(hours=1),
        poke_interval=600,
        timeout=3600 * 4,
    )

    def check_data_quality(**context):
        record_count = context['ti'].xcom_pull(
            task_ids='load_staging', key='record_count'
        )
        if record_count and record_count > 1000:
            return 'process_orders'
        else:
            return 'alert_and_skip'

    quality_check = BranchPythonOperator(
        task_id='quality_check',
        python_callable=check_data_quality,
    )

    process_orders = PythonOperator(
        task_id='process_orders',
        python_callable=process_orders_logic,
    )

    load_warehouse = PythonOperator(
        task_id='load_warehouse',
        python_callable=load_to_warehouse,
    )

    aggregate = PostgresOperator(
        task_id='aggregate_metrics',
        postgres_conn_id='warehouse',
        sql='''
            INSERT INTO daily_metrics (date, order_count, revenue)
            SELECT 
                DATE '{{ ds }}' as date,
                COUNT(*) as order_count,
                SUM(total_amount) as revenue
            FROM staging_orders
            WHERE DATE(created_at) = '{{ ds }}';
        ''',
    )

    alert = PythonOperator(
        task_id='send_alert',
        python_callable=send_slack,
        op_kwargs={'message': 'DAG quality check failed: low record count'},
        trigger_rule='none_upstream_skipped',
    )

    skip = EmptyOperator(task_id='skip_processing', trigger_rule='none_upstream_skipped')

    end = EmptyOperator(
        task_id='end',
        trigger_rule='none_failed_or_skipped',
    )

    start >> wait_extract >> quality_check
    quality_check >> [process_orders, alert]
    quality_check >> skip
    process_orders >> load_warehouse >> aggregate >> end
    alert >> end
    skip >> end
```

### Dynamic DAG with Task Mapping (Airflow 2.3+)

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.decorators import task, dag
from airflow.models import Param

@dag(
    dag_id='multi_region_etl',
    schedule_interval='0 5 * * *',
    start_date=datetime(2024, 1, 1),
    params={
        'regions': ['us-east', 'us-west', 'eu-central', 'ap-south'],
    },
)
def region_etl():
    @task
    def extract(region):
        data = api.fetch(f'/orders?region={region}')
        return {'region': region, 'count': len(data), 'total': sum(d['amount'] for d in data)}

    @task
    def load(region_data):
        warehouse.insert('region_metrics', region_data)

    @task
    def aggregate(**context):
        # Access all results from mapped tasks
        all_data = context['ti'].xcom_pull(task_ids='extract', map_index_template='{{ ti.map_index }}')
        return {'total_regions': len(all_data), 'grand_total': sum(d['total'] for d in all_data)}

    regions = '{{ params.regions }}'.split(',')

    results = extract.expand(region=regions)
    load.expand(region_data=results)
    aggregate()

region_etl_dag = region_etl()
```

### S3 File Processing Pipeline

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.s3_file_transform import S3FileTransformOperator
from airflow.providers.amazon.aws.operators.s3 import S3CopyOperator
from airflow.providers.amazon.aws.operators.glue import AwsGlueJobOperator
from airflow.sensors.s3_key import S3KeySensor

default_args = {
    'owner': 'data-platform',
    'retries': 3,
    'retry_delay': timedelta(minutes=5),
    'aws_conn_id': 'aws_default',
}

with DAG(
    's3_glue_etl',
    default_args=default_args,
    schedule_interval='0 6 * * *',
    start_date=datetime(2024, 1, 1),
) as dag:

    wait_for_file = S3KeySensor(
        task_id='wait_for_input',
        bucket_key='s3://data-incoming/orders/{{ ds_nodash }}/*.parquet',
        bucket_name=None,
        wildcard_match=True,
        poke_interval=300,
        timeout=3600 * 8,
    )

    transform_csv_to_parquet = S3FileTransformOperator(
        task_id='convert_to_parquet',
        source_s3_key='s3://data-incoming/orders/{{ ds_nodash }}/orders.csv',
        dest_s3_key='s3://data-staging/orders/{{ ds_nodash }}/orders.parquet',
        transform_script='s3://scripts/convert_csv_parquet.py',
        select_pattern='*.csv',
        replace=True,
    )

    run_glue_job = AwsGlueJobOperator(
        task_id='run_glue_transform',
        job_name='order-enrichment',
        script_location='s3://scripts/glue/etl.py',
        region_name='us-east-1',
        iam_role_name='GlueExecutionRole',
        script_arguments={
            '--input_path': 's3://data-staging/orders/{{ ds_nodash }}/',
            '--output_path': 's3://data-warehouse/orders/',
            '--execution_date': '{{ ds }}',
        },
        num_of_dpus=10,
        retry_limit=2,
    )

    archive_input = S3CopyOperator(
        task_id='archive_input',
        source_bucket_key='s3://data-incoming/orders/{{ ds_nodash }}/',
        dest_bucket_key='s3://data-archive/orders/{{ ds_nodash }}/',
        replace=False,
    )

    wait_for_file >> transform_csv_to_parquet >> run_glue_job >> archive_input
```

## 10.2 Data Quality & Testing

### Great Expectations Integration

```python
from datetime import datetime, timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from great_expectations_provider.operators.great_expectations import GreatExpectationsOperator

with DAG(
    'data_quality_pipeline',
    schedule_interval='@daily',
    start_date=datetime(2024, 1, 1),
) as dag:

    run_great_expectations = GreatExpectationsOperator(
        task_id='run_suite',
        run_name='daily_validation',
        expectation_suite_name='orders_suite',
        data_asset_name='orders',
        batch_kwargs={
            'path': 's3://data-warehouse/staging/orders/{{ ds_nodash }}.parquet',
            'datasource': 's3_datasource',
        },
        validation_operator_name='action_list_operator',
        fail_task_on_validation_failure=True,
        use_open_lineage=False,
    )
```

## 10.3 Cross-DAG Dependencies

```python
# DAG A: Source extraction
with DAG('extract_pipeline', schedule_interval='0 2 * * *') as dag:
    extract = PythonOperator(task_id='extract', python_callable=extract_data)
    push = PythonOperator(task_id='push_to_staging', python_callable=push_staging)
    extract >> push

# DAG B: Downstream processing (listens to DAG A)
with DAG('process_pipeline', schedule_interval='0 4 * * *') as dag:
    wait = ExternalTaskSensor(
        task_id='wait_for_extract',
        external_dag_id='extract_pipeline',
        external_task_id='push_to_staging',
        execution_delta=timedelta(hours=1),
        poke_interval=600,
    )
    process = PythonOperator(task_id='process', python_callable=process_data)
    wait >> process

# DAG B (Airflow 2.8+): Asset-based trigger
from airflow.assets import Asset

extract_complete = Asset('s3://data-staging/orders/')

with DAG('process_pipeline', schedule_interval=None) as dag:
    DAG(trigger=on=[extract_complete]))  # DAG triggered by asset
```

## 10.4 CI/CD for Airflow

```yaml
# .github/workflows/airflow-ci.yml
name: Airflow CI

on:
  push:
    paths:
      - 'dags/**'
      - 'scripts/**'

jobs:
  test-dags:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Airflow
        run: pip install apache-airflow==2.9.0 --constraint constraints.txt

      - name: Lint DAGs
        run: |
          pip install flake8 black
          flake8 dags/ --max-line-length=120 --ignore=E501
          black --check dags/

      - name: Import DAGs
        run: python -c "
            import sys
            sys.path.insert(0, 'dags')
            from pathlib import Path
            for f in Path('dags').glob('*.py'):
                try:
                    __import__(f.stem)
                    print(f'OK: {f.name}')
                except Exception as e:
                    print(f'FAIL: {f.name}: {e}')
                    sys.exit(1)
            "

      - name: Airflow unit tests
        run: pytest tests/dags/ -v --tb=short
```
