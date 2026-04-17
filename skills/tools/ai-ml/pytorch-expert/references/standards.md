# Standards & Reference

## 7.1 Official Documentation

- [PyTorch Documentation](https://pytorch.org/docs/)
- [PyTorch Tutorials](https://pytorch.org/tutorials/)
- [PyTorch API Reference](https://pytorch.org/docs/stable/index.html)
- [TorchScript](https://pytorch.org/docs/stable/jit.html)
- [PyTorch Mobile](https://pytorch.org/mobile/home/)
- [PyTorch Lightning](https://lightning.ai/docs/pytorch/stable/)
- [HuggingFace Accelerate](https://huggingface.co/docs/accelerate/)

## 7.2 Installation

```bash
# CPU only
pip install torch

# With CUDA (specific version)
pip install torch --index-url https://download.pytorch.org/whl/cu118
pip install torch --index-url https://download.pytorch.org/whl/cu121

# With torchvision, torchaudio
pip install torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

## 7.3 Tensor Operations

### Creation

```python
import torch

# From data
x = torch.tensor([1.0, 2.0, 3.0])

# Zeros, ones, random
z = torch.zeros(3, 4)
r = torch.randn(3, 4)          # Normal distribution
ru = torch.rand(3, 4)          # Uniform [0, 1)

# From numpy
import numpy as np
arr = np.array([1, 2, 3])
x = torch.from_numpy(arr)

# Like another tensor
x_like = torch.zeros_like(x)
```

### Operations

| Operation | Description |
|-----------|-------------|
| `x.view()` | Reshape tensor |
| `x.squeeze()` | Remove dimensions of size 1 |
| `x.unsqueeze()` | Add dimension |
| `x.matmul(y)` | Matrix multiply |
| `x @ y` | Short for matmul |
| `x.sum(dim=0)` | Sum along dimension |
| `x.mean(dim=1)` | Mean along dimension |
| `x.argmax(dim=1)` | Index of max value |

## 7.4 nn.Module Reference

```python
import torch.nn as nn

class MyModel(nn.Module):
    def __init__(self, input_dim, hidden_dim, output_dim):
        super().__init__()  # Always call super().__init__()
        self.layer1 = nn.Linear(input_dim, hidden_dim)
        self.relu = nn.ReLU()
        self.layer2 = nn.Linear(hidden_dim, output_dim)
        self.dropout = nn.Dropout(0.5)

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.dropout(x)
        x = self.layer2(x)
        return x

    def count_parameters(self):
        return sum(p.numel() for p in self.parameters() if p.requires_grad)
```

### Common Layers

| Layer | Description |
|-------|-------------|
| `nn.Linear(in, out)` | Fully connected |
| `nn.Conv2d(in, out, kernel_size)` | 2D convolution |
| `nn.LSTM(input, hidden, num_layers)` | LSTM |
| `nn.BatchNorm2d(channels)` | Batch normalization |
| `nn.Dropout(p)` | Dropout |
| `nn.Embedding(vocab_size, embed_dim)` | Word embeddings |
| `nn.MultiheadAttention(embed, num_heads)` | Attention |

## 7.5 Optimizers Reference

```python
import torch.optim as optim

# SGD with momentum
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9)

# Adam (most common for DL)
optimizer = optim.Adam(model.parameters(), lr=0.001, betas=(0.9, 0.999))

# AdamW (Adam with weight decay)
optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)

# Learning rate scheduler
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=10, gamma=0.1)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)
scheduler = optim.lr_scheduler.OneCycleLR(
    optimizer, max_lr=0.01, epochs=50, steps_per_epoch=100
)
```

## 7.6 DataLoader Reference

```python
from torch.utils.data import Dataset, DataLoader

class CustomDataset(Dataset):
    def __init__(self, X, y):
        self.X = torch.tensor(X, dtype=torch.float32)
        self.y = torch.tensor(y, dtype=torch.long)

    def __len__(self):
        return len(self.y)

    def __getitem__(self, idx):
        return self.X[idx], self.y[idx]

# DataLoader
train_loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True,
    num_workers=4,          # Parallel data loading
    pin_memory=True,          # Faster GPU transfer
    drop_last=True,           # Drop incomplete batch
)

# In training
for batch_idx, (data, targets) in enumerate(train_loader):
    data, targets = data.cuda(), targets.cuda()
    # Training step
```

## 7.7 Distributed Training

```python
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

# Setup
dist.init_process_group("nccl")  # or "gloo" for CPU
local_rank = int(os.environ["LOCAL_RANK"])

# Create model with DDP
model = MyModel().cuda(local_rank)
model = DDP(model, device_ids=[local_rank])

# Training loop
for batch in dataloader:
    optimizer.zero_grad()
    output = model(batch.cuda())
    loss = criterion(output, target.cuda())
    loss.backward()
    optimizer.step()

# Cleanup
dist.destroy_process_group()
```

## 7.8 TorchScript & Export

```python
# Trace model
model.eval()
example_input = torch.randn(1, 3, 224, 224)
traced = torch.jit.trace(model, example_input)
traced.save("model_traced.pt")

# Script model (for control flow)
scripted = torch.jit.script(model)
scripted.save("model_scripted.pt")

# Export to ONNX
torch.onnx.export(
    model, example_input, "model.onnx",
    input_names=["input"],
    output_names=["output"],
    dynamic_axes={"input": {0: "batch"}, "output": {0: "batch"}}
)
```
