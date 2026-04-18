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

### Official (Anthropic)

| Slug | Repo | License | What it is |
|------|------|---------|-----------|
| `anthropics-skills` | [anthropics/skills](https://github.com/anthropics/skills) | MIT | Anthropic's public Agent Skills repo — document skills, artifact builders, internal workflows. |
| `anthropics-claude-plugins-official` | [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | MIT | Anthropic-managed directory of vetted Claude Code plugins (includes `skill-creator`). |
| `anthropics-knowledge-work-plugins` | [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | MIT | Anthropic plugins aimed at knowledge workers using Claude Cowork. |

### Community curated lists

| Slug | Repo | License | What it is |
|------|------|---------|-----------|
| `voltagent-awesome-agent-skills` | [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | MIT | 1000+ skills from official dev teams and the community; cross-compatible with Claude Code, Codex, Cursor, Gemini CLI. |
| `hesreallyhim-awesome-claude-code` | [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | MIT | The de-facto "awesome" list — skills, hooks, slash-commands, orchestrators, plugins. |
| `travisvn-awesome-claude-skills` | [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | MIT | Curated "best of" community skill index (SEO, marketing, design, security, writing, research, testing). |
| `composiohq-awesome-claude-skills` | [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | MIT | Composio's curation focused on workflow-automation agents. |

### Subagents & orchestration

| Slug | Repo | License | What it is |
|------|------|---------|-----------|
| `voltagent-awesome-claude-code-subagents` | [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | MIT | 100+ specialized Claude Code subagents covering development use cases. |
| `wshobson-agents` | [wshobson/agents](https://github.com/wshobson/agents) | MIT | Multi-agent orchestration framework for Claude Code. |
| `0xfurai-claude-code-subagents` | [0xfurai/claude-code-subagents](https://github.com/0xfurai/claude-code-subagents) | MIT | 100+ production-ready development subagents, domain-expert oriented. |

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
