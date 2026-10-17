#!/usr/bin/env python3
"""
Split extracted textbook Markdown into labelled passages
=========================================================
Input :  data/intermediate/markdown/**/*.md   (from extract_markdown.py)
Output:  data/intermediate/passages/{grade}_{subject}.jsonl

One JSON object per passage:
  {"id", "grade", "subject", "book", "chapter", "section", "page", "pages",
   "kind", "text", "n_words", "has_math"}

Why passages: a whole chapter is far too big to retrieve against or to put in a
generation prompt, so each concept needs to match a specific piece of text
(a definition, a worked example, an activity) with its grade and page attached.

Splitting:
  * section boundaries are NUMBERED headings ("## 4.3 Solution of ...") only —
    MinerU also emits "## Solution :" and "## Example 6 : ..." for bold lines,
    which are content, not structure
  * long sections are cut into ~300-word windows with ~50 words of overlap,
    never inside display math, a table or a list item
  * tiny fragments are merged into the previous passage

Cleanup applied on the way (defects measured in data/intermediate/extraction_eval):
  * running headers, page numbers and "Reprint 20xx-xx" footers dropped
  * two \\tag commands on one equation (KaTeX refuses to render it)
  * \\tag holding words rather than an equation number
  * "$a$$b$" adjacency that Markdown math parsers misread
  * figure placeholders reduced to [figure]
  * stray equation-number lines reattached to the equation above

Usage:
  python scripts/build_passages.py                 # all extracted books
  python scripts/build_passages.py --only grade10  # subset by path prefix
  python scripts/build_passages.py --stats         # summarise what was built
"""

import argparse
import json
import re
from collections import Counter
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MD_DIR = BASE_DIR / "data" / "intermediate" / "markdown"
OUT_DIR = BASE_DIR / "data" / "intermediate" / "passages"

TARGET_WORDS = 300          # aim per passage
OVERLAP_WORDS = 50          # carried into the next window so ideas aren't cut in half
MIN_WORDS = 40              # anything shorter is merged backwards

PAGE_RE = re.compile(r"^<!--\s*page\s+(\d+)\s+of\s+\d+\s*-->\s*$")
NUMBERED_HEADING_RE = re.compile(r"^#{1,4}\s+(\d+(?:\.\d+)*)\s+(.+?)\s*$")

# Blocks the books title instead of numbering. Each starts a new passage and fixes the
# passage's kind, because an exercise full of "____" reads exactly like explanation to a
# retriever and must never be served as one.
#
# Counted over all 233 books, so the spellings are the real ones: "Figure it Out" appears
# 226 times across three casings (including a stray "? Figure it Out"), "EXERCISES" 99
# times. The old pattern missed both — `EXERCISE\b` cannot match "EXERCISES", since there
# is no word boundary between E and S, and only two casings of "questions" were listed.
#
# "Solution" (191) is deliberately absent: MinerU marks it as a heading, and splitting
# there would cut every worked example away from the problem it solves.
BLOCK_HEADINGS: tuple[tuple[str, str], ...] = (
    ("figure it out", "exercise"),
    ("let us enhance our learning", "exercise"),
    ("exploratory project", "exercise"),
    ("exercise", "exercise"),
    ("intext question", "questions"),
    ("question", "questions"),
    ("miscellaneous example", "example"),
    ("what you have learnt", "summary"),
    ("in a nutshell", "summary"),
    ("points to ponder", "summary"),
    ("summary", "summary"),
    ("activity", "activity"),
    # Side boxes: real prose, but trivia and asides rather than the explanation. Left as
    # "text" they get retrieved as grounding — "Integers" at Grade 7 drew both its
    # anchors from "A Pinch of History". Their own kind keeps them out of that without
    # deleting them.
    ("a pinch of history", "note"),
    ("historical note", "note"),
    ("a step further", "note"),
    ("fascinating facts", "note"),
    ("ever heard of", "note"),
    ("did you ever wonder", "note"),
    ("science and society", "note"),
    ("our scientific heritage", "note"),
    ("know a scientist", "note"),
    ("keep the curiosity alive", "note"),
    ("discover, design", "note"),
    ("learning further", "note"),
    ("safety first", "note"),
    ("snapshots", "note"),
    ("objectives", "note"),
)
NAMED_HEADING_RE = re.compile(
    r"^#{1,4}\s+[^\w]*((?:" + "|".join(re.escape(t) for t, _ in BLOCK_HEADINGS) + r").*)$",
    re.IGNORECASE,
)
LABEL_ONLY_RE = re.compile(r"^\(?\d+\.\d+[a-z]?\)?$")          # "(2.5)" sitting on its own line
FOOTER_RE = re.compile(r"^(Reprint\s+\d{4}-\d{2,4}|\d{1,3})$", re.IGNORECASE)
FIGURE_RE = re.compile(r"!\[[^\]]*\]\([^)]*\)")


