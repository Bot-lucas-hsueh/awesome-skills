## § 5 — Tools & Commands

### 5.1 DeepSeek API Usage

```bash
# Install DeepSeek SDK
pip install openai  # DeepSeek uses OpenAI-compatible API

# API Configuration
export DEEPSEEK_API_KEY="your-api-key"
export DEEPSEEK_BASE_URL="https://api.deepseek.com"

# Python Usage
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url=os.getenv("DEEPSEEK_BASE_URL")
)

# DeepSeek-V3 (chat)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Hello!"}]
)

# DeepSeek-R1 (reasoning)
response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Solve x² + 5x + 6 = 0"}]
)
# Response includes reasoning_content (CoT) and content (final answer)
```

### 5.2 Local Deployment

```bash
# Download from HuggingFace
pip install transformers accelerate

from transformers import AutoModelForCausalLM, AutoTokenizer

# Load DeepSeek-V3 (requires significant GPU memory)
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/DeepSeek-V3",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)

# Load distilled model (more accessible)
model = AutoModelForCausalLM.from_pretrained(
    "deepseek-ai/DeepSeek-R1-Distill-Qwen-32B",
    torch_dtype=torch.bfloat16,
    device_map="auto"
)
```

### 5.3 Model Comparison Matrix

| Use Case | Recommended Model | Parameters | VRAM Needed |
|----------|------------------|------------|-------------|
| Production API | deepseek-chat (V3) | 671B/37B | API-only |
| Complex reasoning | deepseek-reasoner (R1) | 671B/37B | API-only |
| Local 48GB GPU | R1-Distill-Qwen-32B | 32B | ~80GB |
| Local 24GB GPU | R1-Distill-Qwen-14B | 14B | ~35GB |
| Consumer GPU | R1-Distill-Qwen-7B | 7B | ~18GB |
| Edge/CPU | R1-Distill-Qwen-1.5B | 1.5B | ~4GB |

---
