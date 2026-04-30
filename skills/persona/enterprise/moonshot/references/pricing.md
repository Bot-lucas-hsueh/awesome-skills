# Moonshot Pricing Reference

> Current pricing for Kimi models and API usage.

## Official API Pricing

### Kimi K2.5

| Component | Price per 1M Tokens |
|-----------|---------------------|
| Input (Cache Hit) | $0.10 |
| Input (Cache Miss) | $0.60 |
| Output | $3.00 |
| Context Window | 256,000 tokens |

### Kimi K2.5 Long

| Component | Price per 1M Tokens |
|-----------|---------------------|
| Input | $0.80 |
| Output | $4.00 |
| Context Window | 2,000,000 tokens |

### Kimi K2

| Component | Price per 1M Tokens |
|-----------|---------------------|
| Input | $0.14 |
| Output | $2.49 |
| Context Window | 128,000 tokens |

### Kimi K1.5

| Component | Price per 1M Tokens |
|-----------|---------------------|
| Input | $0.50 |
| Output | $2.00 |
| Context Window | 128,000 tokens |

## Cost Comparison (per 1M tokens)

| Model | Input | Output | Context |
|-------|-------|--------|---------|
| **Kimi K2.5** | $0.60 | $3.00 | 256K |
| **Claude Opus 4.5** | $5.00 | $25.00 | 200K |
| **GPT-4o** | $2.50 | $10.00 | 128K |
| **DeepSeek-V3** | $0.14 | $0.28 | 64K |

**Kimi K2.5 is ~9x cheaper than Claude Opus 4.5 for similar capabilities.**

## Membership Pricing (Consumer)

### China Region (RMB)

| Plan | Monthly | Features |
|------|---------|----------|
| 轻量版 (Light) | ¥19 | Basic access, 50K context |
| 标准版 (Standard) | ¥49 | Full features, 200K context |
| 高级版 (Premium) | ¥99 | 2M context, priority access |

### International (USD)

| Plan | Monthly | Features |
|------|---------|----------|
| Moderato | $19 | Standard access, Deep Research quota |
| Fortissimo | $49 | 2M context, unlimited research |

## Cost Optimization Strategies

### 1. Prompt Caching

Reuse system prompts and context to trigger cache hit pricing ($0.10 vs $0.60):

```python
# Cache hit scenario - same prefix
messages = [
    {"role": "system", "content": long_system_prompt},  # Cached
    {"role": "user", "content": "Question 1"}
]
# Next request with same system prompt = cache hit
```

### 2. Context Window Selection

| Use Case | Recommended Model | Why |
|----------|-------------------|-----|
| Chat, Q&A | kimi-k2.5 | Best price/performance |
| Code analysis | kimi-k2.5 | Strong coding benchmarks |
| Document (100+ pages) | kimi-k2.5-long | 2M context needed |
| Quick tasks | kimi-k2 | Most cost-effective |
| Math/Reasoning | kimi-k1.5 | Long-CoT optimized |

### 3. Token Management

```python
# Estimate before calling
import tiktoken

encoder = tiktoken.encoding_for_model("cl100k_base")
tokens = len(encoder.encode(text))

# Optimize long contexts
if tokens > 200000:
    # Use k2.5-long or implement summarization
    model = "kimi-k2.5-long"
else:
    model = "kimi-k2.5"
```

### 4. Output Length Control

Output tokens cost 5x more than input. Control max_tokens:

```python
response = client.chat.completions.create(
    model="kimi-k2.5",
    messages=messages,
    max_tokens=1000  # Limit expensive output
)
```

## Budget Estimation

### Monthly Cost Calculator

| Usage Pattern | Requests/day | Avg Tokens | Monthly Cost |
|--------------|--------------|------------|--------------|
| Light (testing) | 10 | 2K | ~$5 |
| Development | 100 | 5K | ~$100 |
| Production (small) | 1,000 | 10K | ~$1,000 |
| Production (medium) | 10,000 | 10K | ~$10,000 |
| Enterprise | 100,000 | 20K | Custom pricing |

### Formula

```
Monthly Cost = (Requests × Input Tokens × Input Price + 
                Requests × Output Tokens × Output Price) × 30
```

Example: 1000 requests/day, 5000 input tokens, 1000 output tokens:
```
= (1000 × 5000 × $0.60/1M + 1000 × 1000 × $3.00/1M) × 30
= ($3 + $3) × 30
= $180/month
```

## Free Tier

- **Requests**: 100/day
- **Tokens**: 10,000/day
- **Models**: All models available
- **Features**: Full API access

## Enterprise Pricing

Contact Moonshot AI sales for:
- Volume discounts (>10M tokens/month)
- Dedicated capacity
- Custom SLA
- On-premise deployment options

---

*Pricing as of March 2026. Check platform.moonshot.cn for current rates.*
