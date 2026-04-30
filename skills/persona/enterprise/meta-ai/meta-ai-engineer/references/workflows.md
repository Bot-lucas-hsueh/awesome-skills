# Workflows & Code Examples

## Two-Tower Model Implementation

```python
# Two-tower model structure
class TwoTowerModel(nn.Module):
    def __init__(self):
        self.query_tower = QueryEncoder(...)  # User/context
        self.candidate_tower = ItemEncoder(...)  # Content

    def forward(self, query, candidate):
        q_emb = self.query_tower(query)
        c_emb = self.candidate_tower(candidate)
        return F.cosine_similarity(q_emb, c_emb)
```

## Fast Prototyping Workflow

```
Day 1-2: Minimal Working Version
  ├── Single-GPU PyTorch implementation
  ├── 1K-10K sample validation
  └── Metric tracking from start

Day 3-4: Quick Validation
  ├── Expand to realistic data slice
  ├── Compare to baseline
  └── Identify failure modes

Day 5: Stakeholder Demo
  ├── Live demo with real examples
  ├── Gather feedback
  └── Go/no-go for scaling investment
```

## LLaMA Fine-tuning Strategy

```
1. Start with LLaMA-3-8B + QLoRA (4-bit)
   - 16GB GPU sufficient
   - Validate data quality and format
   - 1-day turnaround for first model

2. Scale to 70B if quality insufficient
   - Use FSDP across 4-8 GPUs
   - LoRA for efficiency
   - 3-5 days for production model
```
