#!/usr/bin/env python3
"""
Token Budget Detector

Based on skill-writer/references/standards.md §7.9 Token Budget Optimization

Checks:
- description chars: <263 (<40 skills) / <150 (40-60) / <130 (60+)
- SKILL.md body: <500 lines (folder) / <900 lines (meta)
- HTML comment detection in YAML
- Trigger verb position detection
- Token count estimation (NEW)
- API cost estimation in USD (NEW)
- Token efficiency score (NEW)
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

# Claude API pricing (input tokens) per 1M tokens, USD
# Source: Anthropic pricing page (approximate reference rates)
COST_PER_MILLION_TOKENS: Dict[str, float] = {
    "claude-haiku-4-5": 0.80,
    "claude-sonnet-4-6": 3.00,
    "claude-opus-4-6": 15.00,
}
DEFAULT_MODEL = "claude-sonnet-4-6"

# Token budget thresholds (skill loaded as system prompt at conversation start)
# These reflect reasonable limits so that skill context doesn't crowd out
# the user's own working context.
TOKEN_BUDGET = {
    "description": {"ok": 80, "warn": 120, "over": 200},   # tokens in description field
    "body": {"ok": 1500, "warn": 3000, "over": 5000},       # tokens in SKILL.md body
}


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

    # More sophisticated YAML parsing for multi-line values
    current_key = None
    current_value = []

    for line in fm_raw.splitlines():
        # Skip comments and empty lines
        if line.strip().startswith("#") or not line.strip():
            continue

        # Check if this is a new key line
        if ":" in line and not line.strip().startswith("#"):
            # Save previous key if exists
            if current_key:
                fm[current_key] = " ".join(current_value).strip()

            # Parse new key
            key, sep, val = line.partition(":")
            current_key = key.strip()
            current_value = [val.strip()] if val.strip() else []
        else:
            # Continuation of previous value
            if current_key and line.startswith(" "):
                current_value.append(line.strip())

    # Save last key
    if current_key:
        fm[current_key] = " ".join(current_value).strip()

    return fm, body


def check_description_budget(description: str, total_skills: int = 40) -> Dict[str, Any]:
    """Check if description fits token budget."""
    char_count = len(description)

    # Determine limit based on total skills installed
    if total_skills < 40:
        limit = 263
        tier = "normal"
    elif total_skills < 60:
        limit = 150
        tier = "high"
    else:
        limit = 130
        tier = "very_high"

    status = "OK" if char_count <= limit else "OVER_BUDGET"

    # Check trigger verb position (first 50 chars)
    first_50 = description[:50].lower()
    has_trigger_in_front = any(
        word in first_50
        for word in [
            "write",
            "create",
            "review",
            "score",
            "design",
            "build",
            "analyze",
            "develop",
            "optimize",
        ]
    )

    return {
        "char_count": char_count,
        "limit": limit,
        "status": status,
        "tier": tier,
        "has_trigger_in_front": has_trigger_in_front,
        "first_50_chars": description[:50],
    }


def check_body_lines(body: str, is_meta: bool = False) -> Dict[str, Any]:
    """Check if SKILL.md body fits line budget."""
    lines = [l for l in body.splitlines() if l.strip()]  # Non-empty lines

    # Meta skills (like skill-writer) can have up to 900 lines
    # Regular skills should be under 500
    limit = 900 if is_meta else 500

    status = "OK" if len(lines) <= limit else "OVER_BUDGET"

    return {
        "line_count": len(lines),
        "limit": limit,
        "status": status,
        "is_meta": is_meta,
    }


def check_html_in_yaml(raw_content: str) -> List[Dict[str, Any]]:
    """Check for HTML comments inside YAML frontmatter."""
    issues = []

    if not raw_content.startswith("---"):
        return issues

    parts = raw_content.split("---", 2)
    if len(parts) < 3:
        return issues

    fm_block = parts[1]
    lines = fm_block.splitlines()

    for i, line in enumerate(lines, start=2):
        if "<!--" in line:
            issues.append(
                {
                    "line": i,
                    "content": line.strip(),
                    "severity": "high",
                    "message": "HTML comment in YAML causes parse errors on some platforms",
                }
            )

    return issues


def check_trigger_verbs(description: str) -> Dict[str, Any]:
    """Check trigger verb positioning and quality."""
    # Common trigger verbs
    trigger_verbs = [
        "write",
        "create",
        "review",
        "score",
        "design",
        "build",
        "analyze",
        "develop",
        "optimize",
        "debug",
        "test",
        "deploy",
        "plan",
        "execute",
        "manage",
        "lead",
        "guide",
        "assist",
        "help",
        "transform",
    ]

    description_lower = description.lower()
    found_verbs = [v for v in trigger_verbs if v in description_lower]

    # Check first 50 chars
    first_50 = description_lower[:50]
    front_verbs = [v for v in trigger_verbs if v in first_50]

    return {
        "found_verbs": found_verbs[:5],  # Top 5
        "verb_count": len(found_verbs),
        "front_verbs": front_verbs,
        "has_verbs_in_front": len(front_verbs) > 0,
    }


def check_references_offload(body: str) -> Dict[str, Any]:
    """Check if content is properly offloaded to references/."""
    issues = []

    # Find sections that might be too long (>3 lines) and should be in references/
    section_pattern = r"^##\s+\S+(.*?)(?=^##\s|\Z)"
    sections = re.findall(section_pattern, body, re.MULTILINE | re.DOTALL)

    long_sections = []
    for i, section in enumerate(sections):
        lines = [l for l in section.splitlines() if l.strip()]
        if len(lines) > 10:  # Very rough heuristic
            long_sections.append(
                {
                    "section_num": i + 1,
                    "line_count": len(lines),
                    "preview": lines[0][:50] if lines else "",
                }
            )

    return {
        "potential_offload_candidates": len(long_sections),
        "details": long_sections[:5],  # Top 5
    }


def estimate_token_count(text: str) -> int:
    """Estimate token count for a text string.

    Uses a character-based heuristic:
    - CJK characters (Chinese/Japanese/Korean): ~1 token per character
    - Other characters: ~4 characters per token (English/code average)

    This is a rough approximation; actual tokenisation varies by model.
    """
    cjk_chars = len(re.findall(r"[\u4e00-\u9fff\u3040-\u30ff\uac00-\ud7af]", text))
    other_chars = len(text) - cjk_chars
    return int(cjk_chars * 1.0 + other_chars * 0.25)


def estimate_api_cost(token_count: int, model: str = DEFAULT_MODEL) -> Dict[str, Any]:
    """Estimate API cost for loading this skill as a system prompt.

    Assumes the skill body is sent as input tokens each conversation turn.
    Cost is calculated for a single conversation load (not per turn).
    """
    cost_per_million = COST_PER_MILLION_TOKENS.get(model, COST_PER_MILLION_TOKENS[DEFAULT_MODEL])
    cost_usd = (token_count / 1_000_000) * cost_per_million

    # Classify cost tier
    if token_count <= TOKEN_BUDGET["body"]["ok"]:
        tier = "efficient"
    elif token_count <= TOKEN_BUDGET["body"]["warn"]:
        tier = "moderate"
    elif token_count <= TOKEN_BUDGET["body"]["over"]:
        tier = "expensive"
    else:
        tier = "very_expensive"

    return {
        "token_count": token_count,
        "model": model,
        "cost_per_load_usd": round(cost_usd, 6),
        "cost_per_100_loads_usd": round(cost_usd * 100, 4),
        "cost_tier": tier,
    }


def score_token_efficiency(description_result: Dict[str, Any], body_result: Dict[str, Any], cost_result: Dict[str, Any]) -> Dict[str, Any]:
    """Compute a composite token efficiency score (0-10).

    Combines:
    - Description budget compliance (40%)
    - Body line budget compliance (40%)
    - Absolute token count cost tier (20%)
    """
    desc_score = 0.0
    body_score = 0.0
    cost_score = 0.0

    # Description budget
    status = description_result.get("status", "MISSING")
    if status == "OK":
        ratio = description_result.get("char_count", 0) / max(description_result.get("limit", 1), 1)
        if ratio <= 0.7:
            desc_score = 10
        elif ratio <= 0.9:
            desc_score = 8
        else:
            desc_score = 6
    elif status == "OVER_BUDGET":
        ratio = description_result.get("char_count", 0) / max(description_result.get("limit", 1), 1)
        desc_score = max(0.0, 6 - (ratio - 1.0) * 10)
    else:
        desc_score = 0  # MISSING

    # Body line budget
    body_status = body_result.get("status", "MISSING")
    line_ratio = body_result.get("line_count", 0) / max(body_result.get("limit", 1), 1)
    if body_status == "OK":
        if line_ratio <= 0.5:
            body_score = 10
        elif line_ratio <= 0.8:
            body_score = 8
        else:
            body_score = 6
    else:
        body_score = max(0.0, 6 - (line_ratio - 1.0) * 5)

    # Cost tier
    tier_scores = {"efficient": 10, "moderate": 7, "expensive": 4, "very_expensive": 1}
    cost_score = tier_scores.get(cost_result.get("cost_tier", "expensive"), 4)

    composite = desc_score * 0.40 + body_score * 0.40 + cost_score * 0.20
    grade = "A" if composite >= 9 else "B" if composite >= 7 else "C" if composite >= 5 else "D"

    return {
        "score": round(composite, 2),
        "grade": grade,
        "desc_score": round(desc_score, 2),
        "body_score": round(body_score, 2),
        "cost_score": round(cost_score, 2),
    }


def analyze_token_budget(file_path: Path, total_skills: int = 40) -> Dict[str, Any]:
    """Analyze token budget for a single skill."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"error": str(e), "path": str(file_path)}

    fm, body = parse_frontmatter(content)

    # Get relative path from repo root
    try:
        repo_root = SKILLS_DIR.parent
        rel_path = str(file_path.relative_to(repo_root))
    except ValueError:
        rel_path = str(file_path)

    # Determine category and skill name from path
    parts = file_path.parts
    category = "unknown"
    skill_name = file_path.stem

    if "skills" in parts:
        idx = parts.index("skills")
        if idx + 1 < len(parts):
            category = parts[idx + 1]
        # For folder-based skills (SKILL.md), the skill name is the parent folder
        if file_path.name == "SKILL.md" and idx + 2 < len(parts):
            skill_name = parts[idx + 2]

    results = {
        "path": rel_path,
        "skill": skill_name,
        "category": category,
    }

    # Check description budget
    if fm and "description" in fm:
        description = fm.get("description", "")
        results["description"] = check_description_budget(description, total_skills)
    else:
        results["description"] = {"error": "No description found", "status": "MISSING"}

    # Check body lines
    is_meta = "skill-writer" in str(file_path) or "meta" in str(file_path).lower()
    results["body"] = check_body_lines(body, is_meta)

    # Check HTML in YAML
    results["html_in_yaml"] = check_html_in_yaml(content)

    # Check trigger verbs
    if fm and "description" in fm:
        results["triggers"] = check_trigger_verbs(fm.get("description", ""))

    # Check references offload
    results["references"] = check_references_offload(body)

    # ── NEW: Token count & API cost estimation ────────────────────────────
    body_tokens = estimate_token_count(body)
    results["token_count"] = body_tokens
    results["api_cost"] = estimate_api_cost(body_tokens)

    # Description token count
    if fm and "description" in fm:
        desc_tokens = estimate_token_count(fm.get("description", ""))
        results["description"]["token_count"] = desc_tokens
        results["description"]["token_budget_status"] = (
            "OK" if desc_tokens <= TOKEN_BUDGET["description"]["ok"]
            else "WARN" if desc_tokens <= TOKEN_BUDGET["description"]["warn"]
            else "OVER"
        )

    # ── NEW: Composite token efficiency score ─────────────────────────────
    results["token_efficiency"] = score_token_efficiency(
        results.get("description", {}),
        results["body"],
        results["api_cost"],
    )

    # Overall status
    has_issues = (
        results["description"].get("status") == "OVER_BUDGET"
        or results["body"].get("status") == "OVER_BUDGET"
        or len(results["html_in_yaml"]) > 0
    )
    results["overall_status"] = "ISSUES_FOUND" if has_issues else "OK"

    return results


