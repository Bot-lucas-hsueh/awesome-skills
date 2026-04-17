#!/usr/bin/env python3
"""Tag every SKILL.md with a `kind:` frontmatter field.

Rules:
- `kind: tool-skill` if the SKILL.md's directory contains a `scripts/` OR `assets/`
  subdirectory with at least one real file (recursively).
- `kind: persona` otherwise.

The `kind:` line is inserted immediately after the `name:` line if missing,
or updated in place if present. Idempotent — running twice in a row produces
zero modifications on the second run.

Skips:
- `skills/_common/` (infrastructure, not a skill)
- Any file that is not named exactly `SKILL.md`

Usage:
    python3 scripts/tag_skills_kind.py [--root skills]
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ROOT = REPO_ROOT / "skills"


def dir_has_real_file(directory: Path) -> bool:
    """Return True if `directory` exists and contains at least one file (recursively)."""
    if not directory.is_dir():
        return False
    for p in directory.rglob("*"):
        if p.is_file():
            return True
    return False


def determine_kind(skill_md: Path) -> str:
    """tool-skill if scripts/ or assets/ sibling has a file; else persona."""
    parent = skill_md.parent
    if dir_has_real_file(parent / "scripts") or dir_has_real_file(parent / "assets"):
        return "tool-skill"
    return "persona"


def split_frontmatter(text: str) -> tuple[list[str] | None, str]:
    """Return (frontmatter_lines_without_fences, body_including_closing_fence_and_rest).

    If there is no frontmatter, returns (None, original_text).
    The returned body STARTS with the closing `---` line so we can reconstruct
    the file as: "---\n" + "\n".join(fm_lines) + "\n" + body.
    """
    if not text.startswith("---"):
        return None, text
    # Split on newline, keep simple
    lines = text.split("\n")
    # first line is "---"
    if lines[0].rstrip() != "---":
        return None, text
    # find closing ---
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            fm_lines = lines[1:i]
            body = "\n".join(lines[i:])  # body starts with closing "---"
            return fm_lines, body
    return None, text


def find_top_level_key_index(fm_lines: list[str], key: str) -> int | None:
    """Return the index of the top-level (un-indented) YAML key line, or None."""
    prefix = f"{key}:"
    for i, line in enumerate(fm_lines):
        # top-level => no leading whitespace
        if line.startswith(prefix) and (len(line) == len(prefix) or line[len(prefix)] in (" ", "\t", "")):
            return i
    return None


def upsert_kind(fm_lines: list[str], kind: str) -> tuple[list[str], bool]:
    """Insert or update `kind:` line. Returns (new_lines, changed)."""
    desired = f"kind: {kind}"
    kind_idx = find_top_level_key_index(fm_lines, "kind")

    if kind_idx is not None:
        if fm_lines[kind_idx].rstrip() == desired:
            return fm_lines, False
        new_lines = list(fm_lines)
        new_lines[kind_idx] = desired
        return new_lines, True

    # Insert right after `name:` (top-level). If name: is missing, insert at top.
    name_idx = find_top_level_key_index(fm_lines, "name")
    insert_at = (name_idx + 1) if name_idx is not None else 0
    new_lines = list(fm_lines)
    new_lines.insert(insert_at, desired)
    return new_lines, True


def process_file(skill_md: Path) -> str:
    """Return one of: 'unchanged', 'persona', 'tool-skill', 'skipped'."""
    text = skill_md.read_text(encoding="utf-8")
    fm_lines, body = split_frontmatter(text)
    if fm_lines is None:
        print(f"WARN: no frontmatter in {skill_md}", file=sys.stderr)
        return "skipped"

    kind = determine_kind(skill_md)
    new_fm, changed = upsert_kind(fm_lines, kind)

    if not changed:
        return "unchanged"

    new_text = "---\n" + "\n".join(new_fm) + "\n" + body
    skill_md.write_text(new_text, encoding="utf-8")
    return kind


def iter_skill_files(root: Path):
    for p in sorted(root.rglob("SKILL.md")):
        # Skip _common infra
        try:
            rel = p.relative_to(root)
        except ValueError:
            continue
        if rel.parts and rel.parts[0] == "_common":
            continue
        yield p


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--root", type=Path, default=DEFAULT_ROOT,
                    help="Root directory to scan (default: skills/)")
    args = ap.parse_args()

    root: Path = args.root
    if not root.is_dir():
        print(f"ERROR: root not found: {root}", file=sys.stderr)
        return 2

    counts = {"persona": 0, "tool-skill": 0, "unchanged": 0, "skipped": 0}
    for skill_md in iter_skill_files(root):
        result = process_file(skill_md)
        counts[result] = counts.get(result, 0) + 1

    print(
        f"{counts['persona']} skills tagged persona, "
        f"{counts['tool-skill']} tagged tool-skill, "
        f"{counts['unchanged']} unchanged"
    )
    if counts["skipped"]:
        print(f"{counts['skipped']} skipped (no frontmatter)", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
