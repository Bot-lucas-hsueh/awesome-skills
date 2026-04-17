#!/usr/bin/env python3
"""
Deduplicate legacy batch-generated files in skills/*/references/ folders.

Three generations of files were produced for the same conceptual topics:
  - Oldest: double-digit prefix  e.g. 07-standards.md
  - Middle: single-digit prefix  e.g. 7-standards-reference.md
  - Newest: no prefix             e.g. standards-reference.md

This script collapses each alias group down to one canonical file per topic,
keeping the newest-style name when multiple aliases are present, or the one
with more lines when the priority tier ties.

Skips any references/ folder already converted to the clean three-folder
layout (examples/, frameworks/, standards/ all present as subfolders).

Uses plain filesystem mv/rm for speed, then a single `git add -A` at the end
so that both renames and deletions are tracked by git.
"""

from __future__ import annotations

import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

# Regex matching a leading numeric prefix like "1-", "01-", "9-2-" etc.
# We only strip a single leading "<digits>-" segment per pass.
NUMBERED_PREFIX_RE = re.compile(r"^(?P<num>0?[0-9]+)-(?P<rest>.+)$")

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

# Canonical topic -> list of alias filenames (in no particular order)
CANONICAL_MAP: dict[str, list[str]] = {
    "standards.md": [
        "07-standards.md",
        "7-standards-reference.md",
        "standards-reference.md",
        "5-standards-reference.md",
        "6-standards-reference.md",
        "11-standards-reference.md",
    ],
    "workflow.md": [
        "08-workflow.md",
        "7-standard-workflow.md",
        "8-standard-workflow.md",
        "standard-workflow.md",
        "8-workflow.md",
        "08-standard-workflow.md",
        "6-standard-operating-procedures.md",
    ],
    "scenarios.md": [
        "09-scenarios.md",
        "8-scenario-examples.md",
        "9-scenario-examples.md",
        "scenario-examples.md",
        "10-examples.md",
        "11-scenarios.md",
        "10-scenario-examples.md",
    ],
    "pitfalls.md": [
        "10-pitfalls.md",
        "9-common-pitfalls.md",
        "common-pitfalls.md",
        "9-common-pitfalls-anti-patterns.md",
        "10-common-pitfalls.md",
        "11-pitfalls.md",
    ],
    "overview.md": [
        "2-what-this-skill-does.md",
        "1-what-this-skill-does.md",
        "3-what-this-skill-does.md",
    ],
    "risks.md": [
        "3-risk-disclaimer.md",
        "4-risk-disclaimer.md",
        "5-risk-disclaimer.md",
        "7-risk-documentation.md",
    ],
    "philosophy.md": [
        "4-core-philosophy.md",
        "5-core-philosophy.md",
        "3-core-philosophy.md",
    ],
    "toolkit.md": [
        "5-professional-toolkit.md",
        "6-professional-toolkit.md",
        "7-professional-toolkit.md",
        "8-professional-toolkit.md",
    ],
    "domain.md": [
        "6-domain-knowledge.md",
        "2-domain-knowledge.md",
        "4-domain-knowledge.md",
        "5-domain-knowledge.md",
    ],
    "platform.md": ["5-platform-support.md"],
    "cases.md": ["20-case-studies.md", "21-case-studies.md", "12-case-studies.md"],
    "glossary.md": ["09-glossary.md", "10-glossary.md", "11-glossary.md"],
    "troubleshooting.md": [
        "08-troubleshooting.md",
        "9-troubleshooting.md",
        "10-troubleshooting.md",
    ],
}

# Subfolders that signal a references/ folder is already in the clean layout
CLEAN_LAYOUT_SUBFOLDERS = {"examples", "frameworks", "standards"}


def prefix_tier(name: str) -> int:
    """Return priority tier: 0 = no-prefix (best), 1 = single-digit, 2 = double-digit."""
    head = name.split("-", 1)[0]
    if not head.isdigit():
        return 0
    if len(head) == 1:
        return 1
    return 2


def line_count(path: Path) -> int:
    try:
        with path.open("rb") as fh:
            return sum(1 for _ in fh)
    except OSError:
        return 0


