#!/usr/bin/env python3
"""
Stage 3 — Content Planner
==========================
For each (concept × grade) pair in the knowledge graph, assembles a focused
content plan that will drive the final Wikipedia-style page generation.

Three-pronged context assembly:
  1. NCERT chunks  — fuzzy-match concept against existing parsed chunk files
  2. Wikipedia     — fetch the Wikipedia article for the concept (web)
  3. LLM summary   — if too much raw text, compress with LLM to fit token budget

Output: data/content_plans/{concept_slug}_grade{N}.json

Schema:
{
  "concept_slug": "newtons-first-law-of-motion",
  "canonical_name": "Newton's First Law of Motion",
  "subject": "physics",
  "grade": 9,
  "page_depth": "standard",        # "overview" | "standard" | "deep-dive"
  "target_words": 1200,
  "context_summary": "...",         # max ~3000 chars of reference material
  "context_sources": ["ncert:grade9/science/chapter9", "wikipedia"],
  "prerequisites_to_link": ["force-and-motion"],
  "successors_to_link": ["newtons-second-law-of-motion"],
  "related_to_link": ["friction"],
  "sections": ["Lead", "Explanation", "Mathematical Formulation", "Examples", "See Also"],
  "grade_note": "Semi-quantitative. Simple numericals, no calculus."
}
"""

import argparse
import json
import logging
import os
import re
import sys
from pathlib import Path
from typing import Any

import requests
from bs4 import BeautifulSoup
from thefuzz import fuzz

# Local LLaMA-8B inference (Stage 3 uses local model per implementation plan)
from llm_local import llm_call as _local_llm_call

# ─── Paths ───────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
GRAPH_PATH = BASE_DIR / "data" / "knowledge_graph" / "graph.json"
CHUNKS_DIR = BASE_DIR / "data" / "intermediate" / "chunks"
OUTPUT_DIR = BASE_DIR / "data" / "content_plans"

# ─── Config ───────────────────────────────────────────────────────────────────
FUZZY_THRESHOLD = 70          # Minimum similarity to consider a chunk relevant
MAX_CHUNKS_PER_CONCEPT = 5    # Max NCERT chunks to include
MAX_CONTEXT_CHARS = 4000      # Hard cap on context_summary length
WIKI_MAX_CHARS = 3000         # Max Wikipedia text to include per concept

# ─── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ─── LLM helpers ─────────────────────────────────────────────────────────────
# Stage 3 uses local LLaMA-8B (implementation plan).

def llm_call(
    system: str,
    user: str,
    temperature: float = 0.2,
    max_new_tokens: int = 2048,
) -> str:
    """Thin wrapper around the local LLaMA-8B inference."""
    return _local_llm_call(system=system, user=user,
                           temperature=temperature, max_new_tokens=max_new_tokens)


def extract_json_from_text(text: str) -> Any:
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    fence = re.search(r"```(?:json)?\s*([\s\S]+?)\s*```", text)
    if fence:
        try:
            return json.loads(fence.group(1))
        except json.JSONDecodeError:
            pass
    for s, e in [("{", "}"), ("[", "]")]:
        si, ei = text.find(s), text.rfind(e)
        if si != -1 and ei > si:
            try:
                return json.loads(text[si : ei + 1])
            except json.JSONDecodeError:
                pass
    raise ValueError("Could not extract JSON")


# ─── NCERT chunk search ───────────────────────────────────────────────────────

def _load_all_chunks(subject: str, grade: int) -> list[dict]:
    """Load all chunk JSON files for a given subject + grade."""
    chunks: list[dict] = []

    # Direct subject path (e.g. chunks/grade9/science/)
    subject_dir = CHUNKS_DIR / f"grade{grade}" / subject
    if subject_dir.exists():
        for chapter_dir in subject_dir.iterdir():
            if chapter_dir.is_dir():
                for chunk_file in sorted(chapter_dir.glob("*.json")):
                    try:
                        chunks.append(json.loads(chunk_file.read_text()))
                    except Exception:
                        pass

    # Also check "science" for physics/chemistry/biology at grades ≤10
    if subject in ("physics", "chemistry", "biology") and grade <= 10:
        sci_dir = CHUNKS_DIR / f"grade{grade}" / "science"
        if sci_dir.exists():
            for chapter_dir in sci_dir.iterdir():
                if chapter_dir.is_dir():
                    for chunk_file in sorted(chapter_dir.glob("*.json")):
                        try:
                            chunks.append(json.loads(chunk_file.read_text()))
                        except Exception:
                            pass

    return chunks


