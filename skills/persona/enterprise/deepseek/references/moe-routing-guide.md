# DeepSeekMoE Routing Guide

## Overview

DeepSeekMoE uses a Mixture-of-Experts architecture with:
- 256 routed experts + 1 shared expert
- Top-8 expert selection per token
- 671B total parameters, 37B active (5.5%)

## Architecture

```
Input Token
    |
    v
[Shared Expert] -----> Always active
    |                      |
    v                      |
[Router Network] --------|
    |
    v
[Select Top-8 from 256 Routed Experts]
    |
    v
[Combine outputs weighted by routing scores]
    |
    v
Output
```

## Routing Mechanism

### Standard Approach (with auxiliary loss)

```python
# Gating network
gates = softmax(router(x))  # Shape: (256,)

# Select top-k
top_gates, top_indices = torch.topk(gates, k=8)

# Normalize selected gates
top_gates = top_gates / top_gates.sum()

# Compute output
output = sum(gate * experts[idx](x) for gate, idx in zip(top_gates, top_indices))

# Auxiliary loss (load balancing)
aux_loss = coefficient * sum(fraction_i * mean_gates_i)
# This degrades model performance!
```

### DeepSeek Solution (aux-loss-free)

```python
class AuxLossFreeRouter(nn.Module):
    def __init__(self, d_model, n_experts=256):
        super().__init__()
        self.router = nn.Linear(d_model, n_experts)
        # Learnable bias for load balancing
        self.load_balance_bias = nn.Parameter(torch.zeros(n_experts))
        
    def forward(self, x):
        # Raw routing scores
        raw_scores = self.router(x)
        
        # Add load-balancing bias
        balanced_scores = raw_scores + self.load_balance_bias
        
        # Softmax to get probabilities
        gates = torch.softmax(balanced_scores, dim=-1)
        
        # Select top-k
        top_gates, top_indices = torch.topk(gates, k=8)
        
        # Normalize
        top_gates = top_gates / top_gates.sum(dim=-1, keepdim=True)
        
        return top_gates, top_indices
    
    def update_bias(self, expert_loads):
        # Called after each iteration
        # Increase bias for underloaded experts
        # Decrease bias for overloaded experts
        target_load = 1.0 / len(expert_loads)
        for i, load in enumerate(expert_loads):
            if load < target_load * 0.9:
                self.load_balance_bias[i] += 0.01
            elif load > target_load * 1.1:
                self.load_balance_bias[i] -= 0.01
```

## Expert Configuration

```python
class DeepSeekMoE(nn.Module):
    def __init__(self, d_model, n_routed=256, n_shared=1, top_k=8):
        super().__init__()
        
        # Shared experts (always active)
        self.shared_experts = nn.ModuleList([
            nn.Sequential(
                nn.Linear(d_model, 4 * d_model),
                nn.GELU(),
                nn.Linear(4 * d_model, d_model)
            ) for _ in range(n_shared)
        ])
        
        # Routed experts (selective activation)
        self.routed_experts = nn.ModuleList([
            nn.Sequential(
                nn.Linear(d_model, d_model // n_routed * 4),
                nn.GELU(),
                nn.Linear(d_model // n_routed * 4, d_model)
            ) for _ in range(n_routed)
        ])
        
        # Router network
        self.router = AuxLossFreeRouter(d_model, n_routed)
        self.top_k = top_k
        
    def forward(self, x):
        # Shared expert output (always computed)
        shared_out = sum(expert(x) for expert in self.shared_experts)
        
        # Get routing decisions
        top_gates, top_indices = self.router(x)
        
        # Compute routed expert outputs
        batch_size, seq_len, d_model = x.shape
        routed_out = torch.zeros_like(x)
        
        # Efficient implementation would use grouped GEMM
        for b in range(batch_size):
            for s in range(seq_len):
                for i in range(self.top_k):
                    expert_idx = top_indices[b, s, i]
                    gate_value = top_gates[b, s, i]
                    expert_out = self.routed_experts[expert_idx](x[b, s])
                    routed_out[b, s] += gate_value * expert_out
        
        return shared_out + routed_out
```

## Device-Limited Routing

For distributed training, limit experts to M devices:

```python
def device_limited_routing(gates, expert_to_device, M=4):
    # Only select experts from at most M devices
    # Reduces all-to-all communication overhead
    
    device_scores = {}
    for expert_idx, score in enumerate(gates):
        device = expert_to_device[expert_idx]
        device_scores[device] = device_scores.get(device, 0) + score
    
    # Select top devices
    top_devices = sorted(device_scores.items(), key=lambda x: -x[1])[:M]
    allowed_experts = [e for e, d in expert_to_device.items() 
                       if d in [d for d, _ in top_devices]]
    
    # Mask and re-normalize
    masked_gates = gates.clone()
    masked_gates[[e for e in range(len(gates)) if e not in allowed_experts]] = 0
    masked_gates = masked_gates / masked_gates.sum()
    
    return masked_gates
```

## Load Balancing Metrics

| Metric | Target | DeepSeek-V3 |
|--------|--------|-------------|
| Expert utilization | Uniform | Within 10% of mean |
| Load balance loss | 0 (aux-free) | 0 |
| Communication overhead | Minimal | Device-limited helps |

## Efficiency Results

| Configuration | Total Params | Active Params | Training Cost |
|--------------|--------------|---------------|---------------|
| Dense 70B | 70B | 70B (100%) | ~$50M+ |
| DeepSeekMoE | 671B | 37B (5.5%) | $5.576M |
| Savings | 9.6x more | 1.9x fewer | 9x cheaper |

## Key Insights

1. **Shared experts** capture common patterns
2. **Routed experts** specialize by token type
3. **Bias-based balancing** eliminates auxiliary loss
4. **Device-limited routing** enables efficient distribution
