#!/usr/bin/env python3
"""
Skill Dependency Graph

Extracts machine-readable skill composition relationships from SKILL.md files
by parsing:
  1. YAML frontmatter `requires:` field (explicit dependencies)
  2. `## Integration with Other Skills` section (cross-references)

Outputs:
  - adjacency list (who requires whom)
  - dependency depth (BFS from each node)
  - clusters (connected components)
  - JSON export for tooling integration

Usage:
    from tools.skill_analyzer.skill_graph import SkillGraph
    g = SkillGraph()
    g.build()
    g.print_summary()
    json_data = g.to_dict()

    # CLI: python -m tools.skill_analyzer.cli graph
"""

from __future__ import annotations

import json
import re
from collections import defaultdict, deque
from pathlib import Path
from typing import Any, Optional

try:
    from .yaml_utils import read_skill, get_str
except ImportError:
    from yaml_utils import read_skill, get_str  # type: ignore[no-redef]

SKILLS_DIR = Path(__file__).parent.parent.parent / "skills"

# Regex to extract skill references from Integration sections
# Matches patterns like: `backend-developer`, [backend-developer], backend-developer skill
_SKILL_REF_RE = re.compile(
    r"`([a-z][a-z0-9-]{2,63})`"          # backtick-quoted kebab-case
    r"|"
    r"\[([a-z][a-z0-9-]{2,63})\]"         # markdown link label [skill-name]
    r"|"
    r"\b([a-z][a-z0-9-]{2,63})\s+skill\b",  # "X skill" phrase
    re.IGNORECASE,
)


def _extract_integration_refs(body: str) -> list[str]:
    """Extract skill names referenced in the Integration section."""
    section = re.search(
        r"^##\s+.*Integration.*?\n(.*?)(?=^##\s|\Z)",
        body,
        re.MULTILINE | re.DOTALL,
    )
    if not section:
        return []

    text = section.group(1)
    refs = []
    for m in _SKILL_REF_RE.finditer(text):
        name = m.group(1) or m.group(2) or m.group(3)
        if name:
            refs.append(name.lower())
    return list(dict.fromkeys(refs))  # deduplicate preserving order


