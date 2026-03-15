"""
Progress Tracker Dashboard
Displays quality progress of all skills in the repository.
"""

import json
import sys
from pathlib import Path
from typing import Dict, List, Any, Optional
from datetime import datetime

# Add tools to path
TOOLS_DIR = Path(__file__).parent.parent
sys.path.insert(0, str(TOOLS_DIR))


def load_all_scores() -> List[Dict[str, Any]]:
    """Load scores from all analyzers."""
    from skill_analyzer import scorer, tokenizer, structure, antipattern

    print("Loading scores...")
    scores = scorer.score_all_skills()
    print(f"  Loaded {len(scores)} skills from scorer")

    return scores


def calculate_progress(results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Calculate progress statistics."""
    tiers = {"exemplary": 0, "expert": 0, "community": 0, "basic": 0}
    categories = {}
    total = 0
    total_score = 0

    for r in results:
        if "error" in r:
            continue

        total += 1
        tier = r.get("tier", "basic")
        tiers[tier] = tiers.get(tier, 0) + 1

        # Category stats
        cat = r.get("category", "unknown")
        if cat not in categories:
            categories[cat] = {
                "total": 0,
                "exemplary": 0,
                "expert": 0,
                "community": 0,
                "basic": 0,
                "avg_score": 0,
            }
        categories[cat]["total"] += 1
        categories[cat][tier] = categories[cat].get(tier, 0) + 1

        total_score += r.get("weighted_avg", 0)

    # Calculate averages
    avg_score = total_score / total if total > 0 else 0

    # Calculate category avg scores
    for cat, data in categories.items():
        # This is simplified - ideally we'd store all scores
        pass

    return {
        "total": total,
        "tiers": tiers,
        "categories": categories,
        "avg_score": avg_score,
    }


def print_dashboard(results: List[Dict[str, Any]]) -> None:
    """Print the progress dashboard."""
    from rich.console import Console
    from rich.table import Table
    from rich.panel import Panel
    from rich.text import Text

    console = Console()
    progress = calculate_progress(results)

    # Title
    console.print("\n")
    console.print(
        Panel.fit(
            "[bold cyan]Awesome Skills - Quality Progress Dashboard[/bold cyan]\n"
            f"Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
            border_style="cyan",
        )
    )

    # Overall stats
    total = progress["total"]
    tiers = progress["tiers"]

    console.print("\n[bold]Overall Quality Distribution[/bold]")

    # Tier distribution bar
    bar_width = 40
    tier_order = [
        ("exemplary", "⭐⭐", "green"),
        ("expert", "⭐", "yellow"),
        ("community", "✓", "blue"),
        ("basic", "📝", "red"),
    ]

    for tier, emoji, color in tier_order:
        count = tiers.get(tier, 0)
        pct = (count / total * 100) if total > 0 else 0
        filled = int(bar_width * count / total) if total > 0 else 0
        bar = "█" * filled + "░" * (bar_width - filled)

        console.print(
            f"  {emoji} {tier.upper():12} [{color}]{bar}[/{color}] {count:3} ({pct:5.1f}%)"
        )

    # Summary numbers
    console.print(f"\n[bold]Summary[/bold]")
    console.print(f"  Total Skills: {total}")
    console.print(f"  Average Score: {progress['avg_score']:.2f}/10")
    console.print(
        f"  Exemplary + Expert: {tiers.get('exemplary', 0) + tiers.get('expert', 0)} ({((tiers.get('exemplary', 0) + tiers.get('expert', 0)) / total * 100) if total > 0 else 0:.1f}%)"
    )

    # Category breakdown
    console.print("\n[bold]Category Breakdown[/bold]")

    cat_table = Table(show_header=True, header_style="bold magenta")
    cat_table.add_column("Category", style="cyan", width=25)
    cat_table.add_column("Total", justify="right")
    cat_table.add_column("⭐⭐", justify="right", style="green")
    cat_table.add_column("⭐", justify="right", style="yellow")
    cat_table.add_column("✓", justify="right", style="blue")
    cat_table.add_column("📝", justify="right", style="red")
    cat_table.add_column("Progress", width=20)

    # Sort categories by total skills
    sorted_cats = sorted(progress["categories"].items(), key=lambda x: x[1]["total"], reverse=True)

    for cat, data in sorted_cats:
        cat_total = data["total"]
        exemplary = data.get("exemplary", 0)
        expert = data.get("expert", 0)
        community = data.get("community", 0)
        basic = data.get("basic", 0)

        # Progress bar
        high_quality = exemplary + expert
        pct = (high_quality / cat_total * 100) if cat_total > 0 else 0
        filled = int(10 * high_quality / cat_total) if cat_total > 0 else 0
        bar = "█" * filled + "░" * (10 - filled)

        cat_table.add_row(
            cat,
            str(cat_total),
            str(exemplary),
            str(expert),
            str(community),
            str(basic),
            f"[green]{bar}[/green] {pct:.0f}%",
        )

    console.print(cat_table)

    # Top skills
    console.print("\n[bold green]Top 10 Exemplary Skills[/bold green]")

    top_table = Table(show_header=True)
    top_table.add_column("Rank", justify="right", width=5)
    top_table.add_column("Skill", style="cyan")
    top_table.add_column("Category", style="dim")
    top_table.add_column("Score", justify="right", style="green")

    # Sort by score
    sorted_results = sorted(
        [r for r in results if "error" not in r],
        key=lambda x: x.get("weighted_avg", 0),
        reverse=True,
    )

    for i, r in enumerate(sorted_results[:10], 1):
        score = r.get("weighted_avg", 0)
        top_table.add_row(str(i), r.get("skill", ""), r.get("category", ""), f"{score:.2f}")

    console.print(top_table)

    # Bottom skills (needs attention)
    console.print("\n[bold red]Bottom 10 Basic Skills (Needs Upgrade)[/bold red]")

    bottom_table = Table(show_header=True)
    bottom_table.add_column("Rank", justify="right", width=5)
    bottom_table.add_column("Skill", style="cyan")
    bottom_table.add_column("Category", style="dim")
    bottom_table.add_column("Score", justify="right", style="red")

    basic_skills = [r for r in sorted_results if r.get("tier") == "basic"]

    for i, r in enumerate(basic_skills[:10], 1):
        score = r.get("weighted_avg", 0)
        bottom_table.add_row(str(i), r.get("skill", ""), r.get("category", ""), f"{score:.2f}")

    console.print(bottom_table)

    # Recommendations
    console.print("\n[bold cyan]Recommendations[/bold cyan]")

    # Find categories with most basic skills
    basic_by_cat = {}
    for r in results:
        if "error" not in r and r.get("tier") == "basic":
            cat = r.get("category", "unknown")
            basic_by_cat[cat] = basic_by_cat.get(cat, 0) + 1

    top_basic_cats = sorted(basic_by_cat.items(), key=lambda x: x[1], reverse=True)[:5]

    console.print("  Priority categories for upgrade:")
    for cat, count in top_basic_cats:
        console.print(f"    - {cat}: {count} basic skills")


def export_json(results: List[Dict[str, Any]], output_path: str) -> None:
    """Export results to JSON."""
    progress = calculate_progress(results)

    output = {
        "generated_at": datetime.now().isoformat(),
        "summary": progress,
        "skills": results,
    }

    with open(output_path, "w") as f:
        json.dump(output, f, indent=2)

    print(f"Exported to {output_path}")


def export_csv(results: List[Dict[str, Any]], output_path: str) -> None:
    """Export results to CSV."""
    import csv

    with open(output_path, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["skill", "category", "tier", "score", "section_count", "code_blocks"])

        for r in results:
            if "error" in r:
                continue
            writer.writerow(
                [
                    r.get("skill", ""),
                    r.get("category", ""),
                    r.get("tier", ""),
                    r.get("weighted_avg", 0),
                    r.get("section_count", 0),
                    r.get("code_blocks", 0),
                ]
            )

    print(f"Exported to {output_path}")


def main():
    """Main entry point."""
    import argparse

    parser = argparse.ArgumentParser(description="Progress Tracker Dashboard")
    parser.add_argument("--output", "-o", choices=["text", "json", "csv"], default="text")
    parser.add_argument("--path", "-p", help="Output file path (for json/csv)")
    parser.add_argument("--category", "-c", help="Filter by category")
    args = parser.parse_args()

    results = load_all_scores()

    # Filter by category if specified
    if args.category:
        results = [r for r in results if "error" not in r and r.get("category") == args.category]

    if args.output == "json":
        if args.path:
            export_json(results, args.path)
        else:
            print(json.dumps(calculate_progress(results), indent=2))
    elif args.output == "csv":
        if args.path:
            export_csv(results, args.path)
        else:
            print("Error: --path required for CSV export")
    else:
        print_dashboard(results)


if __name__ == "__main__":
    main()
