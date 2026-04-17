# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Logging too frequently | 🟡 Medium | Log every N steps, not every batch |
| 2 | Logging large tensors | 🟡 Medium | Log summaries, not raw tensors |
| 3 | Not grouping related runs | 🟡 Medium | Use `group` parameter |
| 4 | Using same name for all runs | 🟡 Medium | Use unique names or let W&B auto-generate |
| 5 | Forgetting to finish runs | 🟡 Medium | Always call `wandb.finish()` |
| 6 | Logging sensitive data | 🔴 High | Use `wandb.Api` to redact or exclude |
| 7 | Not using config | 🟡 Medium | Log hyperparameters in config |
| 8 | Large artifact without versioning | 🟡 Medium | Use Artifacts for version control |
| 9 | Inconsistent metric names | 🟡 Medium | Use consistent naming convention |
| 10 | Logging after finish | 🟡 Medium | Check `run.status` before logging |

## 10.2 Performance Issues

### Slow Logging

```python
# Problem: Too many logs slow down training
# Solution: Log less frequently

# BAD: Log every batch
for batch in dataloader:
    wandb.log({"loss": loss.item()})

# GOOD: Log every N steps
if step % 100 == 0:
    wandb.log({"loss": loss.item()})
```

### Large Artifacts

```python
# Problem: Large model files slow down syncing
# Solution: Use Artifact versioning and compression

artifact = wandb.Artifact("model", type="model")
artifact.add_file("large_model.h5", name="model_weights")
run.log_artifact(artifact)

# For very large models, use artifact reference
artifact.add_reference("s3://bucket/large-model/", name="model")
```

## 10.3 Data Leakage Prevention

```python
# Problem: Accidentally logging sensitive data
# Solution: Use wandb.Api to sanitize

# Before logging
import wandb
api = wandb.Api()

# Check if data contains sensitive info
def sanitize_data(data):
    # Remove PII columns
    sensitive_cols = ['ssn', 'password', 'credit_card']
    for col in sensitive_cols:
        if col in data.columns:
            data = data.drop(columns=[col])
    return data

# Log only non-sensitive metrics
wandb.log({"accuracy": accuracy, "auc": auc})  # No PII
```

## 10.4 Multi-Process Logging

```python
# Problem: Duplicate logs in distributed training
# Solution: Use rank-aware logging

def log_metrics(rank, metrics, step):
    if rank == 0:
        wandb.log(metrics, step=step)

# Or use W&B's built-in multi-process support
wandb.init(settings=wandb.Settings(
    start_method="thread",
    init_kwargs={"group": "distributed-training"}
))
```

## 10.5 Offline Mode Best Practices

```python
# Work offline and sync later
wandb.init(mode="offline")

# Training code...

wandb.finish()

# Sync when online
# wandb sync /path/to/logs
```

## 10.6 Security Best Practices

```python
# Don't log API keys
# BAD:
wandb.log({"api_key": my_api_key})

# GOOD: Use environment variables
import os
api_key = os.environ.get("WANDB_API_KEY")
if api_key:
    wandb.login(key=api_key)

# Use secret for sensitive configs
wandb.config.update({
    "public_param": 0.01,
    # "private_param": 0.01  # Don't log sensitive params
})

# Redact sensitive patterns from logs
wandb.init()
run = wandb.run
run.config.update({"seed": 42}, allow_val_change=True)
```

## 10.7 Quick Reference Checklist

```python
# Before training
wandb.login()                                  # Login
wandb.init(                                    # Initialize
    project="project-name",
    entity="team-name",
    name="run-name",
    config={"lr": 0.01, "bs": 32}
)

# During training
wandb.log({"loss": loss, "acc": acc}, step=step)  # Log metrics
wandb.watch(model)                             # Watch gradients
wandb.log_artifact(artifact)                   # Log artifacts

# After training
wandb.finish()                                 # Always finish

# For sweeps
wandb.agent(sweep_id, function=train)          # Run agent
```
