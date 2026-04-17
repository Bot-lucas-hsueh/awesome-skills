# Standard Workflow

## 8.1 MLflow Project Workflow

```
Phase 1: Setup
├── Initialize MLflow tracking server (optional)
├── Set MLFLOW_TRACKING_URI
└── Create or select experiment

Phase 2: Training Pipeline
├── Define hyperparameters to track
├── Log parameters before training
├── Train model with logging
└── Log metrics after each epoch/batch

Phase 3: Model Logging
├── Create model signature
├── Log model with framework flavor
├── Log artifacts (plots, configs)
└── Add tags for organization

Phase 4: Evaluation
├── Log evaluation metrics
├── Compare runs in UI
└── Select best model for registry

Phase 5: Deployment
├── Register model
├── Transition to staging/production
└── Deploy from registry
```

## 8.2 Complete Training Pipeline

```python
import mlflow
import mlflow.sklearn
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score, f1_score
from sklearn.datasets import load_iris
import numpy as np

# Setup tracking
mlflow.set_tracking_uri("http://localhost:5000")
mlflow.set_experiment("iris_classification")

# Load data
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2
)

# Enable autologging
mlflow.sklearn.autolog()

# Grid search with logging
with mlflow.start_run(run_name="rf_grid_search"):
    param_grid = {
        "n_estimators": [50, 100, 200],
        "max_depth": [3, 5, 10],
        "min_samples_split": [2, 5],
    }

    rf = RandomForestClassifier()
    grid_search = GridSearchCV(
        rf, param_grid, cv=5, scoring="accuracy"
    )

    grid_search.fit(X_train, y_train)

    # Best model predictions
    best_model = grid_search.best_estimator_
    y_pred = best_model.predict(X_test)

    # Log additional metrics
    mlflow.log_metrics({
        "test_accuracy": accuracy_score(y_test, y_pred),
        "test_f1": f1_score(y_test, y_pred, average="weighted"),
    })

    # Log best params explicitly
    mlflow.log_params(grid_search.best_params_)

    # Log model with signature
    signature = mlflow.models.infer_signature(
        X_test, y_pred
    )
    mlflow.sklearn.log_model(
        best_model,
        "model",
        signature=signature
    )

    print(f"Best params: {grid_search.best_params_}")
```

## 8.3 Custom Logging Workflow

```python
import mlflow
import numpy as np
import matplotlib.pyplot as plt

# For frameworks without native autolog
with mlflow.start_run(run_name="custom_training"):
    # Log parameters
    mlflow.log_param("optimizer", "adam")
    mlflow.log_param("learning_rate", 0.001)
    mlflow.log_param("batch_size", 32)
    mlflow.log_param("epochs", 100)

    # Training loop
    for epoch in range(100):
        train_loss = train_epoch()
        val_loss, val_acc = evaluate()

        # Log metrics per epoch
        mlflow.log_metrics({
            "train_loss": train_loss,
            "val_loss": val_loss,
            "val_accuracy": val_acc,
        }, step=epoch)

        # Log plot at certain intervals
        if epoch % 10 == 0:
            fig = plot_training_curves()
            mlflow.log_artifact("training_plot.png")

    # Log final model and config
    mlflow.log_artifact("config.json")
    mlflow.log_dict({"training_config": {...}}, "config.json")
```

## 8.4 Model Registry Workflow

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

model_name = "recommendation_model"

# Register from run
run_id = "abc123"
model_uri = f"runs:/{run_id}/model"

client.register_model(model_uri, model_name)

# Transition through stages
for version in [1, 2, 3]:
    # Staging
    client.transition_model_version_stage(
        name=model_name,
        version=version,
        stage="Staging"
    )

    # After validation...
    if validate_model(model_name, version):
        client.transition_model_version_stage(
            name=model_name,
            version=version,
            stage="Production"
        )
        # Archive older production versions
        archive_old_production(client, model_name, version)

# Load production model
production_model = mlflow.pyfunc.load_model(
    f"models:/{model_name}/production"
)
```

## 8.5 Distributed Training with MLflow

```python
import mlflow
from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Only main process logs
if rank == 0:
    mlflow.set_experiment("distributed_training")
    run = mlflow.start_run(run_name="multi_gpu")
    mlflow.log_param("num_gpus", comm.Get_size())

# All processes do training
model = train_distributed(comm)

if rank == 0:
    mlflow.log_metric("final_loss", model.loss)
    mlflow.sklearn.log_model(model, "model")
    mlflow.end_run()
```

## 8.6 MLflow Projects Workflow

```yaml
# MLproject file
name: training_pipeline

entry_points:
  main:
    command: "python train.py --lr {lr} --epochs {epochs}"
    parameters:
      lr:
        type: float
        default: 0.01
      epochs:
        type: int
        default: 100

conda_env: conda.yaml
```

```bash
# Run project
mlflow run github.com/user/repo --param1=value1

# Run locally
mlflow run . -P lr=0.001 -P epochs=50

# Run with specific Git ref
mlflow run git://github.com/user/repo@v1.0 --entry-point main
```