def clean_math(text: str) -> str:
    """Repair the LaTeX defects that stop KaTeX rendering or confuse Markdown."""
    # two \tag on one equation -> keep the equation number, keep the other as text
    def one_tag(m: re.Match) -> str:
        first, second = m.group(1), m.group(2)
        number, word = (second, first) if re.fullmatch(r"[\d.]+", second) else (first, second)
        return f"\\tag{{{number}}}" if re.fullmatch(r"[\d.]+", number) else f"\\tag{{{word}}}"

    text = re.sub(r"\\tag\s*\{([^{}]*)\}\s*\\tag\s*\{([^{}]*)\}", one_tag, text)
    # \tag holding words (e.g. a mangled side note) is noise
    text = re.sub(r"\\tag\s*\{\s*\\\(.*?\\\)[^{}]*\}", "", text)
    # "$a$$b$" reads as display math to most parsers
    text = re.sub(r"(?<=[^\s$])\$\$(?=[^\s$])", "$ $", text)
    # commands the model invented or put in text mode, where KaTeX refuses to render
    text = text.replace("\\cosine", "\\cos")

    def fix_text_mode(m: re.Match) -> str:
        inner = m.group(1)
        inner = inner.replace("\\Delta", "Δ").replace("\\delta", "δ")
        inner = re.sub(r"\\overline\s*\{([^{}]*)\}",
                       lambda o: o.group(1) + "\u0304", inner)            # P(\overline{E}) -> P(Ē)
        return f"\\text{{{inner}}}"

    text = re.sub(r"\\text\s*\{([^{}]*)\}", fix_text_mode, text)
    return text


def strip_furniture(lines: list[str], repeated: set[str]) -> list[str]:
    """Drop page numbers, reprint footers and running headers."""
    out = []
    for line in lines:
        s = line.strip()
        if not s or FOOTER_RE.match(s) or s in repeated:
            if not s:
                out.append("")
            continue
        out.append(line)
    return out


def repeated_short_lines(lines: list[str]) -> set[str]:
    """Running headers repeat on many pages and are short."""
    counts = Counter(l.strip() for l in lines if 0 < len(l.strip()) <= 60)
    return {
        text for text, n in counts.items()
        if n >= 3 and not text.startswith(("#", "$", "|", "-", "*"))
        and (text.isupper() or text.istitle())
        and not re.search(r"[.=]", text)
    }


def blocks_of(lines: list[tuple[str, int]]) -> list[tuple[str, int]]:
    """Group (line, page) pairs into atomic blocks (paragraph, display math, table, list item)."""
    blocks: list[tuple[str, int]] = []
    buf: list[str] = []
    page = lines[0][1] if lines else 1
    in_math = False

    def flush() -> None:
        nonlocal buf
        if buf and "\n".join(buf).strip():
            blocks.append(("\n".join(buf).strip(), page))
        buf = []

    for line, line_page in lines:
        if not buf:
            page = line_page          # a block is attributed to the page it starts on
        if line.strip() == "$$":
            buf.append(line)
            if in_math:          # closing delimiter ends the block
                in_math = False
                flush()
            else:
                in_math = True
            continue
        if in_math:
            buf.append(line)
            continue
        if not line.strip():
            flush()
            continue
        if LABEL_ONLY_RE.match(line.strip()) and blocks and not buf:
            prev, prev_page = blocks[-1]          # "(2.5)" belongs to the equation above
            blocks[-1] = (f"{prev}  {line.strip()}", prev_page)
            continue
        buf.append(line)
    flush()
    return blocks