def find_relevant_ncert_chunks(
    concept_name: str,
    subject: str,
    grade: int,
) -> list[dict]:
    """
    Find the most relevant NCERT chunks for a concept using fuzzy matching.
    Returns up to MAX_CHUNKS_PER_CONCEPT chunks sorted by relevance.
    """
    chunks = _load_all_chunks(subject, grade)
    if not chunks:
        return []

    scored: list[tuple[int, dict]] = []
    for chunk in chunks:
        topic_title = chunk.get("topic_title", "")
        chapter_title = chunk.get("chapter_title", "")
        content = chunk.get("content", "")

        # Score by title similarity + content mention
        title_score = max(
            fuzz.token_sort_ratio(concept_name.lower(), topic_title.lower()),
            fuzz.token_sort_ratio(concept_name.lower(), chapter_title.lower()),
        )
        # Bonus if concept name appears literally in content
        content_bonus = 20 if concept_name.lower() in content.lower() else 0
        total_score = title_score + content_bonus

        if total_score >= FUZZY_THRESHOLD:
            scored.append((total_score, chunk))

    # Sort descending by score, deduplicate by content hash
    scored.sort(key=lambda x: -x[0])
    seen_content: set[int] = set()
    result: list[dict] = []
    for _score, chunk in scored:
        content_hash = hash(chunk.get("content", "")[:200])
        if content_hash not in seen_content:
            seen_content.add(content_hash)
            result.append(chunk)
        if len(result) >= MAX_CHUNKS_PER_CONCEPT:
            break

    return result


# ─── Wikipedia fetcher ────────────────────────────────────────────────────────

WIKI_API = "https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
WIKI_SEARCH = "https://en.wikipedia.org/w/api.php"

def fetch_wikipedia_content(concept_name: str, timeout: int = 10) -> tuple[str, str]:
    """
    Fetch a Wikipedia article for the concept.
    Returns (text, url) — text is truncated to WIKI_MAX_CHARS.
    """
    # Try direct title first
    slug = concept_name.replace(" ", "_")
    url = WIKI_API.format(title=slug)
    try:
        resp = requests.get(url, timeout=timeout, headers={"User-Agent": "ncert-learn-bot/1.0"})
        if resp.status_code == 200:
            data = resp.json()
            extract = data.get("extract", "")
            page_url = data.get("content_urls", {}).get("desktop", {}).get("page", "")
            if extract:
                return extract[:WIKI_MAX_CHARS], page_url
    except requests.RequestException:
        pass

    # Fallback: Wikipedia search API
    try:
        params = {
            "action": "query",
            "list": "search",
            "srsearch": concept_name,
            "format": "json",
            "srlimit": 3,
        }
        resp = requests.get(
            WIKI_SEARCH, params=params, timeout=timeout,
            headers={"User-Agent": "ncert-learn-bot/1.0"}
        )
        if resp.status_code == 200:
            results = resp.json().get("query", {}).get("search", [])
            if results:
                top_title = results[0]["title"]
                summary_url = WIKI_API.format(title=top_title.replace(" ", "_"))
                resp2 = requests.get(summary_url, timeout=timeout, headers={"User-Agent": "ncert-learn-bot/1.0"})
                if resp2.status_code == 200:
                    data = resp2.json()
                    extract = data.get("extract", "")
                    page_url = data.get("content_urls", {}).get("desktop", {}).get("page", "")
                    return extract[:WIKI_MAX_CHARS], page_url
    except requests.RequestException:
        pass

    return "", ""


# ─── LLM-based context summarisation ─────────────────────────────────────────

SYSTEM_SUMMARISE = """You are an expert educational content curator.
Summarise the provided reference material about a specific educational concept.
Focus on:
- Key definitions and formal statements
- Mathematical formulas (keep them accurate, use LaTeX notation)
- Important examples and applications
- Grade-appropriate content

Write a dense, information-rich summary of ~400-600 words. Include all formulas and
definitions verbatim. Do NOT add commentary — just compress and organise the material."""


