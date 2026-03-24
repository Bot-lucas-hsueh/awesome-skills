#!/usr/bin/env python3
"""
CI Quality Gate — Awesome Skills

Enforces minimum quality thresholds for skill files submitted via PR or push.
Fails the CI pipeline (exit code 1) when any changed skill violates the gates.

Usage:
    # Check specific files (e.g. changed files on a PR)
    python3 .github/scripts/quality_gate.py skills/software/backend-developer/SKILL.md

    # Check all skills
    python3 .github/scripts/quality_gate.py --all

    # Read changed files from stdin (git diff output)
    git diff --name-only origin/main...HEAD -- 'skills/**/*.md' | \\
        python3 .github/scripts/quality_gate.py --stdin

    # Override thresholds
    python3 .github/scripts/quality_gate.py --min-score 5.0 --max-tokens 6000 --all

Exit codes:
    0  All gates passed
    1  One or more gates failed (CI should block merge)
"""

import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Any, Optional

# ── Path setup ────────────────────────────────────────────────────────────────
REPO_ROOT = Path(__file__).parent.parent.parent
TOOLS_DIR = REPO_ROOT / "tools"
SKILLS_DIR = REPO_ROOT / "skills"
EXTERNAL_AUTHOR_DIRS = [
    REPO_ROOT / "external" / "aakashg",
    REPO_ROOT / "external" / "wdavidturner",
]
sys.path.insert(0, str(TOOLS_DIR))

from skill_analyzer import scorer, tokenizer  # noqa: E402

# ── Gate thresholds ───────────────────────────────────────────────────────────

# Minimum weighted quality score (0–10) for any skill to be merged.
# 4.0 = "community" tier floor; raise to 5.0+ for stricter enforcement.
DEFAULT_MIN_SCORE = 4.0

# Maximum token count for a skill body (system-prompt context budget).
# Skills exceeding this risk crowding out user context window.
DEFAULT_MAX_BODY_TOKENS = 6000

# Maximum description character count (absolute upper bound; per-tier limits
# are still checked by tokenizer but this is an unconditional hard stop).
DEFAULT_MAX_DESC_CHARS = 400

# Per-dimension minimum scores (only checked for Expert Verified skills).
# Keys match scorer.WEIGHTS keys.
EXPERT_DIMENSION_MINIMUMS: Dict[str, float] = {
    "system_prompt": 5.0,
    "domain_knowledge": 5.0,
    "workflow": 5.0,
    "risk_documentation": 4.0,
    "example_quality": 5.0,
    "metadata": 5.0,
    "content_efficiency": 4.0,
    "token_cost_efficiency": 4.0,
}

# Skills that must meet EXPERT_DIMENSION_MINIMUMS
EXPERT_SKILL_PATHS = {
    "skills/executive/ceo/SKILL.md",
    "skills/executive/cfo/SKILL.md",
    "skills/executive/cmo/SKILL.md",
    "skills/executive/coo/SKILL.md",
    "skills/executive/cto/SKILL.md",
    "skills/software/backend-developer/SKILL.md",
    "skills/software/data-scientist/SKILL.md",
    "skills/software/devops-engineer/SKILL.md",
    "skills/software/frontend-developer/SKILL.md",
    "skills/software/qa-engineer/SKILL.md",
    "skills/software/security-engineer/SKILL.md",
    "skills/software/software-architect/SKILL.md",
    "skills/software/algorithm-engineer/SKILL.md",
    "skills/software/ai-ml-engineer/SKILL.md",
    "skills/ai-ml/ai-application-engineer/SKILL.md",
    "skills/ai-ml/ai-product-manager/SKILL.md",
    "skills/ai-ml/ai-safety-researcher/SKILL.md",
    "skills/ai-ml/ai-chip-architect/SKILL.md",
    "skills/ai-ml/ai-compute-platform-engineer/SKILL.md",
    "skills/ai-ml/llm-research-scientist/SKILL.md",
    "skills/ai-ml/llm-training-engineer/SKILL.md",
    "skills/ai-ml/machine-learning-engineer/SKILL.md",
    "skills/ai-ml/prompt-engineer/SKILL.md",
    "skills/finance/cpa/SKILL.md",
    "skills/finance/financial-analyst/SKILL.md",
    "skills/finance/fund-manager/SKILL.md",
    "skills/finance/investment-analyst/SKILL.md",
    "skills/business/management-consultant/SKILL.md",
    "skills/business/strategy-consultant/SKILL.md",
    "skills/legal/legal-counsel/SKILL.md",
    "skills/legal/patent-attorney/SKILL.md",
    "skills/healthcare/general-practitioner/SKILL.md",
    "skills/healthcare/psychologist/SKILL.md",
    "skills/marketing/digital-marketing-specialist/SKILL.md",
    "skills/marketing/marketing-manager/SKILL.md",
    "skills/marketing/sales-manager/SKILL.md",
    "skills/product/product-manager/SKILL.md",
    "skills/product/ux-designer/SKILL.md",
    "skills/data/data-analyst/SKILL.md",
    "skills/data/data-engineer/SKILL.md",
    "skills/research/principal-investigator/SKILL.md",
    "skills/research/statistician/SKILL.md",
    "skills/special/skill-writer/SKILL.md",
    "skills/special/agent-persona-designer/SKILL.md",
    "skills/it-support/macos-config-expert/SKILL.md",
}


