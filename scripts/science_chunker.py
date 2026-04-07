"""
Science Chunker — 1 topic = 1 chunk (using manually-provided headings)
══════════════════════════════════════════════════════════════════════
Unlike maths, science books lack consistent heading formatting.
Headings are provided via topics.txt files (one per chapter).

Reads topics.txt + PDFs, finds heading text in the PDF, extracts text
between consecutive headings to form chunks.

Output: data/intermediate/chunks/grade{N}/science/chapter{M}/{num}_{title}.json
        (identical format to maths chunker)

topics.txt format:
    Chapter name: <chapter title>
    5.1 How do we Measure?
    5.2 Standard Units
    ...
"""
import fitz
import json
import re
import os
from pathlib import Path
from typing import List, Dict, Tuple, Optional


# ═══════════ TOPICS.TXT PARSER ═══════════

def parse_topics_file(topics_path: str) -> Dict:
    """Parse a topics.txt file into chapter info + flat heading list.

    Returns:
        {
            "chapter_title": "...",
            "chapter_number": "5",
            "topics": [
                {"number": "5.1", "title": "How do we Measure?"},
                {"number": "5.2", "title": "Standard Units"},
                ...
            ]
        }
    """
    with open(topics_path, "r", encoding="utf-8") as f:
        lines = [l.strip() for l in f if l.strip()]

    chapter_title = None
    chapter_number = None
    topics = []

    heading_re = re.compile(r'^(\d+\.\d+(?:\.\d+)*)\s+(.+)$')

    for line in lines:
        # Check for chapter name line
        if line.lower().startswith("chapter name:"):
            chapter_title = line.split(":", 1)[1].strip()
            continue

        # Check for heading line (e.g., "5.1 How do we Measure?")
        m = heading_re.match(line)
        if m:
            number = m.group(1)
            title = m.group(2).strip()
            topics.append({"number": number, "title": title})

            # Extract chapter number from first heading
            if chapter_number is None:
                chapter_number = number.split(".")[0]

    return {
        "chapter_title": chapter_title or "Unknown",
        "chapter_number": chapter_number or "0",
        "topics": topics,
    }


# ═══════════ PDF TEXT EXTRACTION ═══════════

def _extract_full_text(doc) -> List[Dict]:
    """Extract text from all pages with page/y-position info.

    Returns a list of dicts:
        [{"text": "...", "page": 0, "y": 123.4}, ...]
    One entry per text line.
    """
    all_lines = []
    for pg_num in range(len(doc)):
        page = doc[pg_num]
        blocks = page.get_text("dict")["blocks"]
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_text = "".join(span["text"] for span in line["spans"]).strip()
                if line_text:
                    all_lines.append({
                        "text": line_text,
                        "page": pg_num,
                        "y": line["bbox"][1],  # top y of line
                    })
    return all_lines


def _find_heading_position(all_lines: List[Dict], heading_title: str,
                            heading_number: str) -> Optional[Dict]:
    """Find the position of a heading in the extracted text.

    Tries multiple matching strategies:
    1. Exact match of "<number> <title>" in a line
    2. Number + partial title match
    3. Title substring match (fuzzy)
    """
    # Normalize for comparison
    title_lower = heading_title.lower().strip()
    number = heading_number.strip()

    # Strategy 0: Unnumbered headings (e.g., "Summary" with a fake number like "5.8")
    # If the title is a common standalone heading, search for it directly
    is_unnumbered = title_lower in ("summary", "keywords", "exercises",
                                     "let us enhance our learning", "learning further")
    if is_unnumbered:
        for line_info in all_lines:
            text = line_info["text"].strip().lower()
            if text == title_lower or text.startswith(title_lower):
                return line_info

    # Strategy 1: Look for the heading number + title in a single line
    full_heading = f"{number} {heading_title}"
    for line_info in all_lines:
        text = line_info["text"].strip()
        # Exact or near-exact match
        if text.lower().startswith(full_heading.lower()):
            return line_info
        # Number at start + title contained
        if text.startswith(number) and title_lower[:20] in text.lower():
            return line_info

    # Strategy 2: Just the number at the start with something after
    for line_info in all_lines:
        text = line_info["text"].strip()
        if re.match(r'^' + re.escape(number) + r'\s', text):
            # Check if any significant words from the title appear
            title_words = [w.lower() for w in heading_title.split() if len(w) >= 3]
            text_lower = text.lower()
            matches = sum(1 for w in title_words if w in text_lower)
            if matches >= min(2, len(title_words)):
                return line_info

    # Strategy 3: Title substring match (for cases where number might
    # be formatted differently)
    # Use first few significant words
    title_words = [w for w in heading_title.split() if len(w) >= 3]
    search_phrase = " ".join(title_words[:4]).lower()
    if len(search_phrase) >= 8:
        for line_info in all_lines:
            if search_phrase in line_info["text"].lower():
                return line_info

    return None


# ═══════════ TEXT EXTRACTION BETWEEN POSITIONS ═══════════

