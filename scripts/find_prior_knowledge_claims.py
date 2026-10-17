"""Find English pages that tell the student what they have already learned.

Sentences like "You have already studied X" or "as you learned in earlier classes"
are claims about the student's past. Nothing in the pipeline checks them: they are
either copied from a source book written for a different grade, or invented by the
model. This script only FINDS them (no edits, no API calls).

    python scripts/find_prior_knowledge_claims.py                 # grades 6 7 8, summary
    python scripts/find_prior_knowledge_claims.py --grades 8 -v   # also print each sentence
    python scripts/find_prior_knowledge_claims.py --csv out.csv

The pattern list is deliberately broad; read the sentences before acting on counts.
Pages are read from data/generated_pages/<domain>/grade<N>/<slug>.md (English only).
"""
import argparse, csv, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PAGES = ROOT / "data" / "generated_pages"

# (label, regex). Matched per sentence, case-insensitive.
PATTERNS = [
    ("already studied/learned/seen",
     r"\b(you|we|students?)\b[^.]{0,30}\balready\b[^.]{0,20}\b(studied|learn(?:ed|t)|seen|met|covered|know|knew|come across|used|done)\b"),
    ("already know",
     r"\balready\s+(know|knows|knew|familiar)\b"),
    ("you have studied/learned (no 'already')",
     r"\byou(?:'ve|’ve| have| had)\s+(?:also\s+|previously\s+|earlier\s+)?(studied|learn(?:ed|t)|seen|met|come across|worked with|used)\b"),
    ("we have learnt/studied",
     r"\bwe\s+(?:have|'ve|’ve)\s+(?:already\s+)?(studied|learn(?:ed|t)|seen)\b"),
    ("you may/might recall/know/remember",
     r"\byou\s+(?:may|might|must|can)\s+(?:already\s+|also\s+)?(?:recall|remember|know|have (?:seen|learn(?:ed|t)|studied|noticed))\b"),
    ("recall that / remember that",
     r"\b(recall|remember|revise|revisit)\s+(that|how|what|the)\b"),
    ("earlier / previous class, grade, chapter",
     r"\b(earlier|previous|lower|past)\s+(classes|class|grades?|chapters?|lessons?|years?)\b"),
    ("in class/grade N",
     r"\b(?:in|from)\s+(?:class|grade)\s+(?:[IVX]+|\d+)\b"),
    ("from your earlier / school years",
     r"\b(?:from|in)\s+(?:your\s+)?(?:earlier|previous|primary|school)\s+(?:studies|classes|years|schooling)\b"),
    ("as you know / as you have seen",
     r"\bas\s+you\s+(?:already\s+)?(?:know|have\s+(?:seen|learn(?:ed|t)|studied)|learn(?:ed|t))\b"),
    ("builds on your knowledge",
     r"\b(?:builds?\s+on|based\s+on|extends?)\s+(?:what\s+you|your\s+(?:knowledge|understanding|earlier))\b"),
    ("textbook chapter reference",
     r"\b(?:in|from)\s+(?:the\s+)?chapter\s+[‘'\"“]"),
]
COMPILED = [(n, re.compile(p, re.I)) for n, p in PATTERNS]

def english_pages(grades):
    for dom in sorted(p for p in PAGES.iterdir() if p.is_dir()):
        for g in grades:
            d = dom / f"grade{g}"
            if not d.is_dir():
                continue
            for f in sorted(d.glob("*.md")):
                if re.search(r"\.(hi|te|od)\.md$", f.name):
                    continue
                yield g, dom.name, f

def body(path):
    t = path.read_text(encoding="utf-8")
    if t.startswith("---"):
        t = t.split("\n---", 1)[1] if "\n---" in t[3:] else t
    t = re.sub(r"<!--.*?-->", "", t, flags=re.S)
    t = re.sub(r"\$\$.*?\$\$", " ", t, flags=re.S)          # display maths
    t = re.sub(r"\$[^$\n]*\$", " ", t)                      # inline maths
    t = re.sub(r"\[S\d+(?:,\s*S\d+)*\]", "", t)
    return t

def sentences(text):
    for para in re.split(r"\n\s*\n|\n(?=[#*\-\d])", text):
        for s in re.split(r"(?<=[.!?])\s+", para.strip()):
            s = " ".join(s.split())
            if s:
                yield s

def scan(path):
    hits = []
    for s in sentences(body(path)):
        if s.startswith("#"):
            continue
        for name, rx in COMPILED:
            if rx.search(s):
                hits.append((name, s))
                break
    return hits

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--grades", nargs="+", type=int, default=[6, 7, 8])
    ap.add_argument("-v", "--verbose", action="store_true", help="print every matching sentence")
    ap.add_argument("--csv", help="write one row per matching sentence")
    a = ap.parse_args()
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

    total = {g: [0, 0, 0] for g in a.grades}   # pages, pages with a hit, sentences
    rows, by_label = [], {}
    for g, dom, f in english_pages(a.grades):
        hits = scan(f)
        total[g][0] += 1
        if hits:
            total[g][1] += 1
            total[g][2] += len(hits)
        for name, s in hits:
            rows.append((g, dom, f.stem, name, s))
            by_label[name] = by_label.get(name, 0) + 1
        if hits and a.verbose:
            print(f"\n[{g}] {dom}/{f.stem}  ({len(hits)})")
            for name, s in hits:
                print(f"   - ({name}) {s[:230]}")

    print("\nEnglish pages with prior-knowledge claims")
    print(f"{'grade':>6} {'pages':>6} {'with a hit':>11} {'share':>6} {'sentences':>10}")
    tp = th = ts = 0
    for g in a.grades:
        p, h, s = total[g]
        tp, th, ts = tp + p, th + h, ts + s
        print(f"{g:>6} {p:>6} {h:>11} {(100*h/p if p else 0):>5.0f}% {s:>10}")
    print(f"{'all':>6} {tp:>6} {th:>11} {(100*th/tp if tp else 0):>5.0f}% {ts:>10}")
    print("\nBy pattern:")
    for k, v in sorted(by_label.items(), key=lambda x: -x[1]):
        print(f"  {v:>4}  {k}")
    if a.csv:
        with open(a.csv, "w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh); w.writerow(["grade", "domain", "slug", "pattern", "sentence"]); w.writerows(rows)
        print(f"\nwrote {len(rows)} rows to {a.csv}")

if __name__ == "__main__":
    main()
