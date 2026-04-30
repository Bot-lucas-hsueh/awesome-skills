# Distributed Training (DDP)

Multi-GPU distributed training using DistributedDataParallel.

```python
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data import DistributedSampler

# Setup (use torchrun for launching)
# torchrun --standalone --nnodes=1 --nproc_per_node=4 train.py

def setup():
    dist.init_process_group("nccl")
    torch.cuda.set_device(int(os.environ["LOCAL_RANK"]))

def cleanup():
    dist.destroy_process_group()

setup()
rank = dist.get_rank()
local_rank = int(os.environ["LOCAL_RANK"])

model = MyModel().cuda(local_rank)
model = DDP(model, device_ids=[local_rank])

sampler = DistributedSampler(dataset, num_replicas=dist.get_world_size(), rank=rank)
train_loader = DataLoader(dataset, batch_size=batch_size, sampler=sampler)

# Training loop
model.train()
for batch in train_loader:
    outputs = model(batch.cuda())
    loss = criterion(outputs, batch["labels"].cuda())
    loss.backward()
    optimizer.step()

cleanup()

# Key points:
# - Use torchrun for proper multi-GPU launching
# - DDP replicates model on each GPU
# - DistributedSampler handles data partitioning
# - All GPUs must see same initial weights
```
