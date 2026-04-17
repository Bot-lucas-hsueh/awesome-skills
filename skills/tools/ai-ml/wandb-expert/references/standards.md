# Standards & Reference

## 7.1 Official Documentation

- [W&B Documentation](https://docs.wandb.ai/)
- [W&B Python SDK](https://docs.wandb.ai/library)
- [W&B Weave](https://wandb.github.io/weave/)
- [W&B Sweeps](https://docs.wandb.ai/library/sweeps)
- [W&B Artifacts](https://docs.wandb.ai/library/artifacts)

## 7.2 Installation

```bash
pip install wandb
pip install wandb[media]  # With media logging support
pip install wandb[ios]    # With iOS support
```

## 7.3 Quick Start

```python
import wandb

# Login
wandb.login()

# Initialize run
wandb.init(
    project="my-project",
    entity="my-team",           # Team/organization
    name="experiment-001",       # Run name
    notes="Baseline experiment",
    tags=["baseline", "v1"]
)

# Log metrics
wandb.log({"loss": 0.5, "accuracy": 0.8})

# Log configuration
wandb.config.update({
    "learning_rate": 0.01,
    "batch_size": 32,
    "epochs": 100
})

# Log model
wandb.save("model.h5")
wandb.log_artifact(artifact)

# Finish run
wandb.finish()
```

## 7.4 Logging Reference

| Function | Description | Example |
|----------|-------------|---------|
| `log()` | Log metrics | `wandb.log({"loss": 0.5})` |
| `log()` with step | Log with explicit step | `wandb.log({"loss": 0.5}, step=100)` |
| `log_code()` | Log source code | `wandb.log_code()` |
| `log_model()` | Log model checkpoint | `wandb.log_model()` |
| `log_artifact()` | Log artifact | `wandb.log_artifact(artifact)` |
| `log_text()` | Log text | `wandb.log({"table": wandb.Table(...)})` |
| `log_image()` | Log image | `wandb.log({"image": wandb.Image(...)})` |
| `log_table()` | Log table | `wandb.log({"table": wandb.Table(...)})` |

## 7.5 Configuration Reference

```python
wandb.init(
    # Project settings
    project="project-name",
    entity="team-name",

    # Run metadata
    name="run-name",
    notes="Description",
    tags=["tag1", "tag2"],

    # Configuration
    config={"lr": 0.01, "bs": 32},

    # Logging
    dir="/path/to/logs",
    mode="online",      # "offline", "dryrun", "disabled"

    # Tracking
    track_numpy=True,    # Auto-track numpy arrays
    log_artifacts=True, # Log output artifacts
)
```

## 7.6 Artifacts Reference

```python
# Create artifact
artifact = wandb.Artifact("my-dataset", type="dataset")

# Add files
artifact.add_file("data.csv")
artifact.add_dir("images/")
artifact.add_reference("s3://bucket/path")

# Log artifact
run.log_artifact(artifact)

# Use artifact in another run
artifact = run.use_artifact("my-dataset:latest")
artifact.download()
```

## 7.7 Sweeps Reference

```yaml
# sweep.yaml
program: train.py
method: bayes
metric:
  name: val_loss
  goal: minimize
parameters:
  learning_rate:
    min: 0.0001
    max: 0.1
    distribution: log_uniform
  batch_size:
    values: [16, 32, 64]
```

```bash
# Start sweep
wandb sweep sweep.yaml

# Run agent
wandb agent wandb/team/project/sweep-id
```

## 7.8 Integration Reference

```python
# Keras
from wandb.keras import WandbCallback

model.fit(
    X_train, y_train,
    callbacks=[WandbCallback()]
)

# PyTorch
from wandb.sdk.wandb_run import watch

watch(model)  # Log gradients and parameters

# Scikit-learn
from wandb.sklearn import plot_classifier, plot_regressor

wandb.sklearn.plot_classifier(clf, X_train, X_test, y_train, y_test, ...)
```

## 7.9 Table Reference

```python
import pandas as pd

# Create table
table = wandb.Table(dataframe=df)

# Log table
wandb.log({"predictions": table})

# Create manually
table = wandb.Table(
    columns=["epoch", "loss", "accuracy"],
    data=[[1, 0.5, 0.8], [2, 0.3, 0.9]]
)

# Add rows
table.add_data(3, 0.2, 0.95)

# Log with matplotlib
wandb.log({"chart": wandb.Image(plt)})
```
