# Enterprise Skill Development Notes

Planning and analysis documents used while building out the
`skills/enterprise/` tree. These are **not skills** — they are internal
design notes about industry coverage, talent profiles, and methodology
research.

They were previously parked at `skills/enterprise/*.md`, which caused
`validate_skills.py` to treat them as malformed flat skills (no frontmatter).
Moved here in pass 4 so the skill validator can run cleanly.

## Files

| Doc | Topic |
|-----|-------|
| AI-COMPANIES-ANALYSIS.md | Scan of the AI-industry players worth modelling |
| BATCH-CREATE-SCRIPT.md | Notes on the batch generation workflow |
| ENTERPRISE-SKILL-DEVELOPMENT.md | Core methodology for company-role skills |
| GAMING-INDUSTRY-EXTENSION.md | Proposal to expand gaming coverage |
| INDUSTRY-ANALYSIS-AND-ROADMAP.md | Coverage roadmap |
| MISSING-INDUSTRIES-ANALYSIS.md | Gaps vs. industry benchmarks |
| NEW-SKILLS-SUMMARY.md | Round-up of recently added enterprise skills |
| NICHE-UNIQUE-METHODOLOGIES.md | Methodology patterns worth preserving |
| QUICK-REFERENCE.md | Cheat sheet for enterprise skill structure |
| SENSITIVE-INDUSTRIES-OUTLINE.md | Handling sensitive / regulated sectors |
| TOP-INDUSTRIES-METHODOLOGY-ANALYSIS.md | Analysis of dominant methodologies |
| TOP-TALENT-PROFILES-EXTENDED.md | Extended talent profile list |
| TOP1-ENTERPRISE-MATRIX.md | First-tier enterprise matrix |
| TOP2-ENTERPRISE-ROADMAP.md | Second-tier roadmap |
| WORKER-RIGHTS-METHODOLOGIES.md | Labour-relations methodology notes |

## Relationship to `skills/`

Everything actionable from these notes is already reflected in concrete
`SKILL.md` files under `skills/enterprise/`. Treat these docs as background;
no runtime agent should load them.
