#!/usr/bin/env python3
"""
Shared YAML / frontmatter utilities.

Replaces the bespoke line-by-line parsers that were duplicated across
scorer.py, tokenizer.py, structure.py, antipattern.py, and the GitHub
scripts.  Uses pyyaml.safe_load so multi-line values, lists, and nested
mappings are handled correctly.
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Optional

try:
    import yaml
    _YAML_AVAILABLE = True
except ImportError:
    _YAML_AVAILABLE = False


def parse_frontmatter(content: str) -> tuple[Optional[dict[str, Any]], str]:
    """Split SKILL.md content into (frontmatter_dict, body).

    Uses pyyaml.safe_load when available; falls back to a simple
    line-based parser so the tools still work without extra installs.

    Returns
    -------
    (fm, body)  where fm is None if no valid frontmatter was found.
    """
    if not content.startswith("---"):
        return None, content

    parts = content.split("---", 2)
    if len(parts) < 3:
        return None, content

    fm_raw = parts[1]
    body = parts[2]

    if _YAML_AVAILABLE:
        try:
            fm = yaml.safe_load(fm_raw) or {}
            # Flatten single-element lists that come from YAML list syntax
            # so downstream code can do fm["version"] without list checks.
            normalized: dict[str, Any] = {}
            for k, v in fm.items():
                if isinstance(v, list) and len(v) == 1 and isinstance(v[0], str):
                    normalized[k] = v[0]
                else:
                    normalized[k] = v
            return normalized, body
        except yaml.YAMLError:
            pass  # fall through to simple parser

    # Fallback: simple key: value parser (handles only flat scalar values)
    fm: dict[str, Any] = {}
    for line in fm_raw.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if ":" in stripped:
            key, _, val = stripped.partition(":")
            val = val.strip().strip('"').strip("'")
            fm[key.strip()] = val
    return fm, body


def read_skill(path: Path) -> tuple[Optional[dict[str, Any]], str]:
    """Read a SKILL.md file and return (frontmatter, body)."""
    content = path.read_text(encoding="utf-8")
    return parse_frontmatter(content)


def get_str(fm: Optional[dict[str, Any]], key: str, default: str = "") -> str:
    """Safely get a string value from a frontmatter dict."""
    if not fm:
        return default
    val = fm.get(key, default)
    if isinstance(val, list):
        return " ".join(str(v) for v in val)
    return str(val) if val is not None else default