def windows(blocks: list[tuple[str, int]]) -> list[tuple[str, list[int]]]:
    """Pack blocks into ~TARGET_WORDS passages, overlapping a little, never splitting a block."""
    passages: list[tuple[str, list[int]]] = []
    cur: list[str] = []
    cur_pages: list[int] = []
    cur_words = 0

    # A huge table arrives as one block that can never be split by packing alone,
    # so cut oversized blocks on word boundaries first.
    sized: list[tuple[str, int]] = []
    for text, page in blocks:
        words = text.split()
        if len(words) > TARGET_WORDS * 2:
            step = TARGET_WORDS - OVERLAP_WORDS
            for i in range(0, len(words), step):
                sized.append((" ".join(words[i:i + TARGET_WORDS]), page))
        else:
            sized.append((text, page))

    for text, page in sized:
        n = len(text.split())
        if cur_words + n > TARGET_WORDS and cur_words >= MIN_WORDS:
            passages.append(("\n\n".join(cur), sorted(set(cur_pages))))
            tail, tail_words = [], 0
            for prev in reversed(cur):            # carry a little context forward
                w = len(prev.split())
                if tail_words + w > OVERLAP_WORDS:
                    break
                tail.insert(0, prev)
                tail_words += w
            cur, cur_pages, cur_words = tail, [page], tail_words
        cur.append(text)
        cur_pages.append(page)
        cur_words += n

    if cur:
        if passages and cur_words < MIN_WORDS:    # merge a runt into the previous passage
            prev_text, prev_pages = passages[-1]
            passages[-1] = (prev_text + "\n\n" + "\n\n".join(cur), sorted(set(prev_pages + cur_pages)))
        else:
            passages.append(("\n\n".join(cur), sorted(set(cur_pages))))
    return passages


def classify(text: str, section: str) -> str:
    """Label the passage, preferring its section heading over its first words.

    Driven by the same BLOCK_HEADINGS table that decides where a section starts, so a
    block can never be split out as its own section and then labelled as prose. The
    longer titles are listed first there, which matters here: "intext question" must be
    tested before "question" and "what you have learnt" before "summary".

    Matching is anchored to the start of the block title, never a substring anywhere in
    the heading — "6.5 The 'Why' Question for Adolescence" is a real prose section and
    must not be labelled a question set.
    """
    # Sections built above read "<numbered section> — <block title>", so the block is
    # whatever follows the last dash. The section number is stripped as well, because a
    # chapter's own summary arrives as a numbered heading ("4.5 Summary") and would
    # otherwise never match. Stripping the number is safe for the substring risk above:
    # "6.5 The 'Why' Question for Adolescence" still begins with "the", not "question".
    tail = section.lower().rsplit("—", 1)[-1].strip()
    tail = re.sub(r"^[\d.]+\s*", "", tail)
    for title, kind in BLOCK_HEADINGS:
        if tail.startswith(title):
            return kind

    # Fallback for a block whose heading MinerU did not mark up at all, so it was never
    # split off: such a passage begins with the title itself.
    head = re.sub(r"^[^\w]+", "", text[:120].lower())
    for title, kind in BLOCK_HEADINGS:
        if head.startswith(title):
            return kind
    if head.startswith("example"):
        return "example"
    return "text"


