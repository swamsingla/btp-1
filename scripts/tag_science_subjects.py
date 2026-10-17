#!/usr/bin/env python3
"""
Tag every science concept as physics, chemistry or biology
===========================================================
The science graph is one file covering seven grades, but the books split into three
from grade 11 and a learner browsing "chemistry" should not be shown mechanics. Each
of the 36 areas is assigned below by hand.

Four areas needed their concepts read before deciding, because the name alone is
ambiguous:
  * Atomic Structure holds Mole Concept, Stoichiometry, Valency and Dalton's Atomic
    Theory -> chemistry. The physics-side atomic models live in Modern Physics.
  * Heat and Thermodynamics holds Kinetic Theory, Ideal Gas Laws and Heat Engines ->
    physics. The chemistry side is the separate Thermochemistry area.
  * Matter and Classification holds Pure Substances, Mixtures and Separation
    Techniques -> chemistry.
  * Biomolecules is taught as class 11 biology AND class 12 chemistry. Tagged biology
    because its concepts lean on biological function (Enzymes, Lipids as cell
    membrane), but it is the one genuinely arguable call here.

Two concepts are overridden individually where their area as a whole goes the other
way — an area tag cannot be right for every member.

Usage:
  python scripts/tag_science_subjects.py --check
  python scripts/tag_science_subjects.py
"""

import argparse
import json
from collections import Counter
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GRAPH = BASE / "data" / "knowledge_graph" / "science" / "graph.json"

AREA_SUBJECT: dict[str, str] = {
    # physics
    "Mechanics": "physics",
    "Electricity and Magnetism": "physics",
    "Optics": "physics",
    "Modern Physics": "physics",
    "Heat and Thermodynamics": "physics",
    "Waves and Sound": "physics",
    "Units and Measurement": "physics",
    "Gravitation": "physics",
    "Fluid Mechanics": "physics",
    "Oscillations": "physics",
    # chemistry
    "Organic Chemistry": "chemistry",
    "Atomic Structure": "chemistry",
    "Chemical Reactions": "chemistry",
    "Chemical Bonding": "chemistry",
    "Matter and Classification": "chemistry",
    "Periodic Classification": "chemistry",
    "Acids Bases and Salts": "chemistry",
    "Electrochemistry": "chemistry",
    "Solutions": "chemistry",
    "Thermochemistry": "chemistry",
    "Solid State": "chemistry",
    "Environmental Chemistry": "chemistry",
    "Surface Chemistry": "chemistry",
    "Chemical Kinetics": "chemistry",
    # biology
    "Ecology": "biology",
    "Human Physiology": "biology",
    "Genetics and Evolution": "biology",
    "Reproduction": "biology",
    "Plant Biology": "biology",
    "Cell Biology": "biology",
    "Diversity of Life": "biology",
    "Health and Disease": "biology",
    "Biomolecules": "biology",
    "Biotechnology": "biology",
    "Nutrition and Digestion": "biology",
    "Agriculture and Food Resources": "biology",
}

# An area tag cannot be right for every concept inside it.
CONCEPT_OVERRIDE: dict[str, str] = {
    # Solid State is a class 12 chemistry chapter, but band theory is class 12 physics
    "band-theory": "physics",
    # sits in the Ecology area for want of a better one; it is astronomy
    "earths-rotation-revolution": "physics",
}


def main() -> None:
    p = argparse.ArgumentParser(description="Tag science concepts by subject")
    p.add_argument("--check", action="store_true", help="report only, write nothing")
    args = p.parse_args()

    graph = json.loads(GRAPH.read_text(encoding="utf-8"))
    concepts = graph["concepts"]

    areas = {c["area"] for c in concepts.values()}
    missing = sorted(areas - set(AREA_SUBJECT))
    extra = sorted(set(AREA_SUBJECT) - areas)
    if missing:
        raise SystemExit(f"areas with no subject assigned: {missing}")
    if extra:
        print(f"note: mapping lists areas no concept uses: {extra}")
    unknown = [s for s in CONCEPT_OVERRIDE if s not in concepts]
    if unknown:
        raise SystemExit(f"override slugs not in graph: {unknown}")

    counts: Counter[str] = Counter()
    for slug, c in concepts.items():
        subject = CONCEPT_OVERRIDE.get(slug, AREA_SUBJECT[c["area"]])
        counts[subject] += 1
        if not args.check:
            c["subject"] = subject

    total = sum(counts.values())
    for subject, n in counts.most_common():
        print(f"  {subject:10}{n:>4} concepts ({100 * n / total:.0f}%)")
    print(f"  {'total':10}{total:>4}")

    if args.check:
        print("\n--check: nothing written")
        return
    GRAPH.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"\nwritten {GRAPH.relative_to(BASE).as_posix()}")


if __name__ == "__main__":
    main()
