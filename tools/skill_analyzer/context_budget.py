#!/usr/bin/env python3
"""
Context Window Budget Calculator

Determines how many skills can fit within a model's context window when
loaded at runtime. Implements the progressive-disclosure pattern:

  - Phase 1 (catalog phase): frontmatter only → compact catalog injected
    into the system prompt for routing decisions.
  - Phase 2 (execution phase): selected skills loaded in full.

Reference models and context windows are based on the April 2026 pricing table:
  claude-opus-4-7    1M tokens
  claude-opus-4-6    1M tokens
  claude-sonnet-4-6  1M tokens
  claude-haiku-4-5   200K tokens

Usage:
    from tools.skill_analyzer.context_budget import ContextBudgetCalculator
    calc = ContextBudgetCalculator()
    report = calc.report(model="claude-opus-4-7", user_budget_tokens=20000)
    print(report)

    # CLI: python -m tools.skill_analyzer.cli budget --model claude-opus-4-7
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Optional

try:
    from .yaml_utils import read_skill, get_str
except ImportError:
    from yaml_utils import read_skill, get_str  # type: ignore[no-redef]

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

# Model context windows (tokens)
MODEL_CONTEXT = {
    "claude-opus-4-7": 1_000_000,
    "claude-opus-4-6": 1_000_000,
    "claude-sonnet-4-6": 1_000_000,
    "claude-haiku-4-5": 200_000,
}

# Cost per 1M tokens (input), April 2026
MODEL_INPUT_COST_PER_M = {
    "claude-opus-4-7": 5.00,
    "claude-opus-4-6": 5.00,
    "claude-sonnet-4-6": 3.00,
    "claude-haiku-4-5": 1.00,
}

# Realistic overhead: system prompt, conversation history, output buffer
SYSTEM_OVERHEAD_TOKENS = 2_000
CONVERSATION_OVERHEAD_TOKENS = 4_000
OUTPUT_BUFFER_TOKENS = 8_000
TOTAL_OVERHEAD_TOKENS = SYSTEM_OVERHEAD_TOKENS + CONVERSATION_OVERHEAD_TOKENS + OUTPUT_BUFFER_TOKENS


def estimate_tokens(text: str) -> int:
    """Rough token estimate (~0.25 tokens/char Latin, ~1.0 per CJK char)."""
    cjk = len(re.findall(r"[一-鿿぀-ヿ]", text))
    other = len(text) - cjk
    return int(cjk * 1.0 + other * 0.25)


def _extract_frontmatter_text(path: Path) -> str:
    """Return the raw YAML frontmatter block as text."""
    try:
        raw = path.read_text(encoding="utf-8")
    except Exception:
        return ""
    if not raw.startswith("---"):
        return ""
    parts = raw.split("---", 2)
    return parts[1] if len(parts) >= 3 else ""


class SkillBudgetEntry:
    """Token budget breakdown for a single skill."""

    def __init__(self, path: Path):
        self.path = path
        parts = path.parts
        self.category = "unknown"
        self.skill_name = path.parent.name
        if "skills" in parts:
            idx = parts.index("skills")
            if idx + 1 < len(parts):
                self.category = parts[idx + 1]

        fm, body = read_skill(path)
        self.description = get_str(fm, "description") if fm else ""

        fm_text = _extract_frontmatter_text(path)
        full_text = path.read_text(encoding="utf-8") if path.exists() else ""

        self.fm_tokens = estimate_tokens(fm_text)
        self.body_tokens = estimate_tokens(body)
        self.total_tokens = estimate_tokens(full_text)

        # Catalog entry = name + description only (phase 1)
        catalog_line = f"{self.skill_name}: {self.description}"
        self.catalog_tokens = estimate_tokens(catalog_line)


class ContextBudgetCalculator:
    """Calculate how many skills fit within a model's context window."""

    def __init__(self, skills_dir: Optional[Path] = None):
        self.skills_dir = skills_dir or SKILLS_DIR
        self._entries: Optional[list[SkillBudgetEntry]] = None

    def _load(self) -> list[SkillBudgetEntry]:
        if self._entries is not None:
            return self._entries
        entries = []
        for path in sorted(self.skills_dir.rglob("SKILL.md")):
            if any(x in path.parts for x in ["references", "assets", "_common"]):
                continue
            entries.append(SkillBudgetEntry(path))
        self._entries = entries
        return entries

    def catalog_budget(self) -> dict[str, Any]:
        """Report catalog-phase token usage (frontmatter descriptions only)."""
        entries = self._load()
        total_catalog = sum(e.catalog_tokens for e in entries)
        return {
            "phase": "catalog",
            "total_skills": len(entries),
            "catalog_tokens_total": total_catalog,
            "avg_catalog_tokens_per_skill": round(total_catalog / len(entries), 1) if entries else 0,
            "skills": [
                {
                    "skill": e.skill_name,
                    "category": e.category,
                    "catalog_tokens": e.catalog_tokens,
                    "description_chars": len(e.description),
                }
                for e in sorted(entries, key=lambda x: x.catalog_tokens, reverse=True)
            ],
        }

    def execution_budget(self) -> dict[str, Any]:
        """Report execution-phase token usage (full skill body)."""
        entries = self._load()
        return {
            "phase": "execution",
            "skills": [
                {
                    "skill": e.skill_name,
                    "category": e.category,
                    "fm_tokens": e.fm_tokens,
                    "body_tokens": e.body_tokens,
                    "total_tokens": e.total_tokens,
                }
                for e in sorted(entries, key=lambda x: x.total_tokens, reverse=True)
            ],
        }

    def fit_analysis(
        self,
        model: str = "claude-sonnet-4-6",
        user_budget_tokens: Optional[int] = None,
    ) -> dict[str, Any]:
        """Analyze how many skills (catalog + execution) fit in the model's context."""
        context_window = MODEL_CONTEXT.get(model, 200_000)
        available = context_window - TOTAL_OVERHEAD_TOKENS
        if user_budget_tokens is not None:
            available = min(available, user_budget_tokens)

        entries = self._load()
        total_catalog = sum(e.catalog_tokens for e in entries)

        # Tokens remaining after loading the full catalog
        after_catalog = available - total_catalog

        # How many full skills can be loaded in the execution phase?
        sorted_by_size = sorted(entries, key=lambda x: x.total_tokens)
        cumulative = 0
        fits_full = 0
        for e in sorted_by_size:
            if cumulative + e.total_tokens <= after_catalog:
                cumulative += e.total_tokens
                fits_full += 1
            else:
                break

        cost_per_load = (available / 1_000_000) * MODEL_INPUT_COST_PER_M.get(model, 3.0)

        return {
            "model": model,
            "context_window_tokens": context_window,
            "overhead_tokens": TOTAL_OVERHEAD_TOKENS,
            "available_tokens": available,
            "catalog_tokens": total_catalog,
            "catalog_fits": total_catalog <= available,
            "tokens_after_catalog": after_catalog,
            "max_full_skills_in_execution": fits_full,
            "total_skills": len(entries),
            "est_cost_per_full_load_usd": round(cost_per_load, 6),
            "est_cost_per_100_loads_usd": round(cost_per_load * 100, 4),
        }

    def report(
        self,
        model: str = "claude-sonnet-4-6",
        user_budget_tokens: Optional[int] = None,
    ) -> str:
        """Return a human-readable context budget report."""
        fit = self.fit_analysis(model=model, user_budget_tokens=user_budget_tokens)
        entries = self._load()
        total_body = sum(e.body_tokens for e in entries)
        avg_body = total_body / len(entries) if entries else 0

        lines = [
            f"Context Budget Report — {model}",
            "=" * 50,
            f"  Context window:          {fit['context_window_tokens']:>10,} tokens",
            f"  Overhead (sys+conv+out): {fit['overhead_tokens']:>10,} tokens",
            f"  Available for skills:    {fit['available_tokens']:>10,} tokens",
            "",
            "Catalog Phase (frontmatter descriptions only):",
            f"  Total catalog tokens:    {fit['catalog_tokens']:>10,} tokens",
            f"  Catalog fits in window:  {'YES' if fit['catalog_fits'] else 'NO — TRIM DESCRIPTIONS'}",
            f"  Tokens after catalog:    {fit['tokens_after_catalog']:>10,} tokens",
            "",
            "Execution Phase (full skill bodies):",
            f"  Total skills:            {fit['total_skills']:>10}",
            f"  Max full skills loadable:{fit['max_full_skills_in_execution']:>10}",
            f"  Average body tokens:     {avg_body:>10,.0f}",
            "",
            "Cost Estimate:",
            f"  Per full context load:   ${fit['est_cost_per_full_load_usd']:.6f}",
            f"  Per 100 loads:           ${fit['est_cost_per_100_loads_usd']:.4f}",
        ]
        return "\n".join(lines)
