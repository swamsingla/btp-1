#!/usr/bin/env python3
"""
Graph-RAG Context Assembler  (Approach B)
==========================================
For each (concept × grade) pair in the knowledge graph, gathers contextual
information from three sources:

  1. Knowledge Graph structure  — prerequisites, leads_to, related, same-area
  2. NCERT textbook chunks      — fuzzy-matched from parsed PDFs
  3. Wikipedia summaries        — fetched in parallel via REST API (optional)

Produces a content plan JSON per (concept, grade) that feeds into generate.py.

Output: data/content_plans/{concept_slug}_grade{N}.json

Usage:
  python graph_rag.py                       # build ALL plans (with Wikipedia)
  python graph_rag.py --grade 6             # one grade
  python graph_rag.py --concept fractions   # one concept
  python graph_rag.py --no-wiki            # skip Wikipedia (fast, offline)
  python graph_rag.py --check-coverage     # verify all plans exist
  python graph_rag.py --workers 16         # parallel Wikipedia threads (default 12)
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path
from typing import Any

import requests
from thefuzz import fuzz

# ─── Paths ────────────────────────────────────────────────────────────────────
BASE_DIR   = Path(__file__).resolve().parent.parent.parent
GRAPH_PATH = BASE_DIR / "webapp" / "public" / "maths_v2.json"
CHUNKS_DIR = BASE_DIR / "data" / "intermediate" / "chunks"
OUTPUT_DIR = BASE_DIR / "data" / "content_plans"

# ─── Config ───────────────────────────────────────────────────────────────────
FUZZY_THRESHOLD      = 62    # Min similarity for NCERT chunk match
MAX_CHUNKS           = 5     # Max NCERT chunks per concept
MAX_CONTEXT_CHARS    = 5500  # Hard cap on context_summary
WIKI_MAX_CHARS       = 2500  # Max Wikipedia text per concept
DEFAULT_WIKI_WORKERS = 12    # Parallel Wikipedia fetches

# ─── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger("graph_rag")


# ══════════════════════════════════════════════════════════════════════════════
# 1.  Knowledge Graph
# ══════════════════════════════════════════════════════════════════════════════

def load_graph(path: Path | None = None) -> dict:
    p = path or GRAPH_PATH
    if not p.exists():
        log.error("Graph not found: %s", p)
        sys.exit(1)
    return json.loads(p.read_text(encoding="utf-8"))


def gather_graph_context(slug: str, grade: int, concepts: dict) -> dict:
    """Extract structured context from knowledge graph edges for one concept."""
    concept = concepts.get(slug, {})

    def _resolve(slugs: list[str], limit: int = 8) -> list[dict]:
        out = []
        for s in slugs[:limit]:
            c = concepts.get(s)
            if c:
                out.append({
                    "slug": s,
                    "name": c["canonical_name"],
                    "description": c.get("description", ""),
                    "area": c.get("area", ""),
                    "grades": c.get("grades", []),
                })
        return out

    prereqs   = _resolve(concept.get("prerequisites", []))
    leads_to  = _resolve(concept.get("leads_to",      []))
    related   = _resolve(concept.get("related",       []), 6)

    # Same-area peers at same grade (for see-also)
    area = concept.get("area", "")
    same_area = [
        {"slug": s, "name": c["canonical_name"]}
        for s, c in concepts.items()
        if s != slug and c.get("area") == area and grade in c.get("grades", [])
    ][:8]

    return {
        "prerequisites": prereqs,
        "leads_to":      leads_to,
        "related":       related,
        "same_area":     same_area,
    }


# ══════════════════════════════════════════════════════════════════════════════
# 2.  NCERT Chunk Search
# ══════════════════════════════════════════════════════════════════════════════

# Module-level chunk cache: grade → list[dict]
_chunk_cache: dict[int, list[dict]] = {}


def _load_chunks_for_grade(grade: int) -> list[dict]:
    """Load all maths chunks for a grade, using _all_chunks.json when available."""
    if grade in _chunk_cache:
        return _chunk_cache[grade]

    chunks: list[dict] = []
    grade_dir = CHUNKS_DIR / f"grade{grade}" / "maths"
    if not grade_dir.exists():
        grade_dir = CHUNKS_DIR / f"grade{grade}"
    if not grade_dir.exists():
        _chunk_cache[grade] = chunks
        return chunks

    for root, _dirs, files in os.walk(str(grade_dir)):
        # Prefer _all_chunks.json (contains all topics for a chapter in one file)
        if "_all_chunks.json" in files:
            try:
                raw = json.loads(
                    (Path(root) / "_all_chunks.json").read_text(encoding="utf-8")
                )
                if isinstance(raw, list):
                    chunks.extend(raw)
                elif isinstance(raw, dict):
                    # Some files are wrapped: {"chunks": [...]}
                    chunks.extend(raw.get("chunks", [raw]))
                continue            # skip individual topic files in this dir
            except Exception:
                pass
        for fname in sorted(files):
            if fname.endswith(".json") and not fname.startswith("_"):
                try:
                    raw = json.loads(
                        (Path(root) / fname).read_text(encoding="utf-8")
                    )
                    if isinstance(raw, dict):
                        chunks.append(raw)
                    elif isinstance(raw, list):
                        chunks.extend(raw)
                except Exception:
                    pass

    log.debug("Loaded %d chunks for grade %d", len(chunks), grade)
    _chunk_cache[grade] = chunks
    return chunks


def find_relevant_chunks(concept_name: str, grade: int) -> list[dict]:
    """Fuzzy-match NCERT chunks against concept_name for a given grade."""
    chunks = _load_chunks_for_grade(grade)
    if not chunks:
        return []

    scored: list[tuple[int, dict]] = []
    for chunk in chunks:
        topic   = (chunk.get("topic_title") or chunk.get("title") or "").strip()
        chapter = (chunk.get("chapter_title") or "").strip()
        content = (chunk.get("content") or chunk.get("text") or "").strip()

        title_score = max(
            fuzz.token_sort_ratio(concept_name.lower(), topic.lower()),
            fuzz.token_sort_ratio(concept_name.lower(), chapter.lower()),
        )
        bonus = 20 if concept_name.lower() in content.lower() else 0
        total = title_score + bonus

        if total >= FUZZY_THRESHOLD:
            scored.append((total, chunk))

    scored.sort(key=lambda x: -x[0])
    seen: set[int] = set()
    result: list[dict] = []
    for _, chunk in scored:
        content = (chunk.get("content") or chunk.get("text") or "")
        h = hash(content[:200])
        if h not in seen:
            seen.add(h)
            result.append(chunk)
        if len(result) >= MAX_CHUNKS:
            break
    return result


def chunks_to_text(chunks: list[dict], grade: int) -> tuple[str, list[str]]:
    """Convert matched chunks into a text block + source references."""
    ncert_text = ""
    ncert_refs: list[str] = []
    for chunk in chunks:
        topic   = chunk.get("topic_title") or chunk.get("title") or ""
        ch_num  = chunk.get("chapter_number") or ""
        content = (chunk.get("content") or chunk.get("text") or "")[:1000]
        ncert_refs.append(f"ncert:grade{grade}/maths/ch{ch_num}")
        ncert_text += f"\n[NCERT Grade{grade} Ch{ch_num} — {topic}]\n{content}\n"
    return ncert_text, ncert_refs


# ══════════════════════════════════════════════════════════════════════════════
# 3.  Wikipedia  (with parallel fetching)
# ══════════════════════════════════════════════════════════════════════════════

_WIKI_API    = "https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
_WIKI_SEARCH = "https://en.wikipedia.org/w/api.php"
_HEADERS     = {"User-Agent": "ncert-learn-bot/1.0"}


def fetch_wikipedia(concept_name: str, timeout: int = 8) -> str:
    """Fetch a concise Wikipedia summary. Returns empty string on failure."""
    def _get_summary(title: str) -> str:
        try:
            r = requests.get(_WIKI_API.format(title=title.replace(" ", "_")),
                             timeout=timeout, headers=_HEADERS)
            if r.status_code == 200:
                text = r.json().get("extract", "")
                if len(text) > 100:
                    return text[:WIKI_MAX_CHARS]
        except requests.RequestException:
            pass
        return ""

    def _search_and_get(query: str) -> str:
        try:
            params = {
                "action": "query", "list": "search",
                "srsearch": query, "format": "json", "srlimit": 1,
            }
            r = requests.get(_WIKI_SEARCH, params=params, timeout=timeout, headers=_HEADERS)
            if r.status_code == 200:
                results = r.json().get("query", {}).get("search", [])
                if results:
                    return _get_summary(results[0]["title"])
        except requests.RequestException:
            pass
        return ""

    # Try 1: exact title
    text = _get_summary(concept_name)
    if text:
        return text

    # Try 2: search with "mathematics" qualifier
    text = _search_and_get(concept_name + " mathematics")
    if text:
        return text

    # Try 3: search without qualifier (shorter concepts like "Angles", "Fractions")
    if len(concept_name.split()) <= 3:
        text = _search_and_get(concept_name)
        if text:
            return text

    return ""


def prefetch_wikipedia_parallel(
    concept_names: list[str],
    workers: int = DEFAULT_WIKI_WORKERS,
) -> dict[str, str]:
    """
    Fetch Wikipedia summaries for all concept_names in parallel.
    Returns {canonical_name: wiki_text}.
    """
    results: dict[str, str] = {}
    log.info("Fetching Wikipedia for %d concepts with %d workers …",
             len(concept_names), workers)
    with ThreadPoolExecutor(max_workers=workers) as pool:
        future_to_name = {pool.submit(fetch_wikipedia, name): name
                          for name in concept_names}
        done = 0
        for future in as_completed(future_to_name):
            name = future_to_name[future]
            try:
                results[name] = future.result()
            except Exception:
                results[name] = ""
            done += 1
            if done % 50 == 0:
                log.info("  Wikipedia: %d/%d fetched", done, len(concept_names))
    found = sum(1 for v in results.values() if v)
    log.info("Wikipedia done: %d/%d had content", found, len(concept_names))
    return results


# ══════════════════════════════════════════════════════════════════════════════
# 4.  Page-depth / structure planning
# ══════════════════════════════════════════════════════════════════════════════

def _grade_note(grade: int) -> str:
    if grade <= 7:
        return (
            "Very basic introduction. Use everyday examples, colourful analogies, "
            "simple language. Avoid formal proofs. Target: Class 6-7 student."
        )
    if grade <= 9:
        return (
            "Qualitative and semi-quantitative. Use simple numericals and diagrams. "
            "Minimal calculus. Target: Class 8-9 student."
        )
    if grade == 10:
        return (
            "Full conceptual and numerical treatment at CBSE Board-exam level. "
            "No calculus. Target: Class 10 student."
        )
    return (
        "Full mathematical rigour. Include proofs where standard. "
        "JEE-level depth where appropriate. Target: Class 11-12 student."
    )


def _determine_depth(concept: dict, grade: int) -> tuple[str, int, list[str]]:
    """Returns (page_depth, target_words, sections)."""
    n_prereqs  = len(concept.get("prerequisites", []))
    n_leads_to = len(concept.get("leads_to",      []))
    total_links = n_prereqs + n_leads_to

    if total_links >= 6:
        return "deep-dive", 1500, [
            "Lead", "Background", "Explanation",
            "Mathematical Formulation", "Worked Examples",
            "Applications", "Common Mistakes", "See Also",
        ]
    if total_links >= 3:
        return "standard", 1100, [
            "Lead", "Explanation", "Mathematical Formulation",
            "Worked Examples", "Applications", "See Also",
        ]
    return "standard", 800, [
        "Lead", "Explanation", "Worked Examples", "See Also",
    ]


# ══════════════════════════════════════════════════════════════════════════════
# 5.  Build one content plan
# ══════════════════════════════════════════════════════════════════════════════

def build_plan(
    slug: str,
    concept: dict,
    grade: int,
    concepts: dict,
    wiki_cache: dict[str, str],
) -> dict:
    canonical_name = concept["canonical_name"]

    # Graph-RAG context
    gctx = gather_graph_context(slug, grade, concepts)

    # NCERT chunks
    matched_chunks = find_relevant_chunks(canonical_name, grade)
    ncert_text, ncert_refs = chunks_to_text(matched_chunks, grade)

    # Wikipedia (from pre-fetched cache)
    wiki_text = wiki_cache.get(canonical_name, "")

    # Combine into context_summary
    parts: list[str] = []
    if ncert_text.strip():
        parts.append(ncert_text.strip())
    if wiki_text.strip():
        parts.append(f"[Wikipedia]\n{wiki_text.strip()}")

    if parts:
        context_summary = "\n\n".join(parts)
    else:
        context_summary = (
            f"No external source material found. Generate based on NCERT "
            f"curriculum knowledge for Grade {grade} Mathematics."
        )
    if len(context_summary) > MAX_CONTEXT_CHARS:
        context_summary = context_summary[:MAX_CONTEXT_CHARS] + "\n[…truncated]"

    sources = ncert_refs.copy()
    if wiki_text:
        sources.append("wikipedia")

    # Page structure
    depth, target_words, sections = _determine_depth(concept, grade)
    if grade <= 8:
        target_words = min(target_words, 900)
        sections = [s for s in sections
                    if s not in ("Mathematical Formulation", "Background")]

    # Deduplicated see-also list
    see_also = list(dict.fromkeys(
        [p["name"] for p in gctx["prerequisites"]]
        + [s["name"] for s in gctx["leads_to"]]
        + [r["name"] for r in gctx["related"]]
        + [a["name"] for a in gctx["same_area"]]
    ))

    return {
        "concept_slug":               slug,
        "canonical_name":             canonical_name,
        "subject":                    "maths",
        "grade":                      grade,
        "area":                       concept.get("area", ""),
        "description":                concept.get("description", ""),
        "page_depth":                 depth,
        "target_words":               target_words,
        "context_summary":            context_summary,
        "context_sources":            sources,
        "ncert_chunks_found":         len(matched_chunks),
        "wiki_found":                 bool(wiki_text),
        # Links for generator prompts
        "prerequisites_to_link":      [p["name"] for p in gctx["prerequisites"]],
        "prerequisites_descriptions": {p["name"]: p["description"]
                                       for p in gctx["prerequisites"]},
        "successors_to_link":         [s["name"] for s in gctx["leads_to"]],
        "related_to_link":            [r["name"] for r in gctx["related"]],
        "see_also":                   see_also[:16],
        "sections":                   sections,
        "grade_note":                 _grade_note(grade),
        "aliases":                    concept.get("aliases", []),
    }


# ══════════════════════════════════════════════════════════════════════════════
# 6.  Batch runner
# ══════════════════════════════════════════════════════════════════════════════

def collect_tasks(
    graph: dict,
    grade_filter: int | None,
    slug_filter: str | None,
    skip_existing: bool,
) -> list[tuple[str, dict, int]]:
    """Return (slug, concept, grade) triples that need plans."""
    tasks = []
    for slug, concept in graph.get("concepts", {}).items():
        if slug_filter and slug_filter not in slug:
            continue
        for grade in concept.get("grades", []):
            if grade_filter is not None and grade != grade_filter:
                continue
            out_path = OUTPUT_DIR / f"{slug}_grade{grade}.json"
            if skip_existing and out_path.exists():
                continue
            tasks.append((slug, concept, grade))
    return tasks


def run(
    graph: dict,
    *,
    grade_filter: int | None   = None,
    slug_filter:  str | None   = None,
    skip_existing: bool        = True,
    use_wiki: bool             = True,
    wiki_workers: int          = DEFAULT_WIKI_WORKERS,
) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    concepts = graph.get("concepts", {})

    tasks = collect_tasks(graph, grade_filter, slug_filter, skip_existing)
    if not tasks:
        log.info("Nothing to do (all plans exist or no matching concepts).")
        return

    log.info("Building plans for %d (concept, grade) pairs …", len(tasks))

    # Pre-fetch Wikipedia in parallel for all unique concept names
    wiki_cache: dict[str, str] = {}
    if use_wiki:
        unique_names = list({concept["canonical_name"]
                             for _, concept, _ in tasks})
        wiki_cache = prefetch_wikipedia_parallel(unique_names, wiki_workers)

    # Build plans sequentially (fast — no network after Wikipedia pre-fetch)
    created = 0
    failed  = 0
    t0 = time.time()
    for i, (slug, concept, grade) in enumerate(tasks, 1):
        try:
            plan = build_plan(slug, concept, grade, concepts, wiki_cache)
            out_path = OUTPUT_DIR / f"{slug}_grade{grade}.json"
            out_path.write_text(
                json.dumps(plan, ensure_ascii=False, indent=2),
                encoding="utf-8",
            )
            created += 1
        except Exception as exc:
            log.error("Failed %s grade%d: %s", slug, grade, exc)
            failed += 1

        if i % 50 == 0:
            elapsed = time.time() - t0
            log.info("  Progress: %d/%d plans (%.0fs elapsed)", i, len(tasks), elapsed)

    elapsed = time.time() - t0
    log.info("═" * 60)
    log.info("Planning complete in %.1fs:", elapsed)
    log.info("  Created : %d", created)
    log.info("  Failed  : %d", failed)
    log.info("  Skipped : %d (already existed)",
             len(list(graph.get("concepts", {}).items())) - len(tasks))
    log.info("  Output  : %s", OUTPUT_DIR)


def check_coverage(graph: dict) -> None:
    """Verify every (concept, grade) has a content plan."""
    concepts = graph.get("concepts", {})
    missing: list[str] = []
    for slug, concept in concepts.items():
        for grade in concept.get("grades", []):
            if not (OUTPUT_DIR / f"{slug}_grade{grade}.json").exists():
                missing.append(f"{slug}_grade{grade}")
    total = sum(len(c.get("grades", [])) for c in concepts.values())
    if missing:
        log.warning("Missing plans (%d / %d):", len(missing), total)
        for m in missing[:20]:
            log.warning("  %s", m)
        if len(missing) > 20:
            log.warning("  … and %d more", len(missing) - 20)
    else:
        log.info("Coverage ✓  — all %d (concept, grade) pairs have plans", total)


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def main() -> None:
    p = argparse.ArgumentParser(
        description="Graph-RAG Content Planner — KG + NCERT chunks + Wikipedia",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    p.add_argument("--grade",    type=int, help="Process only this grade")
    p.add_argument("--concept",  help="Concept slug (partial match)")
    p.add_argument("--graph",    default=str(GRAPH_PATH))
    p.add_argument("--skip-existing", action="store_true", default=True)
    p.add_argument("--no-skip-existing", dest="skip_existing", action="store_false")
    p.add_argument("--no-wiki",  action="store_true", help="Skip Wikipedia")
    p.add_argument("--workers",  type=int, default=DEFAULT_WIKI_WORKERS,
                   help="Parallel Wikipedia fetch threads")
    p.add_argument("--check-coverage", action="store_true")
    args = p.parse_args()

    graph = load_graph(Path(args.graph))
    log.info("Loaded graph: %d concepts, %d edges",
             graph.get("total_concepts", 0), graph.get("total_edges", 0))

    if args.check_coverage:
        check_coverage(graph)
        return

    run(
        graph,
        grade_filter  = args.grade,
        slug_filter   = args.concept,
        skip_existing = args.skip_existing,
        use_wiki      = not args.no_wiki,
        wiki_workers  = args.workers,
    )


if __name__ == "__main__":
    main()
