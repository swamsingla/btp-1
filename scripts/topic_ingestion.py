#!/usr/bin/env python3
"""
Stage 1 — Multi-Source Topic Ingestion
=======================================
Discovers the COMPLETE set of topics a student should learn at each
grade × subject, combining:
  1. NCERT headings already parsed (data/intermediate/headings/)
  2. LLM-powered comprehensive discovery across NCERT, ICSE, all state boards

Output: data/intermediate/raw_topics/{grade}_{subject}.json

Schema:
{
  "grade": 10,
  "subject": "science",
  "topics": [
    {
      "raw_name": "Chemical Reactions and Equations",
      "ncert_refs": ["chapter1"],
      "subtopics": ["Combination Reactions", "Decomposition Reactions"],
      "source_boards": ["NCERT", "ICSE"],
      "note": ""
    },
    ...
  ]
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

from thefuzz import fuzz

# Local LLaMA-8B inference (Stages 1-3 use local model per implementation plan)
from llm_local import llm_call as _local_llm_call

# ─── Paths ───────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
HEADINGS_DIR = BASE_DIR / "data" / "intermediate" / "headings"
OUTPUT_DIR = BASE_DIR / "data" / "intermediate" / "raw_topics"

# ─── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ─── Supported grades and subjects ───────────────────────────────────────────
GRADE_SUBJECTS: dict[int, list[str]] = {
    6:  ["maths", "science"],
    7:  ["maths", "science"],
    8:  ["maths", "science"],
    9:  ["maths", "science"],
    10: ["maths", "science"],
    11: ["maths", "physics", "chemistry", "biology"],
    12: ["maths", "physics", "chemistry", "biology"],
}

# ─── LLM helpers ─────────────────────────────────────────────────────────────
# Stages 1-3 use the local LLaMA-8B model (implementation plan).
# _local_llm_call is imported from llm_local at the top of this file.

def llm_call(
    system: str,
    user: str,
    temperature: float = 0.2,
    max_new_tokens: int = 4096,
) -> str:
    """Thin wrapper around the local LLaMA-8B inference."""
    return _local_llm_call(system=system, user=user,
                           temperature=temperature, max_new_tokens=max_new_tokens)


# ─── JSON extraction helper ───────────────────────────────────────────────────

def extract_json(text: str) -> Any:
    """Extract the first valid JSON object or array from a freeform LLM response."""
    # Try the whole text first
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass
    # Try to find JSON block inside markdown fences
    fence_match = re.search(r"```(?:json)?\s*([\s\S]+?)\s*```", text)
    if fence_match:
        try:
            return json.loads(fence_match.group(1))
        except json.JSONDecodeError:
            pass
    # Try greedy bracket extraction
    for start_char, end_char in [("{", "}"), ("[", "]")]:
        start = text.find(start_char)
        end = text.rfind(end_char)
        if start != -1 and end != -1 and end > start:
            try:
                return json.loads(text[start : end + 1])
            except json.JSONDecodeError:
                pass
    # Last resort: recover partial array — strip trailing incomplete item
    # e.g. "[{...}, {...}, {..." → parse "[{...}, {...}]"
    start = text.find("[")
    if start != -1:
        chunk = text[start:]
        # Walk backwards trying progressively shorter tails
        for end in range(len(chunk) - 1, 0, -1):
            if chunk[end] in ("]", "}"):
                candidate = chunk[: end + 1]
                # Close any unclosed array
                if candidate.rstrip()[-1] == "}":
                    candidate = candidate + "]"
                try:
                    parsed = json.loads(candidate)
                    if isinstance(parsed, list) and parsed:
                        log.warning("Recovered %d partial items from truncated LLM array", len(parsed))
                        return parsed
                except json.JSONDecodeError:
                    continue
    raise ValueError(f"Could not extract JSON from LLM response:\n{text[:500]}")


# ─── NCERT heading loader ─────────────────────────────────────────────────────

def load_ncert_headings(grade: int, subject: str) -> list[dict]:
    """
    Load all chapter heading JSONs for a grade+subject.
    Returns a flat list of topics with ncert chapter ref.
    """
    grade_dir = HEADINGS_DIR / f"grade{grade}" / subject
    if not grade_dir.exists():
        log.warning("No NCERT headings found at %s", grade_dir)
        return []

    topics: list[dict] = []
    for chapter_file in sorted(grade_dir.glob("**/chapter*.json")):
        try:
            data = json.loads(chapter_file.read_text())
        except Exception as exc:
            log.warning("Could not read %s: %s", chapter_file, exc)
            continue

        chapter_ref = chapter_file.stem  # e.g. "chapter1"
        chapter_title = data.get("chapter_title", "")

        for topic in data.get("topics", []):
            t_title = topic.get("title", "").strip()
            if not t_title:
                continue
            subtopics = [st.get("title", "") for st in topic.get("subtopics", []) if st.get("title")]
            topics.append(
                {
                    "raw_name": t_title,
                    "ncert_refs": [chapter_ref],
                    "subtopics": subtopics,
                    "source_boards": ["NCERT"],
                    "note": f"From NCERT {chapter_title}",
                }
            )
    log.info("  Loaded %d NCERT topics for grade%d/%s", len(topics), grade, subject)
    return topics


# ─── LLM-powered comprehensive topic discovery ───────────────────────────────

SYSTEM_TOPIC_DISCOVERY = """You are an expert Indian curriculum designer with deep knowledge of
NCERT, ICSE, CBSE, and all major state board syllabi (Maharashtra, Tamil Nadu, Karnataka, etc.).

