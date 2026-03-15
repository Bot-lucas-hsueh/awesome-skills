#!/usr/bin/env python3
"""
Skill Scorer - 6-Dimension Quality Scoring Engine

Based on skill-writer/references/standards.md §7.1 Quality Rubric

Scoring Dimensions:
- System Prompt Depth (20%)
- Domain Knowledge Density (25%)
- Workflow Actionability (15%)
- Risk Documentation (10%)
- Example Quality (20%)
- Metadata Completeness (10%)
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Any

# Add parent to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

# Scoring weights from standards.md §7.1
WEIGHTS = {
    "system_prompt": 0.20,
    "domain_knowledge": 0.25,
    "workflow": 0.15,
    "risk_documentation": 0.10,
    "example_quality": 0.20,
    "metadata": 0.10,
}

# 16 standard sections
STANDARD_SECTIONS = [
    "System Prompt",
    "What This Skill Does",
    "Risk Disclaimer",
    "Core Philosophy",
    "Platform Support",
    "Professional Toolkit",
    "Standards & Reference",
    "Standard Workflow",
    "Scenario Examples",
    "Common Pitfalls",
    "Integration with Other Skills",
    "Scope & Limitations",
    "How to Use This Skill",
    "Quality Verification",
    "Version History",
    "License & Author",
]


def parse_frontmatter(content: str) -> Tuple[Optional[Dict[str, str]], str]:
    """Extract YAML frontmatter and body from markdown content."""
    if not content.startswith("---"):
        return None, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content

    fm_raw = parts[1]
    body = parts[2]
    fm = {}

    for line in fm_raw.splitlines():
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            key, _, val = line.partition(":")
            val = val.strip().strip('"').strip("'")
            fm[key.strip()] = val

    return fm, body


def count_h2_sections(body: str) -> int:
    """Count ## level headings in markdown body."""
    return len(re.findall(r"^##\s+\S", body, re.MULTILINE))


def has_section(body: str, section_name: str) -> bool:
    """Check if a section exists in the body."""
    pattern = rf"^##\s+.*{re.escape(section_name)}"
    return bool(re.search(pattern, body, re.MULTILINE | re.IGNORECASE))


def count_code_blocks(body: str) -> int:
    """Count fenced code blocks."""
    return len(re.findall(r"^```", body, re.MULTILINE))


def count_tables(body: str) -> int:
    """Count markdown tables."""
    return len(re.findall(r"^\|", body, re.MULTILINE))


def analyze_system_prompt(body: str) -> float:
    """Score System Prompt depth (0-10)."""
    score = 0

    # Check for §1 System Prompt section (handles ## 1. System Prompt, ## System Prompt, ## §1 System Prompt, etc.)
    if not has_section(body, "System Prompt"):
        return 1.0  # Basic: missing section

    # Extract System Prompt section content - handle numbered sections like ## 1. System Prompt
    sp_match = re.search(
        r"^##\s+(?:\d+\.|\§\d+)?\s*System Prompt.*?\n(.*?)(?=^##\s|\Z)",
        body,
        re.MULTILINE | re.DOTALL,
    )
    if not sp_match:
        return 2.0

    sp_content = sp_match.group(1)

    # Check for role definition
    if re.search(r"You are a|Identity:|Expert in", sp_content, re.IGNORECASE):
        score += 2

    # Check for decision framework (gate questions)
    if re.search(r"Gate|Decision|Question|Before", sp_content, re.IGNORECASE):
        score += 2

    # Check for thinking patterns
    if re.search(r"Thinking Patterns|Thinking|Dimension|Perspective", sp_content, re.IGNORECASE):
        score += 2

    # Check for communication style
    if re.search(r"Communication Style|Style|Tone", sp_content, re.IGNORECASE):
        score += 1

    # Check for code block (actual prompt example)
    if "```" in sp_content:
        score += 2

    # Length check - should be substantial
    if len(sp_content.splitlines()) > 20:
        score += 1

    return min(score, 10)