# ── Gate logic ────────────────────────────────────────────────────────────────


def collect_skill_files(paths: List[str]) -> List[Path]:
    """Resolve paths to SKILL.md files, skipping non-skill content."""
    EXCLUDED_DIRS = {"_common", "references", "agents", "assets", "evals"}
    files: List[Path] = []

    for p_str in paths:
        p = Path(p_str)
        if p.is_file() and p.suffix == ".md":
            files.append(p)
        elif p.is_dir():
            for f in sorted(p.rglob("SKILL.md")):
                if any(part in EXCLUDED_DIRS for part in f.parts):
                    continue
                files.append(f)

    return files


def get_rel_path(path: Path) -> str:
    """Return path relative to repo root."""
    try:
        return str(path.relative_to(REPO_ROOT))
    except ValueError:
        return str(path)


def check_skill(
    path: Path,
    min_score: float,
    max_body_tokens: int,
    max_desc_chars: int,
    total_skills: int,
) -> Dict[str, Any]:
    """Run all quality gates on a single skill. Returns gate result dict."""
    rel = get_rel_path(path)
    failures: List[str] = []
    warnings: List[str] = []

    # ── 1. Quality scoring ────────────────────────────────────────────────
    score_result = scorer.score_skill(path)
    if "error" in score_result:
        failures.append(f"Cannot read/score file: {score_result['error']}")
        return {"path": rel, "passed": False, "failures": failures, "warnings": warnings}

    weighted_avg = score_result["weighted_avg"]
    tier = score_result["tier"]
    scores = score_result.get("scores", {})

    if weighted_avg < min_score:
        failures.append(
            f"Quality score {weighted_avg:.2f}/10 below minimum {min_score:.1f} "
            f"(tier: {tier}). Improve the skill to reach 'community' level or higher."
        )

    # ── 2. Per-dimension minimums for Expert skills ───────────────────────
    is_expert = rel in EXPERT_SKILL_PATHS
    if is_expert:
        for dim, min_dim in EXPERT_DIMENSION_MINIMUMS.items():
            dim_score = scores.get(dim, 0)
            if dim_score < min_dim:
                failures.append(
                    f"Expert skill: dimension '{dim}' score {dim_score:.1f} "
                    f"below required minimum {min_dim:.1f}"
                )

    # ── 3. Token budget: body ─────────────────────────────────────────────
    token_result = tokenizer.analyze_token_budget(path, total_skills)
    body_tokens = token_result.get("token_count", 0)
    if body_tokens > max_body_tokens:
        failures.append(
            f"Body token count {body_tokens:,} exceeds limit {max_body_tokens:,}. "
            "Offload large reference content to references/ subdirectory."
        )
    elif body_tokens > max_body_tokens * 0.8:
        warnings.append(
            f"Body token count {body_tokens:,} is approaching limit {max_body_tokens:,} "
            f"({body_tokens / max_body_tokens * 100:.0f}%)"
        )

    # ── 4. Token budget: description ──────────────────────────────────────
    desc_info = token_result.get("description", {})
    desc_chars = desc_info.get("char_count", 0)
    desc_status = desc_info.get("status", "MISSING")

    if desc_status == "MISSING":
        failures.append("Missing 'description' field in YAML frontmatter.")
    elif desc_chars > max_desc_chars:
        failures.append(
            f"Description length {desc_chars} chars exceeds hard limit {max_desc_chars}. "
            "Shorten the description to improve token efficiency."
        )
    elif desc_status == "OVER_BUDGET":
        tier_str = desc_info.get("tier", "")
        warnings.append(
            f"Description {desc_chars}/{desc_info.get('limit', '?')} chars over tier budget "
            f"({tier_str}). Consider shortening for better token efficiency."
        )

    # ── 5. HTML in YAML ───────────────────────────────────────────────────
    html_issues = token_result.get("html_in_yaml", [])
    if html_issues:
        for issue in html_issues:
            failures.append(
                f"HTML comment in YAML frontmatter at line ~{issue['line']}: "
                f"{issue['content']!r}"
            )

    # ── 6. Content efficiency warning ────────────────────────────────────
    content_eff = scores.get("content_efficiency", 10)
    if content_eff < 4.0:
        warnings.append(
            f"Content efficiency score {content_eff:.1f}/10 is low. "
            "Check for repetitive content or prose walls."
        )

    # ── 7. Token cost efficiency warning ─────────────────────────────────
    token_eff = token_result.get("token_efficiency", {})
    eff_score = token_eff.get("score", 10)
    if eff_score < 4.0:
        warnings.append(
            f"Token efficiency score {eff_score:.1f}/10 is low. "
            "Optimize description length and body size."
        )

    cost_info = token_result.get("api_cost", {})

    return {
        "path": rel,
        "passed": len(failures) == 0,
        "failures": failures,
        "warnings": warnings,
        "quality_score": weighted_avg,
        "quality_tier": tier,
        "body_tokens": body_tokens,
        "desc_chars": desc_chars,
        "token_efficiency": eff_score,
        "cost_per_load_usd": cost_info.get("cost_per_load_usd", 0),
        "is_expert": is_expert,
    }


