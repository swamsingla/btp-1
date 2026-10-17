#!/usr/bin/env python3
"""
Match graph concepts to textbook passages
==========================================
For every (concept, grade) pair in the knowledge graphs, find the passages that
actually teach it, using the hybrid index built by build_index.py.

Output: data/intermediate/concept_evidence/{maths,science}.jsonl
  {"slug", "canonical_name", "grade", "area", "n_hits", "best_cosine",
   "evidence": "strong" | "weak" | "none",            # in the TAGGED grade
   "hits": [{"passage_id", "chapter", "section", "page", "cosine", "hybrid"}],
   "source_grade", "grade_delta", "context_evidence",  # where context comes from
   "fallback_best_cosine", "fallback_hits"}            # only when text was borrowed

Why: the graph says what each grade teaches, but nothing has ever checked that
against the books. The evidence label drives the audit (concepts with no
textbook support, passages no concept claims, prerequisites taught too late).

Grades in the graph are board-agnostic, so "no text in this grade" is a gap in the
corpus, not proof the tag is wrong. When the tagged grade has nothing solid, the
nearest grade that does is borrowed as generation context, and grade_delta records
how far off it is so the prompt can adjust the level ("this text is Grade 11; write
it for Grade 9"). The in-grade verdict is left untouched so the audit still reports
the real coverage gap.

Ranking uses the hybrid score, but the STRENGTH label uses raw cosine, because
hybrid scores are normalised per query and so the top hit always scores ~1.

Usage:
  python scripts/match_concepts.py --device cuda        # match everything
  python scripts/match_concepts.py --subject maths
  python scripts/match_concepts.py --calibrate          # show the score spread
"""

import argparse
import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build_index import Index, tokenize  # noqa: E402

BASE_DIR = Path(__file__).resolve().parent.parent
GRAPHS = {
    "maths": BASE_DIR / "data" / "knowledge_graph" / "maths" / "graph.json",
    "science": BASE_DIR / "data" / "knowledge_graph" / "science" / "graph.json",
}
OUT_DIR = BASE_DIR / "data" / "intermediate" / "concept_evidence"

# Science splits into separate books at grade 11; before that it is one book.
SCIENCE_SUBJECTS = ("science", "physics", "chemistry", "biology")
# Retrieval depth and the two caps that come out of it serve different jobs:
#   TOP_K       how deep to look. Was 8, which is far too shallow for a coverage
#               question: Grade 11 chemistry chapter 6 holds 130 passages and two
#               concepts, so at most 16 of them could ever be reached.
#   CONTEXT_K   how many candidates are kept for generation to choose among. It is a
#               shortlist, not the final context: build_context.py drops exercises,
#               caps two passages per section and keeps the best five. At 5 there was
#               nothing left to choose from once those filters ran.
#   COVERAGE_K  how many count as "this concept covers that passage" for the audit.
TOP_K = 30
CONTEXT_K = 12
COVERAGE_K = 30
STRONG_COSINE = 0.78          # calibrated below; see --calibrate
WEAK_COSINE = 0.70
# How far the fallback ladder may reach, and it is deliberately asymmetric. Text from a
# LOWER grade is always safe to build on — it is the same idea told more simply. Text from
# a higher grade assumes background the student does not have, and the further up, the less
# of it survives rewriting: "Physical Quantities" at Grade 9 borrowed Grade 11 dimensional
# analysis and offered [M L T^-2] as the source for a Grade 9 page.
MAX_DELTA_DOWN = 2
MAX_DELTA_UP = 1


def subjects_for(subject: str, concept: dict | None = None, grade: int = 0) -> tuple[str, ...]:
    """Which books a concept may be grounded in.

    Below grade 11 science is one book, so the whole family is fair game. From grade 11
    the books split, and a concept tagged chemistry should be grounded in the chemistry
    book: "States of Matter" at grade 11 was drawing anchors from grade 11 physics
    "MOLECULAR NATURE OF MATTER". The physics book is not wrong about matter, but it is
    not the book this page belongs to.
    """
    if subject == "maths":
        return ("maths",)
    stream = (concept or {}).get("subject")
    if grade >= 11 and stream in ("physics", "chemistry", "biology"):
        return (stream,)
    return SCIENCE_SUBJECTS


