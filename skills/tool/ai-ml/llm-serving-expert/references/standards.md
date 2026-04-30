# Standards & Reference

## 7.1 Official Documentation

- [vLLM Documentation](https://docs.vllm.ai/)
- [vLLM GitHub](https://github.com/vllm-project/vllm)
- [Triton Inference Server](https://docs.nvidia.com/deeplearning/triton-inference-server/)
- [TensorRT-LLM](https://nvidia.github.io/TensorRT-LLM/)
- [HuggingFace TGI](https://huggingface.co/docs/text-generation-inference/)
- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [Ray Serve](https://docs.ray.io/en/latest/serve/index.html)

## 7.2 vLLM Installation

```bash
# From PyPI
pip install vllm

# From source (for latest features)
git clone https://github.com/vllm-project/vllm.git
cd vllm
pip install -e .

# With CUDA support
pip install vllm --extra-index-url https://wheels.vllm.ai/nightly
```

## 7.3 vLLM API Reference

### Offline Inference

```python
from vllm import LLM, SamplingParams

llm = LLM(model="meta-llama/Llama-2-7b-hf")

sampling_params = SamplingParams(
    temperature=0.8,
    top_p=0.95,
    max_tokens=256,
    stop=["<|endoftext|>", "User:"]
)

outputs = llm.generate(["Hello, my name is", "The capital of France is"], sampling_params)

for output in outputs:
    print(f"Prompt: {output.prompt}")
    print(f"Generated: {output.outputs[0].text}")
```

### OpenAI-Compatible Server

```bash
# Start server
vllm serve meta-llama/Llama-2-7b-hf \
    --dtype half \
    --port 8000 \
    --tensor-parallel-size 2

# Query with OpenAI client
curl http://localhost:8000/v1/completions \
    -H "Content-Type: application/json" \
    -d '{
        "model": "meta-llama/Llama-2-7b-hf",
        "prompt": "The future of AI is",
        "max_tokens": 100
    }'
```

## 7.4 TensorRT-LLM Reference

```bash
# Install TensorRT-LLM
pip install tensorrtllm_backend

# Build engine
python /opt/tensorrt_llm/examples/llama/build.py \
    --model_dir=meta-llama/Llama-2-7b-hf \
    --dtype=float16 \
    --tp_size=1 \
    --output_dir=./llama_engine

# Run inference
trtllm-run ./llama_engine/engine_caption.bin \
    --tokenizer=meta-llama/Llama-2-7b-hf \
    --max_output_len=100
```

## 7.5 Quantization Formats

| Format | Bits | Use Case | Tool |
|--------|------|----------|------|
| FP16 | 16 | Baseline | vLLM, TGI |
| INT8 | 8 | Speed | bitsandbytes, GPTQ |
| INT4 | 4 | Memory | AWQ, GGUF Q4 |
| FP8 | 8 | Hopper only | TensorRT-LLM |
| GPTQ | 4/8 | Post-training | AutoGPTQ |
| AWQ | 4 | Activation-aware | AWQ |

## 7.6 Deployment Configurations

### Single GPU

```bash
vllm serve meta-llama/Llama-2-13b-hf \
    --dtype half \
    --gpu-memory-utilization 0.9
```

### Multi-GPU (Tensor Parallelism)

```bash
vllm serve meta-llama/Llama-2-70b-hf \
    --tensor-parallel-size 4 \
    --dtype half
```

### Multi-Node

```bash
# On node 0
vllm serve meta-llama/Llama-2-70b-hf \
    --tensor-parallel-size 8 \
    --pipeline-parallel-size 2 \
    --headless \
    --port 8000

# Connect worker nodes
torchrun --nnodes=2 --node_rank=0 --master_addr=$HEAD_NODE_IP \
    vllm/entrypoints/openai/api_server.py \
    --model meta-llama/Llama-2-70b-hf
```

## 7.7 vLLM Parameters

| Parameter | Default | Description |
|-----------|---------|-------------|
| `--max-model-len` | auto | Maximum sequence length |
| `--gpu-memory-utilization` | 0.9 | GPU memory fraction |
| `--tensor-parallel-size` | 1 | Number of GPUs for TP |
| `--dtype` | auto | Model dtype (float16, bfloat16) |
| `--max-num-batched-tokens` | dynamic | Max tokens per iteration |
| `--max-num-seqs` | dynamic | Max sequences per iteration |
| `--enforce-eager` | False | Disable CUDA graph |