def run_gate(
    skill_files: List[Path],
    min_score: float,
    max_body_tokens: int,
    max_desc_chars: int,
    total_skills: int,
    output_json: bool = False,
) -> int:
    """Run quality gate on all provided skill files. Returns exit code."""
    if not skill_files:
        print("No skill files to check.")
        return 0

    results = []
    for path in skill_files:
        result = check_skill(path, min_score, max_body_tokens, max_desc_chars, total_skills)
        results.append(result)

    if output_json:
        print(json.dumps(results, indent=2))
        return 0 if all(r["passed"] for r in results) else 1

    # ── Human-readable output ─────────────────────────────────────────────
    print(f"\n{'═' * 64}")
    print(f"  Awesome Skills — Quality Gate")
    print(f"  Checking {len(skill_files)} skill(s)")
    print(f"  Min score: {min_score}  |  Max body tokens: {max_body_tokens:,}  |  Max desc chars: {max_desc_chars}")
    print(f"{'═' * 64}\n")

    failed_count = 0
    warned_count = 0

    for r in results:
        status_icon = "✅" if r["passed"] else "❌"
        warn_icon = "⚠️ " if r["warnings"] and r["passed"] else ""

        print(f"{status_icon} {warn_icon}{r['path']}")
        print(
            f"   Score: {r.get('quality_score', '?'):.2f}/10 ({r.get('quality_tier', '?')}) | "
            f"Tokens: {r.get('body_tokens', '?'):,} | "
            f"Efficiency: {r.get('token_efficiency', '?'):.1f}/10 | "
            f"Cost/load: ${r.get('cost_per_load_usd', 0):.5f}"
        )

        for failure in r["failures"]:
            print(f"   ❌ FAIL: {failure}")

        for warning in r["warnings"]:
            print(f"   ⚠️  WARN: {warning}")

        if not r["passed"]:
            failed_count += 1
        elif r["warnings"]:
            warned_count += 1

        print()

    # ── Summary ───────────────────────────────────────────────────────────
    total = len(results)
    passed = total - failed_count

    print(f"{'─' * 64}")
    print(f"Skills checked : {total}")
    print(f"Passed         : {passed}")
    print(f"Failed         : {failed_count}")
    print(f"Warnings       : {warned_count}")
    print()

    if failed_count == 0:
        if warned_count > 0:
            print(f"⚠️  Gate passed with {warned_count} warning(s). Consider addressing them.")
        else:
            print("✅ All quality gates passed.")
        return 0
    else:
        print(f"❌ {failed_count} skill(s) failed quality gate — fix before merging.")
        return 1


# ── CLI ───────────────────────────────────────────────────────────────────────


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CI Quality Gate for Awesome Skills",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="Skill files or directories to check",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="Check all skills (overrides paths)",
    )
    parser.add_argument(
        "--stdin",
        action="store_true",
        help="Read file paths from stdin (one per line)",
    )
    parser.add_argument(
        "--min-score",
        type=float,
        default=DEFAULT_MIN_SCORE,
        help=f"Minimum weighted quality score 0-10 (default: {DEFAULT_MIN_SCORE})",
    )
    parser.add_argument(
        "--max-tokens",
        type=int,
        default=DEFAULT_MAX_BODY_TOKENS,
        help=f"Maximum body token count (default: {DEFAULT_MAX_BODY_TOKENS})",
    )
    parser.add_argument(
        "--max-desc-chars",
        type=int,
        default=DEFAULT_MAX_DESC_CHARS,
        help=f"Maximum description char count (default: {DEFAULT_MAX_DESC_CHARS})",
    )
    parser.add_argument(
        "--total-skills",
        type=int,
        default=40,
        help="Total installed skills (affects description budget tier, default: 40)",
    )
    parser.add_argument(
        "--output",
        "-o",
        choices=["text", "json"],
        default="text",
        help="Output format (default: text)",
    )

    args = parser.parse_args()

    # Collect files
    if args.all:
        all_dirs = [str(SKILLS_DIR)] + [str(d) for d in EXTERNAL_AUTHOR_DIRS if d.exists()]
        skill_files = collect_skill_files(all_dirs)
    elif args.stdin:
        raw_lines = [l.strip() for l in sys.stdin.readlines() if l.strip()]
        skill_files = collect_skill_files(raw_lines)
    elif args.paths:
        skill_files = collect_skill_files(args.paths)
    else:
        parser.print_help()
        return 0

    return run_gate(
        skill_files=skill_files,
        min_score=args.min_score,
        max_body_tokens=args.max_tokens,
        max_desc_chars=args.max_desc_chars,
        total_skills=args.total_skills,
        output_json=(args.output == "json"),
    )


if __name__ == "__main__":
    sys.exit(main())
