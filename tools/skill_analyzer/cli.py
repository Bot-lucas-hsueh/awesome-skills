#!/usr/bin/env python3
"""
CLI - Unified Entry Point for Skill Analyzer Tools

Usage:
    python -m tools.skill_analyzer.cli score --category software
    python -m tools.skill_analyzer.cli tokenizer --path skills/software/backend-developer/SKILL.md
    python -m tools.skill_analyzer.cli structure
    python -m tools.skill_analyzer.cli antipattern
    python -m tools.skill_analyzer.cli gate --path skills/software/backend-developer/SKILL.md
    python -m tools.skill_analyzer.cli all
"""

import sys
import argparse
from pathlib import Path

# Add tools to path
TOOLS_DIR = Path(__file__).parent
sys.path.insert(0, str(TOOLS_DIR))


def cmd_score(args):
    """Run scoring."""
    import sys
    from pathlib import Path

    tools_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(tools_dir))

    from skill_analyzer import scorer

    if args.path:
        result = scorer.score_skill(Path(args.path))
        if args.output == "json":
            import json

            print(json.dumps(result, indent=2))
        else:
            from rich.console import Console

            console = Console()
            console.print(f"[bold]{result['skill']}[/bold] ({result['category']})")
            console.print(f"Score: {result['weighted_avg']}/10 ({result['tier']})")
            console.print(f"Estimated tokens: {result.get('estimated_tokens', '?'):,}")
            console.print("\n[bold]Dimension Scores:[/bold]")
            # Group dimensions: original 6 + new 2
            for dim, score in result["scores"].items():
                tag = " [NEW]" if dim in ("content_efficiency", "token_cost_efficiency") else ""
                console.print(f"  {dim}{tag}: {score}/10")
    else:
        results = scorer.score_all_skills()

        # Filter
        if args.category:
            results = [r for r in results if "error" not in r and r["category"] == args.category]
        if args.tier:
            results = [r for r in results if "error" not in r and r["tier"] == args.tier]

        if args.output == "json":
            import json

            print(json.dumps(results, indent=2))
        else:
            scorer.print_score_summary(results)


def cmd_tokenizer(args):
    """Run token budget check."""
    import sys
    from pathlib import Path

    tools_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(tools_dir))

    from skill_analyzer import tokenizer

    if args.path:
        result = tokenizer.analyze_token_budget(Path(args.path), args.total_skills)
        if args.output == "json":
            import json

            print(json.dumps(result, indent=2))
        else:
            from rich.console import Console

            console = Console()
            console.print(f"[bold]{result['skill']}[/bold]")
            console.print(f"Path: {result['path']}")

            if "description" in result and "error" not in result.get("description", {}):
                d = result["description"]
                console.print(
                    f"\nDescription: {d['char_count']}/{d['limit']} chars - {d['status']}"
                )

            if "body" in result:
                b = result["body"]
                console.print(f"Body: {b['line_count']}/{b['limit']} lines - {b['status']}")

            if result.get("html_in_yaml"):
                console.print(f"\n[red]HTML in YAML: {len(result['html_in_yaml'])} issues[/red]")
    else:
        results = tokenizer.analyze_all_skills(total_skills=args.total_skills)

        if args.category:
            results = [r for r in results if args.category in r.get("path", "")]

        if args.output == "json":
            import json

            print(json.dumps(results, indent=2))
        else:
            tokenizer.print_token_summary(results)


def cmd_structure(args):
    """Run structure check."""
    import sys
    from pathlib import Path

    tools_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(tools_dir))

    from skill_analyzer import structure

    if args.path:
        result = structure.check_structure(Path(args.path))
        if args.output == "json":
            import json

            print(json.dumps(result, indent=2))
        else:
            from rich.console import Console

            console = Console()
            console.print(f"[bold]{result['skill']}[/bold]")
            console.print(f"Sections: {result['sections']['total']}/16")
            console.print(f"Score: {result.get('overall_score', 0)}%")

            c = result.get("completeness", {})
            if c.get("missing"):
                console.print("\n[red]Missing sections:[/red]")
                for m in c["missing"]:
                    console.print(f"  - §{m['num']}: {m['name']}")
    else:
        results = structure.analyze_all_skills()

        if args.output == "json":
            import json

            print(json.dumps(results, indent=2))
        else:
            structure.print_structure_summary(results)


