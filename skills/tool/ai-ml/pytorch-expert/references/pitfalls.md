# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | Forgetting `zero_grad()` | 🔴 High | Call before every backward |
| 2 | Not calling `model.train()`/`eval()` | 🔴 High | Set mode explicitly |
| 3 | Mixing numpy and tensor types | 🔴 High | Convert consistently |
| 4 | Not moving data to device | 🔴 High | `data = data.to(device)` |
| 5 | Forgetting to detach tensors | 🟡 Medium | Use `.detach()` for tensors |
| 6 | Memory leak from retained graphs | 🟡 Medium | Check `.backward(retain_graph=False)` |
| 7 | Wrong loss function for task | 🔴 High | CrossEntropy for classification |
| 8 | No gradient clipping | 🟡 Medium | `clip_grad_norm_` for RNNs |
| 9 | DataLoader num_workers=0 on GPU | 🟡 Medium | Use 2-4 workers with pin_memory |
| 10 | Saving model during training | 🟡 Medium | Save state_dict, not entire model |

## 10.2 Common Error Solutions

### CUDA Out of Memory

```python
# Solution 1: Reduce batch size
batch_size = batch_size // 2

# Solution 2: Empty cache
torch.cuda.empty_cache()

# Solution 3: Check memory usage
print(torch.cuda.memory_allocated() / 1024**3)  # GB
print(torch.cuda.memory_reserved() / 1024**3)

# Solution 4: Use mixed precision
from torch.cuda.amp import autocast, GradScaler
scaler = GradScaler()
with autocast():
    output = model(input)
```

### Gradient Accumulation for Large Models

```python
accumulation_steps = 4
effective_batch_size = batch_size * accumulation_steps

optimizer.zero_grad()
for i, batch in enumerate(dataloader):
    output = model(batch)
    loss = criterion(output, target) / accumulation_steps
    loss.backward()

    if (i + 1) % accumulation_steps == 0:
        optimizer.step()
        optimizer.zero_grad()
```

## 10.3 DataLoader Best Practices

```python
# Recommended DataLoader settings for GPU training
train_loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4,           # Parallel data loading
    pin_memory=True,            # Faster CPU->GPU transfer
    persistent_workers=True,    # Keep workers alive
    prefetch_factor=2,          # Batches per worker
    drop_last=True,             # Skip incomplete batch
)
```

## 10.4 Memory Management

```python
# For large models, gradient checkpointing
from torch.utils.checkpoint import checkpoint

class Model(nn.Module):
    def forward(self, x):
        return checkpoint(self.layers, x, use_reentrant=False)

# Free up memory after inference
del model
torch.cuda.empty_cache()

# Move to device more efficiently
def prepare_batch(batch, device):
    if isinstance(batch, (list, tuple)):
        return [prepare_batch(b, device) for b in batch]
    return batch.to(device, non_blocking=True)
```

## 10.5 Inference Optimization

```python
# TorchScript for faster inference
model = torch.jit.trace(model, example_input)
model = torch.jit.optimize_for_inference(model)

# Inference with torch.no_grad
model.eval()
with torch.no_grad():
    # Disable dropout
    # Use eval batchnorm
    output = model(input)

# Quantization for deployment
model_int8 = torch.quantization.quantize_dynamic(
    model, {nn.Linear}, dtype=torch.qint8
)
```

## 10.6 Reproducibility

```python
import random
import numpy as np
import torch

def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)
    torch.manual_seed(seed)
    torch.cuda.manual_seed_all(seed)

    # Deterministic operations (slower)
    torch.backends.cudnn.deterministic = True
    torch.backends.cudnn.benchmark = False

set_seed(42)
```
