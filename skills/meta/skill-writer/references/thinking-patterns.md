# Thinking Patterns Reference

## Pattern 1: Structure-First Design

**When to Use**: Before writing any content

**Process**:
```
1. SELECT TIER
   └── Lite (50-150 lines) / Standard (150-500) / Enterprise (500-1500)

2. DESIGN SYSTEM PROMPT
   └── §1.1 Identity & Worldview
   └── §1.2 Decision Framework
   └── §1.3 Thinking Patterns

3. MAP DOMAIN KNOWLEDGE
   └── Key methodologies
   └── Specific data points
   └── Tool specifications

4. PLAN WORKFLOW
   └── 4-5 phases
   └── Done/Fail criteria
   └── Gates between phases

5. DESIGN EXAMPLES
   └── 5 scenarios
   └── Realistic contexts
   └── Specific data

6. PLAN PROGRESSIVE DISCLOSURE
   └── What stays in SKILL.md
   └── What goes to references/
```

## Pattern 2: Data-Driven Content

**When to Use**: Throughout content creation

**Rules**:
```
FORBIDDEN (Generic):
├── "professional"
├── "expert"
├── "best practices"
├── "industry leader"
├── "years of experience"
└── "high quality"

REQUIRED (Specific):
├── Company: "McKinsey & Company, $15B revenue, 30K employees"
├── Methodology: "McKinsey 7-S Framework, 7 elements, 32-step assessment"
├── Tool: "OpenAI GPT-4o, 128K context, $5/1M tokens input"
├── Benchmark: "16.7% error reduction, 23% efficiency gain"
└── Metric: "Text≥8.0, Runtime≥8.0, Variance<1.0"
```

## Pattern 3: Progressive Disclosure Architecture

**When to Use**: Organizing all content

**Structure**:
```
SKILL.md (< 300 lines)
├── One-liner description
├── System Prompt (§1.1/1.2/1.3)
├── Problem signature (brief)
├── Domain knowledge (summary)
├── Workflow (phases table)
├── Examples (index)
└── Anti-patterns (summary)

references/ (3000+ lines)
├── Detailed SOPs
├── Full examples (5 scenarios)
├── Deep domain dives
├── Complete risk docs
└── Extended patterns
```

## Pattern 4: Evaluator-Driven Quality

**When to Use**: Validating completed skill

**Checklist**:
```
Text Quality (50%):
├── [ ] System Prompt: §1.1/1.2/1.3 present
├── [ ] Domain Knowledge: Specific data verified
├── [ ] Workflow: 4-5 phases with Done/Fail
├── [ ] Error Handling: Anti-patterns documented
├── [ ] Examples: 5+ detailed scenarios
└── [ ] Metadata: Complete YAML

Runtime Quality (50%):
├── [ ] Role immersion: Clear identity
├── [ ] Framework execution: Decision hierarchy works
├── [ ] Output actionability: Concrete steps
├── [ ] Knowledge accuracy: Data verified
├── [ ] Long-conversation stability: Consistent
└── [ ] Resilience: Error handling tested

Certification:
├── [ ] Text Score ≥ 8.0
├── [ ] Runtime Score ≥ 8.0
└── [ ] Variance < 1.0
```

## Pattern 5: Example-Rich Documentation

**When to Use**: Demonstrating correct usage

**Requirements**:
```
Each Example Must Have:
├── Realistic context (industry, situation)
├── Specific user input (exact trigger)
├── Detailed expert response
├── Concrete outputs (data, formats)
└── Success indicators

Coverage Requirements:
├── Minimum 5 examples
├── Different use cases
├── Edge cases included
├── Common pitfalls shown
└── Best practices demonstrated
```
