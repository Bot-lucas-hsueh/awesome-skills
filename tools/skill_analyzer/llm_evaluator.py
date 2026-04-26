#!/usr/bin/env python3
"""
LLM-as-Judge Evaluator

Uses Claude as a judge to score skills on dimensions not easily captured
by rule-based heuristics:
  - system_prompt_quality    Clarity, specificity, decision frameworks
  - domain_depth             Domain knowledge density, expert-level content
  - workflow_clarity         Actionability, phase-gate structure
  - safety_awareness         Risk documentation, edge-case coverage
  - example_realism          Scenario authenticity and conversational flow
  - behavioral_coherence     Persona consistency (per CharacterBench dimensions)

Implements prompt caching: static rubric stays in the system prompt (cached
with cache_control "ephemeral"); the variable skill text goes in the user turn.

Usage:
    from tools.skill_analyzer.llm_evaluator import evaluate_skill
    result = evaluate_skill(Path("skills/software/backend-developer/SKILL.md"))

    # CLI: python -m tools.skill_analyzer.cli llm-eval --path skills/...
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any, Optional

try:
    import anthropic
    _ANTHROPIC_AVAILABLE = True
except ImportError:
    _ANTHROPIC_AVAILABLE = False

try:
    from .yaml_utils import read_skill
except ImportError:
    from yaml_utils import read_skill  # type: ignore[no-redef]

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

# Evaluation rubric injected into the cached system prompt
_RUBRIC = """
You are a rigorous evaluator of AI agent persona skill files (SKILL.md format).

Each SKILL.md file defines a professional persona that an LLM agent will embody.
You will score the skill across 6 dimensions, each on a scale of 0–10.

## Scoring Dimensions

### 1. system_prompt_quality (0–10)
Evaluate the § System Prompt section:
- 0–3: Missing, vague, or only a role statement ("You are a backend developer")
- 4–6: Has role + some constraints but no decision framework
- 7–8: Has role + decision gates + thinking patterns + communication style
- 9–10: Complete system prompt with code-block example, multi-layered decision framework,
        explicit reasoning style, and behavioral anchors

### 2. domain_depth (0–10)
Evaluate the depth and specificity of domain knowledge:
- 0–3: Generic lists ("write clean code", "follow best practices")
- 4–6: Some domain-specific content but lacks quantified thresholds or frameworks
- 7–8: Concrete frameworks with named methodologies, tools, and metrics
- 9–10: Expert-level content with decision trees, quantified thresholds,
        domain-specific trade-off analysis; would fool a domain expert

### 3. workflow_clarity (0–10)
Evaluate the Standard Workflow section:
- 0–3: Missing or just bullet points without actionability
- 4–6: Has steps but lacks phase gates or completion criteria
- 7–8: Phase-gate structure with [✓ Done] criteria and deliverables
- 9–10: Production-grade workflow with decision branches, time estimates,
        prerequisite checks, and output templates

### 4. safety_awareness (0–10)
Evaluate the Risk Disclaimer and risk-related content throughout:
- 0–3: Generic ("AI may be wrong, verify output") or missing
- 4–6: Has some domain-specific risks but no severity levels or mitigations
- 7–8: 5+ domain-specific risks with severity (High/Med/Low) and mitigations
- 9–10: Comprehensive risk taxonomy with consequences, mitigation playbooks,
        escalation paths, and boundary conditions

### 5. example_realism (0–10)
Evaluate the Scenario Examples section:
- 0–3: Missing, trivial, or obviously artificial
- 4–6: Has examples but they feel generic or don't show the persona's unique value
- 7–8: Realistic scenarios with dialogue flows that showcase domain expertise
- 9–10: Multi-turn conversation examples that demonstrate complex reasoning,
        edge-case handling, and persona-consistent communication style

### 6. behavioral_coherence (0–10)
Evaluate whether the persona is internally consistent throughout the document
(per CharacterBench: identity, knowledge, tone, values, decision style):
- 0–3: Persona is generic, inconsistent, or could apply to any role
- 4–6: Has some personality but it's shallow or contradicts itself
- 7–8: Consistent expert identity with distinct perspective, values, and style
- 9–10: Deeply coherent persona that would produce recognizably different
        outputs than other domain experts; passes the "impersonation test"

## Output Format

Respond with ONLY valid JSON in this exact schema:
{
  "scores": {
    "system_prompt_quality": <int 0-10>,
    "domain_depth": <int 0-10>,
    "workflow_clarity": <int 0-10>,
    "safety_awareness": <int 0-10>,
    "example_realism": <int 0-10>,
    "behavioral_coherence": <int 0-10>
  },
  "weighted_avg": <float>,
  "tier": "<basic|community|expert|exemplary>",
  "strengths": ["<concise strength>", ...],
  "gaps": [{"dimension": "<dim>", "score": <int>, "suggestion": "<action>"}],
  "one_line_summary": "<25 word summary of skill quality>"
}

Compute weighted_avg as:
  (system_prompt_quality * 0.20 + domain_depth * 0.25 + workflow_clarity * 0.15
   + safety_awareness * 0.12 + example_realism * 0.18 + behavioral_coherence * 0.10)

Tier: exemplary ≥ 9.0, expert ≥ 7.0, community ≥ 4.0, basic < 4.0

