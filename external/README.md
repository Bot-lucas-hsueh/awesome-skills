# External — Skill Ecosystem Hub

A curated registry of third-party Claude Code / agent-skill repositories.

`awesome-skills` **does not vendor** these repos. The authoritative source for
every entry here is the upstream project listed in the table; this directory
ships a registry (`sources.yml`) plus a sync script so users can pull the
subset they want into `external/<slug>/` on their own machine.

## Why a registry, not submodules?

- **Zero clone-time overhead** for users who only need our own skills.
- **No license entanglement** — upstream LICENSE files stay with upstream.
- **Fast re-sync** — shallow clones (`--depth=1`) keep disk usage tiny.
- **Opt-in** — users pick the sources they trust; we are a pointer, not a mirror.

## Quick start

```bash
# Clone / fast-forward every source in sources.yml
python3 scripts/sync_external.py --all

# Pull a single source
python3 scripts/sync_external.py --slug anthropics-skills

# List what's registered without touching disk
python3 scripts/sync_external.py --list

# Remove a local clone (upstream is untouched)
python3 scripts/sync_external.py --remove voltagent-awesome-agent-skills
```

Everything below `external/<slug>/` is gitignored — the sync is a local
working copy, not a committed mirror.

## Registered sources

### Individual author skill packs

