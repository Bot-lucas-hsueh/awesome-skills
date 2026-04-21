#!/usr/bin/env python3
"""
Cleanup script for skill files - removes boilerplate, generic content,
and other quality issues discovered during review.

Issues fixed:
1. Self-Score artifacts (423 files)
2. Generic §16-19 boilerplate sections (450-559 files each)
3. Generic §21 Resources & References section
4. Quality Checklist / Performance Metrics / Additional Resources boilerplate
5. Board Prep workflow boilerplate in non-executive skills (195 files)
6. Generic Error Handling with "Retry with Budget overrun" (184 files)
7. Generic Error Handling & Recovery table boilerplate
8. Generic Examples placeholder sections (645 files)
9. Generic §1.1 Identity/§1.2 Decision Framework/§1.3 Thinking Patterns tables
10. Generic ###1.1 Role Definition template blocks
11. Duplicate frontmatter descriptions (138 files)
"""

import re
import os
import glob
from pathlib import Path

SKILLS_DIR = Path('/home/user/awesome-skills/skills')

# Patterns that identify purely generic (non-domain-specific) sections

GENERIC_SECTION_16 = re.compile(
    r'\n## § 16 · Domain Deep Dive\n'
    r'.*?'
    r'(?=\n## (?!§ 1[7-9])|$)',
    re.DOTALL
)

GENERIC_SECTION_17 = re.compile(
    r'\n## § 17 · Risk Management Deep Dive\n'
    r'.*?'
    r'(?=\n## (?!§ 18)|$)',
    re.DOTALL
)

GENERIC_SECTION_18 = re.compile(
    r'\n## § 18 · Excellence Framework\n'
    r'.*?'
    r'(?=\n## (?!§ 19)|$)',
    re.DOTALL
)

GENERIC_SECTION_19 = re.compile(
    r'\n## § 19 · Best Practices Library\n'
    r'.*?'
    r'(?=\n## (?!§ 2[01])|$)',
    re.DOTALL
)

# Generic §21 with only generic rows (Industry Standards / Research Papers / Case Studies)
GENERIC_SECTION_21 = re.compile(
    r'\n## § 21 · Resources & References\n'
    r'\n\| Resource \| Type \| Key Takeaway \|\n'
    r'\|[-|]+\|\n'
    r'\| Industry Standards \| Guidelines \| Compliance requirements \|\n'
    r'\| Research Papers \| Academic \| Latest methodologies \|\n'
    r'\| Case Studies \| Practical \| Real-world applications \|\n',
    re.DOTALL
)

# Generic Quality Checklist + Performance Metrics + Additional Resources block
GENERIC_QUALITY_BLOCK = re.compile(
    r'\n### Quality Checklist\n'
    r'- \[ \] Requirements met\n'
    r'- \[ \] Standards compliant\n'
    r'- \[ \] Reviewed by peers\n'
    r'\n*'
    r'(?:'
        r'\n### Performance Metrics\n'
        r'\| Metric \| Target \| Actual \| Status \|\n'
        r'\|[-|]+\|\n'
        r'\n*'
    r')?'
    r'(?:'
        r'\n### Additional Resources\n'
        r'- Industry standards\n'
        r'- Best practice guides\n'
        r'- Training materials\n'
    r')?',
    re.DOTALL
)

# Empty performance metrics table (standalone)
EMPTY_PERF_METRICS = re.compile(
    r'\n### Performance Metrics\n'
    r'\| Metric \| Target \| Actual \| Status \|\n'
    r'\|[-|]+\|\n'
    r'\n',
)

# Generic §1.1 Identity table (always empty under the heading)
GENERIC_S1_IDENTITY = re.compile(
    r'\n### § 1\.1 · Identity — Professional DNA\n'
    r'\n*'
    r'(?=### § 1\.2|### 1\.1|\Z)',
    re.DOTALL
)

# Generic §1.2 Decision Framework table (identical across all files)
GENERIC_S1_DECISION_TABLE = re.compile(
    r'\n### § 1\.2 · Decision Framework — Weighted Criteria \(0-100\)\n'
    r'\n'
    r'\| Criterion \| Weight \| Assessment Method \| Threshold \| Fail Action \|\n'
    r'\|[-|]+\|\n'
    r'\| Quality \| 30 \| Verification against standards \| Meet criteria \| Revise \|\n'
    r'\| Efficiency \| 25 \| Time/resource optimization \| Within budget \| Optimize \|\n'
    r'\| Accuracy \| 25 \| Precision and correctness \| Zero defects \| Fix \|\n'
    r'\| Safety \| 20 \| Risk assessment \| Acceptable \| Mitigate \|\n'
    r'\n*',
)

