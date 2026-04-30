# DeepSeek API Documentation

## Base Configuration

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)
```

## Available Models

| Model | ID | Use Case |
|-------|-----|----------|
| DeepSeek-V3 | deepseek-chat | General chat, fast responses |
| DeepSeek-R1 | deepseek-reasoner | Complex reasoning tasks |

## Pricing (per 1M tokens)

| Model | Input (cache hit) | Input (cache miss) | Output |
|-------|-------------------|-------------------|--------|
| DeepSeek-V3 | $0.014 | $0.14 | $0.28 |
| DeepSeek-R1 | $0.14 | $0.55 | $2.19 |

Comparison: GPT-4o charges $2.50/$10.00 per 1M tokens (27x more expensive)

## Chat Completion Example

```python
# Standard chat (V3)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"}
    ],
    stream=False
)

print(response.choices[0].message.content)
```

## Reasoning Example (R1)

```python
# Reasoning model (R1)
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {"role": "user", "content": "Solve x^2 + 5x + 6 = 0"}
    ]
)

# The model thinks through the problem
print("Reasoning:", response.choices[0].message.reasoning_content)
print("Answer:", response.choices[0].message.content)
```

Response structure includes:
- reasoning_content: Chain-of-thought reasoning
- content: Final answer

## Streaming

```python
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True
)

for chunk in response:
    print(chunk.choices[0].delta.content, end="")
```

## Context Caching

DeepSeek automatically caches repeated inputs:
- Cache hit: 90% cost reduction
- Automatically applied to API calls
- No code changes needed

## Rate Limits

| Tier | RPM | TPM |
|------|-----|-----|
| Free | 10 | 100K |
| Tier 1 | 100 | 1M |
| Tier 2 | 1000 | 10M |
| Enterprise | Custom | Custom |

## Error Handling

```python
from openai import RateLimitError, APIError

try:
    response = client.chat.completions.create(...)
except RateLimitError:
    # Handle rate limit
    pass
except APIError as e:
    # Handle API error
    print(f"API Error: {e}")
```

## Best Practices

1. Use deepseek-chat for most tasks (faster, cheaper)
2. Use deepseek-reasoner only for complex problems
3. Implement retry logic for rate limits
4. Cache results when possible
5. Monitor token usage for cost control
