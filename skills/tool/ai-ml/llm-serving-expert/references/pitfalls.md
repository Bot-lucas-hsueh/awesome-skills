# Common Pitfalls & Anti-Patterns

## 10.1 Anti-Patterns

| # | Anti-Pattern | Severity | Quick Fix |
|---|-------------|----------|-----------|
| 1 | OOM during batch inference | 🔴 High | Reduce batch size, enable prefix caching |
| 2 | Using FP32 for large models | 🟡 Medium | Use FP16/BF16 for memory savings |
| 3 | Ignoring CUDA graph overhead | 🟡 Medium | Use `--enforce-eager=False` |
| 4 | Not setting max_model_len | 🔴 High | Set based on model and hardware |
| 5 | Single GPU for 70B+ models | 🔴 High | Use tensor parallelism |
| 6 | High latency without streaming | 🟡 Medium | Enable streaming for perceived latency |
| 7 | Ignoring KV cache tuning | 🟡 Medium | Adjust block_size and gpu_memory_utilization |
| 8 | No pre-warming | 🟡 Medium | Send warmup prompts before production |
| 9 | Inefficient prompt batching | 🟡 Medium | Group similar-length prompts |
| 10 | Missing health checks | 🟡 Medium | Add /health endpoint monitoring |

## 10.2 CUDA Out of Memory Solutions

```python
# Problem: CUDA OOM during large batch
# Solution 1: Reduce memory usage
llm = LLM(
    model="meta-llama/Llama-2-70b-hf",
    tensor_parallel_size=4,
    gpu_memory_utilization=0.7,  # Reduce from 0.9
    max_model_len=2048,          # Limit sequence length
)

# Solution 2: Use quantization
llm = LLM(
    model="meta-llama/Llama-2-70b-hf",
    tokenizer="meta-llama/Llama-2-70b-hf",
    enforce_eager=False,
)

# Solution 3: Chunk long sequences
MAX_SEQ_LEN = 2048
long_prompt = "..."  # 4000 tokens

# Split into chunks, generate separately, concatenate
```

## 10.3 Performance Optimization Checklist

```python
# 1. Enable CUDA graphs (default, unless debugging)
llm = LLM(model="...", enforce_eager=False)

# 2. Enable prefix caching (if using repeated prefixes)
llm = LLM(model="...", enable_prefix_caching=True)

# 3. Tune batch parameters
llm = LLM(
    model="...",
    max_num_batched_tokens=8192,  # Increase for throughput
    max_num_seqs=256,             # Increase for parallelism
)

# 4. Use appropriate dtype
llm = LLM(model="...", dtype="half")       # FP16
llm = LLM(model="...", dtype="bfloat16")   # BF16 (better range)
llm = LLM(model="...", dtype="float")      # FP32 (if needed)

# 5. Pre-warm model
_ = llm.generate(["warmup"], SamplingParams(max_tokens=1))
```

## 10.4 Latency vs Throughput Tradeoffs

| Goal | Configuration |
|------|---------------|
| Max throughput | Larger batches, more prefill |
| Low latency | Smaller batches, streaming |
| Long outputs | Higher max_tokens, KV cache |
| Short outputs | Faster TTFT, streaming |

```python
# For latency-sensitive applications
sampling_params = SamplingParams(
    temperature=0.0,
    max_tokens=100,       # Limit output length
    use_beam_search=False, # Greedy for speed
)

# For throughput-sensitive applications
sampling_params = SamplingParams(
    temperature=0.8,
    max_tokens=512,
    use_beam_search=True,  # Beam search (better quality)
)

# For mixed workloads, use streaming
sampling_params = SamplingParams(
    stream=True,  # Start returning immediately
    max_tokens=512,
)
```

## 10.5 Monitoring & Observability

```python
# Add metrics to vLLM server
# Start with prometheus endpoint
vllm serve model --port 8000 --metrics-port 8001

# Prometheus metrics available:
# - vllm:num_tokens_total
# - vllm:num_preemptions_total
# - vllm:gpu_cache_usage
# - vllm:time_to_first_token_seconds
# - vllm:time_per_output_token_seconds

# Custom monitoring wrapper
import time
from prometheus_client import Counter, Histogram

REQUEST_LATENCY = Histogram('llm_request_latency', 'Request latency')
TOKEN_LATENCY = Histogram('llm_token_latency', 'Token generation latency')

@REQUEST_LATENCY.time()
def generate_with_metrics(prompt, params):
    start = time.time()
    output = llm.generate([prompt], params)[0]
    elapsed = time.time() - start

    num_tokens = len(output.outputs[0].token_ids)
    TOKEN_LATENCY.observe(num_tokens / elapsed)

    return output
```

## 10.6 Security Considerations

```bash
# Never expose inference server publicly without auth

# Option 1: API key authentication
vllm serve model --port 8000 --api-key "your-secret-key"

# Option 2: Behind authenticated proxy
# nginx with JWT validation

# Rate limiting
curl -X POST http://localhost:8000/v1/completions \
    -H "X-RateLimit-Limit: 100" \
    -H "X-RateLimit-Remaining: 99"

# Content filtering (outside scope of inference server)
# Implement in your application layer
```
