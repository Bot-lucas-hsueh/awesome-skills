# Standards & Reference

## 7.1 Official Documentation

- [MLflow Documentation](https://mlflow.org/docs/latest/index.html)
- [MLflow GitHub](https://github.com/mlflow/mlflow)
- [MLflow Tracking API](https://mlflow.org/docs/latest/python_api/mlflow.html)
- [MLflow Models](https://mlflow.org/docs/latest/models.html)
- [MLflow Model Registry](https://mlflow.org/docs/latest/model-registry.html)
- [MLflow Projects](https://mlflow.org/docs/latest/projects.html)

## 7.2 Installation

```bash
pip install mlflow>=2.0
pip install mlflow[extras]  # With common integrations

# Database backend
pip install mlflow[sqlalchemy]
pip install mlflow[databricks]

# For specific integrations
pip install mlflow[sklearn]
pip install mlflow[xgboost]
pip install mlflow[catboost]
pip install mlflow[spark]
```

## 7.3 MLflow Tracking API

### Starting Runs

```python
import mlflow

# Simple tracking
mlflow.start_run()
mlflow.log_param("learning_rate", 0.01)
mlflow.log_metric("accuracy", 0.95)
mlflow.end_run()

# Context manager (recommended)
with mlflow.start_run(run_name="experiment_001"):
    mlflow.log_param("epochs", 100)
    mlflow.log_metric("loss", 0.25)
```

### Logging Data Types

| Function | Description | Example |
|----------|-------------|---------|
| `log_param()` | Log parameter | `mlflow.log_param("lr", 0.01)` |
| `log_metric()` | Log metric | `mlflow.log_metric("acc", 0.95)` |
| `log_params()` | Log dict of params | `mlflow.log_params({"lr": 0.01, "bs": 32})` |
| `log_metrics()` | Log dict of metrics | `mlflow.log_metrics({"acc": 0.95, "f1": 0.92})` |
| `log_artifact()` | Log file artifact | `mlflow.log_artifact("model.pkl")` |
| `log_model()` | Log model | `mlflow.sklearn.log_model(model, "model")` |

## 7.4 Framework-Specific Logging

```python
# Scikit-learn
import mlflow.sklearn

mlflow.sklearn.autolog()
model.fit(X_train, y_train)
mlflow.sklearn.log_model(model, "model")

# PyTorch
import mlflow.pytorch
mlflow.pytorch.autolog()

# XGBoost
import mlflow.xgboost
mlflow.xgboost.autolog()

# Keras/TensorFlow
mlflow.tensorflow.autolog()

# LightGBM
mlflow.lightgbm.autolog()
```

## 7.5 MLflow Experiments

```python
# Create experiment
mlflow.create_experiment("my_experiment")

# Set active experiment
mlflow.set_experiment("my_experiment")

# List experiments
experiments = mlflow.list_experiments()

# Get experiment by name
exp = mlflow.get_experiment_by_name("my_experiment")
```

## 7.6 MLflow Models

```python
from mlflow.models import infer_signature

# Log model with signature
signature = infer_signature(X_test, model.predict(X_test))
mlflow.sklearn.log_model(
    model,
    "model",
    signature=signature,
    input_example=X_test[:1]
)

# Load model
loaded_model = mlflow.sklearn.load_model("runs:/run_id/model")

# Model flavors
mlflow.spark.log_model(spark_model, "model")
mlflow.pyfunc.log_model("model", loader_module=custom_module)
```

## 7.7 Model Registry

```python
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Register model
model_uri = "runs:/run_id/model"
model_name = "production_model"
client.register_model(model_uri, model_name)

# Transition stages
client.transition_model_version_stage(
    name=model_name,
    version=1,
    stage="Production"
)

# Get latest version in stage
latest = client.get_latest_version(model_name, stage="Production")
```

## 7.8 MLflow Server

```bash
# Local file store (default)
mlflow server --backend-store-uri ./mlruns --port 5000

# SQLite backend
mlflow server --backend-store-uri sqlite:///mlflow.db

# PostgreSQL backend
mlflow server \
    --backend-store-uri postgresql://user:pass@host/mlflow \
    --default-artifact-root s3://bucket/path

# With tracking URI
export MLFLOW_TRACKING_URI=http://localhost:5000
```
