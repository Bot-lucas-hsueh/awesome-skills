#!/usr/bin/env python3
"""
description_linter.py
=====================

Surface pairs of skills whose YAML-frontmatter ``description:`` fields overlap
heavily. Agent runtimes (Claude, OpenCode, ...) use this description for skill
*discovery* - if many skills share overlapping descriptions, the runtime picks
a random / noisy winner.

Usage
-----
    python3 scripts/description_linter.py \
        --threshold 0.6 \
        --format markdown \
        --output reports/description_overlap.md

No external dependencies are required. If PyYAML is installed it is used for
frontmatter parsing; otherwise a tiny line-based fallback parser is applied.

Exit codes
----------
    0  - success, no violations (or ``--fail-above`` not exceeded)
    1  - more than ``--fail-above`` high-similarity pairs were found
    2  - usage / IO error
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

try:  # prefer PyYAML when available; fall back to line parser otherwise
    import yaml  # type: ignore

    _HAS_YAML = True
except ImportError:  # pragma: no cover - CI installs pyyaml
    _HAS_YAML = False


# ---------------------------------------------------------------------------
# Tokenisation
# ---------------------------------------------------------------------------

STOPWORDS = frozenset(
    {
        # articles / determiners / conjunctions
        "a", "an", "the", "and", "or", "but", "nor", "so", "yet",
        # prepositions
        "for", "with", "to", "of", "in", "on", "by", "at", "from", "as",
        "into", "onto", "upon", "over", "under", "per", "via", "about",
        # common skill-boilerplate verbs / trigger words
        "use", "uses", "used", "using", "when", "this", "that", "these",
        "those", "is", "are", "was", "were", "be", "been", "being",
        "it", "its", "you", "your", "their", "his", "her", "our",
        "skill", "skills",
        # noisy helper words
        "also", "any", "all", "not", "no", "yes", "only", "more", "most",
        "than", "then", "such", "can", "will", "should", "would", "may",
        "might", "do", "does", "done", "doing",
    }
)

_PUNCT_TRANS = str.maketrans({c: " " for c in r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""})


def tokenise(text: str) -> set:
    """Lower-case, strip punctuation, split on whitespace, drop stopwords + <3 chars."""
    if not text:
        return set()
    cleaned = text.lower().translate(_PUNCT_TRANS)
    return {
        t for t in cleaned.split()
        if len(t) >= 3 and t not in STOPWORDS and not t.isdigit()
    }


def jaccard(a: set, b: set) -> float:
    if not a or not b:
        return 0.0
    inter = len(a & b)
    if inter == 0:
        return 0.0
    return inter / len(a | b)


# ---------------------------------------------------------------------------
# Frontmatter parsing
# ---------------------------------------------------------------------------

def _read_text(path: Path) -> Optional[str]:
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        print(f"warn: {path}: non-UTF-8, skipping", file=sys.stderr)
        return None
    except OSError as exc:
        print(f"warn: {path}: cannot read ({exc}), skipping", file=sys.stderr)
        return None


def _extract_frontmatter_block(text: str) -> Optional[str]:
    """Return the raw YAML frontmatter between the first pair of ``---`` lines."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return "\n".join(lines[1:i])
    return None


def _parse_fm_line_based(block: str) -> Dict[str, str]:
    """Tiny fallback parser: supports ``key: value`` and folded scalars (``>``, ``|``).

    Only the fields we actually need (``name``, ``description``) are returned.
    Lists / nested objects are ignored.
    """
    out: Dict[str, str] = {}
    lines = block.splitlines()
    i = 0
    while i < len(lines):
        raw = lines[i]
        stripped = raw.strip()
        if not stripped or stripped.startswith("#"):
            i += 1
            continue

        # Only consider top-level keys (no leading whitespace) to avoid picking
        # up nested tag / metadata values.
        if raw[:1] in (" ", "\t"):
            i += 1
            continue

        if ":" not in stripped:
            i += 1
            continue

        key, _, value = stripped.partition(":")
        key = key.strip()
        value = value.strip()

        # Folded (>) / literal (|) block scalar
        if value in (">", "|", ">-", "|-", ">+", "|+"):
            i += 1
            collected: List[str] = []
            while i < len(lines) and (lines[i].startswith((" ", "\t")) or lines[i] == ""):
                collected.append(lines[i].strip())
                i += 1
            joiner = "\n" if value.startswith("|") else " "
            out[key] = joiner.join(c for c in collected if c).strip()
            continue

        # Strip matched surrounding quotes
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ("'", '"'):
            value = value[1:-1]

        out[key] = value
        i += 1
    return out


