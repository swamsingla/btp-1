"""
md_to_json.py — Convert generated markdown files to the JSON format
expected by the NCERT Smart Wiki server and MongoDB uploader.

Usage:
    python scripts/md_to_json.py output/qwen3_v2/
    python scripts/md_to_json.py data/output/grade11/maths/chapter1/

Output:
    data/generated/grade{N}/maths/chapter{N}/en.json

Changes from original:
  - Adds heading numbering (1. Prerequisites, 2. Introduction, etc.)
  - Removes Exam-Style Questions section entirely
  - Orders practice problems: Easy → Medium → Hard
  - Related Topics become full page links for individual topic pages
  - Difficulty badges: 🟢 🟡 🔴 wrapped in styled spans
  - Properly includes theorems/proofs in blockquotes

LaTeX is preserved ($...$ and $$...$$) — KaTeX on the client renders it.
"""

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent.parent


def md_to_html(text: str, topic_num_to_id: dict, grade: int, subject: str,
               chapter: int) -> str:
    """
    Lightweight markdown → HTML converter.
    Preserves LaTeX, adds heading numbering, removes exam questions,
    orders practice problems, converts related topics to page links.
    """
    # ── Step 0: Remove Exam-Style Questions section ─────────────────
    text = re.sub(
        r'##\s*Exam-Style Questions.*?(?=\n##\s|\Z)',
        '', text, flags=re.DOTALL
    )

    # ── Step 1: Protect LaTeX from markdown processing ──────────────
    latex_blocks = []

    def stash_latex(m):
        idx = len(latex_blocks)
        latex_blocks.append(m.group(0))
        return f"LATEXBLOCK{idx}LATEXEND"

    text = re.sub(r'\$\$(.+?)\$\$', stash_latex, text, flags=re.DOTALL)
    text = re.sub(r'\$([^\$\n]+?)\$', stash_latex, text)

    # ── Step 2: Process markdown ────────────────────────────────────
    lines = text.split('\n')
    html_lines = []
    in_ul = False
    in_ol = False
    in_table = False
    in_blockquote = False
    table_rows = []

    def flush_list():
        nonlocal in_ul, in_ol
        if in_ul:
            html_lines.append('</ul>')
            in_ul = False
        if in_ol:
            html_lines.append('</ol>')
            in_ol = False

    def flush_table():
        nonlocal in_table, table_rows
        if in_table and table_rows:
            html_lines.append('<div class="table-wrap"><table class="key-formulas">')
            for r_idx, row in enumerate(table_rows):
                cells = [c.strip() for c in row.strip('|').split('|')]
                tag = 'th' if r_idx == 0 else 'td'
                html_lines.append('<tr>' + ''.join(f'<{tag}>{c}</{tag}>' for c in cells) + '</tr>')
            html_lines.append('</table></div>')
            table_rows = []
            in_table = False

    def flush_blockquote():
        nonlocal in_blockquote
        if in_blockquote:
            html_lines.append('</blockquote>')
            in_blockquote = False

    def inline(s: str) -> str:
        s = re.sub(r'\*\*\*(.+?)\*\*\*', r'<strong><em>\1</em></strong>', s)
        s = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', s)
        s = re.sub(r'(?<!\*)\*(?!\*)([^*\n]+?)(?<!\*)\*(?!\*)', r'<em>\1</em>', s)
        s = re.sub(r'`([^`]+)`', r'<code>\1</code>', s)
        s = re.sub(r'~~(.+?)~~', r'<del>\1</del>', s)
        # Difficulty emojis → styled spans
        s = s.replace('🟢 Easy', '<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold difficulty-easy">🟢 Easy</span>')
        s = s.replace('🟡 Medium', '<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold difficulty-medium">🟡 Medium</span>')
        s = s.replace('🔴 Hard', '<span class="inline-flex items-center gap-1 px-2 py-0.5 rounded-full text-xs font-semibold difficulty-hard">🔴 Hard</span>')
        return s

    i = 0
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped in ('---', '***', '___'):
            flush_list(); flush_table(); flush_blockquote()
            html_lines.append('<hr/>')
            i += 1; continue

        # Headings with numbering
        h_match = re.match(r'^(#{1,6})\s+(.+)$', stripped)
        if h_match:
            flush_list(); flush_table(); flush_blockquote()
            level = len(h_match.group(1))
            heading_text = inline(h_match.group(2).strip())
            html_lines.append(f'<h{level}>{heading_text}</h{level}>')
            i += 1; continue

        # Table rows
        if stripped.startswith('|') and stripped.endswith('|'):
            flush_list(); flush_blockquote()
            if re.match(r'^\|[\s\-:|]+\|$', stripped):
                i += 1; continue
            in_table = True
            table_rows.append(stripped)
            i += 1; continue
        else:
            flush_table()

        # Blockquote
        if stripped.startswith('> '):
            flush_list()
            content = stripped[2:]
            if not in_blockquote:
                html_lines.append('<blockquote>')
                in_blockquote = True
            html_lines.append(f'<p>{inline(content)}</p>')
            i += 1; continue
        else:
            flush_blockquote()

        # Unordered list
        li_match = re.match(r'^[-*+]\s+(.+)$', stripped)
        if li_match:
            if in_ol:
                html_lines.append('</ol>'); in_ol = False
            if not in_ul:
                html_lines.append('<ul>')
                in_ul = True
            html_lines.append(f'<li>{inline(li_match.group(1))}</li>')
            i += 1; continue

        # Ordered list
        nli_match = re.match(r'^(\d+)\.\s+(.+)$', stripped)
        if nli_match:
            if in_ul:
                html_lines.append('</ul>'); in_ul = False
            if not in_ol:
                html_lines.append('<ol>')
                in_ol = True
            html_lines.append(f'<li>{inline(nli_match.group(2))}</li>')
            i += 1; continue

        if not stripped:
            flush_list()
            i += 1; continue

        flush_list()
        html_lines.append(f'<p>{inline(stripped)}</p>')
        i += 1

    flush_list(); flush_table(); flush_blockquote()
    html = '\n'.join(html_lines)

    # ── Step 3: Restore LaTeX placeholders ──────────────────────────
    for idx, block in enumerate(latex_blocks):
        if block.startswith('$$'):
            html = html.replace(
                f"LATEXBLOCK{idx}LATEXEND",
                f'<span class="math-display">{block}</span>'
            )
        else:
            html = html.replace(f"LATEXBLOCK{idx}LATEXEND", block)

    # ── Step 4: Convert Related Topics links to page links ──────────
    # Pattern: [1.7 Universal Set] → link to the topic page
    def replace_topic_link(m):
        full_text = m.group(1)
        num_match = re.match(r'^(\d+\.\d+(?:\.\d+)?)', full_text)
        if num_match:
            topic_num = num_match.group(1)
            topic_id = topic_num_to_id.get(topic_num)
            if topic_id:
                href = f"/grade/{grade}/{subject}/chapter/{chapter}/topic/TOPICID_{topic_id}"
                return f'<a href="{href}" class="related-link">{full_text}</a>'
        return f'<span class="related-ref">{full_text}</span>'

    html = re.sub(r'\[(\d+\.\d+(?:\.\d+)?[^\]]*)\]', replace_topic_link, html)

    # Also match bold-wrapped related topics: **1.2 Topic Name** → link
    # This catches LLM output that uses bold instead of square brackets
    def replace_bold_topic_link(m):
        full_text = m.group(1)
        num_match = re.match(r'^(\d+\.\d+(?:\.\d+)?)', full_text)
        if num_match:
            topic_num = num_match.group(1)
            topic_id = topic_num_to_id.get(topic_num)
            if topic_id:
                href = f"/grade/{grade}/{subject}/chapter/{chapter}/topic/TOPICID_{topic_id}"
                return f'<a href="{href}" class="related-link">{full_text}</a>'
        return f'<strong>{full_text}</strong>'

    # Only apply in Related Topics section to avoid false positives
    related_section_match = re.search(r'(<h2[^>]*>.*?Related\s+Topics.*?</h2>)(.*?)(?=<h2|$)', html, re.DOTALL | re.IGNORECASE)
    if related_section_match:
        section_html = related_section_match.group(2)
        updated_section = re.sub(r'<strong>(\d+\.\d+(?:\.\d+)?[^<]*)</strong>', replace_bold_topic_link, section_html)
        html = html[:related_section_match.start(2)] + updated_section + html[related_section_match.end(2):]

    return html


