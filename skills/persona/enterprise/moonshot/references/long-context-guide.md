# Long Context Optimization Guide

> Techniques for effectively utilizing Kimi's 256K-2M token context windows.

## Why Long Context Matters

As Yang Zhilin stated: *"If an AI cannot remember an entire book, how can it truly understand and reason about a complex world?"*

### Use Cases Enabled

- **Legal**: Analyze 500-page contracts without chunking
- **Research**: Process entire research papers with all citations
- **Medical**: Review complete patient histories
- **Financial**: Analyze years of SEC filings
- **Literature**: Read full novels for analysis
- **Code**: Understand million-line codebases

## Architecture: Multi-head Latent Attention (MLA)

### Problem with Standard Attention

```
Standard Attention: KV cache = O(n × d × h)
- n = sequence length
- d = head dimension  
- h = number of heads

At 256K context: ~100GB+ just for KV cache!
```

### MLA Solution

```
MLA: Compress keys/values into latent vectors
- Low-rank compression of KV matrices
- Sub-linear memory growth
- ~80% memory reduction

Effective KV cache = O(n × d_latent) where d_latent << d × h
```

## Optimization Strategies

### 1. Hierarchical Context Management

```
Layer 3 (Active): 4K tokens
  ↓ attended by
Layer 2 (Working): 16K tokens  
  ↓ retrieved from
Layer 1 (Full): 256K-2M tokens

Only Layer 3 uses dense attention
Layers 2-1 use sparse retrieval
```

**Implementation:**

```python
class HierarchicalContext:
    def __init__(self, full_context: str):
        self.full = full_context  # 256K+ tokens
        self.segments = self._segment(full_context, 4_000)
        self.summaries = [self._summarize(s) for s in self.segments]
        self.active_window = []
    
    def retrieve_relevant(self, query: str, k: int = 3):
        """Retrieve top-k relevant segments"""
        scores = [self._relevance(query, s) for s in self.summaries]
        top_k = np.argsort(scores)[-k:]
        return [self.segments[i] for i in top_k]
    
    def get_active_context(self, query: str):
        relevant = self.retrieve_relevant(query)
        return "\n\n".join(relevant)
```

### 2. KV Cache Optimization

```python
# FlashAttention-3 with MLA
from flash_attn import flash_attn_func

# MLA reduces KV cache by 80%
# Cache eviction strategy
class SlidingWindowKVCache:
    def __init__(self, window_size: int = 16_384):
        self.window_size = window_size
        self.cache = {}
    
    def update(self, position: int, kv_tuple):
        self.cache[position] = kv_tuple
        # Evict oldest if beyond window
        if len(self.cache) > self.window_size:
            oldest = min(self.cache.keys())
            del self.cache[oldest]
    
    def get(self, positions: List[int]):
        return [self.cache[p] for p in positions if p in self.cache]
```

### 3. Prompt Compression

```python
# Remove redundant content before sending
import re

def compress_prompt(text: str, target_ratio: float = 0.8) -> str:
    """Compress prompt while preserving semantic content"""
    # Remove extra whitespace
    text = re.sub(r'\n+', '\n', text)
    text = re.sub(r' +', ' ', text)
    
    # Remove common filler phrases
    fillers = [
        r'\b(as mentioned earlier|as noted above|in summary)\b',
        r'\b(it is important to note that|it should be noted that)\b',
    ]
    for filler in fillers:
        text = re.sub(filler, '', text, flags=re.IGNORECASE)
    
    return text.strip()

# Use with Kimi
compressed = compress_prompt(long_document)
response = client.chat.completions.create(
    model="kimi-k2.5",
    messages=[{
        "role": "user",
        "content": f"Analyze this document:\n{compressed}"
    }]
)
```

### 4. Needle-in-Haystack Testing

```python
def needle_in_haystack_test(model, context_length: int):
    """Test retrieval accuracy at given context length"""
    needle = "The secret code is 12345."
    haystack = generate_filler_text(context_length - len(needle))
    
    # Insert needle at random position
    position = random.randint(0, len(haystack))
    full_text = haystack[:position] + needle + haystack[position:]
    
    response = client.chat.completions.create(
        model=model,
        messages=[{
            "role": "user",
            "content": f"What is the secret code?\n\nContext:\n{full_text}"
        }]
    )
    
    return "12345" in response.choices[0].message.content

# Run test at different depths
depths = [0.0, 0.25, 0.5, 0.75, 1.0]  # Beginning to end
for depth in depths:
    accuracy = test_at_depth(depth, context_length=256_000)
    print(f"Depth {depth}: {accuracy}%")
```

## Best Practices

### 1. Document Preprocessing

