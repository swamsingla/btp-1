"""Fix LaTeX formatting in existing generated .md files.

Fixes:
  1. Display math $$...$$ put on its own line
  2. Inline math $...$ gets spaces around it
  3. Multiple $$...$$ on same line split apart

Usage:
  python scripts/fix_latex.py data/output/grade10/maths/chapter1
  python scripts/fix_latex.py data/output   # fix all
"""
import re
import sys
from pathlib import Path


def fix_latex_formatting(text: str) -> str:
    """Fix LaTeX formatting for proper MathJax/markdown rendering."""

    # Step 1: Split consecutive display math blocks onto separate lines.
    # $$...$$$$...$$ → $$...$$ \n\n $$...$$
    # Repeat until stable (handles 3+ consecutive blocks)
    for _ in range(5):
        new = re.sub(r'(\$\$[^$]+\$\$)\s*(\$\$[^$])', r'\1\n\n\2', text)
        if new == text:
            break
        text = new

    # Step 2: Display math $$...$$ on its own line.
    # Text before $$: add newline
    text = re.sub(r'([^\n$])\s*(\$\$)(?!\$)', r'\1\n\n\2', text)
    # Text after closing $$: add newline
    text = re.sub(r'(\$\$)\s*([^\n$\s])', r'\1\n\n\2', text)

    # Step 3: Ensure spaces around inline $...$.
    # Space before opening $ if preceded by letter/digit/punctuation
    text = re.sub(r'([a-zA-Z0-9,;:})\]\.])\$(?!\$)', r'\1 $', text)
    # Space after closing $ if followed by letter/digit
    text = re.sub(r'(?<!\$)\$([^$\n]+)\$([a-zA-Z0-9({[\[])', lambda m: f'${m.group(1)}$ {m.group(2)}', text)

    # Step 4: Clean up excessive blank lines (max 2 consecutive)
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    return text


def fix_file(filepath: Path) -> bool:
    """Fix a single .md file. Returns True if changes were made."""
    with open(filepath, 'r', encoding='utf-8') as f:
        original = f.read()

    fixed = fix_latex_formatting(original)

    if fixed != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(fixed)
        return True
    return False


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    target = Path(sys.argv[1])
    base = Path(__file__).parent.parent

    if not target.is_absolute():
        target = base / target

    if target.is_file() and target.suffix == '.md':
        files = [target]
    elif target.is_dir():
        files = sorted(target.rglob("*.md"))
    else:
        print(f"ERROR: {target} not found")
        sys.exit(1)

    fixed_count = 0
    for f in files:
        if fix_file(f):
            print(f"  Fixed: {f.name}")
            fixed_count += 1

    print(f"\n{fixed_count}/{len(files)} files fixed.")


if __name__ == "__main__":
    main()
