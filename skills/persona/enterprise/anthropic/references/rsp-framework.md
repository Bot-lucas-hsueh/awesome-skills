# Responsible Scaling Policy (RSP) Reference

## Overview

Anthropic's Responsible Scaling Policy (RSP) is a framework for managing catastrophic risks from advanced AI systems. First published September 2023, updated to v3.0 February 2026.

## AI Safety Levels (ASL)

Modeled on biosafety levels (BSL) for laboratory safety:

| Level | Risk Profile | Safeguards | Deployment Status |
|-------|--------------|------------|-------------------|
| **ASL-1** | Minimal risk; narrow/smaller models | Standard software security | Unrestricted |
| **ASL-2** | Early signs of hazardous capabilities; general-purpose models | Automated monitoring; security reviews | Standard deployment with monitoring |
| **ASL-3** | Models could significantly accelerate misuse or show autonomous behaviors | Strict security; access controls; red-teaming; conditional deployment | Deployment only if safeguards verified |
| **ASL-4** | Catastrophic risk potential from misuse or autonomous action | Nation-state-level security; external oversight; possible pause | Conditional; may require pause |
| **ASL-5+** | Speculative; transformative AI | Currently undefined; requires unsolved research | Undefined |

## Current Model Classifications

| Model | ASL Classification | Notes |
|-------|-------------------|-------|
| Claude 3 family | ASL-2 | Standard deployment with monitoring |
| Claude Opus 4 | ASL-3 | Additional safeguards required |
| Future models | TBD | Evaluated before deployment |

## If-Then Commitments

Core structure of RSP:
- **IF** model reaches capability threshold X
- **THEN** implement safeguard Y before training/deploying

This creates accountability for safety investment proportional to capability.

## RSP v3.0 Changes (Feb 2026)

Key updates:
- Separates Anthropic's internal commitments from industry-wide recommendations
- Addresses collective action problem (catastrophic risk depends on all frontier developers)
- Removes perverse incentives that discouraged declaring capability thresholds
- Emphasizes that overall risk depends on least responsible actor

## Evaluation Framework

Capability categories evaluated:
- **Biological capabilities** — Could model assist with bioweapon development?
- **Cyber capabilities** — Could model enable significant cyberattacks?
- **Autonomous Replication and Adaptation (ARA)** — Could model self-replicate and adapt?
- **Persuasion/Deception** — Could model manipulate at scale?
- **Chemical/Radiological/Nuclear (CBRN)** — Could model assist with CBRN threats?

## Long-Term Benefit Trust (LTBT)

Governance structure ensuring RSP adherence:
- 5 financially disinterested trustees
- Authority to select/remove portion of Board (growing over time to majority)
- Ensures mission alignment over financial pressure
- Works alongside Public Benefit Corporation structure

## Key Personnel

- **Holden Karnofsky**: Leads RSP development (husband of President Daniela Amodei)
- **Responsible Scaling Officer**: Mandatory role per RSP
- **Safety teams**: Conduct evaluations and red-teaming

## Industry Impact

RSP has influenced:
- California SB-53 (frontier AI regulation)
- New York RAISE Act
- EU AI Act provisions
- 11+ companies adopting similar frameworks
- OpenAI Preparedness Framework
- Google DeepMind Frontier Safety Framework
