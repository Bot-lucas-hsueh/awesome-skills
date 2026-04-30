# FP8 Mixed Precision Training Guide

## Overview

DeepSeek-V3 was the first 671B parameter model trained with FP8 mixed precision, achieving:
- 1.2x speedup vs BF16
- 38% memory reduction
- Zero accuracy loss
- Perfect training stability

## FP8 Number Formats

### E4M3 (Forward Pass)
- 4-bit exponent
- 3-bit mantissa
- 1 sign bit
- Range: ~0.00195 to 448
- Best for: Activations (need precision)

### E5M2 (Backward Pass)  
- 5-bit exponent
- 2-bit mantissa
- 1 sign bit
- Range: ~0.000015 to 57344
- Best for: Gradients (need range)

## Training Strategy

```
Master Weights:     BF16 (high precision)
Optimizer States:   BF16 (stability)
Forward Activations: FP8-E4M3
Backward Gradients:  FP8-E5M2
All-Reduce:         BF16 (accumulation)
```

## Implementation

```python
import torch
import torch.nn as nn

class FP8Linear(nn.Module):
    def __init__(self, in_features, out_features):
        super().__init__()
        
        # Master weights in BF16 (high precision for updates)
        self.weight_master = nn.Parameter(
            torch.empty(out_features, in_features, dtype=torch.bfloat16)
        )
        self.bias = nn.Parameter(torch.zeros(out_features))
        
        # Scaling factor for FP8
        self.register_buffer("weight_scale", torch.tensor(1.0))
        self.register_buffer("input_scale", torch.tensor(1.0))
        
        # Initialize
        nn.init.kaiming_uniform_(self.weight_master)
    
    def cast_to_fp8(self, tensor, fmt="E4M3"):
        """Cast tensor to FP8 format"""
        if fmt == "E4M3":
            # E4M3: max value 448
            max_val = 448.0
        else:  # E5M2
            # E5M2: max value 57344
            max_val = 57344.0
        
        # Calculate scale to maximize FP8 range usage
        abs_max = tensor.abs().max()
        scale = max_val / (abs_max + 1e-12)
        
        # Scale, round, clamp
        scaled = tensor * scale
        fp8_val = torch.clamp(scaled, -max_val, max_val)
        
        return fp8_val, scale
    
    def forward(self, x):
        batch_size = x.shape[0]
        
        # Cast input to FP8-E4M3
        x_fp8, input_scale = self.cast_to_fp8(x, "E4M3")
        
        # Cast weight to FP8-E4M3
        w_fp8, weight_scale = self.cast_to_fp8(self.weight_master, "E4M3")
        
        # FP8 matmul (simulated - actual uses hardware FP8 units)
        # In practice: torch._scaled_mm on H100/H800
        output = torch.matmul(x_fp8, w_fp8.t())
        
        # Rescale output
        output = output / (input_scale * weight_scale)
        
        return output + self.bias

class FP8Optimizer:
    """Optimizer that maintains BF16 master weights"""
    
    def __init__(self, params, lr=1e-4):
        self.params = list(params)
        self.lr = lr
        
        # Master weights already in BF16
        # Optimizer states in BF16
        self.states = {}
        for p in self.params:
            self.states[p] = {
                "exp_avg": torch.zeros_like(p.data),
                "exp_avg_sq": torch.zeros_like(p.data),
            }
    
    def step(self, gradients):
        """Update using FP8 gradients, apply to BF16 master"""
        for p, g in zip(self.params, gradients):
            if g is None:
                continue
            
            # Gradient in FP8-E5M2 comes from backward
            # Dequantized to BF16 for optimizer
            state = self.states[p]
            
            # Adam update in BF16 (stable)
            state["exp_avg"] = 0.9 * state["exp_avg"] + 0.1 * g
            state["exp_avg_sq"] = 0.999 * state["exp_avg_sq"] + 0.001 * g * g
            
            update = state["exp_avg"] / (state["exp_avg_sq"].sqrt() + 1e-8)
            p.data -= self.lr * update
```

## Loss Scaling

```python
class DynamicLossScaler:
    def __init__(self, init_scale=2**16, growth_factor=2):
        self.scale = init_scale
        self.growth_factor = growth_factor
        self.good_steps = 0
        
    def scale_loss(self, loss):
        """Scale loss before backward"""
        return loss * self.scale
    
    def update(self, gradients):
        """Update scale based on gradient status"""
        # Check for inf/nan in gradients
        has_inf = any(torch.isinf(g).any() for g in gradients if g is not None)
        has_nan = any(torch.isnan(g).any() for g in gradients if g is not None)
        
        if has_inf or has_nan:
            # Overflow - reduce scale
            self.scale /= self.growth_factor
            self.good_steps = 0
            return False  # Skip step
        else:
            # Good step
            self.good_steps += 1
            if self.good_steps > 100:
                # Try increasing scale
                self.scale *= self.growth_factor
                self.good_steps = 0
            return True  # Proceed with step
```

## Training Loop

```python
def train_step_fp8(model, batch, optimizer, loss_scaler):
    x, y = batch
    
    # Forward pass (FP8)
    with torch.cuda.amp.autocast(dtype=torch.float8_e4m3fn):
        logits = model(x)
        loss = F.cross_entropy(logits, y)
    
    # Scale loss
    scaled_loss = loss_scaler.scale_loss(loss)
    
    # Backward pass (produces FP8-E5M2 gradients)
    scaled_loss.backward()
    
    # Unscale gradients
    for p in model.parameters():
        if p.grad is not None:
            p.grad /= loss_scaler.scale
    
    # Update scaler and check for overflow
    should_update = loss_scaler.update([p.grad for p in model.parameters()])
    
    if should_update:
        optimizer.step()
    
    optimizer.zero_grad()
    return loss
```

## Hardware Requirements

| Feature | Requirement |
|---------|-------------|
| FP8 Tensor Cores | NVIDIA H100/H800 or newer |
| Framework | PyTorch 2.0+ with FP8 support |
| Transformer Engine | NVIDIA optimized kernels |

## DeepSeek-V3 Results

| Metric | BF16 | FP8 | Change |
|--------|------|-----|--------|
| Memory | 100% | 62% | -38% |
| Speed | 1.0x | 1.2x | +20% |
| MMLU | 88.5% | 88.4% | -0.1% |
| Stability | Multiple rollbacks | Zero rollbacks | Better |

## Best Practices

1. **Always use BF16 master weights** - Essential for stability
2. **Dynamic loss scaling** - Handle FP8 range limitations
3. **E4M3 for forward, E5M2 for backward** - Optimal precision/range tradeoff
4. **Validate at scale** - FP8 behavior changes with model size
5. **Monitor for overflow** - More critical than with BF16

## Validation Checklist

- [ ] Small-scale (1B) validation passes
- [ ] Medium-scale (7B) validation passes  
- [ ] Large-scale (70B+) validation passes
- [ ] No accuracy degradation on key benchmarks
- [ ] Training stability (no loss spikes)
- [ ] Inference compatibility maintained
