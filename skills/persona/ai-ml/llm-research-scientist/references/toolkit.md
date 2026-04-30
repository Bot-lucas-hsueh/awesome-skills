## § 6 · Professional Toolkit

| Category / 类别 | Tools / 工具 | Notes
|----------------|------------|------------|
| **Training Frameworks** | PyTorch FSDP, Megatron-LM, DeepSpeed ZeRO | Megatron for 70B+; FSDP for 7B-30B |
| **Fine-tuning** | HuggingFace TRL, LLaMA-Factory, Axolotl | TRL for RLHF/DPO; LLaMA-Factory for SFT |
| **Parameter Efficient** | LoRA, QLoRA, Adapter, Prefix Tuning | QLoRA: 70B fine-tuning on 2×A100 |
| **Evaluation** | lm-evaluation-harness, HELM, BIG-Bench | lm-eval-harness is the standard |
| **Alignment** | TRL PPO/DPO, OpenRLHF, DeepSpeed-Chat | OpenRLHF for distributed PPO |
| **Data Curation** | DataTrove, Dolma toolkit, FineWeb recipes | MinHash dedup; quality classifiers |
| **Interpretability** | TransformerLens, Baukit, Activation Patching | TransformerLens for mechanistic interp |
| **Inference Optimization** | vLLM, TensorRT-LLM, SGLang | vLLM for research serving |

---
