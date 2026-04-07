"""
Science/Biology/Chemistry/Physics PDF Headings Extractor (v4)
─────────────────────────────────────────────────────────────
Key design decisions:
  1. MODE dedup — keeps most-common text at each position cluster
  2. Overlaid flag — spans with count>1 use direct concat; normal use spaces
  3. No min-size filter — small-caps headings (9pt within 13pt) are kept
  4. Title length cap — 80 chars max prevents body text contamination
  5. Per-heading bold/size filter — only same-style spans included
"""
import fitz
import re
import json
from pathlib import Path
from collections import Counter
from typing import List, Dict, Tuple


class ScienceHeadingsExtractor:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.doc = fitz.open(pdf_path)
        self.chapter_number = None
        self.chapter_title = None

    # ═══════════ SPAN DEDUP ═══════════
    def _deduplicate_spans(self, page, tol=2.0):
        blocks = page.get_text("dict")["blocks"]
        raw = []
        for blk in blocks:
            if "lines" not in blk:
                continue
            for ln in blk["lines"]:
                for sp in ln["spans"]:
                    t = sp["text"].strip()
                    if t:
                        raw.append({
                            "text": t,
                            "size": round(sp["size"], 1),
                            "bold": bool(sp["flags"] & (1 << 4)),
                            "x": sp["origin"][0],
                            "y": sp["origin"][1],
                            "x1": sp["bbox"][2],
                        })

        clusters = []
        for sp in raw:
            merged = False
            for cl in clusters:
                if (abs(sp["x"] - cl["x"]) < tol and
                        abs(sp["y"] - cl["y"]) < tol and
                        abs(sp["size"] - cl["size"]) < 1.0):
                    cl["texts"][sp["text"]] += 1
                    cl["bold"] = cl["bold"] or sp["bold"]
                    if sp["text"] not in cl["x1_map"]:
                        cl["x1_map"][sp["text"]] = sp["x1"]
                    merged = True
                    break
            if not merged:
                clusters.append({
                    "x": sp["x"], "y": sp["y"],
                    "size": sp["size"], "bold": sp["bold"],
                    "texts": Counter({sp["text"]: 1}),
                    "x1_map": {sp["text"]: sp["x1"]},
                })

        result = []
        for cl in clusters:
            best = cl["texts"].most_common(1)[0][0]
            total = sum(cl["texts"].values())
            result.append({
                "text": best,
                "size": cl["size"],
                "bold": cl["bold"],
                "x": cl["x"],
                "y": cl["y"],
                "x1": cl["x1_map"][best],
                "overlaid": total > 1,
            })
        result.sort(key=lambda s: (s["y"], s["x"]))
        return result

    # ═══════════ LINE BUILDING ═══════════
    def _build_lines(self, spans, y_tol=3.0):
        if not spans:
            return []
        lines, cur, cy = [], [spans[0]], spans[0]["y"]
        for sp in spans[1:]:
            if abs(sp["y"] - cy) <= y_tol:
                cur.append(sp)
            else:
                cur.sort(key=lambda s: s["x"])
                lines.append(cur)
                cur, cy = [sp], sp["y"]
        cur.sort(key=lambda s: s["x"])
        lines.append(cur)
        return lines

    # ═══════════ FRAGMENT JOINING ═══════════
    def _line_text(self, line_spans):
        """
        Overlaid spans → direct concat (fragments of same word split by PDF).
        Normal spans → space-separated (proper word boundaries).
        """
        if not line_spans:
            return ""
        parts = [line_spans[0]["text"]]
        prev_overlaid = line_spans[0]["overlaid"]
        prev_x1 = line_spans[0]["x1"]

        for sp in line_spans[1:]:
            gap = sp["x"] - prev_x1
            # For overlaid spans, use tight gap threshold for direct concat
            if sp["overlaid"] or prev_overlaid:
                threshold = sp["size"] * 0.35
                if gap < threshold:
                    parts[-1] += sp["text"]
                else:
                    parts.append(sp["text"])
            else:
                # Normal spans: always space-separated
                parts.append(sp["text"])
            prev_overlaid = sp["overlaid"]
            prev_x1 = sp["x1"]

        return " ".join(parts)

    # ═══════════ TEXT CLEANING ═══════════
    def _clean_text(self, text):
        for _ in range(5):
            text = re.sub(r'\b([A-Z])\s([A-Z])', r'\1\2', text)
        return re.sub(r'\s+', ' ', text).strip()

    # ═══════════ CHAPTER INFO ═══════════
    def _extract_chapter_info(self):
        for pn in range(min(3, len(self.doc))):
            page = self.doc[pn]
            spans = self._deduplicate_spans(page)
            for sp in spans:
                t, sz = sp["text"].strip(), sp["size"]
                if sz >= 30 and re.match(r'^\d{1,2}$', t) and not self.chapter_number:
                    self.chapter_number = int(t)
                if 18 <= sz <= 50 and len(t) > 3 and not re.match(r'^\d+$', t):
                    skip = ['chapter', 'unit', 'probe', 'ponder', 'objective',
                            'hapter', 'nit']
                    if any(w in t.lower() for w in skip):
                        continue
                    self.chapter_title = (self.chapter_title + " " + t
                                         if self.chapter_title else t)
        if self.chapter_title:
            self.chapter_title = self._clean_text(self.chapter_title)
            if self.chapter_title.isupper() and len(self.chapter_title) > 5:
                self.chapter_title = self.chapter_title.title()

    # ═══════════ HEADING NUMBER VALIDATION ═══════════
    @staticmethod
    def _valid_heading_number(num_str, chapter_num):
        parts = num_str.split(".")
        try:
            first, second = int(parts[0]), int(parts[1])
        except (ValueError, IndexError):
            return False
        if first < 1 or first > 20:
            return False
        if chapter_num and first != chapter_num:
            return False
        if second > 12:
            return False
        if len(parts) >= 3:
            try:
                if int(parts[2]) > 12:
                    return False
            except ValueError:
                return False
        return len(parts) <= 3

    # ═══════════ HEADING EXTRACTION ═══════════
    def _extract_headings(self):
        heading_re = re.compile(r'^(\d+\.\d+(?:\.\d+)*)\s+(.+)')
        skip_start = re.compile(
            r'^(Activity|Example|Solution|Table|Figure|Fig)\b', re.I)

        all_headings = []
        seen = set()

        for pn in range(len(self.doc)):
            page = self.doc[pn]
            spans = self._deduplicate_spans(page)
            lines = self._build_lines(spans)

            for line_spans in lines:
                # Build text using overlaid-aware joining
                text = self._line_text(line_spans)
                text = self._clean_text(text)

                m = heading_re.match(text)
                if not m:
                    continue

                number, title = m.group(1), m.group(2).strip()

                if not self._valid_heading_number(number, self.chapter_number):
                    continue
                if skip_start.match(title):
                    continue

                # ── Title length cap: prevent body text contamination ──
                if len(title) > 80:
                    # Cut at last space before 80 chars
                    cut = title[:80].rfind(' ')
                    if cut > 10:
                        title = title[:cut]

                # Skip extremely short titles
                if len(title) < 3:
                    continue
                # TOC entries (left margin, small text, short)
                max_sz = max(s["size"] for s in line_spans)
                if max_sz <= 10.5 and line_spans[0]["x"] < 55:
                    continue
                if number in seen:
                    continue
                seen.add(number)

                # Title case if ALL CAPS
                if title.isupper() and len(title) > 3:
                    title = title.title()

                all_headings.append({
                    "number": number, "title": title,
                    "page": pn + 1, "size": max_sz,
                })

        return all_headings

    # ═══════════ HIERARCHY ═══════════
    def _build_hierarchy(self, headings):
        topics, current_main = [], None
        for h in headings:
            depth = len(h["number"].split("."))
            entry = {"number": h["number"], "title": h["title"], "page": h["page"]}
            if depth == 2:
                entry["subtopics"] = []
                topics.append(entry)
                current_main = entry
            elif depth >= 3 and current_main:
                current_main["subtopics"].append(entry)
            else:
                topics.append(entry)
        return topics

    # ═══════════ PUBLIC ═══════════
    def extract(self):
        self._extract_chapter_info()
        headings = self._extract_headings()
        return {
            "chapter_number": self.chapter_number,
            "chapter_title": self.chapter_title,
            "topics": self._build_hierarchy(headings),
        }