```python
def prepare_long_document(doc: str) -> str:
    """Prepare document for long context processing"""
    # 1. Extract structure
    sections = extract_sections(doc)
    
    # 2. Create table of contents
    toc = "\n".join([f"- {s.title}" for s in sections])
    
    # 3. Prioritize sections
    priority_order = prioritize_by_relevance(sections)
    
    # 4. Reconstruct with TOC
    processed = f"""TABLE OF CONTENTS:
{toc}

---

{chr(10).join(s.content for s in priority_order)}
"""
    return processed
```

### 2. Conversation Management

```python
class LongContextConversation:
    def __init__(self, max_tokens: int = 256_000):
        self.max_tokens = max_tokens
        self.messages = []
        self.summaries = []
    
    def add_message(self, role: str, content: str):
        self.messages.append({"role": role, "content": content})
        
        # Check token count
        total_tokens = sum(
            estimate_tokens(m["content"]) 
            for m in self.messages
        )
        
        # Summarize oldest messages if needed
        while total_tokens > self.max_tokens * 0.9:
            old_messages = self.messages[:3]
            summary = self._summarize_conversation(old_messages)
            self.summaries.append(summary)
            self.messages = self.messages[3:]
            total_tokens = sum(
                estimate_tokens(m["content"]) 
                for m in self.messages
            )
    
    def get_context(self):
        """Get conversation context with summaries"""
        context = []
        if self.summaries:
            context.append({
                "role": "system",
                "content": f"Previous conversation summary: {' '.join(self.summaries)}"
            })
        context.extend(self.messages)
        return context
```

### 3. Multi-Document Processing

```python
def merge_documents(docs: List[str], strategy: str = "concat") -> str:
    """Merge multiple documents for long context processing"""
    
    if strategy == "concat":
        # Simple concatenation with separators
        return "\n\n---\n\n".join(docs)
    
    elif strategy == "hierarchical":
        # Summarize each, then merge summaries
        summaries = [summarize(d) for d in docs]
        full_summaries = "\n\n".join(summaries)
        
        # Include full text of most relevant
        relevance_scores = [score_relevance(s) for s in summaries]
        most_relevant_idx = np.argmax(relevance_scores)
        
        return f"""DOCUMENT SUMMARIES:
{full_summaries}

---

FULL TEXT OF MOST RELEVANT DOCUMENT:
{docs[most_relevant_idx]}
"""
```

## Performance Benchmarks

### Context Length vs Latency

| Context | TTFT (p50) | TTFT (p99) | Throughput |
|---------|------------|------------|------------|
| 4K | 150ms | 300ms | 100 tok/s |
| 32K | 200ms | 400ms | 80 tok/s |
| 128K | 300ms | 600ms | 60 tok/s |
| 256K | 400ms | 800ms | 40 tok/s |
| 2M | 1s | 2s | 20 tok/s |

### Memory Usage

| Context | MLA | Standard Attention | Savings |
|---------|-----|-------------------|---------|
| 32K | 20GB | 80GB | 75% |
| 128K | 80GB | 320GB | 75% |
| 256K | 160GB | 640GB | 75% |

## Common Pitfalls

| Pitfall | Impact | Solution |
|---------|--------|----------|
| **Loading full context into dense attention** | OOM, slow | Use MLA + hierarchical retrieval |
| **No context compression** | Token waste | Preprocess, remove redundancy |
| **Monolithic prompts** | Poor retrieval | Structure with clear sections |
| **Ignoring position bias** | Lost information at middle | Test needle-in-haystack |
| **No conversation management** | Context overflow | Implement summarization |

## Advanced Techniques

### 1. Query-Aware Context Pruning

```python
def prune_context(query: str, context: str, max_tokens: int) -> str:
    """Keep only relevant sections based on query"""
    sections = split_into_sections(context)
    
    # Score each section
    scores = [
        (section, semantic_similarity(query, section))
        for section in sections
    ]
    
    # Keep highest scoring until max_tokens
    result = []
    current_tokens = 0
    for section, score in sorted(scores, key=lambda x: -x[1]):
        section_tokens = estimate_tokens(section)
        if current_tokens + section_tokens <= max_tokens:
            result.append(section)
            current_tokens += section_tokens
    
    return "\n\n".join(result)
```

### 2. Progressive Summarization

```python
def progressive_summarize(text: str, levels: int = 3) -> List[str]:
    """Create multi-level summaries"""
    summaries = [text]
    
    for _ in range(levels):
        current = summaries[-1]
        if len(current) < 1000:
            break
        summary = summarize(current, ratio=0.3)
        summaries.append(summary)
    
    return summaries

# Usage: Different detail levels for different queries
summaries = progressive_summarize(long_document)
# Level 0: Full text (2M tokens)
# Level 1: Summary (600K tokens)
# Level 2: Abstract (180K tokens)
```

---

*Guide for maximizing Kimi's long context capabilities | Updated: 2026-03-21*
