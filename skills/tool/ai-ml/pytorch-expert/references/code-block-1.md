# Modern Training Loop (AMP + GradScaler)

Complete PyTorch training loop with Automatic Mixed Precision for efficient GPU training.

```python
import torch
import torch.nn as nn
from torch.cuda.amp import autocast, GradScaler

model = MyModel().cuda()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()
scaler = GradScaler()

for epoch in range(num_epochs):
    for batch in train_loader:
        optimizer.zero_grad(set_to_none=True)

        with autocast(device_type='cuda', dtype=torch.bfloat16):
            outputs = model(batch["inputs"])
            loss = criterion(outputs, batch["labels"])

        scaler.scale(loss).backward()

        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        scaler.step(optimizer)
        scaler.update()

# Key points:
# - zero_grad(set_to_none=True) is faster than zero_grad()
# - autocast with bfloat16 on Ampere+ GPUs
# - GradScaler prevents NaN in fp16 gradients
# - clip_grad_norm_ prevents gradient explosion
```
