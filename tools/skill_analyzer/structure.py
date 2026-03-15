#!/usr/bin/env python3
"""
Structure Checker - 16-Section Completeness

Based on skill-writer/references/standards.md §7.3 16-Section Checklist

Checks:
- All 16 standard sections present
- Section order correct
- Bilingual format (E/C separator)
- Required subsections in System Prompt
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

# Standard 16 sections from TEMPLATE.md
STANDARD_SECTIONS = [
    ("1", "System Prompt", ["system prompt", "system prompt"]),
    ("2", "What This Skill Does", ["what this skill does", "此技能做什么"]),
    ("3", "Risk Disclaimer", ["risk", "风险"]),
    ("4", "Core Philosophy", ["core philosophy", "核心理念"]),
    ("5", "Platform Support", ["platform", "平台"]),
    ("6", "Professional Toolkit", ["toolkit", "工具"]),
    ("7", "Standards & Reference", ["standards", "standard"]),
    ("8", "Standard Workflow", ["workflow", "工作流程"]),
    ("9", "Scenario Examples", ["scenario", "example", "场景", "示例"]),
    ("10", "Common Pitfalls", ["pitfall", "anti-pattern", "陷阱"]),
    ("11", "Integration", ["integration", "integration with", "集成"]),
    ("12", "Scope & Limitations", ["scope", "limitation", "范围"]),
    ("13", "How to Use", ["how to use", "如何使用", "install"]),
    ("14", "Quality Verification", ["quality", "verification", "质量"]),
    ("15", "Version History", ["version history", "版本历史"]),
    ("16", "License & Author", ["license", "author", "许可证"]),
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


def find_sections(body: str) -> List[Dict[str, Any]]:
    """Find all H2 sections in the body."""
    sections = []

    # Find ## headings
    pattern = r"^##\s+(.+?)(?:\n|$)"
    matches = re.finditer(pattern, body, re.MULTILINE)

    for match in matches:
        title = match.group(1).strip()
        start_pos = match.start()

        # Find content (until next ## or end)
        content_match = re.search(r"(?<=[\n])##\s+|\Z", body[start_pos + len(match.group(0)) :])
        if content_match:
            end_pos = start_pos + len(match.group(0)) + content_match.start()
            content = body[start_pos + len(match.group(0)) : end_pos]
        else:
            content = body[start_pos + len(match.group(0)) :]

        sections.append(
            {
                "title": title,
                "position": len(sections) + 1,
                "start_pos": start_pos,
                "content": content[:200],  # First 200 chars for analysis
                "line_count": len([l for l in content.splitlines() if l.strip()]),
            }
        )

    return sections


def check_section_completeness(sections: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Check if all 16 standard sections are present."""
    found_titles = [s["title"].lower() for s in sections]

    missing = []
    found = []

    for num, name, keywords in STANDARD_SECTIONS:
        # Check if any section matches this standard
        matched = False
        for title in found_titles:
            if any(kw in title for kw in keywords):
                matched = True
                break

        if matched:
            found.append({"num": num, "name": name, "found": True})
        else:
            missing.append({"num": num, "name": name, "found": False})

    # Check order
    order_issues = []
    for i in range(len(sections) - 1):
        current_title = sections[i]["title"].lower()
        next_title = sections[i + 1]["title"].lower()

        # Check if current section should come before next
        for num, name, keywords in STANDARD_SECTIONS:
            if any(kw in current_title for kw in keywords):
                current_num = int(num)
                break
        else:
            continue

        for num, name, keywords in STANDARD_SECTIONS:
            if any(kw in next_title for kw in keywords):
                next_num = int(num)
                break
        else:
            continue

        if current_num > next_num:
            order_issues.append(
                {"section": sections[i]["title"], "should_be_before": sections[i + 1]["title"]}
            )

    return {
        "total_sections": len(sections),
        "required": 16,
        "found": found,
        "missing": missing,
        "complete": len(missing) == 0,
        "order_issues": order_issues[:3],  # Top 3
    }


def check_bilingual_format(body: str) -> Dict[str, Any]:
    """Check bilingual format compliance."""
    issues = []

    # Check for bilingual labels in headings (should use / separator)
    heading_pattern = r"^(#{1,6})\s+(.+?)$"
    for match in re.finditer(heading_pattern, body, re.MULTILINE):
        heading = match.group(2)
        # If heading has Chinese, should use / separator
        if re.search(r"[\u4e00-\u9fff]", heading):
            if "/" not in heading and len(heading) > 30:
                issues.append(
                    {
                        "type": "heading",
                        "content": heading[:50],
                        "suggestion": "Use / separator for bilingual headings",
                    }
                )

    # Check table headers
    table_issues = 0
    for match in re.finditer(r"\|(.+?)\|", body):
        header = match.group(1)
        if re.search(r"[\u4e00-\u9fff]", header):
            # Has Chinese in table - should use / separator
            if "/" not in header and "---" not in header:
                table_issues += 1

    if table_issues > 5:
        issues.append(
            {
                "type": "table",
                "count": table_issues,
                "suggestion": "Use / separator in table headers with Chinese",
            }
        )

    # Check for HTML comments in body (should be in code blocks or removed)
    html_comments = len(re.findall(r"<!--[\s\S]*?-->", body))

    return {
        "issues": issues,
        "html_comments": html_comments,
        "format_ok": len(issues) == 0 and html_comments < 10,
    }


