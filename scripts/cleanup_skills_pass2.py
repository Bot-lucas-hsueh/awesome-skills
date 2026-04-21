#!/usr/bin/env python3
"""
Second-pass cleanup script for skill files.
Fixes remaining issues missed by the first pass due to pattern variations.

Remaining issues fixed:
1. Self-Score with format "**Self-Score: X.X/10 — ..." (colon not followed by **)
2. Generic §16 with ### prefix (3 hashes instead of 2)
3. Standalone "### Additional Resources" with generic content
4. Duplicate frontmatter descriptions (fix_duplicate_description regex bug)
5. Generic ## Workflow with Board Prep in README.md files (enterprise/)
6. Empty "## § 1 · System Prompt" header left after sub-section removal
"""

import re
import os
import glob
from pathlib import Path

SKILLS_DIR = Path('/home/user/awesome-skills/skills')

# Fix 1: More permissive Self-Score pattern
# Handles: **Self-Score: 8.5/10 — Expert Tier, **Self-Score: 9.5/10 — EXCELLENCE ⭐⭐⭐**
SELF_SCORE_PERMISSIVE = re.compile(
    r'\n\*\*Self-Score:[^\n]*',
)

# Fix 2: §16 with ### prefix
GENERIC_SECTION_16_H3 = re.compile(
    r'\n### § 16 · Domain Deep Dive\n'
    r'.*?'
    r'(?=\n### § 1[7-9]|\n## (?!§ 1[7-9])|\Z)',
    re.DOTALL
)

# Also handle §17-19 with ### prefix
GENERIC_SECTION_17_H3 = re.compile(
    r'\n### § 17 · Risk Management Deep Dive\n'
    r'.*?'
    r'(?=\n### § 18|\n## (?!§ 18)|\Z)',
    re.DOTALL
)

GENERIC_SECTION_18_H3 = re.compile(
    r'\n### § 18 · Excellence Framework\n'
    r'.*?'
    r'(?=\n### § 19|\n## (?!§ 19)|\Z)',
    re.DOTALL
)

GENERIC_SECTION_19_H3 = re.compile(
    r'\n### § 19 · Best Practices Library\n'
    r'.*?'
    r'(?=\n### § 2[01]|\n## (?!§ 2[01])|\Z)',
    re.DOTALL
)

# Fix 3: Standalone "### Additional Resources" with generic content
GENERIC_ADDITIONAL_RESOURCES = re.compile(
    r'\n### Additional Resources\n'
    r'- Industry standards\n'
    r'- Best practice guides\n'
    r'- Training materials\n',
)

# Fix 4: Duplicate frontmatter description (corrected version)
def fix_duplicate_description(content):
    """Remove duplicate text in frontmatter description field."""
    def dedup_desc(m):
        full_line = m.group(0)
        prefix = 'description: '
        if not full_line.startswith(prefix):
            return full_line
        desc = full_line[len(prefix):]
        words = desc.split()
        if len(words) < 10:
            return full_line
        # Use first 5 words to detect repetition
        first5 = ' '.join(words[:5])
        count = desc.count(first5)
        if count <= 1:
            return full_line
        # Find the second occurrence and truncate before it
        idx = desc.find(first5, len(first5))
        if idx > 0:
            cleaned = desc[:idx].rstrip('. ')
            return f'{prefix}{cleaned}'
        return full_line

    return re.sub(r'^description: .+$', dedup_desc, content, flags=re.MULTILINE)

# Fix 5: Generic ## Workflow with Board Prep (handles multiple blank lines before section)
def remove_board_prep_workflow(content):
    """Remove ## Workflow section only when it contains the Board Prep boilerplate."""
    pattern = re.compile(
        r'\n+## Workflow\n+'
        r'.*?'
        r'(?=\n## [^#]|\Z)',
        re.DOTALL
    )
    def replace_if_board_prep(m):
        if '### Phase 1: Board Prep' in m.group():
            return ''
        return m.group()
    return pattern.sub(replace_if_board_prep, content)

# Fix 6: Clean up empty ## § 1 · System Prompt header
# After removing sub-sections, sometimes left with empty header + separators
EMPTY_SYSTEM_PROMPT = re.compile(
    r'\n## § 1 · System Prompt\n'
    r'(?:\n|---\n)*'
    r'\n*'
    r'(?=\n## |\n### |\n# )',
)

# Also fix: Empty "## § 1 · System Prompt" with only separators and empty lines
def clean_empty_section1(content):
    """Remove § 1 header if it has no meaningful content after sub-section removal."""
    pattern = re.compile(
        r'(## § 1 · System Prompt\n)'
        r'(\n|---\n|\n---\n)*'
        r'(?=\n## [^§]|\n## § [^1])',
    )
    def replace_if_empty(m):
        # If there's nothing but newlines and --- between header and next ##, remove it
        middle = m.group(0)[len(m.group(1)):]
        if re.match(r'^[\n\-]+$', middle.strip()):
            return ''
        return m.group(0)
    return pattern.sub(replace_if_empty, content)

# Generic Error Handling section with multi-newline prefix
def remove_generic_error_handling(content):
    """Remove ## Error Handling section with boilerplate content."""
    pattern = re.compile(
        r'\n+## Error Handling\n'
        r'.*?'
        r'(?=\n## [^#]|\Z)',
        re.DOTALL
    )
    def replace_if_generic(m):
        if 'Retry with Budget overrun' in m.group():
            return ''
        return m.group()
    return pattern.sub(replace_if_generic, content)


def cleanup_file(filepath):
    """Apply second-pass cleanup to a single file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    content = original

    # Fix duplicate descriptions
    content = fix_duplicate_description(content)

    # Fix Self-Score (permissive pattern)
    content = SELF_SCORE_PERMISSIVE.sub('', content)

    # Fix §16-19 with ### prefix
    content = GENERIC_SECTION_16_H3.sub('', content)
    content = GENERIC_SECTION_17_H3.sub('', content)
    content = GENERIC_SECTION_18_H3.sub('', content)
    content = GENERIC_SECTION_19_H3.sub('', content)

    # Remove standalone Additional Resources boilerplate
    content = GENERIC_ADDITIONAL_RESOURCES.sub('\n', content)

    # Remove Board Prep workflow (more permissive)
    content = remove_board_prep_workflow(content)

    # Remove generic error handling (more permissive)
    content = remove_generic_error_handling(content)

    # Clean up empty § 1 header
    content = clean_empty_section1(content)

    # Clean up excessive blank lines
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    content = content.rstrip('\n') + '\n'

    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        return True
    return False


def main():
    # Process both SKILL.md and README.md files in skills/
    skill_files = sorted(SKILLS_DIR.rglob('SKILL.md'))
    readme_files = sorted(SKILLS_DIR.rglob('README.md'))
    all_files = skill_files + readme_files

    total = len(all_files)
    modified = 0
    errors = []

    print(f"Processing {total} files (pass 2)...")

    for filepath in all_files:
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
