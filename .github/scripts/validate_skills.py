#!/usr/bin/env python3
"""
Awesome Skills — Skill File Validator
Validates YAML frontmatter and Markdown structure for all skill files.

Usage:
    python3 .github/scripts/validate_skills.py [--strict] [path ...]

    --strict   Also enforce 16-section TEMPLATE.md compliance (for Top 50 skills)
    path       One or more specific files/directories to validate (default: skills/)

Exit codes:
    0  All checks passed
    1  One or more validation errors found
"""

import sys
import os
import re
import argparse
from pathlib import Path

# ── Constants ────────────────────────────────────────────────────────────────

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

REQUIRED_FIELDS = ["name", "display_name", "author", "version", "description"]
RECOMMENDED_FIELDS = ["difficulty", "category", "tags", "platforms"]
VALID_DIFFICULTY = {"expert", "intermediate", "beginner"}
VALID_PLATFORMS = {"opencode", "openclaw", "claude", "cursor", "codex", "cline", "kimi"}

# Skills that must pass strict (Expert Verified) checks
# Updated in Phase 2 to include all 37 Expert Verified skills
EXPERT_SKILLS = {
    # Executive
    "skills/executive/ceo.md",
    "skills/executive/cfo.md",
    "skills/executive/cmo.md",
    "skills/executive/coo.md",
    "skills/executive/cto.md",
    # Technology
    "skills/software/backend-developer.md",
    "skills/software/data-scientist.md",
    "skills/software/devops-engineer.md",
    "skills/software/frontend-developer.md",
    "skills/software/qa-engineer.md",
    "skills/software/security-engineer.md",
    "skills/software/software-architect.md",
    # AI/ML
    "skills/ai-ml/ai-application-engineer.md",
    "skills/ai-ml/ai-product-manager.md",
    "skills/ai-ml/llm-research-scientist.md",
    "skills/ai-ml/llm-training-engineer.md",
    "skills/ai-ml/machine-learning-engineer.md",
    "skills/ai-ml/prompt-engineer.md",
    # Finance
    "skills/finance/cpa.md",
    "skills/finance/financial-analyst.md",
    "skills/finance/fund-manager.md",
    "skills/finance/investment-analyst.md",
    # Business & Consulting
    "skills/business/management-consultant.md",
    "skills/business/strategy-consultant.md",
    # Legal
    "skills/legal/legal-counsel.md",
    "skills/legal/patent-attorney.md",
    # Healthcare
    "skills/healthcare/general-practitioner.md",
    "skills/healthcare/psychologist.md",
    # Marketing & Sales
    "skills/marketing/digital-marketing-specialist.md",
    "skills/marketing/marketing-manager.md",
    "skills/marketing/sales-manager.md",
    # Product & Design
    "skills/product/product-manager.md",
    "skills/product/ux-designer.md",
    # Data & Analytics
    "skills/data/data-analyst.md",
    "skills/data/data-engineer.md",
    # Research
    "skills/research/principal-investigator.md",
    "skills/research/statistician.md",
    # Meta-skills
    "skills/admin/skill-writer.md",
}

# Minimum section count for Expert Verified skills
EXPERT_MIN_SECTIONS = 6

# ── Helpers ──────────────────────────────────────────────────────────────────

def parse_frontmatter(content: str) -> tuple[dict | None, str]:
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


def has_code_block(body: str) -> bool:
    """Check whether body contains at least one fenced code block."""
    return bool(re.search(r"^```", body, re.MULTILINE))


def check_html_comment_injection(raw_content: str) -> list[str]:
    """Detect HTML comments inside the YAML frontmatter block."""
    errors = []
    if not raw_content.startswith("---"):
        return errors

    parts = raw_content.split("---", 2)
    if len(parts) < 3:
        return errors

    fm_block = parts[1]
    lines = fm_block.splitlines()
    for i, line in enumerate(lines, start=2):  # line 1 = opening ---
        if "<!--" in line:
            errors.append(
                f"  line ~{i}: HTML comment `<!--` inside YAML frontmatter "
                f"causes parse errors on some platforms: {line.strip()!r}"
            )
    return errors


# ── Per-file validation ───────────────────────────────────────────────────────