def check_system_prompt_subsection(body: str) -> Dict[str, Any]:
    """Check if System Prompt has required subsections."""
    # Find System Prompt section
    sp_match = re.search(
        r"^##\s+.?System Prompt.*?\n(.*?)(?=^##\s|\Z)", body, re.MULTILINE | re.DOTALL
    )

    if not sp_match:
        return {
            "has_section": False,
            "missing_subsections": ["Role Definition", "Decision Framework"],
        }

    sp_content = sp_match.group(1)

    # Check for subsections
    subsections = {
        "role_definition": bool(
            re.search(r"Role|Identity|You are a|Expert in", sp_content, re.IGNORECASE)
        ),
        "decision_framework": bool(
            re.search(r"Gate|Decision|Question|Before", sp_content, re.IGNORECASE)
        ),
        "thinking_patterns": bool(
            re.search(r"Thinking|Dimension|Perspective", sp_content, re.IGNORECASE)
        ),
        "communication_style": bool(
            re.search(r"Style|Communication|Tone", sp_content, re.IGNORECASE)
        ),
        "code_block": bool(re.search(r"```", sp_content)),
    }

    missing = [k for k, v in subsections.items() if not v]

    return {
        "has_section": True,
        "subsections": subsections,
        "missing_subsections": missing,
        "complete": len(missing) == 0,
    }


def check_structure(file_path: Path) -> Dict[str, Any]:
    """Check structure for a single skill."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"error": str(e), "path": str(file_path)}

    fm, body = parse_frontmatter(content)

    # Find sections
    sections = find_sections(body)

    # Check completeness
    completeness = check_section_completeness(sections)

    # Check bilingual format
    bilingual = check_bilingual_format(body)

    # Check System Prompt subsections
    sp_subsection = check_system_prompt_subsection(body)

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

    return {
        "path": rel_path,
        "skill": skill_name,
        "category": category,
        "sections": {
            "total": len(sections),
            "details": [{"title": s["title"], "lines": s["line_count"]} for s in sections[:10]],
        },
        "completeness": completeness,
        "bilingual": bilingual,
        "system_prompt": sp_subsection,
        "overall_score": calculate_overall_score(completeness, bilingual, sp_subsection),
    }


def calculate_overall_score(completeness: Dict, bilingual: Dict, sp: Dict) -> int:
    """Calculate overall structure score (0-100)."""
    score = 0

    # Section completeness (50 points)
    total_sections = completeness.get("total_sections", 0)
    required = completeness.get("required", 16)
    completeness_pct = (total_sections / required) * 50
    score += min(completeness_pct, 50)

    # Missing sections penalty
    score -= len(completeness.get("missing", [])) * 5

    # Bilingual format (20 points)
    if bilingual["format_ok"]:
        score += 20
    else:
        score += max(0, 20 - len(bilingual["issues"]) * 5)

    # System Prompt subsections (30 points)
    if sp.get("complete", False):
        score += 30
    elif sp.get("has_section", False):
        score += 15

    return max(0, min(100, score))


def analyze_all_skills(skills_dir: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Analyze structure for all skills."""
    if skills_dir is None:
        skills_dir = SKILLS_DIR

    results = []

    for skill_path in sorted(skills_dir.rglob("SKILL.md")):
        if any(x in skill_path.parts for x in ["references", "assets", "_common"]):
            continue
        result = check_structure(skill_path)
        results.append(result)

    return results


def print_structure_summary(results: List[Dict[str, Any]]) -> None:
    """Print structure summary."""
    from rich.console import Console
    from rich.table import Table

    console = Console()

    # Count issues
    incomplete = 0
    format_issues = 0
    sp_incomplete = 0

    for r in results:
        if "error" in r:
            continue

        if not r.get("completeness", {}).get("complete", False):
            incomplete += 1
        if not r.get("bilingual", {}).get("format_ok", True):
            format_issues += 1
        if not r.get("system_prompt", {}).get("complete", True):
            sp_incomplete += 1

    console.print("\n[bold]Structure Check Summary[/bold]")
    console.print(f"  Skills analyzed: {len(results)}")
    console.print(f"  Missing sections: {incomplete}")
    console.print(f"  Format issues: {format_issues}")
    console.print(f"  System Prompt incomplete: {sp_incomplete}")

    # Show problematic skills
    console.print("\n[bold yellow]Skills with Structure Issues[/bold yellow]")
    table = Table(show_header=True)
    table.add_column("Skill")
    table.add_column("Sections")
    table.add_column("Missing")
    table.add_column("Score")

    for r in results:
        if "error" in r:
            continue

        c = r.get("completeness", {})
        if not c.get("complete", False) or r.get("overall_score", 100) < 80:
            missing_names = [m["name"] for m in c.get("missing", [])[:2]]
            table.add_row(
                r["skill"],
                f"{c.get('total', 0)}/16",
                ", ".join(missing_names) if missing_names else "-",
                f"{r.get('overall_score', 0)}%",
            )

    console.print(table)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Check skill structure")
    parser.add_argument("--path", "-p", help="Specific skill path")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text")
    args = parser.parse_args()

    if args.path:
        result = check_structure(Path(args.path))
        if args.output == "json":
            import json

            print(json.dumps(result, indent=2))
        else:
            from rich.console import Console

            console = Console()
            console.print(f"[bold]{result['skill']}[/bold]")
            console.print(f"Sections: {result['sections']['total']}/16")
            console.print(f"Score: {result.get('overall_score', 0)}%")

            c = result.get("completeness", {})
            if c.get("missing"):
                console.print("\n[red]Missing sections:[/red]")
                for m in c["missing"]:
                    console.print(f"  - §{m['num']}: {m['name']}")
    else:
        results = analyze_all_skills()

        if args.output == "json":
            import json

            print(json.dumps(results, indent=2))
        else:
            print_structure_summary(results)


if __name__ == "__main__":
    main()
