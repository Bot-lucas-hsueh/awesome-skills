#!/usr/bin/env python3
"""
Anti-Pattern Scanner

Based on skill-writer/references/anti-patterns.md and 2024-2026 research:
  - SkillReducer (arXiv 2603.29919): 60%+ of skill body content is non-actionable
  - PRISM (arXiv 2603.18507): expert personas hurt factual tasks when overclaiming
  - OWASP Agentic Skills Top 10 (Dec 2025): hallucination risk & safety patterns
  - CharacterBench (AAAI 2025): behavioral coherence dimensions

Detects 12 anti-patterns (9 original + 3 new):
Original:
  - Scope Sprawl (跨领域)
  - Shallow Depth (通用列表)
  - Self-Inconsistency (自相矛盾)
  - Token Waste (冗余内容)
  - Generic Risk (通用风险)
  - HTML in YAML
  - Platform Coverage (平台覆盖)
  - Literal Translation (字面翻译)
  - Prose Wall (长段落)
New (2025-2026 research):
  - Hallucination Risk (虚假专业知识 — unverifiable claims, fake citations)
  - Capability Overclaiming (过度宣称能力 — PRISM finding: hurts factual tasks)
  - Missing Uncertainty Communication (缺少不确定性表达 — HELM calibration metric)
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

try:
    from tools.skill_analyzer.yaml_utils import parse_frontmatter
except ImportError:
    try:
        from skill_analyzer.yaml_utils import parse_frontmatter  # type: ignore[no-redef]
    except ImportError:
        from yaml_utils import parse_frontmatter  # type: ignore[no-redef]

# Anti-pattern definitions
ANTIPATTERNS = {
    "scope_sprawl": {
        "name": "Scope Sprawl",
        "severity": "high",
        "description": "Skill covers multiple domains or job titles",
        "patterns": [
            r"(?:and|,)\s*(?:DevOps|Cloud|Security|AI\/ML|Frontend|Backend|Mobile)",
            r"covers?:.*(?:and|or|,).*(?:architecture|development|operations)",
        ],
    },
    "shallow_depth": {
        "name": "Shallow Depth",
        "severity": "high",
        "description": "Content is generic lists without domain-specific frameworks",
        "patterns": [
            r"##\s*(?:Core Philosophy|Principles|Best Practices).*?\n.*?(?:\d+\.|\-|•)\s*(?:Write clean|Follow best|Test your)",
            r"write clean code|follow best practices|test your code",
        ],
    },
    "self_inconsistency": {
        "name": "Self-Inconsistency",
        "severity": "high",
        "description": "Skill doesn't follow its own rules",
        "patterns": [
            r"missing required field|must include all",
        ],
    },
    "token_waste": {
        "name": "Token Waste",
        "severity": "medium",
        "description": "Unnecessary repetition or verbose content",
        "patterns": [
            r"(?:Category|Domain):\s*\n(?:.*\n){5,}",  # Long static lists
            r"(?:目录|tree).*?(\n.*){20,}",  # Long directory trees
        ],
    },
    "generic_risk": {
        "name": "Generic Risk",
        "severity": "medium",
        "description": "Risk entries are generic without domain specificity",
        "patterns": [
            r"(?:Risk|Mitigation).*?(?:AI may be wrong|Verify output|Check result)",
            r"\|.*?(?:Accuracy|AI Error|Verification).*?\|.*?(?:Verify|Check)",
        ],
    },
    "html_in_yaml": {
        "name": "HTML in YAML",
        "severity": "medium",
        "description": "HTML comments in YAML frontmatter",
        "patterns": [
            r"^---\s*\n.*<!--",
        ],
    },
    "platform_coverage": {
        "name": "Platform Coverage",
        "severity": "medium",
        "description": "Missing platforms in installation guide",
        "patterns": [
            r"(?:Platform|Installation).*?(Claude Code|OpenCode|Cursor|Kimi)",
        ],
    },
    "literal_translation": {
        "name": "Literal Translation",
        "severity": "low",
        "description": "Chinese translations are word-for-word",
        "patterns": [
            r"(?:think outside the box|think out of the box).*?(?:盒子外|箱外)",
            r"(?:kill two birds|hit two birds).*?(?:一石二鸟)",
        ],
    },
    "prose_wall": {
        "name": "Prose Wall",
        "severity": "low",
        "description": "Long paragraphs without structure",
        "patterns": [
            r"^[^\n#]{200,}\n[^\n#]{200,}\n[^\n#]{200,}",  # 3+ long lines
        ],
    },
}


def check_scope_sprawl(body: str) -> List[Dict[str, Any]]:
    """Check for scope sprawl (multiple domains)."""
    issues = []

    # Look for multiple domains in description or headers
    domains = [
        "DevOps",
        "Cloud",
        "ML",
        "Frontend",
        "Backend",
        "Mobile",
        "Full-stack",
        "Analytics",
    ]

    found_domains = []
    for domain in domains:
        if re.search(rf"\b{domain}\b", body, re.IGNORECASE):
            found_domains.append(domain)

    if len(found_domains) > 3:
        issues.append(
            {
                "type": "scope_sprawl",
                "severity": "high",
                "message": f"Found {len(found_domains)} domains: {', '.join(found_domains[:5])}",
                "suggestion": "Split into multiple focused skills",
            }
        )

    return issues


def check_shallow_depth(body: str) -> List[Dict[str, Any]]:
    """Check for shallow depth (generic content)."""
    issues = []

    # Check for generic best practices without specifics
    generic_phrases = [
        r"write clean code",
        r"follow best practices",
        r"test your code",
        r"use best tools",
        r"stay updated",
    ]

    found = []
    for phrase in generic_phrases:
        if re.search(phrase, body, re.IGNORECASE):
            found.append(phrase)

    # Check if there are actual frameworks
    has_frameworks = bool(
        re.search(r"(?:framework|decision tree|matrix|checklist)", body, re.IGNORECASE)
    )

    if len(found) >= 2 and not has_frameworks:
        issues.append(
            {
                "type": "shallow_depth",
                "severity": "high",
                "message": "Generic best practices without domain frameworks",
                "suggestion": "Add specific decision frameworks with thresholds",
            }
        )

    return issues


def check_html_in_yaml(content: str) -> List[Dict[str, Any]]:
    """Check for HTML comments in YAML frontmatter."""
    issues = []

    if not content.startswith("---"):
        return issues

    parts = content.split("---", 2)
    if len(parts) < 3:
        return issues

    fm_block = parts[1]

    if "<!--" in fm_block:
        issues.append(
            {
                "type": "html_in_yaml",
                "severity": "medium",
                "message": "HTML comments found in YAML frontmatter",
                "suggestion": "Remove HTML comments from YAML or use # instead",
            }
        )

    return issues


def check_generic_risk(body: str) -> List[Dict[str, Any]]:
    """Check for generic risk entries."""
    issues = []

    # Find Risk section
    risk_match = re.search(r"^##\s+.?Risk.*?\n(.*?)(?=^##\s|\Z)", body, re.MULTILINE | re.DOTALL)

    if not risk_match:
        return issues

    risk_content = risk_match.group(1)

    # Check for generic risks
    generic_risks = [
        r"AI may be wrong",
        r"verify output",
        r"check result",
        r"AI can make mistakes",
    ]

    found_generic = []
    for risk in generic_risks:
        if re.search(risk, risk_content, re.IGNORECASE):
            found_generic.append(risk)

    if found_generic:
        issues.append(
            {
                "type": "generic_risk",
                "severity": "medium",
                "message": f"Generic risk entries found: {len(found_generic)}",
                "suggestion": "Add domain-specific risks with concrete consequences",
            }
        )

    return issues


def check_platform_coverage(body: str) -> List[Dict[str, Any]]:
    """Check for platform coverage."""
    issues = []

    # Look for Platform Support section - more precise regex
    # Match ## followed by optional number, then "Platform Support" as the main title
    platform_match = re.search(
        r"^##\s+(?:\d+\.?\s*|\§\d+\.?\s*)?Platform Support.*?\n(.*?)(?=^##\s|\Z)",
        body,
        re.MULTILINE | re.DOTALL,
    )

    if not platform_match:
        issues.append(
            {
                "type": "platform_coverage",
                "severity": "medium",
                "message": "No Platform Support section found",
                "suggestion": "Add installation instructions for all 7 platforms",
            }
        )
        return issues

    platform_content = platform_match.group(1)

    # If content is very short, check if it's a reference to another file
    if len(platform_content.strip()) < 50:
        # Check if it references INSTALL.md or similar
        if re.search(r"INSTALL|install|references/", platform_content, re.IGNORECASE):
            # It's a reference - this is OK for meta-skills
            return issues

    # Check for key platforms (more flexible matching)
    platform_patterns = {
        "Claude Code": [r"Claude Code", r"Claude"],
        "OpenCode": [r"OpenCode"],
        "Cursor": [r"Cursor"],
        "Kimi": [r"Kimi"],
    }
    found_platforms = []

    for platform, patterns in platform_patterns.items():
        for pattern in patterns:
            if re.search(pattern, platform_content, re.IGNORECASE):
                found_platforms.append(platform)
                break

    # If it's a reference to external file (meta-skill pattern), consider it OK
    is_reference = bool(re.search(r"→.*?\.md|assets/|references/", platform_content))

    if is_reference and len(found_platforms) >= 1:
        # Meta-skill with external reference - this is acceptable
        return issues

    if len(found_platforms) < 3:
        issues.append(
            {
                "type": "platform_coverage",
                "severity": "medium",
                "message": f"Only {len(found_platforms)}/4 platforms mentioned",
                "suggestion": "Add installation for all 7 platforms",
            }
        )

    return issues


def check_prose_wall(body: str) -> List[Dict[str, Any]]:
    """Check for long prose sections."""
    issues = []

    # Find sections with long paragraphs
    section_pattern = r"^##\s+\S+(.*?)(?=^##\s|\Z)"
    sections = re.findall(section_pattern, body, re.MULTILINE | re.DOTALL)

    long_sections = []
    for section in sections:
        lines = [l for l in section.splitlines() if l.strip() and not l.strip().startswith("|")]
        if len(lines) > 15:
            # Check if it's mostly prose (not tables or lists)
            prose_lines = [l for l in lines if not re.match(r"^[\-\*\d\.]|", l)]
            if len(prose_lines) > 10:
                long_sections.append(len(prose_lines))

    if long_sections:
        issues.append(
            {
                "type": "prose_wall",
                "severity": "low",
                "message": f"Found {len(long_sections)} sections with >10 prose lines",
                "suggestion": "Convert to tables or move to references/",
            }
        )

    return issues


def check_hallucination_risk(body: str) -> List[Dict[str, Any]]:
    """Check for hallucination risk patterns.

    Based on OWASP Agentic Skills Top 10 (Dec 2025) and 'Towards Secure Agent
    Skills' (arXiv 2604.02837). Flags unverifiable authoritative claims,
    fabricated citations, and false precision in numerical claims.
    """
    issues = []

    # Pattern 1: Authoritative statistics without citation
    # e.g. "studies show 94% of developers...", "research proves that..."
    unverified_stats = re.findall(
        r"(?:studies? (?:show|prove|find|indicate)|research (?:shows?|proves?)|"
        r"according to (?:experts?|research)|statistics show)\s+\d",
        body,
        re.IGNORECASE,
    )
    if unverified_stats:
        issues.append(
            {
                "type": "hallucination_risk",
                "severity": "high",
                "message": f"Unverified authoritative statistics ({len(unverified_stats)} instances) — cite sources or qualify with 'typically'",
                "suggestion": "Replace bare statistics with cited sources or qualified estimates (e.g. 'typically', 'in practice')",
            }
        )

    # Pattern 2: Fabricated tool/library references that may not exist
    # e.g. "use the XYZ-Pro library version 4.2.1"
    specific_version_refs = re.findall(
        r"\b(?:version|v)\s*\d+\.\d+(?:\.\d+)?\s+of\s+\w+",
        body,
        re.IGNORECASE,
    )
    if len(specific_version_refs) > 5:
        issues.append(
            {
                "type": "hallucination_risk",
                "severity": "medium",
                "message": f"Many specific version references ({len(specific_version_refs)}) may become stale or incorrect",
                "suggestion": "Use version ranges or link to official docs instead of pinning exact versions",
            }
        )

    # Pattern 3: False precision — exact percentages without context
    exact_pcts = re.findall(r"\b(?:exactly|precisely)\s+\d+(?:\.\d+)?%", body, re.IGNORECASE)
    if exact_pcts:
        issues.append(
            {
                "type": "hallucination_risk",
                "severity": "medium",
                "message": f"False precision ({len(exact_pcts)} instances of 'exactly X%') — without experimental context these mislead users",
                "suggestion": "Use approximate language ('roughly', 'approximately') or cite the study source",
            }
        )

    return issues


def check_capability_overclaiming(body: str, fm: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """Check for capability overclaiming.

    Based on PRISM (arXiv 2603.18507): expert persona prompting hurts
    factual tasks when the persona overclaims. Skills should be honest
    about their scope and constraints.
    """
    issues = []

    # Pattern 1: Claims to handle "all" or "every" type of problem
    all_claims = re.findall(
        r"\b(?:handles?|covers?|solves?|addresses?|manages?)\s+(?:all|every|any)\s+\w+",
        body,
        re.IGNORECASE,
    )
    if len(all_claims) >= 2:
        issues.append(
            {
                "type": "capability_overclaiming",
                "severity": "high",
                "message": f"Claims to handle 'all/every/any' scenarios ({len(all_claims)} instances) — per PRISM research this degrades factual accuracy",
                "suggestion": "Replace 'handles all X' with specific scope: 'handles X in context Y, escalates for Z'",
            }
        )

    # Pattern 2: Claims to be the best/most/only
    superlative_claims = re.findall(
        r"\b(?:best|most (?:powerful|advanced|comprehensive|complete)|only|#1|number (?:one|1))\b",
        body,
        re.IGNORECASE,
    )
    if len(superlative_claims) >= 3:
        issues.append(
            {
                "type": "capability_overclaiming",
                "severity": "medium",
                "message": f"Superlative capability claims ({len(superlative_claims)} instances) undermine credibility",
                "suggestion": "Replace superlatives with specific, verifiable claims",
            }
        )

    # Pattern 3: Missing Scope & Limitations section despite broad claims
    has_scope_section = bool(re.search(r"^##\s+.*(?:Scope|Limitations?|Constraints?)", body, re.MULTILINE | re.IGNORECASE))
    broad_scope = bool(re.search(r"\b(?:full[- ]?stack|end[- ]?to[- ]?end|complete solution)", body, re.IGNORECASE))
    if broad_scope and not has_scope_section:
        issues.append(
            {
                "type": "capability_overclaiming",
                "severity": "medium",
                "message": "Claims broad 'full-stack' or 'end-to-end' scope but has no Scope & Limitations section",
                "suggestion": "Add a '## Scope & Limitations' section defining what this skill doesn't handle",
            }
        )

    return issues


def check_missing_uncertainty(body: str) -> List[Dict[str, Any]]:
    """Check for missing uncertainty communication.

    Based on HELM calibration metric and OWASP Agentic Skills Top 10.
    AI agents should express appropriate uncertainty on high-stakes decisions
    rather than presenting all outputs with equal confidence.
    """
    issues = []

    # Check for high-stakes domains that need uncertainty language
    HIGH_STAKES_DOMAINS = {
        "legal": ["legal advice", "contract", "liability", "lawsuit", "court", "attorney"],
        "medical": ["diagnos", "treatment", "medication", "symptom", "prognosis", "clinical"],
        "financial": ["invest", "portfolio", "trading", "financial advice", "tax advice"],
        "security": ["vulnerabilit", "exploit", "malware", "penetration", "breach"],
    }

    detected_domains = []
    for domain, keywords in HIGH_STAKES_DOMAINS.items():
        for kw in keywords:
            if re.search(rf"\b{re.escape(kw)}", body, re.IGNORECASE):
                detected_domains.append(domain)
                break

    if not detected_domains:
        return issues

    # Check for uncertainty language
    uncertainty_markers = re.findall(
        r"\b(?:consult (?:a |an )?(?:professional|expert|specialist|attorney|doctor|advisor)|"
        r"this is not (?:legal|medical|financial) advice|"
        r"I (?:cannot|can't) guarantee|"
        r"results? (?:may|might|can) vary|"
        r"should be verified|"
        r"not a substitute for|"
        r"uncertainty|"
        r"confident(?:ly|ce)|"
        r"approximate|"
        r"typically|"
        r"in most cases|"
        r"may not apply)\b",
        body,
        re.IGNORECASE,
    )

    if len(uncertainty_markers) < 2:
        issues.append(
            {
                "type": "missing_uncertainty",
                "severity": "high",
                "message": f"High-stakes domain ({', '.join(detected_domains)}) with insufficient uncertainty communication ({len(uncertainty_markers)} markers)",
                "suggestion": "Add explicit uncertainty markers: 'results may vary', 'consult a professional for X', 'this is not [legal/medical/financial] advice'",
            }
        )

    return issues


def scan_antipatterns(file_path: Path) -> Dict[str, Any]:
    """Scan a single skill for anti-patterns."""
    try:
        content = file_path.read_text(encoding="utf-8")
    except Exception as e:
        return {"error": str(e), "path": str(file_path)}

    fm, body = parse_frontmatter(content)

    all_issues = []

    # Run all checks
    all_issues.extend(check_scope_sprawl(body))
    all_issues.extend(check_shallow_depth(body))
    all_issues.extend(check_html_in_yaml(content))
    all_issues.extend(check_generic_risk(body))
    all_issues.extend(check_platform_coverage(body))
    all_issues.extend(check_prose_wall(body))
    # New patterns (2025-2026 research)
    all_issues.extend(check_hallucination_risk(body))
    all_issues.extend(check_capability_overclaiming(body, fm))
    all_issues.extend(check_missing_uncertainty(body))

    # Count by severity
    severity_counts = {"high": 0, "medium": 0, "low": 0}
    for issue in all_issues:
        severity = issue.get("severity", "medium")
        severity_counts[severity] = severity_counts.get(severity, 0) + 1

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
        "total_issues": len(all_issues),
        "severity_counts": severity_counts,
        "issues": all_issues,
        "has_critical": severity_counts.get("high", 0) > 0,
    }


def scan_all_skills(skills_dir: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Scan all skills for anti-patterns."""
    if skills_dir is None:
        skills_dir = SKILLS_DIR

    results = []

    for skill_path in sorted(skills_dir.rglob("SKILL.md")):
        if any(x in skill_path.parts for x in ["references", "assets", "_common"]):
            continue
        result = scan_antipatterns(skill_path)
        results.append(result)

    return results