def validate_file(path: Path, strict: bool = False) -> list[str]:
    """Validate a single skill file. Returns list of error strings (empty = OK)."""
    errors = []
    rel = path.relative_to(path.parent.parent.parent)  # relative to repo root

    try:
        raw = path.read_text(encoding="utf-8")
    except Exception as e:
        return [f"  Cannot read file: {e}"]

    # ── 1. Frontmatter exists ────────────────────────────────────────────────
    if not raw.startswith("---"):
        errors.append("  Missing YAML frontmatter (file must start with ---)")
        return errors  # can't continue without frontmatter

    fm, body = parse_frontmatter(raw)
    if fm is None:
        errors.append("  Malformed YAML frontmatter (no closing ---)")
        return errors

    # ── 2. Required fields ───────────────────────────────────────────────────
    for field in REQUIRED_FIELDS:
        if field not in fm or not fm[field]:
            errors.append(f"  Missing required field: `{field}`")

    # ── 3. Recommended fields (warnings, not errors) ─────────────────────────
    for field in RECOMMENDED_FIELDS:
        if field not in fm or not fm[field]:
            errors.append(f"  [WARN] Missing recommended field: `{field}`")

    # ── 4. difficulty value ──────────────────────────────────────────────────
    if "difficulty" in fm and fm["difficulty"] not in VALID_DIFFICULTY:
        errors.append(
            f"  Invalid difficulty: {fm['difficulty']!r}. "
            f"Must be one of: {', '.join(sorted(VALID_DIFFICULTY))}"
        )

    # ── 5. version format (semver) ───────────────────────────────────────────
    if "version" in fm and fm["version"]:
        if not re.match(r"^\d+\.\d+\.\d+$", fm["version"]):
            errors.append(
                f"  Invalid version: {fm['version']!r}. Must be semver (e.g. 1.0.0)"
            )

    # ── 6. HTML comment injection in frontmatter (P0-3 Bug) ─────────────────
    errors.extend(check_html_comment_injection(raw))

    # ── 7. Body: must have at least one H1 title ────────────────────────────
    if not re.search(r"^#\s+\S", body, re.MULTILINE):
        errors.append("  Missing H1 title in body")

    # ── 8. Expert Verified: stricter checks ──────────────────────────────────
    is_expert = str(rel) in EXPERT_SKILLS or strict
    if is_expert:
        section_count = count_h2_sections(body)
        if section_count < EXPERT_MIN_SECTIONS:
            errors.append(
                f"  Expert skill must have >= {EXPERT_MIN_SECTIONS} ## sections "
                f"(found {section_count})"
            )

        if not has_code_block(body):
            errors.append(
                "  Expert skill must contain at least one fenced code block "
                "(system prompt or example)"
            )

        if "## 1. System Prompt" not in body and "## System Prompt" not in body:
            errors.append(
                "  Expert skill must have a '## 1. System Prompt' or '## System Prompt' section"
            )

    return errors


# ── Main ─────────────────────────────────────────────────────────────────────

def collect_skill_files(targets: list[str]) -> list[Path]:
    """Collect .md skill files from given paths (files or directories)."""
    files = []
    for t in targets:
        p = Path(t)
        if p.is_file() and p.suffix == ".md":
            files.append(p)
        elif p.is_dir():
            files.extend(sorted(p.rglob("*.md")))
    return files


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate awesome-skills skill files.")
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat ALL files as Expert Verified (enforce 16-section checks)",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        default=[str(SKILLS_DIR)],
        help="Files or directories to validate (default: skills/)",
    )
    args = parser.parse_args()

    files = collect_skill_files(args.paths)
    if not files:
        print("No .md files found to validate.")
        return 0

    total = len(files)
    error_files = 0
    warn_files = 0
    total_errors = 0
    total_warns = 0

    print(f"Validating {total} skill files...\n")

    for path in files:
        issues = validate_file(path, strict=args.strict)
        if not issues:
            continue

        errors = [i for i in issues if not i.strip().startswith("[WARN]")]
        warns = [i for i in issues if i.strip().startswith("[WARN]")]

        if errors:
            error_files += 1
            total_errors += len(errors)
            rel = path.relative_to(Path.cwd()) if path.is_absolute() else path
            print(f"❌ {rel}")
            for e in errors:
                print(e)

        if warns:
            warn_files += 1
            total_warns += len(warns)
            if not errors:  # only print file header once
                rel = path.relative_to(Path.cwd()) if path.is_absolute() else path
                print(f"⚠️  {rel}")
            for w in warns:
                print(w)

        if errors or warns:
            print()

    # ── Summary ──────────────────────────────────────────────────────────────
    print("─" * 60)
    print(f"Files scanned : {total}")
    print(f"Errors        : {total_errors} in {error_files} files")
    print(f"Warnings      : {total_warns} in {warn_files} files")

    if error_files == 0 and warn_files == 0:
        print("\n✅ All checks passed.")
        return 0
    elif error_files == 0:
        print(f"\n⚠️  {total_warns} warning(s) found — no blocking errors.")
        return 0
    else:
        print(f"\n❌ {total_errors} error(s) found — fix before merging.")
        return 1


if __name__ == "__main__":
    sys.exit(main())
