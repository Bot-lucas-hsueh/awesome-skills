# Firefly AI Capabilities Guide

## Overview

Adobe Firefly is a family of generative AI models designed for creative workflows, emphasizing **commercial safety** through training on licensed Adobe Stock content and public domain materials. Firefly is integrated across Creative Cloud, Document Cloud, and Adobe Express.

## Model Family

### Firefly Image Model 3

**Capabilities**:
- Text-to-image generation with improved prompt understanding
- Higher quality outputs with better lighting and detail
- Enhanced text rendering within images
- 4x faster generation than previous models

**Key Features**:
- **Generative Fill**: Add, remove, or replace image elements
- **Generative Expand**: Extend canvas with AI-generated content
- **Generate Similar**: Create variations of existing images
- **Structure Reference**: Use reference images for composition guidance

**Integration Points**:
- Photoshop (native)
- Illustrator (beta)
- Adobe Express
- Firefly Web Application

### Firefly Vector Model

**Capabilities**:
- Text-to-vector graphic generation
- Editable SVG output with standard paths
- Organized layers and groups
- Scalable without quality loss

**Key Features**:
- **Generative Shape Fill**: Add detailed vector content to shapes
- **Text to Vector Graphic**: Generate icons, logos, illustrations
- Style consistency across generations

**Integration Points**:
- Adobe Illustrator (native)
- Adobe Express

### Firefly Video Model

**Capabilities**:
- Text-to-video generation
- Image-to-video animation
- Video extension (Generative Extend)
- Camera angle and motion controls

**Key Features**:
- **Composition Reference**: Match structure of reference video
- **Style Presets**: Claymation, anime, line art, 2D animation
- **Keyframe Cropping**: First/last frame-based generation
- **Generate Sound Effects**: Text-to-audio for video

**Integration Points**:
- Premiere Pro (Generative Extend)
- Firefly Web Application
- After Effects (planned)

### Firefly Design Model

**Capabilities**:
- Text-to-template generation
- Layout optimization
- Brand-consistent design

**Key Features**:
- Marketing asset generation
- Social media template creation
- Multi-format output

**Integration Points**:
- Adobe Express
- Firefly Web Application

## Firefly Services (Enterprise)

### Custom Models

**Training Process**:
1. Upload proprietary brand assets (50-200 images)
2. Define style parameters and constraints
3. Model training (24-48 hours)
4. Deployment for team access

**Use Cases**:
- Brand-consistent product photography
- Style-matched illustration generation
- Marketing asset templates

### Firefly APIs

**Available Endpoints**:
```javascript
// Image Generation
POST /v2/images/generate
{
  "prompt": "Product photography, minimalist setting",
  "model": "firefly-image-3",
  "size": "1024x1024",
  "styles": ["photographic"],
  "negativePrompt": "blurry, distorted"
}

// Generative Fill
POST /v2/images/fill
{
  "image": "base64_encoded_image",
  "mask": "base64_encoded_mask",
  "prompt": "Add wooden table surface",
  "match": {
    "lighting": true,
    "perspective": true
  }
}

// Generative Expand
POST /v2/images/expand
{
  "image": "base64_encoded_image",
  "targetSize": { "width": 2048, "height": 1024 },
  "prompt": "Extend landscape with mountains"
}
```

## Generative Credits System

### Allocation by Plan

| Plan | Monthly Credits |
|------|-----------------|
| Creative Cloud All Apps | 1,000 |
| Single App | 500 |
| Adobe Stock | 500 |
| Express Premium | 250 |
| Firefly Premium | 100 |
| Free | 25 |
| Enterprise All Apps | 1,000+ |
| Pro Plus All Apps | 3,000 |

### Usage Guidelines

**Standard Generations**:
- Text-to-Image: 1 credit per generation
- Generative Fill: 1 credit per generation
- Vector Generation: 2 credits per generation

**Priority Processing**:
- After credit depletion: Slower generation
- Additional credits: $4.99/100 credits

## Firefly Boards (Beta)

**Purpose**: Collaborative AI-powered ideation canvas

**Features**:
- Real-time multiplayer editing
- Text-to-image generation in shared space
- Version history and branching
- Export to Creative Cloud apps

**Workflow**:
1. Create board for project/moodboard
2. Generate images with team feedback
3. Remix and iterate on concepts
4. Export favorites for refinement

## Content Authenticity

### Content Credentials

**Implementation**:
- Cryptographic metadata embedding
- Provenance tracking from capture to edit
- Tamper-evident seals

**Do Not Train**:
- Artist opt-out registry
- Content exclusion from model training
- Transparent usage rights

### CAI Web App

**Features**:
- Verify content authenticity
- View edit history
- Check AI generation status
- Export credentials

## Latest Updates (2024-2025)

### Q4 2024

- **Firefly Image Model 3**: Higher quality, better text
- **Generative Workspace** (Photoshop Beta): Multi-prompt brainstorming
- **Distraction Removal**: AI-powered object detection

### Q1 2025

- **Firefly Video Model GA**: Text-to-video production ready
- **Acrobat AI Assistant**: Document understanding with Firefly
- **Style Kits**: Brand consistency at scale

### Q2 2025 (Planned)

- **Text to Avatar**: Character generation from description
- **Voice-Powered Audio Sync**: Natural language video editing
- **3D to Image**: Product visualization from 3D models

## Best Practices

### Prompt Engineering

**Effective Prompt Structure**:
```
[Subject] + [Action/Setting] + [Style] + [Lighting] + [Camera] + [Quality]

Example:
"Professional product photography, wireless headphones on marble surface,
minimalist Scandinavian style, soft natural window light, 85mm lens,
8K, highly detailed"
```

**Negative Prompts**:
- Use to exclude unwanted elements
- Common: "blurry, distorted, deformed, watermark, signature"

### Workflow Integration

**Ideation Phase**:
- Firefly Boards for concept exploration
- Generate 10-20 variations per concept
- Use Structure Reference for consistency

**Production Phase**:
- Photoshop Generative Fill for refinement
- Illustrator for vector asset creation
- Premiere Pro for video integration

**Asset Management**:
- Tag generated assets in AEM
- Track generative credit usage
- Document prompt patterns

## Competitive Comparison

| Feature | Firefly | Midjourney | DALL-E 3 | Stable Diffusion |
|---------|---------|------------|----------|------------------|
| Commercial Safety | ✅ Licensed | ❌ Web-scraped | ⚠️ Mixed | ❌ Varies |
| Creative Cloud | ✅ Native | ❌ Discord | ⚠️ ChatGPT | ❌ Third-party |
| Vector Output | ✅ Yes | ❌ No | ❌ No | ⚠️ Plugins |
| Video Generation | ✅ Beta | ❌ No | ⚠️ Sora | ⚠️ ComfyUI |
| Custom Training | ✅ Enterprise | ❌ No | ❌ No | ✅ Open |

---

*Source: Adobe Firefly Documentation, Adobe MAX 2024, Adobe Blog*
