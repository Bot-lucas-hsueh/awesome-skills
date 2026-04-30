# awesome-skills Repository — Glossary

## Repository & Skill Structure

**SKILL.md** — The primary file defining a skill's behavior, workflow, and metadata. Follows a 16-section template with H2 headings.

**Skill** — A reusable configuration that provides an AI agent with domain-specific instructions, reference materials, and workflows. The fundamental unit of the awesome-skills repository.

**Category** — A top-level directory grouping related skills (e.g., `software/`, `crafts/`, `medical/`). Used for organizational taxonomy and discovery.

**Subcategory** — A second-level directory within a category (e.g., `software/devops-engineer`, `factory-worker/cnc-operator`).

**Skill Name** — The directory name of a skill. Must be lowercase, hyphen-separated, alphanumeric only, max 40 characters, unique within the repository.

**Frontmatter / YAML Block** — The YAML metadata block at the top of a SKILL.md file containing `name`, `display_name`, `author`, `version`, `quality`, `score`, `difficulty`, `category`, `tags`, `platforms`, and `description`.

**Trigger Word** — A phrase that activates a skill. Listed in the SKILL.md frontmatter and description. Examples: "gerrit permissions", "create skill", "review skill".

## Quality Model

**Exemplary** — Rating tier for skills scoring 9.5–10.0. All quality gates met with exceptional depth and domain coverage.

**Expert** — Rating tier for skills scoring 7.0–9.4. All quality gates met with high-quality domain content.

**Good** — Rating tier for skills scoring 6.0–6.9. Most quality gates met, solid content.

**Basic** — Rating tier for skills scoring 5.0–5.9. Minimum requirements met.

**Quality Gate** — An automated or manual checkpoint that must pass before a skill can be merged. Blocks merge if failed.

**Quality Score / Rubric Score** — A numeric score (0–10) assigned to a skill based on evaluation across weighted dimensions: System Prompt (20%), Domain Knowledge (25%), Workflow (15%), Risk Documentation (10%), Examples/Scenarios (20%), Metadata Completeness (10%).

**Self-Score** — The quality score a skill author assigns their own skill before submission.

## Git Workflow

**Branch Naming Convention** — The standard pattern for naming Git branches:
- Feature: `feature/[skill-name]`
- Bugfix: `fix/[issue-description]`
- Documentation: `docs/[topic]`
- Upgrade: `upgrade/[skill-name]`
- Hotfix: `hotfix/[issue-description]`

**Commit Message Format** — The Conventional Commits standard used in the repository:
```
<type>(<scope>): <subject>

<body>

<footer>
```
Types: `feat`, `fix`, `docs`, `refactor`, `test`, `chore`, `quality`.

**Squash Merge** — A merge strategy that combines all commits in a PR into a single commit on the target branch. Preferred for skill contributions to maintain clean history.

**Atomic Commit** — A commit that makes exactly one logical change. One skill per commit; one logical change per PR.

**PR Template** — A standardized pull request description format ensuring all required information (summary, quality checklist, changes, testing notes) is included.

**CI/CD Pipeline** — Automated workflow triggered on push/PR. Runs linting, link checking, YAML validation, and quality scoring.

## Skill Development

**Pipeline Phase** — A distinct stage in the skill development lifecycle:
- Phase 1: Discovery (issue creation, scope verification)
- Phase 2: Branch (branch creation, template application)
- Phase 3: Development (content writing, section completion)
- Phase 4: Validation (CI checks, rubric scoring, testing)
- Phase 5: Review (PR creation, maintainer review)
- Phase 6: Merge (approval, squash merge)

**16-Section Template** — The required structure for SKILL.md files:
1. System Prompt
2. What This Skill Does
3. Risk Disclaimer
4. Core Philosophy / Guiding Principles
5. Platform Support
6. Professional Toolkit
7. Standards & Reference
8. Standard Workflow
9. Scenario Examples
10. Common Pitfalls & Anti-Patterns
11. Integration with Other Skills
12. Scope & Limitations
13. How to Use This Skill
14. Quality Verification
15. Version History
16. License & Author

**Section §1 (System Prompt)** — The foundational instruction block defining the agent's role, identity, decision framework, thinking patterns, and communication style. Typically 30–50 lines.

**Section §3 (Risk Disclaimer)** — Documentation of potential risks associated with the skill (quality drift, scope creep, broken links, metadata errors, token overflow), their severity, and mitigations.

