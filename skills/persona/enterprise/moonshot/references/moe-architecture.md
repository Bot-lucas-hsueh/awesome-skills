# Mixture-of-Experts (MoE) Architecture Guide

> Deep dive into MoE architecture as implemented in Kimi K2.5.

## What is MoE?

Mixture-of-Experts is a neural network architecture where:
- **Total parameters**: 1 trillion (stored)
- **Active parameters**: 32 billion (computed per token)
- **Efficiency**: Only ~3.2% of parameters used per forward pass

```
┌─────────────────────────────────────────┐
│           Input Token                   │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│         Router Network                  │
│  (learns which experts to activate)     │
└──────────────┬──────────────────────────┘
               ↓
┌─────────────────────────────────────────┐
│    Select Top-k Experts (k=8)           │
│    ┌─────┐ ┌─────┐        ┌─────┐       │
│    │ E1  │ │ E23 │  ...   │ E384│       │
│    └──┬──┘ └──┬──┘        └──┬──┘       │
│       └───────┴──────────────┘          │
│           (8 selected from 384)         │
└──────────────────┬──────────────────────┘
                   ↓
┌─────────────────────────────────────────┐
│      Weighted Combination               │
│      (gate values × expert outputs)     │
└──────────────────┬──────────────────────┘
                   ↓
┌─────────────────────────────────────────┐
│            Output                       │
└─────────────────────────────────────────┘
```

## Kimi K2.5 MoE Specifications

```yaml
Total Parameters: 1,000,000,000,000 (1 trillion)
Active Parameters: 32,000,000,000 (32 billion)
Number of Experts: 384
Experts per Token: 8 (top-k)
Expert Capacity Factor: 1.0-1.25
Hidden Dimension: 7168
Attention Heads: Multi-head Latent Attention (MLA)
Layers: 61 (1 dense + 60 MoE)
```

## Router Design

### Noisy Top-K Gating

```python
def noisy_top_k_gating(x, k=8, noise_epsilon=1e-2):
    """Router with noise for exploration during training"""
    # Clean logits
    clean_logits = x @ router_weights
    
    # Add noise during training
    if training:
        noise = torch.randn_like(clean_logits) * noise_epsilon
        noisy_logits = clean_logits + noise
    else:
        noisy_logits = clean_logits
    
    # Top-k selection
    top_logits, top_indices = noisy_logits.topk(k, dim=-1)
    
    # Softmax over selected experts
    gates = F.softmax(top_logits, dim=-1)
    
    return gates, top_indices
```

### Load Balancing Loss

Prevents expert collapse (all tokens routed to same few experts):

```python
def load_balancing_loss(router_probs, expert_indices, num_experts):
    """Auxiliary loss for balanced expert utilization"""
    # Fraction of tokens routed to each expert
    router_prob_per_expert = torch.mean(router_probs, dim=0)
    
    # Average probability of selecting each expert
    aux_loss = num_experts * torch.sum(
        router_prob_per_expert * router_prob_per_expert
    )
    
    return aux_loss

# Total training loss
total_loss = model_loss + coeff * aux_loss + z_coeff * router_z_loss
```

### Router Z-Loss

Penalizes sharp router distributions (encourages exploration):

```python
def router_z_loss(router_logits):
    """Penalize extreme router logits"""
    return torch.sum(router_logits ** 2, dim=-1).mean()
```

## Expert Design

### Feed-Forward Expert

```python
class Expert(nn.Module):
    def __init__(self, d_model, d_ff):
        super().__init__()
        self.w1 = nn.Linear(d_model, d_ff)
        self.w2 = nn.Linear(d_ff, d_model)
        self.w3 = nn.Linear(d_model, d_ff)  # Gated linear unit
    
    def forward(self, x):
        # SwiGLU activation
        return self.w2(F.silu(self.w1(x)) * self.w3(x))
```

### Expert Parallelism

```python
# Distribute experts across GPUs
class ExpertParallelMoE(nn.Module):
    def __init__(self, num_experts, d_model, world_size):
        super().__init__()
        self.world_size = world_size
        experts_per_rank = num_experts // world_size
        
        # Each GPU holds subset of experts
        self.experts = nn.ModuleList([
            Expert(d_model, d_model * 4) 
            for _ in range(experts_per_rank)
        ])
    
    def forward(self, x, expert_indices):
        # All-to-all communication
        # Send tokens to GPUs hosting their assigned experts
        x = all_to_all(x, expert_indices)
        
        # Compute on local experts
        outputs = [expert(x) for expert in self.experts]
        
        # All-to-all communication back
        return all_to_all(outputs, reverse=True)
```

## Training Dynamics

