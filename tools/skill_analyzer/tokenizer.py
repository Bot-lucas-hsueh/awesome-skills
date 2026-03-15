#!/usr/bin/env python3
"""
Token Budget Detector

Based on skill-writer/references/standards.md §7.9 Token Budget Optimization

Checks:
- description chars: <263 (<40 skills) / <150 (40-60) / <130 (60+)
- SKILL.md body: <500 lines (folder) / <900 lines (meta)
- HTML comment detection in YAML
- Trigger verb position detection
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"


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

    for r in results:
        if "error" in r:
            continue

        if r.get("description", {}).get("status") == "OVER_BUDGET":
            over_desc += 1
        if r.get("body", {}).get("status") == "OVER_BUDGET":
            over_body += 1
        if r.get("html_in_yaml"):
            html_issues += 1

    console.print("\n[bold]Token Budget Summary[/bold]")
    console.print(f"  Skills analyzed: {len(results)}")
    console.print(f"  Description over budget: {over_desc}")
    console.print(f"  Body over budget: {over_body}")
    console.print(f"  HTML in YAML: {html_issues}")

    # Show problematic skills
    console.print("\n[bold yellow]Skills with Token Issues[/bold yellow]")
    table = Table(show_header=True)
    table.add_column("Skill")
    table.add_column("Issue Type")
    table.add_column("Details")

    for r in results:
        if "error" in r:
            continue

        issues = []
        if r.get("description", {}).get("status") == "OVER_BUDGET":
            d = r["description"]
            issues.append(f"Desc: {d['char_count']}/{d['limit']}")
        if r.get("body", {}).get("status") == "OVER_BUDGET":
            b = r["body"]
            issues.append(f"Body: {b['line_count']}/{b['limit']}")
        if r.get("html_in_yaml"):
            issues.append(f"HTML: {len(r['html_in_yaml'])} issues")

        if issues:
            table.add_row(r["skill"], ", ".join(issues[:2]), r["path"])

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
