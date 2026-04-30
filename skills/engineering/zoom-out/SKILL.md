---
name: zoom-out
kind: workflow
version: 1.0.0
tags:
  - domain: engineering
  - subtype: zoom-out
  - methodology: codebase-navigation
description: "Codebase orientation skill: navigate unfamiliar code by ascending abstraction layers to map modules, callers, and domain vocabulary. Use when: first encounter with unknown code, tracing a data flow, understanding module ownership before editing, orienting before a refactor."
license: MIT
metadata:
  author: theNeoAI <lucas_hsueh@hotmail.com>
  inspired_by: mattpocock/skills
---

# Zoom Out

## One-Liner

When lost in code detail, go up a layer of abstraction — map all relevant modules and callers using the project's own vocabulary before touching anything.

---

## § 1 · Core Philosophy

Implementation details are the lowest layer of knowledge. When you are lost in them, the fastest path forward is not to read more code at the same level — it is to **ascend** until you can see the module boundaries, the data flow, and the domain terms the project actually uses.

A zoom-out produces a **map**, not a reading. The map tells you:
- What modules own what behavior
- Where the seams are (where behavior can shift without editing in place)
- What the project calls things (canonical vocabulary that later prompts should reuse)

---

## § 2 · Workflow

### Step 1 — Read Domain Context First

Before exploring code, look for existing orientation documents:

1. `CONTEXT.md` — domain glossary and canonical terms
2. `README.md` or `docs/` — high-level architecture
3. ADR files (`docs/adr/`, `decisions/`) — past architectural decisions
4. `AGENTS.md` or `SKILL.md` — any agent-specific context

If these exist, read them **before** opening source files. They compress hours of reading into minutes.

### Step 2 — Identify the Entry Point

For the area you need to understand, find the highest-level caller:

- For a web request: the router or controller
- For a CLI: the top-level command handler
- For a library: the public API surface (`index.ts`, `__init__.py`, `lib.rs`)
- For a background job: the scheduler or queue consumer

### Step 3 — Map One Layer at a Time

Starting from the entry point, map **one call level at a time**:

```
Entry point
  └── Module A  (owns: X, Y)
        └── Module B  (owns: Z)
              └── Module C  (owns: persistence)
  └── Module D  (owns: validation)
```

For each module, note:
- What it **owns** (single responsibility)
- What it **calls** (dependencies)
- What it **exposes** (public interface)

Stop when you reach the level relevant to your task — you do not need to map the entire codebase.

### Step 4 — Collect Domain Vocabulary

As you map, note every domain-specific term you encounter:
- Entity names (Order, Account, Shipment)
- Action names (fulfill, provision, reconcile)
- State names (pending, in-flight, settled)

These are the **canonical terms** you must use in all subsequent prompts and code. Using non-canonical terms causes agents to introduce inconsistencies.

### Step 5 — Produce the Map

Output a structured summary:

```
## Module Map: <area>

Entry: <file or function>
Domain terms: <list>

Modules:
- <name>: owns [X, Y] | calls [A, B] | public interface: <description>
- ...

Key seams (where behavior can be changed without editing in place):
- <description>

Open questions:
- <anything that needs clarification before editing>
```

---

## § 3 · Signs You Need This Skill

- "I'm not sure which file owns this behavior"
- "I keep finding circular dependencies when I try to trace the flow"
- "The agent keeps using the wrong terminology"
- "I want to refactor but I don't know where the seams are"
- "I need to add a feature but I don't know which module it belongs in"

---

## § 4 · When to Use This Skill

**Use when:**
- Starting work in an unfamiliar part of the codebase
- Before any significant refactor
- Before designing a new feature that touches existing modules
- When an agent has been producing inconsistent terminology

**Do NOT use when:**
- The area is already well-understood (skip the overhead)
- The codebase is small enough to hold entirely in context

---

## § 5 · Relationship to Other Skills

| Skill | When to reach for it |
|-------|---------------------|
| `tdd-workflow` | After zoom-out — you know the interfaces, start writing tests |
| `debug-diagnose` | After zoom-out — you have the map to place your feedback loop |
| `architecture-review` | After zoom-out reveals shallow modules or unclear ownership |
| `grill-with-docs` | After zoom-out — validate your understanding against domain docs |
