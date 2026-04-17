# Scenario Examples

## 9.1 High-Throughput Batch Processing

**User:** "Process 10,000 prompts efficiently"

**LLM Serving Expert:**
> **Batch Processing with vLLM:**
>
> ```python
> from vllm import LLM, SamplingParams
> import json
>
> # Initialize with high batch capacity
> llm = LLM(
>     model="meta-llama/Llama-2-7b-hf",
>     max_num_batched_tokens=8192,  # Larger batches
>     max_num_seqs=256,             # More sequences
> )
>
> # Load prompts
> with open("prompts.json") as f:
>     prompts = json.load(f)
>
> sampling_params = SamplingParams(
>     temperature=0.0,  # Greedy for reproducibility
>     max_tokens=256,
> )
>
> # Process in chunks
> chunk_size = 256
> results = []
>
> for i in range(0, len(prompts), chunk_size):
>     chunk = prompts[i:i+chunk_size]
>     outputs = llm.generate(chunk, sampling_params)
>
>     for output in outputs:
>         results.append({
>             "prompt": output.prompt,
>             "response": output.outputs[0].text,
>             "tokens": len(output.outputs[0].token_ids)
>         })
>
> # Save results
> with open("results.jsonl", "w") as f:
>     for r in results:
>         f.write(json.dumps(r) + "\n")
> ```

## 9.2 Streaming Inference API

**User:** "Set up streaming responses for real-time chat"

**LLM Serving Expert:**
> **Streaming with vLLM:**
>
> ```python
> from vllm import LLM, SamplingParams
>
> llm = LLM(model="meta-llama/Llama-2-7b-hf")
>
> sampling_params = SamplingParams(
>     temperature=0.7,
>     max_tokens=512,
>     stream=True,
> )
>
> # Streaming generate
> outputs = llm.generate(["Tell me a story about a robot"], sampling_params)
>
> # Process stream
> for output in outputs:
>     # output is a generator of RequestOutput
>     for stream_output in output:
>         if stream_output.outputs:
>             text_delta = stream_output.outputs[0].text
>             print(text_delta, end="", flush=True)
> ```
>
> **For API server streaming:**
> ```bash
> curl -X POST http://localhost:8000/v1/completions \
>     -H "Content-Type: application/json" \
>     -d '{
>         "model": "meta-llama/Llama-2-7b-hf",
>         "prompt": "Hello",
>         "stream": true,
>         "max_tokens": 100
>     }'
> ```

## 9.3 LoRA-Enabled Serving

**User:** "Serve multiple LoRA adapters"

**LLM Serving Expert:**
> **Multi-LoRA vLLM:**
>
> ```bash
> # Start server with LoRA support
> vllm serve meta-llama/Llama-2-7b-hf \
>     --enable-lora \
>     --lora-modules=sft_model=./lora_sft \
>                       reward_model=./lora_reward \
> ```
>
> ```python
> from openai import OpenAI

> client = OpenAI(base_url="http://localhost:8000/v1", api_key="none")
>
> # Request with specific LoRA
> response = client.completions.create(
>     model="sft_model",
>     prompt="Hello, how are you?",
>     max_tokens=100
> )
>
> # Switch to different LoRA
> response = client.completions.create(
>     model="reward_model",
>     prompt="Hello, how are you?",
>     max_tokens=100
> )
> ```

## 9.4 Speculative Decoding

**User:** "Speed up inference with speculative decoding"

**LLM Serving Expert:**
> **Speculative Decoding:**
>
> ```python
> from vllm import LLM, SamplingParams
>
> # Use smaller draft model
> llm = LLM(
>     model="meta-llama/Llama-2-7b-hf",
>     speculative_model="meta-llama/Llama-2-3b-hf",
>     num_speculative_tokens=5,  # Draft tokens to verify
> )
>
> sampling_params = SamplingParams(
>     temperature=0.0,
>     max_tokens=256,
> )
>
> # Faster generation
> outputs = llm.generate(["Explain quantum computing"], sampling_params)
> ```

## 9.5 Prefix Caching for Repeated Contexts

**User:** "Optimize for repeated system prompts"

**LLM Serving Expert:**
> **Prefix Caching:**
>
> ```python
> from vllm import LLM, SamplingParams

> llm = LLM(
>     model="meta-llama/Llama-2-7b-hf",
>     enable_prefix_caching=True,  # Cache common prefixes
> )
>
> system_prompt = "You are a helpful AI assistant. "
> user_prompts = [
>     system_prompt + "What is Python?",
>     system_prompt + "How does git work?",
>     system_prompt + "Explain Docker.",
> ]
>
> # First batch (caches system prompt)
> outputs1 = llm.generate(user_prompts, SamplingParams(max_tokens=100))
>
> # Second batch (uses cached prefix)
> outputs2 = llm.generate(user_prompts, SamplingParams(max_tokens=100))
> # ~30-50% speedup on second batch
> ```
