#!/usr/bin/env python3
"""
Stage 2 — Canonical Knowledge Graph Builder
============================================
Converts the raw per-grade topic lists (from topic_ingestion.py) into a
structured, multi-level knowledge graph with prerequisite edges.

Pipeline per subject:
  1. Load all raw_topics JSONs for that subject across grades 6-12.
  2. Call LLM to extract a canonical concept hierarchy
     (Domain → Area → Concept → Sub-concept).
  3. Call LLM to establish prerequisite edges between concepts.
  4. Build a NetworkX DiGraph, validate it is a DAG (no cycles).
  5. Compute per-grade importance scores and entry-point concepts.
  6. Save the graph in two forms:
     • data/knowledge_graph/graph_by_subject/{subject}.json   (subject graph)
     • data/knowledge_graph/graph.json                        (merged global graph)

Output schema  →  see GRAPH_SCHEMA_EXAMPLE at the bottom of this file.
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import networkx as nx
from thefuzz import fuzz

# Local LLaMA-8B inference (Stages 1-3 per implementation plan)
from llm_local import llm_call as _local_llm_call

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_TOPICS_DIR = BASE_DIR / "data" / "intermediate" / "raw_topics"
KG_DIR = BASE_DIR / "data" / "knowledge_graph"
CKPT_DIR = KG_DIR / ".checkpoints"


def _ckpt_save(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2))


def _ckpt_load(path: Path) -> Any | None:
    if path.exists():
        try:
            return json.loads(path.read_text())
        except Exception:
            pass
    return None

# ─── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ─── Subjects & grades ───────────────────────────────────────────────────────
ALL_SUBJECTS = ["maths", "science", "physics", "chemistry", "biology"]
ALL_GRADES = list(range(6, 13))

# ─── LLM helpers ─────────────────────────────────────────────────────────────
# Stages 1-3 use local LLaMA-8B (implementation plan).

def llm_call(
    system: str,
    user: str,
    temperature: float = 0.2,
    max_new_tokens: int = 6000,
) -> str:
    """Thin wrapper around the local LLaMA-8B inference."""
    return _local_llm_call(system=system, user=user,
                           temperature=temperature, max_new_tokens=max_new_tokens)


def extract_json(text: str) -> Any:
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
    # Last resort: recover partial array — LLM truncated output mid-item
    start = text.find("[")
    if start != -1:
        chunk = text[start:]
        for end in range(len(chunk) - 1, 0, -1):
            if chunk[end] in ("]", "}"):
                candidate = chunk[:end + 1]
                if candidate.rstrip()[-1] == "}":
                    candidate += "]"
                try:
                    parsed = json.loads(candidate)
                    if isinstance(parsed, list) and parsed:
                        log.warning("Recovered %d partial items from truncated LLM array", len(parsed))
                        return parsed
                except json.JSONDecodeError:
                    continue
    raise ValueError(f"Cannot extract JSON from: {text[:400]}")


# ─── Slug helpers ─────────────────────────────────────────────────────────────

def slugify(name: str) -> str:
    """Convert a concept name to a URL-safe slug."""
    s = name.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = re.sub(r"^-+|-+$", "", s)
    return s


# ─── Load raw topics ─────────────────────────────────────────────────────────

def load_raw_topics_for_subject(subject: str) -> dict[int, list[dict]]:
    """
    Returns {grade: [topics]} for a subject, loading all available grade files.
    Grade 10 "science" is mapped to cover physics/chemistry/biology for grades ≤10.
    """
    grade_topics: dict[int, list[dict]] = {}

    # Map: which file names to look for per subject
    file_subjects = [subject]
    if subject in ("physics", "chemistry", "biology"):
        # These also exist under "science" for grades 6-10
        file_subjects.append("science")

    for grade in ALL_GRADES:
        for fs in file_subjects:
            path = RAW_TOPICS_DIR / f"grade{grade}_{fs}.json"
            if path.exists():
                data = json.loads(path.read_text())
                grade_topics.setdefault(grade, []).extend(data.get("topics", []))

    log.info("Loaded raw topics for subject=%s across grades: %s", subject, sorted(grade_topics.keys()))
    return grade_topics


# ─── Step 2a: Canonical concept hierarchy extraction ─────────────────────────

SYSTEM_HIERARCHY = """You are a knowledge engineer building an educational knowledge graph.
Convert a flat list of raw topics (from multiple boards) into a canonical concept hierarchy.

