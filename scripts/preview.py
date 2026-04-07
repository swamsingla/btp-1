"""
preview.py — Convert Markdown+LaTeX (.md) files to HTML with MathJax rendering.

Opens the result in the default browser for proper LaTeX formula display.

Usage:
  python scripts/preview.py <file.md>                  # Preview a single file
  python scripts/preview.py <directory>                 # Preview all .md files in dir
  python scripts/preview.py data/output/grade10/maths/chapter1  # Preview a chapter
"""

import sys
import re
import webbrowser
from pathlib import Path

# MathJax processes raw LaTeX directly — we just need to preserve $...$ and $$...$$
# and convert the markdown structure to HTML around them.

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<script>
window.MathJax = {{
  tex: {{
    inlineMath: [['$', '$']],
    displayMath: [['$$', '$$']],
    processEscapes: true,
    processEnvironments: true,
    tags: 'ams'
  }},
  svg: {{
    fontCache: 'global'
  }},
  options: {{
    skipHtmlTags: ['script', 'noscript', 'style', 'textarea', 'pre', 'code'],
    ignoreHtmlClass: 'no-mathjax'
  }},
  startup: {{
    pageReady: function() {{
      return MathJax.startup.defaultPageReady().then(function() {{
        console.log('MathJax rendering complete');
      }});
    }}
  }}
}};
</script>
<script id="MathJax-script" async
  src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-svg.js">
