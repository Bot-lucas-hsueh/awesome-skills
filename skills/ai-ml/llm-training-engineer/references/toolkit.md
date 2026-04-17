## § 6 · Professional Toolkit

| Category | Tools | Notes |
|----------|-------|-------|
| **Training Frameworks** | PyTorch FSDP, Megatron-LM, DeepSpeed ZeRO | Megatron for 70B+; FSDP for 7B-30B |
| **Fine-tuning** | HuggingFace TRL, LLaMA-Factory, Axolotl | TRL for RLHF/DPO; LLaMA-Factory for SFT |
| **PEFT** | LoRA, QLoRA, adapters, IA3 | QLoRA for limited VRAM |
| **Data Curation** | DataTrove, Dolma toolkit, MinHash dedup | MinHash LSH for near-dedup at scale |
| **Evaluation** | lm-evaluation-harness, HELM, BIG-Bench | lm-eval-harness is the standard |
| **Inference Serving** | vLLM, TensorRT-LLM, SGLang, Ollama | vLLM for research; TensorRT-LLM for production |
| **Quantization** | bitsandbytes, GPTQ, AWQ, llama.cpp | AWQ for minimal quality loss |
| **Monitoring** | WandB, MLflow, TensorBoard, NVIDIA Nsight | WandB for run tracking; Nsight for GPU profiling |

---
