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
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
SKILLS_DIR = REPO_ROOT / "skills"

# Canonical topic -> list of alias filenames (in no particular order)
CANONICAL_MAP: dict[str, list[str]] = {
    "standards.md": ["07-standards.md", "7-standards-reference.md", "standards-reference.md"],
    "workflow.md": [
        "08-workflow.md",
        "7-standard-workflow.md",
        "8-standard-workflow.md",
        "standard-workflow.md",
    ],
    "scenarios.md": [
        "09-scenarios.md",
        "8-scenario-examples.md",
        "9-scenario-examples.md",
        "scenario-examples.md",
    ],
    "pitfalls.md": ["10-pitfalls.md", "9-common-pitfalls.md", "common-pitfalls.md"],
    "overview.md": ["2-what-this-skill-does.md"],
    "risks.md": ["3-risk-disclaimer.md"],
    "philosophy.md": ["4-core-philosophy.md"],
    "toolkit.md": ["5-professional-toolkit.md", "6-professional-toolkit.md"],
    "domain.md": ["6-domain-knowledge.md"],
    "platform.md": ["5-platform-support.md"],
    "cases.md": ["20-case-studies.md"],
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


def main() -> int:
    if not SKILLS_DIR.is_dir():
        sys.stderr.write(f"skills dir not found: {SKILLS_DIR}\n")
        return 1

    stats = {
        "folders_processed": 0,
        "folders_skipped": 0,
        "folders_touched": 0,
        "files_deleted": 0,
        "files_renamed": 0,
    }
    anomalies: list[str] = []

    references_dirs = sorted(p for p in SKILLS_DIR.rglob("references") if p.is_dir())

    for ref_dir in references_dirs:
        try:
            process_references(ref_dir, stats, anomalies)
        except Exception as exc:  # noqa: BLE001
            anomalies.append(f"error processing {ref_dir}: {exc}")

    # Stage all changes in one shot so git tracks renames + deletions.
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
    print(f"  folders touched (any change):   {stats['folders_touched']}")
    print(f"  files renamed to canonical:     {stats['files_renamed']}")
    print(f"  duplicate files deleted:        {stats['files_deleted']}")
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
