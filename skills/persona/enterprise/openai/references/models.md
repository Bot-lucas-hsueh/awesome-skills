# OpenAI Models Reference

## GPT Series Evolution

### GPT-1 (June 2018)
- **Parameters**: 117M
- **Context**: 512 tokens
- **Innovation**: Proof of concept for generative pre-training
- **Architecture**: Decoder-only transformer, 12 layers
- **Dataset**: BookCorpus (7,000 books)
- **Significance**: Demonstrated unsupervised pre-training enables transfer learning

### GPT-2 (February 2019)
- **Parameters**: 1.5B
- **Context**: 1,024 tokens
- **Innovation**: Zero-shot task transfer without fine-tuning
- **Staged Release**: Controversial phased release due to misuse concerns
- **Dataset**: WebText (40GB of internet text)
- **Significance**: First demonstration of emergent few-shot capabilities

### GPT-3 (June 2020)
- **Parameters**: 175B (largest dense model at time)
- **Context**: 2,048 tokens
- **Innovation**: Few-shot learning, in-context learning, API launch
- **Dataset**: 300B tokens (filtered Common Crawl, books, Wikipedia)
- **Significance**: Demonstrated scale enables qualitatively new capabilities
- **Compute**: ~3.14 × 10^23 FLOPs

### GPT-3.5 (March 2022)
- **Base**: Refined GPT-3 architecture
- **Innovation**: InstructGPT alignment training
- **Products**: text-davinci-003, ChatGPT foundation
- **Significance**: RLHF makes models more helpful and harmless

### GPT-4 (March 2023)
- **Architecture**: Mixture of Experts (MoE), ~1.8T total, ~280B active
- **Context**: 8,192 (standard), 32,768 (extended)
- **Modalities**: Text + image (multimodal)
- **Training**: RLHF with extensive safety mitigations
- **Significance**: First "GPT-4 class" model, major capability jump

### GPT-4 Turbo (November 2023)
- **Context**: 128K tokens (~300 pages)
- **Knowledge**: Current to April 2023
- **Features**: JSON mode, reproducible outputs, parallel function calling
- **Cost**: 3× cheaper than GPT-4

### GPT-4o (May 2024)
- **"o"**: "omni" — native multimodal across text, image, audio
- **Context**: 128K tokens
- **Voice**: Native audio in/out, ~320ms latency
- **Vision**: Improved image understanding
- **Cost**: 50% cheaper than GPT-4 Turbo

### GPT-4.1 (April 2025)
- **Context**: Up to 1M tokens
- **Improvements**: Enhanced instruction following, code understanding
- **Features**: Supervised fine-tuning support

### GPT-5 (August 2025)
- **Architecture**: ~2T MoE, unified fast + reasoning modes
- **Context**: 128K-1M tokens
- **Innovation**: Adaptive compute — automatically switches between fast and deep thinking
- **Integration**: o-series reasoning capabilities merged into main model

## o-Series Reasoning Models

### o1-preview (September 2024)
- **Innovation**: Chain-of-thought reasoning with RL training
- **Use Case**: Complex STEM problems
- **Limitation**: No browsing, file upload, or image understanding

### o1 (December 2024)
- **Features**: Full tool use, image understanding, structured outputs
- **Context**: 200K input, 100K output
- **Improvement**: More reliable reasoning than preview

### o3-mini (January 2025)
- **Optimization**: Efficient reasoning for STEM tasks
- **Latency**: Faster than full o3
- **Cost**: Lower price point for reasoning

### o3 (June 2025)
- **Capability**: Advanced multi-step reasoning and planning
- **Use Cases**: Research, engineering analysis, complex problem-solving

### o4-mini (March 2025)
- **Focus**: Latency-optimized reasoning
- **Use Case**: Real-time applications requiring reasoning

## Multimodal Models

### DALL-E Series

**DALL-E (January 2021)**
- Architecture: dVAE + GPT-3
- Resolution: 256×256
- Innovation: First text-to-image at scale

**DALL-E 2 (April 2022)**
- Architecture: CLIP + diffusion model
- Resolution: 1024×1024
- Features: Inpainting, outpainting, variations

**DALL-E 3 (October 2023)**
- Integration: Native in ChatGPT
- Improvement: Prompt following, text rendering
- Safety: Enhanced content filtering

### Sora Series

**Sora (February 2024)**
- Capability: Text-to-video, up to 60 seconds
- Resolution: Up to 1920×1080
- Innovation: Spacetime patches, diffusion transformer
- Physics: Realistic world simulation

**Sora 2 (Late 2024)**
- Duration: Extended capabilities
- Consistency: Better character/object continuity
- Control: Enhanced prompt adherence

### Whisper

**Whisper v1 (September 2022)**
- Architecture: Encoder-decoder transformer
- Languages: 99 languages
- Tasks: Speech recognition, translation, identification
- Release: Open weights (unusual for OpenAI)

**Whisper v2/v3**
- Improved accuracy
- Better noisy audio handling
- Large-v3: Best quality
- Turbo: Speed-optimized

## Embedding Models

| Model | Dimensions | Context | Best For |
|-------|------------|---------|----------|
| text-embedding-3-small | 1,536 | 8,191 | Cost-effective, fast |
| text-embedding-3-large | 3,072 | 8,191 | Best quality |
| text-embedding-ada-002 | 1,536 | 8,191 | Legacy compatibility |

## Model Specifications Summary

| Model | Input | Output | Context | Training Data |
|-------|-------|--------|---------|---------------|
| GPT-4o | Text, Image, Audio | Text, Audio | 128K | Web, books, code, images |
| GPT-4o mini | Text, Image | Text | 128K | GPT-4o distillation |
| o1 | Text, Image | Text | 200K | Reasoning traces, STEM |
| o3 | Text, Image | Text | 200K | Advanced reasoning |
| DALL-E 3 | Text | Image | 4,000 | Text-image pairs |
| Whisper | Audio | Text | 30s | Multilingual audio |
| TTS | Text | Audio | 4,096 | Speech synthesis |

## Deprecated Models

| Model | Replacement | Deprecation Date |
|-------|-------------|------------------|
| GPT-3 | GPT-3.5 Turbo | January 2024 |
| text-davinci-003 | GPT-3.5 Turbo | January 2024 |
| code-davinci-002 | GPT-4 | March 2023 |
| GPT-4 (original) | GPT-4 Turbo | Various |

---

*Last Updated: March 2026*
