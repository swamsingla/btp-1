"""
Maths Chunker — 1 topic = 1 chunk
══════════════════════════════════
Reads heading JSONs + PDFs, extracts text between consecutive headings.
Each chunk = all text from one topic heading to the next.

Output: data/intermediate/chunks/grade{N}/maths/chapter{M}/{num}_{title}.json
"""
import fitz
import json
import re
import os
from pathlib import Path
from typing import List, Dict, Tuple, Optional


def _flatten_headings(topics: List[Dict], result: List[Dict] = None) -> List[Dict]:
    """Flatten nested topics into a flat list ordered by page/number."""
    if result is None:
        result = []
    for t in topics:
        result.append({
            "number": t["number"],
            "title": t["title"],
            "page": t["page"],
        })
        if t.get("subtopics"):
            _flatten_headings(t["subtopics"], result)
    return result


def _find_heading_in_page(page, heading_number: str) -> Optional[float]:
    """Find the y-position of a heading number in a page.
    Returns the y-coordinate or None if not found."""
    blocks = page.get_text("dict")["blocks"]
    # Look for the heading number pattern (e.g., "1.1", "3.3.1")
    pattern = re.compile(r'(?:^|\s)' + re.escape(heading_number) + r'(?:\s|$)')
    
    for block in blocks:
        if "lines" not in block:
            continue
        for line in block["lines"]:
            for span in line["spans"]:
                text = span["text"].strip()
                sz = span["size"]
                bold = bool(span["flags"] & (1 << 4))
                # Heading spans are typically bold and >= 10.5pt
                if (bold and sz >= 10.5) or sz >= 14:
                    if text.startswith(heading_number) or pattern.search(text):
                        return span["origin"][1]  # y-position
    return None


def _extract_text_from_range(doc, start_page: int, start_y: Optional[float],
                              end_page: int, end_y: Optional[float]) -> str:
    """Extract text from a page/y range in the PDF.
    Pages are 0-indexed internally."""
    text_parts = []
    
    for pg_num in range(start_page, min(end_page + 1, len(doc))):
        page = doc[pg_num]
        blocks = page.get_text("dict")["blocks"]
        
        for block in blocks:
            if "lines" not in block:
                continue
            for line in block["lines"]:
                line_y = line["bbox"][1]  # top y of line
                
                # Skip lines before start_y on start page
                if pg_num == start_page and start_y is not None:
                    if line_y < start_y - 2:  # small tolerance
                        continue
                
                # Skip lines after end_y on end page
                if pg_num == end_page and end_y is not None:
                    if line_y >= end_y - 2:
                        continue
                
                line_text = "".join(span["text"] for span in line["spans"]).strip()
                if line_text:
                    text_parts.append(line_text)
    
    return "\n".join(text_parts)


def _clean_chunk_text(text: str, heading_number: str, heading_title: str) -> str:
    """Clean extracted text: remove heading line itself, page numbers,
    headers/footers, exercise prompts, etc."""
    lines = text.split("\n")
    cleaned = []
    
    # Skip patterns
    skip_patterns = [
        re.compile(r'^\d+$'),  # bare page numbers
        re.compile(r'^©\s*NCERT', re.I),  # copyright
        re.compile(r'^not\s+to\s+be\s+republished', re.I),
        re.compile(r'^Free\s+Distribution', re.I),
        re.compile(r'^MATHEMATICS$', re.I),  # header
        re.compile(r'^NCERT$', re.I),
        re.compile(r'^Textbook', re.I),
        re.compile(r'^Rationalised\s+\d', re.I),
    ]
    
    for i, line in enumerate(lines):
        line_stripped = line.strip()
        if not line_stripped:
            continue
        
        # Skip the heading line itself (first occurrence)
        if i < 3 and heading_number in line_stripped and heading_title[:20] in line_stripped:
            continue
        
        # Skip matching patterns
        if any(p.match(line_stripped) for p in skip_patterns):
            continue
        
        cleaned.append(line_stripped)
    
    return "\n".join(cleaned)


def chunk_chapter(pdf_path: str, headings_json: Dict) -> List[Dict]:
    """Chunk a chapter PDF into topic-level chunks.
    
    Args:
        pdf_path: Path to the PDF file
        headings_json: Parsed heading JSON with chapter_number, chapter_title, topics
    
    Returns:
        List of chunk dicts with topic info and extracted content
    """
    doc = fitz.open(pdf_path)
    
    # Flatten all headings
    flat_headings = _flatten_headings(headings_json["topics"])
    
    if not flat_headings:
        doc.close()
        return []
    
    # Find precise y-positions for each heading
    for h in flat_headings:
        pg = h["page"] - 1  # Convert to 0-indexed
        if 0 <= pg < len(doc):
            y = _find_heading_in_page(doc[pg], h["number"])
            h["y"] = y
            h["page_0idx"] = pg
        else:
            h["y"] = None
            h["page_0idx"] = max(0, min(pg, len(doc) - 1))
    
    chunks = []
    
    for i, heading in enumerate(flat_headings):
        # Skip "Summary" topics — they don't contain learning content
        if heading["title"].lower().strip() in ("summary",):
            continue
        
        start_page = heading["page_0idx"]
        start_y = heading["y"]
        
        # End = start of next heading (or end of doc)
        if i + 1 < len(flat_headings):
            end_page = flat_headings[i + 1]["page_0idx"]
            end_y = flat_headings[i + 1]["y"]
        else:
            end_page = len(doc) - 1
            end_y = None
        
        # Extract text
        raw_text = _extract_text_from_range(doc, start_page, start_y,
                                             end_page, end_y)
        
        # Clean text
        content = _clean_chunk_text(raw_text, heading["number"], heading["title"])
        
        # Determine if this is a subtopic (has 3+ dots: e.g., "1.2.1")
        depth = len(heading["number"].split("."))
        
        chunk = {
            "grade": None,  # filled by caller
            "subject": "maths",
            "chapter_number": headings_json["chapter_number"],
            "chapter_title": headings_json["chapter_title"],
            "topic_number": heading["number"],
            "topic_title": heading["title"],
            "depth": depth,  # 2 = topic (e.g., 1.1), 3 = subtopic (e.g., 1.1.1)
            "page_start": heading["page"],
            "content": content,
            "content_length": len(content),
        }
        chunks.append(chunk)
    
    doc.close()
    return chunks