def parse_frontmatter(text: str) -> Optional[Dict[str, str]]:
    block = _extract_frontmatter_block(text)
    if block is None:
        return None
    if _HAS_YAML:
        try:
            data = yaml.safe_load(block)
        except yaml.YAMLError:
            # A common failure: unquoted description containing ``:`` confuses
            # the YAML scanner. Fall back to the line-based parser so we still
            # recover the fields we need.
            return _parse_fm_line_based(block) or None
        if not isinstance(data, dict):
            return _parse_fm_line_based(block) or None
        result: Dict[str, str] = {}
        for key in ("name", "description"):
            val = data.get(key)
            if isinstance(val, str):
                result[key] = val
        # If PyYAML succeeded but did not yield a description, line-parse too —
        # some files use folded/multiline forms the line parser recovers fine.
        if "description" not in result:
            fallback = _parse_fm_line_based(block)
            if "description" in fallback:
                result["description"] = fallback["description"]
            if "name" not in result and "name" in fallback:
                result["name"] = fallback["name"]
        return result or None
    return _parse_fm_line_based(block) or None


# ---------------------------------------------------------------------------
# Scanning
# ---------------------------------------------------------------------------

class Skill:
    __slots__ = ("name", "description", "path", "category", "tokens")

    def __init__(self, name: str, description: str, path: Path, category: str):
        self.name = name
        self.description = description
        self.path = path
        self.category = category
        self.tokens = tokenise(description)

    def rel_path(self, root: Path) -> str:
        try:
            return str(self.path.relative_to(root))
        except ValueError:
            return str(self.path)


def _category_key(skill_path: Path, skills_root: Path) -> str:
    """Return a stable key representing 'immediate parent' (or references folder).

    - ``skills/admin/chef/SKILL.md``           -> ``admin/chef`` (parent dir)
    - ``skills/admin/chef/references/X/SKILL.md`` -> ``admin/chef/references``
    """
    rel = skill_path.relative_to(skills_root)
    parts = rel.parts[:-1]  # drop SKILL.md
    if "references" in parts:
        idx = parts.index("references")
        return "/".join(parts[: idx + 1])
    # 'Immediate parent' is the directory holding SKILL.md
    return "/".join(parts)


def scan_skills(skills_root: Path) -> Tuple[List[Skill], int, int]:
    """Walk ``skills_root`` and return parsed skills plus (skipped, warnings) counters."""
    skipped = 0
    warnings = 0
    skills: List[Skill] = []

    for md_path in sorted(skills_root.rglob("SKILL.md")):
        text = _read_text(md_path)
        if text is None:
            skipped += 1
            continue

        fm = parse_frontmatter(text)
        if fm is None:
            print(f"warn: {md_path}: no parseable frontmatter, skipping", file=sys.stderr)
            warnings += 1
            skipped += 1
            continue

        desc = (fm.get("description") or "").strip()
        if not desc:
            print(f"warn: {md_path}: empty description, skipping", file=sys.stderr)
            warnings += 1
            skipped += 1
            continue

        name = (fm.get("name") or md_path.parent.name).strip()
        category = _category_key(md_path, skills_root)
        skills.append(Skill(name=name, description=desc, path=md_path, category=category))

    return skills, skipped, warnings


# ---------------------------------------------------------------------------
# Pairwise similarity
# ---------------------------------------------------------------------------

def find_overlaps(
    skills: List[Skill],
    threshold: float,
    include_siblings: bool,
) -> List[Tuple[Skill, Skill, float]]:
    """Return pairs ``(a, b, similarity)`` with similarity >= ``threshold``.

    Pairs inside the same category (same immediate parent or same
    ``references/`` folder) are skipped unless ``include_siblings`` is True.
    """
    results: List[Tuple[Skill, Skill, float]] = []
    n = len(skills)
    for i in range(n):
        a = skills[i]
        ta = a.tokens
        if not ta:
            continue
        for j in range(i + 1, n):
            b = skills[j]
            if not include_siblings and a.category == b.category:
                continue
            tb = b.tokens
            if not tb:
                continue
            sim = jaccard(ta, tb)
            if sim >= threshold:
                results.append((a, b, sim))
    results.sort(key=lambda r: r[2], reverse=True)
    return results


# ---------------------------------------------------------------------------
# Output renderers
# ---------------------------------------------------------------------------

def _truncate(s: str, n: int = 140) -> str:
    s = " ".join(s.split())
    return s if len(s) <= n else s[: n - 1] + "\u2026"


def render_text(pairs, skills, threshold, skills_root) -> str:
    lines = [f"description-linter: threshold={threshold}"]
    if not pairs:
        lines.append("No high-similarity pairs found.")
    else:
        for a, b, sim in pairs:
            lines.append(
                f"{sim:.3f}  {a.rel_path(skills_root)}  <->  {b.rel_path(skills_root)}"
            )
            lines.append(f"         A: {_truncate(a.description)}")
            lines.append(f"         B: {_truncate(b.description)}")
    lines.append("")
    lines.append(f"{len(skills)} skills scanned, {len(pairs)} pairs above threshold")
    return "\n".join(lines) + "\n"


