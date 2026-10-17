#!/usr/bin/env python3
"""
Search index over textbook passages
====================================
Input :  data/intermediate/passages/*.jsonl   (from build_passages.py)
Output:  data/intermediate/index/{embeddings.npy, passages.jsonl, bm25.pkl, meta.json}

Two retrievers, because neither is enough on its own:
  * BM25 catches exact wording — "Baudhayana", "NaOH", "Heron's formula"
  * embeddings catch paraphrase — "how fast something speeds up" -> acceleration
Scores are normalised per query and blended (hybrid), then filtered by grade/subject.

This replaces the old fuzzy title match, which compared a concept name against a
section title and then kept the first 1,000 characters of the section.

Usage:
  python scripts/build_index.py                                   # build
  python scripts/build_index.py --query "quadratic formula" --grade 10 --subject maths
  python scripts/build_index.py --selftest                        # known-answer checks
"""

import argparse
import json
import pickle
import re
from pathlib import Path

import numpy as np

BASE_DIR = Path(__file__).resolve().parent.parent
PASSAGE_DIR = BASE_DIR / "data" / "intermediate" / "passages"
INDEX_DIR = BASE_DIR / "data" / "intermediate" / "index"
MODEL_NAME = "BAAI/bge-small-en-v1.5"      # 133 MB, runs fine on CPU
BM25_WEIGHT = 0.4                          # rest goes to the embedding score

TOKEN_RE = re.compile(r"[a-z0-9]+")


def tokenize(text: str) -> list[str]:
    return TOKEN_RE.findall(text.lower())


def load_passages() -> list[dict]:
    passages = []
    for path in sorted(PASSAGE_DIR.glob("*.jsonl")):
        with path.open(encoding="utf-8") as f:
            passages.extend(json.loads(line) for line in f)
    if not passages:
        raise SystemExit(f"no passages in {PASSAGE_DIR} — run build_passages.py first")
    return passages


def embed_text(rec: dict) -> str:
    """Give the embedder the section heading too — it carries the topic name."""
    return f"{rec['section']}\n{rec['text']}" if rec["section"] else rec["text"]


def build(device: str, batch_size: int) -> None:
    from sentence_transformers import SentenceTransformer
    from rank_bm25 import BM25Okapi

    passages = load_passages()
    print(f"{len(passages)} passages from {len(list(PASSAGE_DIR.glob('*.jsonl')))} files")
    INDEX_DIR.mkdir(parents=True, exist_ok=True)

    print(f"embedding with {MODEL_NAME} on {device} …")
    model = SentenceTransformer(MODEL_NAME, device=device)
    vectors = model.encode(
        [embed_text(p) for p in passages],
        batch_size=batch_size, normalize_embeddings=True,
        show_progress_bar=True, convert_to_numpy=True,
    ).astype("float32")

    print("building BM25 …")
    bm25 = BM25Okapi([tokenize(embed_text(p)) for p in passages])

    np.save(INDEX_DIR / "embeddings.npy", vectors)
    (INDEX_DIR / "bm25.pkl").write_bytes(pickle.dumps(bm25))
    with (INDEX_DIR / "passages.jsonl").open("w", encoding="utf-8") as f:
        for p in passages:
            f.write(json.dumps(p, ensure_ascii=False) + "\n")
    (INDEX_DIR / "meta.json").write_text(json.dumps({
        "model": MODEL_NAME, "passages": len(passages),
        "dim": int(vectors.shape[1]), "bm25_weight": BM25_WEIGHT,
    }, indent=2), encoding="utf-8")
    print(f"index written to {INDEX_DIR.relative_to(BASE_DIR).as_posix()} "
          f"({len(passages)} passages, dim {vectors.shape[1]})")


class Index:
    """Loaded index; search() blends BM25 and embedding similarity."""

    def __init__(self, device: str = "cpu") -> None:
        from sentence_transformers import SentenceTransformer

        self.passages = [json.loads(l) for l in (INDEX_DIR / "passages.jsonl").open(encoding="utf-8")]
        self.vectors = np.load(INDEX_DIR / "embeddings.npy")
        self.bm25 = pickle.loads((INDEX_DIR / "bm25.pkl").read_bytes())
        self.model = SentenceTransformer(MODEL_NAME, device=device)

    def search(self, query: str, k: int = 5, grade: int | None = None,
               subject: str | None = None) -> list[tuple[float, dict]]:
        keep = np.array([
            (grade is None or p["grade"] == grade) and (subject is None or p["subject"] == subject)
            for p in self.passages
        ])
        if not keep.any():
            return []

        lexical = np.asarray(self.bm25.get_scores(tokenize(query)), dtype="float32")
        dense = self.vectors @ self.model.encode(query, normalize_embeddings=True).astype("float32")

        def norm(x: np.ndarray) -> np.ndarray:          # per-query, so the blend is meaningful
            x = np.where(keep, x, -np.inf)
            finite = x[np.isfinite(x)]
            lo, hi = (finite.min(), finite.max()) if finite.size else (0.0, 1.0)
            return np.where(np.isfinite(x), (x - lo) / (hi - lo + 1e-9), 0.0)

        score = BM25_WEIGHT * norm(lexical) + (1 - BM25_WEIGHT) * norm(dense)
        score = np.where(keep, score, -1.0)
        return [(float(score[i]), self.passages[i]) for i in np.argsort(-score)[:k]]


# Known answers: query -> (grade, subject, text that must appear in a top hit)
SELFTESTS = [
    ("quadratic formula", 10, "maths", "4ac"),
    ("nature of roots discriminant", 10, "maths", "discriminant"),
    ("balancing a chemical equation", 10, "science", "balanc"),
    ("displacement reaction copper sulphate", 10, "science", "CuSO"),
    ("what is a fractional unit", 6, "maths", "fraction"),
    ("Heron's formula area of triangle", 9, "maths", "Heron"),
    ("photosynthesis in plants", 10, "science", "photosynth"),
    ("Pythagoras theorem right triangle", 10, "maths", "square"),
]


def selftest() -> None:
    index = Index()
    passed = 0
    for query, grade, subject, needle in SELFTESTS:
        hits = index.search(query, k=3, grade=grade, subject=subject)
        ok = any(needle.lower() in (h[1]["text"] + h[1]["section"]).lower() for h in hits)
        passed += ok
        top = hits[0][1] if hits else None
        where = f"{top['chapter']} · {top['section'][:32]!r} p{top['page']}" if top else "no hits"
        print(f"  {'PASS' if ok else 'FAIL'}  {query!r} (gr{grade} {subject}) -> {where}")
    print(f"{passed}/{len(SELFTESTS)} known-answer checks passed")


def main() -> None:
    p = argparse.ArgumentParser(description="Build/query the passage search index")
    p.add_argument("--query")
    p.add_argument("--grade", type=int)
    p.add_argument("--subject")
    p.add_argument("-k", type=int, default=5)
    p.add_argument("--device", default="cpu", help="cpu keeps the GPU free for extraction")
    p.add_argument("--batch-size", type=int, default=32)
    p.add_argument("--selftest", action="store_true")
    args = p.parse_args()

    if args.selftest:
        selftest()
    elif args.query:
        for score, rec in Index(args.device).search(args.query, args.k, args.grade, args.subject):
            print(f"\n[{score:.3f}] grade {rec['grade']} {rec['subject']} · {rec['chapter']} · "
                  f"{rec['section'][:50]!r} · p{rec['page']} · {rec['kind']}")
            print("   " + " ".join(rec["text"].split())[:300])
    else:
        build(args.device, args.batch_size)


if __name__ == "__main__":
    main()
