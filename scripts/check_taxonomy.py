#!/usr/bin/env python3
"""check_taxonomy.py — validate taxonomy.yml against the real filesystem.

Checks:
  1. Every skills/<subfolder> (except entries in ignore.skills) is listed as
     an alias under exactly one category in taxonomy.yml.
  2. Every packages/*.md is referenced by some category's `package:` field.
  3. Every roadmap/*.md (except entries in ignore.roadmap) is referenced
     by some category's `roadmap:` field or listed under extra_roadmaps.
  4. Every alias in taxonomy.yml has a corresponding skills/<alias>/ dir.
  5. Every category's `skills_dir`, `package`, and `roadmap` path (if set)
     points to something that actually exists on disk.
  6. No alias appears in more than one category.

Exits 0 on success, 1 on any failure.

Usage:
    python3 scripts/check_taxonomy.py [--verbose]
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Install with: pip install pyyaml", file=sys.stderr)
    sys.exit(2)


REPO_ROOT = Path(__file__).resolve().parent.parent
TAXONOMY_PATH = REPO_ROOT / "taxonomy.yml"
SKILLS_DIR = REPO_ROOT / "skills"
PACKAGES_DIR = REPO_ROOT / "packages"
ROADMAP_DIR = REPO_ROOT / "roadmap"


def load_taxonomy() -> dict:
    if not TAXONOMY_PATH.exists():
        print(f"ERROR: {TAXONOMY_PATH} not found", file=sys.stderr)
        sys.exit(2)
    with TAXONOMY_PATH.open("r", encoding="utf-8") as f:
        return yaml.safe_load(f)


def list_skills_subdirs() -> set[str]:
    if not SKILLS_DIR.is_dir():
        return set()
    return {p.name for p in SKILLS_DIR.iterdir() if p.is_dir()}


def list_dir_files(directory: Path, suffix: str = ".md") -> set[str]:
    if not directory.is_dir():
        return set()
    return {p.name for p in directory.iterdir() if p.is_file() and p.suffix == suffix}


def rel(p: str | Path) -> str:
    """Return a repo-root-relative path string."""
    pp = Path(p)
    if pp.is_absolute():
        try:
            return str(pp.relative_to(REPO_ROOT))
        except ValueError:
            return str(pp)
    return str(pp)


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate taxonomy.yml against the repo.")
    parser.add_argument("--verbose", "-v", action="store_true", help="Show happy-path details")
    args = parser.parse_args()

    taxonomy = load_taxonomy()
    categories = taxonomy.get("categories", []) or []
    ignore = taxonomy.get("ignore", {}) or {}
    extra_roadmaps = taxonomy.get("extra_roadmaps", {}) or {}
    extra_packages = taxonomy.get("extra_packages", {}) or {}

    ignore_skills = set(ignore.get("skills", []) or [])
    ignore_roadmap = set(ignore.get("roadmap", []) or [])
    ignore_packages = set(ignore.get("packages", []) or [])

    errors: list[str] = []
    warnings: list[str] = []
    info: list[str] = []

    # Build lookup: alias -> category id
    alias_to_cat: dict[str, str] = {}
    duplicate_aliases: list[tuple[str, str, str]] = []
    category_ids: set[str] = set()

    for cat in categories:
        cid = cat.get("id")
        if not cid:
            errors.append(f"Category missing `id`: {cat!r}")
            continue
        if cid in category_ids:
            errors.append(f"Duplicate category id: {cid}")
        category_ids.add(cid)

        for alias in cat.get("aliases", []) or []:
            if alias in alias_to_cat:
                duplicate_aliases.append((alias, alias_to_cat[alias], cid))
            else:
                alias_to_cat[alias] = cid

    for alias, first_cat, second_cat in duplicate_aliases:
        errors.append(
            f"Alias `{alias}` appears in multiple categories: `{first_cat}` and `{second_cat}`"
        )

    # ---------- Check 1: every skills/<subfolder> is aliased somewhere ----------
    skills_subdirs = list_skills_subdirs()
    orphan_skills = []
    for sub in sorted(skills_subdirs):
        if sub in ignore_skills:
            continue
        if sub not in alias_to_cat:
            orphan_skills.append(sub)

    for sub in orphan_skills:
        errors.append(f"Orphan: skills/{sub}/ is not listed as an alias in any taxonomy category")

    # ---------- Check 4: every alias maps to an existing skills/<alias>/ dir ----
    for alias, cid in sorted(alias_to_cat.items()):
        if not (SKILLS_DIR / alias).is_dir():
            # This is a warning, not an error, since taxonomy is advisory
            # and aliases may reference pre-existing concepts not yet foldered.
            warnings.append(
                f"Alias `{alias}` (category `{cid}`) has no corresponding skills/{alias}/ directory"
            )

    # ---------- Check 2: every packages/*.md is referenced ----------
    package_files = list_dir_files(PACKAGES_DIR, ".md")
    referenced_packages: set[str] = set()
    for cat in categories:
        pkg = cat.get("package")
        if pkg:
            referenced_packages.add(Path(pkg).name)
            # And check that file actually exists
            pkg_path = REPO_ROOT / pkg
            if not pkg_path.is_file():
                errors.append(
                    f"Category `{cat.get('id')}` references missing package file: {rel(pkg)}"
                )

    for cid, extras in extra_packages.items():
        if cid not in category_ids:
            errors.append(f"extra_packages references unknown category id: {cid}")
        for pkg in extras or []:
            referenced_packages.add(Path(pkg).name)
            pkg_path = REPO_ROOT / pkg
            if not pkg_path.is_file():
                errors.append(
                    f"extra_packages[{cid}] references missing package file: {rel(pkg)}"
                )

    ignore_package_names = {Path(p).name for p in ignore_packages}
    unreferenced_packages = package_files - referenced_packages - ignore_package_names
    for f in sorted(unreferenced_packages):
        errors.append(
            f"Orphan: packages/{f} is not referenced by any category's `package:` field "
            f"(add to a category, to extra_packages, or to ignore.packages)"
        )

    # ---------- Check 3: every roadmap/*.md is referenced or ignored ----------
    roadmap_files = list_dir_files(ROADMAP_DIR, ".md")
    referenced_roadmaps: set[str] = set()
    for cat in categories:
        rm = cat.get("roadmap")
        if rm:
            referenced_roadmaps.add(Path(rm).name)
            rm_path = REPO_ROOT / rm
            if not rm_path.is_file():
                errors.append(
                    f"Category `{cat.get('id')}` references missing roadmap file: {rel(rm)}"
                )

    for cid, extras in extra_roadmaps.items():
        if cid not in category_ids:
            errors.append(f"extra_roadmaps references unknown category id: {cid}")
        for rm in extras or []:
            referenced_roadmaps.add(Path(rm).name)
            rm_path = REPO_ROOT / rm
            if not rm_path.is_file():
                errors.append(
                    f"extra_roadmaps[{cid}] references missing roadmap file: {rel(rm)}"
                )

    ignore_roadmap_names = {Path(p).name for p in ignore_roadmap}
    unreferenced_roadmaps = roadmap_files - referenced_roadmaps - ignore_roadmap_names
    for f in sorted(unreferenced_roadmaps):
        errors.append(
            f"Orphan: roadmap/{f} is not referenced by any category's `roadmap:` field "
            f"(add to a category, to extra_roadmaps, or to ignore.roadmap)"
        )

    # ---------- Check 5: skills_dir paths exist ----------
    for cat in categories:
        sd = cat.get("skills_dir")
        if sd:
            sd_path = REPO_ROOT / sd
            if not sd_path.is_dir():
                warnings.append(
                    f"Category `{cat.get('id')}` skills_dir does not exist: {rel(sd)}"
                )

    # ---------- Happy path info ----------
    if args.verbose:
        info.append(f"Categories defined: {len(category_ids)}")
        info.append(f"Total aliases: {len(alias_to_cat)}")
        info.append(f"skills/ subfolders (non-ignored): {len(skills_subdirs - ignore_skills)}")
        info.append(f"packages/ files: {len(package_files)}")
        info.append(f"roadmap/ files: {len(roadmap_files)}")
        info.append("")
        info.append("Category → aliases:")
        for cat in categories:
            cid = cat.get("id", "?")
            aliases = cat.get("aliases", []) or []
            info.append(f"  {cid}: {', '.join(aliases)}")

    # ---------- Output ----------
    if info:
        for line in info:
            print(line)
        print()

    if warnings:
        print("WARNINGS:")
        for w in warnings:
            print(f"  - {w}")
        print()

    if errors:
        print("ERRORS:")
        for e in errors:
            print(f"  - {e}")
        print()
        print(f"FAIL: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1

    print(f"OK: taxonomy.yml is consistent ({len(category_ids)} categories, "
          f"{len(alias_to_cat)} aliases, {len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