def _extract_text_between(all_lines: List[Dict],
                           start_page: int, start_y: float,
                           end_page: Optional[int], end_y: Optional[float]) -> str:
    """Extract all text lines between two positions."""
    text_parts = []
    collecting = False

    for line_info in all_lines:
        pg = line_info["page"]
        y = line_info["y"]

        # Start collecting at start position
        if pg == start_page and abs(y - start_y) < 2:
            collecting = True
            continue  # Skip the heading line itself

        if pg > start_page and not collecting:
            collecting = True

        if not collecting:
            continue

        # Stop at end position
        if end_page is not None and end_y is not None:
            if pg > end_page:
                break
            if pg == end_page and y >= end_y - 2:
                break

        text_parts.append(line_info["text"])

    return "\n".join(text_parts)


# ═══════════ TEXT CLEANING ═══════════

def _clean_chunk_text(text: str, heading_number: str, heading_title: str) -> str:
    """Clean extracted text: remove page numbers, headers/footers,
    copyright notices, etc."""
    lines = text.split("\n")
    cleaned = []

    # Skip patterns
    skip_patterns = [
        re.compile(r'^\d+$'),                              # bare page numbers
        re.compile(r'^©\s*NCERT', re.I),                   # copyright
        re.compile(r'^not\s+to\s+be\s+republished', re.I),
        re.compile(r'^Free\s+Distribution', re.I),
        re.compile(r'^SCIENCE$', re.I),                    # header
        re.compile(r'^NCERT$', re.I),
        re.compile(r'^Textbook', re.I),
        re.compile(r'^Rationalised\s+\d', re.I),
        re.compile(r'^Reprint\s+\d', re.I),                # reprint notices
        re.compile(r'^Curiosity\s*$', re.I),               # common science headers
        re.compile(r'^Ponder\s*$', re.I),
        re.compile(r'^Probe\s*$', re.I),
    ]

    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue

        # Skip the heading line itself (first few lines)
        if i < 3 and heading_number in line_stripped and heading_title[:15] in line_stripped:
            continue

        # Skip matching patterns
        if any(p.match(line_stripped) for p in skip_patterns):
            continue

        cleaned.append(line_stripped)

    return "\n".join(cleaned)


# ═══════════ MAIN CHUNKING ═══════════

def chunk_chapter(pdf_path: str, topics_info: Dict) -> List[Dict]:
    """Chunk a science chapter PDF into topic-level chunks using
    heading positions from topics.txt.

    Args:
        pdf_path: Path to the chapter PDF
        topics_info: Parsed topics.txt dict with chapter_title, topics list

    Returns:
        List of chunk dicts (same format as maths chunker)
    """
    doc = fitz.open(pdf_path)
    topics = topics_info["topics"]

    if not topics:
        doc.close()
        return []

    # Extract all text lines with positions
    all_lines = _extract_full_text(doc)

    # Find positions of each heading
    heading_positions = []
    for topic in topics:
        pos = _find_heading_position(all_lines, topic["title"], topic["number"])
        heading_positions.append({
            "number": topic["number"],
            "title": topic["title"],
            "position": pos,
        })

    # Report any headings not found
    for hp in heading_positions:
        if hp["position"] is None:
            print(f"  WARNING: Could not find heading '{hp['number']} {hp['title']}' in PDF")

    chunks = []
    for i, hp in enumerate(heading_positions):
        if hp["position"] is None:
            continue

        start_page = hp["position"]["page"]
        start_y = hp["position"]["y"]

        # End = start of next heading (or end of document)
        end_page = None
        end_y = None
        for j in range(i + 1, len(heading_positions)):
            if heading_positions[j]["position"] is not None:
                end_page = heading_positions[j]["position"]["page"]
                end_y = heading_positions[j]["position"]["y"]
                break

        # Extract text between positions
        raw_text = _extract_text_between(all_lines, start_page, start_y,
                                          end_page, end_y)

        # Clean text
        content = _clean_chunk_text(raw_text, hp["number"], hp["title"])

        # Determine depth
        depth = len(hp["number"].split("."))

        chunk = {
            "grade": None,  # filled by caller
            "subject": "science",
            "chapter_number": topics_info["chapter_number"],
            "chapter_title": topics_info["chapter_title"],
            "topic_number": hp["number"],
            "topic_title": hp["title"],
            "depth": depth,
            "page_start": start_page + 1,  # 1-indexed for output
            "content": content,
            "content_length": len(content),
        }
        chunks.append(chunk)

    doc.close()
    return chunks


# ═══════════ BATCH PROCESSING ═══════════