class SkillGraph:
    """Directed graph of skill dependencies."""

    def __init__(self, skills_dir: Optional[Path] = None):
        self.skills_dir = skills_dir or SKILLS_DIR
        # node_id → metadata
        self._nodes: dict[str, dict[str, Any]] = {}
        # node_id → set of dependency node_ids (edges: A → B means A requires B)
        self._edges: dict[str, set[str]] = defaultdict(set)
        # reverse: node_id → set of dependents
        self._rev_edges: dict[str, set[str]] = defaultdict(set)
        self._built = False

    # ── Build ──────────────────────────────────────────────────────────────────

    def build(self) -> "SkillGraph":
        """Scan all SKILL.md files and build the dependency graph."""
        self._nodes = {}
        self._edges = defaultdict(set)
        self._rev_edges = defaultdict(set)

        skill_paths: dict[str, Path] = {}

        for path in sorted(self.skills_dir.rglob("SKILL.md")):
            if any(x in path.parts for x in ["references", "assets", "_common"]):
                continue

            fm, body = read_skill(path)
            skill_name = path.parent.name
            parts = path.parts
            category = "unknown"
            if "skills" in parts:
                idx = parts.index("skills")
                if idx + 1 < len(parts):
                    category = parts[idx + 1]

            try:
                rel = str(path.relative_to(self.skills_dir.parent))
            except ValueError:
                rel = str(path)

            node_id = skill_name
            self._nodes[node_id] = {
                "name": skill_name,
                "category": category,
                "path": rel,
                "description": get_str(fm, "description") if fm else "",
                "difficulty": get_str(fm, "difficulty") if fm else "",
            }
            skill_paths[node_id] = path

            # Explicit requires from frontmatter
            requires: list[str] = []
            if fm and "requires" in fm:
                raw_req = fm["requires"]
                if isinstance(raw_req, list):
                    requires = [str(r).strip().lower() for r in raw_req if r]
                elif isinstance(raw_req, str):
                    requires = [r.strip().lower() for r in raw_req.split(",") if r.strip()]

            # Implicit references from Integration section
            integration_refs = _extract_integration_refs(body)

            all_deps = list(dict.fromkeys(requires + integration_refs))
            self._nodes[node_id]["requires"] = requires
            self._nodes[node_id]["integration_refs"] = integration_refs
            self._nodes[node_id]["all_deps"] = all_deps

            for dep in all_deps:
                self._edges[node_id].add(dep)
                self._rev_edges[dep].add(node_id)

        self._built = True
        return self

    # ── Analysis ───────────────────────────────────────────────────────────────

    def dependency_depth(self, node_id: str) -> int:
        """BFS depth from node_id following its dependency edges."""
        if node_id not in self._edges or not self._edges[node_id]:
            return 0
        visited = {node_id}
        queue: deque[tuple[str, int]] = deque([(node_id, 0)])
        max_depth = 0
        while queue:
            current, depth = queue.popleft()
            for dep in self._edges.get(current, set()):
                if dep not in visited and dep in self._nodes:
                    visited.add(dep)
                    max_depth = max(max_depth, depth + 1)
                    queue.append((dep, depth + 1))
        return max_depth

    def dependents(self, node_id: str) -> list[str]:
        """Skills that depend on (require) this skill."""
        return sorted(self._rev_edges.get(node_id, set()))

    def most_depended_on(self, top_k: int = 10) -> list[tuple[str, int]]:
        """Skills with the most dependents (hub skills)."""
        counts = [(node, len(self._rev_edges.get(node, set()))) for node in self._nodes]
        return sorted(counts, key=lambda x: x[1], reverse=True)[:top_k]

    def orphans(self) -> list[str]:
        """Skills with no dependencies and no dependents."""
        return [
            n for n in self._nodes
            if not self._edges.get(n) and not self._rev_edges.get(n)
        ]

    def cycles(self) -> list[list[str]]:
        """Detect cycles using DFS (returns list of cycle paths)."""
        found: list[list[str]] = []
        visited: set[str] = set()
        path: list[str] = []
        in_path: set[str] = set()

        def dfs(node: str) -> None:
            if node in in_path:
                # Found a cycle
                cycle_start = path.index(node)
                found.append(path[cycle_start:] + [node])
                return
            if node in visited:
                return
            visited.add(node)
            in_path.add(node)
            path.append(node)
            for dep in self._edges.get(node, set()):
                if dep in self._nodes:
                    dfs(dep)
            path.pop()
            in_path.discard(node)

        for node in self._nodes:
            dfs(node)

        return found

    # ── Export ─────────────────────────────────────────────────────────────────

    def to_dict(self) -> dict[str, Any]:
        """Export graph as JSON-serializable dict."""
        if not self._built:
            self.build()

        nodes_out = {}
        for node_id, meta in self._nodes.items():
            nodes_out[node_id] = {
                **meta,
                "dependents": self.dependents(node_id),
                "dependency_depth": self.dependency_depth(node_id),
            }

        return {
            "total_nodes": len(self._nodes),
            "total_edges": sum(len(v) for v in self._edges.values()),
            "hub_skills": self.most_depended_on(10),
            "orphans": self.orphans(),
            "cycles": self.cycles(),
            "nodes": nodes_out,
        }

    def print_summary(self) -> None:
        """Print a human-readable summary."""
        if not self._built:
            self.build()

        try:
            from rich.console import Console
            from rich.table import Table

            console = Console()
            console.print(f"\n[bold]Skill Dependency Graph[/bold]")
            console.print(f"  Nodes (skills): {len(self._nodes)}")
            console.print(f"  Edges (deps):   {sum(len(v) for v in self._edges.values())}")
            console.print(f"  Orphans:        {len(self.orphans())}")

            cycle_list = self.cycles()
            if cycle_list:
                console.print(f"  [red]Cycles detected: {len(cycle_list)}[/red]")
            else:
                console.print("  [green]No cycles detected[/green]")

            console.print("\n[bold]Hub Skills (most depended-on)[/bold]")
            table = Table(show_header=True)
            table.add_column("Skill")
            table.add_column("Dependents")
            table.add_column("Depth")

            for skill, count in self.most_depended_on(15):
                if count > 0:
                    table.add_row(skill, str(count), str(self.dependency_depth(skill)))

            console.print(table)

        except ImportError:
            print(f"Skill graph: {len(self._nodes)} nodes, {sum(len(v) for v in self._edges.values())} edges")
            for skill, count in self.most_depended_on(10):
                if count > 0:
                    print(f"  {skill}: {count} dependents")
