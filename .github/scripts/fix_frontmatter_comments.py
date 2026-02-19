#!/usr/bin/env python3
"""
Fix HTML comment injection in YAML frontmatter (P0-3 Bug).

Removes HTML comments (<!-- ... -->) that appear inside the YAML frontmatter
block of skill files. Comments in the markdown body are left untouched.

Usage:
    python3 .github/scripts/fix_frontmatter_comments.py [--dry-run] [path ...]
"""

import sys
import re
import argparse
from pathlib import Path

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"


def fix_file(path: Path, dry_run: bool = False) -> bool:
    """
    Remove HTML comments from the YAML frontmatter of a skill file.
    Returns True if the file was (or would be) changed.
    """
    content = path.read_text(encoding="utf-8")

    if not content.startswith("---"):
        return False

    parts = content.split("---", 2)
    if len(parts) < 3:
        return False

    opening, fm_block, body = "---", parts[1], parts[2]
    original_fm = fm_block

    # Remove inline HTML comments: <!-- ... --> (single line)
    fm_block = re.sub(r"\s*<!--.*?-->\s*", "\n", fm_block, flags=re.DOTALL)

    # Remove any lines that became blank-only after comment removal
    # but preserve intentional blank lines in description blocks
    cleaned_lines = []
    prev_blank = False
    for line in fm_block.splitlines():
        stripped = line.strip()
        if stripped == "":
            if not prev_blank:
                cleaned_lines.append("")
            prev_blank = True
        else:
            cleaned_lines.append(line)
            prev_blank = False

    # Strip leading/trailing blank lines inside the frontmatter block
    while cleaned_lines and cleaned_lines[0].strip() == "":
        cleaned_lines.pop(0)
    while cleaned_lines and cleaned_lines[-1].strip() == "":
        cleaned_lines.pop()

    fm_block = "\n" + "\n".join(cleaned_lines) + "\n"

    if fm_block == original_fm:
        return False  # nothing changed

    new_content = opening + fm_block + "---" + body

    if dry_run:
        print(f"[dry-run] Would fix: {path}")
        # Show diff summary
        old_lines = original_fm.count("\n")
        new_lines = fm_block.count("\n")
        print(f"          Frontmatter lines: {old_lines} → {new_lines}")
    else:
        path.write_text(new_content, encoding="utf-8")
        print(f"Fixed: {path}")

    return True


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Remove HTML comments from YAML frontmatter in skill files."
    )
    parser.add_argument("--dry-run", action="store_true", help="Show changes without writing files")
    parser.add_argument(
        "paths",
        nargs="*",
        default=[str(SKILLS_DIR)],
        help="Files or directories to process (default: skills/)",
    )
    args = parser.parse_args()

    files: list[Path] = []
    for t in args.paths:
        p = Path(t)
        if p.is_file() and p.suffix == ".md":
            files.append(p)
        elif p.is_dir():
            files.extend(sorted(p.rglob("*.md")))

    changed = 0
    for path in files:
        if fix_file(path, dry_run=args.dry_run):
            changed += 1

    action = "Would fix" if args.dry_run else "Fixed"
    print(f"\n{action} {changed} of {len(files)} files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