def analyze_domain_knowledge(body: str) -> float:
    """Score Domain Knowledge Density (0-10)."""
    score = 0

    # Check for frameworks (tables or lists with specific content)
    table_count = count_tables(body)
    if table_count >= 3:
        score += 3
    elif table_count >= 1:
        score += 1

    # Check for specific metrics or thresholds
    if re.search(r"\d+%|target|threshold|metric", body, re.IGNORECASE):
        score += 2

    # Check for domain-specific terminology
    domain_terms = len(re.findall(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+){1,3}\b", body))
    if domain_terms > 20:
        score += 3
    elif domain_terms > 10:
        score += 2

    # Check for decision frameworks
    if re.search(r"Decision|Tree|Matrix|Framework", body, re.IGNORECASE):
        score += 2

    return min(score, 10)


def analyze_workflow(body: str) -> float:
    """Score Workflow Actionability (0-10)."""
    score = 0

    # Check for Standard Workflow section
    if not has_section(body, "Standard Workflow") and not has_section(body, "Work Process"):
        return 2.0

    # Extract workflow section - handle numbered sections like ## 8. Standard Workflow
    wf_match = re.search(
        r"^##\s+(?:\d+\.|\§\d+)?\s*.?(?:Standard Workflow|Work Process).*?\n(.*?)(?=^##\s|\Z)",
        body,
        re.MULTILINE | re.DOTALL,
    )
    if not wf_match:
        return 3.0

    wf_content = wf_match.group(1)

    # Check for References-First pattern (short content with external reference)
    # This is the skill-writer standard: content in references/ folder
    is_reference_pattern = bool(
        re.search(r"→.*?references/|→.*?\.md|see.*?references", wf_content, re.IGNORECASE)
    )

    # If it's a reference pattern (符合 skill-writer 的 References-First 原则)
    if is_reference_pattern:
        # Short reference to external file = valid pattern
        if len(wf_content.strip()) < 100:
            # Check if it mentions the phase-gate process (indicates understanding)
            if re.search(r"phase|gate|workflow", wf_content, re.IGNORECASE):
                return 7.0  # Good - references external detailed workflow
            return 5.0  # OK - has reference but minimal context

    # Check for phases (Phase 1, Phase 2, etc.)
    phases = len(re.findall(r"Phase \d+|Phase \d+:", wf_content, re.IGNORECASE))
    if phases >= 3:
        score += 3
    elif phases >= 1:
        score += 1

    # Check for [✓ Done] or checkboxes
    if re.search(r"\[.\]|✓|✓ Done|Done:", wf_content):
        score += 3

    # Check for templates or examples
    if re.search(r"template|example|step \d+", wf_content, re.IGNORECASE):
        score += 2

    # Check for actionable steps
    steps = len(re.findall(r"^\d+\.|\d+\)", wf_content, re.MULTILINE))
    if steps >= 5:
        score += 2

    return min(score, 10)


def analyze_risk_documentation(body: str) -> float:
    """Score Risk Documentation (0-10)."""
    score = 0

    # Check for Risk Disclaimer section (handles ## 3. Risk Disclaimer, ## Risk Disclaimer, etc.)
    if not has_section(body, "Risk"):
        return 1.0

    # Extract risk section - handle numbered sections
    risk_match = re.search(
        r"^##\s+(?:\d+\.|\§\d+)?\s*.*?Risk.*?\n(.*?)(?=^##\s|\Z)", body, re.MULTILINE | re.DOTALL
    )
    if not risk_match:
        return 2.0

    risk_content = risk_match.group(1)

    # Count risk entries (table rows or list items)
    risk_rows = len(re.findall(r"\|.*?\|.*?\|", risk_content))
    if risk_rows >= 5:
        score += 4
    elif risk_rows >= 3:
        score += 2

    # Check for severity indicators
    if re.search(r"🔴|High|Medium|Low|severity", risk_content, re.IGNORECASE):
        score += 3

    # Check for mitigation strategies
    if re.search(r"Mitigation|mitigation|prevent|solve", risk_content, re.IGNORECASE):
        score += 3

    return min(score, 10)


def analyze_example_quality(body: str) -> float:
    """Score Example Quality (0-10)."""
    score = 0

    # Check for Scenario Examples section
    if not has_section(body, "Scenario") and not has_section(body, "Example"):
        return 1.0

    # Count code blocks (indicates real examples)
    code_blocks = count_code_blocks(body)
    if code_blocks >= 3:
        score += 4
    elif code_blocks >= 1:
        score += 2

    # Check for conversation flows
    if re.search(r"User:|Expert:|Response:|Answer:", body):
        score += 3

    # Check for full scenario descriptions
    scenario_count = len(re.findall(r"^\d+\.|Scenario|Use Case", body, re.MULTILINE))
    if scenario_count >= 3:
        score += 3
    elif scenario_count >= 1:
        score += 1

    return min(score, 10)


def analyze_metadata(fm: Optional[Dict[str, str]], body: str) -> float:
    """Score Metadata Completeness (0-10)."""
    score = 0

    required_fields = ["name", "display_name", "author", "version", "description"]
    recommended_fields = ["difficulty", "category", "tags", "platforms", "quality"]

    if fm:
        # Required fields
        for field in required_fields:
            if field in fm and fm[field]:
                score += 1

        # Recommended fields
        for field in recommended_fields:
            if field in fm and fm[field]:
                score += 0.5

        # Check version format (semver)
        if "version" in fm and re.match(r"^\d+\.\d+\.\d+$", fm.get("version", "")):
            score += 1

    # Check for Version History section
    if has_section(body, "Version History"):
        score += 2

    # Check for License section
    if has_section(body, "License") or has_section(body, "Author"):
        score += 1

    return min(score, 10)


def calculate_weighted_score(scores: Dict[str, float]) -> float:
    """Calculate weighted average score."""
    total = 0
    for dimension, weight in WEIGHTS.items():
        total += scores[dimension] * weight
    return round(total, 2)


def determine_tier(score: float) -> str:
    """Determine quality tier based on score."""
    if score >= 9.0:
        return "exemplary"
    elif score >= 7.0:
        return "expert"
    elif score >= 4.0:
        return "community"
    else:
        return "basic"


def get_gaps(scores: Dict[str, float]) -> List[Dict[str, Any]]:
    """Identify gaps and improvement suggestions."""
    gaps = []

    gap_suggestions = {
        "system_prompt": {
            "threshold": 7,
            "suggestion": "Add decision framework, thinking patterns, and code block example to System Prompt",
        },
        "domain_knowledge": {
            "threshold": 7,
            "suggestion": "Add domain-specific frameworks with quantified metrics and decision trees",
        },
        "workflow": {
            "threshold": 7,
            "suggestion": "Add 3+ phases with [✓ Done] criteria and actionable steps",
        },
        "risk_documentation": {
            "threshold": 7,
            "suggestion": "Add 5+ domain-specific risks with severity ratings and mitigations",
        },
        "example_quality": {
            "threshold": 7,
            "suggestion": "Add 3+ full conversation scenario flows with code/examples",
        },
        "metadata": {
            "threshold": 7,
            "suggestion": "Complete all 9 YAML fields, add Version History and License sections",
        },
    }

    for dimension, data in gap_suggestions.items():
        if scores[dimension] < data["threshold"]:
            gaps.append(
                {
                    "dimension": dimension,
                    "score": scores[dimension],
                    "suggestion": data["suggestion"],
                }
            )

    return gaps


def score_skill(file_path: Path) -> Dict[str, Any]:
    """Score a single skill file."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"error": str(e), "path": str(file_path)}

    fm, body = parse_frontmatter(content)

    # Score each dimension
    scores = {
        "system_prompt": analyze_system_prompt(body),
        "domain_knowledge": analyze_domain_knowledge(body),
        "workflow": analyze_workflow(body),
        "risk_documentation": analyze_risk_documentation(body),
        "example_quality": analyze_example_quality(body),
        "metadata": analyze_metadata(fm, body),
    }

    weighted_avg = calculate_weighted_score(scores)
    tier = determine_tier(weighted_avg)
    gaps = get_gaps(scores)

    # Determine category and skill name from path
    parts = file_path.parts
    category = "unknown"
    skill_name = file_path.stem  # Default

    if "skills" in parts:
        idx = parts.index("skills")
        if idx + 1 < len(parts):
            category = parts[idx + 1]

        # For folder-based skills (SKILL.md), the skill name is the parent folder
        if file_path.name == "SKILL.md" and idx + 2 < len(parts):
            skill_name = parts[idx + 2]

    # Get relative path from repo root
    try:
        repo_root = SKILLS_DIR.parent
        rel_path = str(file_path.relative_to(repo_root))
    except ValueError:
        rel_path = str(file_path)

    return {
        "skill": skill_name,
        "category": category,
        "path": rel_path,
        "scores": scores,
        "weighted_avg": weighted_avg,
        "tier": tier,
        "gaps": gaps,
        "section_count": count_h2_sections(body),
        "code_blocks": count_code_blocks(body),
        "tables": count_tables(body),
    }


def score_all_skills(skills_dir: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Score all skills in the directory."""
    if skills_dir is None:
        skills_dir = SKILLS_DIR

    results = []

    # Find all SKILL.md files
    for skill_path in sorted(skills_dir.rglob("SKILL.md")):
        # Skip references, assets, etc.
        if any(x in skill_path.parts for x in ["references", "assets", "_common"]):
            continue
        result = score_skill(skill_path)
        results.append(result)

    return results


def print_score_summary(results: List[Dict[str, Any]]) -> None:
    """Print a summary of scores."""
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel

    console = Console()

    # Count by tier
    tiers = {"exemplary": 0, "expert": 0, "community": 0, "basic": 0, "error": 0}
    for r in results:
        if "error" in r:
            tiers["error"] += 1
        else:
            tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1

    # Print tier distribution
    console.print("\n[bold]Quality Distribution[/bold]")
    total = len([r for r in results if "error" not in r])
    for tier, count in tiers.items():
        if tier != "error":
            pct = (count / total * 100) if total > 0 else 0
            console.print(f"  {tier.upper()}: {count} ({pct:.1f}%)")

    # Print detailed table for Exemplary skills
    console.print("\n[bold green]Exemplary Skills (≥9.0)[/bold green]")
    table = Table(show_header=True)
    table.add_column("Skill")
    table.add_column("Category")
    table.add_column("Score")
    table.add_column("Key Gaps")

    for r in results:
        if "error" not in r and r["tier"] == "exemplary":
            gap_count = len(r.get("gaps", []))
            table.add_row(r["skill"], r["category"], f"{r['weighted_avg']:.2f}", str(gap_count))

    console.print(table)

    # Print skills needing work
    console.print("\n[bold yellow]Skills Needing Attention[/bold yellow]")
    needs_work = [r for r in results if "error" not in r and r["tier"] in ["basic", "community"]]
    if needs_work:
        for r in needs_work[:10]:  # Show top 10
            console.print(f"  - {r['category']}/{r['skill']} ({r['weighted_avg']:.2f})")
    else:
        console.print("  [green]All skills are at Expert or Exemplary level![/green]")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Score skills against quality rubric")
    parser.add_argument("--path", "-p", help="Specific skill path to score")
    parser.add_argument("--category", "-c", help="Filter by category")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text")
    parser.add_argument("--tier", "-t", choices=["exemplary", "expert", "community", "basic"])
    args = parser.parse_args()

    if args.path:
        # Score specific skill
        result = score_skill(Path(args.path))
        if args.output == "json":
            print(json.dumps(result, indent=2))
        else:
            from rich.console import Console

            console = Console()
            console.print(f"[bold]{result['skill']}[/bold] ({result['category']})")
            console.print(f"Score: {result['weighted_avg']}/10 ({result['tier']})")
            console.print("\n[bold]Dimension Scores:[/bold]")
            for dim, score in result["scores"].items():
                console.print(f"  {dim}: {score}/10")
            if result["gaps"]:
                console.print("\n[bold yellow]Gaps:[/bold yellow]")
                for gap in result["gaps"]:
                    console.print(f"  - {gap['dimension']}: {gap['suggestion']}")
    else:
        # Score all skills
        results = score_all_skills()

        # Filter by tier if specified
        if args.tier:
            results = [r for r in results if "error" not in r and r["tier"] == args.tier]

        # Filter by category if specified
        if args.category:
            results = [r for r in results if "error" not in r and r["category"] == args.category]

        if args.output == "json":
            print(json.dumps(results, indent=2))
        else:
            print_score_summary(results)


if __name__ == "__main__":
    main()
