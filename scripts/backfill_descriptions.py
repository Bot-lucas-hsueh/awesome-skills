#!/usr/bin/env python3
"""Backfill `description:` frontmatter field on SKILL.md files that lack one.

Targets the files reported by `regenerate_catalog.py --check` as
"missing description". Idempotent: a second run is a no-op.

Usage:
    python3 scripts/backfill_descriptions.py                 # apply
    python3 scripts/backfill_descriptions.py --dry-run       # no writes
    python3 scripts/backfill_descriptions.py --only PATH     # one file

Description sourcing (in order):
    1. First `description:` line found in the body (after the first
       `---`...`---` frontmatter block). The repo convention embeds
       a second frontmatter-style block mid-file that often contains a
       curated one-liner -- use that when present and non-trivial.
    2. First usable prose paragraph in the body (skipping markdown
       headings, tables, code fences, horizontal rules, blank lines,
       list bullets). First 1-2 sentences, truncated to ~280 chars.
    3. Synthesized from `name:` (or fallback parent-dir slug):
       "Expert <Role> skill. Use when: <role> tasks, <role> outputs."

YAML-safety: wraps in double quotes (escaping internal `"`) whenever
the description contains YAML-problematic chars (`:`, `#`, `[`, `]`,
`{`, `}`, newlines, leading indicators).
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_ROOT = REPO_ROOT / "skills"

MAX_DESC = 280


# --------------------------------------------------------------------------
# Frontmatter location
# --------------------------------------------------------------------------

def locate_frontmatter(text: str) -> tuple[int, int] | None:
    """Return (start_line_idx, end_line_idx) for the first --- ... --- block.

    Indices are into text.split("\n"); the --- lines themselves are included.
    """
    lines = text.split("\n")
    if not lines or lines[0].rstrip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].rstrip() == "---":
            return (0, i)
    return None


def parse_fm_block(fm_lines: list[str]) -> dict[str, str]:
    """Lightweight top-level scalar parse (mirrors regenerate_catalog)."""
    data: dict[str, str] = {}
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        if (
            not line
            or line.startswith(" ")
            or line.startswith("\t")
            or line.startswith("-")
        ):
            i += 1
            continue
        colon = line.find(":")
        if colon < 0:
            i += 1
            continue
        key = line[:colon].strip()
        rest = line[colon + 1 :].strip()

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

        if rest == "":
            # nested mapping -- skip indented block
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

        value = rest
        if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
            value = value[1:-1]
        data[key] = value
        i += 1
    return data


# --------------------------------------------------------------------------
# Description sourcing
# --------------------------------------------------------------------------

TRIVIAL_DESC_PATTERNS = [
    # "Expert skill for Evaluation Report - name" and close variants
    re.compile(r"evaluation\s+report", re.I),
    # Placeholder "Expert skill for X" / "Expert skill for X Y Z"
    # without any richer content (no periods, comma-list, or "Use when")
    re.compile(r"^\s*expert skill for\s+[A-Za-z0-9 &'\-]+\.?\s*$", re.I),
]

SENTENCE_SPLIT = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9])")


def _is_trivial(desc: str) -> bool:
    if not desc:
        return True
    for pat in TRIVIAL_DESC_PATTERNS:
        if pat.search(desc):
            return True
    return False


def _clean(s: str) -> str:
    s = s.strip()
    # collapse internal whitespace
    s = re.sub(r"\s+", " ", s)
    return s


def _truncate_sentences(text: str, max_chars: int = MAX_DESC) -> str:
    text = _clean(text)
    if not text:
        return ""
    sentences = SENTENCE_SPLIT.split(text)
    out = sentences[0]
    if len(sentences) > 1 and len(out) + 1 + len(sentences[1]) <= max_chars:
        out = out + " " + sentences[1]
    if len(out) > max_chars:
        out = out[: max_chars - 3].rstrip() + "..."
    return out


def extract_embedded_description(body: str) -> str | None:
    """Look for a `description:` line in the body. Return cleaned value or None."""
    for m in re.finditer(r"^description:\s*(.*)$", body, re.MULTILINE):
        raw = m.group(1).strip()
        if raw in ("", "|", ">", "|-", ">-", "|+", ">+"):
            continue
        # strip surrounding quotes if fully quoted
        if len(raw) >= 2 and raw[0] == raw[-1] and raw[0] in ('"', "'"):
            raw = raw[1:-1]
        raw = _clean(raw)
        if _is_trivial(raw):
            continue
        if len(raw) < 20:
            continue
        if len(raw) > MAX_DESC:
            raw = raw[: MAX_DESC - 3].rstrip() + "..."
        return raw
    return None


SKIP_LINE_RE = re.compile(
    r"""^(
        \s*$                        # blank
        | \s*\#{1,6}\s              # markdown heading
        | \s*---+\s*$               # hr / frontmatter fence
        | \s*\*\*\*+\s*$            # alt hr
        | \s*\|.*\|                 # table row
        | \s*[-*+]\s                # bullet
        | \s*\d+\.\s                # numbered
        | \s*>                      # blockquote
        | \s*`{3,}                  # code fence (treated as transparent)
        | \s*~{3,}                  # code fence
    )""",
    re.VERBOSE,
)

# Metadata-style lines we don't want as a description source.
METADATA_LINE_RE = re.compile(
    r"""^\s*(
        \*{1,2}\s*(version|created|author|updated|license|tags?|last[ _-]?updated|domain|source|category)\b
        | (name|description|license|version|kind|tags?|metadata|author|subtype|domain|level|source|updated|created)\s*:
        | see\s+also\b
        | copyright\b
    )""",
    re.VERBOSE | re.IGNORECASE,
)

# YAML key: "value" lines -- clearly structured data, not prose.
YAML_KV_RE = re.compile(r"""^\s*[a-z_][a-z0-9_]*\s*:\s*["']""", re.IGNORECASE)
# Simple "key:" on a line (possibly nested) with no value -- structural.
YAML_KEY_RE = re.compile(r"""^\s*[a-z_][a-z0-9_]*\s*:\s*$""", re.IGNORECASE)


EVAL_JARGON_RE = re.compile(
    r"\b(rubric score|quality tier|identical quality|anti-pattern|"
    r"exemplary tier|verdict|evaluation report)\b",
    re.IGNORECASE,
)


def _flush_paragraph(paragraph: list[str]) -> str | None:
    if not paragraph:
        return None
    joined = _clean(" ".join(paragraph))
    # Strip leading markdown emphasis markers
    joined = re.sub(r"^[\*_]{1,3}\s*", "", joined)
    if len(joined) < 40:
        return None
    # Reject if paragraph looks like a pipe-table row remnant
    if joined.count("|") >= 3:
        return None
    # Reject metadata-ish lines
    if METADATA_LINE_RE.match(joined):
        return None
    # Reject paragraphs that look like evaluation-report content
    if EVAL_JARGON_RE.search(joined):
        return None
    return _truncate_sentences(joined)


def _strip_html_comments(body: str) -> str:
    return re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL)


def extract_first_prose_paragraph(body: str) -> str | None:
    """Return the first substantive prose paragraph from body.

    Treats ``` code fences as transparent so role-definition prose commonly
    wrapped in fences is still reachable.
    """
    body = _strip_html_comments(body)
    lines = body.split("\n")
    paragraph: list[str] = []
    for raw in lines:
        stripped = raw.rstrip()
        if (
            SKIP_LINE_RE.match(stripped)
            or METADATA_LINE_RE.match(stripped)
            or YAML_KV_RE.match(stripped)
            or YAML_KEY_RE.match(stripped)
        ):
            got = _flush_paragraph(paragraph)
            if got:
                return got
            paragraph = []
            continue
        paragraph.append(stripped)
    return _flush_paragraph(paragraph)


def humanize(slug: str) -> str:
    """Turn 'uav-flight-control-engineer' into 'UAV flight control engineer'."""
    UPPER_TOKENS = {
        "uav", "ai", "ml", "nlp", "llm", "gpu", "cpu", "fpga", "asic",
        "pcb", "iot", "ntn", "v2x", "api", "ios", "os", "sdk", "qa",
        "ux", "ui", "sre", "devops", "seo", "saas", "paas", "iaas",
        "rf", "em", "dsp", "hpc", "qc", "hr", "pr",
    }
    parts = slug.split("-")
    humanized = []
    for i, p in enumerate(parts):
        if p.lower() in UPPER_TOKENS:
            humanized.append(p.upper())
        elif i == 0:
            humanized.append(p.capitalize())
        else:
            humanized.append(p.lower())
    return " ".join(humanized)


def synthesize_description(name: str) -> str:
    role = humanize(name)
    role_lc = role.lower()
    return (
        f"Expert {role_lc} skill. "
        f"Use when: {role_lc} tasks, {role_lc} deliverables, "
        f"{role_lc} decisions."
    )


# --------------------------------------------------------------------------
# YAML-safe serialization
# --------------------------------------------------------------------------

YAML_UNSAFE_CHARS = set(":#[]{}")


def yaml_escape(desc: str) -> str:
    """Return a YAML-safe scalar for the given description."""
    desc = _clean(desc)
    needs_quote = False
    if any(c in YAML_UNSAFE_CHARS for c in desc) or "\n" in desc:
        needs_quote = True
    if desc and desc[0] in "!&*?|>%@`,[]{}#":
        needs_quote = True
    if desc and (desc[0] in " " or desc[-1] in " "):
        needs_quote = True
    if not needs_quote:
        return desc
    # escape backslashes and double quotes for double-quoted YAML scalar
    escaped = desc.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


# --------------------------------------------------------------------------
# Core backfill
# --------------------------------------------------------------------------

def _name_from_fm_or_dir(fm: dict[str, str], skill_md: Path) -> str:
    name = fm.get("name", "").strip()
    if name:
        return name
    # slug-case parent dir
    parent = skill_md.parent.name
    return parent.lower().strip().replace(" ", "-").replace("_", "-")


def backfill_one(skill_md: Path, dry_run: bool = False) -> tuple[str, str | None]:
    """Backfill `description:` in one SKILL.md.

    Returns (status, description) where status is one of:
      - "ok"         : description inserted
      - "already"    : already had a non-empty description
      - "no-fm"      : no valid frontmatter block
      - "error:<msg>": unexpected failure
    """
    text = skill_md.read_text(encoding="utf-8")
    loc = locate_frontmatter(text)
    if loc is None:
        return ("no-fm", None)

    start, end = loc
    lines = text.split("\n")
    fm_lines = lines[start + 1 : end]
    fm = parse_fm_block(fm_lines)

    existing = fm.get("description", "")
    if isinstance(existing, str) and existing.strip():
        return ("already", existing)

    body = "\n".join(lines[end + 1 :])

    # If the body is an "Evaluation Report" document (detect by header or
    # rubric markers near the top), skip prose extraction entirely.
    body_head = body[:2000].lower()
    is_eval_report = (
        "rubric score" in body_head
        or "evaluation report" in body_head
        or "quality tier" in body_head
    )

    desc: str | None = None
    if not is_eval_report:
        # Source 1: embedded description in body (repo's convention).
        desc = extract_embedded_description(body)
        # Source 2: first prose paragraph
        if not desc:
            desc = extract_first_prose_paragraph(body)

    # Source 3: synthesize
    synthesized = False
    if not desc:
        name = _name_from_fm_or_dir(fm, skill_md)
        desc = synthesize_description(name)
        synthesized = True

    desc = _clean(desc)
    if len(desc) > MAX_DESC:
        desc = desc[: MAX_DESC - 3].rstrip() + "..."

    yaml_value = yaml_escape(desc)
    new_line = f"description: {yaml_value}"

    # Remove any existing empty "description:" line (e.g. `description: |` with
    # no indented continuation) so we don't create duplicates.
    new_fm_lines: list[str] = []
    i = 0
    removed_empty = False
    while i < len(fm_lines):
        ln = fm_lines[i]
        stripped = ln.strip()
        if stripped.startswith("description:") and not removed_empty:
            # check if it's empty (rest is empty, |, >, or just whitespace)
            rest = stripped[len("description:"):].strip()
            if rest in ("", "|", ">", "|-", ">-", "|+", ">+"):
                # skip this line and any immediately-following indented
                # continuation lines
                i += 1
                while i < len(fm_lines) and (
                    fm_lines[i].startswith(" ") or fm_lines[i].startswith("\t")
                ):
                    i += 1
                removed_empty = True
                continue
        new_fm_lines.append(ln)
        i += 1

    # Insert after `name:` line (top-level), or at top if no name
    insert_idx = 0
    for idx, ln in enumerate(new_fm_lines):
        stripped = ln.lstrip()
        if (
            not ln.startswith(" ")
            and not ln.startswith("\t")
            and not ln.startswith("-")
            and stripped.startswith("name:")
        ):
            insert_idx = idx + 1
            break
    new_fm_lines.insert(insert_idx, new_line)

    # Reassemble
    new_lines = lines[: start + 1] + new_fm_lines + lines[end:]
    new_text = "\n".join(new_lines)

    if not dry_run:
        skill_md.write_text(new_text, encoding="utf-8")

    return ("ok" + (":synth" if synthesized else ""), desc)


# --------------------------------------------------------------------------
# Discovery
# --------------------------------------------------------------------------

def find_offenders() -> list[Path]:
    offenders: list[Path] = []
    for skill_md in sorted(SKILLS_ROOT.rglob("SKILL.md")):
        rel = skill_md.relative_to(SKILLS_ROOT)
        if rel.parts and rel.parts[0] == "_common":
            continue
        try:
            text = skill_md.read_text(encoding="utf-8")
        except Exception:
            continue
        loc = locate_frontmatter(text)
        if loc is None:
            continue
        start, end = loc
        fm_lines = text.split("\n")[start + 1 : end]
        fm = parse_fm_block(fm_lines)
        desc = fm.get("description", "")
        if not (isinstance(desc, str) and desc.strip()):
            offenders.append(skill_md)
    return offenders


# --------------------------------------------------------------------------
# CLI
# --------------------------------------------------------------------------

def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="Do not write files.")
    ap.add_argument(
        "--only",
        type=str,
        default=None,
        help="Operate on just this one SKILL.md path (absolute or repo-relative).",
    )
    args = ap.parse_args()

    if args.only:
        p = Path(args.only)
        if not p.is_absolute():
            p = REPO_ROOT / p
        targets = [p]
    else:
        targets = find_offenders()

    backfilled = 0
    skipped = 0
    failed: list[tuple[Path, str]] = []
    synth: list[Path] = []

    for skill_md in targets:
        try:
            status, desc = backfill_one(skill_md, dry_run=args.dry_run)
        except Exception as e:  # noqa: BLE001
            failed.append((skill_md, f"error: {e}"))
            continue

        rel = skill_md.relative_to(REPO_ROOT)
        if status == "already":
            skipped += 1
            continue
        if status == "no-fm":
            failed.append((skill_md, "no frontmatter"))
            continue
        backfilled += 1
        if status.endswith(":synth"):
            synth.append(skill_md)
        verb = "[DRY]" if args.dry_run else "[OK] "
        print(f"{verb} {rel}: {desc[:120]}")

    print("")
    print(
        f"Backfilled {backfilled} descriptions "
        f"(skipped {skipped} already-had-one)"
    )
    if synth:
        print(f"Synthesized from name for {len(synth)} file(s):")
        for p in synth:
            print(f"  - {p.relative_to(REPO_ROOT)}")
    if failed:
        print(f"Failed {len(failed)}:", file=sys.stderr)
        for p, why in failed:
            print(f"  - {p.relative_to(REPO_ROOT)}: {why}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