@dataclass
class Candidate:
    path: Path
    tier: int
    lines: int

    def sort_key(self) -> tuple[int, int]:
        # lower tier wins; on tie, more lines wins (so negate)
        return (self.tier, -self.lines)


def should_skip(references_dir: Path) -> bool:
    subdirs = {p.name for p in references_dir.iterdir() if p.is_dir()}
    return CLEAN_LAYOUT_SUBFOLDERS.issubset(subdirs)


def process_references(references_dir: Path, stats: dict, anomalies: list) -> None:
    if should_skip(references_dir):
        stats["folders_skipped"] += 1
        return

    stats["folders_processed"] += 1
    touched = False

    existing_names = {p.name for p in references_dir.iterdir() if p.is_file()}

    for canonical, aliases in CANONICAL_MAP.items():
        present: list[Candidate] = []
        for alias in aliases:
            if alias in existing_names:
                p = references_dir / alias
                present.append(Candidate(p, prefix_tier(alias), line_count(p)))

        canonical_path = references_dir / canonical
        canonical_exists = canonical in existing_names

        if not present and not canonical_exists:
            continue

        if canonical_exists:
            # Treat already-canonical file as a tier-0 contender
            present.append(Candidate(canonical_path, 0, line_count(canonical_path)))

        if not present:
            continue

        present.sort(key=Candidate.sort_key)
        winner = present[0]
        losers = present[1:]

        for loser in losers:
            try:
                os.unlink(loser.path)
                stats["files_deleted"] += 1
                touched = True
            except FileNotFoundError:
                anomalies.append(f"missing loser file: {loser.path}")
            except OSError as exc:
                anomalies.append(f"failed to delete {loser.path}: {exc}")

        if winner.path != canonical_path:
            # canonical_path should not exist at this point (either absent
            # originally or just deleted as a loser). Guard anyway.
            if canonical_path.exists():
                try:
                    os.unlink(canonical_path)
                except OSError as exc:
                    anomalies.append(
                        f"could not clear canonical before rename {canonical_path}: {exc}"
                    )
                    continue
            try:
                os.rename(winner.path, canonical_path)
                stats["files_renamed"] += 1
                touched = True
            except OSError as exc:
                anomalies.append(
                    f"failed to rename {winner.path} -> {canonical_path}: {exc}"
                )

    if touched:
        stats["folders_touched"] += 1


def strip_numeric_prefixes(
    references_dir: Path, stats: dict, anomalies: list, dry_run: bool = False
) -> None:
    """Second pass: strip a leading '<digits>-' prefix from any remaining
    files under references/ folders. On collision with an already-unprefixed
    file, keep the larger (by line count) and delete the smaller. Prefer the
    unprefixed name as the winner (i.e. if unprefixed wins, remove prefixed;
    if prefixed wins, rename prefixed over unprefixed).

    We repeat until no file in the folder has a leading numeric prefix or
    until no more renames are possible (safety cap on iterations).
    """
    if should_skip(references_dir):
        return

    touched = False

    # Iterate until stable (handles nested prefixes like "9-2-foo.md" -> "2-foo.md" -> "foo.md")
    MAX_ITERS = 10
    for _ in range(MAX_ITERS):
        files = sorted(p for p in references_dir.iterdir() if p.is_file())
        candidates = [p for p in files if NUMBERED_PREFIX_RE.match(p.name)]
        if not candidates:
            break

        progress = False
        for src in candidates:
            if not src.exists():
                continue  # may have been deleted earlier this iteration
            m = NUMBERED_PREFIX_RE.match(src.name)
            if not m:
                continue
            new_name = m.group("rest")
            dst = references_dir / new_name

            if dst.exists() and dst != src:
                # Collision: keep larger, prefer the unprefixed destination as canonical.
                src_lines = line_count(src)
                dst_lines = line_count(dst)
                if dst_lines >= src_lines:
                    # Unprefixed (dst) is at least as big -> delete prefixed src.
                    if dry_run:
                        print(f"  WOULD DELETE (collision loser): {src}")
                    else:
                        try:
                            os.unlink(src)
                            stats["prefix_files_deleted"] += 1
                            touched = True
                            progress = True
                        except OSError as exc:
                            anomalies.append(f"failed to delete {src}: {exc}")
                else:
                    # Prefixed src is larger -> replace unprefixed dst with it.
                    if dry_run:
                        print(f"  WOULD REPLACE {dst} with larger {src}")
                    else:
                        try:
                            os.unlink(dst)
                            os.rename(src, dst)
                            stats["prefix_files_deleted"] += 1
                            stats["prefix_files_renamed"] += 1
                            touched = True
                            progress = True
                        except OSError as exc:
                            anomalies.append(
                                f"failed to replace {dst} with {src}: {exc}"
                            )
            else:
                # No collision: simple rename.
                if dry_run:
                    print(f"  WOULD RENAME {src} -> {dst}")
                else:
                    try:
                        os.rename(src, dst)
                        stats["prefix_files_renamed"] += 1
                        touched = True
                        progress = True
                    except OSError as exc:
                        anomalies.append(f"failed to rename {src} -> {dst}: {exc}")

        if not progress:
            break
        if dry_run:
            # In dry-run we can't actually see the filesystem change, so don't loop.
            break

    if touched:
        stats["prefix_folders_touched"] += 1


