#!/usr/bin/env python3
"""
Add hand-written concepts for topics the books teach and the graph was missing
==============================================================================
Most of the 296 "unclaimed" sections are NOT missing concepts. Two other causes
dominate, and adding a node for those would only bloat the graph:

  * TOP_K=8 caps how many passages one concept-grade pair can claim, so a big
    chapter looks uncovered even when its concept exists. Grade 11 chemistry
    chapter 6 has 130 passages and two concepts (Chemical Equilibrium, Ionic
    Equilibrium) that between them can claim at most 16.
  * Narrative headings in the new books ("Reema's Curiosity", "A Pinch of
    History") and mis-detected headings are not topics at all.

What is left is whole chapters the graph genuinely does not reach — checked by
confirming no concept with that name exists, not by a similarity threshold.
Every concept below was written by hand: grades from where the books teach it,
prerequisites chosen from existing slugs and deliberately kept at or below the
concept's own grade so this does not recreate the backwards edges step 2 removed.

Usage:
  python scripts/add_concepts.py --check     # validate, write nothing
  python scripts/add_concepts.py
"""

import argparse
import json
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
GRAPHS = {s: BASE / "data" / "knowledge_graph" / s / "graph.json" for s in ("maths", "science")}

NEW: dict[str, dict[str, dict]] = {
    "science": {
        # Grade 7 chapter 12 — nothing in the graph mentioned eclipses at all
        "solar-eclipse": {
            "canonical_name": "Solar Eclipse",
            "grades": [7],
            "area": "Optics",
            "description": "The Moon passes between the Sun and the Earth and its shadow falls on the Earth",
            "aliases": ["solar eclipse", "eclipse of the Sun", "Moon's shadow on the Earth"],
            "prerequisites": ["rectilinear-propagation", "light-sources-and-shadows",
                              "earths-rotation-revolution"],
            "leads_to": [],
        },
        "lunar-eclipse": {
            "canonical_name": "Lunar Eclipse",
            "grades": [7],
            "area": "Optics",
            "description": "The Earth passes between the Sun and the Moon, so the Moon moves through the Earth's shadow",
            "aliases": ["lunar eclipse", "eclipse of the Moon", "Earth's shadow on the Moon"],
            "prerequisites": ["rectilinear-propagation", "light-sources-and-shadows",
                              "earths-rotation-revolution"],
            "leads_to": [],
        },
        # Grade 7 chapter 6 — a whole chapter with no concept anywhere near it
        "adolescence-and-puberty": {
            "canonical_name": "Adolescence and Puberty",
            "grades": [7],
            "area": "Reproduction",
            "description": "Physical and emotional changes of the teenage years and the onset of reproductive capability",
            "aliases": ["puberty", "growing with age", "the teenage years",
                        "changes at adolescence"],
            "prerequisites": ["health-and-hygiene"],
            "leads_to": ["human-reproductive-system", "reproductive-health"],
        },
        # Grade 7 chapter 3 — electricity is introduced here, but every electricity
        # concept in the graph starts at grade 8
        "electrical-conductors-insulators": {
            "canonical_name": "Electrical Conductors and Insulators",
            "grades": [7],
            "area": "Electricity and Magnetism",
            "description": "Materials that let electric current pass through them and materials that do not",
            "aliases": ["conductors and insulators", "materials that conduct electricity",
                        "testing whether a material conducts"],
            "prerequisites": [],
            "leads_to": ["electric-circuit", "electric-current"],
        },
        "circuit-diagrams-symbols": {
            "canonical_name": "Circuit Diagrams and Symbols",
            "grades": [7],
            "area": "Electricity and Magnetism",
            "description": "Standard symbols for a cell, switch, bulb and wires, and drawing a circuit from them",
            "aliases": ["circuit diagram", "symbols for circuit components",
                        "electric switch", "drawing an electric circuit"],
            "prerequisites": [],
            "leads_to": ["electric-circuit"],
        },
        # Grade 6 chapter 11 — resources; the graph only had these from grade 10
        "fossil-fuels": {
            "canonical_name": "Fossil Fuels",
            "grades": [6],
            "area": "Ecology",
            "description": "Coal, petroleum and natural gas formed from the remains of ancient organisms; exhaustible",
            "aliases": ["coal and petroleum", "natural gas", "non-renewable fuels"],
            "prerequisites": [],
            "leads_to": ["natural-resources-management", "air-pollution"],
        },
        "forests-and-their-importance": {
            "canonical_name": "Forests and Their Importance",
            "grades": [6],
            "area": "Ecology",
            "description": "Forests as a resource: oxygen, timber, habitat for wildlife and protection of soil",
            "aliases": ["forests", "why forests matter", "deforestation"],
            "prerequisites": [],
            "leads_to": ["biodiversity", "natural-resources-management"],
        },
        # Grade 8 chapter 12 — ecosystem interactions at grade 8 level
        "decomposition-and-recycling": {
            "canonical_name": "Decomposition and Nutrient Recycling",
            "grades": [8],
            "area": "Ecology",
            "description": "Decomposers break down dead matter and return nutrients to the soil",
            "aliases": ["what happens to waste in nature", "decomposers",
                        "breakdown of dead matter", "composting"],
            "prerequisites": ["microorganisms"],
            "leads_to": ["nitrogen-cycle", "carbon-cycle", "energy-flow-in-ecosystem"],
        },
        "organism-interactions": {
            "canonical_name": "Interactions Among Organisms",
            "grades": [8],
            "area": "Ecology",
            "description": "How living things affect one another and their surroundings: predation, competition and living together",
            "aliases": ["interactions among organisms and their surroundings",
                        "who lives together in nature", "balance in ecosystems"],
            "prerequisites": ["ecosystem-concept", "food-chains-and-webs"],
            "leads_to": ["population-interactions"],
        },
        # Grade 9 chapter 12 — a 29-passage chapter with one claimed passage
        "crop-improvement": {
            "canonical_name": "Crop Variety Improvement",
            "grades": [9],
            "area": "Agriculture and Food Resources",
            "description": "Breeding crop varieties for higher yield, disease resistance and better quality",
            "aliases": ["crop variety improvement", "hybridisation of crops",
                        "improvement in crop yields", "plant breeding for yield"],
            "prerequisites": [],
            "leads_to": ["crop-production-management"],
        },
        "crop-production-management": {
            "canonical_name": "Crop Production and Management",
            "grades": [9],
            "area": "Agriculture and Food Resources",
            "description": "Nutrient management, irrigation, cropping patterns and protection of crops from pests and weeds",
            "aliases": ["nutrient management", "irrigation", "cropping patterns",
                        "crop protection management", "manure and fertilisers"],
            "prerequisites": ["soil-types-and-formation", "crop-improvement"],
            "leads_to": [],
        },
        "animal-husbandry": {
            "canonical_name": "Animal Husbandry",
            "grades": [9],
            "area": "Agriculture and Food Resources",
            "description": "Scientific rearing of cattle, poultry, fish and bees for food and other produce",
            "aliases": ["cattle farming", "poultry farming", "fish production",
                        "bee-keeping", "marine and inland fisheries"],
            "prerequisites": [],
            "leads_to": [],
        },
    },
    "maths": {
        # Grade 6 chapter 3 (Number Play) — 4 of 35 passages claimed
        "estimation": {
            "canonical_name": "Estimation and Approximation",
            "grades": [6],
            "area": "Number Systems",
            "description": "Judging a value quickly by rounding to convenient numbers, and checking whether an answer is reasonable",
            "aliases": ["simple estimation", "rounding off", "approximate value",
                        "mental math"],
            "prerequisites": ["place-value", "whole-numbers"],
            "leads_to": [],
        },
        "palindromic-numbers": {
            "canonical_name": "Palindromic Numbers",
            "grades": [6],
            "area": "Number Theory",
            "description": "Numbers that read the same forwards and backwards, and the patterns made while building them",
            "aliases": ["palindrome", "pretty palindromic patterns",
                        "numbers that read the same both ways"],
            "prerequisites": ["place-value", "number-patterns"],
            "leads_to": [],
        },
    },
}