You MUST respond with a valid JSON array of strings only — no objects, no keys, no markdown fences, no explanation.
Example of the ONLY acceptable format:
["Quadratic Equations", "Trigonometric Ratios", "Surface Areas and Volumes"]

Do NOT use objects. Do NOT use keys like raw_name or source_boards. Just a flat list of topic name strings."""

SYSTEM_SUBTOPIC_ENRICHMENT = """You are an expert Indian curriculum designer.
Given a list of educational topics for a specific grade and subject, generate precise,
concept-specific subtopics for each topic.

Rules:
- Subtopics must be SPECIFIC to the topic — never generic phrases like "Making Predictions", "Analyzing Data", "Understanding X"
- Each subtopic should name a concrete skill, concept, or procedure (e.g., "Cross-multiplication of fractions", "Prime factorization method")
- 3 to 6 subtopics per topic, ordered from foundational to advanced
- Subtopics must make sense without reading the parent topic name

You MUST respond with a valid JSON array only — no prose, no markdown fences. Each element:
{
  "raw_name": "<exact topic name as given>",
  "subtopics": ["<specific subtopic 1>", "<specific subtopic 2>", ...]
}"""


def discover_topics_via_llm(
    grade: int,
    subject: str,
    ncert_topic_names: list[str],
) -> list[dict]:
    """
    Ask the LLM to enumerate additional topics (beyond NCERT) for grade+subject.
    Returns topics WITHOUT subtopics — those are enriched separately.
    """
    ncert_preview = "\n".join(f"- {t}" for t in ncert_topic_names[:60])

    if ncert_topic_names:
        ncert_section = f"Topics already in NCERT (do NOT repeat these):\n{ncert_preview}\n\nList ONLY additional topics from ICSE or major state boards not in the list above."
    else:
        ncert_section = f"There are no NCERT topics for this grade/subject. List ALL important {subject.title()} topics taught at Grade {grade} across NCERT, ICSE, CBSE and major state boards (Maharashtra, Tamil Nadu, Karnataka, AP/Telangana)."

    user_prompt = f"""Grade {grade} {subject.title()}

{ncert_section}

Rules:
- Proper Wikipedia-style topic names only (e.g. "Quadratic Equations", not "2.3 Solving Equations")
- Distinct self-contained concepts, not chapter headings
- Aim for 15-25 topics

Return ONLY a JSON array of strings. Example: ["Topic A", "Topic B", "Topic C"]
No objects, no keys, no markdown, no explanation."""

    raw = llm_call(system=SYSTEM_TOPIC_DISCOVERY, user=user_prompt, temperature=0.2, max_new_tokens=4000)
    try:
        result = extract_json(raw)
        if isinstance(result, dict) and "topics" in result:
            result = result["topics"]
        if not isinstance(result, list):
            log.warning("Unexpected LLM JSON shape; got type %s", type(result).__name__)
            return []
        # LLM returns either plain strings ["Topic", ...] or objects [{"raw_name":...}, ...]
        cleaned = []
        for item in result:
            if isinstance(item, str):
                name = item.strip()
            elif isinstance(item, dict):
                name = (item.get("raw_name") or item.get("name") or item.get("topic") or "").strip()
            else:
                continue
            if not name:
                continue
            cleaned.append({
                "raw_name": name,
                "source_boards": [],
                "note": "",
                "subtopics": [],
            })
        return cleaned
    except ValueError as exc:
        # Attempt 2: normalize mixed escaping (LLM sometimes produces \" inside "..." strings)
        normalized = raw.replace('\\"', '"')
        if normalized != raw:
            try:
                result2 = extract_json(normalized)
                if isinstance(result2, dict) and "topics" in result2:
                    result2 = result2["topics"]
                if isinstance(result2, list):
                    cleaned = []
                    for item in result2:
                        if not isinstance(item, dict):
                            continue
                        name = (item.get("raw_name") or item.get("name") or item.get("topic") or "").strip()
                        if not name:
                            continue
                        cleaned.append({
                            "raw_name": name,
                            "source_boards": item.get("source_boards") or item.get("boards") or [],
                            "note": item.get("note", ""),
                            "subtopics": item.get("subtopics", []),
                        })
                    if cleaned:
                        log.info("Mixed-escaping normalization rescued %d topics", len(cleaned))
                        return cleaned
            except ValueError:
                pass
        # Attempt 3: regex fallback — extract raw_name values from utterly broken JSON
        names = re.findall(r'["\']?(?:\\?"?)raw_name["\']?\s*:\s*["\']?\\?"?([A-Za-z][^"\\,\n\]{]+)', normalized, re.IGNORECASE)
        if names:
            cleaned = [{"raw_name": n.strip().rstrip('",\\'), "source_boards": [], "note": "", "subtopics": []} for n in names if n.strip()]
            cleaned = [c for c in cleaned if c["raw_name"]]
            if cleaned:
                log.warning("Regex fallback extracted %d topic names for grade%d/%s", len(cleaned), grade, subject)
                return cleaned
        log.error("All JSON extraction methods failed for grade%d/%s: %s", grade, subject, exc)
        return []


def enrich_subtopics_batch(
    grade: int,
    subject: str,
    topics: list[dict],
    batch_size: int = 10,
) -> dict[str, list[str]]:
    """
    For a list of topics that have no/poor subtopics, call the LLM in batches
    to generate specific, high-quality subtopics.
    Returns a dict mapping raw_name → list[subtopic_str].
    """
    result: dict[str, list[str]] = {}

    for i in range(0, len(topics), batch_size):
        batch = topics[i : i + batch_size]
        topic_list = "\n".join(f'- "{t["raw_name"]}"' for t in batch)

        user_prompt = f"""Grade: {grade}  Subject: {subject.title()}