Hierarchy levels:
  Domain > Area > Concept > Sub-concept

Rules:
1. Every node that a student might search for should be a separate entry.
2. Use proper Wikipedia-style names ("Newton's First Law of Motion", not "1.1 Laws").
3. Include aliases (alternative names or regional terminology).
4. Assign grades: the list of grade levels (6-12) where this concept is taught.
5. Assign importance per grade (1=minor, 5=central).

Respond with a JSON array of concept objects ONLY (no prose):
[
  {
    "canonical_name": "Newton's First Law of Motion",
    "slug": "newtons-first-law-of-motion",
    "aliases": ["Law of Inertia"],
    "domain": "Mechanics",
    "area": "Newton's Laws of Motion",
    "parent": "newtons-laws-of-motion",
    "grades": [8, 9, 11],
    "importance_by_grade": {"8": 4, "9": 5, "11": 3},
    "source_boards": ["NCERT", "ICSE"]
  },
  ...
]
"""


def extract_canonical_concepts(
    subject: str,
    grade_topics: dict[int, list[dict]],
    batch_size: int = 20,
) -> list[dict]:
    """
    Calls the LLM in batches to extract canonical concepts from raw topics.
    Saves per-batch checkpoints so the run can be resumed after interruption.
    Returns a deduplicated list of concept dicts.
    """
    # Collect all unique raw topic names across grades (with grade context)
    raw_entries: list[str] = []
    seen_raw: set[str] = set()
    for grade, topics in sorted(grade_topics.items()):
        for t in topics:
            name = t.get("raw_name", "").strip()
            if not name or name in seen_raw:
                continue
            seen_raw.add(name)
            subtopics = t.get("subtopics", [])
            sub_str = f" [subtopics: {', '.join(subtopics[:5])}]" if subtopics else ""
            raw_entries.append(f"- (grade {grade}) {name}{sub_str}")

    log.info("  Total unique raw topics to canonicalize: %d", len(raw_entries))

    all_concepts: list[dict] = []
    seen_slugs: set[str] = set()

    # ── Reload already-completed batches from checkpoint ──────────────────────
    num_batches = (len(raw_entries) + batch_size - 1) // batch_size
    completed_batches: set[int] = set()
    for batch_idx in range(num_batches):
        batch_start = batch_idx * batch_size
        ckpt_path = CKPT_DIR / f"{subject}_concepts_batch{batch_start}.json"
        cached = _ckpt_load(ckpt_path)
        if cached is not None:
            log.info("  [ckpt] Loading batch %d from checkpoint", batch_start)
            for c in cached:
                if c.get("slug") and c["slug"] not in seen_slugs:
                    seen_slugs.add(c["slug"])
                    all_concepts.append(c)
            completed_batches.add(batch_start)

    # Process in batches
    for batch_start in range(0, len(raw_entries), batch_size):
        if batch_start in completed_batches:
            continue  # already loaded from checkpoint

        batch = raw_entries[batch_start : batch_start + batch_size]
        batch_str = "\n".join(batch)

        user_prompt = f"""Subject: {subject.title()}
Grade range of these topics: 6–12

Raw topics (from NCERT + ICSE + state boards):
{batch_str}

