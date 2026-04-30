## § 8 · Scenario Examples

### Example 1: Customer Support Chatbot

**Context**: RAG-based chatbot for customer support.

**Architecture**:
```
Components:
├── Vector DB: Pinecone with 100K support articles
├── Embeddings: OpenAI text-embedding-3-large
├── LLM: GPT-4-turbo for generation
├── Re-ranking: Cohere cross-encoder

Flow:
├── User query → embedding
├── Retrieve top-5 relevant articles
├── Re-rank for precision
├── Generate answer with citations
└── Fallback to human if confidence low

Results:
├── 85% resolution rate without human
├── < 2s response time
└── CSAT: 4.2/5
```

---

### Example 2: Legal Document Analysis

**Context**: Contract review and clause extraction.

**Solution**:
```
Approach:
├── Base model: Legal-BERT (domain-specific)
├── Fine-tuned: Named entity recognition (parties, dates, amounts)
├── Classification: Clause type identification
├── Generation: Risk summary generation

Deployment:
├── On-premise (privacy requirement)
├── Quantized to INT8 for speed
├── Batch processing for bulk review
└── Human-in-the-loop for critical clauses
```

---

### Example 3: Multilingual Sentiment Analysis

**Context**: Analyze sentiment in 50 languages.

**Implementation**:
```
Model: XLM-RoBERTa-large
├── Pre-trained on 100 languages
├── Fine-tuned on multilingual sentiment corpus
├── Zero-shot for low-resource languages

Optimization:
├── Distilled version (60% size, 95% accuracy)
├── ONNX runtime for inference
├── Batch inference for throughput

Results:
├── F1: 0.89 average across languages
├── Latency: < 50ms per text
```

---

### Example 4: Code Generation Assistant

**Context**: GitHub Copilot-like code completion.

**Architecture**:
```
Model: Fine-tuned CodeLlama-34B
├── Fine-tuned on company codebase
├── LoRA adapters for specific languages
├── Speculative decoding for speed

Features:
├── Multi-line completion
├── Natural language to code
├── Code explanation
├── Test generation

Constraints:
├── < 100ms suggestion latency
├── Filter for security vulnerabilities
├── License compliance checking
```

---

### Example 5: Content Moderation System

**Context**: Real-time toxicity detection for user-generated content.

**System**:
```
Pipeline:
├── Fast filter: Regex + keyword (blocks obvious)
├── BERT classifier: Toxicity score 0-1
├── LLM judge: Borderline cases
├── Human review: Appeals and edge cases

Metrics:
├── Precision: 98% (low false positives)
├── Recall: 95% (catches most toxicity)
├── Latency: < 20ms (p99)
```

---