def print_antipattern_summary(results: List[Dict[str, Any]]) -> None:
    """Print anti-pattern scan summary."""
    from rich.console import Console
    from rich.table import Table

    console = Console()

    # Count issues
    total_high = sum(r.get("severity_counts", {}).get("high", 0) for r in results)
    total_medium = sum(r.get("severity_counts", {}).get("medium", 0) for r in results)
    total_low = sum(r.get("severity_counts", {}).get("low", 0) for r in results)

    console.print("\n[bold]Anti-Pattern Summary[/bold]")
    console.print(f"  Skills scanned: {len(results)}")
    console.print(f"  🔴 High severity: {total_high}")
    console.print(f"  🟡 Medium severity: {total_medium}")
    console.print(f"  🟢 Low severity: {total_low}")

    # Show problematic skills
    console.print("\n[bold yellow]Skills with Issues[/bold yellow]")
    table = Table(show_header=True)
    table.add_column("Skill")
    table.add_column("Total")
    table.add_column("High")
    table.add_column("Medium")
    table.add_column("Sample Issue")

    for r in results:
        if "error" in r:
            continue

        counts = r.get("severity_counts", {})
        if r.get("total_issues", 0) > 0:
            sample = r["issues"][0].get("message", "")[:40] if r.get("issues") else ""
            table.add_row(
                r["skill"],
                str(r.get("total_issues", 0)),
                str(counts.get("high", 0)),
                str(counts.get("medium", 0)),
                sample,
            )

    console.print(table)


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Scan skills for anti-patterns")
    parser.add_argument("--path", "-p", help="Specific skill path")
    parser.add_argument("--output", "-o", choices=["json", "text"], default="text")
    parser.add_argument(
        "--fail-on",
        choices=["high", "medium", "low"],
        help="Exit with error if issues of this severity found",
    )
    args = parser.parse_args()

    if args.path:
        result = scan_antipatterns(Path(args.path))
        if args.output == "json":
            import json

            print(json.dumps(result, indent=2))
        else:
            from rich.console import Console

            console = Console()
            console.print(f"[bold]{result['skill']}[/bold]")
            console.print(f"Total issues: {result.get('total_issues', 0)}")

            counts = result.get("severity_counts", {})
            console.print(f"  🔴 High: {counts.get('high', 0)}")
            console.print(f"  🟡 Medium: {counts.get('medium', 0)}")
            console.print(f"  🟢 Low: {counts.get('low', 0)}")

            if result.get("issues"):
                console.print("\n[bold]Issues:[/bold]")
                for issue in result["issues"][:5]:
                    console.print(
                        f"  [{issue.get('severity', 'medium').upper()}] {issue.get('message', '')}"
                    )
    else:
        results = scan_all_skills()

        if args.output == "json":
            import json

            print(json.dumps(results, indent=2))
        else:
            print_antipattern_summary(results)

            # Exit code check
            if args.fail_on:
                has_fail = False
                for r in results:
                    counts = r.get("severity_counts", {})
                    if args.fail_on == "high" and counts.get("high", 0) > 0:
                        has_fail = True
                        break
                    if args.fail_on == "medium" and (
                        counts.get("high", 0) > 0 or counts.get("medium", 0) > 0
                    ):
                        has_fail = True
                        break
                if has_fail:
                    sys.exit(1)


if __name__ == "__main__":
    main()