def cmd_antipattern(args):
    """Run anti-pattern scan."""
    import sys
    from pathlib import Path

    tools_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(tools_dir))

    from skill_analyzer import antipattern

    if args.path:
        result = antipattern.scan_antipatterns(Path(args.path))
        if args.output == "json":
            import json

            print(json.dumps(result, indent=2))
        else:
            from rich.console import Console

            console = Console()
            console.print(f"[bold]{result['skill']}[/bold]")
            console.print(f"Total issues: {result.get('total_issues', 0)}")

            counts = result.get("severity_counts", {})
            console.print(f"  🔴 High: {counts.get('high', 0)}")
            console.print(f"  🟡 Medium: {counts.get('medium', 0)}")
            console.print(f"  🟢 Low: {counts.get('low', 0)}")

            if result.get("issues"):
                console.print("\n[bold]Issues:[/bold]")
                for issue in result["issues"][:5]:
                    console.print(
                        f"  [{issue.get('severity', 'medium').upper()}] {issue.get('message', '')}"
                    )
    else:
        results = antipattern.scan_all_skills()

        if args.output == "json":
            import json

            print(json.dumps(results, indent=2))
        else:
            antipattern.print_antipattern_summary(results)


def cmd_gate(args):
    """Run the quality gate check (enforces thresholds)."""
    import sys
    from pathlib import Path

    repo_root = Path(__file__).parent.parent.parent
    gate_script = repo_root / ".github" / "scripts" / "quality_gate.py"

    # Build argument list for quality_gate.py
    gate_args = []
    if args.all:
        gate_args.append("--all")
    elif args.path:
        gate_args.append(args.path)

    gate_args += [
        "--min-score", str(args.min_score),
        "--max-tokens", str(args.max_tokens),
        "--max-desc-chars", str(args.max_desc_chars),
        "--total-skills", str(args.total_skills),
        "--output", args.output,
    ]

    import importlib.util
    spec = importlib.util.spec_from_file_location("quality_gate", gate_script)
    mod = importlib.util.module_from_spec(spec)
    # Patch sys.argv so quality_gate.main() sees our args
    old_argv = sys.argv
    sys.argv = ["quality_gate"] + gate_args
    try:
        spec.loader.exec_module(mod)
        sys.exit(mod.main())
    finally:
        sys.argv = old_argv


def cmd_all(args):
    """Run all analyzers."""
    import sys
    from pathlib import Path

    tools_dir = Path(__file__).parent.parent
    sys.path.insert(0, str(tools_dir))

    from skill_analyzer import scorer, tokenizer, structure, antipattern

    from rich.console import Console
    from rich.progress import Progress

    console = Console()
    console.print("[bold]Running all analyzers...[/bold]\n")

    # Score
    console.print("[cyan]1. Quality Scoring...[/cyan]")
    score_results = scorer.score_all_skills()

    # Token
    console.print("[cyan]2. Token Budget...[/cyan]")
    token_results = tokenizer.analyze_all_skills(total_skills=args.total_skills)

    # Structure
    console.print("[cyan]3. Structure Check...[/cyan]")
    struct_results = structure.analyze_all_skills()

    # Antipatterns
    console.print("[cyan]4. Anti-Pattern Scan...[/cyan]")
    anti_results = antipattern.scan_all_skills()

    # Summary
    console.print("\n[bold green]✅ All checks complete![/bold green]")

    # Print summaries
    console.print("\n[bold]Quality Distribution:[/bold]")
    tiers = {"exemplary": 0, "expert": 0, "community": 0, "basic": 0}
    for r in score_results:
        if "error" not in r:
            tiers[r["tier"]] = tiers.get(r["tier"], 0) + 1
    for tier, count in tiers.items():
        console.print(f"  {tier.upper()}: {count}")

    console.print("\n[bold]Token Issues:[/bold]")
    over_desc = sum(
        1 for r in token_results if r.get("description", {}).get("status") == "OVER_BUDGET"
    )
    console.print(f"  Description over budget: {over_desc}")

    console.print("\n[bold]Anti-Patterns:[/bold]")
    high = sum(r.get("severity_counts", {}).get("high", 0) for r in anti_results)
    medium = sum(r.get("severity_counts", {}).get("medium", 0) for r in anti_results)
    console.print(f"  🔴 High: {high}")
    console.print(f"  🟡 Medium: {medium}")

    console.print("\n[bold]Token Cost Summary:[/bold]")
    total_tokens = sum(r.get("token_count", 0) for r in token_results if "error" not in r)
    total_cost = sum(
        r.get("api_cost", {}).get("cost_per_load_usd", 0.0) for r in token_results if "error" not in r
    )
    console.print(f"  Total body tokens: {total_tokens:,}")
    console.print(f"  Est. API cost (all skills, 1 load, claude-sonnet-4-6): ${total_cost:.4f} USD")
    console.print(f"  Est. API cost per 100 loads: ${total_cost * 100:.2f} USD")

    console.print("\n[bold]New Dimensions (content_efficiency & token_cost_efficiency):[/bold]")
    eff_scores = [
        r["scores"].get("content_efficiency", 0)
        for r in score_results
        if "error" not in r and "scores" in r
    ]
    tok_scores = [
        r["scores"].get("token_cost_efficiency", 0)
        for r in score_results
        if "error" not in r and "scores" in r
    ]
    if eff_scores:
        avg_eff = sum(eff_scores) / len(eff_scores)
        avg_tok = sum(tok_scores) / len(tok_scores)
        console.print(f"  Avg content_efficiency:      {avg_eff:.2f}/10")
        console.print(f"  Avg token_cost_efficiency:   {avg_tok:.2f}/10")