Extract the canonical concept hierarchy for these topics.
Each raw topic may produce 1 high-level concept OR multiple sub-concepts.
IMPORTANT: Populate the "slug" field using lowercase-hyphenated form of canonical_name.
Return JSON array only."""

        raw_resp = llm_call(system=SYSTEM_HIERARCHY, user=user_prompt, max_new_tokens=2500)

        try:
            concepts = extract_json(raw_resp)
            if not isinstance(concepts, list):
                log.warning("Unexpected shape from LLM (batch %d): %s", batch_start, type(concepts))
                continue
        except ValueError as exc:
            log.error("Failed to parse batch %d: %s", batch_start, exc)
            continue

        # Assign subject + deduplicate by slug
        new_in_batch: list[dict] = []
        for c in concepts:
            if "canonical_name" not in c:
                continue
            if "slug" not in c or not c["slug"]:
                c["slug"] = slugify(c["canonical_name"])
            c["subject"] = subject
            if c["slug"] in seen_slugs:
                continue
            seen_slugs.add(c["slug"])
            all_concepts.append(c)
            new_in_batch.append(c)

        # ── Save batch checkpoint ─────────────────────────────────────────────
        ckpt_path = CKPT_DIR / f"{subject}_concepts_batch{batch_start}.json"
        _ckpt_save(ckpt_path, new_in_batch)

        log.info(
            "  Batch %d-%d → %d new concepts (total so far: %d)",
            batch_start,
            batch_start + len(batch),
            len(new_in_batch),
            len(all_concepts),
        )
        # Be polite to the API between batches
        time.sleep(1)

    log.info("  Canonical concept extraction complete: %d unique concepts", len(all_concepts))
    return all_concepts


# ─── Step 2b: Prerequisite edge extraction ───────────────────────────────────

SYSTEM_PREREQS = """You are an expert curriculum sequencer.
Given a list of educational concepts, determine the prerequisite relationships between them.

Rules:
1. A prerequisite means: a student MUST understand concept A before studying concept B.
2. Only list DIRECT prerequisites — skip transitively implied ones.
3. related: concepts useful to read alongside (no strict order required).
4. see_also: interesting connections, possibly in other domains.
5. Only use slugs from the provided concept list — do NOT invent new slugs.

Return a JSON array ONLY:
[
  {
    "slug": "newtons-second-law-of-motion",
    "prerequisites": ["newtons-first-law-of-motion", "force-and-motion"],
    "related": ["friction", "mass-and-weight"],
    "see_also": ["momentum"]
  },
  ...
]"""


def extract_prerequisite_edges(
    concepts: list[dict],
    grade: int,
    subject: str = "",
    batch_size: int = 40,
) -> list[dict]:
    """
    For the concepts relevant to a given grade, ask the LLM for prerequisite edges.
    Saves per-grade checkpoints so the run can be resumed after interruption.
    Returns a list of {slug, prerequisites, related, see_also} dicts.
    """
    grade_concepts = [c for c in concepts if grade in c.get("grades", [])]
    if not grade_concepts:
        return []

    # ── Check full-grade checkpoint ───────────────────────────────────────────
    grade_ckpt = CKPT_DIR / f"{subject}_edges_grade{grade}.json"
    cached = _ckpt_load(grade_ckpt)
    if cached is not None:
        log.info("  [ckpt] Loading grade %d edges from checkpoint (%d records)", grade, len(cached))
        return cached

    all_edges: list[dict] = []
    slug_set = {c["slug"] for c in grade_concepts}

    for batch_start in range(0, len(grade_concepts), batch_size):
        batch = grade_concepts[batch_start : batch_start + batch_size]
        concept_list = "\n".join(f"- {c['slug']}: {c['canonical_name']}" for c in batch)
        subj = batch[0].get("subject", subject)

        user_prompt = f"""Grade: {grade}
Subject: {subj}

Concepts for this grade:
{concept_list}