### Expert Specialization

Over training, experts naturally specialize:

| Expert Group | Specialization | Emergence Point |
|--------------|----------------|-----------------|
| Syntax Experts | Grammar, punctuation | 10K steps |
| Semantic Experts | Meaning, entities | 50K steps |
| Code Experts | Programming languages | 100K steps |
| Math Experts | Numerical reasoning | 150K steps |

### Load Balance Monitoring

```python
def analyze_expert_utilization(model, dataloader):
    """Track expert usage across dataset"""
    expert_counts = torch.zeros(num_experts)
    
    for batch in dataloader:
        _, expert_indices = model.route(batch)
        for idx in expert_indices.flatten():
            expert_counts[idx] += 1
    
    # Calculate utilization entropy
    probs = expert_counts / expert_counts.sum()
    entropy = -torch.sum(probs * torch.log(probs + 1e-10))
    max_entropy = np.log(num_experts)
    
    return {
        "entropy": entropy.item(),
        "normalized_entropy": entropy.item() / max_entropy,
        "min_usage": expert_counts.min().item(),
        "max_usage": expert_counts.max().item(),
    }

# Target: normalized_entropy > 0.9
```

## Inference Optimization

### Expert Caching

```python
class ExpertCache:
    """Cache frequently used expert weights"""
    def __init__(self, max_cached_experts=64):
        self.cache = {}
        self.access_count = defaultdict(int)
        self.max_cached = max_cached_experts
    
    def get_expert(self, expert_id):
        if expert_id in self.cache:
            self.access_count[expert_id] += 1
            return self.cache[expert_id]
        
        # Load from disk
        expert = load_expert(expert_id)
        
        # Evict least used if cache full
        if len(self.cache) >= self.max_cached:
            lru_id = min(self.cache, key=lambda k: self.access_count[k])
            del self.cache[lru_id]
            del self.access_count[lru_id]
        
        self.cache[expert_id] = expert
        return expert
```

### Batched Expert Execution

```python
def batch_expert_execution(tokens, expert_assignments, experts):
    """Group tokens by expert for efficient batching"""
    expert_batches = defaultdict(list)
    token_indices = defaultdict(list)
    
    # Group tokens by their assigned expert
    for i, (token, expert_id) in enumerate(zip(tokens, expert_assignments)):
        expert_batches[expert_id].append(token)
        token_indices[expert_id].append(i)
    
    # Process each expert's batch
    outputs = torch.zeros_like(tokens)
    for expert_id, batch in expert_batches.items():
        batch_tensor = torch.stack(batch)
        expert_output = experts[expert_id](batch_tensor)
        
        # Scatter back to original positions
        for idx, output in zip(token_indices[expert_id], expert_output):
            outputs[idx] = output
    
    return outputs
```

## Comparison: MoE vs Dense

| Aspect | MoE (1T/32B) | Dense (32B) |
|--------|--------------|-------------|
| Parameters | 1 trillion | 32 billion |
| Active per token | 32 billion | 32 billion |
| Memory (inference) | ~200GB | ~64GB |
| Throughput | Similar | Similar |
| Quality | Higher | Lower |
| Training Cost | Higher | Lower |
| Expert Specialization | Yes | No |

## Common Issues & Fixes

### Issue 1: Expert Collapse

**Symptom**: 80% of tokens routed to 3 of 64 experts

**Fixes**:
1. Increase load balancing loss coefficient
2. Add router z-loss
3. Increase noise epsilon during training
4. Use expert dropout

### Issue 2: Load Imbalance Across GPUs

**Symptom**: Some GPUs overloaded, others idle

**Fixes**:
1. Dynamic expert capacity factor
2. Token dropping for overloaded experts
3. Better expert placement strategy

### Issue 3: Communication Overhead

**Symptom**: All-to-all communication dominates runtime

**Fixes**:
1. Overlap communication with computation
2. Use faster interconnect (InfiniBand, NVLink)
3. Increase batch size to amortize cost

## MoE in Kimi K2.5

### Unique Features

1. **Dense + MoE Hybrid**: First layer is dense for stability
2. **MLA Integration**: MoE combined with memory-efficient attention
3. **Native INT4**: Experts quantized with QAT for 2x speed
4. **Agent Swarm Training**: Expert specialization for agent tasks

### Performance

| Metric | Value |
|--------|-------|
| Expert Utilization Entropy | 4.1/4.16 (98% uniform) |
| Load Balance Ratio | 1.3 (target <1.5) |
| Router Latency | <5% of total |
| Memory Savings | 75% vs dense 1T model |

---

*Architecture guide for Kimi K2.5's MoE implementation | Updated: 2026-03-21*
