# Standard Workflow

## 8.1 W&B Experiment Tracking Workflow

```
Phase 1: Setup
├── Install wandb: pip install wandb
├── Login: wandb login
└── Initialize project

Phase 2: Configuration
├── Define hyperparameters in config
├── Group related experiments
└── Tag experiments for filtering

Phase 3: Training
├── Log metrics per step/epoch
├── Log artifacts (models, plots)
├── Log configuration
└── Use structured logging

Phase 4: Analysis
├── Compare runs in dashboard
├── Analyze learning curves
├── Track hyperparameters
└── Export data for analysis

Phase 5: Deployment
├── Log final model as artifact
├── Register model in model registry
└── Share results
```

## 8.2 Complete Training Workflow

```python
import wandb
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# Initialize
wandb.login()
wandb.init(
    project="iris-classification",
    entity="my-team",
    name="rf-baseline",
    config={
        "model": "RandomForest",
        "n_estimators": 100,
        "max_depth": 10,
        "random_state": 42
    }
)

# Load data
from sklearn.datasets import load_iris
data = load_iris()
X_train, X_test, y_train, y_test = train_test_split(
    data.data, data.target, test_size=0.2
)

# Train
model = RandomForestClassifier(
    n_estimators=wandb.config.n_estimators,
    max_depth=wandb.config.max_depth,
    random_state=wandb.config.random_state
)

# Training loop with logging
for i in range(wandb.config.n_estimators):
    model.fit(X_train, y_train)
    
    if i % 10 == 0:
        train_score = model.score(X_train, y_train)
        test_score = model.score(X_test, y_test)
        
        wandb.log({
            "train_accuracy": train_score,
            "test_accuracy": test_score,
            "n_estimators": i + 1
        })

# Final evaluation
from sklearn.metrics import classification_report
y_pred = model.predict(X_test)
wandb.log({"classification_report": wandb.Table(
    dataframe=pd.DataFrame(classification_report(y_test, y_pred, output_dict=True)).transpose()
)})

wandb.finish()
```

## 8.3 Keras Training Workflow

```python
import wandb
from wandb.keras import WandbMetricsLogger, WandbModelCheckpoint
from tensorflow import keras

wandb.init(project="image-classification")

# Build model
model = keras.Sequential([
    keras.layers.Dense(256, activation='relu', input_shape=(784,)),
    keras.layers.Dropout(0.3),
    keras.layers.Dense(10, activation='softmax')
])

model.compile(
    optimizer='adam',
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Train with W&B callbacks
model.fit(
    X_train, y_train,
    epochs=10,
    validation_data=(X_test, y_test),
    callbacks=[
        WandbMetricsLogger(),
        WandbModelCheckpoint("models/")
    ]
)

wandb.finish()
```

## 8.4 PyTorch Training Workflow

```python
import wandb
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

wandb.init(project="image-classification")

# Watch model
wandb.watch(model, log="all", log_freq=100)

# Training loop
model.train()
for epoch in range(num_epochs):
    for batch_idx, (data, targets) in enumerate(dataloader):
        optimizer.zero_grad()
        output = model(data)
        loss = criterion(output, targets)
        loss.backward()
        optimizer.step()

        if batch_idx % 100 == 0:
            wandb.log({
                "epoch": epoch,
                "batch": batch_idx,
                "loss": loss.item(),
                "learning_rate": optimizer.param_groups[0]['lr']
            })

# Log gradients and parameters
wandb.log({
    "model_gradients": wandb.Histogram(model.conv1.weight.grad),
    "model_parameters": wandb.Histogram(model.conv1.weight)
})

wandb.finish()
```

## 8.5 Hyperparameter Sweeps Workflow

```python
# train.py
import wandb

def main():
    wandb.init()
    config = wandb.config

    # Train with sweep config
    model = train_model(
        learning_rate=config.learning_rate,
        batch_size=config.batch_size,
        optimizer=config.optimizer,
    )

    # Log final metrics
    wandb.log({"test_accuracy": evaluate(model)})

if __name__ == "__main__":
    main()
```

```bash
# Create sweep
wandb sweep sweep.yaml

# Launch sweep
wandb agent <sweep_id>
```

## 8.6 Artifact Management Workflow

```python
# Log artifact
run = wandb.init(project="my-project")
artifact = wandb.Artifact("model", type="model")
artifact.add_file("model.pkl")
run.log_artifact(artifact)

# Use artifact in another run
run2 = wandb.init(project="my-project")
artifact = run2.use_artifact("my-project/model:latest")
artifact_dir = artifact.download()
model = joblib.load(f"{artifact_dir}/model.pkl")
```
