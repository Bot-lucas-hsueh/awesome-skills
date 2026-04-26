#!/usr/bin/env python3
"""
Semantic Skill Search

TF-IDF + cosine similarity search over all SKILL.md files.
Inspired by SkillRouter (arXiv 2603.22455) finding that the skill body —
not just the description — is the decisive routing signal.

Indexes both frontmatter fields and the full skill body so queries like
"authentication JWT Python" surface the right skill even if the description
is terse.

Usage:
    from tools.skill_analyzer.semantic_search import SkillSearchIndex
    idx = SkillSearchIndex()
    idx.build()
    results = idx.search("kubernetes deployment pipeline", top_k=5)

    # CLI: python -m tools.skill_analyzer.cli search "kubernetes deployment"
"""

from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Optional

try:
    from .yaml_utils import read_skill, get_str
except ImportError:
    from yaml_utils import read_skill, get_str  # type: ignore[no-redef]

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

# ── Text utilities ─────────────────────────────────────────────────────────────


def _tokenize(text: str) -> list[str]:
    """Lowercase, strip punctuation, split on whitespace."""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", " ", text)
    return [t for t in text.split() if len(t) > 1]


def _build_document(fm: Optional[dict[str, Any]], body: str) -> str:
    """Combine frontmatter fields + body into a single searchable document.

    Per SkillRouter findings the body carries 91.7% of routing signal weight,
    so we include it in full. Frontmatter fields are boosted via repetition.
    """
    parts = []
    if fm:
        # Boost description and name (repeat 3x to increase weight)
        name = get_str(fm, "name")
        desc = get_str(fm, "description")
        tags = fm.get("tags", [])
        category = get_str(fm, "category")
        parts += [name] * 3
        parts += [desc] * 3
        parts += [category] * 2
        if isinstance(tags, list):
            for tag in tags:
                if isinstance(tag, str):
                    parts += [tag] * 2
                elif isinstance(tag, dict):
                    parts += [" ".join(str(v) for v in tag.values())] * 2
        elif isinstance(tags, str):
            parts += [tags] * 2
    # Full body (the decisive routing signal)
    parts.append(body)
    return " ".join(parts)


# ── TF-IDF Index ───────────────────────────────────────────────────────────────


class SkillSearchIndex:
    """Build and query a TF-IDF index over all SKILL.md files."""

    def __init__(self, skills_dir: Optional[Path] = None):
        self.skills_dir = skills_dir or SKILLS_DIR
        self._docs: list[dict[str, Any]] = []
        self._tfidf: list[dict[str, float]] = []
        self._idf: dict[str, float] = {}
        self._built = False

    # ── Build ──────────────────────────────────────────────────────────────────

    def build(self) -> "SkillSearchIndex":
        """Scan all SKILL.md files and build the TF-IDF index."""
        self._docs = []

        for skill_path in sorted(self.skills_dir.rglob("SKILL.md")):
            if any(x in skill_path.parts for x in ["references", "assets", "_common"]):
                continue

            fm, body = read_skill(skill_path)
            doc_text = _build_document(fm, body)
            tokens = _tokenize(doc_text)

            parts = skill_path.parts
            category, skill_name = "unknown", skill_path.parent.name
            if "skills" in parts:
                idx = parts.index("skills")
                if idx + 1 < len(parts):
                    category = parts[idx + 1]

            try:
                repo_root = self.skills_dir.parent
                rel_path = str(skill_path.relative_to(repo_root))
            except ValueError:
                rel_path = str(skill_path)

            self._docs.append(
                {
                    "path": rel_path,
                    "skill": skill_name,
                    "category": category,
                    "description": get_str(fm, "description") if fm else "",
                    "tokens": tokens,
                    "token_count": len(tokens),
                }
            )

        self._build_tfidf()
        self._built = True
        return self

    def _build_tfidf(self) -> None:
        """Compute TF-IDF vectors for all documents."""
        n_docs = len(self._docs)
        if n_docs == 0:
            return

        # Document frequency
        df: dict[str, int] = defaultdict(int)
        tf_lists: list[Counter] = []
        for doc in self._docs:
            tf = Counter(doc["tokens"])
            tf_lists.append(tf)
            for term in tf:
                df[term] += 1

        # IDF with smoothing
        self._idf = {
            term: math.log((n_docs + 1) / (count + 1)) + 1
            for term, count in df.items()
        }

        # TF-IDF vectors (L2 normalized)
        self._tfidf = []
        for tf in tf_lists:
            max_tf = max(tf.values()) if tf else 1
            vec: dict[str, float] = {}
            for term, count in tf.items():
                vec[term] = (count / max_tf) * self._idf.get(term, 1.0)
            norm = math.sqrt(sum(v * v for v in vec.values())) or 1.0
            self._tfidf.append({t: v / norm for t, v in vec.items()})

    # ── Query ──────────────────────────────────────────────────────────────────

    def search(
        self,
        query: str,
        top_k: int = 10,
        category_filter: Optional[str] = None,
    ) -> list[dict[str, Any]]:
        """Return top_k most relevant skills for the query."""
        if not self._built:
            self.build()

        query_tokens = _tokenize(query)
        if not query_tokens:
            return []

        # Query TF-IDF vector
        qtf = Counter(query_tokens)
        max_qtf = max(qtf.values())
        qvec: dict[str, float] = {}
        for term, count in qtf.items():
            idf = self._idf.get(term, math.log((len(self._docs) + 1) / 1) + 1)
            qvec[term] = (count / max_qtf) * idf
        q_norm = math.sqrt(sum(v * v for v in qvec.values())) or 1.0
        qvec = {t: v / q_norm for t, v in qvec.items()}

        # Cosine similarity
        scores: list[tuple[float, int]] = []
        for i, doc_vec in enumerate(self._tfidf):
            doc = self._docs[i]
            if category_filter and doc["category"] != category_filter:
                continue
            sim = sum(qvec.get(t, 0) * w for t, w in doc_vec.items())
            scores.append((sim, i))

        scores.sort(reverse=True)
        results = []
        for sim, i in scores[:top_k]:
            if sim <= 0:
                break
            doc = self._docs[i].copy()
            doc["score"] = round(sim, 4)
            doc.pop("tokens", None)
            results.append(doc)

        return results

    # ── Stats ──────────────────────────────────────────────────────────────────

    def stats(self) -> dict[str, Any]:
        """Return index statistics."""
        return {
            "total_skills": len(self._docs),
            "vocabulary_size": len(self._idf),
            "built": self._built,
        }


# ── Module-level singleton (lazily built) ────────────────────────────────────

_INDEX: Optional[SkillSearchIndex] = None


def get_index(rebuild: bool = False) -> SkillSearchIndex:
    """Return the module-level search index, building it on first call."""
    global _INDEX
    if _INDEX is None or rebuild:
        _INDEX = SkillSearchIndex()
        _INDEX.build()
    return _INDEX


def search(query: str, top_k: int = 10, category_filter: Optional[str] = None) -> list[dict[str, Any]]:
    """Convenience function: search using the global index."""
    return get_index().search(query, top_k=top_k, category_filter=category_filter)
