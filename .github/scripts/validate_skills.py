#!/usr/bin/env python3
"""
Awesome Skills — Skill File Validator
Validates YAML frontmatter and Markdown structure for all skill files.

Supports two skill formats (per Agent Skills standard — https://agentskills.io):
  1. Flat file:  skills/{category}/{skill-name}.md
  2. Folder:     skills/{category}/{skill-name}/SKILL.md

Usage:
    python3 .github/scripts/validate_skills.py [--strict] [path ...]

    --strict   Also enforce 16-section TEMPLATE.md compliance (for Expert Verified skills)
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
from typing import Optional, Dict, Any, List, Tuple

try:
    import json as _json
    _SCHEMA_PATH = Path(__file__).parent.parent.parent / "schema" / "frontmatter.schema.json"
    _FRONTMATTER_SCHEMA: Optional[Dict[str, Any]] = None
    if _SCHEMA_PATH.exists():
        with open(_SCHEMA_PATH) as _f:
            _FRONTMATTER_SCHEMA = _json.load(_f)
    try:
        import jsonschema as _jsonschema
        _JSONSCHEMA_AVAILABLE = True
    except ImportError:
        _JSONSCHEMA_AVAILABLE = False
except Exception:
    _FRONTMATTER_SCHEMA = None
    _JSONSCHEMA_AVAILABLE = False

try:
    import yaml as _yaml
    _YAML_AVAILABLE = True
except ImportError:
    _YAML_AVAILABLE = False

# ── Constants ────────────────────────────────────────────────────────────────

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"
_EXTERNAL_AUTHOR_DIRS = [
    SKILLS_DIR.parent / "benchmarks" / "aakashg",
    SKILLS_DIR.parent / "benchmarks" / "wdavidturner",
]

REQUIRED_FIELDS = ["name", "display_name", "author", "version", "description"]
RECOMMENDED_FIELDS = ["difficulty", "category", "tags", "platforms", "quality"]
VALID_DIFFICULTY = {"expert", "intermediate", "beginner"}
VALID_PLATFORMS = {"opencode", "openclaw", "claude", "cursor", "codex", "cline", "kimi"}
VALID_QUALITY = {"basic", "community", "expert", "exemplary"}

# Skills that must pass strict (Expert Verified) checks
# Updated to new folder format (skills/category/skill-name/SKILL.md)
EXPERT_SKILLS = {
    # Executive
    "skills/persona/executive/ceo/SKILL.md",
    "skills/persona/executive/cfo/SKILL.md",
    "skills/persona/executive/cmo/SKILL.md",
    "skills/persona/executive/coo/SKILL.md",
    "skills/persona/executive/cto/SKILL.md",
    # Technology
    "skills/persona/software/backend-developer/SKILL.md",
    "skills/persona/software/data-scientist/SKILL.md",
    "skills/persona/software/devops-engineer/SKILL.md",
    "skills/persona/software/frontend-developer/SKILL.md",
    "skills/persona/software/qa-engineer/SKILL.md",
    "skills/persona/software/security-engineer/SKILL.md",
    "skills/persona/software/software-architect/SKILL.md",
    "skills/persona/software/algorithm-engineer/SKILL.md",
    "skills/persona/software/ai-ml-engineer/SKILL.md",
    # AI/ML
    "skills/persona/ai-ml/ai-application-engineer/SKILL.md",
    "skills/persona/ai-ml/ai-product-manager/SKILL.md",
    "skills/persona/ai-ml/ai-safety-researcher/SKILL.md",
    "skills/persona/ai-ml/ai-chip-architect/SKILL.md",
    "skills/persona/ai-ml/ai-compute-platform-engineer/SKILL.md",
    "skills/persona/ai-ml/llm-research-scientist/SKILL.md",
    "skills/persona/ai-ml/llm-training-engineer/SKILL.md",
    "skills/persona/ai-ml/machine-learning-engineer/SKILL.md",
    "skills/persona/ai-ml/prompt-engineer/SKILL.md",
    # Finance
    "skills/persona/finance/cpa/SKILL.md",
    "skills/persona/finance/financial-analyst/SKILL.md",
    "skills/persona/finance/fund-manager/SKILL.md",
    "skills/persona/finance/investment-analyst/SKILL.md",
    # Business & Consulting
    "skills/persona/business/management-consultant/SKILL.md",
    "skills/persona/business/strategy-consultant/SKILL.md",
    # Legal
    "skills/persona/legal/legal-counsel/SKILL.md",
    "skills/persona/legal/patent-attorney/SKILL.md",
    # Healthcare
    "skills/persona/healthcare/general-practitioner/SKILL.md",
    "skills/persona/healthcare/psychologist/SKILL.md",
    # Marketing & Sales
    "skills/persona/marketing/digital-marketing-specialist/SKILL.md",
    "skills/persona/marketing/marketing-manager/SKILL.md",
    "skills/persona/marketing/sales-manager/SKILL.md",
    # Product & Design
    "skills/persona/product/product-manager/SKILL.md",
    "skills/persona/product/ux-designer/SKILL.md",
    # Data & Analytics
    "skills/persona/data/data-analyst/SKILL.md",
    "skills/persona/data/data-engineer/SKILL.md",
    # Research
    "skills/persona/research/principal-investigator/SKILL.md",
    "skills/persona/research/statistician/SKILL.md",
    # Special
    "skills/persona/special/skill-writer/SKILL.md",
    "skills/persona/special/agent-persona-designer/SKILL.md",
    "skills/persona/it-support/macos-config-expert/SKILL.md",
}

# Minimum H2 section count for Expert Verified skills (full 16-section structure)
EXPERT_MIN_SECTIONS = 16

# ── Helpers ──────────────────────────────────────────────────────────────────


def parse_frontmatter(content: str) -> Tuple[Optional[Dict[str, Any]], str]:
    """Extract YAML frontmatter and body from markdown content.

    Uses pyyaml.safe_load when available for correct handling of lists,
    nested mappings, and multi-line values. Falls back to a simple parser.
    """
    if not content.startswith("---"):
        return None, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content

    fm_raw = parts[1]
    body = parts[2]

    if _YAML_AVAILABLE:
        try:
            fm = _yaml.safe_load(fm_raw) or {}
            return fm, body
        except _yaml.YAMLError:
            pass  # fall through to simple parser

    fm: Dict[str, Any] = {}
    for line in fm_raw.splitlines():
        line = line.strip()
        if ":" in line and not line.startswith("#"):
            key, _, val = line.partition(":")
            val = val.strip().strip('"').strip("'")
            fm[key.strip()] = val

    return fm, body


def validate_frontmatter_schema(fm: Dict[str, Any]) -> List[str]:
    """Validate frontmatter dict against JSON Schema. Returns list of error strings."""
    if not _JSONSCHEMA_AVAILABLE or _FRONTMATTER_SCHEMA is None:
        return []
    errors = []
    try:
        validator = _jsonschema.Draft202012Validator(_FRONTMATTER_SCHEMA)
        for error in sorted(validator.iter_errors(fm), key=lambda e: e.path):
            path = ".".join(str(p) for p in error.path) or "(root)"
            errors.append(f"  [schema] {path}: {error.message}")
    except Exception as e:
        errors.append(f"  [schema] Validation error: {e}")
    return errors


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

# Folder-based skills (SKILL.md) follow the Agent Skills minimum spec:
# only `name` and `description` are required. The awesome-skills extended
# fields are recommended but not required for Agent Skills compatibility.
AGENT_SKILLS_REQUIRED = ["name", "description"]


def validate_file(path: Path, strict: bool = False) -> list[str]:
    """Validate a single skill file. Returns list of error strings (empty = OK).

    Folder-based skills (SKILL.md) are validated against the Agent Skills
    minimum spec (name + description required only). Flat .md skill files
    are validated against the full awesome-skills spec.
    """
    errors = []
    rel = path.relative_to(path.parent.parent.parent)  # relative to repo root

    # Detect folder-based skill (SKILL.md inside a named subdirectory)
    is_folder_skill = path.name == "SKILL.md"

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
    # Folder skills: Agent Skills minimum spec (name + description only)
    # Flat files: full awesome-skills required fields
    required = AGENT_SKILLS_REQUIRED if is_folder_skill else REQUIRED_FIELDS
    for field in required:
        if field not in fm or not fm[field]:
            errors.append(f"  Missing required field: `{field}`")

    # ── 2b. Folder skill: name must match parent directory name ───────────────
    if is_folder_skill and "name" in fm and fm["name"]:
        folder_name = path.parent.name
        if fm["name"] != folder_name:
            errors.append(
                f"  Agent Skills: `name` field ({fm['name']!r}) must match "
                f"parent folder name ({folder_name!r})"
            )

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

    # ── 4b. quality value ────────────────────────────────────────────────────
    if "quality" in fm and fm["quality"] and fm["quality"] not in VALID_QUALITY:
        errors.append(
            f"  Invalid quality: {fm['quality']!r}. "
            f"Must be one of: {', '.join(sorted(VALID_QUALITY))}"
        )

    # ── 5. version format (semver) ───────────────────────────────────────────
    if "version" in fm and fm["version"]:
        if not re.match(r"^\d+\.\d+\.\d+$", fm["version"]):
            errors.append(
                f"  Invalid version: {fm['version']!r}. Must be semver (e.g. 1.0.0)"
            )

    # ── 5b. JSON Schema validation (when jsonschema + schema file available) ──
    if _JSONSCHEMA_AVAILABLE and _FRONTMATTER_SCHEMA is not None and fm:
        errors.extend(validate_frontmatter_schema(fm))

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

        if not re.search(r"^##.*[Ss]ystem\s+[Pp]rompt", body, re.MULTILINE):
            errors.append(
                "  Expert skill must have a System Prompt section "
                "(e.g. '## 1. System Prompt', '## System Prompt', or '## § 1 · System Prompt')"
            )

    return errors


# ── Main ─────────────────────────────────────────────────────────────────────


def collect_skill_files(targets: list[str]) -> list[Path]:
    """Collect .md skill files from given paths (files or directories).

    Supports two formats:
      - Flat files: any .md file directly under a category directory
      - Folder skills: SKILL.md files inside skill subdirectories

    Excludes non-skill content:
      - _common/  — shared content fragments
      - references/ — reference docs bundled with folder skills (not skill entrypoints)
      - agents/   — sub-agent instruction files bundled with folder skills
      - assets/   — asset directories inside folder skills
      - evals/    — evaluation files inside folder skills
    """
    EXCLUDED_DIRS = {"_common", "references", "agents", "assets", "evals"}
    # Helper / meta docs that may sit alongside a skill (or one level above it)
    # and must not be validated as skill files themselves.
    EXCLUDED_FILENAMES = {
        "README.md",
        "PROFILE_NOTES.md",
        "EVALUATION_REPORT.md",
        "RESTORATION_REPORT.md",
        "CHANGELOG.md",
    }
    files = []
    for t in targets:
        p = Path(t)
        if p.is_file() and p.suffix == ".md":
            files.append(p)
        elif p.is_dir():
            for f in sorted(p.rglob("*.md")):
                # Skip files inside excluded subdirectories
                if any(part in EXCLUDED_DIRS for part in f.parts):
                    continue
                # Skip well-known helper filenames regardless of location
                if f.name in EXCLUDED_FILENAMES:
                    continue
                # For folder-based skills: only validate SKILL.md (the entrypoint)
                # Skip other .md files that happen to be inside skill folders
                parent = f.parent
                if f.name != "SKILL.md" and (parent / "SKILL.md").exists():
                    continue
                # Skip loose .md in a dir that has any SKILL.md anywhere below —
                # such docs are category-level notes, not skills.
                if f.name != "SKILL.md" and any(parent.rglob("SKILL.md")):
                    continue
                files.append(f)
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
        default=[str(SKILLS_DIR)] + [str(d) for d in _EXTERNAL_AUTHOR_DIRS if d.exists()],
        help="Files or directories to validate (default: skills/ + external author dirs)",
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
