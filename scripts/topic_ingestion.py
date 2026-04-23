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
    for chapter_file in sorted(grade_dir.glob("chapter*.json")):
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
You have been asked to create a COMPREHENSIVE list of topics for a grade and subject.

Your goal: A student who masters ALL topics on this list should have world-class
understanding at this grade level — covering every important concept across all Indian boards
plus universally important concepts taught globally at this level.

You MUST respond with a valid JSON array only (no prose, no markdown fences). Each element:
{
  "raw_name": "<topic name — proper Wikipedia-style title>",
  "subtopics": ["<sub-topic 1>", "<sub-topic 2>", ...],
  "source_boards": ["NCERT", "ICSE", "State Boards"],
  "note": "<optional: which boards include this / any clarification>"
}"""


def discover_topics_via_llm(
    grade: int,
    subject: str,
    ncert_topic_names: list[str],
) -> list[dict]:
    """
    Ask the LLM to enumerate the complete canonical topic set for grade+subject,
    using the already-known NCERT topic names as a grounding anchor.
    """
    ncert_preview = "\n".join(f"- {t}" for t in ncert_topic_names[:60])

    user_prompt = f"""Grade: {grade}
Subject: {subject.title()}

The following topics are confirmed to appear in NCERT textbooks for this grade+subject:
{ncert_preview}

Now produce the COMPLETE list of topics for Grade {grade} {subject.title()}.
Requirements:
1. Include ALL topics from NCERT (those above and any you know are there)
2. Include additional important topics from ICSE and state boards NOT in NCERT
3. Include any universally important concepts taught globally at this grade level
4. Use proper Wikipedia-style names (e.g., "Quadratic Equations" not "2.3 Solving Equations")
5. Each topic should be a distinct, self-contained concept — not a chapter name
6. Include 3-8 meaningful subtopics per topic
7. Aim for completeness — it is better to include too many than to miss important ones

Return a JSON array directly (no markdown, no preamble)."""

    raw = llm_call(system=SYSTEM_TOPIC_DISCOVERY, user=user_prompt, temperature=0.2, max_new_tokens=6000)
    try:
        result = extract_json(raw)
        if isinstance(result, list):
            return result
        if isinstance(result, dict) and "topics" in result:
            return result["topics"]
        log.warning("Unexpected LLM JSON shape; got type %s", type(result).__name__)
        return []
    except ValueError as exc:
        log.error("JSON extraction failed for grade%d/%s: %s", grade, subject, exc)
        return []


# ─── Deduplication / merging ──────────────────────────────────────────────────

FUZZY_THRESHOLD = 85  # similarity score out of 100


def fuzzy_merge(
    ncert_topics: list[dict],
    llm_topics: list[dict],
) -> list[dict]:
    """
    Merge NCERT topics and LLM-discovered topics using fuzzy name matching.
    NCERT topics are ground-truth; LLM topics are treated as additional discoveries.
    Deduplicates by name similarity ≥ FUZZY_THRESHOLD.
    """
    merged: list[dict] = []
    # Index for dedup: list of normalized names already in merged
    seen_names: list[str] = []

    def _add(topic: dict) -> None:
        name_key = topic["raw_name"].lower().strip()
        for existing in seen_names:
            if fuzz.token_sort_ratio(name_key, existing) >= FUZZY_THRESHOLD:
                # Merge metadata into the existing entry
                idx = seen_names.index(existing)
                for board in topic.get("source_boards", []):
                    if board not in merged[idx]["source_boards"]:
                        merged[idx]["source_boards"].append(board)
                for st in topic.get("subtopics", []):
                    if st not in merged[idx]["subtopics"]:
                        merged[idx]["subtopics"].append(st)
                # Keep NCERT note if present
                if not merged[idx].get("note") and topic.get("note"):
                    merged[idx]["note"] = topic["note"]
                return
        # New entry
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
    return merged


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

    # Step 2: LLM comprehensive discovery
    log.info("  Calling LLM for comprehensive topic discovery …")
    llm_topics = discover_topics_via_llm(grade, subject, ncert_names)
    log.info("  LLM discovered %d topics", len(llm_topics))

    # Step 3: Merge & deduplicate
    merged = fuzzy_merge(ncert_topics, llm_topics)

    # Step 4: Serialise
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
