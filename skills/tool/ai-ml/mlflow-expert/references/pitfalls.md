# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Not setting tracking URI | 🟡 Medium | `mlflow.set_tracking_uri()` early |
| 2 | Logging too many metrics | 🟡 Medium | Log summary, not per-batch |
| 3 | Using same run for multiple experiments | 🔴 High | Create separate runs |
| 4 | Not logging artifacts | 🟡 Medium | Log configs, plots, data samples |
| 5 | Missing model signatures | 🟡 Medium | Always add `infer_signature()` |
| 6 | Large artifact storage | 🟡 Medium | Log model only, not raw data |
| 7 | No experiment naming | 🟡 Medium | Use descriptive experiment names |
| 8 | Not using autolog | 🟡 Medium | Enable autolog for supported frameworks |
| 9 | Hardcoded run IDs | 🔴 High | Use URI pattern `runs:/run_id/path` |
| 10 | Ignoring model registry | 🟡 Medium | Use registry for production models |

## 10.2 Performance Issues

### Slow Tracking

```python
# Problem: Tracking slows down training
# Solution: Batch metric logging

# BAD: Log every batch
for batch in dataloader:
    mlflow.log_metric("batch_loss", loss.item())

# GOOD: Buffer and log periodically
batch_losses = []
for batch in dataloader:
    batch_losses.append(loss.item())
    if len(batch_losses) >= 100:
        mlflow.log_metric("avg_loss", np.mean(batch_losses[-100:]))
```

### Large Model Artifacts

```python
# Problem: Model artifact too large
# Solution: Use compression or exclude files

# Compress before logging
import shutil
model_path = "/tmp/model"
mlflow.sklearn.log_model(model, "model", serialization_format="pickle")

# Exclude large files from artifacts
mlflow.log_artifact("model.pkl", exclude_paths=["*.h5", "*.pt"])

# Use artifact location optimization
# Configure artifact root to fast storage
mlflow server --artifact-root /fast-nvme/artifacts
```

## 10.3 Model Registry Issues

```python
# Problem: Version conflicts
# Solution: Use unique stage assignments

from mlflow.exceptions import MlflowException

try:
    client.transition_model_version_stage(
        name=model_name,
        version=new_version,
        stage="Production"
    )
except MlflowException:
    # Archive current production first
    current = client.get_latest_version(model_name, stage="Production")
    client.transition_model_version_stage(
        name=model_name,
        version=current.version,
        stage="Archived"
    )
    # Then promote new version
    client.transition_model_version_stage(
        name=model_name,
        version=new_version,
        stage="Production"
    )
```

## 10.4 Multi-Node Training Issues

```python
# Problem: Duplicate logging in distributed training
# Solution: Use rank 0 for logging

def train_distributed(rank, world_size):
    if rank == 0:
        mlflow.start_run(run_name="distributed_training")
        mlflow.log_param("world_size", world_size)

    # All workers do training
    train_sync()

    if rank == 0:
        mlflow.log_metric("final_metric", result)
        mlflow.end_run()
```

## 10.5 Autolog Best Practices

```python
# Enable autolog with customization
mlflow.sklearn.autolog(
    log_input_examples=True,
    log_model_signatures=True,
    max_tuning_runs=5,  # Limit for hyperparameter search
    silent=False,        # Show autolog warnings
)

# Disable autolog for specific code
mlflow.sklearn.autolog(disable=True)
custom_training_code()
mlflow.sklearn.autolog(enable=True)
```

## 10.6 Storage Configuration

```python
# Recommended backend configurations

# For SQLite (small scale)
mlflow server --backend-store-uri sqlite:///mlflow.db

# For PostgreSQL (medium scale)
mlflow server \
    --backend-store-uri postgresql://user:pass@host/mlflowdb \
    --default-artifact-root s3://bucket/mlartifacts

# For production with S3
import boto3
mlflow.set_tracking_uri("http://mlflow-server:5000")

# Configure S3 artifact storage
mlflow.s3.extra_env['AWS_ACCESS_KEY_ID'] = access_key
mlflow.s3.extra_env['AWS_SECRET_ACCESS_KEY'] = secret_key
```