def query_variants(concept: dict) -> list[str]:
    """One query for the concept itself, plus one per alias.

    Each is scored separately and the best match wins, rather than concatenating
    them into a single query. Concatenation averages the embedding, so adding an
    alias drags the query away from its own meaning and can score *worse* — measured
    on the first 46 aliases, 19 of them got worse that way. Scored separately an
    alias can only help: if it matches better it wins, if not the original stands.

    The aliases carry the words the book uses instead of the concept's name —
    "Finding the Unknown" for Linear Equations in One Variable, "Pressure Exerted by
    Air" for Atmospheric Pressure.
    """
    name = concept["canonical_name"]
    base = f"{name}. {concept['description']}" if concept.get("description") else name
    return [base] + [f"{name}. {alias}" for alias in concept.get("aliases", [])]


def query_for(concept: dict) -> str:
    """The single best-effort query, for callers that want just one (e.g. --calibrate)."""
    return query_variants(concept)[0]


def label_for(best_cosine: float) -> str:
    return ("strong" if best_cosine >= STRONG_COSINE
            else "weak" if best_cosine >= WEAK_COSINE else "none")


class Matcher:
    def __init__(self, device: str) -> None:
        self.index = Index(device)
        self.by_key: dict[tuple[int, str], np.ndarray] = {}
        for i, p in enumerate(self.index.passages):
            self.by_key.setdefault((p["grade"], p["subject"]), []).append(i)
        self.by_key = {k: np.array(v) for k, v in self.by_key.items()}
        self.grades = sorted({p["grade"] for p in self.index.passages})

    def candidates(self, grade: int, subjects: tuple[str, ...]) -> np.ndarray:
        idx = [self.by_key.get((grade, s)) for s in subjects]
        idx = [a for a in idx if a is not None and a.size]
        return np.concatenate(idx) if idx else np.array([], dtype=int)

    def prepare(self, queries: str | list[str]) -> tuple[np.ndarray, np.ndarray]:
        """Encode every query variant and score each lexically, keeping the best.

        Both results cover the whole corpus and do not depend on the grade, so they
        are reusable across every grade the fallback ladder may visit and every grade
        the concept is tagged to. Taking the max over variants means an alias that
        matches nothing simply never wins.
        """
        if isinstance(queries, str):
            queries = [queries]
        qvecs = self.index.model.encode(
            queries, normalize_embeddings=True, convert_to_numpy=True,
            show_progress_bar=False,
        ).astype("float32")
        lexical = np.vstack([
            np.asarray(self.index.bm25.get_scores(tokenize(q)), dtype="float32")
            for q in queries
        ])
        return qvecs, lexical.max(axis=0)

    def score(self, pool: np.ndarray, qvecs: np.ndarray, lexical_all: np.ndarray) -> list[dict]:
        if pool.size == 0:
            return []
        cosine = (self.index.vectors[pool] @ qvecs.T).max(axis=1)
        lexical = lexical_all[pool]

        def norm(x: np.ndarray) -> np.ndarray:
            lo, hi = float(x.min()), float(x.max())
            return (x - lo) / (hi - lo + 1e-9)

        hybrid = 0.4 * norm(lexical) + 0.6 * norm(cosine)
        order = np.argsort(-hybrid)[:TOP_K]

        hits = []
        for j in order:
            p = self.index.passages[pool[j]]
            hits.append({
                "passage_id": p["id"], "chapter": p["chapter"], "section": p["section"],
                "page": p["page"], "kind": p["kind"],
                "cosine": round(float(cosine[j]), 4), "hybrid": round(float(hybrid[j]), 4),
            })
        return hits

    def match(self, concept: dict, grade: int, subjects: tuple[str, ...]) -> list[dict]:
        qvecs, lexical_all = self.prepare(query_variants(concept))
        return self.score(self.candidates(grade, subjects), qvecs, lexical_all)

    def borrow(self, grade: int, subject: str, concept: dict, qvecs: np.ndarray,
               lexical_all: np.ndarray) -> tuple[int, float, list[dict]] | None:
        """Find another grade whose text can serve as context for this one.

        A strongly supported grade wins first, then the nearest one — text that actually
        explains the topic two years away beats text that barely mentions it one year
        away, and MAX_GRADE_DELTA already bounds how far this can reach.

        Two limits keep the borrowed text usable:
          * bounded by MAX_DELTA_DOWN / MAX_DELTA_UP — rewriting Grade 11 dimensional
            analysis for Grade 9 is writing from scratch, and the passage only misleads
          * only explanatory prose qualifies a grade. Exercises score well on topic
            words while being a list of questions, so they cannot ground an explanation.

        The book family is resolved per candidate grade: a grade 11 chemistry concept
        borrowing downwards must look in grade 10 "science", because the chemistry book
        does not exist below grade 11.
        """
        scored = []
        for g in self.grades:
            if g == grade or not (-MAX_DELTA_DOWN <= g - grade <= MAX_DELTA_UP):
                continue
            hits = self.score(self.candidates(g, subjects_for(subject, concept, g)),
                              qvecs, lexical_all)
            prose = [h for h in hits if h["kind"] == "text"]
            best = max((h["cosine"] for h in prose), default=0.0)
            if best >= WEAK_COSINE:
                ranked = prose + [h for h in hits if h["kind"] != "text"]
                scored.append((label_for(best) != "strong", abs(g - grade), -best, g,
                               best, ranked))
        if not scored:
            return None
        _, _, _, g, best, hits = min(scored)
        return g, best, hits


