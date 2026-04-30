# Gemini AI Model Family Reference

Comprehensive reference for Google's Gemini model family.

## Model Evolution Timeline

| Version | Release | Key Innovation |
|---------|---------|----------------|
| Gemini 1.0 | Dec 2023 | Native multimodality |
| Gemini 1.5 | Feb 2024 | 1M token context, MoE |
| Gemini 2.0 | Dec 2024 | Real-time streaming |
| Gemini 2.5 | Apr 2025 | Advanced reasoning |
| Gemini 3.0 | Nov 2025 | Agentic capabilities |

## Current Models (2025)

### Gemini 3.1 Pro (Latest)
**Release:** November 2025

**Capabilities:**
- Context window: 2M tokens
- Multimodal: Text, image, audio, video, code
- Reasoning: ARC-AGI-2 score 77.1%
- Tool use: Native Google Search, code execution, API calls
- Special: SVG animation, 3D simulation generation

**Best For:**
- Complex problem-solving
- Long-document analysis
- Creative coding
- Research tasks

### Gemini 2.5 Pro
**Release:** April 2025

**Capabilities:**
- Context window: 1M tokens
- "Thinking" mode: Adjustable compute budget
- Deep Think: Parallel reasoning for complex problems
- Multimodal inputs: All modalities

**Performance Benchmarks:**
- MATH: 95%+
- Codeforces: Expert-level
- GPQA Diamond: 80%+

**Variants:**
- Standard: Balanced speed/quality
- Deep Think: Maximum accuracy (slower)

### Gemini 2.5 Flash
**Release:** June 2025

**Capabilities:**
- Context window: 1M tokens
- Optimized: Speed and cost
- Thinking: Configurable budget
- Multimodal: All inputs

**Use Cases:**
- High-volume applications
- Real-time assistants
- Cost-sensitive workloads

### Gemini 2.5 Flash-Lite
**Release:** June 2025

**Capabilities:**
- Ultra-low latency
- Highest throughput per dollar
- 1M token context

**Best For:**
- Simple tasks at massive scale
- Edge deployment
- Background processing

## Architecture Details

### Mixture of Experts (MoE)
```
Total Parameters: 1.5T+ (Gemini 3)
Active Parameters: 50B per token
Efficiency: 3x vs dense models
Routing: Learned expert selection
```

### Multimodal Native Design
```
┌─────────────────────────────────────┐
│         Unified Transformer         │
│   (Single model, all modalities)    │
└─────────────────────────────────────┘
                   │
    ┌──────────────┼──────────────┐
    ▼              ▼              ▼
┌────────┐   ┌────────┐   ┌────────┐
│  Text  │   │ Image  │   │ Audio  │
│Encoder │   │Encoder │   │Encoder │
└────────┘   └────────┘   └────────┘
    │              │              │
    └──────────────┼──────────────┘
                   ▼
        ┌─────────────────┐
        │  Cross-Modal    │
        │  Attention      │
        └─────────────────┘
```

### Training Infrastructure
| Component | Specification |
|-----------|---------------|
| Hardware | TPU v5 (512+ chips) |
| Training Data | Multimodal web corpus |
| Data Quality | Multi-stage filtering |
| Safety | Constitutional AI, RLHF |
| Evaluation | 50+ benchmarks |

## API Capabilities

### Generation Config
```python
generation_config = {
    'temperature': 0.9,        # Creativity (0-2)
    'top_p': 0.95,            # Nucleus sampling
    'top_k': 40,              # Top-k sampling
    'max_output_tokens': 8192,
    'stop_sequences': ['END'],
}
```

### Safety Settings
```python
safety_settings = {
    'HARASSMENT': 'BLOCK_MEDIUM_AND_ABOVE',
    'HATE_SPEECH': 'BLOCK_HIGH',
    'SEXUALLY_EXPLICIT': 'BLOCK_HIGH',
    'DANGEROUS_CONTENT': 'BLOCK_HIGH',
}
```

### Tool Use
```python
tools = [
    {'google_search': {}},
    {'code_execution': {}},
    {'function_declarations': [custom_functions]},
]
```

## Performance Benchmarks

### Academic Benchmarks
| Benchmark | Gemini 3.1 Pro | GPT-4 | Claude 3.5 |
|-----------|----------------|-------|------------|
| MMLU | 90%+ | 87% | 88% |
| MATH | 95%+ | 73% | 71% |
| HumanEval | 92% | 87% | 92% |
| GPQA | 80%+ | 53% | 65% |
| ARC-AGI-2 | 77.1% | 45% | 50% |

### Multimodal Benchmarks
| Benchmark | Score |
|-----------|-------|
| MMMU (multimodal) | 78% |
| MathVista | 73% |
| Video-MME | 65% |

## Integration Points

### Google Workspace
- Gmail: Smart Compose, summarize
- Docs: Writing assistant
- Sheets: Data analysis, formulas
- Slides: Content generation
- Meet: Live captions, summaries

### Google Cloud
- Vertex AI: Model serving
- BigQuery: SQL generation
- Looker: Natural language queries
- Security Command Center: Threat analysis

### Android
- On-device: Gemini Nano
- System-level: Smart Reply, Now Playing
- Pixel exclusive: Call Screen, Hold for Me

### Developer Tools
- Android Studio: Code completion
- Firebase: App suggestions
- Chrome: Help me write
- Google AI Studio: Prototyping

## Pricing (Vertex AI)

### Input Tokens
| Model | Price per 1M tokens |
|-------|---------------------|
| Gemini 3.1 Pro | $3.50 |
| Gemini 2.5 Pro | $1.25 |
| Gemini 2.5 Flash | $0.15 |
| Gemini 2.5 Flash-Lite | $0.075 |

### Output Tokens
| Model | Price per 1M tokens |
|-------|---------------------|
| Gemini 3.1 Pro | $10.50 |
| Gemini 2.5 Pro | $10.00 |
| Gemini 2.5 Flash | $0.60 |
| Gemini 2.5 Flash-Lite | $0.30 |

### Context Caching
- Cached input: 25% of standard price
- Minimum: 1 hour
- Maximum: 1 hour (adjustable)

## Responsible AI

### Safety Approaches
1. **Pre-training:** Data filtering, quality scoring
2. **Post-training:** RLHF, constitutional AI
3. **Inference:** Safety classifiers, query filtering
4. **Evaluation:** Red teaming, harm assessments

### Known Limitations
- Hallucinations on edge cases
- Knowledge cutoff (training date)
- Biases from training data
- Reasoning gaps on novel problems

### Best Practices
- Always verify factual claims
- Use grounding for critical applications
- Implement human-in-the-loop for high-stakes
- Monitor for bias in production
