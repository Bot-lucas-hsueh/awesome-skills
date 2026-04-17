#!/usr/bin/env python3
"""Sync the authoritative skill count into README.md and index.html.

Counts every second-level directory under ``skills/`` (one directory per
skill) and rewrites the badge + stat markers in the web/README assets so
the surfaced numbers match reality.
"""

from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
README = ROOT / "README.md"
INDEX_HTML = ROOT / "index.html"


def count_skills() -> int:
    if not SKILLS_DIR.is_dir():
        raise SystemExit(f"skills/ not found at {SKILLS_DIR}")
    return sum(
        1
        for category in SKILLS_DIR.iterdir()
        if category.is_dir() and not category.name.startswith("_")
        for role in category.iterdir()
        if role.is_dir()
    )


def update_readme(count: int) -> bool:
    text = README.read_text(encoding="utf-8")
    new = re.sub(
        r"(img\.shields\.io/badge/skills-)\d+(-blueviolet)",
        rf"\g<1>{count}\g<2>",
        text,
    )
    new = re.sub(
        r"\*\*A curated library of role-based AI skills[^\n]*",
        "**A curated library of role-based AI skills, organised by professional domain.**",
        new,
    )
    new = re.sub(
        r"(A library of \*\*)\d+(\s*skill files\*\*)",
        rf"\g<1>{count}\g<2>",
        new,
    )
    new = re.sub(
        r"(共 \*\*)\d+(\s*个技能\*\*)",
        rf"\g<1>{count}\g<2>",
        new,
    )
    if new != text:
        README.write_text(new, encoding="utf-8")
        return True
    return False


def update_index(count: int) -> bool:
    text = INDEX_HTML.read_text(encoding="utf-8")
    new = re.sub(
        r'(id="skillCount">)\d+(</div>)',
        rf"\g<1>{count}\g<2>",
        text,
    )
    new = re.sub(
        r'(heroSubtitle">)[^<]*(</p>)',
        rf"\g<1>{count} expert skills. One command away.\g<2>",
        new,
        count=1,
    )
    # Chinese heroSubtitle (must come before the generic English one so the
    # generic pattern does not clobber the zh locale).
    new = re.sub(
        r"(heroSubtitle: ')[^']*专家技能[^']*(',)",
        rf"\g<1>{count} 专家技能，一键安装。\g<2>",
        new,
    )
    new = re.sub(
        r"(heroSubtitle: ')[^']*expert skills[^']*(',)",
        rf"\g<1>{count} expert skills. One command away.\g<2>",
        new,
    )
    new = re.sub(
        r'(footerText">)\d+(\s*Expert Skills)',
        rf"\g<1>{count}\g<2>",
        new,
    )
    if new != text:
        INDEX_HTML.write_text(new, encoding="utf-8")
        return True
    return False


def main() -> None:
    count = count_skills()
    print(f"Counted {count} skills under skills/")
    changed = []
    if update_readme(count):
        changed.append("README.md")
    if update_index(count):
        changed.append("index.html")
    if changed:
        print(f"Updated: {', '.join(changed)}")
    else:
        print("No changes (counts already in sync)")


if __name__ == "__main__":
    main()