# ════════════════════ BATCH / CLI ════════════════════
def get_all_science_pdfs(base_dir):
    base = Path(base_dir)
    results = []
    subjects = {"science", "biology", "chemistry", "physics"}
    for gd in sorted(base.iterdir()):
        if not gd.is_dir() or not gd.name.startswith("grade"):
            continue
        for sd in sorted(gd.iterdir()):
            if not sd.is_dir() or sd.name not in subjects:
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


def process_single(pdf_path):
    return ScienceHeadingsExtractor(pdf_path).extract()


def process_all(base_dir, output_dir):
    pdfs = get_all_science_pdfs(base_dir)
    base, out = Path(base_dir), Path(output_dir)
    print(f"Found {len(pdfs)} science PDFs\n")
    for pp, label in pdfs:
        try:
            result = process_single(pp)
            rel = Path(pp).relative_to(base)
            of = out / rel.with_suffix(".json")
            of.parent.mkdir(parents=True, exist_ok=True)
            with open(of, "w", encoding="utf-8") as f:
                json.dump(result, f, indent=2, ensure_ascii=False)
            n = len(result.get("topics", []))
            st = f"{n} topics" if n else "NO SECTIONS"
            print(f"  OK  {label}: Ch {result.get('chapter_number','?')} "
                  f"'{result.get('chapter_title','?')}' - {st}")
        except Exception as e:
            print(f"  ERR {label}: {e}")


if __name__ == "__main__":
    import sys
    base = Path(__file__).parent.parent / "data" / "input"
    out = Path(__file__).parent.parent / "data" / "intermediate" / "headings"

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        test_files = [
            base / "grade6" / "science" / "chapter1.pdf",
            base / "grade9" / "science" / "chapter1.pdf",
            base / "grade10" / "science" / "chapter1.pdf",
            base / "grade11" / "biology" / "chapter1.pdf",
            base / "grade12" / "chemistry" / "part1" / "chapter1.pdf",
            base / "grade12" / "biology" / "chapter1.pdf",
        ]
        for tf in test_files:
            if not tf.exists():
                print(f"Not found: {tf}")
                continue
            print(f"\n{'='*60}")
            print(f"FILE: {tf.relative_to(base)}")
            print('='*60)
            r = process_single(str(tf))
            print(json.dumps(r, indent=2, ensure_ascii=False))
    elif len(sys.argv) > 1:
        r = process_single(sys.argv[1])
        print(json.dumps(r, indent=2, ensure_ascii=False))
    else:
        process_all(str(base), str(out))
