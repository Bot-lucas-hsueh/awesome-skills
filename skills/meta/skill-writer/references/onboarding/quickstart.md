# 30-Second Quick Start

> Create your first skill in under 5 minutes

---

## The Absolute Minimum

A skill needs only **one file**: `SKILL.md`

### Step 1: Create the File

Create `SKILL.md` with this content:

```markdown
---
name: hello-world
description: "Simple greeting skill. Use when: user wants a greeting."
---

# Hello World Skill

## What I Do
I provide friendly greetings.

## Usage Examples
- "Say hello"
- "Greet me"

## How to Use Me
1. User asks for a greeting
2. I respond with a friendly message
```

### Step 2: Done! ✅

That's it. You have a working skill.

**Time taken:** ~30 seconds

---

## Test It Immediately

Ask the AI:
> "Use the hello-world skill to greet me"

Expected response:
> "Hello! 👋 Welcome! How can I help you today?"

---

## What Just Happened?

### The Metadata Block
```yaml
---
name: hello-world              # Unique identifier
description: "..."             # When to use this skill
---
```

This tells the AI:
- What this skill is called
- When to activate it

### The Content
The markdown after `---` is instructions for the AI.

---

## Make It Better (Optional)

Add one capability:

```markdown
---
name: hello-world
description: "Simple greeting skill. Use when: user wants a greeting or current time."
---

# Hello World Skill

## Capabilities
✅ Provide friendly greetings
✅ Tell current time

## Usage Examples
- "Say hello"
- "What time is it?"

## How to Use Me
1. Identify what user wants (greeting or time)
2. Provide appropriate response
3. Be friendly and helpful
```

---

## Next Steps

Ready for more? Choose your path:

| Path | Time | Goal |
|------|------|------|
| **First Real Skill** | 30 min | Create PDF rotator skill |
| **Standard Workflow** | 1-2 hrs | Production-quality skill |
| **Concepts** | 15 min | Understand why skills work |

---

**Go deeper:**
→ First Real Skill: first-skill.md  
→ Why Skills Work: ../concepts/what-is-skill.md
