# FSDP for Large Models

FullyShardedDataParallel for training models too large to fit on a single GPU.

```python
from torch.distributed.fsdp import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp import ShardingStrategy, MixedPrecision
from torch.distributed.fsdp.wrap import transformer_auto_wrap_policy

# Mixed precision for FSDP
bf16 = torch.bfloat16
mixed_precision = MixedPrecision(param_dtype=bf16, reduce_dtype=bf16, buffer_dtype=bf16)

model = MyLargeModel()
fsdp_model = FSDP(
    model,
    sharding_strategy=ShardingStrategy.FULL_SHARD,
    mixed_precision=mixed_precision,
    auto_wrap_policy=transformer_auto_wrap_policy,
    device_id=torch.cuda.current_device(),
)

# Training
for batch in dataloader:
    with FSDP.autocast():
        outputs = fsdp_model(batch)
        loss = criterion(outputs, labels)

    fsdp_model.backward(loss)
    fsdp_model.step()

# Key points:
# - FSDP shards model across GPUs (vs DDP which replicates)
# - Mixed precision with bf16 saves memory
# - transformer_auto_wrap_policy wraps Transformer layers
# - Enables training 2-4x larger models
```
