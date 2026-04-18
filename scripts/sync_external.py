#!/usr/bin/env python3
"""Clone / fast-forward third-party skill repos declared in external/sources.yml.

Usage:
    python3 scripts/sync_external.py --list
    python3 scripts/sync_external.py --all              # clone + update every source
    python3 scripts/sync_external.py --slug <slug> ...  # clone + update specific sources
    python3 scripts/sync_external.py --all --dry-run    # show what would happen
    python3 scripts/sync_external.py --remove <slug>    # delete the local clone only

Working directories live under ``external/<slug>/`` and are gitignored. The
script performs shallow clones (``--depth=1``) by default; pass
``--full-history`` to fetch everything.
"""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    sys.stderr.write("error: PyYAML not installed — run: pip install pyyaml\n")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
EXTERNAL = ROOT / "external"
SOURCES = EXTERNAL / "sources.yml"


def load_sources() -> list[dict]:
    if not SOURCES.is_file():
        raise SystemExit(f"error: {SOURCES} not found")
    data = yaml.safe_load(SOURCES.read_text(encoding="utf-8"))
    sources = data.get("sources") or []
    for entry in sources:
        for key in ("slug", "url"):
            if not entry.get(key):
                raise SystemExit(f"error: source missing required field '{key}': {entry}")
    return sources


def run(cmd: list[str], cwd: Path | None = None, dry_run: bool = False) -> int:
    label = " ".join(cmd)
    prefix = f"[dry-run] " if dry_run else ""
    where = f" (cwd={cwd})" if cwd else ""
    print(f"{prefix}$ {label}{where}")
    if dry_run:
        return 0
    return subprocess.call(cmd, cwd=cwd)


def sync_one(entry: dict, *, full_history: bool, dry_run: bool) -> bool:
    slug = entry["slug"]
    url = entry["url"]
    branch = entry.get("branch")
    target = EXTERNAL / slug

    if target.exists():
        print(f"→ update  {slug}")
        rc = run(["git", "fetch", "--depth=1", "origin"], cwd=target, dry_run=dry_run) if not full_history \
             else run(["git", "fetch", "origin"], cwd=target, dry_run=dry_run)
        if rc != 0:
            print(f"  fetch failed for {slug}")
            return False
        target_ref = f"origin/{branch}" if branch else "origin/HEAD"
        rc = run(["git", "reset", "--hard", target_ref], cwd=target, dry_run=dry_run)
        return rc == 0

    print(f"→ clone   {slug}")
    cmd = ["git", "clone"]
    if not full_history:
        cmd += ["--depth=1"]
    if branch:
        cmd += ["--branch", branch, "--single-branch"]
    cmd += [url, str(target)]
    return run(cmd, dry_run=dry_run) == 0


def remove_one(slug: str, *, dry_run: bool) -> bool:
    target = EXTERNAL / slug
    if not target.exists():
        print(f"  nothing to remove at {target}")
        return True
    print(f"→ remove  {slug}  ({target})")
    if dry_run:
        return True
    shutil.rmtree(target)
    return True


def cmd_list(sources: list[dict]) -> int:
    width = max(len(s["slug"]) for s in sources)
    for s in sources:
        installed = (EXTERNAL / s["slug"]).is_dir()
        flag = "[installed]" if installed else "[registry ]"
        print(f"{flag}  {s['slug']:<{width}}  {s.get('category', '-')}  {s['url']}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--list", action="store_true", help="list registered sources and whether they are cloned locally")
    parser.add_argument("--all", action="store_true", help="sync every registered source")
    parser.add_argument("--slug", action="append", default=[], help="sync a specific slug (repeatable)")
    parser.add_argument("--remove", action="append", default=[], help="delete the local clone of a slug (repeatable)")
    parser.add_argument("--full-history", action="store_true", help="fetch full git history instead of shallow --depth=1")
    parser.add_argument("--dry-run", action="store_true", help="print actions without executing")
    args = parser.parse_args()

    EXTERNAL.mkdir(exist_ok=True)
    sources = load_sources()
    by_slug = {s["slug"]: s for s in sources}

    if args.list or (not args.all and not args.slug and not args.remove):
        return cmd_list(sources)

    failures: list[str] = []

    for slug in args.remove:
        if slug not in by_slug:
            print(f"warning: '{slug}' is not in sources.yml — removing clone anyway")
        if not remove_one(slug, dry_run=args.dry_run):
            failures.append(f"remove:{slug}")

    targets: list[dict] = []
    if args.all:
        targets = sources
    for slug in args.slug:
        if slug not in by_slug:
            print(f"error: unknown slug '{slug}'")
            failures.append(f"unknown:{slug}")
            continue
        entry = by_slug[slug]
        if entry not in targets:
            targets.append(entry)

    for entry in targets:
        if not sync_one(entry, full_history=args.full_history, dry_run=args.dry_run):
            failures.append(f"sync:{entry['slug']}")

    if failures:
        print(f"\nFAILED: {len(failures)} — {', '.join(failures)}")
        return 1
    print(f"\nOK: processed {len(targets)} source(s), removed {len(args.remove)}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except BrokenPipeError:
        # Caller piped our output and closed early (e.g. `| head`). Exit quietly.
        sys.stderr.close()
