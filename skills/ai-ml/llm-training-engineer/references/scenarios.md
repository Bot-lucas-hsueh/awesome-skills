## § 9 · Scenario Examples

### Scenario: Fine-tuning Strategy Selection

**User:** "I have a 70B base model and limited compute (4× A100). Should I use full fine-tuning or LoRA?"

**LLM Training Engineer:**

> **Fine-tuning Strategy: 70B on 4×A100 (320GB VRAM)**
>
> **Full fine-tuning memory requirement:**
> - Model weights: 70B × 2 bytes (bf16) = 140GB
> - Gradients: 140GB
> - Optimizer state (Adam): 140GB × 2 = 280GB
> - Total: **~560GB** — impossible on 4×A100 (320GB total)
>
> **Recommendation: QLoRA**
>
> ```python
> from transformers import BitsAndBytesConfig
> from peft import LoraConfig, get_peft_model
>
> bnb_config = BitsAndBytesConfig(
>     load_in_4bit=True,
>     bnb_4bit_compute_dtype=torch.bfloat16,
>     bnb_4bit_use_double_quant=True,
>     bnb_4bit_quant_type="nf4"
> )
>
> lora_config = LoraConfig(
>     r=64,
>     lora_alpha=128,
>     target_modules=["q_proj", "k_proj", "v_proj", "o_proj",
>                     "gate_proj", "up_proj", "down_proj"],
>     lora_dropout=0.05,
>     bias="none"
> )
> ```
>
> **Quality note:** QLoRA r=64 achieves 95-98% of full fine-tuning quality (Dettmers et al., 2023).

---

### Scenario: Inference Optimization

**User:** "Our 7B model at P95 latency is 2.5s per request. We need < 500ms. How?"

**LLM Training Engineer:**

> **Step 1: Profile the bottleneck**
> ```bash
> python -m vllm.entrypoints.openai.api_server \
>     --model ./your-7b-model \
>     --dtype bfloat16 \
>     --tensor-parallel-size 2
> ```
>
> **Step 2: Optimizations by impact**
>
> | Optimization | Latency Gain | Implementation |
> |--------------|-------------|----------------|
> | vLLM (continuous batching) | 3-5× | Drop-in replacement |
> | AWQ 4-bit quantization | 1.5-2× | Benchmark before switch |
> | Tensor parallelism | 1.8× | --tensor-parallel-size 2 |
> | Speculative decoding | 2-3× | Requires draft model |
>
> **Result:** vLLM + AWQ + 2 GPUs = 200-400ms P95 typically

---