def render_json(pairs, skills, threshold, skills_root) -> str:
    payload = {
        "threshold": threshold,
        "skills_scanned": len(skills),
        "pairs_above_threshold": len(pairs),
        "pairs": [
            {
                "similarity": round(sim, 4),
                "a": {
                    "name": a.name,
                    "path": a.rel_path(skills_root),
                    "description": a.description,
                },
                "b": {
                    "name": b.name,
                    "path": b.rel_path(skills_root),
                    "description": b.description,
                },
            }
            for a, b, sim in pairs
        ],
    }
    return json.dumps(payload, indent=2) + "\n"


def render_markdown(pairs, skills, threshold, skills_root) -> str:
    lines = [
        "# Description-Overlap Report",
        "",
        f"- Skills scanned: **{len(skills)}**",
        f"- Similarity threshold: **{threshold}**",
        f"- Pairs above threshold: **{len(pairs)}**",
        "",
    ]
    # Bucket summary
    buckets = [0.9, 0.8, 0.7, 0.6]
    counts = {b: sum(1 for _, _, s in pairs if s >= b) for b in buckets}
    lines.append("## Bucket counts")
    lines.append("")
    lines.append("| Threshold | Pairs |")
    lines.append("|-----------|-------|")
    for b in buckets:
        lines.append(f"| >= {b:.1f} | {counts[b]} |")
    lines.append("")

    lines.append("## Top overlapping pairs")
    lines.append("")
    if not pairs:
        lines.append("_No pairs above threshold._")
    else:
        lines.append("| Similarity | Skill A | Skill B |")
        lines.append("|------------|---------|---------|")
        for a, b, sim in pairs:
            lines.append(
                f"| {sim:.3f} | `{a.rel_path(skills_root)}` | `{b.rel_path(skills_root)}` |"
            )
        lines.append("")
        lines.append("## Pair details")
        lines.append("")
        for idx, (a, b, sim) in enumerate(pairs, 1):
            lines.append(f"### {idx}. `{a.name}`  vs  `{b.name}`  ({sim:.3f})")
            lines.append("")
            lines.append(f"- **A** (`{a.rel_path(skills_root)}`): {_truncate(a.description, 400)}")
            lines.append(f"- **B** (`{b.rel_path(skills_root)}`): {_truncate(b.description, 400)}")
            lines.append("")

    lines.append("---")
    lines.append("")
    lines.append(f"_{len(skills)} skills scanned, {len(pairs)} pairs above threshold._")
    return "\n".join(lines) + "\n"


RENDERERS = {
    "text": render_text,
    "json": render_json,
    "markdown": render_markdown,
}


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _default_skills_root() -> Path:
    # Repo layout: <repo>/scripts/description_linter.py -> <repo>/skills
    return Path(__file__).resolve().parent.parent / "skills"


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description="Surface overlapping skill descriptions.")
    p.add_argument("--threshold", type=float, default=0.6,
                   help="Jaccard similarity threshold (default 0.6)")
    p.add_argument("--format", choices=("text", "json", "markdown"), default="text",
                   help="Output format (default text)")
    p.add_argument("--output", type=Path, default=None,
                   help="Output path (stdout if omitted)")
    p.add_argument("--fail-above", type=int, default=-1,
                   help="Exit 1 if more than N pairs above threshold (-1 disables)")
    p.add_argument("--include-siblings", action="store_true",
                   help="Also compare skills that share the same immediate parent")
    p.add_argument("--skills-root", type=Path, default=_default_skills_root(),
                   help="Root directory to walk (default <repo>/skills)")
    return p


def main(argv: Optional[Iterable[str]] = None) -> int:
    args = build_parser().parse_args(list(argv) if argv is not None else None)

    if not (0.0 <= args.threshold <= 1.0):
        print("error: --threshold must be in [0, 1]", file=sys.stderr)
        return 2
    if not args.skills_root.is_dir():
        print(f"error: skills root not found: {args.skills_root}", file=sys.stderr)
        return 2

    skills, skipped, warnings = scan_skills(args.skills_root)
    pairs = find_overlaps(skills, args.threshold, args.include_siblings)

    renderer = RENDERERS[args.format]
    output = renderer(pairs, skills, args.threshold, args.skills_root)

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(output, encoding="utf-8")
    else:
        sys.stdout.write(output)

    if skipped:
        print(f"note: skipped {skipped} file(s); {warnings} warning(s)", file=sys.stderr)

    if args.fail_above >= 0 and len(pairs) > args.fail_above:
        print(
            f"error: {len(pairs)} pairs above threshold (limit {args.fail_above})",
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