def split_book(md_path: Path) -> list[dict]:
    rel = md_path.relative_to(MD_DIR)
    parts = rel.with_suffix("").parts          # e.g. ('grade11','physics','part1','chapter2')
    grade = int(re.sub(r"\D", "", parts[0]))
    subject = parts[1]
    chapter = parts[-1]
    book = "/".join(parts[2:-1]) or "main"

    raw = md_path.read_text(encoding="utf-8")
    raw = clean_math(raw)
    raw = FIGURE_RE.sub("[figure]", raw)
    raw = re.sub(r"(?m)^\\([-*])", r"\1", raw)        # MinerU escapes list bullets as "\-"
    lines = raw.splitlines()
    lines = strip_furniture(lines, repeated_short_lines(lines))

    # Resolve the page for every line first, so page numbers survive sectioning
    paged: list[tuple[str, int]] = []
    page = 1
    for line in lines:
        m = PAGE_RE.match(line.strip())
        if m:
            page = int(m.group(1))
            continue
        paged.append((line, page))

    # Cut into sections at numbered headings and at the titled blocks, then window each.
    # A block keeps the numbered section it sits inside ("7.1 Fractions — Figure it Out"),
    # so a citation still says where in the chapter it came from, and the block's own
    # passages stay separate from the explanation they interrupt.
    sections: list[tuple[str, list[tuple[str, int]]]] = [("", [])]
    numbered = ""
    for line, line_page in paged:
        numbered_match = NUMBERED_HEADING_RE.match(line)
        block_match = None if numbered_match else NAMED_HEADING_RE.match(line)
        if numbered_match:
            numbered = " ".join(g for g in numbered_match.groups() if g).strip()
            sections.append((numbered, []))
        elif block_match:
            block = block_match.group(1).strip()
            sections.append((f"{numbered} — {block}" if numbered else block, []))
        else:
            sections[-1][1].append((line, line_page))

    out: list[dict] = []
    for section, sec_lines in sections:
        for text, pages in windows(blocks_of(sec_lines)):
            words = len(text.split())
            if words < 15:                      # drop scraps
                continue
            out.append({
                # The book part belongs in the id: grades 7, 8 and 12 maths and grades
                # 11-12 physics and chemistry ship as part1/part2 with chapter numbering
                # restarting at 1 in each, so without it 1,502 of 8,267 passages collided
                # and a citation could resolve to a different passage entirely.
                "id": (f"g{grade}_{subject}_"
                       f"{book.replace('/', '_') + '_' if book != 'main' else ''}"
                       f"{chapter}_{len(out):03d}"),
                "grade": grade, "subject": subject, "book": book, "chapter": chapter,
                "section": section, "page": pages[0] if pages else None, "pages": pages,
                "kind": classify(text, section), "n_words": words,
                "has_math": "$" in text,
                "text": text,
            })
    return out


def main() -> None:
    p = argparse.ArgumentParser(description="Split extracted Markdown into labelled passages")
    p.add_argument("--only", default="", help="Only books whose path under markdown/ starts with this")
    p.add_argument("--stats", action="store_true", help="Print a summary of what was built")
    args = p.parse_args()

    books = sorted(b for b in MD_DIR.rglob("*.md")
                   if b.relative_to(MD_DIR).as_posix().startswith(args.only))
    if not books:
        raise SystemExit(f"no extracted markdown under {MD_DIR}")

    OUT_DIR.mkdir(parents=True, exist_ok=True)
    per_file: dict[Path, list[dict]] = {}
    for book in books:
        passages = split_book(book)
        parts = book.relative_to(MD_DIR).parts
        per_file.setdefault(OUT_DIR / f"{parts[0]}_{parts[1]}.jsonl", []).extend(passages)

    for out_path, passages in per_file.items():
        with out_path.open("w", encoding="utf-8") as f:
            for rec in passages:
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")
        print(f"{out_path.relative_to(BASE_DIR).as_posix()}: {len(passages)} passages from "
              f"{len({r['chapter'] for r in passages})} chapters")

    if args.stats:
        allp = [r for rs in per_file.values() for r in rs]
        words = sorted(r["n_words"] for r in allp)
        print(f"\ntotal {len(allp)} passages | median {words[len(words)//2]} words | "
              f"p90 {words[int(len(words)*0.9)]} | max {words[-1]}")
        print("kinds:", dict(Counter(r['kind'] for r in allp)))
        print("with math:", sum(r["has_math"] for r in allp),
              "| sections detected:", len({(r['chapter'], r['section']) for r in allp}))


if __name__ == "__main__":
    main()
