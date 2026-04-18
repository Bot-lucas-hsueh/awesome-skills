#!/usr/bin/env python3
"""Insert a top-level H1 heading after the frontmatter for SKILL.md files that lack one.

The Agent Skills validator (`.github/scripts/validate_skills.py`) requires the
body of every skill to start with an `# H1` title. Several legacy skills omit
it — the body opens with a ``>`` blockquote or ``##`` section instead. This
script walks ``skills/`` and, for each SKILL.md whose body has no H1, inserts

    # <Humanized Role Name>

immediately after the closing frontmatter ``---``.

The humanized name is derived from ``name:`` in the frontmatter (fallback: the
parent folder name), converting kebab-case to Title Case.

Idempotent: a file with an existing H1 is left untouched.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "skills"


def humanize(slug: str) -> str:
    # Preserve common acronyms when re-casing.
    acronyms = {"ai", "ml", "ai-ml", "api", "sdk", "cli", "rtx", "cfo", "ceo",
                "cto", "coo", "cmo", "hr", "it", "qa", "qe", "ux", "ui", "r&d",
                "rpa", "erp", "crm", "cms", "seo", "sem", "pm", "pmo", "kpi",
                "saas", "iaas", "paas", "sre", "devops"}
    parts = slug.replace("_", "-").split("-")
    out = []
    for p in parts:
        if p.lower() in acronyms:
            out.append(p.upper().replace("&", "&"))
        else:
            out.append(p.capitalize())
    return " ".join(out)


def frontmatter_bounds(text: str) -> tuple[int, int] | None:
    """Return (start, end) indices of the frontmatter block, or None."""
    if not text.startswith("---"):
        return None
    # find the closing ---
    m = re.search(r"\n---\s*\n", text)
    if not m:
        return None
    return 0, m.end()


_H1_RE = re.compile(r"^#\s+\S", re.MULTILINE)


def has_h1(body: str) -> bool:
    """Match the validator's rule: any `# H1` line anywhere in the body."""
    return bool(_H1_RE.search(body))


def get_name(fm_text: str, folder: str) -> str:
    for line in fm_text.splitlines():
        m = re.match(r"\s*name:\s*(.+?)\s*$", line)
        if m:
            return m.group(1).strip().strip('"').strip("'")
    return folder


def process(path: Path, dry_run: bool) -> bool:
    text = path.read_text(encoding="utf-8")
    bounds = frontmatter_bounds(text)
    if not bounds:
        return False
    _, fm_end = bounds
    body = text[fm_end:]
    if has_h1(body):
        return False
    fm_text = text[:fm_end]
    name = get_name(fm_text, path.parent.name)
    heading = f"\n# {humanize(name)}\n"
    new_text = fm_text + heading + body
    if dry_run:
        print(f"[dry] would add H1 to {path.relative_to(ROOT)} → '# {humanize(name)}'")
    else:
        path.write_text(new_text, encoding="utf-8")
        print(f"fixed {path.relative_to(ROOT)} → '# {humanize(name)}'")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    changed = 0
    scanned = 0
    for p in sorted(SKILLS.rglob("SKILL.md")):
        scanned += 1
        if process(p, args.dry_run):
            changed += 1
    verb = "would fix" if args.dry_run else "fixed"
    print(f"\n{verb} {changed}/{scanned} SKILL.md files", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
