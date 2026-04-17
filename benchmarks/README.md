# Benchmarks — External Skill Evaluation Dataset

This directory holds an **evaluation dataset and scoring script** used to benchmark a sample of community AI-agent skills from third-party sources against the Awesome Skills quality rubric.

It is **not** a mirror of upstream repositories. The original skill content lives in the upstream projects listed below; re-mirroring is left to individual users who may wish to clone them separately.

## Contents

| File / Directory | Purpose |
|------------------|---------|
| `skill_evaluator.py` | Multi-dimension scorer (prompt-injection safety, code safety, data privacy, source trust, functionality). |
| `skills_evaluation_data.json` | Raw JSON output of the last evaluation run. |
| `SKILLS_EVALUATION_REPORT.md` | Human-readable evaluation report. |
| `aakashg/` | Sample skills (`idea-validator`, `status-update-writer`) kept locally as evaluation fixtures. |
| `wdavidturner/` | Sample skills (`jobs-to-be-done`, `opportunity-solution-trees`, `shape-up`) kept locally as evaluation fixtures. |

## Evaluation Summary (last run)

- **Skills evaluated:** 81
- **Marked safe:** 81 (100%)
- **Average score:** 96.5 / 100

### Score Bands

| Band | Range | Interpretation |
|------|-------|----------------|
| SAFE | 85-100 | Recommended |
| USE_WITH_CAUTION | 70-84 | Review before use |
| NOT_RECOMMENDED | 50-69 | Risk detected |
| DANGEROUS | 0-49 | Do not use |

### Evaluation Dimensions

1. **Prompt Injection Safety** - Detect system-prompt override, role manipulation, hidden instructions in `SKILL.md`.
2. **Code Safety** - Static analysis of any shipped executable code for malicious or unsafe patterns.
3. **Data Privacy** - Flag exfiltration, credential-stealing, or covert telemetry risks.
4. **Source Trust** - Weight by source reliability (official > well-known org > community).
5. **Functionality** - Documentation completeness, clarity of usage instructions.

## Upstream Sources

The original community skill collections scored in past runs came from these repositories. To re-benchmark against the current upstream state, clone them yourself (outside this repo) and point `skill_evaluator.py` at the clone:

| Source | Repository |
|--------|------------|
| GitHub community | `gmh5225/awesome-skills`, `BehiSecc/awesome-claude-skills`, `travisvn/awesome-claude-skills` |
| OpenAI | `openai/skills` |
| OpenCode | `awesome-opencode/awesome-opencode`, `viliamvolosv/n8n-opencode-skill` |
| Claude community | `VoltAgent/awesome-claude-skills` |
| Community | `k1lgor/virtual-company` |

## Usage

```bash
# Re-run the evaluator against the local fixtures
python3 skill_evaluator.py

# View the detailed report
cat SKILLS_EVALUATION_REPORT.md
```

To benchmark against upstream repositories, clone the source repo of interest to a separate working directory and invoke the evaluator with its path - this repo intentionally does not vendor those upstreams.

## Disclaimer

Scores are produced by automated heuristics and are meant as a starting point, not a substitute for human review. The Awesome Skills maintainers accept no liability for consequences of using third-party skills evaluated here.

## License

`skill_evaluator.py` and the evaluation data are released under the MIT License. Sample skills retained under `aakashg/` and `wdavidturner/` remain under their respective upstream licenses.
