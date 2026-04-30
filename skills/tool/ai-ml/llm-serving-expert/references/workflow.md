# Standard Workflow

## 8.1 LLM Serving Pipeline

```
Phase 1: Model Preparation
├── Download/checkpoint model
├── Apply quantization if needed
├── Convert format (HF → TensorRT, GGUF)
└── Verify model integrity

Phase 2: Server Configuration
├── Determine hardware (GPU count, VRAM)
├── Choose serving framework
├── Configure batch sizes and limits
└── Set up tensor parallelism

Phase 3: Deployment
├── Start inference server
├── Verify endpoint availability
├── Test with sample requests
└── Configure autoscaling if needed

Phase 4: Production
├── Set up monitoring
├── Configure rate limiting
├── Enable caching if applicable
└── Set up logging and tracing
```

## 8.2 vLLM Production Deployment

```python
from vllm import LLM, SamplingParams
from vllm.engine.arg_utils import EngineArgs

# Engine configuration
engine_args = EngineArgs(
    model="meta-llama/Llama-2-7b-hf",
    tensor_parallel_size=2,
    gpu_memory_utilization=0.85,
    max_model_len=4096,
    dtype="half",
    enforce_eager=False,  # Enable CUDA graphs
    block_size=16,
    enable_prefix_caching=True,
)

# Create engine
llm = LLM.from_engine_args(engine_args)

# Sampling params
sampling_params = SamplingParams(
    temperature=0.7,
    top_p=0.9,
    top_k=50,
    max_tokens=512,
    stop=["<|endoftext|>"],
    logprobs=5,
)

# Batch inference
prompts = [
    "Once upon a time",
    "The meaning of life is",
    "In the future, AI will",
]

outputs = llm.generate(prompts, sampling_params)
```

## 8.3 TGI (Text Generation Inference) Deployment

```bash
# Using Docker
docker run --gpus all \
    --shm-size 1g \
    -e NUM_SHARD=2 \
    -e MAX_BATCH_PREFILL_TOKENS=4096 \
    -p 8080:80 \
    -v /data:/data \
    ghcr.io/huggingface/text-generation-inference:latest \
    --model-id meta-llama/Llama-2-7b-hf \
    --max-input-length 4096 \
    --max-total-tokens 8192

# Python client
from huggingface_hub import InferenceClient

client = InferenceClient(
    model="http://localhost:8080",
    timeout=120
)

output = client.text_generation(
    prompt="The future of AI is",
    max_new_tokens=100,
    temperature=0.7,
)
```

## 8.4 TensorRT-LLM Deployment

```python
# Build engine from HuggingFace model
# In a Python script or notebook
from tensorrt_llm.runtime import ModelConfig, SamplingConfig
from tensorrt_llm.logger import logger

# Configuration
model_config = ModelConfig(
    vocab_size=32000,
    num_layers=32,
    num_heads=32,
    hidden_size=4096,
    gpt_attention_plugin=True,
    tf_gemm_plugin=True,
)

# Generate with engine
def generate_engine(prompt, max_new_tokens=100):
    from tensorrt_llm.runtime import LLM

    llm = LLM(model_path="./llama_engine")
    outputs = llm.generate([prompt], max_new_tokens=max_new_tokens)
    return outputs[0]

# Serve via Triton
# triton_model_repo/
#   llama/
#     1/
#       model.py
#     config.pbtxt
```

## 8.5 Benchmarking Workflow

```python
import time
import statistics
from vllm import LLM, SamplingParams

llm = LLM(model="meta-llama/Llama-2-7b-hf")

# Test prompts
test_prompts = [f"Test prompt {i}" for i in range(100)]

sampling_params = SamplingParams(max_tokens=256)

# Throughput test
def benchmark_throughput(num_requests=100):
    start = time.time()
    outputs = llm.generate(test_prompts[:num_requests], sampling_params)
    elapsed = time.time() - start

    total_tokens = sum(len(o.outputs[0].token_ids) for o in outputs)
    throughput = num_requests / elapsed
    tokens_per_sec = total_tokens / elapsed

    return {
        "requests_per_sec": throughput,
        "tokens_per_sec": tokens_per_sec,
        "total_time": elapsed,
        "total_tokens": total_tokens,
    }

# Latency test
def benchmark_latency(num_requests=50):
    latencies = []
    for prompt in test_prompts[:num_requests]:
        start = time.time()
        llm.generate([prompt], sampling_params)
        latencies.append(time.time() - start)

    return {
        "mean": statistics.mean(latencies),
        "median": statistics.median(latencies),
        "p95": sorted(latencies)[int(len(latencies) * 0.95)],
        "p99": sorted(latencies)[int(len(latencies) * 0.99)],
    }
```

## 8.6 Autoscaling Configuration

```yaml
# kubernetes deployment.yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: llm-inference
spec:
  replicas: 2
  template:
    spec:
      containers:
      - name: vllm
        image: vllm/vllm-openai:latest
        resources:
          limits:
            nvidia.com/gpu: 2
            memory: "60Gi"
          requests:
            nvidia.com/gpu: 2
            memory: "50Gi"
        env:
        - name: VLLM_MODEL
          value: "meta-llama/Llama-2-7b-hf"
        - name: VLLM_TENSOR_PARALLEL_SIZE
          value: "2"
---
apiVersion: v1
kind: Service
metadata:
  name: llm-service
spec:
  type: LoadBalancer
  ports:
  - port: 80
    targetPort: 8000
  selector:
    app: llm-inference
```
