# Moonshot API Reference

> Complete API documentation for Kimi models and Moonshot platform integration.

## Base URL

```
https://api.moonshot.cn/v1
```

## Authentication

All API requests require an API key in the Authorization header:

```bash
curl https://api.moonshot.cn/v1/chat/completions \
  -H "Authorization: Bearer $MOONSHOT_API_KEY" \
  -H "Content-Type: application/json"
```

## Models

| Model ID | Context Window | Description |
|----------|----------------|-------------|
| `kimi-k2.5` | 256,000 tokens | Latest general-purpose model with MoE architecture |
| `kimi-k2.5-long` | 2,000,000 tokens | Extended context for document processing |
| `kimi-k2` | 128,000 tokens | Cost-efficient long context model |
| `kimi-k1.5` | 128,000 tokens | Reasoning-focused model with Long-CoT |
| `kimi-latest` | 131,072 tokens | Alias to latest stable model |

## Chat Completions

### Endpoint

```
POST /v1/chat/completions
```

### Request Format

```json
{
  "model": "kimi-k2.5",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  "temperature": 0.3,
  "max_tokens": 4096,
  "stream": false
}
```

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `model` | string | Yes | — | Model ID |
| `messages` | array | Yes | — | Conversation history |
| `temperature` | float | No | 0.3 | Sampling temperature (0-2) |
| `max_tokens` | integer | No | — | Maximum tokens to generate |
| `stream` | boolean | No | false | Stream response tokens |
| `response_format` | object | No | — | JSON mode: `{"type": "json_object"}` |

### Vision/Multimodal Requests

```json
{
  "model": "kimi-k2.5",
  "messages": [{
    "role": "user",
    "content": [
      {"type": "text", "text": "What's in this image?"},
      {"type": "image_url", "image_url": {"url": "data:image/png;base64,abc123..."}}
    ]
  }]
}
```

### Streaming Response

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_KEY", base_url="https://api.moonshot.cn/v1")

stream = client.chat.completions.create(
    model="kimi-k2.5",
    messages=[{"role": "user", "content": "Hello"}],
    stream=True
)

for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
```

## Token Counting

### Endpoint

```
POST /v1/tokenizers/estimate-token-count
```

### Request

```json
{
  "model": "kimi-k2.5",
  "messages": [
    {"role": "user", "content": "Hello, world!"}
  ]
}
```

### Response

```json
{
  "data": {
    "total_tokens": 15
  }
}
```

## Error Handling

### HTTP Status Codes

| Code | Meaning | Resolution |
|------|---------|------------|
| 400 | Bad Request | Check request format |
| 401 | Unauthorized | Verify API key |
| 429 | Rate Limited | Implement exponential backoff |
| 500 | Server Error | Retry with backoff |

### Error Response Format

```json
{
  "error": {
    "message": "Rate limit exceeded",
    "type": "rate_limit_error",
    "code": "rate_limit_exceeded"
  }
}
```

## Rate Limits

| Tier | Requests/min | Tokens/min |
|------|--------------|------------|
| Free | 20 | 100,000 |
| Tier 1 | 100 | 1,000,000 |
| Tier 2 | 500 | 5,000,000 |
| Enterprise | Custom | Custom |

## SDK Examples

### Python (OpenAI SDK)

```python
from openai import OpenAI

client = OpenAI(
    api_key="YOUR_MOONSHOT_API_KEY",
    base_url="https://api.moonshot.cn/v1"
)

response = client.chat.completions.create(
    model="kimi-k2.5",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(response.choices[0].message.content)
```

### Node.js

```javascript
import OpenAI from 'openai';

const client = new OpenAI({
  apiKey: process.env.MOONSHOT_API_KEY,
  baseURL: 'https://api.moonshot.cn/v1'
});

const response = await client.chat.completions.create({
  model: 'kimi-k2.5',
  messages: [{ role: 'user', content: 'Hello!' }]
});

console.log(response.choices[0].message.content);
```

### cURL

```bash
curl -X POST "https://api.moonshot.cn/v1/chat/completions" \
  -H "Authorization: Bearer $MOONSHOT_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "kimi-k2.5",
    "messages": [{"role": "user", "content": "Hello!"}]
  }'
```

## File Upload (for long context)

For documents exceeding API limits, use the file upload API:

```bash
curl -X POST "https://api.moonshot.cn/v1/files" \
  -H "Authorization: Bearer $MOONSHOT_API_KEY" \
  -F "file=@document.pdf" \
  -F "purpose=batch"
```

Then reference in chat:

```json
{
  "model": "kimi-k2.5-long",
  "messages": [{
    "role": "user",
    "content": "Analyze the uploaded document",
    "file_ids": ["file-abc123"]
  }]
}
```

---

*Reference: Moonshot AI Platform Documentation | Updated: 2026-03-21*