def main() -> int:
    if not SKILLS_DIR.is_dir():
        sys.stderr.write(f"skills dir not found: {SKILLS_DIR}\n")
        return 1

    dry_run = "--dry-run" in sys.argv
    skip_alias_pass = "--skip-alias-pass" in sys.argv
    skip_prefix_pass = "--skip-prefix-pass" in sys.argv

    stats = {
        "folders_processed": 0,
        "folders_skipped": 0,
        "folders_touched": 0,
        "files_deleted": 0,
        "files_renamed": 0,
        "prefix_folders_touched": 0,
        "prefix_files_renamed": 0,
        "prefix_files_deleted": 0,
    }
    anomalies: list[str] = []

    references_dirs = sorted(p for p in SKILLS_DIR.rglob("references") if p.is_dir())

    if not skip_alias_pass:
        for ref_dir in references_dirs:
            try:
                process_references(ref_dir, stats, anomalies)
            except Exception as exc:  # noqa: BLE001
                anomalies.append(f"error processing {ref_dir}: {exc}")

    if not skip_prefix_pass:
        if dry_run:
            print("\n=== DRY RUN: numeric-prefix stripping pass ===")
        for ref_dir in references_dirs:
            try:
                strip_numeric_prefixes(ref_dir, stats, anomalies, dry_run=dry_run)
            except Exception as exc:  # noqa: BLE001
                anomalies.append(f"error stripping prefixes in {ref_dir}: {exc}")

    # Stage all changes in one shot so git tracks renames + deletions.
    if dry_run:
        print("\n(DRY RUN: skipping git add)")
    else:
        print("Staging changes with `git add -A skills/`...")
        result = subprocess.run(
            ["git", "-C", str(REPO_ROOT), "add", "-A", "skills/"],
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            anomalies.append(f"git add failed: {result.stderr.strip()}")

    print("\n=== dedupe_references.py summary ===")
    print(f"  references/ folders found:      {len(references_dirs)}")
    print(f"  folders processed:              {stats['folders_processed']}")
    print(f"  folders skipped (clean layout): {stats['folders_skipped']}")
    print(f"  folders touched (alias pass):   {stats['folders_touched']}")
    print(f"  files renamed to canonical:     {stats['files_renamed']}")
    print(f"  duplicate files deleted:        {stats['files_deleted']}")
    print(f"  folders touched (prefix pass):  {stats['prefix_folders_touched']}")
    print(f"  prefixed files renamed:         {stats['prefix_files_renamed']}")
    print(f"  prefixed files deleted (colls): {stats['prefix_files_deleted']}")
    if anomalies:
        print(f"\n  anomalies ({len(anomalies)}):")
        for a in anomalies[:50]:
            print(f"    - {a}")
        if len(anomalies) > 50:
            print(f"    ... and {len(anomalies) - 50} more")
    else:
        print("\n  no anomalies")
    return 0


if __name__ == "__main__":
    sys.exit(main())
