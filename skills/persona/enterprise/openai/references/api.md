# OpenAI API Reference

## Overview

The OpenAI API provides programmatic access to GPT models, DALL-E, Whisper, and embedding models. It serves 2M+ developers with billions of daily requests.

**Base URL**: `https://api.openai.com/v1`

**Authentication**: Bearer token in Authorization header
```
Authorization: Bearer $OPENAI_API_KEY
```

## Core Endpoints

### Chat Completions

**Endpoint**: `POST /v1/chat/completions`

**Primary API for GPT-4, GPT-4o, o1, etc.**

```json
{
  "model": "gpt-4o",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ],
  "temperature": 0.7,
  "max_tokens": 150
}
```

**Parameters:**

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| model | string | required | Model ID (gpt-4o, gpt-4o-mini, o1, etc.) |
| messages | array | required | Conversation history |
| temperature | float | 1.0 | Randomness (0-2) |
| max_tokens | integer | null | Max completion tokens |
| top_p | float | 1.0 | Nucleus sampling |
| n | integer | 1 | Number of completions |
| stream | boolean | false | Server-sent events |
| stop | string/array | null | Stop sequences |
| presence_penalty | float | 0 | -2.0 to 2.0 |
| frequency_penalty | float | 0 | -2.0 to 2.0 |

**Message Roles:**
- `system`: Set assistant behavior
- `user`: User input
- `assistant`: Model responses
- `tool`: Tool output (function calling)

### Completions (Legacy)

**Endpoint**: `POST /v1/completions`

**Legacy text completion (GPT-3 series)**

```json
{
  "model": "gpt-3.5-turbo-instruct",
  "prompt": "Once upon a time",
  "max_tokens": 100
}
```

### Embeddings

**Endpoint**: `POST /v1/embeddings`

```json
{
  "input": "The food was delicious and the waiter...",
  "model": "text-embedding-3-small"
}
```

### Images (DALL-E)

**Endpoint**: `POST /v1/images/generations`

```json
{
  "model": "dall-e-3",
  "prompt": "A cute baby sea otter",
  "n": 1,
  "size": "1024x1024",
  "quality": "standard",
  "style": "vivid"
}
```

**Sizes:**
- DALL-E 2: 256×256, 512×512, 1024×1024
- DALL-E 3: 1024×1024, 1792×1024, 1024×1792

### Audio

**Speech-to-Text (Whisper)**:
```bash
curl https://api.openai.com/v1/audio/transcriptions \
  -H "Authorization: Bearer $OPENAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@audio.mp3" \
  -F model="whisper-1"
```

**Text-to-Speech**:
```json
{
  "model": "tts-1",
  "input": "Hello world",
  "voice": "alloy"
}
```

Voices: alloy, echo, fable, onyx, nova, shimmer

## Advanced Features

### Function Calling

Enable models to call external functions:

```json
{
  "model": "gpt-4o",
  "messages": [{"role": "user", "content": "What's the weather in Paris?"}],
  "tools": [{
    "type": "function",
    "function": {
      "name": "get_weather",
      "description": "Get weather for a location",
      "parameters": {
        "type": "object",
        "properties": {
          "location": {"type": "string"},
          "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]}
        },
        "required": ["location"]
      }
    }
  }]
}
```

### JSON Mode

Force valid JSON output:

```json
{
  "model": "gpt-4o",
  "messages": [{"role": "user", "content": "List 3 planets"}],
  "response_format": {"type": "json_object"}
}
```

### Streaming

Real-time token delivery:

```javascript
const stream = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [{role: "user", content: "Say hello"}],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
```

### Batch API

Process large volumes asynchronously at 50% discount:

```json
// Create batch file (JSONL)
{"custom_id": "request-1", "method": "POST", "url": "/v1/chat/completions", "body": {...}}
{"custom_id": "request-2", "method": "POST", "url": "/v1/chat/completions", "body": {...}}

// Upload and process
POST /v1/batches
{
  "input_file_id": "file-abc123",
  "endpoint": "/v1/chat/completions",
  "completion_window": "24h"
}
```

## Assistants API (Beta)

Build AI assistants with persistent threads:

```javascript
// Create assistant
const assistant = await openai.beta.assistants.create({
  name: "Math Tutor",
  instructions: "You are a helpful math tutor...",
  model: "gpt-4o",
  tools: [{type: "code_interpreter"}]
});

// Create thread
const thread = await openai.beta.threads.create();

// Add message
await openai.beta.threads.messages.create(thread.id, {
  role: "user",
  content: "Solve 2x + 3 = 7"
});

// Run
const run = await openai.beta.threads.runs.create(thread.id, {
  assistant_id: assistant.id
});
```

## Fine-tuning

Customize models for specific tasks:

```bash
# Prepare data (JSONL)
{"messages": [{"role": "system", "content": "Marv is factual."}, {"role": "user", "content": "..."}, {"role": "assistant", "content": "..."}]}

# Upload
openai api files.create -f data.jsonl -p fine-tune

# Create job
openai api fine_tunes.create -t file-abc123 -m gpt-4o-mini-2024-07-18
```

## Pricing (as of 2025)

| Model | Input | Output |
|-------|-------|--------|
| GPT-5 | $3.00 / 1M tokens | $12.00 / 1M tokens |
| GPT-4o | $2.50 / 1M tokens | $10.00 / 1M tokens |
| GPT-4o mini | $0.150 / 1M tokens | $0.600 / 1M tokens |
| o1 | $15.00 / 1M tokens | $60.00 / 1M tokens |
| o3-mini | $1.10 / 1M tokens | $4.40 / 1M tokens |
| DALL-E 3 | $0.040 / image (standard) | $0.080 / image (HD) |
| Whisper | $0.006 / minute | - |
| TTS | $15.00 / 1M characters | - |
| Embeddings 3 small | $0.020 / 1M tokens | - |
| Embeddings 3 large | $0.130 / 1M tokens | - |

**Batch API**: 50% discount, 24h turnaround

## Rate Limits

| Tier | RPM | TPM | Batch Queue |
|------|-----|-----|-------------|
| Free | 3 | 150K | No |
| Tier 1 | 500 | 1M | Yes |
| Tier 2 | 5,000 | 10M | Yes |
| Tier 3 | 10,000 | 50M | Yes |
| Tier 4 | 20,000 | 200M | Yes |
| Tier 5 | 40,000 | 2B | Yes |

*RPM = Requests Per Minute, TPM = Tokens Per Minute*

## SDKs

**Python**:
```bash
pip install openai
```

```python
from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o",
    messages=[{"role": "user", "content": "Hello!"}]
)
print(completion.choices[0].message.content)
```

**JavaScript/TypeScript**:
```bash
npm install openai
```

```javascript
import OpenAI from 'openai';
const openai = new OpenAI();

const completion = await openai.chat.completions.create({
  model: "gpt-4o",
  messages: [{role: "user", content: "Hello!"}]
});
```

## Error Handling

| Code | Description | Retry? |
|------|-------------|--------|
| 400 | Bad request | No |
| 401 | Authentication | No |
| 429 | Rate limit | Yes (exponential backoff) |
| 500 | Server error | Yes |
| 503 | Service unavailable | Yes |

---

*Last Updated: March 2026*
