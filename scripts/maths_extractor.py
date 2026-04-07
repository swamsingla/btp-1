"""
Maths PDF Headings Extractor v2
═══════════════════════════════
Handles ALL NCERT maths PDF formats (grades 6-12):
  - Grade 6:  ch# sz=39 no-bold, title sz=35 no-bold, section sz=17 bold
  - Grade 9:  ch# sz=16 bold, title sz=14 bold, section sz=12 bold  
  - Grade 10: ch# sz=60 bold, title sz=19.6+28(dropcap) bold, section sz=12 bold
  - Grade 11: ch# sz=28 bold, title sz=19-24 bold, section sz=12 bold
  - Grade 12: ch# sz=28 bold, title sz=20 bold, section sz=12 bold

Key fixes over v1:
  1. Multi-line title collection (drop-cap titles spanning 2 lines)
  2. Body text filtering within heading lines (stop at non-bold span)
  3. Decorative drop-cap note exclusion (non-bold large chars)
  4. Grade-adaptive thresholds for chapter info and sections
  5. Proper chapter number extraction for double-digit numbers
"""
import fitz
import re
import json
import os
from pathlib import Path
from typing import List, Dict, Optional, Tuple


class MathsHeadingsExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.chapter_number = None
        self.chapter_title = None

    def close(self):
        self.doc.close()

    # ═══════════ CHAPTER INFO ═══════════
    def _extract_chapter_info(self):
        """Extract chapter number and title from first 2 pages."""
        title_spans = []

        for page_num in range(min(2, len(self.doc))):
            page = self.doc[page_num]
            blocks = page.get_text("dict")["blocks"]

            for block in blocks:
                if "lines" not in block:
                    continue

                for line in block["lines"]:
                    for span in line["spans"]:
                        text = span["text"].strip()
                        if not text:
                            continue
                        sz = span["size"]
                        bold = bool(span["flags"] & (1 << 4))
                        y = span["origin"][1]

                        # ── Chapter number: large digit(s) ──
                        if not self.chapter_number and text.isdigit() and len(text) <= 2:
                            if sz >= 15:  # Works for all grades (16-60)
                                self.chapter_number = int(text)

                        # Also try "Chapter N" pattern
                        if not self.chapter_number:
                            m = re.match(r'^Chapter\s+(\d+)', text, re.I)
                            if m:
                                self.chapter_number = int(m.group(1))

                        # ── Collect potential title spans ──
                        # Must be: reasonably large, not a digit, not "Chapter"
                        if (sz >= 14 and len(text) > 2 and
                                not text.isdigit() and
                                not re.match(r'^Chapter\b', text, re.I) and
                                not re.match(r'^Unit\b', text, re.I) and
                                not re.match(r'^\d+\.\d+', text)):
                            # Skip known non-title content
                            skip_words = ['objective', 'probe', 'ponder',
                                          'after studying', 'you have learnt',
                                          'note', 'a note']
                            if any(w in text.lower() for w in skip_words):
                                continue
                            title_spans.append({
                                'text': text, 'size': sz, 'bold': bold,
                                'y': y, 'page': page_num
                            })

        # ── Find the chapter title from collected spans ──
        if not title_spans:
            return

        # Group title spans by size range (within 15pt of each other)
        # The title is typically the LARGEST bold text, or largest text overall
        # Sort by size descending
        title_spans.sort(key=lambda s: s['size'], reverse=True)

        # Find the title size group: largest (that isn't a lone decoration)
        # Strategy: find the most common "large" size that forms coherent text
        max_sz = title_spans[0]['size']

        # Collect all spans within a size band that could be title
        # For drop-cap: 28.0 and 19.6 are both title. Use wider tolerance.
        # The title group is spans with size >= max_sz * 0.6 (to catch 19.6 with 28.0)
        min_title_sz = max_sz * 0.65
        candidate_spans = [s for s in title_spans if s['size'] >= min_title_sz]

        # Filter: only from page 0 (title page)
        candidate_spans = [s for s in candidate_spans if s['page'] == 0]
        if not candidate_spans:
            candidate_spans = [s for s in title_spans if s['size'] >= min_title_sz]

        if not candidate_spans:
            return

        # Group by y-line (tolerance 5pt)
        y_groups = []
        for sp in sorted(candidate_spans, key=lambda s: s['y']):
            merged = False
            for grp in y_groups:
                if abs(sp['y'] - grp['y']) < 35:  # Wide tolerance for drop-cap offset
                    grp['spans'].append(sp)
                    merged = True
                    break
            if not merged:
                y_groups.append({'y': sp['y'], 'spans': [sp]})

        # The title group(s): find contiguous y-groups with title-sized text
        # Collect text from ALL spans in order
        title_parts = []
        for grp in sorted(y_groups, key=lambda g: g['y']):
            # Build text from this y-group, sorted by x
            # We need to get x positions too - re-extract
            line_text = " ".join(s['text'] for s in grp['spans'])
            if line_text and len(line_text) > 1:
                title_parts.append(line_text)

        if title_parts:
            self.chapter_title = " ".join(title_parts)
            # Clean up extra spaces
            self.chapter_title = re.sub(r'\s+', ' ', self.chapter_title).strip()

        # ── Validation: reject garbage titles ──
        if self.chapter_title:
            # If title is way too long, it's body text
            if len(self.chapter_title) > 60:
                self.chapter_title = None
            # If title contains sentence-like content, truncate
            elif '.' in self.chapter_title and len(self.chapter_title) > 40:
                self.chapter_title = self.chapter_title.split('.')[0].strip()

    def _extract_chapter_info_v2(self):
        """Improved: extract using x-position aware span grouping."""
        # First pass: get ALL spans from first 2 pages
        all_spans = []
        for page_num in range(min(2, len(self.doc))):
            page = self.doc[page_num]
            blocks = page.get_text("dict")["blocks"]
            for block in blocks:
                if "lines" not in block:
                    continue
                for line in block["lines"]:
                    for span in line["spans"]:
                        t = span["text"].strip()
                        if t:
                            all_spans.append({
                                'text': t,
                                'size': round(span["size"], 1),
                                'bold': bool(span["flags"] & (1 << 4)),
                                'x': round(span["origin"][0], 1),
                                'y': round(span["origin"][1], 1),
                                'page': page_num
                            })

        # ── Chapter number ──
        for sp in all_spans:
            if sp['text'].isdigit() and len(sp['text']) <= 2 and sp['size'] >= 15:
                if not self.chapter_number:
                    self.chapter_number = int(sp['text'])
                    break
        # Fallback: "Chapter N"
        if not self.chapter_number:
            for sp in all_spans:
                m = re.match(r'^Chapter\s+(\d+)', sp['text'], re.I)
                if m:
                    self.chapter_number = int(m.group(1))
                    break

        # ── Chapter title ──
        # Find the "title band": largest sized text that's not a digit and not "Chapter"
        skip_re = re.compile(
            r'^(Chapter|Unit|Objective|Probe|Ponder|After\s+studying|'
            r'You\s+have|Note|Appendix|\d+\.\d+)', re.I)

        title_candidates = []
        for sp in all_spans:
            if sp['page'] > 0 and title_candidates:
                break  # Don't look past page 0 if we found stuff
            t = sp['text']
            if (sp['size'] >= 14 and
                    not t.isdigit() and not skip_re.match(t)):
                # Allow single chars IF they're large (drop-cap)
                if len(t) <= 1 and sp['size'] < 20:
                    continue
                title_candidates.append(sp)

        if not title_candidates:
            return

        # Find max size
        max_sz = max(s['size'] for s in title_candidates)

        # Title band: spans >= 65% of max, on page 0
        pg0 = [s for s in title_candidates if s['page'] == 0 and s['size'] >= max_sz * 0.65]
        if not pg0:
            pg0 = [s for s in title_candidates if s['size'] >= max_sz * 0.65]
        if not pg0:
            return

        # Group into y-lines (tol=15 to keep drop-cap on same line
        # but separate actual multi-line titles)
        pg0.sort(key=lambda s: (s['y'], s['x']))
        lines = []
        cur_line = [pg0[0]]
        for sp in pg0[1:]:
            if abs(sp['y'] - cur_line[0]['y']) < 15:
                cur_line.append(sp)
            else:
                lines.append(cur_line)
                cur_line = [sp]
        lines.append(cur_line)

        # Build title text
        title_parts = []
        for line in lines:
            line.sort(key=lambda s: s['x'])
            # Join spans: handle drop-cap (single letter + UPPERCASE continuation)
            # Only merge when sizes differ (true drop-cap) to avoid
            # merging standalone "A" with next word like "PEEK"
            parts = []
            for i, sp in enumerate(line):
                t = sp['text']
                if i == 0:
                    parts.append(t)
                else:
                    prev_sp = line[i - 1]
                    prev = parts[-1]
                    # Drop-cap: single uppercase at LARGER size,
                    # followed by UPPERCASE rest at smaller size
                    sz_ratio = min(sp['size'], prev_sp['size']) / max(sp['size'], prev_sp['size'])
                    if (len(prev) == 1 and prev.isupper() and
                            t and t[0].isupper() and sz_ratio < 0.85):
                        parts[-1] = prev + t
                    else:
                        parts.append(t)
            line_text = " ".join(parts)
            if line_text.strip():
                title_parts.append(line_text.strip())

        if title_parts:
            self.chapter_title = " ".join(title_parts)
            self.chapter_title = re.sub(r'\s+', ' ', self.chapter_title).strip()

            # Safety: reject garbage
            if len(self.chapter_title) > 80:
                # Try just the first line
                self.chapter_title = title_parts[0] if title_parts else None
            if self.chapter_title and len(self.chapter_title) > 80:
                self.chapter_title = None

    # ═══════════ SECTION HEADINGS ═══════════
    def _extract_section_headings(self) -> List[Dict]:
        """Extract section headings. Handles:
        - Split spans: "10.1" + "Introduction" as separate spans
        - Body text on same line: stop collecting at non-bold/smaller span
        - Different size thresholds per grade
        """
        heading_re = re.compile(r'^(\d+\.\d+(?:\.\d+)*)\s+(.*)')
        all_headings = []

        for page_num in range(len(self.doc)):
            page = self.doc[page_num]
            blocks = page.get_text("dict")["blocks"]

            for block in blocks:
                if "lines" not in block:
                    continue

                for line in block["lines"]:
                    spans = line["spans"]
                    if not spans:
                        continue

                    # ── Build heading text: only from bold spans ──
                    # First, check if line starts with a heading number
                    first_text = spans[0]["text"].strip()
                    first_sz = spans[0]["size"]
                    first_bold = bool(spans[0]["flags"] & (1 << 4))

                    # Heading spans must be bold and at least a minimum size
                    # Grade 6 uses sz=17 bold, grades 9-12 use sz=11-12 bold
                    if first_sz < 10.5 or not first_bold:
                        continue

                    # ── Collect text only from BOLD spans of similar size ──
                    heading_text_parts = []
                    heading_max_sz = first_sz

                    for span in spans:
                        t = span["text"]
                        sz = span["size"]
                        bold = bool(span["flags"] & (1 << 4))

                        # Stop if: not bold, or size drops significantly
                        if not bold:
                            break
                        if sz < first_sz * 0.85:
                            break

                        heading_text_parts.append(t)
                        heading_max_sz = max(heading_max_sz, sz)

                    heading_text = "".join(heading_text_parts).strip()

                    # Also try: heading number in first span, title in next
                    # e.g., "10.1" + "Introduction" as separate spans
                    if not heading_re.match(heading_text):
                        # Try joining with space between spans
                        heading_text2 = " ".join(p.strip() for p in heading_text_parts if p.strip())
                        if heading_re.match(heading_text2):
                            heading_text = heading_text2

                    # ── Match heading pattern ──
                    m = heading_re.match(heading_text)
                    if not m:
                        continue

                    number = m.group(1)
                    title = m.group(2).strip()

                    # Reject heading numbers starting with 0
                    # (e.g. "0.2 kg of capsicums" is body text)
                    if number.startswith('0.'):
                        continue

                    # ── Validation ──
                    # Must start with letter
                    if not title or not title[0].isalpha():
                        continue

                    # Minimum meaningful title
                    if len(title) < 3:
                        continue

                    # Not an equation or numeric expression
                    if re.match(r'^[\d\s\+\-\*\/=\(\)\[\]\.,]+$', title):
                        continue

                    # At least 1 word with 3+ letters
                    valid_words = sum(1 for w in title.split()
                                     if len(w) >= 3 and any(c.isalpha() for c in w))
                    if valid_words < 1:
                        continue

                    # Title length cap: cut at last space before 100 chars
                    if len(title) > 100:
                        cut = title[:100].rfind(' ')
                        if cut > 10:
                            title = title[:cut]

                    # Skip exercise/example patterns  
                    if re.match(r'^(Exercise|Example|Solution|Table|Figure|Fig)\b', title, re.I):
                        continue

                    all_headings.append({
                        "number": number,
                        "title": title.strip(),
                        "page": page_num + 1,
                        "size": heading_max_sz
                    })

        return all_headings

    # ═══════════ HIERARCHY ═══════════
    def _build_hierarchy(self, headings: List[Dict]) -> List[Dict]:
        """Build hierarchical structure from flat headings list."""
        hierarchy = []
        stack = []

        for heading in headings:
            number = heading["number"]
            level = len(number.split('.'))

            node = {
                "number": number,
                "title": heading["title"],
                "page": heading["page"],
                "subtopics": []
            }

            while stack and len(stack[-1]["number"].split('.')) >= level:
                stack.pop()

            if stack:
                stack[-1]["subtopics"].append(node)
            else:
                hierarchy.append(node)

            stack.append(node)

        return hierarchy

    # ═══════════ PUBLIC ═══════════
    def extract(self) -> Dict:
        """Extract chapter info and topic hierarchy."""
        self._extract_chapter_info_v2()
        headings = self._extract_section_headings()
        topics = self._build_hierarchy(headings)

        return {
            "chapter_number": self.chapter_number,
            "chapter_title": self.chapter_title,
            "topics": topics
        }

    def extract_topics(self) -> Dict:
        """Alias for backward compat."""
        return self.extract()

    @staticmethod
    def _count_topics(topics: List[Dict]) -> int:
        count = len(topics)
        for t in topics:
            if t.get("subtopics"):
                count += MathsHeadingsExtractor._count_topics(t["subtopics"])
        return count