def main():
    parser = argparse.ArgumentParser(
        description="Awesome Skills Analyzer CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Score command
    score_parser = subparsers.add_parser("score", help="Score skills (6-dimension)")
    score_parser.add_argument("--path", "-p", help="Specific skill path")
    score_parser.add_argument("--category", "-c", help="Filter by category")
    score_parser.add_argument("--tier", "-t", choices=["exemplary", "expert", "community", "basic"])
    score_parser.add_argument("--output", "-o", choices=["json", "text"], default="text")
    score_parser.set_defaults(func=cmd_score)

    # Tokenizer command
    token_parser = subparsers.add_parser("tokenizer", help="Check token budget")
    token_parser.add_argument("--path", "-p", help="Specific skill path")
    token_parser.add_argument("--category", "-c", help="Filter by category")
    token_parser.add_argument("--total-skills", "-t", type=int, default=40)
    token_parser.add_argument("--output", "-o", choices=["json", "text"], default="text")
    token_parser.set_defaults(func=cmd_tokenizer)

    # Structure command
    struct_parser = subparsers.add_parser("structure", help="Check 16-section structure")
    struct_parser.add_argument("--path", "-p", help="Specific skill path")
    struct_parser.add_argument("--output", "-o", choices=["json", "text"], default="text")
    struct_parser.set_defaults(func=cmd_structure)

    # Antipattern command
    anti_parser = subparsers.add_parser("antipattern", help="Scan anti-patterns")
    anti_parser.add_argument("--path", "-p", help="Specific skill path")
    anti_parser.add_argument("--output", "-o", choices=["json", "text"], default="text")
    anti_parser.add_argument("--fail-on", choices=["high", "medium", "low"])
    anti_parser.set_defaults(func=cmd_antipattern)

    # Gate command (CI quality gate — enforces thresholds)
    gate_parser = subparsers.add_parser(
        "gate",
        help="Run CI quality gate (enforces score/token thresholds, exits 1 on failure)",
    )
    gate_parser.add_argument("--path", "-p", help="Specific skill path to gate-check")
    gate_parser.add_argument("--all", action="store_true", help="Check all skills")
    gate_parser.add_argument("--min-score", type=float, default=4.0, help="Min quality score (default: 4.0)")
    gate_parser.add_argument("--max-tokens", type=int, default=6000, help="Max body token count (default: 6000)")
    gate_parser.add_argument("--max-desc-chars", type=int, default=400, help="Max description chars (default: 400)")
    gate_parser.add_argument("--total-skills", type=int, default=40, help="Total installed skills (default: 40)")
    gate_parser.add_argument("--output", "-o", choices=["text", "json"], default="text")
    gate_parser.set_defaults(func=cmd_gate)

    # All command
    all_parser = subparsers.add_parser("all", help="Run all analyzers")
    all_parser.add_argument("--total-skills", "-t", type=int, default=40)
    all_parser.set_defaults(func=cmd_all)

    args = parser.parse_args()

    if args.command is None:
        parser.print_help()
        return

    args.func(args)


if __name__ == "__main__":
    main()
