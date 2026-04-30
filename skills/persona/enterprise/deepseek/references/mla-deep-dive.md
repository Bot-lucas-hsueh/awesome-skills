# Multi-Head Latent Attention (MLA) Deep Dive

## Problem Statement

Standard Multi-Head Attention (MHA) requires storing Key and Value tensors for all previous tokens:

```
KV Cache Size = 2 x n_layers x n_heads x d_head x seq_len x batch_size x bytes_per_param
```

For a 128K context with standard configuration:
- Layers: 64
- Heads: 128
- Head dim: 128
- BF16: 2 bytes

Cache per layer: ~2GB
Total cache: ~128GB

## MLA Solution

Compress Key-Value representations into a latent vector:

```
Standard: Store full K, V tensors
MLA: Store compressed latent vector, reconstruct on-the-fly
```

## Architecture Details

### Step 1: Compression

```python
# Given hidden state h_t at position t
c_t = W_DKV @ h_t

# W_DKV shape: (d_c, d_model)
# d_c = compression dimension (e.g., 512)
# d_model = model dimension (e.g., 7168)
# Result: c_t shape (d_c,) - much smaller than K,V
```

### Step 2: Key/Value Reconstruction

```python
# Reconstruct key and value from latent
k_t = W_UK @ c_t  # Shape: (d_model,)
v_t = W_UV @ c_t  # Shape: (d_model,)

# W_UK, W_UV shape: (d_model, d_c)
```

### Step 3: Position Encoding

Standard RoPE (Rotary Position Embedding) cannot be applied after compression.

MLA solution: Decoupled RoPE

```python
# Separate path for position information
k_R = RoPE(W_KR @ h_t)

# W_KR shape: (d_h_R, d_model)
# k_R contains position information only
```

### Step 4: Combined Key

```python
# Concatenate content key and position key
k_t_final = concat([k_t, k_R])

# Now has both semantic content and position information
```

## Memory Comparison

| Configuration | Standard MHA | MLA | Savings |
|---------------|--------------|-----|---------|
| Cache per token | ~1MB | ~70KB | 93% |
| 128K context | ~128GB | ~9GB | 14x |
| 64K context | ~64GB | ~4.5GB | 14x |

## Implementation

```python
import torch
import torch.nn as nn
import math

class MLAAttention(nn.Module):
    def __init__(self, d_model, n_heads, d_c=512):
        super().__init__()
        self.d_model = d_model
        self.n_heads = n_heads
        self.d_head = d_model // n_heads
        self.d_c = d_c
        
        # Compression matrix
        self.W_DKV = nn.Linear(d_model, d_c, bias=False)
        
        # Up-projection matrices
        self.W_UK = nn.Linear(d_c, d_model, bias=False)
        self.W_UV = nn.Linear(d_c, d_model, bias=False)
        
        # Query transformation
        self.W_Q = nn.Linear(d_model, d_model, bias=False)
        
        # Decoupled RoPE
        self.W_KR = nn.Linear(d_model, d_c, bias=False)
        
        # Output projection
        self.W_O = nn.Linear(d_model, d_model, bias=False)
        
    def apply_rope(self, x, positions):
        # Simplified RoPE implementation
        d = x.shape[-1]
        freqs = torch.arange(0, d, 2, device=x.device)
        inv_freq = 1.0 / (10000 ** (freqs / d))
        angles = positions.unsqueeze(-1) * inv_freq
        cos = torch.cos(angles)
        sin = torch.sin(angles)
        
        x1, x2 = x[..., ::2], x[..., 1::2]
        rotated = torch.stack([-x2, x1], dim=-1).flatten(-2)
        return x * cos + rotated * sin
    
    def forward(self, x, past_cache=None):
        batch, seq_len, _ = x.shape
        
        # Compression - only store this
        c_t = self.W_DKV(x)  # (batch, seq, d_c)
        
        # Reconstruct K, V
        k_content = self.W_UK(c_t)  # (batch, seq, d_model)
        v = self.W_UV(c_t)  # (batch, seq, d_model)
        
        # Decoupled RoPE for position
        positions = torch.arange(seq_len, device=x.device)
        k_rot = self.apply_rope(self.W_KR(x), positions)
        
        # Combine content and position for keys
        # (In practice, reshape and concatenate appropriately)
        k = k_content  # Simplified - actual impl more complex
        
        # Query
        q = self.W_Q(x)
        
        # Multi-head reshape
        q = q.view(batch, seq_len, self.n_heads, self.d_head).transpose(1, 2)
        k = k.view(batch, seq_len, self.n_heads, self.d_head).transpose(1, 2)
        v = v.view(batch, seq_len, self.n_heads, self.d_head).transpose(1, 2)
        
        # Attention
        scores = torch.matmul(q, k.transpose(-2, -1)) / math.sqrt(self.d_head)
        attn = torch.softmax(scores, dim=-1)
        out = torch.matmul(attn, v)
        
        # Reshape and project
        out = out.transpose(1, 2).contiguous().view(batch, seq_len, self.d_model)
        return self.W_O(out), c_t  # Return cache = c_t only
```

## DeepSeek-V3 Configuration

| Parameter | Value |
|-----------|-------|
| d_model | 7168 |
| n_heads | 128 |
| d_head | 128 |
| d_c (compression) | 512 |
| Cache reduction | 14x (93%) |

## Benefits

1. **Memory:** 14x smaller KV cache
2. **Throughput:** More sequences per batch
3. **Long Context:** 128K+ feasible
4. **Cost:** Lower inference costs

## Trade-offs

1. **Compute:** Slight increase for reconstruction
2. **Complexity:** More implementation complexity
3. **Training:** Careful initialization needed

## Validation

DeepSeek-V3 proves MLA at 671B scale:
- 14.8T tokens trained
- Zero accuracy loss vs standard MHA
- 128K context support
- Production deployment