# ════════════════════ BATCH / CLI ════════════════════
def get_all_maths_pdfs(base_dir):
    base = Path(base_dir)
    results = []
    for gd in sorted(base.iterdir()):
        if not gd.is_dir() or not gd.name.startswith("grade"):
            continue
        for sd in sorted(gd.iterdir()):
            if not sd.is_dir() or sd.name != "maths":
                continue
            pdf_dirs = []
            if any(d.name.startswith("part") for d in sd.iterdir() if d.is_dir()):
                for pd in sorted(sd.iterdir()):
                    if pd.is_dir() and pd.name.startswith("part"):
                        pdf_dirs.append(pd)
            else:
                pdf_dirs.append(sd)
            for pdir in pdf_dirs:
                for f in sorted(pdir.glob("chapter*.pdf")):
                    results.append((str(f), str(f.relative_to(base))))
    return results


def process_all(base_dir, output_dir):
    pdfs = get_all_maths_pdfs(base_dir)
    base, out = Path(base_dir), Path(output_dir)
    print(f"Found {len(pdfs)} maths PDFs\n")
    for pp, label in pdfs:
        try:
            ext = MathsHeadingsExtractor(pp)
            result = ext.extract()
            ext.close()

            rel = Path(pp).relative_to(base)
            of = out / rel.with_suffix(".json")
            of.parent.mkdir(parents=True, exist_ok=True)
            with open(of, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)

            n = len(result.get("topics", []))
            total = MathsHeadingsExtractor._count_topics(result.get("topics", []))
            print(f"  OK  {label}: Ch {result.get('chapter_number','?')} "
                  f"'{result.get('chapter_title','?')}' - {total} headings")
        except Exception as e:
            print(f"  ERR {label}: {e}")