def process_all(input_dir: str, headings_dir: str, output_dir: str):
    """Process all maths PDFs: read headings, chunk text, save."""
    input_base = Path(input_dir)
    headings_base = Path(headings_dir)
    output_base = Path(output_dir)
    
    total_chunks = 0
    total_files = 0
    
    for grade_dir in sorted(input_base.iterdir()):
        if not grade_dir.is_dir() or not grade_dir.name.startswith("grade"):
            continue
        
        grade_num = int(re.search(r'\d+', grade_dir.name).group())
        maths_dir = grade_dir / "maths"
        if not maths_dir.exists():
            continue
        
        # Find all PDF directories (direct or part1/part2)
        pdf_dirs = []
        if any(d.name.startswith("part") for d in maths_dir.iterdir() if d.is_dir()):
            for pd in sorted(maths_dir.iterdir()):
                if pd.is_dir() and pd.name.startswith("part"):
                    pdf_dirs.append(pd)
        else:
            pdf_dirs.append(maths_dir)
        
        for pdir in pdf_dirs:
            for pdf_file in sorted(pdir.glob("chapter*.pdf")):
                # Find corresponding heading JSON
                rel = pdf_file.relative_to(input_base)
                json_path = headings_base / rel.with_suffix(".json")
                
                if not json_path.exists():
                    print(f"  SKIP {rel} (no heading JSON)")
                    continue
                
                with open(json_path, "r", encoding="utf-8") as f:
                    headings = json.load(f)
                
                # Chunk
                chunks = chunk_chapter(str(pdf_file), headings)
                
                # Fill in grade
                for c in chunks:
                    c["grade"] = grade_num
                
                # Save individual chunk files
                ch_num = headings.get("chapter_number", "0")
                ch_dir = output_base / f"grade{grade_num}" / "maths"
                # Add part subdirectory if applicable
                if pdir.name.startswith("part"):
                    ch_dir = ch_dir / pdir.name
                ch_dir = ch_dir / f"chapter{ch_num}"
                ch_dir.mkdir(parents=True, exist_ok=True)
                
                for chunk in chunks:
                    # Filename: topic_number_title.json
                    safe_title = re.sub(r'[^\w\s-]', '', chunk["topic_title"])
                    safe_title = re.sub(r'\s+', '_', safe_title)[:50]
                    fname = f"{chunk['topic_number']}_{safe_title}.json"
                    
                    out_path = ch_dir / fname
                    with open(out_path, "w", encoding="utf-8") as f:
                        json.dump(chunk, f, indent=2, ensure_ascii=False)
                
                # Also save full chapter chunks file
                chapter_out = ch_dir / "_all_chunks.json"
                with open(chapter_out, "w", encoding="utf-8") as f:
                    json.dump({
                        "grade": grade_num,
                        "subject": "maths",
                        "chapter_number": headings.get("chapter_number"),
                        "chapter_title": headings.get("chapter_title"),
                        "total_chunks": len(chunks),
                        "chunks": chunks,
                    }, f, indent=2, ensure_ascii=False)
                
                total_chunks += len(chunks)
                total_files += 1
                print(f"  OK  {rel}: {len(chunks)} chunks")
    
    print(f"\nDone: {total_files} PDFs → {total_chunks} chunks")


if __name__ == "__main__":
    import sys
    
    base = Path(__file__).parent.parent
    input_dir = base / "data" / "input"
    headings_dir = base / "data" / "intermediate" / "headings"
    output_dir = base / "data" / "intermediate" / "chunks"
    
    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Test on one chapter
        pdf = input_dir / "grade10" / "maths" / "chapter1.pdf"
        json_path = headings_dir / "grade10" / "maths" / "chapter1.json"
        
        with open(json_path, "r", encoding="utf-8") as f:
            headings = json.load(f)
        
        chunks = chunk_chapter(str(pdf), headings)
        for c in chunks:
            c["grade"] = 10
        
        print(f"Chapter: {headings['chapter_title']}")
        print(f"Chunks: {len(chunks)}")
        for c in chunks:
            preview = c["content"][:150].replace("\n", " ")
            print(f"\n  [{c['topic_number']}] {c['topic_title']} "
                  f"({c['content_length']} chars)")
            print(f"    Preview: {preview}...")
    else:
        process_all(str(input_dir), str(headings_dir), str(output_dir))
