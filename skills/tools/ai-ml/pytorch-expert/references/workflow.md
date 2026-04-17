# Standard Workflow

## 8.1 Deep Learning Training Pipeline

```
Phase 1: Data Preparation
├── Create Dataset class
├── Implement __len__ and __getitem__
├── Add transforms (augmentation, normalization)
└── Create DataLoader with appropriate settings

Phase 2: Model Definition
├── Define nn.Module subclass
├── Initialize layers in __init__
├── Implement forward pass
└── Verify with dummy input

Phase 3: Training Loop
├── Set device (cuda/cpu)
├── Initialize optimizer and scheduler
├── For each epoch:
│   ├── Set model to train mode
│   ├── For each batch:
│   │   ├── Zero gradients
│   │   ├── Forward pass
│   │   ├── Compute loss
│   │   ├── Backward pass
│   │   └── Optimizer step
│   └── Evaluate on validation
└── Save best model

Phase 4: Deployment
├── Export to TorchScript or ONNX
└── Test exported model
```

## 8.2 Complete Training Example

```python
import torch
import torch.nn as nn
import torch.optim as optim
from torch.utils.data import DataLoader, TensorDataset

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

class Classifier(nn.Module):
    def __init__(self, input_dim, hidden_dim, num_classes):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(0.3),
            nn.Linear(hidden_dim, num_classes)
        )

    def forward(self, x):
        return self.net(x)

# Create data
X = torch.randn(1000, 20)
y = torch.randint(0, 3, (1000,))
dataset = TensorDataset(X, y)
train_loader = DataLoader(dataset, batch_size=32, shuffle=True)

# Initialize
model = Classifier(20, 128, 3).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=0.001, weight_decay=0.01)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)

# Training
best_acc = 0.0
for epoch in range(50):
    model.train()
    total_loss = 0.0
    correct = 0
    total = 0

    for batch_x, batch_y in train_loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)

        optimizer.zero_grad()
        outputs = model(batch_x)
        loss = criterion(outputs, batch_y)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()
        _, predicted = outputs.max(1)
        correct += predicted.eq(batch_y).sum().item()
        total += batch_y.size(0)

    scheduler.step()

    train_acc = 100. * correct / total
    print(f"Epoch {epoch+1}: Loss={total_loss/len(train_loader):.4f}, Acc={train_acc:.2f}%")

# Save model
torch.save(model.state_dict(), "best_model.pth")
```

## 8.3 Custom Dataset Workflow

```python
from torch.utils.data import Dataset
from PIL import Image
import os

class ImageClassificationDataset(Dataset):
    def __init__(self, root_dir, transform=None):
        self.root_dir = root_dir
        self.transform = transform
        self.classes = sorted(os.listdir(root_dir))
        self.class_to_idx = {c: i for i, c in enumerate(self.classes)}
        self.samples = self._collect_samples()

    def _collect_samples(self):
        samples = []
        for class_name in self.classes:
            class_dir = os.path.join(self.root_dir, class_name)
            for img_name in os.listdir(class_dir):
                if img_name.endswith(('.jpg', '.png')):
                    samples.append((
                        os.path.join(class_dir, img_name),
                        self.class_to_idx[class_name]
                    ))
        return samples

    def __len__(self):
        return len(self.samples)

    def __getitem__(self, idx):
        img_path, label = self.samples[idx]
        image = Image.open(img_path).convert('RGB')

        if self.transform:
            image = self.transform(image)

        return image, label

# Transforms
from torchvision import transforms

train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.2),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])
```

## 8.4 Distributed Training Workflow

```python
import os
import torch
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP

def setup(rank, world_size):
    os.environ['MASTER_ADDR'] = 'localhost'
    os.environ['MASTER_PORT'] = '12355'
    dist.init_process_group("nccl", rank=rank, world_size=world_size)

def cleanup():
    dist.destroy_process_group()

def train_ddp(rank, world_size):
    setup(rank, world_size)

    model = MyModel().to(rank)
    model = DDP(model, device_ids=[rank])

    # Create distributed sampler
    train_sampler = torch.utils.data.distributed.DistributedSampler(
        dataset,
        num_replicas=world_size,
        rank=rank,
        shuffle=True
    )

    train_loader = DataLoader(
        dataset,
        batch_size=batch_size,
        sampler=train_sampler,
        num_workers=4,
        pin_memory=True
    )

    for epoch in range(num_epochs):
        train_sampler.set_epoch(epoch)

        for batch in train_loader:
            # Training code
            ...

    cleanup()

# Launch with torchrun
# torchrun --nproc_per_node=4 train.py
```

## 8.5 Mixed Precision Training

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()

for batch in dataloader:
    optimizer.zero_grad()

    with autocast(dtype=torch.float16):
        outputs = model(batch)
        loss = criterion(outputs, targets)

    scaler.scale(loss).backward()
    scaler.step(optimizer)
    scaler.update()
```

## 8.6 Checkpointing Workflow

```python
def save_checkpoint(model, optimizer, epoch, path="checkpoint.pth"):
    checkpoint = {
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "optimizer_state_dict": optimizer.state_dict(),
    }
    torch.save(checkpoint, path)

def load_checkpoint(model, optimizer, path="checkpoint.pth"):
    checkpoint = torch.load(path)
    model.load_state_dict(checkpoint["model_state_dict"])
    optimizer.load_state_dict(checkpoint["optimizer_state_dict"])
    return checkpoint["epoch"]

# Save best and periodic
if val_acc > best_acc:
    best_acc = val_acc
    torch.save({
        "epoch": epoch,
        "model_state_dict": model.state_dict(),
        "val_acc": val_acc,
    }, "best_model.pth")

if epoch % 10 == 0:
    torch.save(model.state_dict(), f"checkpoint_epoch_{epoch}.pth")
```
