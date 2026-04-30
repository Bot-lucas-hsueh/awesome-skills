#!/usr/bin/env python3
"""Regenerate CATALOG.md from skills/**/SKILL.md frontmatter.

Structure of the generated catalog:

    # Catalog
    <N total skills auto-generated on <date>. ...>

    ## Personas (<M>) — role-based professional skills
    ### <domain> (<count>)
    | Skill | Description |
    ...

    ## Tools (<K>) — technology-specific expert skills
    ### <technology> (<count>)
    | Skill | Description |
    ...

    ## Workflows (<W>) — process-driven action skills
    ### <area> (<count>)
    | Skill | Description |
    ...

Usage:
    python3 scripts/regenerate_catalog.py            # write CATALOG.md
    python3 scripts/regenerate_catalog.py --check    # exit 1 if would differ
"""
from __future__ import annotations

import argparse
import datetime as _dt
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"
CATALOG_PATH = REPO_ROOT / "CATALOG.md"

DESC_TRUNCATE = 100


def parse_frontmatter(text: str) -> dict | None:
    """Parse frontmatter into a dict of top-level scalars.

    Intentionally does NOT use PyYAML, because many descriptions contain
    unquoted colons (e.g. "Use when: foo, bar") which are invalid YAML but
    commonplace in this repo. We only need top-level scalar keys
    (name, kind, description, version, license) plus simple folded-scalar
    support for descriptions (`description: >` followed by indented lines).
    """
    if not text.startswith("---"):
        return None
    lines = text.split("\n")
    if lines[0].rstrip() != "---":
        return None
    # find closing ---
    end_idx = None
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            end_idx = i
            break
    if end_idx is None:
        return None
    fm_lines = lines[1:end_idx]

    data: dict = {}
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        # Only top-level keys: no leading whitespace, and first ":" separates key from value.
        if not line or line.startswith(" ") or line.startswith("\t") or line.startswith("-"):
            i += 1
            continue
        colon = line.find(":")
        if colon < 0:
            i += 1
            continue
        key = line[:colon].strip()
        rest = line[colon + 1 :].strip()

        # Folded scalar: `key: >` or `key: |`
        if rest in (">", "|", ">-", "|-", ">+", "|+"):
            collected: list[str] = []
            i += 1
            while i < len(fm_lines):
                nxt = fm_lines[i]
                if nxt and not (nxt.startswith(" ") or nxt.startswith("\t")):
                    break
                collected.append(nxt.strip())
                i += 1
            if rest.startswith(">"):
                data[key] = " ".join(s for s in collected if s)
            else:
                data[key] = "\n".join(collected).rstrip()
            continue

        # Nested mapping (rest is empty): skip its indented block entirely.
        if rest == "":
            i += 1
            while i < len(fm_lines):
                nxt = fm_lines[i]
                if not nxt:
                    i += 1
                    continue
                if nxt.startswith(" ") or nxt.startswith("\t") or nxt.startswith("-"):
                    i += 1
                    continue
                break
            continue

        # Plain scalar. Strip quotes if fully quoted.
        value = rest
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
            value = value[1:-1]
        data[key] = value
        i += 1

    return data


_KIND_CONTAINERS = {"persona", "tool", "workflow"}


def category_for(skill_md: Path) -> str:
    """Derive domain/category from path relative to skills/.

    New 3-tier structure:
    - skills/<kind>/<domain>/<name>/SKILL.md  -> <domain>
    - skills/<kind>/<domain>/<sub>/<name>/SKILL.md -> <domain>/<sub>

    Legacy flat structure (fallback):
    - skills/<cat>/<name>/SKILL.md -> <cat>
    """
    rel = skill_md.relative_to(SKILLS_ROOT)
    parts = rel.parts
    if parts and parts[0] in _KIND_CONTAINERS and len(parts) >= 3:
        # New: kind / domain / [sub...] / name / SKILL.md
        category_parts = parts[1:-2]
        return "/".join(category_parts) if category_parts else "(root)"
    # Legacy: category_parts are everything except the last two (name + SKILL.md)
    category_parts = parts[:-2]
    return "/".join(category_parts) if category_parts else "(root)"


def truncate_desc(desc: str) -> str:
    # Normalize whitespace (multiline folded descriptions become one line).
    desc = " ".join(desc.split())
    if len(desc) > DESC_TRUNCATE:
        return desc[:DESC_TRUNCATE].rstrip() + "..."
    return desc