if __name__ == "__main__":
    import sys
    base = Path(__file__).parent.parent / "data" / "input"
    out = Path(__file__).parent.parent / "data" / "intermediate" / "headings"

    if len(sys.argv) > 1 and sys.argv[1] == "batch":
        process_all(str(base), str(out))
    elif len(sys.argv) > 1 and sys.argv[1] != "test":
        ext = MathsHeadingsExtractor(sys.argv[1])
        r = ext.extract()
        ext.close()
        print(json.dumps(r, indent=2, ensure_ascii=False))
    else:
        # Test mode: specific files
        test_files = [
            base / "grade6" / "maths" / "chapter1.pdf",
            base / "grade9" / "maths" / "chapter1.pdf",
            base / "grade10" / "maths" / "chapter1.pdf",
            base / "grade10" / "maths" / "chapter8.pdf",
            base / "grade10" / "maths" / "chapter12.pdf",
            base / "grade11" / "maths" / "chapter3.pdf",
            base / "grade11" / "maths" / "chapter6.pdf",
            base / "grade11" / "maths" / "chapter10.pdf",
            base / "grade12" / "maths" / "part1" / "chapter5.pdf",
            base / "grade12" / "maths" / "part2" / "chapter5.pdf",
        ]
        for tf in test_files:
            if not tf.exists():
                print(f"Not found: {tf}")
                continue
            print(f"\n{'='*60}")
            print(f"FILE: {tf.relative_to(base)}")
            print('='*60)
            ext = MathsHeadingsExtractor(str(tf))
            r = ext.extract()
            ext.close()
            print(json.dumps(r, indent=2, ensure_ascii=False))