**Section §7 (Standards & Reference)** — Industry standards, regulatory bodies, professional associations, and official documentation relevant to the skill's domain.

**Section §8 (Standard Workflow)** — Step-by-step operational procedures for common tasks. Structured as numbered steps with tables.

**Section §9 (Scenario Examples)** — Real-world usage scenarios demonstrating how to apply the skill. Includes trigger, reasoning, and outcome.

**Section §10 (Common Pitfalls)** — Anti-patterns and common mistakes with severity ratings and quick fixes.

**References Directory** — A subdirectory within each skill containing domain-specific reference files. Standard files: `07-standards.md`, `08-troubleshooting.md`, `09-glossary.md`, `10-examples.md`.

**Reference Files** — Domain-specific supplementary documents. 07-standards (industry standards), 08-troubleshooting (common issues), 09-glossary (terminology), 10-examples (real-world scenarios).

## Validation & Automation

**yamllint** — A linting tool that validates YAML frontmatter syntax in SKILL.md files.

**markdownlint** — A linting tool that validates Markdown structure, heading hierarchy, and formatting.

**Link Checker / Broken Link Detection** — Automated check verifying all internal and external URLs in skill files return HTTP 200.

**Score Automation** — Scripts or workflows that calculate the rubric score from SKILL.md content.

**Lint Gate** — A CI checkpoint that runs yamllint and markdownlint. Blocks merge if linting fails.

**Rubric Calculator** — The tool or script used to compute the weighted quality score across all dimensions.

**Token Count** — The number of tokens in a SKILL.md. Skills exceeding ~500 tokens may experience slow loads in some AI platforms.

**Traceable Decision** — A merge decision linked to a documented issue, RFC, or PR discussion.

## Semantic Versioning

**Patch Version** — Third component of version number (e.g., `1.0.1` from `1.0.0`). Incremented for bug fixes, typo corrections, minor content corrections.

**Minor Version** — Second component (e.g., `1.1.0` from `1.0.0`). Incremented for new features, content additions, new reference materials.

**Major Version** — First component (e.g., `2.0.0` from `1.0.0`). Incremented for breaking changes, structural restructuring, template changes.

## Maintenance & Lifecycle

**Skill Upgrade** — The process of improving an existing skill's content, adding new capabilities, refreshing outdated information, or bumping the version.

**Skill Migration** — Moving a skill to a new category, renaming it, or adapting it to a new template version.

**Deprecation** — Marking a skill as outdated or superseded. Done via version history, README updates, and potentially a redirect.

**Scope Creep** — When a single skill attempts to cover multiple domains. A blocking anti-pattern; each skill should have a single, focused scope.

**Quality Drift** — The gradual degradation of skill quality over time due to outdated information, broken links, or lowered standards. Mitigated by strict quality gates.

**Regression** — A previously passing quality check that fails after changes. Detected via CI and manual review.

**Reviewer** — A maintainer who evaluates submitted skills against the quality rubric and provides feedback.

**Maintainer** — A repository contributor with merge privileges who approves and merges validated skill contributions.

## Reference File Types

**07-standards.md** — Reference file listing industry standards (ISO, NIST, regulatory bodies), professional associations, and official documentation relevant to the skill's domain.

**08-troubleshooting.md** — Reference file documenting common issues encountered when using the skill, with diagnosis steps and fixes.

**09-glossary.md** — Reference file defining domain-specific terminology for the skill's profession or trade.

**10-examples.md** — Reference file containing detailed real-world scenario examples demonstrating the skill in action.

## Content Anti-Patterns

**Placeholder Content** — Fake or generic text (e.g., "example.com", "Lorem ipsum") that must be replaced with real domain-specific content before merge.

**Placeholder URL** — A fake URL used as a placeholder that must be replaced with actual verifiable resources.

**Score Inflation** — Claiming a higher quality score than the actual content warrants. A high-severity anti-pattern that erodes user trust.

**Commit Overload** — Combining multiple unrelated changes into a single commit or PR. Violates atomic commit principle.

**HTML in YAML** — Using HTML tags within YAML frontmatter blocks. Causes YAML parse failures.

**Generic System Prompt** — An underspecified system prompt (e.g., "You are a helpful assistant") that provides no domain-specific guidance.

**Token Waste** — Placing lengthy content in SKILL.md instead of offloading to reference files, causing slow skill loads.
