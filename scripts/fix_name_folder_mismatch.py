#!/usr/bin/env python3
"""Normalize each SKILL.md's ``name:`` field to match its parent folder name.

The Agent Skills spec identifies a skill by its folder; the ``name:`` field
in frontmatter must agree. This fixer walks ``skills/`` and, for every
SKILL.md whose declared ``name:`` differs from the parent directory, rewrites
the ``name:`` line to the folder name. Idempotent.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"

NAME_LINE_RE = re.compile(r"^(name:)\s*.*$", re.MULTILINE)


def frontmatter_end(text: str) -> int:
    if not text.startswith("---"):
        return -1
    m = re.search(r"\n---\s*\n", text)
    return m.end() if m else -1


def current_name(fm: str) -> str | None:
    for line in fm.splitlines():
        m = re.match(r"\s*name:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return None


def process(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    end = frontmatter_end(text)
    if end < 0:
        return False
    fm = text[:end]
    body = text[end:]
    name = current_name(fm)
    folder = path.parent.name
    if name == folder:
        return False
    new_fm, n = NAME_LINE_RE.subn(f"name: {folder}", fm, count=1)
    if n == 0:
        # No name: line at all; insert after opening ---.
        new_fm = fm.replace("---\n", f"---\nname: {folder}\n", 1)
    if new_fm == fm:
        return False
    if dry_run:
        print(f"[dry] {path.relative_to(ROOT)}: {name!r} → {folder!r}")
    else:
        path.write_text(new_fm + body, encoding="utf-8")
        print(f"fixed {path.relative_to(ROOT)}: {name!r} → {folder!r}")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    changed = 0
    for p in sorted(SKILLS.rglob("SKILL.md")):
        if process(p, args.dry_run):
            changed += 1
    verb = "would fix" if args.dry_run else "fixed"
    print(f"\n{verb} {changed} SKILL.md files", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