def main() -> None:
    p = argparse.ArgumentParser(description="Add hand-written concepts to the graphs")
    p.add_argument("--check", action="store_true", help="validate only, write nothing")
    args = p.parse_args()

    for subject, additions in NEW.items():
        path = GRAPHS[subject]
        graph = json.loads(path.read_text(encoding="utf-8"))
        concepts = graph["concepts"]

        clash = [s for s in additions if s in concepts]
        if clash:
            raise SystemExit(f"{subject}: already present: {clash}")
        known = set(concepts) | set(additions)
        for slug, c in additions.items():
            bad = [r for r in c["prerequisites"] + c["leads_to"] if r not in known]
            if bad:
                raise SystemExit(f"{subject}/{slug}: unknown related slugs {bad}")

        # a prerequisite must not be taught after the concept that needs it
        def min_grade(s: str) -> int:
            return min((concepts.get(s) or additions[s])["grades"])

        for slug, c in additions.items():
            for pre in c["prerequisites"]:
                if min_grade(pre) > min(c["grades"]):
                    raise SystemExit(f"{subject}/{slug}: prerequisite {pre} is taught later")
            for nxt in c["leads_to"]:
                if min_grade(nxt) < min(c["grades"]):
                    raise SystemExit(f"{subject}/{slug}: leads_to {nxt} is taught earlier")

        if args.check:
            print(f"{subject}: {len(additions)} concepts validate cleanly")
            continue

        for slug, c in additions.items():
            concepts[slug] = {"canonical_name": c["canonical_name"], "slug": slug,
                              "grades": c["grades"], "area": c["area"],
                              "description": c["description"], "aliases": c["aliases"],
                              "prerequisites": list(c["prerequisites"]),
                              "leads_to": list(c["leads_to"])}
        # Mirror each link on the other concept and add the edge. A link between two
        # concepts in this same batch is declared twice — once as a prerequisite and
        # once as a leads_to — so the edge set has to be deduplicated.
        seen = {(e["from"], e["to"]) for e in graph["edges"]}

        def link(pre: str, post: str) -> None:
            concepts[pre].setdefault("leads_to", [])
            if post not in concepts[pre]["leads_to"]:
                concepts[pre]["leads_to"].append(post)
            concepts[post].setdefault("prerequisites", [])
            if pre not in concepts[post]["prerequisites"]:
                concepts[post]["prerequisites"].append(pre)
            if (pre, post) not in seen:
                seen.add((pre, post))
                graph["edges"].append({"from": pre, "to": post, "type": "prerequisite"})

        for slug, c in additions.items():
            for pre in c["prerequisites"]:
                link(pre, slug)
            for nxt in c["leads_to"]:
                link(slug, nxt)

        graph["total_concepts"] = len(concepts)
        graph["total_edges"] = len(graph["edges"])
        path.write_text(json.dumps(graph, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"{subject}: +{len(additions)} concepts -> {len(concepts)}, "
              f"{len(graph['edges'])} edges")
        for slug, c in additions.items():
            print(f"    {c['canonical_name'][:38]:40} gr{c['grades']}  {c['area']}")


if __name__ == "__main__":
    main()