| Slug | Repo | License | What it is |
|------|------|---------|-----------|
| `mattpocock-skills` | [mattpocock/skills](https://github.com/mattpocock/skills) | MIT | Matt Pocock's opinionated engineering workflow skills: `/tdd`, `/diagnose`, `/zoom-out`, `/grill-with-docs`, `/triage`, `/improve-codebase-architecture`, `/caveman`. Built around the principle "build a reliable feedback loop first." Install: `npx skills@latest add mattpocock/skills`. |

### Official (Anthropic)

| Slug | Repo | License | What it is |
|------|------|---------|-----------|
| `anthropics-skills` | [anthropics/skills](https://github.com/anthropics/skills) | MIT | Anthropic's public Agent Skills repo — document skills, artifact builders, internal workflows. |
| `anthropics-claude-plugins-official` | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | MIT | Anthropic-managed directory of vetted Claude Code plugins (includes `skill-creator`). |
| `anthropics-knowledge-work-plugins` | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | MIT | Anthropic plugins aimed at knowledge workers using Claude Cowork. |

### Community curated lists

| Slug | Stars | Repo | License | What it is |
|------|-------|------|---------|-----------|
| `sickn33-antigravity-awesome-skills` | 35.6k | [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | MIT | 1,400+ installable agentic skills for Claude Code, Cursor, Codex CLI, Gemini CLI, and Antigravity; includes installer CLI and community bundles. |
| `voltagent-awesome-agent-skills` | 19.3k | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | MIT | 1000+ skills from official dev teams and the community; cross-compatible with Claude Code, Codex, Cursor, Gemini CLI. |
| `hesreallyhim-awesome-claude-code` | 41.7k | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | MIT | The de-facto "awesome" list — skills, hooks, slash-commands, orchestrators, plugins. |
| `travisvn-awesome-claude-skills` | 11.9k | [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | MIT | Curated "best of" community skill index (SEO, marketing, design, security, writing, research, testing). |
| `composiohq-awesome-claude-skills` | — | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | MIT | Composio's curation focused on workflow-automation agents. |
| `rohitg00-awesome-claude-code-toolkit` | 1.5k | [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | MIT | Comprehensive toolkit: 135 agents, 35 curated skills, 176+ plugins, 20 hooks, 14 MCP configs, and 26 companion apps. |
| `prat011-awesome-llm-skills` | 1.2k | [Prat011/awesome-llm-skills](https://github.com/Prat011/awesome-llm-skills) | MIT | Curated LLM and AI Agent Skills compatible with Claude Code, Codex, Gemini CLI, and custom agents. |
| `davepoon-buildwithclaude` | 2.8k | [davepoon/buildwithclaude](https://github.com/davepoon/buildwithclaude) | MIT | Single hub for Claude Skills, Agents, Commands, Hooks, Plugins, and Marketplace collections across Claude Code, Claude Desktop, Agent SDK, and OpenClaw. |
| `karanb192-awesome-claude-skills` | 281 | [karanb192/awesome-claude-skills](https://github.com/karanb192/awesome-claude-skills) | MIT | 50+ verified Claude Skills covering TDD, debugging, git workflows, and document processing. |
| `mxyhi-ok-skills` | 311 | [mxyhi/ok-skills](https://github.com/mxyhi/ok-skills) | MIT | Curated AI coding agent skills and AGENTS.md playbooks for Codex, Claude Code, Cursor, OpenClaw, and other SKILL.md-compatible tools. |

### Subagents & orchestration

| Slug | Stars | Repo | License | What it is |
|------|-------|------|---------|-----------|
| `voltagent-awesome-claude-code-subagents` | — | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | MIT | 100+ specialized Claude Code subagents covering development use cases. |
| `wshobson-agents` | — | [wshobson/agents](https://github.com/wshobson/agents) | MIT | Multi-agent orchestration framework for Claude Code. |
| `0xfurai-claude-code-subagents` | — | [0xfurai/claude-code-subagents](https://github.com/0xfurai/claude-code-subagents) | MIT | 100+ production-ready development subagents, domain-expert oriented. |
| `zippoxer-subtask` | 328 | [zippoxer/subtask](https://github.com/zippoxer/subtask) | MIT | Claude Skill that runs tasks using subagents in isolated Git worktrees for safe parallel execution. |

### Specialized domain skills

| Slug | Stars | Repo | License | What it is |
|------|-------|------|---------|-----------|
| `agriculci-daniel-claude-seo` | 5.7k | [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo) | MIT | Universal SEO skill for Claude Code: 19 sub-skills, 12 subagents, 3 extensions; covers technical SEO, E-E-A-T, schema, GEO/AEO, and PDF/Excel reporting. |
| `zubair-trabzada-ai-marketing-claude` | 1.5k | [zubair-trabzada/ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude) | MIT | AI Marketing Suite: 15 marketing skills with parallel subagents for website audit, copy, email sequences, ad campaigns, and competitive intelligence. |
| `agents365-drawio-skill` | 765 | [Agents365-ai/drawio-skill](https://github.com/Agents365-ai/drawio-skill) | MIT | Agent Skill that generates professional draw.io diagrams from natural language and exports to PNG/SVG/PDF. |
| `arpitg1304-robotics-agent-skills` | 187 | [arpitg1304/robotics-agent-skills](https://github.com/arpitg1304/robotics-agent-skills) | MIT | Agent skills for production-grade robotics software with ROS1/ROS2, design patterns, SOLID principles, and testing. |
| `eyadkelleh-awesome-claude-skills-security` | 200 | [Eyadkelleh/awesome-claude-skills-security](https://github.com/Eyadkelleh/awesome-claude-skills-security) | MIT | Security testing toolkit for Claude Code — SecLists wordlists, injection payloads, and expert agents for authorized pentesting, CTFs, and bug bounties. |

### Skill toolkits & frameworks

| Slug | Stars | Repo | License | What it is |
|------|-------|------|---------|-----------|
| `gotalab-cc-sdd` | 3.2k | [gotalab/cc-sdd](https://github.com/gotalab/cc-sdd) | MIT | Spec-Driven Development harness — turns approved specs into long-running autonomous implementations; supports Claude Code, Codex, Cursor, Copilot, Windsurf, OpenCode, and Gemini CLI. |
| `francyjg-agent-skill-creator` | 816 | [FrancyJGLisboa/agent-skill-creator](https://github.com/FrancyJGLisboa/agent-skill-creator) | MIT | Turn any workflow into reusable AI agent skills that install on 14+ tools — Claude Code, Copilot, Cursor, Windsurf, Codex, Gemini, Kiro, and more. |
| `zhu1090093659-spec-driven-develop` | 705 | [zhu1090093659/spec_driven_develop](https://github.com/zhu1090093659/spec_driven_develop) | MIT | Cross-platform skill that turns migration or rewrite requests into a disciplined document-driven workflow — analyze, decompose, track, execute. |

## Proposing a new source

1. Add an entry to [`sources.yml`](./sources.yml) using the schema documented at
   the top of that file.
2. Run `python3 scripts/sync_external.py --slug <your-slug>` to smoke-test the
   clone and confirm the upstream `SKILL.md` / plugin files are readable.
3. Open a PR. Criteria for inclusion:
   - **Scope fit** — skills, subagents, slash-commands, hooks, or plugin
     marketplaces for Claude Code / Anthropic agent runtimes.
   - **Signal** — ≥ 100 GitHub stars **or** official backing from a
     recognised vendor / foundation.
   - **Licensing** — MIT / Apache-2.0 / BSD / similar permissive; AGPL and
     unlicensed repos are declined.
   - **Activity** — at least one commit in the last 12 months.

## Relationship to `skills/` and `benchmarks/`

- `skills/` — **first-party** role-based skills authored in this repo. Subject
  to our quality gates.
- `benchmarks/` — third-party skill sets we evaluate against (aakashg,
  wdavidturner). Vendored for reproducibility of benchmark runs.
- `external/` — **this directory**. Pointers to external projects for
  discoverability and convenience; not vendored, not gated by our CI.

CI exempts `external/` from lint + validation — we do not enforce our style on
upstream projects.