def _reorder_practice_problems(text: str) -> str:
    """Reorder practice problems so Easy comes first, then Medium, then Hard."""
    # Find the Practice Problems section
    pp_match = re.search(
        r'(## Practice Problems\s*\n)(.*?)(?=\n## |\Z)',
        text, re.DOTALL
    )
    if not pp_match:
        return text

    header = pp_match.group(1)
    body = pp_match.group(2)

    # Split into individual problems (each starts with a numbered item or bold marker)
    problems = re.split(r'(?=\n\d+\.\s+\*\*|\n\*\*(?:Problem|Question)\s+\d)', body)

    easy, medium, hard, other = [], [], [], []
    for p in problems:
        p_stripped = p.strip()
        if not p_stripped:
            continue
        if '🟢' in p or 'Easy' in p.split('\n')[0]:
            easy.append(p)
        elif '🟡' in p or 'Medium' in p.split('\n')[0]:
            medium.append(p)
        elif '🔴' in p or 'Hard' in p.split('\n')[0]:
            hard.append(p)
        else:
            other.append(p)

    if not (easy or medium or hard):
        return text

    reordered = '\n'.join(easy + medium + hard + other)
    return text[:pp_match.start()] + header + reordered + text[pp_match.end():]


def extract_summary(md_text: str) -> str:
    m = re.search(r'## Introduction\s*\n+(.+?)(?=\n##|\n---|\Z)', md_text, re.DOTALL)
    if m:
        text = re.sub(r'\*\*(.+?)\*\*', r'\1', m.group(1))
        text = re.sub(r'\$[^\$\n]+?\$', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text[:400]
    for line in md_text.split('\n'):
        line = line.strip()
        if line and not line.startswith('#') and not line.startswith('>') and not line.startswith('-'):
            return line[:400]
    return ''


def strip_html_tags(html: str) -> str:
    """Strip HTML tags to create searchable plain text."""
    text = re.sub(r'<[^>]+>', ' ', html)
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def convert(output_dir: Path, dest_json: Path):
    """Convert a model output directory to en.json."""
    index_file = output_dir / '_index.json'
    if not index_file.exists():
        raise FileNotFoundError(f"No _index.json found in {output_dir}")

    with open(index_file, encoding='utf-8') as f:
        index = json.load(f)

    model = index.get('model', 'unknown')
    grade = index.get('grade', 11)
    chapter_num = index.get('chapter_number', 1)
    chapter_title = index.get('chapter_title', f'Chapter {chapter_num}')
    subject = index.get('subject', 'maths')
    topics_meta = index.get('topics', [])

    topic_num_to_id = {t['topic_number']: i + 1 for i, t in enumerate(topics_meta)}

    topics_html = []
    chapter_summary = ''

    # Read LLM-generated chapter intro if available
    intro_file = output_dir / '_chapter_intro.txt'
    if intro_file.exists():
        chapter_summary = intro_file.read_text(encoding='utf-8').strip()
        print(f"  📖 Using chapter intro from _chapter_intro.txt ({len(chapter_summary)} chars)")

    for i, meta in enumerate(topics_meta):
        md_file = output_dir / meta['file']
        if not md_file.exists():
            print(f"  ⚠  Missing file: {meta['file']}, skipping")
            continue

        md_text = md_file.read_text(encoding='utf-8')

        # Strip the top-level # heading and metadata line
        md_text = re.sub(r'^#\s+.+\n', '', md_text, count=1)
        md_text = re.sub(r'^>\s+\*\*Grade.+\n', '', md_text, flags=re.MULTILINE)

        # Reorder practice problems
        md_text = _reorder_practice_problems(md_text)

        html = md_to_html(md_text, topic_num_to_id, grade, subject, chapter_num)
        search_text = strip_html_tags(html)

        if i == 0 and not chapter_summary:
            chapter_summary = extract_summary(md_text)  # fallback if no _chapter_intro.txt

        topics_html.append({
            'id': i + 1,
            'title': meta['topic_title'],
            'topicNumber': meta['topic_number'],
            'importance': meta.get('importance', 3),
            'content': html,
            'searchText': search_text,
            'subtopics': [],
        })

        print(f"  [{i+1}/{len(topics_meta)}] {meta['topic_number']} {meta['topic_title']}"
              f" ({len(html)} chars HTML)")

    output = {
        'title': f'Chapter {chapter_num}: {chapter_title}',
        'subject': subject.capitalize() if subject == 'maths' else subject.title(),
        'grade': grade,
        'chapter': chapter_num,
        'language': 'en',
        'status': 'ready',
        'model': model,
        'source_dir': str(output_dir.name),
        'summary': chapter_summary,
        'topics': topics_html,
    }

    dest_json.parent.mkdir(parents=True, exist_ok=True)
    with open(dest_json, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"\n✅  Written to {dest_json}")
    print(f"   Model : {model}")
    print(f"   Topics: {len(topics_html)}")
    total_html = sum(len(t['content']) for t in topics_html)
    print(f"   Total HTML chars: {total_html:,}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/md_to_json.py <output_dir>")
        print("  e.g. python scripts/md_to_json.py output/qwen3_v2/")
        print("  e.g. python scripts/md_to_json.py data/output/grade11/maths/chapter1/")
        sys.exit(1)

    output_dir = ROOT / sys.argv[1].rstrip('/')
    if not output_dir.exists():
        print(f"Error: directory not found: {output_dir}")
        sys.exit(1)

    with open(output_dir / '_index.json', encoding='utf-8') as f:
        idx = json.load(f)
    grade = idx.get('grade', 11)
    chapter = idx.get('chapter_number', 1)
    subject = idx.get('subject', 'maths')

    dest = ROOT / 'data' / 'generated' / f'grade{grade}' / subject / f'chapter{chapter}' / 'en.json'

    print(f"Converting: {output_dir.name}  →  {dest.relative_to(ROOT)}")
    print(f"Topics: {len(idx.get('topics', []))}\n")

    convert(output_dir, dest)


if __name__ == '__main__':
    main()