# Generic §1.3 Thinking Patterns table (identical across all files)
GENERIC_S1_THINKING_TABLE = re.compile(
    r'\n### § 1\.3 · Thinking Patterns — Mental Models\n'
    r'\n'
    r'\| Dimension \| Mental Model \|\n'
    r'\|[-|]+\|\n'
    r'\| Root Cause \| 5 Whys Analysis \|\n'
    r'\| Trade-offs \| Pareto Optimization \|\n'
    r'\| Verification \| Multiple Layers \|\n'
    r'\| Learning \| PDCA Cycle \|\n'
    r'\n*',
)

# Generic ### 1.1 Role Definition block (boilerplate expert template)
GENERIC_ROLE_DEF = re.compile(
    r'\n### 1\.1 Role Definition\n'
    r'\n'
    r'\*\*Identity:\*\*\n'
    r'You are an expert .+? with 15\+ years of professional experience\. '
    r'You combine deep domain expertise with practical execution capabilities '
    r'to deliver exceptional results in complex environments\.\n'
    r'\n'
    r'\*\*Core Expertise:\*\*\n'
    r'- Comprehensive theoretical and practical mastery of the domain\n'
    r'- Cross-industry experience and pattern recognition capabilities  \n'
    r'- Cutting-edge methodology and best practice implementation\n'
    r'- Strategic thinking combined with tactical execution excellence\n'
    r'\n'
    r'\*\*Personality & Approach:\*\*\n'
    r'- Professional yet approachable communication style\n'
    r'- Detail-oriented and systematic in problem-solving\n'
    r'- Data-driven and evidence-based decision making\n'
    r'- Collaborative and solution-focused mindset\n',
    re.DOTALL
)

# Generic 1.2 Decision Framework (First Principles + generic table)
GENERIC_DECISION_FRAMEWORK = re.compile(
    r'\n### 1\.2 Decision Framework\n'
    r'\n'
    r'\*\*First Principles:\*\*\n'
    r'1\. \*\*Safety & Ethics First\*\* — Always prioritize safety, compliance, and ethical considerations\n'
    r'2\. \*\*Validate Assumptions\*\* — Test hypotheses before building solutions\n'
    r'3\. \*\*Balance Theory & Practice\*\* — Combine ideal practices with practical constraints\n'
    r'4\. \*\*Document Rationale\*\* — Record decisions and their justifications\n'
    r'\n'
    r'\*\*Decision Hierarchy:\*\*\n'
    r'\| Priority \| Factor \| Key Questions \|\n'
    r'\|[-|]+\|\n'
    r'\| 1 \| Safety \| Is this safe\? Compliant\? Ethical\? \|\n'
    r'\| 2 \| Quality \| Does this meet standards\? Sustainable\? \|\n'
    r'\| 3 \| Efficiency \| Resource-optimal\? Timeline feasible\? \|\n'
    r'\| 4 \| Innovation \| Better approach possible\? \|\n',
    re.DOTALL
)

# Generic 1.3 Thinking Patterns (Analytical/Creative/Pragmatic)
GENERIC_THINKING_PATTERNS = re.compile(
    r'\n### 1\.3 Thinking Patterns\n'
    r'\n'
    r'\*\*Analytical Approach:\*\*\n'
    r'- Decompose complex problems into manageable components\n'
    r'- Identify root causes rather than symptoms\n'
    r'- Apply structured frameworks and methodologies\n'
    r'- Validate conclusions with evidence and data\n'
    r'\n'
    r'\*\*Creative Approach:\*\*\n'
    r'- Explore multiple solution paths simultaneously\n'
    r'- Apply cross-domain knowledge for innovation\n'
    r'- Challenge conventional thinking constructively\n'
    r'- Prototype and iterate rapidly\n'
    r'\n'
    r'\*\*Pragmatic Approach:\*\*\n'
    r'- Balance theoretical ideals with practical constraints\n'
    r'- Consider implementation feasibility and maintainability\n'
    r'- Plan for failure modes and contingencies\n'
    r'- Optimize for long-term sustainability\n',
    re.DOTALL
)

# Self-Score line (single line, various formats)
SELF_SCORE_LINE = re.compile(
    r'\n\*\*Self-Score:\*\*[^\n]*',
)

# Generic ## Workflow section containing Board Prep (not domain-specific)
def remove_board_prep_workflow(content):
    """Remove ## Workflow section only when it contains the Board Prep boilerplate."""
    pattern = re.compile(
        r'\n## Workflow\n'
        r'.*?'
        r'(?=\n## [^#]|\Z)',
        re.DOTALL
    )
    def replace_if_board_prep(m):
        if '### Phase 1: Board Prep' in m.group():
            return ''
        return m.group()
    return pattern.sub(replace_if_board_prep, content)

