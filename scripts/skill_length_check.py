#!/usr/bin/env python3
"""Check SKILL.md length against progressive-disclosure targets.

Anthropic's skill spec recommends SKILL.md stay short (navigation +
frontmatter) and push deep content into ``references/``. This linter
scans every SKILL.md in ``skills/`` and reports violations:

* ``warn`` threshold (default 300 lines) — informational
* ``fail`` threshold (default 800 lines) — non-zero exit

CI usage: ``python3 scripts/skill_length_check.py --fail 800``
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"


def count_lines(path: Path) -> int:
    with path.open("rb") as fh:
        return sum(1 for _ in fh)


def gather() -> list[tuple[Path, int]]:
    if not SKILLS_DIR.is_dir():
        raise SystemExit(f"skills/ not found at {SKILLS_DIR}")
    rows: list[tuple[Path, int]] = []
    for skill_md in SKILLS_DIR.rglob("SKILL.md"):
        rows.append((skill_md, count_lines(skill_md)))
    return rows


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--warn", type=int, default=300,
                        help="lines above which to warn (default 300)")
    parser.add_argument("--fail", type=int, default=800,
                        help="lines above which to fail the check (default 800)")
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--top", type=int, default=20,
                        help="show top-N worst offenders (default 20)")
    args = parser.parse_args()

    rows = sorted(gather(), key=lambda r: r[1], reverse=True)
    warn_rows = [r for r in rows if r[1] > args.warn]
    fail_rows = [r for r in rows if r[1] > args.fail]

    if args.format == "json":
        payload = {
            "total": len(rows),
            "warn_threshold": args.warn,
            "fail_threshold": args.fail,
            "over_warn": len(warn_rows),
            "over_fail": len(fail_rows),
            "top": [
                {"path": str(p.relative_to(ROOT)), "lines": n}
                for p, n in rows[: args.top]
            ],
        }
        json.dump(payload, sys.stdout, indent=2)
        sys.stdout.write("\n")
    else:
        print(f"Total SKILL.md: {len(rows)}")
        print(f"Over {args.warn} lines (warn): {len(warn_rows)}")
        print(f"Over {args.fail} lines (fail): {len(fail_rows)}")
        print()
        print(f"Top {args.top} longest:")
        for p, n in rows[: args.top]:
            marker = "FAIL" if n > args.fail else ("warn" if n > args.warn else "ok")
            print(f"  [{marker:4}] {n:5d} lines  {p.relative_to(ROOT)}")

    return 1 if fail_rows else 0


if __name__ == "__main__":
    raise SystemExit(main())
