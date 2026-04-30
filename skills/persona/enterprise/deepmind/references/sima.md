# SIMA Deep Dive

## Overview

SIMA (Scalable Instructable Multiworld Agent) is DeepMind's generalist AI agent for following natural language instructions in diverse 3D virtual environments and video games.

---

## Motivation

### The Embodied AI Challenge

Traditional game AI:
- Hand-crafted rules or scripts
- Environment-specific (different AI for each game)
- No natural language understanding
- Brittle to environmental changes

Human gameplay:
- Follows natural language instructions
- Generalizes across games
- Learns from observation and trial
- Adapts to new situations

**Goal**: Build an AI that plays games like humans do — following instructions, learning from observation, generalizing across environments.

---

## SIMA 1 (March 2024)

### Design Principles

1. **No API access**: Only pixels, like humans
2. **No internal game state**: No privileged information
3. **Keyboard/mouse interface**: Same controls as humans
4. **Cross-game generalization**: Train on multiple games, test on new ones
5. **Natural language**: Follow instructions in plain English

### Architecture

```
Input: (RGB frame, Language instruction)
              ↓
    ┌─────────────────┐
    │  Vision Encoder │  CNN or Vision Transformer
    │                 │  Processes visual observations
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │  Language Encoder│ Transformer encoder
    │                  │ Encodes instruction semantics
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │  Fusion Module  │ Cross-modal attention
    │  (Perceiver)    │ Combines vision + language
    └────────┬────────┘
             ↓
    ┌─────────────────┐
    │  Policy Network  │ Transformer decoder
    │                  │ Outputs action distribution
    └────────┬────────┘
             ↓
Output: Action vector (keyboard keys, mouse movement, clicks)
```

### Training Data

**Data Collection:**
- Human players follow language instructions
- Screen recording + action logging
- Paired (observation, instruction, action) triples

**Environments:**
- 9 diverse 3D environments:
  - Minecraft (open-world crafting)
  - No Man's Sky (space exploration)
  - Goat Simulator 3 (chaotic physics)
  - Teardown (destructible environments)
  - Unity ML-Agents (custom environments)
  - And others

**Skills:**
- ~600 distinct skills:
  - Navigation: "turn left", "go to the red house"
  - Interaction: "open the door", "pick up the key"
  - Menu: "open map", "open inventory"
  - Object manipulation: "place block", "craft item"

### Training

```python
# Simplified training objective

# Vision encoding
visual_features = vision_encoder(rgb_frame)  # [B, T, D]

# Language encoding
language_features = language_encoder(instruction)  # [B, D]

# Cross-modal fusion
fused = perceiver_fusion(
    inputs=visual_features,
    latents=language_features
)  # [B, T, D]

# Action prediction
action_logits = policy_head(fused)  # [B, T, A]

# Loss: Behavior cloning on human demonstrations
loss = cross_entropy(action_logits, human_actions)
```

### Performance

| Task Type | Success Rate | Notes |
|-----------|--------------|-------|
| Simple navigation | ~60% | "turn left", "walk forward" |
| Object interaction | ~45% | "pick up the key" |
| Complex multi-step | ~31% | "find the red house and enter" |
| Human baseline | ~71% | Reference performance |

**Key Finding:** SIMA 1 learned pixel-to-action mapping but lacked deep reasoning and planning capabilities.

---

## SIMA 2 (November 2025)

### Key Advance: Gemini Integration

SIMA 2 integrates Gemini as the reasoning engine:

```
SIMA 2 Architecture:

Observation + Instruction
           ↓
    ┌──────────────┐
    │   Gemini     │ 2.5 Flash Lite
    │  Reasoning   │ High-level planning
    │   Engine     │ Goal decomposition
    └──────┬───────┘
           ↓
    Verbal plan: "I need to: 1) Find the red house
                  2) Approach the door
                  3) Press E to enter"
           ↓
    ┌──────────────┐
    │   SIMA       │ Low-level control
    │  Controller  │ Motor skills from SIMA 1
    │              │ Vision-language-action
    └──────┬───────┘
           ↓
    Actions executed in environment
           ↓
    Experience stored for self-improvement
```

### New Capabilities

| Capability | SIMA 1 | SIMA 2 |
|------------|--------|--------|
| Reasoning | Pattern matching | Gemini-powered planning |
| Explanation | None | Verbal explanation of actions |
| Multi-step planning | Limited | Hierarchical planning |
| Self-improvement | No | Yes, from experience |
| User interaction | Commands only | Conversational |

### Multimodal Instructions

SIMA 2 accepts diverse instruction types:

```
Instruction Types:
├── Text: "Build a shelter"
├── Sketch: Hand-drawn map on screen
├── Emoji: 🔥 (find fire/campfire)
├── Gesture: Pointing at object
└── Multi-turn conversation

Example interaction:
User: "Go to that house" [draws circle on screen]
SIMA 2: "I see you've highlighted the blue house on the hill. 
         I'll navigate there now."
[navigates to blue house]
SIMA 2: "I've reached the blue house. What would you like me to do?"
User: "Go inside and find the key"
SIMA 2: "I'll enter the house and search for a key. Let me check 
         the rooms systematically..."
```

