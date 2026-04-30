# Claude Model Family Reference

## Current Model Lineup (March 2026)

### Claude 4 Series (Latest)

| Model | Release | Context | Strengths | Input Price | Output Price |
|-------|---------|---------|-----------|-------------|--------------|
| **Claude Opus 4** | May 2025 | 200K | Complex reasoning, coding, agentic workflows | $15/M tokens | $75/M tokens |
| **Claude Opus 4.1** | Aug 2025 | 200K | Advanced coding, long-horizon planning, hybrid reasoning | $15/M tokens | $75/M tokens |
| **Claude Sonnet 4** | May 2025 | 200K | Balanced performance, fast responses | $3/M tokens | $15/M tokens |
| **Claude Sonnet 4.5** | Sep 2025 | 200K | Extended thinking mode, improved reasoning | $3/M tokens | $15/M tokens |

### Claude 3.5 Series

| Model | Release | Context | Strengths | Input Price | Output Price |
|-------|---------|---------|-----------|-------------|--------------|
| **Claude 3.5 Sonnet** | Jun 2024 | 200K | Strong all-around; coding; visual reasoning | $3/M tokens | $15/M tokens |
| **Claude 3.5 Haiku** | Nov 2024 | 200K | Fastest responses; cost-effective; real-time | $0.80/M tokens | $4/M tokens |

### Claude 3 Series (Previous Gen)

| Model | Context | Position |
|-------|---------|----------|
| Claude 3 Opus | 200K | Flagship (superseded by Opus 4) |
| Claude 3 Sonnet | 200K | Mid-tier (superseded by Sonnet 4) |
| Claude 3 Haiku | 200K | Fastest (superseded by Haiku 3.5) |

## Key Capabilities

### Extended Thinking (Reasoning Mode)

Available on Opus 4.1 and Sonnet 4.5:
- Step-by-step logical chain generation
- "Thinking budget" configurable up to 8K tokens
- Trade-off: more accurate but slower responses

### Computer Use (Beta)

Released October 2024:
- Claude can control computers via GUI interactions
- Capabilities: move cursor, click, type, navigate interfaces
- OSWorld benchmark: 14.9% screenshot-only; 22.0% with multi-step
- Use cases: automation, software testing, open-ended research tasks
- Safety: experimental; requires sandboxing and monitoring

### Artifacts

Released June 2024:
- Interactive content generation workspace
- Creates: code snippets, documents, web apps, visualizations
- Users can view, edit, and build upon AI-generated content in real-time
- Upgraded 2025: app hosting, sharing, dedicated workspace
- Enables "vibe coding" — non-technical users creating applications

### Context Window

- **Standard**: 200,000 tokens (~150,000 words, ~300 pages)
- **Extended**: Up to 1 million tokens (for specific models/use cases)
- **Knowledge cutoff**: Varies by model (Jan 2025 for Sonnet 4.5)

## Benchmark Performance

### Claude Sonnet 4.5 (example)
- MMLU: 89.8%
- HumanEval: 94.6%
- GSM8K: 96.7%

## Model Selection Guide

| Use Case | Recommended Model | Reasoning |
|----------|-------------------|-----------|
| Complex analysis, coding | Opus 4/4.1 | Highest capability |
| General enterprise tasks | Sonnet 4/4.5 | Best speed/capability balance |
| High-volume, real-time | Haiku 3.5 | Fastest, most cost-effective |
| Long document processing | Any 200K model | Extended context required |
| Agentic workflows | Opus 4.1 | Best tool use and planning |
| Interactive app building | Sonnet 4.5 + Artifacts | Fast iteration, good capability |

## Access Methods

- **Claude.ai**: Consumer web interface
- **Anthropic API**: Direct API access
- **Amazon Bedrock**: AWS integration
- **Google Cloud Vertex AI**: GCP integration
- **Claude Code**: Developer-focused IDE integration

## Safety Classifications

| Model | ASL Level | Notes |
|-------|-----------|-------|
| Claude 3.5 Sonnet/Haiku | ASL-2 | Standard deployment |
| Claude 4 Sonnet | ASL-2 | Standard deployment |
| Claude 4 Opus | ASL-3 | Additional safeguards required |
| Claude 4 Opus 4.1 | ASL-3 | Extended thinking evaluated separately |