def summarise_context(
    concept_name: str,
    grade: int,
    raw_text: str,
) -> str:
    """Compress raw reference text into a dense summary using local LLaMA-8B."""
    user_prompt = f"""Concept: {concept_name}
Grade level: {grade}

Reference material to summarise:
---
{raw_text[:6000]}
---

Write a dense, accurate summary for use as background material when writing
an educational Wikipedia-style article about this concept for Grade {grade} students.
Include all definitions, formulas, and important examples. Keep it to ~500 words."""

    return llm_call(system=SYSTEM_SUMMARISE, user=user_prompt, max_new_tokens=1000)


# ─── Page depth and section planning ─────────────────────────────────────────

def _grade_note(subject: str, grade: int) -> str:
    """Return a grade-appropriate depth instruction."""
    if grade <= 7:
        return "Very basic introduction. Use everyday examples, no formulas, simple language."
    if grade <= 9:
        return "Qualitative + semi-quantitative. Use simple numericals. Minimal calculus."
    if grade == 10:
        return "Full conceptual + numerical treatment. Board-exam level. No calculus."
    # Grades 11-12
    subject_note = {
        "physics": "Rigorous, mathematical. Include vector treatment, derivations, calculus where standard.",
        "chemistry": "Quantitative, include stoichiometry, thermodynamic/kinetic treatment as applicable.",
        "maths": "Full rigour. Include proofs where standard. Use precise mathematical language.",
        "biology": "Detailed mechanistic understanding. Include molecular/biochemical level for Grade 12.",
    }
    return subject_note.get(subject, "Advanced treatment with mathematical rigour for senior secondary level.")


def _determine_page_depth(concept: dict, grade: int) -> tuple[str, int, list[str]]:
    """
    Returns (page_depth, target_words, sections).
    page_depth: "overview" | "standard" | "deep-dive"
    """
    importance = concept.get("importance_by_grade", {}).get(str(grade), 3)
    has_children = bool(concept.get("leads_to"))

    # Area-level concepts (have many children) get overview pages
    if concept.get("area") and not concept.get("parent"):
        return "overview", 700, ["Lead", "Topics in This Area", "See Also"]

    if importance >= 4:
        depth, words = "deep-dive", 1500
        sections = ["Lead", "Background", "Explanation", "Mathematical Formulation",
                    "Derivation", "Examples", "Applications", "See Also"]
    elif importance >= 3:
        depth, words = "standard", 1000
        sections = ["Lead", "Explanation", "Examples", "Applications", "See Also"]
    else:
        depth, words = "standard", 700
        sections = ["Lead", "Explanation", "Examples", "See Also"]

    # Reduce for introductory grades
    if grade <= 8:
        words = min(words, 800)
        sections = [s for s in sections if s not in ("Mathematical Formulation", "Derivation")]

    return depth, words, sections


# ─── Main plan builder ────────────────────────────────────────────────────────

def build_content_plan(
    concept: dict,
    grade: int,
) -> dict:
    """Build a complete content plan for one (concept, grade) pair."""
    slug = concept["slug"]
    canonical_name = concept["canonical_name"]
    subject = concept.get("subject", "")

    log.info("  Planning %s | grade=%d", canonical_name, grade)

    # 1. NCERT chunks
    ncert_chunks = find_relevant_ncert_chunks(canonical_name, subject, grade)
    ncert_text = ""
    ncert_refs: list[str] = []
    for chunk in ncert_chunks:
        grade_n = chunk.get("grade", "")
        subj = chunk.get("subject", "")
        ch = chunk.get("chapter_number", "")
        ncert_refs.append(f"grade{grade_n}/{subj}/chapter{ch}")
        ncert_text += f"\n[NCERT {grade_n} {subj} Ch{ch} — {chunk.get('topic_title', '')}]\n"
        ncert_text += chunk.get("content", "")[:800]

    # 2. Wikipedia
    wiki_text, wiki_url = fetch_wikipedia_content(canonical_name)
    sources: list[str] = ncert_refs.copy()
    if wiki_text:
        sources.append("wikipedia")

    # 3. Combine + summarise if needed
    raw_combined = (ncert_text + "\n\n[Wikipedia]\n" + wiki_text).strip()
    if len(raw_combined) > MAX_CONTEXT_CHARS:
        context_summary = summarise_context(canonical_name, grade, raw_combined)
    elif raw_combined:
        context_summary = raw_combined[:MAX_CONTEXT_CHARS]
    else:
        context_summary = f"No external source material found. Generate based on curriculum knowledge for Grade {grade} {subject}."

    # 4. Page structure
    page_depth, target_words, sections = _determine_page_depth(concept, grade)

    return {
        "concept_slug": slug,
        "canonical_name": canonical_name,
        "subject": subject,
        "grade": grade,
        "domain": concept.get("domain", ""),
        "area": concept.get("area", ""),
        "page_depth": page_depth,
        "target_words": target_words,
        "context_summary": context_summary,
        "context_sources": sources,
        "prerequisites_to_link": concept.get("prerequisites", [])[:6],
        "successors_to_link": concept.get("leads_to", [])[:4],
        "related_to_link": concept.get("related", [])[:4],
        "see_also": concept.get("see_also", [])[:4],
        "sections": sections,
        "grade_note": _grade_note(subject, grade),
        "aliases": concept.get("aliases", []),
        "source_boards": concept.get("source_boards", []),
    }