### Performance Evolution

| Metric | SIMA 1 | SIMA 2 | Human |
|--------|--------|--------|-------|
| Complex task success | ~31% | ~65% | ~75% |
| Novel environment transfer | Limited | Strong | N/A |
| Reasoning tasks | Poor | Good | Excellent |
| User satisfaction | Moderate | High | N/A |

### Training Enhancements

```
SIMA 2 Training:

1. Human Demonstrations
   ├── Same as SIMA 1 (pixel-action pairs)
   └── Plus: Human verbal explanations

2. Gemini-Generated Annotations
   ├── Automatic instruction labeling
   ├── Plan generation for demonstrations
   └── Self-play with language feedback

3. Self-Improvement Loop
   ├── Agent explores environment
   ├── Gemini evaluates outcomes
   ├── Successful strategies reinforced
   └── Failed strategies avoided
```

---

## Technical Details

### Action Space

**Keyboard:**
- WASD movement (8 directions)
- Space (jump)
- E (interact)
- Number keys (inventory slots)
- Others as needed per game

**Mouse:**
- Delta x, y (camera movement)
- Left click
- Right click
- Scroll wheel

**Total action space:** ~50 discrete/continuous dimensions

### Observation Space

```
Visual input:
├── RGB frames: 224×224 or 320×240
├── Frame rate: ~10 FPS for decision-making
├── Temporal stacking: Last 4 frames
└── No access to: depth, segmentation, game state

Language input:
├── Instruction embedding
├── Conversation history (SIMA 2)
└── Task context
```

### Generalization Testing

| Test Type | Environments |
|-----------|--------------|
| Training | Minecraft, No Man's Sky, Goat Simulator, etc. |
| Zero-shot | Minedojo (Minecraft variant), ASKA (survival game) |
| Fine-tuning | Custom Unity environments |

**SIMA 2 Zero-Shot Results:**
- Minedojo: Successfully adapted despite different interface
- ASKA: Viking survival game, learned resource gathering
- Performance gap vs. training environments: ~10% (vs. ~40% for SIMA 1)

---

## Limitations

| Limitation | Description |
|------------|-------------|
| Long-term memory | Struggles with very long-horizon tasks (>100 steps) |
| Precision control | Fine motor skills limited (e.g., precise aiming) |
| Multi-agent coordination | Limited theory of mind for other agents |
| Physical world | Not yet deployed to real robots |
| Reasoning depth | Complex puzzles still challenging |

---

## Applications Beyond Gaming

### Robotics Pathway

SIMA is viewed as a stepping stone to general-purpose robots:

```
Simulation → Reality Pipeline:

1. Learn in diverse simulated environments (SIMA)
2. Develop generalizable skills and reasoning
3. Transfer to physical robot embodiment
4. Sim-to-real adaptation
5. Real-world deployment

Challenges:
├── Physics gap: Simulation ≠ Reality
├── Observation gap: Pixels vs. sensors
├── Action gap: Keyboard vs. motors
└── Safety: Real-world consequences
```

### Training Data for Robotics

- SIMA provides unlimited training data in simulation
- Natural language supervision for robot tasks
- Cross-environment generalization reduces sim-to-real gap

---

## Comparison to Other Embodied AI

| System | Approach | Strengths |
|--------|----------|-----------|
| **SIMA** | Pixel → Language → Action | True generalization, no APIs |
| **Minecraft agents** | Programmatic APIs | Higher performance on specific tasks |
| **RT-2** | Vision-language-action | Direct robot control |
| **Voyager** | Code generation | Compositional skill learning |

---

## Key Insights

1. **Pixels-only is possible**: No API access needed for competent agents
2. **Language is the interface**: Natural language enables flexible instruction
3. **Cross-game training helps**: Diversity improves generalization
4. **Reasoning matters**: SIMA 2 shows planning dramatically improves performance
5. **Conversational agents**: Interactive dialogue improves usability

---

## Future Directions

- Long-horizon memory architectures
- Multi-agent collaboration
- Real robot deployment
- User personalization
- Creative task performance

---

## Citations

**SIMA 1:**
```
DeepMind Blog (2024). SIMA: A generalist AI agent for 3D virtual 
environments. https://deepmind.google/blog/sima/
```

**SIMA 2:**
```
DeepMind Blog (2025). SIMA 2: An agent that plays, reasons, and 
learns with you in virtual 3D worlds.
https://deepmind.google/blog/sima-2/
```

---

## Key Quote

> "SIMA 2 is a step change and improvement in capabilities over SIMA 1. 
> It's a more general agent. It can complete complex tasks in previously 
> unseen environments. And it's a self-improving agent."  
> — Joe Marino, Senior Research Scientist, DeepMind