# Generic ## Error Handling section with "Retry with Budget overrun"
def remove_generic_error_handling(content):
    """Remove ## Error Handling section only when it contains the boilerplate recovery strategies."""
    pattern = re.compile(
        r'\n## Error Handling\n'
        r'.*?'
        r'(?=\n## [^#]|\Z)',
        re.DOTALL
    )
    def replace_if_generic(m):
        if 'Retry with Budget overrun' in m.group():
            return ''
        return m.group()
    return pattern.sub(replace_if_generic, content)

# Generic ## Error Handling & Recovery table
GENERIC_ERROR_RECOVERY = re.compile(
    r'\n## Error Handling & Recovery\n'
    r'\n'
    r'\| Scenario \| Response \|\n'
    r'\|[-|]+\|\n'
    r'\| Failure \| Analyze root cause and retry \|\n'
    r'\| Timeout \| Log and report status \|\n'
    r'\| Edge case \| Document and handle gracefully \|\n',
    re.DOTALL
)

# Generic ## Examples section with placeholder content
def remove_generic_examples(content):
    """Remove ## Examples section only when it has generic placeholder content."""
    pattern = re.compile(
        r'\n## Examples\n'
        r'.*?'
        r'(?=\n## [^#]|\Z)',
        re.DOTALL
    )
    def replace_if_generic(m):
        text = m.group()
        if ('Handle standard' in text and 'request with standard procedures' in text
                and 'Gather requirements' in text and 'Standard timeline: 2-5 business days' in text):
            return ''
        return m.group()
    return pattern.sub(replace_if_generic, content)

# Fix duplicate frontmatter description
def fix_duplicate_description(content):
    """Remove duplicate text in frontmatter description field."""
    def dedup_desc(m):
        desc = m.group(1)
        words = desc.split()
        if len(words) < 10:
            return m.group()
        # Check if first 6 words appear again
        first6 = ' '.join(words[:6])
        count = desc.count(first6)
        if count <= 1:
            return m.group()
        # Find the second occurrence and truncate
        idx = desc.find(first6, len(first6))
        if idx > 0:
            cleaned = desc[:idx].rstrip('. ')
            return f'description: {cleaned}'
        return m.group()

    return re.sub(r'^(description: .+)$', dedup_desc, content, flags=re.MULTILINE)


def cleanup_file(filepath):
    """Apply all cleanup transformations to a single SKILL.md file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    content = original

    # Fix duplicate descriptions first (frontmatter)
    content = fix_duplicate_description(content)

    # Remove self-score artifacts
    content = SELF_SCORE_LINE.sub('', content)

    # Remove generic §1 sub-sections (tables)
    content = GENERIC_S1_IDENTITY.sub('\n', content)
    content = GENERIC_S1_DECISION_TABLE.sub('\n', content)
    content = GENERIC_S1_THINKING_TABLE.sub('\n', content)

    # Remove generic role definition template
    content = GENERIC_ROLE_DEF.sub('\n', content)
    content = GENERIC_DECISION_FRAMEWORK.sub('\n', content)
    content = GENERIC_THINKING_PATTERNS.sub('\n', content)

    # Remove generic §16-19 boilerplate sections
    content = GENERIC_SECTION_16.sub('', content)
    content = GENERIC_SECTION_17.sub('', content)
    content = GENERIC_SECTION_18.sub('', content)
    content = GENERIC_SECTION_19.sub('', content)

    # Remove generic §21 Resources section
    content = GENERIC_SECTION_21.sub('\n', content)

    # Remove quality checklist + performance metrics + additional resources boilerplate
    content = GENERIC_QUALITY_BLOCK.sub('\n', content)
    content = EMPTY_PERF_METRICS.sub('\n', content)

    # Remove board prep workflow in non-executive skills
    content = remove_board_prep_workflow(content)

    # Remove generic error handling sections
    content = remove_generic_error_handling(content)
    content = GENERIC_ERROR_RECOVERY.sub('\n', content)

    # Remove generic examples sections
    content = remove_generic_examples(content)

    # Clean up excessive blank lines (max 2 consecutive)
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    # Ensure file ends with single newline
    content = content.rstrip('\n') + '\n'

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    skill_files = sorted(SKILLS_DIR.rglob('SKILL.md'))
    total = len(skill_files)
    modified = 0
    errors = []

    print(f"Processing {total} SKILL.md files...")

    for i, filepath in enumerate(skill_files):
        try:
            if cleanup_file(filepath):
                modified += 1
                if modified <= 5 or modified % 100 == 0:
                    print(f"  Modified: {filepath.relative_to(SKILLS_DIR)}")
        except Exception as e:
            errors.append((filepath, str(e)))
            print(f"  ERROR: {filepath}: {e}")

    print(f"\nDone: {modified}/{total} files modified")
    if errors:
        print(f"Errors ({len(errors)}):")
        for f, e in errors:
            print(f"  {f}: {e}")


if __name__ == '__main__':
    main()
