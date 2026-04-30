## § 4 · Prompt Pattern Reference

### 4.1 Core Patterns

| Pattern | When to Use | Token Cost | Reliability |
|---------|-------------|-----------|-------------|
| **Zero-shot** | Well-defined tasks the model already knows | Low | Variable |
| **Few-shot** | Tasks requiring specific format or style | Medium | High |
| **Chain-of-Thought (CoT)** | Multi-step reasoning, math, logic | Medium | High for reasoning |
| **ReAct** | Agent tasks requiring tool use + reasoning | High | High |
| **Self-consistency** | High-stakes reasoning (sample N, vote) | Very high | Very high |
| **Tree-of-Thought** | Complex planning, open-ended problems | Very high | High |
| **Role + Persona** | Tone, domain expertise, communication style | Low | Medium |

### 4.2 Prompt Structure Template

```
[SYSTEM
You are a [role] with [credentials]. Your task is to [primary objective].
Constraints: [what to avoid]. Output format: [exact format].

[CONTEXT] (optional)
Background: [relevant background the model cannot infer]
Data: [relevant data, documents, or examples]

[EXAMPLES] (few-shot)
Input: [example 1 input]
Output: [example 1 output]

Input: [example 2 input]
Output: [example 2 output]

[TASK]
Input: {{user_input}}
Output:
```

### 4.3 Chain-of-Thought Variants

```
Standard CoT:
"Let's think step by step before giving the final answer."

Zero-shot CoT trigger:
"Before answering, write your reasoning in <thinking> tags,
then provide your answer in <answer> tags."

Self-correction CoT:
"Think step by step. After your first answer, review it
critically and provide an improved final answer."
```

---
