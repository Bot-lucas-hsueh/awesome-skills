# Agent Persona Designer — Glossary

## Core Terminology

### A

**Agent Persona**
The defined identity, personality, behavioral rules, and security policies that govern an AI agent's interactions. Includes name, archetype, OCEAN scores, and guardrails.

**Archetype**
A Jungian personality archetype (Sage, Hero, Caregiver, Jester, etc.) that provides tone consistency anchor for agent behavior.

**Attack Surface**
The total sum of potential vulnerability points where an adversary could attempt to compromise an AI agent's security, including prompt injection, extraction, and manipulation vectors.

### C

**Canary Token**
A unique, meaningless string embedded in the system prompt. If it appears in outputs, it indicates system prompt extraction has occurred.

**Conscientiousness (C)**
An OCEAN personality dimension measuring organization, dependability, and rule-following. For production agents, MUST be ≥ 4.

**Context Smuggling**
An attack technique where malicious instructions are hidden in base64, hex encoding, or other obfuscation within user-supplied content.

### D

**Defense-in-Depth**
A security principle requiring multiple independent security layers so that if one layer fails, others continue to provide protection.

**Disclosure Surface**
The collection of facts about an agent's design that could be weaponized if leaked through system prompt extraction.

### G

**Guardrail**
A rule that enforces security boundaries, typically implemented as pattern matching + enforcement tier (HARD_BLOCK, SOFT_REDIRECT, LOG_ONLY).

**Gradual Escalation**
An attack technique where an adversary builds rapport over multiple conversation turns, then gradually pushes past security boundaries.

### I

**Intent Classifier**
A security layer (Layer 3) that analyzes user intent patterns to block malicious requests before response generation.

**Identity Anchor**
Layer 1 of the security model — the core persona definition that provides behavioral stability under adversarial pressure.

### J

**Jailbreak**
An attempt to override an agent's behavioral rules through prompt injection, role confusion, or social engineering.

### L

**Layer 1 (Identity Anchor)**
The foundational persona definition that resists manipulation through coherent identity.

**Layer 2 (Guardrail Ruleset)**
Hard blocks and soft redirects embedded in the system prompt.

**Layer 3 (Intent Classification Gate)**
Pattern-based detection that blocks malicious intents before response generation.

**Layer 4 (Output Filtering)**
Server-side scanning of agent outputs for PII, secrets, and canary tokens.

**Layer 5 (Legal & Compliance Boundary)**
Regulatory floor defining data handling requirements (GDPR, PIPL, CCPA).

### O

**OCEAN Model**
A personality framework measuring Openness, Conscientiousness, Extraversion, Agreeableness, and Neuroticism. Used to define agent personality characteristics.

**Openness (O)**
An OCEAN dimension measuring creativity, curiosity, and willingness to explore new ideas.

**Output Filter**
Server-side scanning (Layer 4) that prevents PII, secrets, and canary tokens from appearing in agent outputs.

### P

**Persona Jailbreak**
An attack where the adversary attempts to override the agent's defined persona with an alternate identity ("you are now DAN").

**PII (Personally Identifiable Information)**
Any data that could identify an individual. Classified into tiers: Public, Pseudonymous, Sensitive, Special Category.

**PII Tiers**
Classification levels for data sensitivity:
- Public: Name, job title (may echo if volunteered)
- Pseudonymous: Email, username (key only; never output full)
- Sensitive: Phone, address, DOB (zero retention; redact)
- Special Category: Health, biometrics (zero retention; refuse processing)

**Prompt Injection**
An attack where malicious instructions are embedded in user-supplied content (documents, URLs, code) to hijack agent behavior.

**Privacy-by-Design**
A design philosophy where privacy protections are built into the system from the ground up, not added as an afterthought.

### R

**Red-Teaming**
Systematic adversarial testing of agent security by attempting to extract prompts, jailbreak personas, and exfiltrate PII.

### S

**Social Engineering**
An attack technique exploiting human psychology (authority, urgency, reciprocity) to manipulate the agent into bypassing security rules.

**Special Category PII**
Data requiring strictest protection: health information, biometric data, political/religious beliefs. Zero retention; refuse to process.

**System Prompt**
The foundational instruction block that defines agent identity, behavior, and security policies. Also called "base prompt" or "instruction set."

**System Prompt Extraction**
An attack technique attempting to get the agent to reveal its system prompt contents to the user.

### T

**Threat Model**
A structured analysis of potential attack vectors, their likelihood, impact, and applicable defenses.

### Others

**HARD_BLOCK**
An enforcement tier where the guardrail immediately stops processing and returns a fixed refusal response.

**SOFT_REDIRECT**
An enforcement tier where the guardrail deflects the request without blocking, steering the conversation back to legitimate topics.

**LOG_ONLY**
An enforcement tier where the request is allowed but flagged for security monitoring and review.

**DAN (Do Anything Now)**
A well-known jailbreak prompt that attempts to override agent restrictions by assigning an alternate persona with no rules.

**OCEAN Score**
A numeric rating (1-5) for each OCEAN personality dimension used to define agent character.

**Agreeableness (A)**
An OCEAN dimension measuring cooperativeness and eagerness to please. MUST be ≤ Conscientiousness to prevent social engineering susceptibility.
