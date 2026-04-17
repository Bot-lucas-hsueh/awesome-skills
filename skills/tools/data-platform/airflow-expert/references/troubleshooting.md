# Troubleshooting Guide

## 8.1 DAG Failures

### Task Stuck in Queue
- Check scheduler is running: `airflow scheduler`
- Verify executor has capacity
- Check for deadlocks in DAG
- Review scheduler logs

### Task Failed
- Check task logs in UI
- Verify dependencies completed
- Check retry configuration
- Inspect XCom for data issues

## 8.2 Connection Issues

### Database Connection Failed
```bash
# Test connection
airflow connections test my_postgres

# List connections
airflow connections list
```

### Hook Errors
- Verify connection details in Admin > Connections
- Check secrets backend
- Verify credentials not expired

## 8.3 Scheduler Issues

### DAG Not Loading
- Check DAG folder path in airflow.cfg
- Verify import path correct
- Check for syntax errors in DAG file
- Restart scheduler after changes

### Performance Issues
```ini
# airflow.cfg optimizations
[scheduler]
job_heartbeat_sec = 5
scheduler_heartbeat_sec = 5
min_file_process_interval = 30
dag_dir_list_interval = 300
```

## 8.4 Worker Issues

### Celery Workers Not Starting
- Verify Celery broker (Redis/RabbitMQ) running
- Check worker logs
- Verify Result Backend accessible
- Check Flower for worker status

### Task Executor Issues
```bash
# Check running tasks
airflow tasks list dag_id

# Kill stuck task
airflow tasks kill dag_id task_id execution_date
```

## 8.5 Variable & Secret Issues

### Variable Not Found
- Check variable exists: `airflow variables get my_var`
- Verify serialized JSON format
- Check Variable import

## 8.6 Database Migration Issues

```bash
# Check current version
airflow db check

# Migrate database
airflow db upgrade

# Reset database (development only!)
airflow db reset
```

## 8.7 Debugging Commands

```bash
# Test DAG parsing
python -c "from airflow import DAG; from airflow.example_dags import tutorial; print('OK')"

# List tasks
airflow tasks list my_dag

# Run task locally
airflow tasks test my_dag my_task 2024-01-01

# Clear task instance
airflow tasks clear my_dag -s 2024-01-01 -f -d
```