Be critical. Most skills should score 4–7. Only truly exceptional skills score 9+.
""".strip()


def _build_client() -> Optional[Any]:
    """Return an Anthropic client if the API key is available."""
    if not _ANTHROPIC_AVAILABLE:
        return None
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        return None
    return anthropic.Anthropic(api_key=api_key)


def evaluate_skill(file_path: Path, client: Optional[Any] = None) -> dict[str, Any]:
    """Evaluate a single skill using LLM-as-Judge.

    Returns a dict with scores and feedback. If the Anthropic API is
    unavailable, returns a dict with ``"skipped": True``.
    """
    if client is None:
        client = _build_client()

    if client is None:
        return {
            "skipped": True,
            "reason": "ANTHROPIC_API_KEY not set or anthropic package not installed",
            "path": str(file_path),
        }

    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"error": str(e), "path": str(file_path)}

    # Determine skill identity from path
    parts = file_path.parts
    category = "unknown"
    skill_name = file_path.stem
    if "skills" in parts:
        idx = parts.index("skills")
        if idx + 1 < len(parts):
            category = parts[idx + 1]
        if file_path.name == "SKILL.md" and idx + 2 < len(parts):
            skill_name = parts[idx + 2]

    # Truncate very long skills to keep cost reasonable (first 6 000 chars ≈ ~1 500 tokens)
    skill_text = content[:6000] if len(content) > 6000 else content
    truncated = len(content) > 6000

    user_message = f"""Evaluate the following skill file and return JSON scores.

Skill path: {file_path}
Category: {category}
Skill name: {skill_name}
{"(Note: content truncated to 6 000 chars)" if truncated else ""}

--- BEGIN SKILL.md ---
{skill_text}
--- END SKILL.md ---"""

    try:
        response = client.messages.create(
            model="claude-opus-4-7",
            max_tokens=1024,
            thinking={"type": "adaptive"},
            system=[
                {
                    "type": "text",
                    "text": _RUBRIC,
                    "cache_control": {"type": "ephemeral"},
                }
            ],
            messages=[{"role": "user", "content": user_message}],
        )

        # Extract the text block from the response
        text_content = ""
        for block in response.content:
            if hasattr(block, "text"):
                text_content = block.text
                break

        # Parse JSON from response
        result = json.loads(text_content)
        result["path"] = str(file_path)
        result["skill"] = skill_name
        result["category"] = category
        result["truncated"] = truncated
        result["input_tokens"] = response.usage.input_tokens
        result["output_tokens"] = response.usage.output_tokens
        result["cache_read_tokens"] = getattr(response.usage, "cache_read_input_tokens", 0)
        result["cache_creation_tokens"] = getattr(response.usage, "cache_creation_input_tokens", 0)
        return result

    except json.JSONDecodeError as e:
        return {
            "error": f"JSON parse error: {e}",
            "raw_response": text_content[:500] if text_content else "",
            "path": str(file_path),
        }
    except Exception as e:
        return {"error": str(e), "path": str(file_path)}


def evaluate_all_skills(
    skills_dir: Optional[Path] = None,
    limit: Optional[int] = None,
) -> list[dict[str, Any]]:
    """Evaluate all skills (or up to `limit`) using LLM-as-Judge."""
    if skills_dir is None:
        skills_dir = SKILLS_DIR

    client = _build_client()
    if client is None:
        return [
            {
                "skipped": True,
                "reason": "ANTHROPIC_API_KEY not set or anthropic package not installed",
            }
        ]

    results = []
    skill_paths = sorted(skills_dir.rglob("SKILL.md"))
    if limit:
        skill_paths = skill_paths[:limit]

    for skill_path in skill_paths:
        if any(x in skill_path.parts for x in ["references", "assets", "_common"]):
            continue
        result = evaluate_skill(skill_path, client=client)
        results.append(result)

    return results


def print_eval_summary(results: list[dict[str, Any]]) -> None:
    """Print LLM evaluation summary."""
    try:
        from rich.console import Console
        from rich.table import Table

        console = Console()
        skipped = [r for r in results if r.get("skipped")]
        if skipped:
            console.print(f"[yellow]Skipped {len(skipped)} skills (API unavailable)[/yellow]")
            return

        evaluated = [r for r in results if "scores" in r]
        console.print(f"\n[bold]LLM-as-Judge Evaluation ({len(evaluated)} skills)[/bold]")

        total_cache_read = sum(r.get("cache_read_tokens", 0) for r in evaluated)
        total_cache_creation = sum(r.get("cache_creation_tokens", 0) for r in evaluated)
        console.print(f"  Cache read tokens:     {total_cache_read:,}")
        console.print(f"  Cache creation tokens: {total_cache_creation:,}")

        table = Table(show_header=True)
        table.add_column("Skill")
        table.add_column("Avg")
        table.add_column("Tier")
        table.add_column("Coherence")
        table.add_column("Summary")

        for r in sorted(evaluated, key=lambda x: x.get("weighted_avg", 0), reverse=True)[:20]:
            scores = r.get("scores", {})
            table.add_row(
                r.get("skill", "?"),
                f"{r.get('weighted_avg', 0):.2f}",
                r.get("tier", "?"),
                str(scores.get("behavioral_coherence", "?")),
                r.get("one_line_summary", "")[:50],
            )

        console.print(table)
    except ImportError:
        for r in results:
            if "scores" in r:
                print(f"{r.get('skill')}: {r.get('weighted_avg', 0):.2f} ({r.get('tier')})")
