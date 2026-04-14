"""
translate_uploader.py — Convert translated markdown files and upload to MongoDB.

After running translate_grade9.py, this script:
1. Reads the translated .md files
2. Converts them to HTML using md_to_json logic
3. Updates MongoDB topics with translations: { hi: { content: "..." } }

Usage:
    python scripts/translate_uploader.py data/output/grade9/maths/chapter1/sarvam-api/hi
"""

import json
import os
import re
import sys
from pathlib import Path

try:
    from pymongo import MongoClient, UpdateOne
except ImportError:
    print("pymongo not installed. Run: pip install pymongo[srv]")
    sys.exit(1)

ROOT = Path(__file__).parent.parent

# Import conversion logic from md_to_json
sys.path.insert(0, str(ROOT / "scripts"))
from md_to_json import convert_md_to_html


def get_mongo_uri():
    uri = os.environ.get('MONGODB_URI')
    if uri:
        return uri
    env_file = ROOT / 'webapp' / '.env.local'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith('MONGODB_URI='):
                return line.split('=', 1)[1].strip()
    raise RuntimeError("No MONGODB_URI found")


def upload_translations(translated_dir: Path, lang_code: str):
    """Upload translated content to MongoDB as topic translations."""
    uri = get_mongo_uri()
    client = MongoClient(uri)
    db = client['btp-1']

    # Determine grade, subject, chapter from path
    # Expected: data/output/grade9/maths/chapter1/sarvam-api/hi/
    parts = translated_dir.parts
    grade_str = [p for p in parts if p.startswith('grade')][0]
    grade = int(re.search(r'\d+', grade_str).group())

    subject = 'maths'
    for p in parts:
        if p in ('maths', 'science', 'physics', 'chemistry', 'biology'):
            subject = p
            break

    ch_str = [p for p in parts if p.startswith('chapter')][0]
    chapter = int(re.search(r'\d+', ch_str).group())

    print(f"\nUploading translations: Grade {grade} {subject} Ch {chapter} [{lang_code}]")

    # Get existing topics from DB
    topics_in_db = list(db.topics.find(
        {'grade': grade, 'subject': subject, 'chapter': chapter},
        {'_id': 1, 'order': 1, 'topicNumber': 1, 'title': 1, 'content': 1}
    ).sort('order', 1))

    if not topics_in_db:
        print("  ERROR: No topics found in DB for this chapter")
        return

    # Build topic number to DB ID map
    topic_num_to_dbid = {t['topicNumber']: t['_id'] for t in topics_in_db}
    order_to_id = {t['order']: str(t['_id']) for t in topics_in_db}

    # Also read the English _index.json to get topic number mapping
    # Go up from translated_dir to the chapter dir
    chapter_dir = translated_dir.parent.parent  # up from sarvam-api/hi/ to chapter1/
    index_file = chapter_dir / "_index.json"
    topic_num_to_order = {}
    if index_file.exists():
        index = json.load(open(index_file, encoding='utf-8'))
        for i, t in enumerate(index.get('topics', []), 1):
            topic_num_to_order[t['number']] = i

    # Read translated .md files
    md_files = sorted(translated_dir.glob("*.md"))
    if not md_files:
        print("  No .md files found")
        return

    print(f"  Found {len(md_files)} translated files")

    # Also check for translated chapter intro
    intro_file = translated_dir / "_chapter_intro.txt"
    if intro_file.exists():
        translated_intro = intro_file.read_text(encoding='utf-8').strip()
        # Update chapter with translated summary
        db.chapters.update_one(
            {'grade': grade, 'subject': subject, 'chapter': chapter},
            {'$set': {f'translations.{lang_code}.summary': translated_intro}}
        )
        print(f"  Updated chapter summary translation")

    ops = []
    for md_file in md_files:
        # Extract topic number from filename (e.g., "1.1_Introduction.md" -> "1.1")
        topic_num_match = re.match(r'^(\d+\.\d+(?:\.\d+)?)', md_file.stem)
        if not topic_num_match:
            print(f"  Skipping {md_file.name} (no topic number)")
            continue

        topic_num = topic_num_match.group(1)
        db_id = topic_num_to_dbid.get(topic_num)
        if not db_id:
            print(f"  Skipping {md_file.name} (topic {topic_num} not in DB)")
            continue

        # Read and convert markdown to HTML
        md_content = md_file.read_text(encoding='utf-8')

        # Simple markdown to HTML conversion (reuse existing logic)
        html_content = simple_md_to_html(md_content)

        # Replace TOPICID placeholders
        for order, real_id in order_to_id.items():
            html_content = html_content.replace(f"TOPICID_{order}", real_id)

        ops.append(UpdateOne(
            {'_id': db_id},
            {'$set': {f'translations.{lang_code}.content': html_content}}
        ))
        print(f"  {topic_num}: {len(html_content)} chars HTML")

    if ops:
        result = db.topics.bulk_write(ops)
        print(f"\n  Updated {result.modified_count} topics with {lang_code} translations")

    client.close()


def simple_md_to_html(md_text: str) -> str:
    """Convert markdown to HTML, preserving LaTeX."""
    import markdown

    # Protect LaTeX blocks
    latex_blocks = []

    def protect_latex(m):
        idx = len(latex_blocks)
        latex_blocks.append(m.group(0))
        return f"LATEXBLOCK{idx}LATEXEND"

    text = re.sub(r'\$\$[^$]+\$\$', protect_latex, md_text)
    text = re.sub(r'\$[^$]+\$', protect_latex, text)

    # Convert markdown to HTML
    html = markdown.markdown(text, extensions=['tables', 'fenced_code'])

    # Restore LaTeX
    for idx, block in enumerate(latex_blocks):
        if block.startswith('$$'):
            html = html.replace(
                f"LATEXBLOCK{idx}LATEXEND",
                f'<span class="math-display">{block}</span>'
            )
        else:
            html = html.replace(f"LATEXBLOCK{idx}LATEXEND", block)

    return html


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scripts/translate_uploader.py <translated_dir> [lang_code]")
        print("Example: python scripts/translate_uploader.py data/output/grade9/maths/chapter1/sarvam-api/hi")
        sys.exit(1)

    translated_dir = Path(sys.argv[1])
    if not translated_dir.exists():
        print(f"ERROR: Directory not found: {translated_dir}")
        sys.exit(1)

    # Infer language code from directory name
    lang_code = translated_dir.name  # e.g., "hi"
    if len(sys.argv) > 2:
        lang_code = sys.argv[2]

    upload_translations(translated_dir, lang_code)