</script>
<style>
  :root {{
    --bg: #0d1117;
    --fg: #c9d1d9;
    --accent: #58a6ff;
    --border: #30363d;
    --card-bg: #161b22;
    --code-bg: #1f2937;
  }}
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}
  body {{
    font-family: 'Segoe UI', -apple-system, sans-serif;
    background: var(--bg);
    color: var(--fg);
    line-height: 1.8;
    padding: 2rem;
    max-width: 900px;
    margin: 0 auto;
  }}
  h1 {{ color: var(--accent); font-size: 2rem; margin: 1.5rem 0 1rem;
       border-bottom: 2px solid var(--border); padding-bottom: 0.5rem; }}
  h2 {{ color: #79c0ff; font-size: 1.5rem; margin: 1.8rem 0 0.8rem; }}
  h3 {{ color: #d2a8ff; font-size: 1.2rem; margin: 1.2rem 0 0.5rem; }}
  p {{ margin: 0.6rem 0; }}
  ul, ol {{ margin: 0.6rem 0 0.6rem 1.5rem; }}
  li {{ margin: 0.3rem 0; }}
  blockquote {{
    border-left: 4px solid var(--accent);
    padding: 0.8rem 1.2rem;
    margin: 1rem 0;
    background: var(--card-bg);
    border-radius: 0 8px 8px 0;
  }}
  blockquote p {{ margin: 0.3rem 0; }}
  code {{
    background: var(--code-bg);
    padding: 0.2rem 0.4rem;
    border-radius: 4px;
    font-size: 0.9em;
    font-family: 'Cascadia Code', 'Fira Code', monospace;
  }}
  pre {{
    background: var(--code-bg);
    padding: 1rem;
    border-radius: 8px;
    overflow-x: auto;
    margin: 0.8rem 0;
  }}
  pre code {{ background: none; padding: 0; }}
  strong {{ color: #ffa657; }}
  em {{ color: #d2a8ff; }}
  hr {{ border: none; border-top: 1px solid var(--border); margin: 2rem 0; }}
  /* Display math blocks */
  .display-math {{
    display: block;
    text-align: center;
    margin: 1.2rem 0;
    padding: 0.8rem;
    background: var(--card-bg);
    border-radius: 8px;
    overflow-x: auto;
  }}
  /* Navigation */
  .file-nav {{
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-radius: 8px;
    padding: 1rem;
    margin-bottom: 2rem;
    line-height: 2.2;
  }}
  .file-nav a {{
    color: var(--accent);
    text-decoration: none;
    margin-right: 0.5rem;
    padding: 0.3rem 0.6rem;
    border-radius: 4px;
    font-size: 0.85rem;
  }}
  .file-nav a:hover {{ background: var(--border); }}
  .lang-badge {{
    display: inline-block;
    padding: 0.15rem 0.5rem;
    border-radius: 12px;
    font-size: 0.8rem;
    margin: 0.2rem;
    font-weight: bold;
  }}
  .lang-en {{ background: #1f6feb; color: white; }}
  .lang-hi {{ background: #da3633; color: white; }}
  .lang-te {{ background: #238636; color: white; }}
  .lang-od {{ background: #a371f7; color: white; }}
  .section-divider {{
    margin: 3rem 0;
    border-top: 3px solid var(--accent);
    padding-top: 1rem;
  }}
</style>
</head>
<body>
{nav}
{content}
</body>
</html>"""


def md_to_html(md_text: str) -> str:
    """Convert markdown to HTML while preserving LaTeX for MathJax.

    Strategy: Convert markdown syntax to HTML but leave all $...$ and $$...$$
    completely untouched — MathJax will process them in the browser.
    """
    # First, fix any LaTeX formatting issues in the input
    md_text = _fix_latex_for_display(md_text)

    lines = md_text.split('\n')
    html_parts = []
    in_code_block = False
    in_blockquote = False
    in_list = False
    list_type = None

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        # Code blocks
        if stripped.startswith('```'):
            if in_code_block:
                html_parts.append('</code></pre>')
                in_code_block = False
            else:
                lang = stripped[3:].strip()
                html_parts.append(f'<pre><code class="{lang}">')
                in_code_block = True
            i += 1
            continue

        if in_code_block:
            html_parts.append(_escape_html(line))
            i += 1
            continue

        # Close list if we exit
        if in_list and not stripped and i + 1 < len(lines) and not _is_list_item(lines[i + 1].strip()):
            html_parts.append(f'</{list_type}>')
            in_list = False

        # Close blockquote if we exit
        if in_blockquote and not stripped.startswith('>') and not stripped == '':
            html_parts.append('</blockquote>')
            in_blockquote = False

        # Empty line
        if not stripped:
            i += 1
            continue

        # Horizontal rule
        if stripped in ('---', '***', '___'):
            if in_list:
                html_parts.append(f'</{list_type}>')
                in_list = False
            html_parts.append('<hr>')
            i += 1
            continue

        # Display math block: standalone $$...$$ on its own line
        if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
            if in_list:
                html_parts.append(f'</{list_type}>')
                in_list = False
            html_parts.append(f'<div class="display-math">{stripped}</div>')
            i += 1
            continue

        # Multi-line display math: $$ on its own line
        if stripped == '$$':
            math_lines = ['$$']
            i += 1
            while i < len(lines) and lines[i].strip() != '$$':
                math_lines.append(lines[i])
                i += 1
            math_lines.append('$$')
            if i < len(lines):
                i += 1
            html_parts.append(f'<div class="display-math">{chr(10).join(math_lines)}</div>')
            continue

        # Headers
        header_match = re.match(r'^(#{1,6})\s+(.*)', stripped)
        if header_match:
            if in_list:
                html_parts.append(f'</{list_type}>')
                in_list = False
            level = len(header_match.group(1))
            text = _inline_format(header_match.group(2))
            html_parts.append(f'<h{level}>{text}</h{level}>')
            i += 1
            continue

        # Blockquote
        if stripped.startswith('>'):
            if not in_blockquote:
                html_parts.append('<blockquote>')
                in_blockquote = True
            text = _inline_format(stripped[1:].strip())
            if text:
                html_parts.append(f'<p>{text}</p>')
            i += 1
            continue

        # List items
        if _is_list_item(stripped):
            item_text, new_list_type = _parse_list_item(stripped)
            if not in_list or list_type != new_list_type:
                if in_list:
                    html_parts.append(f'</{list_type}>')
                html_parts.append(f'<{new_list_type}>')
                in_list = True
                list_type = new_list_type
            html_parts.append(f'<li>{_inline_format(item_text)}</li>')
            i += 1
            continue

        # Regular paragraph
        if in_blockquote:
            html_parts.append('</blockquote>')
            in_blockquote = False
        html_parts.append(f'<p>{_inline_format(stripped)}</p>')
        i += 1

    # Close any open elements
    if in_list:
        html_parts.append(f'</{list_type}>')
    if in_blockquote:
        html_parts.append('</blockquote>')
    if in_code_block:
        html_parts.append('</code></pre>')

    return '\n'.join(html_parts)


def _fix_latex_for_display(text: str) -> str:
    """Pre-process text to ensure display math is on its own line for MathJax."""
    # Split consecutive $$...$$ blocks
    for _ in range(5):
        new = re.sub(r'(\$\$[^$]+\$\$)\s*(\$\$[^$])', r'\1\n\n\2', text)
        if new == text:
            break
        text = new

    # Ensure display math is on its own line
    text = re.sub(r'([^\n$])\s*(\$\$)(?!\$)', r'\1\n\n\2', text)
    text = re.sub(r'(\$\$)\s*([^\n$\s])', r'\1\n\n\2', text)

    # Ensure spaces around inline math
    text = re.sub(r'([a-zA-Z0-9,;:})\]\.])\$(?!\$)', r'\1 $', text)
    text = re.sub(
        r'(?<!\$)\$([^$\n]+)\$([a-zA-Z0-9({[\[])',
        lambda m: f'${m.group(1)}$ {m.group(2)}', text
    )

    return text


def _escape_html(text: str) -> str:
    """Escape HTML special characters (for code blocks)."""
    return text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')


def _is_list_item(stripped: str) -> bool:
    """Check if a line is a list item."""
    if stripped.startswith(('- ', '* ', '• ')):
        return True
    if stripped and stripped[0] in '🟢🟡🔴':
        return True
    if stripped and stripped[0].isdigit() and re.match(r'^\d+\.\s', stripped):
        return True
    return False


def _parse_list_item(stripped: str) -> tuple:
    """Parse a list item, returning (text, list_type)."""
    if stripped.startswith(('- ', '* ', '• ')):
        return stripped[2:].strip(), 'ul'
    if stripped and stripped[0] in '🟢🟡🔴':
        return stripped, 'ul'
    m = re.match(r'^\d+\.\s+(.*)', stripped)
    if m:
        return m.group(1), 'ol'
    return stripped, 'ul'


def _inline_format(text: str) -> str:
    """Apply inline markdown formatting while preserving LaTeX."""
    # Split at LaTeX boundaries: process only non-LaTeX parts
    latex_split = re.compile(r'(\$\$[^$]+\$\$|\$[^$]+\$)')
    parts = latex_split.split(text)
    result = []
    for i, part in enumerate(parts):
        if i % 2 == 1:
            # LaTeX — keep exactly as-is
            result.append(part)
        else:
            # Apply markdown formatting to non-LaTeX parts
            # Bold: **text**
            part = re.sub(r'\*\*([^*]+)\*\*', r'<strong>\1</strong>', part)
            # Italic: *text*
            part = re.sub(r'(?<!\*)\*([^*]+)\*(?!\*)', r'<em>\1</em>', part)
            # Inline code: `text`
            part = re.sub(r'`([^`]+)`', r'<code>\1</code>', part)
            result.append(part)
    return ''.join(result)


def preview_file(md_path: Path) -> str:
    """Convert a single .md file to HTML content string."""
    with open(md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return md_to_html(content)


def preview_chapter(chapter_dir: Path) -> str:
    """Create a combined HTML preview for an entire chapter with navigation."""
    chapter_dir = Path(chapter_dir)

    # Find all English .md files
    md_files = sorted(chapter_dir.glob("*.md"))
    if not md_files:
        print(f"No .md files found in {chapter_dir}")
        return ""

    nav_links = []
    sections = []

    # Discover translation directories
    lang_dirs = {}
    for sub in chapter_dir.iterdir():
        if sub.is_dir():
            # Old style: hi/, te/, od/
            if sub.name in ('hi', 'te', 'od'):
                lang_dirs[sub.name] = sub
            # New style: indic1b/hi/, tgemma/te/
            elif sub.name in ('indic1b', 'tgemma'):
                for lang_sub in sub.iterdir():
                    if lang_sub.is_dir() and lang_sub.name in ('hi', 'te', 'od'):
                        lang_dirs[f"{sub.name}/{lang_sub.name}"] = lang_sub

    # English files
    for md_file in md_files:
        fid = md_file.stem.replace('.', '-').replace(' ', '-')
        nav_links.append(f'<a href="#en-{fid}" class="lang-badge lang-en">EN: {md_file.stem}</a>')
        html_content = preview_file(md_file)
        sections.append(
            f'<div class="section-divider" id="en-{fid}">'
            f'<span class="lang-badge lang-en">English</span>'
            f'{html_content}</div>'
        )

    # Translated files
    lang_css = {'hi': 'lang-hi', 'te': 'lang-te', 'od': 'lang-od'}
    lang_names = {'hi': 'Hindi', 'te': 'Telugu', 'od': 'Odia'}

    for lang_key, lang_path in sorted(lang_dirs.items()):
        lang_code = lang_key.split('/')[-1] if '/' in lang_key else lang_key
        css = lang_css.get(lang_code, '')
        label = lang_key.replace('/', ' ').upper()

        for md_file in sorted(lang_path.glob("*.md")):
            fid = f"{lang_key.replace('/', '-')}-{md_file.stem}".replace('.', '-').replace(' ', '-')
            nav_links.append(f'<a href="#{fid}" class="lang-badge {css}">{label}: {md_file.stem}</a>')
            html_content = preview_file(md_file)
            sections.append(
                f'<div class="section-divider" id="{fid}">'
                f'<span class="lang-badge {css}">{label}</span>'
                f'{html_content}</div>'
            )

    nav_html = '<div class="file-nav">\n<strong>Navigate:</strong><br>\n' + '\n'.join(nav_links) + '\n</div>'
    return HTML_TEMPLATE.format(
        title=f"Preview: {chapter_dir.name}",
        nav=nav_html,
        content='\n'.join(sections)
    )


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    target = Path(sys.argv[1])
    base = Path(__file__).parent.parent

    if not target.is_absolute():
        target = base / target

    if target.is_file() and target.suffix == '.md':
        html = HTML_TEMPLATE.format(
            title=target.stem,
            nav='',
            content=preview_file(target)
        )
        out_path = target.with_suffix('.html')
    elif target.is_dir():
        html = preview_chapter(target)
        out_path = target / "_preview.html"
    else:
        print(f"ERROR: {target} is not a .md file or directory")
        sys.exit(1)

    if not html:
        sys.exit(1)

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"Preview: {out_path}")
    webbrowser.open(str(out_path))


if __name__ == "__main__":
    main()