For each concept in this list, specify prerequisite relationships.
IMPORTANT: Only use slugs from the list above — do NOT reference external slugs.
Return JSON array only."""

        raw_resp = llm_call(system=SYSTEM_PREREQS, user=user_prompt, max_new_tokens=4000)
        try:
            edges = extract_json(raw_resp)
            if not isinstance(edges, list):
                continue
        except ValueError:
            continue

        # Filter edges: only keep slugs that actually exist in our concept set
        for e in edges:
            slug = e.get("slug", "")
            if slug not in slug_set:
                continue
            filtered = {
                "slug": slug,
                "prerequisites": [s for s in e.get("prerequisites", []) if s in slug_set],
                "related": [s for s in e.get("related", []) if s in slug_set],
                "see_also": [s for s in e.get("see_also", []) if s in slug_set],
            }
            all_edges.append(filtered)

        time.sleep(1)

    # ── Save full-grade checkpoint ────────────────────────────────────────────
    _ckpt_save(grade_ckpt, all_edges)
    log.info("  [ckpt] Saved grade %d edges checkpoint (%d records)", grade, len(all_edges))

    return all_edges


# ─── Step 2c: Build NetworkX DAG and validate ────────────────────────────────

def build_dag(
    concepts: list[dict],
    edges_by_grade: dict[int, list[dict]],
) -> tuple[nx.DiGraph, dict]:
    """
    Construct a NetworkX DiGraph from concept nodes + grade-aggregated edges.
    Detects and removes cycles (reporting them as warnings).

    Returns:
        G: The validated DAG
        concept_map: {slug: concept_dict} with enriched prerequisite/leads_to fields
    """
    G = nx.DiGraph()
    concept_map: dict[str, dict] = {c["slug"]: c for c in concepts}

    # Add nodes
    for c in concepts:
        G.add_node(c["slug"], **{k: v for k, v in c.items() if k != "slug"})

    # Aggregate edge sets across grades
    prereq_map: dict[str, set[str]] = {c["slug"]: set() for c in concepts}
    related_map: dict[str, set[str]] = {c["slug"]: set() for c in concepts}
    see_also_map: dict[str, set[str]] = {c["slug"]: set() for c in concepts}

    for _grade, edge_list in edges_by_grade.items():
        for e in edge_list:
            slug = e["slug"]
            if slug not in prereq_map:
                continue
            prereq_map[slug].update(e.get("prerequisites", []))
            related_map[slug].update(e.get("related", []))
            see_also_map[slug].update(e.get("see_also", []))

    # Add prerequisite edges (these are what form the DAG)
    for slug, prereqs in prereq_map.items():
        for prereq in prereqs:
            if prereq in concept_map and prereq != slug:
                G.add_edge(prereq, slug, type="prerequisite")

    # Cycle detection and removal
    cycles_removed = 0
    while not nx.is_directed_acyclic_graph(G):
        try:
            cycle = nx.find_cycle(G)
            u, v = cycle[0][0], cycle[0][1]
            log.warning("Cycle detected: removing edge %s → %s", u, v)
            G.remove_edge(u, v)
            prereq_map[v].discard(u)
            cycles_removed += 1
        except nx.NetworkXNoCycle:
            break

    if cycles_removed:
        log.warning("Removed %d cyclic edge(s) to ensure DAG validity", cycles_removed)

    log.info("Graph: %d nodes, %d edges (all DAG-validated)", G.number_of_nodes(), G.number_of_edges())

    # Enrich concept_map with derived fields
    for slug, c in concept_map.items():
        c["prerequisites"] = sorted(prereq_map.get(slug, set()))
        c["leads_to"] = sorted(
            succ for succ in G.successors(slug)
        )
        c["related"] = sorted(related_map.get(slug, set()))
        c["see_also"] = sorted(see_also_map.get(slug, set()))

    return G, concept_map


def compute_grade_views(
    G: nx.DiGraph,
    concept_map: dict[str, dict],
) -> dict[str, dict]:
    """
    For each grade, compute the subgraph of relevant concepts + entry points.
    Entry points = concepts with no prerequisites within that grade's subgraph.
    """
    all_grades = sorted(
        {g for c in concept_map.values() for g in c.get("grades", [])}
    )
    views: dict[str, dict] = {}

    for grade in all_grades:
        grade_slugs = [s for s, c in concept_map.items() if grade in c.get("grades", [])]
        grade_slug_set = set(grade_slugs)

        # Entry points: no prerequisites within this grade
        entry_points = [
            s for s in grade_slugs
            if not any(p in grade_slug_set for p in concept_map[s].get("prerequisites", []))
        ]
        views[str(grade)] = {
            "concepts": grade_slugs,
            "entry_points": entry_points,
            "count": len(grade_slugs),
        }

    return views


# ─── Persist graph ────────────────────────────────────────────────────────────

def serialise_graph(
    subject: str,
    concepts: list[dict],
    concept_map: dict[str, dict],
    G: nx.DiGraph,
    grade_views: dict[str, dict],
) -> dict:
    """Build the final graph dict for serialisation."""
    edges = [
        {"from": u, "to": v, "type": G.edges[u, v].get("type", "prerequisite")}
        for u, v in G.edges()
    ]
    return {
        "subject": subject,
        "total_concepts": len(concept_map),
        "total_edges": len(edges),
        "concepts": concept_map,
        "edges": edges,
        "grade_views": grade_views,
    }


def merge_graphs(subject_graphs: list[dict]) -> dict:
    """Merge per-subject graphs into one global graph."""
    merged_concepts: dict[str, dict] = {}
    merged_edges: list[dict] = []
    merged_views: dict[str, dict] = {}

    for sg in subject_graphs:
        merged_concepts.update(sg.get("concepts", {}))
        merged_edges.extend(sg.get("edges", []))
        for grade, view in sg.get("grade_views", {}).items():
            if grade not in merged_views:
                merged_views[grade] = {"concepts": [], "entry_points": [], "count": 0}
            merged_views[grade]["concepts"].extend(view.get("concepts", []))
            merged_views[grade]["entry_points"].extend(view.get("entry_points", []))
            merged_views[grade]["count"] += view.get("count", 0)

    return {
        "total_concepts": len(merged_concepts),
        "total_edges": len(merged_edges),
        "concepts": merged_concepts,
        "edges": merged_edges,
        "grade_views": merged_views,
    }


# ─── Main per-subject pipeline ────────────────────────────────────────────────

def process_subject(
    subject: str,
    skip_existing: bool,
) -> dict | None:
    KG_DIR.mkdir(parents=True, exist_ok=True)
    subject_out = KG_DIR / "graph_by_subject" / f"{subject}.json"
    subject_out.parent.mkdir(parents=True, exist_ok=True)

    if skip_existing and subject_out.exists():
        log.info("Skipping subject=%s (already exists)", subject)
        return json.loads(subject_out.read_text())

    log.info("=== Building knowledge graph for subject: %s ===", subject)

    # 1. Load raw topics
    grade_topics = load_raw_topics_for_subject(subject)
    if not grade_topics:
        log.warning("No raw topics found for subject=%s; run topic_ingestion.py first", subject)
        return None

    # 2. Extract canonical concept hierarchy via local LLaMA-8B (batched)
    concepts = extract_canonical_concepts(subject, grade_topics)
    if not concepts:
        log.error("No concepts extracted for subject=%s", subject)
        return None

    # 3. Extract prerequisite edges per grade via local LLaMA-8B
    edges_by_grade: dict[int, list[dict]] = {}
    relevant_grades = sorted(grade_topics.keys())
    for grade in relevant_grades:
        log.info("  Extracting prerequisite edges for grade %d …", grade)
        edges = extract_prerequisite_edges(concepts, grade, subject=subject)
        edges_by_grade[grade] = edges
        log.info("    → %d edge records", len(edges))

    # 4. Build DAG
    G, concept_map = build_dag(concepts, edges_by_grade)

    # 5. Grade views
    grade_views = compute_grade_views(G, concept_map)

    # 6. Serialise
    graph_data = serialise_graph(subject, concepts, concept_map, G, grade_views)
    subject_out.write_text(json.dumps(graph_data, ensure_ascii=False, indent=2))
    log.info("✓ Subject graph saved → %s (%d concepts)", subject_out, len(concept_map))

    # 7. Save grade-specific views
    grade_dir = KG_DIR / "graph_by_grade"
    grade_dir.mkdir(parents=True, exist_ok=True)
    for grade, view in grade_views.items():
        grade_concepts = {s: concept_map[s] for s in view["concepts"] if s in concept_map}
        grade_edges = [
            e for e in graph_data["edges"]
            if e["from"] in grade_concepts and e["to"] in grade_concepts
        ]
        grade_file = grade_dir / f"grade{grade}_{subject}.json"
        grade_file.write_text(
            json.dumps(
                {
                    "grade": int(grade),
                    "subject": subject,
                    "concepts": grade_concepts,
                    "edges": grade_edges,
                    "entry_points": view["entry_points"],
                },
                ensure_ascii=False,
                indent=2,
            )
        )

    return graph_data


def validate_graph(graph_data: dict) -> bool:
    """Quick structural validation of a graph dict. Returns True if valid."""
    ok = True
    concepts = graph_data.get("concepts", {})
    edges = graph_data.get("edges", [])

    # Check no orphan nodes (each concept should have at least one grade)
    orphans = [s for s, c in concepts.items() if not c.get("grades")]
    if orphans:
        log.warning("VALIDATION: %d concepts have no grade assignment", len(orphans))

    # Check all edge slugs resolve
    slugs = set(concepts.keys())
    bad_edges = [(e["from"], e["to"]) for e in edges if e["from"] not in slugs or e["to"] not in slugs]
    if bad_edges:
        log.warning("VALIDATION: %d edges reference unknown slugs", len(bad_edges))
        ok = False

    # Rebuild networkx graph and check DAG
    G2 = nx.DiGraph()
    for e in edges:
        G2.add_edge(e["from"], e["to"])
    if not nx.is_directed_acyclic_graph(G2):
        log.error("VALIDATION FAILED: Graph contains cycles!")
        ok = False
    else:
        log.info("VALIDATION: Graph is a valid DAG ✓")

    # Entry points per grade
    for grade, view in graph_data.get("grade_views", {}).items():
        if not view.get("entry_points"):
            log.warning("VALIDATION: Grade %s has no entry points", grade)

    return ok


# ─── CLI ──────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Stage 2 — Knowledge graph builder (uses local LLaMA-8B)")
    p.add_argument("--subject", help="Process only this subject")
    p.add_argument(
        "--model-path",
        default=os.environ.get("LLAMA_MODEL_PATH", str(Path.home() / "models" / "llama-8b")),
        help="Path to the local LLaMA-8B model",
    )
    p.add_argument("--skip-existing", action="store_true", default=True)
    p.add_argument("--no-skip-existing", dest="skip_existing", action="store_false")
    p.add_argument("--validate", action="store_true", help="Validate graph after building")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    os.environ.setdefault("LLAMA_MODEL_PATH", args.model_path)

    subjects = [args.subject] if args.subject else ALL_SUBJECTS

    subject_graphs: list[dict] = []
    for subject in subjects:
        sg = process_subject(subject, args.skip_existing)
        if sg:
            subject_graphs.append(sg)

    if not subject_graphs:
        log.error("No graphs built — nothing to merge.")
        sys.exit(1)

    # Merge into global graph
    log.info("Merging %d subject graphs into global graph.json …", len(subject_graphs))
    global_graph = merge_graphs(subject_graphs)
    global_path = KG_DIR / "graph.json"
    global_path.write_text(json.dumps(global_graph, ensure_ascii=False, indent=2))
    log.info("✓ Global graph saved → %s (%d concepts total)", global_path, global_graph["total_concepts"])

    if args.validate:
        validate_graph(global_graph)


if __name__ == "__main__":
    main()


# ─── Schema example (documentation) ──────────────────────────────────────────
GRAPH_SCHEMA_EXAMPLE = """
{
  "total_concepts": 450,
  "total_edges": 820,
  "concepts": {
    "newtons-first-law-of-motion": {
      "canonical_name": "Newton's First Law of Motion",
      "slug": "newtons-first-law-of-motion",
      "aliases": ["Law of Inertia"],
      "subject": "physics",
      "domain": "Mechanics",
      "area": "Newton's Laws of Motion",
      "parent": "newtons-laws-of-motion",
      "grades": [8, 9, 11],
      "importance_by_grade": {"8": 4, "9": 5, "11": 3},
      "source_boards": ["NCERT", "ICSE"],
      "prerequisites": ["force-and-motion", "types-of-forces"],
      "leads_to": ["newtons-second-law-of-motion"],
      "related": ["friction", "mass-and-weight"],
      "see_also": ["momentum"]
    }
  },
  "edges": [
    {"from": "force-and-motion", "to": "newtons-first-law-of-motion", "type": "prerequisite"}
  ],
  "grade_views": {
    "9": {
      "concepts": ["newtons-first-law-of-motion", "force-and-motion"],
      "entry_points": ["force-and-motion"],
      "count": 2
    }
  }
}
"""