def process_chapter(pdf_path: str, topics_path: str, output_dir: str,
                     grade: int):
    """Process a single science chapter: read topics.txt, chunk PDF, save."""
    # Parse topics
    topics_info = parse_topics_file(topics_path)

    # Chunk
    chunks = chunk_chapter(pdf_path, topics_info)

    # Fill in grade
    for c in chunks:
        c["grade"] = grade

    # Ensure chapter_number is an int if possible
    try:
        ch_num = int(topics_info["chapter_number"])
    except (ValueError, TypeError):
        ch_num = topics_info["chapter_number"]

    # Save individual chunk files
    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    for chunk in chunks:
        safe_title = re.sub(r'[^\w\s-]', '', chunk["topic_title"])
        safe_title = re.sub(r'\s+', '_', safe_title)[:50]
        fname = f"{chunk['topic_number']}_{safe_title}.json"

        out_path = out_dir / fname
        with open(out_path, "w", encoding="utf-8") as f:
            json.dump(chunk, f, indent=2, ensure_ascii=False)

    # Save full chapter chunks file
    chapter_out = out_dir / "_all_chunks.json"
    with open(chapter_out, "w", encoding="utf-8") as f:
        json.dump({
            "grade": grade,
            "subject": "science",
            "chapter_number": ch_num,
            "chapter_title": topics_info["chapter_title"],
            "total_chunks": len(chunks),
            "chunks": chunks,
        }, f, indent=2, ensure_ascii=False)

    print(f"  OK  {len(chunks)} chunks saved to {out_dir}")
    return chunks


def process_all():
    """Process all science chapters that have a topics.txt file."""
    base = Path(__file__).parent.parent
    input_dir = base / "data" / "input"
    chunks_dir = base / "data" / "intermediate" / "chunks"

    total_chunks = 0
    total_files = 0

    # Scan all grades for science chapters with topics.txt
    for grade_dir in sorted(input_dir.iterdir()):
        if not grade_dir.is_dir() or not grade_dir.name.startswith("grade"):
            continue

        grade_num = int(re.search(r'\d+', grade_dir.name).group())
        science_dir = grade_dir / "science"
        if not science_dir.exists():
            continue

        # Find all chapter PDFs
        for pdf_file in sorted(science_dir.glob("chapter*.pdf")):
            ch_match = re.search(r'chapter(\d+)', pdf_file.stem)
            if not ch_match:
                continue
            ch_num = ch_match.group(1)

            # Check if topics.txt exists for this chapter
            topics_dir = chunks_dir / f"grade{grade_num}" / "science" / f"chapter{ch_num}"
            topics_file = topics_dir / "topics.txt"

            if not topics_file.exists():
                print(f"  SKIP grade{grade_num}/science/chapter{ch_num} (no topics.txt)")
                continue

            print(f"\nProcessing grade{grade_num}/science/chapter{ch_num}...")

            output_dir = chunks_dir / f"grade{grade_num}" / "science" / f"chapter{ch_num}"
            chunks = process_chapter(
                str(pdf_file), str(topics_file), str(output_dir), grade_num
            )
            total_chunks += len(chunks)
            total_files += 1

    print(f"\nDone: {total_files} chapters → {total_chunks} chunks")


# ═══════════ CLI ═══════════

if __name__ == "__main__":
    import sys

    base = Path(__file__).parent.parent
    input_dir = base / "data" / "input"
    chunks_dir = base / "data" / "intermediate" / "chunks"

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Test on grade6 science chapter5
        pdf = input_dir / "grade6" / "science" / "chapter5.pdf"
        topics = chunks_dir / "grade6" / "science" / "chapter5" / "topics.txt"

        if not pdf.exists():
            print(f"PDF not found: {pdf}")
            sys.exit(1)
        if not topics.exists():
            print(f"topics.txt not found: {topics}")
            sys.exit(1)

        topics_info = parse_topics_file(str(topics))
        print(f"Chapter: {topics_info['chapter_title']}")
        print(f"Topics: {len(topics_info['topics'])}")
        for t in topics_info['topics']:
            print(f"  {t['number']} {t['title']}")

        chunks = chunk_chapter(str(pdf), topics_info)
        for c in chunks:
            c["grade"] = 6

        print(f"\nChunks: {len(chunks)}")
        for c in chunks:
            preview = c["content"][:150].replace("\n", " ")
            # Safely encode for terminal output
            preview = preview.encode("ascii", errors="replace").decode("ascii")
            print(f"\n  [{c['topic_number']}] {c['topic_title']} "
                  f"({c['content_length']} chars)")
            print(f"    Preview: {preview}...")

    elif len(sys.argv) > 2:
        # Process specific grade/chapter: python science_chunker.py 6 5
        grade = int(sys.argv[1])
        ch = int(sys.argv[2])

        pdf = input_dir / f"grade{grade}" / "science" / f"chapter{ch}.pdf"
        topics = chunks_dir / f"grade{grade}" / "science" / f"chapter{ch}" / "topics.txt"
        output = chunks_dir / f"grade{grade}" / "science" / f"chapter{ch}"

        if not pdf.exists():
            print(f"PDF not found: {pdf}")
            sys.exit(1)
        if not topics.exists():
            print(f"topics.txt not found: {topics}")
            sys.exit(1)

        process_chapter(str(pdf), str(topics), str(output), grade)

    else:
        process_all()
