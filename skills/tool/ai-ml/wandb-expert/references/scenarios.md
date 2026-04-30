# Scenario Examples

## 9.1 Distributed Training Logging

**User:** "Track multi-GPU training across processes"

**W&B Expert:**
> **Distributed Logging:**
>
> ```python
> import wandb
> import torch.distributed as dist
> from torch.nn.parallel import DistributedDataParallel as DDP

> def train(rank, world_size):
>     # Initialize W&B with rank for multi-process
>     wandb.init(
>         project="distributed-training",
>         name=f"rank-{rank}",
>         group="experiment-1",  # Group runs together
>         config={"rank": rank, "world_size": world_size}
>     )
>
>     # Setup DDP
>     dist.init_process_group("nccl", rank=rank, world_size=world_size)
>     model = MyModel().cuda(rank)
>     model = DDP(model, device_ids=[rank])
>
>     # Training
>     for epoch in range(num_epochs):
>         for batch in dataloader:
>             train_step(model, batch)
>
>             # Log only from rank 0 to avoid duplicates
>             if rank == 0:
>                 wandb.log({"loss": loss.item(), "epoch": epoch})
>
>     wandb.finish()
>     dist.destroy_process_group()
> ```

## 9.2 Logging Visualizations

**User:** "Log plots and visualizations"

**W&B Expert:**
> **Visualization Logging:**
>
> ```python
> import wandb
> import matplotlib.pyplot as plt
>
> # Log matplotlib figures
> fig, ax = plt.subplots()
> ax.plot(history['train_loss'], label='Train')
> ax.plot(history['val_loss'], label='Val')
> ax.set_xlabel('Epoch')
> ax.set_ylabel('Loss')
> ax.legend()
> wandb.log({"loss_curves": wandb.Image(fig)})
>
> # Log interactive plotly
> import plotly.express as px
> fig = px.scatter(df, x="prediction", y="actual", color="error")
> wandb.log({"scatter": fig})
>
> # Log histogram
> wandb.log({"feature_distribution": wandb.Histogram(np.array(feature_data))})
>
> # Log 3D point cloud
> wandb.log({"point_cloud": wandb.Object3D(open("scene.glb", "rb").read())})
> ```

## 9.3 Cross-Validation Logging

**User:** "Track cross-validation folds"

**W&B Expert:**
> **Cross-Validation Logging:**
>
> ```python
> import wandb
> from sklearn.model_selection import KFold
>
> wandb.init(project="cross-validation", name="cv-run")
>
> kfold = KFold(n_splits=5, shuffle=True, random_state=42)
> fold_metrics = []
>
> for fold, (train_idx, val_idx) in enumerate(kfold.split(X)):
>     with wandb.init(
>         project="cross-validation",
>         name=f"fold-{fold}",
>         group="experiment",  # Group all folds
>         reinit=True  # Start new run for each fold
>     ):
>         X_train, X_val = X[train_idx], X[val_idx]
>
>         # Train
>         model = train_model(X_train, y_train)
>         metrics = evaluate(model, X_val, y_val)
>
>         # Log fold metrics
>         wandb.log({
>             "fold": fold,
>             "val_accuracy": metrics["accuracy"],
>             "val_f1": metrics["f1"]
>         })
>
>         fold_metrics.append(metrics)
>
> # Aggregate results
> wandb.finish()
>
> # Log summary to parent run
> wandb.init(project="cross-validation", name="cv-summary")
> wandb.log({
>     "mean_accuracy": np.mean([m["accuracy"] for m in fold_metrics]),
>     "std_accuracy": np.std([m["accuracy"] for m in fold_metrics])
> })
> ```

## 9.4 Hyperparameter Search with Sweeps

**User:** "Run automated hyperparameter search"

**W&B Expert:**
> **Sweep Configuration:**
>
> ```yaml
> # sweep.yaml
> project: hp-search
> method: bayes  # Bayesian optimization
> metric:
>   name: val_accuracy
>   goal: maximize
> parameters:
>   learning_rate:
>     min: 0.0001
>     max: 0.1
>     distribution: log_uniform
>   batch_size:
>     values: [16, 32, 64, 128]
>   hidden_size:
>     values: [64, 128, 256, 512]
>   optimizer:
>     values: ["adam", "sgd", "adamw"]
> early_terminate:
>   type: hyperband
>   s: 2
>   eta: 3
> max_iter: 50
> ```
>
> ```bash
> # Start sweep controller
> wandb sweep sweep.yaml
>
> # Run multiple agents
> for i in {1..4}; do
>     wandb agent <sweep-id>
> done
> ```

## 9.5 Model Versioning and Registry

**User:** "Manage model versions in production"

**W&B Expert:**
> **Model Registry:**
>
> ```python
> import wandb
>
> # Log model as artifact
> run = wandb.init(project="production-models")
> artifact = wandb.Artifact(
>     "recommendation-model",
>     type="model",
>     metadata={
>         "accuracy": 0.95,
>         "dataset": "v2",
>         "training_time": "2h"
>     }
> )
> artifact.add_file("model.pkl")
> run.log_artifact(artifact)
>
> # Promote to model registry
> artifact = run.use_artifact("recommendation-model:v3")
> artifact.add_tag("production")
>
> # Load from registry in another project
> run2 = wandb.init(project="inference")
> model_artifact = run2.use_artifact("my-team/production-models/recommendation-model:latest")
> model_dir = model_artifact.download()
> model = joblib.load(f"{model_dir}/model.pkl")
> ```