# ─── Batch runner ─────────────────────────────────────────────────────────────

def run(
    graph: dict,
    grade_filter: int | None,
    subject_filter: str | None,
    slug_filter: str | None,
    skip_existing: bool,
) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    concepts = graph.get("concepts", {})
    total = 0
    skipped = 0
    failed = 0

    for slug, concept in concepts.items():
        if slug_filter and slug != slug_filter:
            continue
        subject = concept.get("subject", "")
        if subject_filter and subject != subject_filter:
            continue

        for grade in concept.get("grades", []):
            if grade_filter and grade != grade_filter:
                continue

            out_path = OUTPUT_DIR / f"{slug}_grade{grade}.json"
            if skip_existing and out_path.exists():
                skipped += 1
                continue

            try:
                plan = build_content_plan(concept, grade)
                out_path.write_text(json.dumps(plan, ensure_ascii=False, indent=2))
                total += 1
            except Exception as exc:
                log.error("Failed %s grade%d: %s", slug, grade, exc)
                failed += 1

    log.info("Content planning complete: %d created, %d skipped, %d failed", total, skipped, failed)
    log.info("Output in: %s", OUTPUT_DIR)


def check_coverage(graph: dict) -> None:
    """CLI --check-coverage: verify all (concept, grade) pairs have a plan."""
    concepts = graph.get("concepts", {})
    missing: list[str] = []
    for slug, concept in concepts.items():
        for grade in concept.get("grades", []):
            path = OUTPUT_DIR / f"{slug}_grade{grade}.json"
            if not path.exists():
                missing.append(f"{slug}_grade{grade}")
    if missing:
        log.warning("Missing content plans (%d):", len(missing))
        for m in missing[:20]:
            log.warning("  %s", m)
    else:
        log.info("Coverage check passed — all (concept, grade) pairs have content plans ✓")


# ─── CLI ──────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Stage 3 — Content planner (uses local LLaMA-8B)")
    p.add_argument("--grade", type=int)
    p.add_argument("--subject")
    p.add_argument("--concept", help="Process only this concept slug")
    p.add_argument(
        "--model-path",
        default=os.environ.get("LLAMA_MODEL_PATH", "/ssd_scratch/models/llama-8b"),
        help="Path to local LLaMA-8B model",
    )
    p.add_argument("--graph", default=str(GRAPH_PATH), help="Path to graph.json")
    p.add_argument("--skip-existing", action="store_true", default=True)
    p.add_argument("--no-skip-existing", dest="skip_existing", action="store_false")
    p.add_argument("--check-coverage", action="store_true", help="Check plan coverage and exit")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    os.environ.setdefault("LLAMA_MODEL_PATH", args.model_path)

    graph_path = Path(args.graph)
    if not graph_path.exists():
        log.error("Graph file not found: %s — run graph_builder.py first", graph_path)
        sys.exit(1)

    graph = json.loads(graph_path.read_text())
    log.info("Loaded graph: %d concepts", len(graph.get("concepts", {})))

    if args.check_coverage:
        check_coverage(graph)
        return

    run(
        graph,
        grade_filter=args.grade,
        subject_filter=args.subject,
        slug_filter=args.concept,
        skip_existing=args.skip_existing,
    )


if __name__ == "__main__":
    main()