def md_escape_cell(text: str) -> str:
    """Escape pipes and newlines so table cells stay on one row."""
    return text.replace("|", "\\|").replace("\n", " ").replace("\r", " ")


def relative_link(skill_md: Path) -> str:
    rel = skill_md.relative_to(REPO_ROOT)
    return "./" + rel.as_posix()


def collect_skills() -> list[dict]:
    """Walk skills/ and return a list of skill records.

    Each record: {name, kind, category, description, path, link}.
    Skills missing name/description are warned and skipped.
    """
    records: list[dict] = []
    for skill_md in sorted(SKILLS_ROOT.rglob("SKILL.md")):
        rel = skill_md.relative_to(SKILLS_ROOT)
        if rel.parts and rel.parts[0] == "_common":
            continue
        try:
            text = skill_md.read_text(encoding="utf-8")
        except Exception as e:
            print(f"WARN: cannot read {skill_md}: {e}", file=sys.stderr)
            continue
        fm = parse_frontmatter(text)
        if not fm:
            print(f"WARN: no/invalid frontmatter, skipping: {skill_md}", file=sys.stderr)
            continue
        name = fm.get("name")
        desc = fm.get("description")
        if not name:
            print(f"WARN: missing name, skipping: {skill_md}", file=sys.stderr)
            continue
        if not desc:
            print(f"WARN: missing description, skipping: {skill_md}", file=sys.stderr)
            continue
        kind = fm.get("kind") or "persona"
        records.append({
            "name": str(name).strip(),
            "kind": str(kind).strip(),
            "category": category_for(skill_md),
            "description": truncate_desc(str(desc)),
            "path": skill_md,
            "link": relative_link(skill_md),
        })
    return records


_KIND_SECTION = {
    "persona": "Personas",
    "tool": "Tools",
    "workflow": "Workflows",
}


def _section_for_kind(kind: str) -> str:
    return _KIND_SECTION.get(kind, kind.title() + "s")


def _build_kind_section(title: str, records: list[dict], lines: list[str]) -> None:
    lines.append(f"## {title} ({len(records)})")
    lines.append("")
    if not records:
        lines.append("_None._")
        lines.append("")
        return

    by_cat: dict[str, list[dict]] = {}
    for r in records:
        by_cat.setdefault(r["category"], []).append(r)

    for cat in sorted(by_cat.keys()):
        items = sorted(by_cat[cat], key=lambda x: x["name"].lower())
        lines.append(f"### {cat} ({len(items)})")
        lines.append("")
        lines.append("| Skill | Description |")
        lines.append("|-------|-------------|")
        for r in items:
            lines.append(
                f"| [{md_escape_cell(r['name'])}]({r['link']}) "
                f"| {md_escape_cell(r['description'])} |"
            )
        lines.append("")


def build_catalog(records: list[dict], today: str) -> str:
    total = len(records)

    personas = [r for r in records if r["kind"] == "persona"]
    tools = [r for r in records if r["kind"] == "tool"]
    workflows = [r for r in records if r["kind"] == "workflow"]
    others = [r for r in records if r["kind"] not in ("persona", "tool", "workflow")]

    lines: list[str] = []
    lines.append("# Catalog")
    lines.append("")
    lines.append(
        f"<{total} total skills auto-generated on {today}. "
        f"To regenerate: `python3 scripts/regenerate_catalog.py`>"
    )
    lines.append("")

    _build_kind_section("Personas", personas, lines)
    _build_kind_section("Tools", tools, lines)
    _build_kind_section("Workflows", workflows, lines)

    if others:
        _build_kind_section("Other", others, lines)

    return "\n".join(lines).rstrip() + "\n"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true",
                    help="Exit 1 if CATALOG.md would differ from a fresh regeneration; do not write.")
    args = ap.parse_args()

    records = collect_skills()
    today = _dt.date.today().isoformat()
    new_content = build_catalog(records, today)

    if args.check:
        old = CATALOG_PATH.read_text(encoding="utf-8") if CATALOG_PATH.exists() else ""
        if old != new_content:
            print(
                "CATALOG.md is out of date. Run: python3 scripts/regenerate_catalog.py",
                file=sys.stderr,
            )
            return 1
        print("CATALOG.md is up to date.")
        return 0

    CATALOG_PATH.write_text(new_content, encoding="utf-8")
    print(
        f"Wrote {CATALOG_PATH.relative_to(REPO_ROOT)} "
        f"({len(records)} skills, {len(new_content)} bytes)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
