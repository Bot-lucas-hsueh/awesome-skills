# Branching Based on External Condition

Conditional task execution based on external system availability.

```python
from airflow.operators.empty import EmptyOperator
from airflow.operators.python import BranchPythonOperator

def should_run_full_pipeline():
    """Decide which branch to execute."""
    if api.is_available():
        return 'extract'  # Run full pipeline
    else:
        return 'skip_pipeline'  # Skip to notification

start = EmptyOperator(task_id='start')
branch = BranchPythonOperator(
    task_id='branching',
    python_callable=should_run_full_pipeline,
)

extract = EmptyOperator(task_id='extract')
transform = EmptyOperator(task_id='transform')
load = EmptyOperator(task_id='load')
skip_pipeline = EmptyOperator(task_id='skip_pipeline')
notify = EmptyOperator(task_id='notify')

# Set dependencies
start >> branch
branch >> [extract, skip_pipeline]  # Branch to either path
extract >> transform >> load >> notify
skip_pipeline >> notify

# Key points:
# - BranchPythonOperator returns task_id to execute
# - All branches must be listed: branch >> [task_a, task_b]
# - Non-selected branches are skipped, not failed
# - Use for conditional logic based on external state
```
