## 7. Standards & Reference

### Parallelism Strategy Reference

| Scenario / 场景 | Strategy / 策略 | Notes
|----------------|----------------|------------|
| Model fits 1 GPU | Single GPU + DDP for data parallel | Baseline; use gradient checkpointing for memory |
| Model fits 1 node | FSDP ZeRO-2 or ZeRO-3 | ZeRO-3 for largest models; overlap comm=True |
| 70B on 512 GPUs | TP=8, PP=8, DP=8 (Megatron 3D) | 3D parallelism for maximum throughput |
| Memory-constrained | DeepSpeed ZeRO-3 + CPU offload | Last resort; kills throughput by 50% |

### Architecture Component Reference

| Component | Options | 2025+ Best Practice |
|-----------|---------|---------------------|
| Attention | MHA / MQA / GQA
| Positional Encoding | Absolute / RoPE
| Normalization | Pre-LN
| Activation | ReLU / GeLU / SwiGLU | SwiGLU (FFN: 8/3 × d_model) |
| Precision | fp32 / bf16

### Domain Data Mix Reference

| Domain | % Tokens | Rationale |
|--------|----------|-----------|
| Web (filtered) | 50-60% | General knowledge, language diversity |
| Code | 15-25% | Reasoning, structured thinking, tool use |
| Books
| Scientific papers | 5-10% | Factual grounding, reasoning |
| Wikipedia | 3-5% | High-quality factual anchor |
| Dialogue