def analyze_all_skills(
    skills_dir: Optional[Path] = None, total_skills: int = 40
) -> List[Dict[str, Any]]:
    """Analyze token budget for all skills."""
    if skills_dir is None:
        skills_dir = SKILLS_DIR

    results = []

    for skill_path in sorted(skills_dir.rglob("SKILL.md")):
        if any(x in skill_path.parts for x in ["references", "assets", "_common"]):
            continue
        result = analyze_token_budget(skill_path, total_skills)
        results.append(result)

    return results


def print_token_summary(results: List[Dict[str, Any]]) -> None:
    """Print token budget summary."""
    from rich.console import Console
    from rich.table import Table

    console = Console()

    # Count issues
    over_desc = 0
    over_body = 0
    html_issues = 0
    total_tokens = 0
    total_cost_usd = 0.0

    for r in results:
        if "error" in r:
            continue

        if r.get("description", {}).get("status") == "OVER_BUDGET":
            over_desc += 1
        if r.get("body", {}).get("status") == "OVER_BUDGET":
            over_body += 1
        if r.get("html_in_yaml"):
            html_issues += 1
        total_tokens += r.get("token_count", 0)
        total_cost_usd += r.get("api_cost", {}).get("cost_per_load_usd", 0.0)

    console.print("\n[bold]Token Budget Summary[/bold]")
    console.print(f"  Skills analyzed: {len(results)}")
    console.print(f"  Description over budget: {over_desc}")
    console.print(f"  Body over budget: {over_body}")
    console.print(f"  HTML in YAML: {html_issues}")
    console.print(f"\n[bold]Cost Estimation (loading all skills once)[/bold]")
    console.print(f"  Total body tokens: {total_tokens:,}")
    console.print(f"  Estimated API cost ({DEFAULT_MODEL}): ${total_cost_usd:.4f} USD")
    console.print(f"  Est. cost per 100 full loads: ${total_cost_usd * 100:.2f} USD")

    # Show problematic skills
    console.print("\n[bold yellow]Skills with Token Issues[/bold yellow]")
    table = Table(show_header=True)
    table.add_column("Skill")
    table.add_column("Tokens")
    table.add_column("Cost/load")
    table.add_column("Efficiency")
    table.add_column("Issue")

    for r in results:
        if "error" in r:
            continue

        issues = []
        if r.get("description", {}).get("status") == "OVER_BUDGET":
            d = r["description"]
            issues.append(f"Desc: {d['char_count']}/{d['limit']}ch")
        if r.get("body", {}).get("status") == "OVER_BUDGET":
            b = r["body"]
            issues.append(f"Body: {b['line_count']}/{b['limit']}L")
        if r.get("html_in_yaml"):
            issues.append(f"HTML: {len(r['html_in_yaml'])}")

        cost = r.get("api_cost", {})
        eff = r.get("token_efficiency", {})

        if issues or cost.get("cost_tier") in ("expensive", "very_expensive"):
            table.add_row(
                r["skill"],
                str(r.get("token_count", "?")),
                f"${cost.get('cost_per_load_usd', 0):.5f}",
                f"{eff.get('score', '?')}/10 ({eff.get('grade', '?')})",
                ", ".join(issues) or cost.get("cost_tier", ""),
            )

    console.print(table)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Check token budget for skills")
    parser.add_argument("--path", "-p", help="Specific skill path")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text")
    parser.add_argument(
        "--total-skills",
        "-t",
        type=int,
        default=40,
        help="Total skills installed (affects description limit)",
    )
    parser.add_argument("--category", "-c", help="Filter by category")
    args = parser.parse_args()

    if args.path:
        result = analyze_token_budget(Path(args.path), args.total_skills)
        if args.output == "json":
            import json

            print(json.dumps(result, indent=2))
        else:
            from rich.console import Console

            console = Console()
            console.print(f"[bold]{result['skill']}[/bold]")
            console.print(f"Path: {result['path']}")

            if "description" in result and "error" not in result.get("description", {}):
                d = result["description"]
                console.print(
                    f"\nDescription: {d['char_count']}/{d['limit']} chars - {d['status']}"
                )

            if "body" in result:
                b = result["body"]
                console.print(f"Body: {b['line_count']}/{b['limit']} lines - {b['status']}")

            if result.get("html_in_yaml"):
                console.print(f"\n[red]HTML in YAML: {len(result['html_in_yaml'])} issues[/red]")
    else:
        results = analyze_all_skills(total_skills=args.total_skills)

        if args.category:
            results = [r for r in results if args.category in r.get("path", "")]

        if args.output == "json":
            import json

            print(json.dumps(results, indent=2))
        else:
            print_token_summary(results)


if __name__ == "__main__":
    main()