def run(subject: str, device: str) -> None:
    graph = json.loads(GRAPHS[subject].read_text(encoding="utf-8"))
    matcher = Matcher(device)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUT_DIR / f"{subject}.jsonl"

    counts = {"strong": 0, "weak": 0, "none": 0}          # evidence in the tagged grade
    ctx_counts = {"strong": 0, "weak": 0, "none": 0}      # after borrowing
    deltas: Counter[int] = Counter()
    n_pairs = sum(len(c["grades"]) for c in graph["concepts"].values())

    with out_path.open("w", encoding="utf-8") as f:
        done = 0
        for slug, concept in graph["concepts"].items():
            # one encode + one BM25 pass serves every grade of this concept
            qvecs, lexical_all = matcher.prepare(query_variants(concept))
            for grade in concept["grades"]:
                # the stream split only exists from grade 11, so this is per grade
                subjects = subjects_for(subject, concept, grade)
                hits = matcher.score(matcher.candidates(grade, subjects), qvecs, lexical_all)
                # Judge the grade on its EXPLANATION, the same rule borrow() uses. An
                # exercise scores well on topic words while teaching nothing: Solar
                # Eclipse's best in-grade score came from a "Let Us Enhance Our Learning"
                # block, which would have labelled the grade strong on a question set.
                prose = [h for h in hits if h["kind"] == "text"]
                best = max((h["cosine"] for h in prose or hits), default=0.0)
                label = label_for(best)
                counts[label] += 1

                # Nothing solid in this grade? Borrow from the nearest grade that has it.
                source_grade, delta, fallback = grade, 0, None
                if label != "strong":
                    fallback = matcher.borrow(grade, subject, concept, qvecs, lexical_all)
                    if fallback and fallback[1] > best:
                        source_grade, best_ctx, fb_hits = fallback
                        delta = source_grade - grade
                    else:
                        fallback = None

                ctx_label = label_for(fallback[1]) if fallback else label
                ctx_counts[ctx_label] += 1
                deltas[delta] += 1

                # Prose first, then the rest. The shortlist is capped at CONTEXT_K and
                # build_context drops non-prose afterwards, so ordering by kind here is
                # what stops exercises and summaries from eating the budget: of 4,402
                # shortlisted maths hits, 995 were exercises and 409 summaries, leaving
                # over half of in-grade prompts with fewer than five anchors.
                solid = [h for h in hits if h["cosine"] >= WEAK_COSINE]
                solid.sort(key=lambda h: (h["kind"] != "text", -h["cosine"]))
                rec = {
                    "slug": slug, "canonical_name": concept["canonical_name"], "grade": grade,
                    "area": concept.get("area", ""), "n_hits": len(hits),
                    "best_cosine": round(best, 4), "evidence": label,
                    "hits": solid[:CONTEXT_K],
                    # Every passage this concept reaches, ids only. The audit asks which
                    # book text nothing covers, and answering that from the handful of
                    # context passages made whole chapters look unclaimed.
                    "covers": [h["passage_id"] for h in solid[:COVERAGE_K]],
                    # where the generation context should come from, and how far off it is
                    "source_grade": source_grade, "grade_delta": delta,
                    "context_evidence": ctx_label,
                }
                if fallback:
                    rec["fallback_best_cosine"] = round(fallback[1], 4)
                    rec["fallback_hits"] = [h for h in fallback[2]
                                            if h["cosine"] >= WEAK_COSINE][:CONTEXT_K]
                f.write(json.dumps(rec, ensure_ascii=False) + "\n")

                done += 1
                if done % 100 == 0:
                    print(f"  {done}/{n_pairs} pairs", flush=True)

    borrowed = n_pairs - deltas[0]
    print(f"{subject}: {n_pairs} concept-grade pairs")
    print(f"  in tagged grade : {counts['strong']} strong, {counts['weak']} weak, "
          f"{counts['none']} none")
    print(f"  after borrowing : {ctx_counts['strong']} strong, {ctx_counts['weak']} weak, "
          f"{ctx_counts['none']} none   ({borrowed} borrowed)")
    spread = ", ".join(f"{d:+d}: {n}" for d, n in sorted(deltas.items()) if d)
    print(f"  grade_delta     : {spread or 'none'}")
    print(f"written to {out_path.relative_to(BASE_DIR).as_posix()}")


