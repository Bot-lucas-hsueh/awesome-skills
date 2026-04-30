# Image Classifier with Modern PyTorch

Complete training pipeline with EfficientNet, AMP, and best practices.

```python
import torch
import torch.nn as nn
import torchvision.models as models
from torch.utils.data import DataLoader
from torch.cuda.amp import autocast, GradScaler

# Model setup
model = models.efficientnet_b0(weights=models.EfficientNet_B0_Weights.IMAGENET1K_V1)
model.classifier[-1] = nn.Linear(model.classifier[-1].in_features, num_classes)
model = model.cuda()

# Mixed precision + gradient clipping
scaler = GradScaler()
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-4, weight_decay=0.01)
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=30)

for epoch in range(30):
    model.train()
    for batch in train_loader:
        optimizer.zero_grad(set_to_none=True)

        with autocast(device_type='cuda'):
            outputs = model(batch["image"].cuda())
            loss = nn.CrossEntropyLoss()(outputs, batch["label"].cuda())

        scaler.scale(loss).backward()
        scaler.unscale_(optimizer)
        torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
        scaler.step(optimizer)
        scaler.update()

    scheduler.step()

    # Validation
    model.eval()
    with torch.no_grad():
        correct = sum((model(batch["image"].cuda()).argmax(1) == batch["label"].cuda()).sum()
        print(f"Epoch {epoch}: acc={correct/len(val_set):.4f}")
```