Generate specific subtopics for each of the following topics:
{topic_list}

Return a JSON array with one object per topic (same order). Each object:
{{
  "raw_name": "<exact topic name>",
  "subtopics": ["<concrete subtopic>", ...]
}}"""

        raw = llm_call(
            system=SYSTEM_SUBTOPIC_ENRICHMENT,
            user=user_prompt,
            temperature=0.1,
            max_new_tokens=2000,
        )
        try:
            parsed = extract_json(raw)
            if not isinstance(parsed, list):
                log.warning("  Subtopic enrichment batch %d: unexpected shape %s", i // batch_size, type(parsed))
                continue
            for item in parsed:
                name = item.get("raw_name", "").strip()
                subs = item.get("subtopics", [])
                if name and isinstance(subs, list) and subs:
                    result[name] = subs
        except ValueError as exc:
            log.warning("  Subtopic enrichment batch %d failed: %s", i // batch_size, exc)

    return result


# Generic/placeholder subtopic phrases to detect and replace
_GENERIC_SUBTOPICS = {
    "making predictions", "analyzing data", "understanding the topic",
    "exploring concepts", "applying knowledge", "reviewing concepts",
    "solving problems", "real-life applications",
}


def _has_generic_subtopics(subtopics: list[str]) -> bool:
    """Return True if the subtopic list is mostly generic/placeholder phrases."""
    if not subtopics:
        return True
    generic_count = sum(
        1 for s in subtopics
        if s.lower().strip() in _GENERIC_SUBTOPICS
        or s.lower().startswith("understanding ")
        or s.lower().startswith("exploring ")
    )
    return generic_count >= len(subtopics) // 2


# ─── Deduplication / merging ──────────────────────────────────────────────────

FUZZY_THRESHOLD = 85  # similarity score out of 100


def fuzzy_merge(
    ncert_topics: list[dict],
    llm_topics: list[dict],
) -> tuple[list[dict], int]:
    """
    Merge NCERT topics and LLM-discovered topics using fuzzy name matching.
    NCERT topics are ground-truth — their subtopics (from actual textbook headings)
    are NEVER overwritten by LLM subtopics.
    LLM topics that don't match any NCERT topic are added as new entries.
    Returns (merged_list, new_from_llm_count).
    """
    merged: list[dict] = []
    seen_names: list[str] = []

    def _add(topic: dict) -> None:
        name_key = (topic.get("raw_name") or "").lower().strip()
        if not name_key:
            return  # skip malformed LLM topics without raw_name
        for idx, existing in enumerate(seen_names):
            if fuzz.token_sort_ratio(name_key, existing) >= FUZZY_THRESHOLD:
                # Merge source_boards only — never clobber NCERT subtopics with LLM ones
                for board in topic.get("source_boards", []):
                    if board not in merged[idx]["source_boards"]:
                        merged[idx]["source_boards"].append(board)
                # Only adopt LLM note if existing entry has none
                if not merged[idx].get("note") and topic.get("note"):
                    merged[idx]["note"] = topic["note"]
                return
        # New entry — include subtopics as-is (will be enriched later if needed)
        merged.append(dict(topic))
        seen_names.append(name_key)

    for t in ncert_topics:
        _add(t)
    new_from_llm = 0
    for t in llm_topics:
        before = len(merged)
        _add(t)
        if len(merged) > before:
            new_from_llm += 1

    log.info(
        "  Merge: %d NCERT + %d LLM → %d merged (LLM added %d new)",
        len(ncert_topics),
        len(llm_topics),
        len(merged),
        new_from_llm,
    )
    return merged, new_from_llm


# ─── Single grade+subject pipeline ───────────────────────────────────────────

def process_grade_subject(
    grade: int,
    subject: str,
    skip_existing: bool,
) -> Path:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    out_path = OUTPUT_DIR / f"grade{grade}_{subject}.json"

    if skip_existing and out_path.exists():
        log.info("Skipping grade%d/%s (already exists at %s)", grade, subject, out_path)
        return out_path

    log.info("Processing grade%d/%s …", grade, subject)

    # Step 1: Load NCERT headings as grounding reference
    ncert_topics = load_ncert_headings(grade, subject)
    ncert_names = [t["raw_name"] for t in ncert_topics]

    # Step 2: LLM discovers ADDITIONAL topics (names + boards only, no subtopics)
    log.info("  Calling LLM for additional topic discovery …")
    llm_topics = discover_topics_via_llm(grade, subject, ncert_names)
    log.info("  LLM discovered %d additional topics", len(llm_topics))

    # Step 3: Merge & deduplicate (NCERT subtopics are preserved; LLM subtopics ignored)
    merged, _ = fuzzy_merge(ncert_topics, llm_topics)

    # Step 4: Enrich subtopics
    #   4a: NCERT topics whose headings had no/poor subtopics
    ncert_needs_subs = [t for t in merged if "NCERT" in t.get("source_boards", []) and _has_generic_subtopics(t.get("subtopics", []))]
    #   4b: LLM-added topics (no textbook headings to rely on)
    llm_only = [t for t in merged if "NCERT" not in t.get("source_boards", [])]
    needs_enrichment = ncert_needs_subs + llm_only
    if needs_enrichment:
        log.info("  Enriching subtopics for %d topics (%d NCERT poor + %d LLM-only) …",
                 len(needs_enrichment), len(ncert_needs_subs), len(llm_only))
        enriched = enrich_subtopics_batch(grade, subject, needs_enrichment)
        for topic in merged:
            if topic["raw_name"] in enriched:
                topic["subtopics"] = enriched[topic["raw_name"]]
        log.info("  Enriched subtopics for %d/%d topics", len(enriched), len(needs_enrichment))

    # Step 6: Serialise
    result = {
        "grade": grade,
        "subject": subject,
        "total_topics": len(merged),
        "topics": merged,
    }
    out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2))
    log.info("  ✓ Wrote %d topics → %s", len(merged), out_path)
    return out_path


# ─── CLI ──────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Stage 1 — Multi-source topic ingestion per grade+subject (uses local LLaMA-8B)"
    )
    p.add_argument("--grade", type=int, help="Process only this grade (6-12)")
    p.add_argument("--subject", type=str, help="Process only this subject (maths/science/…)")
    p.add_argument(
        "--model-path",
        default=os.environ.get("LLAMA_MODEL_PATH", "/ssd_scratch/models/llama-8b"),
        help="Path to the local LLaMA-8B model (default: /ssd_scratch/models/llama-8b)",
    )
    p.add_argument(
        "--skip-existing",
        action="store_true",
        default=True,
        help="Skip grade+subject combos whose output already exists (default: True)",
    )
    p.add_argument(
        "--no-skip-existing",
        dest="skip_existing",
        action="store_false",
        help="Re-process even if output already exists",
    )
    return p.parse_args()


def main() -> None:
    args = parse_args()

    # Set the model path for the local LLaMA singleton (llm_local reads env var or default)
    os.environ.setdefault("LLAMA_MODEL_PATH", args.model_path)

    # Build list of (grade, subject) to process
    pairs: list[tuple[int, str]] = []
    for grade, subjects in GRADE_SUBJECTS.items():
        if args.grade and grade != args.grade:
            continue
        for subject in subjects:
            if args.subject and subject != args.subject:
                continue
            pairs.append((grade, subject))

    if not pairs:
        log.error("No grade+subject pairs match the given filters.")
        sys.exit(1)

    log.info("Will process %d grade+subject pair(s) using local LLaMA-8B", len(pairs))

    for grade, subject in pairs:
        try:
            process_grade_subject(grade, subject, args.skip_existing)
        except Exception as exc:
            log.error("Failed grade%d/%s: %s", grade, subject, exc, exc_info=True)

    log.info("Stage 1 complete. Output in: %s", OUTPUT_DIR)


if __name__ == "__main__":
    main()