def all_grades(subject: str, device: str) -> None:
    """Score every concept against every grade, so the audit can spot wrong grade tags.

    Embeddings only (no BM25): one batch encode, then a matrix product per grade.
    """
    graph = json.loads(GRAPHS[subject].read_text(encoding="utf-8"))
    matcher = Matcher(device)
    subjects = subjects_for(subject)
    slugs = list(graph["concepts"])
    queries = [query_for(graph["concepts"][s]) for s in slugs]

    print(f"{subject}: scoring {len(slugs)} concepts against every grade …")
    qvecs = matcher.index.model.encode(
        queries, batch_size=64, normalize_embeddings=True,
        convert_to_numpy=True, show_progress_bar=False,
    ).astype("float32")

    grades = sorted({p["grade"] for p in matcher.index.passages})
    matrix: dict[str, dict[str, float]] = {s: {} for s in slugs}
    for grade in grades:
        pool = matcher.candidates(grade, subjects)
        if pool.size == 0:
            continue
        best = (matcher.index.vectors[pool] @ qvecs.T).max(axis=0)   # best passage per concept
        for slug, score in zip(slugs, best):
            matrix[slug][str(grade)] = round(float(score), 4)

    out = OUT_DIR / f"{subject}_grades.json"
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(matrix, indent=1), encoding="utf-8")
    print(f"written to {out.relative_to(BASE_DIR).as_posix()}")


def calibrate(device: str) -> None:
    """Print the cosine spread for known-good and known-bad pairs to sanity-check thresholds."""
    matcher = Matcher(device)
    good = [
        ({"canonical_name": "Quadratic Equations", "description": "Standard form ax²+bx+c=0"}, 10, ("maths",)),
        ({"canonical_name": "Photosynthesis", "description": "How green plants make food using sunlight"}, 10, SCIENCE_SUBJECTS),
        ({"canonical_name": "Heron's Formula", "description": "Area of a triangle from its three sides"}, 9, ("maths",)),
    ]
    bad = [
        ({"canonical_name": "Linear Programming", "description": "Optimising a linear objective under constraints"}, 6, ("maths",)),
        ({"canonical_name": "Genetic Engineering", "description": "Recombinant DNA technology"}, 6, SCIENCE_SUBJECTS),
    ]
    for label, cases in (("should match", good), ("should NOT match", bad)):
        print(f"\n{label}:")
        for concept, grade, subjects in cases:
            hits = matcher.match(concept, grade, subjects)
            top = hits[0] if hits else None
            print(f"  {concept['canonical_name']:22} gr{grade}  best cosine "
                  f"{top['cosine'] if top else 0:.3f}  -> {top['section'][:40] if top else 'no hits'!r}")


def main() -> None:
    p = argparse.ArgumentParser(description="Match graph concepts to textbook passages")
    p.add_argument("--subject", choices=list(GRAPHS), help="default: both")
    p.add_argument("--device", default="cuda")
    p.add_argument("--calibrate", action="store_true")
    p.add_argument("--all-grades", action="store_true",
                   help="also score every concept against every grade (for the audit)")
    args = p.parse_args()

    if args.calibrate:
        calibrate(args.device)
        return
    for subject in ([args.subject] if args.subject else list(GRAPHS)):
        if args.all_grades:
            all_grades(subject, args.device)
        else:
            run(subject, args.device)


if __name__ == "__main__":
    main()
