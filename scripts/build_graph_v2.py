#!/usr/bin/env python3
"""
Build graph_v2: only the concept-grade pairs whose OWN grade's book teaches them
================================================================================
Writes, without touching the original graphs:
  data/knowledge_graph/maths/graph_v2.json
  data/knowledge_graph/science/graph_v2.json
  data/knowledge_graph/graph_v2_report.json   (every pair kept or dropped, and why)

Why this exists. A concept listed at two grades gets one page per grade, and the later
page is supposed to go further. When a grade has no text of its own, retrieval borrows
the other grade's extracts, both pages are written from the same text, and the second
comes back as a copy (74-100% word for word, measured) however the prompt asks for more
depth. The fix is in the graph, not the prompt: list a concept only at the grades whose
book actually teaches it.

A pair is kept when ALL of these hold:
  1. build_context.build() anchors it only on its own grade's text (grade_delta 0, no
     sibling-grade skip), at least MIN_SOURCE_WORDS words of it;
  2. a human read of the anchor chapter/section titles (2026-10-17) says that text is a
     section ABOUT the concept, not a neighbouring topic. Pairs ruled otherwise are in
     NOT_IN_BOOK (mostly topics NCERT deleted in the 2022-23 rationalisation), PART_OF
     (taught only inside a broader section another concept owns) or DUPLICATE (the same
     section already carries another concept in that grade);
  3. RESCUE: a few pairs retrieval scored weak, and so sent to another grade, although
     the grade's own chapter teaches them. They are kept with a `source_sections` pin.

Two exceptions, both added 2026-10-17 at the user's request:
  GENERATED  every Grade 6-8 page already generated and hand-audited in all its languages
             is kept even where the rule above would drop it (the work is done and paid
             for). Their rulings stay in the tables below as the record; the build reports
             them separately and does not hold them to the own-grade or floor checks.
  ADD        Grade 9-12 pairs added by reading the books for sections no kept pair used:
             each is pinned to its own section of its own grade's book, so it passes the
             same checks as every other pair.

Edges. Only prerequisite edges between kept concepts survive. A kept concept that
needed a removed one inherits that one's own prerequisites (so a chain A -> X -> B
becomes A -> B), unless the new edge is already implied by another path. Then every
edge whose prerequisite is first taught LATER than the concept is dropped, and the
result is checked for cycles with sync_graphs.validate().

Usage:
  python scripts/build_graph_v2.py            # build, verify, write
  python scripts/build_graph_v2.py --check    # build and verify, write nothing
"""

import argparse
import copy
import json
import math
import sys
from collections import defaultdict
from pathlib import Path

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "scripts"))
import build_context as bc          # noqa: E402
from sync_graphs import validate, late_prerequisites   # noqa: E402

KG = BASE / "data" / "knowledge_graph"
OUT = {s: KG / s / "graph_v2.json" for s in ("maths", "science")}
REPORT = KG / "graph_v2_report.json"
PAGES = BASE / "data" / "generated_pages"

# ── Hand rulings, from reading every kept pair's anchor titles (2026-10-17) ─────────

# The grade's book does not teach it; retrieval took the nearest section.
NOT_IN_BOOK = {
    "maths": {
        6: ["natural-numbers", "whole-numbers"],
        7: ["similar-triangles", "simple-interest"],
        8: ["rational-number-operations"],
        9: ["constructions-triangles", "logarithms", "median-of-triangle", "remainder-theorem"],
        10: ["centroid", "complementary-angle-identities", "completing-the-square",
             "construction-of-tangents", "constructions-advanced", "cross-multiplication-method",
             "euclidean-algorithm", "euclidean-division-lemma", "ogive"],
        11: ["ap-advanced", "coefficient-of-variation", "family-of-lines", "general-term-binomial",
             "principle-of-mathematical-induction", "section-formula-3d", "sum-of-special-series",
             "system-of-inequalities", "trigonometric-equations"],
        12: ["angle-between-planes", "area-between-two-curves", "bernoulli-trials",
             "binomial-distribution", "cramers-rule", "distance-point-to-plane", "equation-of-plane",
             "mean-value-theorem", "probability-distribution", "properties-of-determinants",
             "random-variables", "rolles-theorem", "scalar-triple-product"],
    },
    "science": {
        6: ["measurement-of-mass", "physical-quantities"],
        9: ["centripetal-force", "conservation-of-momentum", "human-ear", "measurement-of-mass",
            "mole-concept"],
        10: ["biogeochemical-cycles", "darwins-theory", "electric-motor", "electromagnetic-induction",
             "speciation", "total-internal-reflection"],
        11: ["gaseous-state", "inclined-plane", "inorganic-qualitative-analysis", "liquid-state",
             "pulleys-and-strings", "relative-motion", "rolling-motion"],
        12: ["crystal-defects", "crystal-lattice-and-packing", "ecological-succession",
             "ecosystem-services", "p-block-elements", "solid-state", "strategies-for-food-enhancement",
             "transistor", "concentration-of-solutions"],
    },
}

# Taught, but only inside a broader section that another concept's page covers.
PART_OF = {
    "maths": {
        6: ["number-line", "types-of-fractions"],
        7: ["conversion-fractions-decimals", "terms-coefficients-degree"],
        8: ["area-of-trapezium", "cube-roots", "direct-and-inverse-variation", "mean-median-mode",
            "profit-loss-percentage", "square-roots", "tax-and-vat"],
        9: ["frequency-polygon", "histogram"],
        10: ["circumference-and-area-of-circle", "consistency-of-system", "experimental-probability",
             "quadratic-formula", "volume-cylinder"],
        11: ["addition-theorem-probability", "combinations-applications",
             "derivatives-trig", "general-equation-of-line",
             "multiple-angle-formulas", "product-to-sum-formulas",
             "angle-between-two-lines"],
        12: ["continuity-types", "differentiability", "equivalence-relations", "inverse-functions",
             "logarithmic-differentiation", "system-of-inequalities"],
    },
    "science": {
        6: ["fossil-fuels", "si-units", "states-of-matter-chemistry"],
        7: ["modes-of-nutrition", "transpiration"],
        8: ["air-pollution", "antibiotics-and-vaccines", "natural-disasters"],
        9: ["blood-composition", "daltons-atomic-theory", "momentum", "wave-motion", "wave-properties"],
        10: ["energy-flow-in-ecosystem", "fertilisation-and-development", "flower-structure",
             "plane-mirrors", "rectilinear-propagation"],
        11: ["alternation-of-generations", "lipids",
             "p-block-elements", "s-block-elements", "spring-mass-system",
             # 94 words inside 1.5 "Laws of chemical combinations"; the rest of what
             # retrieval gave it was the equilibrium chapter.
             "law-of-conservation-of-mass"],
        12: ["catalysis", "faradays-laws-of-electrolysis",
             "radioactivity", "sexual-reproduction-overview", "speciation"],
    },
}

# Same section, same grade, already carried by the concept named after the arrow.
DUPLICATE = {
    "maths": {
        6: {"area-rectangle-square": "area"},
        7: {"simple-equations": "linear-equations-one-variable"},
        9: {"quadrilaterals": "properties-of-parallelogram",
            "parallel-lines-and-transversals": "lines-angles-theorems"},
        10: {"probability-basic": "theoretical-probability",
             "probability-theoretical-approach": "theoretical-probability",
             "similar-triangles-advanced": "similar-triangles",
             "statistics-measures": "mean-of-grouped-data",
             "vieta-s-formulas": "zeroes-coefficients-relationship"},
        11: {"gp-advanced": "geometric-progressions",
             "algebra-of-complex-numbers": "complex-numbers",
             "factorial": "permutations"},
        12: {"applications-of-derivatives": "rate-of-change",
             "graphical-method-lpp": "linear-programming",
             "partial-fractions": "integration-by-partial-fractions"},
    },
    "science": {
        7: {"human-respiratory-system": "breathing-and-gas-exchange"},
        9: {"change-of-state-chemistry": "change-of-state",
            "mass-and-inertia": "inertia"},
        10: {"plant-reproduction-asexual": "asexual-reproduction"},
        11: {"biological-classification-detail": "five-kingdom-classification",
             "chemical-coordination": "endocrine-system",
             "hormones-and-feedback": "endocrine-system",
             "dimensional-formula-applications": "dimensional-analysis",
             "excretory-system-detail": "excretory-system",
             "mendeleevs-periodic-table": "elements-classification-early"},
        12: {"electrochemical-cells": "electrode-potential",
             "fertilisation-and-development": "embryo-development",
             "heredity-and-variation": "mendels-laws",
             "nuclear-energy-sources": "nuclear-fission-fusion"},
    },
}

# Kept pairs whose retrieved anchors were the wrong part of the right book: pin the
# section that actually teaches them. Entries are section titles or passage ids.
PIN = {
    ("maths", "basic-proportionality-theorem", 10): ["6.3 Similarity of Triangles"],
    ("maths", "zeroes-of-a-polynomial", 10): ["2.2 Geometrical Meaning of the Zeroes of a Polynomial"],
    ("maths", "inverse-trigonometric-functions", 12): ["2.2 Basic Concepts"],
    # Grade 6 chapter 9 is the separation chapter; its prose has no section headings.
    ("science", "separation-techniques", 6): ["g6_science_chapter9_000", "g6_science_chapter9_001",
                                              "g6_science_chapter9_002", "g6_science_chapter9_015"],
    # The Grade 9/10 books put the exposition inside "Activity" blocks, which retrieval
    # skips as non-prose; the 11.4 prose block on its own is 22 words.
    ("science", "ohms-law", 10): [f"g10_science_chapter11_{i:03d}" for i in range(8, 14)],
    ("science", "kinetic-energy", 9): [f"g9_science_chapter10_{i:03d}" for i in range(15, 20)],
    ("science", "asexual-reproduction", 10): ["7.2.1 Fission", "g10_science_chapter7_009",
                                              "7.2.3 Regeneration", "7.2.4 Budding",
                                              "7.2.5 Vegetative Propagation", "7.2.6 Spore Formation"],
    ("science", "ecosystem-concept", 10): ["g10_science_chapter13_001", "g10_science_chapter13_002",
                                           "g10_science_chapter13_003", "g10_science_chapter13_004"],
    ("science", "dispersion-of-light", 10): [f"g10_science_chapter10_{i:03d}" for i in range(8, 14)],
    ("science", "buoyancy-and-archimedes", 9): ["g9_science_chapter9_025", "g9_science_chapter9_026",
                                                "g9_science_chapter9_027", "g9_science_chapter9_028",
                                                "g9_science_chapter9_029", "g9_science_chapter9_030",
                                                "g9_science_chapter9_032", "g9_science_chapter9_033"],
    ("science", "magnetic-effect-of-current", 10): [f"g10_science_chapter12_{i:03d}" for i in range(6, 12)],
    ("science", "force-on-current-in-magnetic-field", 10): [f"g10_science_chapter12_{i:03d}"
                                                            for i in range(18, 22)],
    ("science", "acids-bases-indicators", 10): ["g10_science_chapter2_000", "g10_science_chapter2_001",
                                                "g10_science_chapter2_002", "g10_science_chapter2_003"],
    ("science", "properties-of-acids-bases", 10): [f"g10_science_chapter2_{i:03d}"
                                                   for i in (4, 5, 6, 7, 8, 9, 11, 12)],
    ("science", "reactions-of-hydrocarbons", 10): [f"g10_science_chapter4_{i:03d}" for i in range(21, 29)],
    ("science", "colloids", 9): ["2.2.2 WHAT IS A SUSPENSION?", "2.2.3 WHAT IS A COLLOIDAL SOLUTION?"],
    ("science", "decomposition-and-recycling", 8): ["12.6 What Happens to Waste in Nature?",
                                                    "13.4.2 Soil, rocks, and minerals",
                                                    "13.4.3 Plants, animals, and microorganisms"],
    ("science", "body-fluids-and-circulation", 11): [f"g11_biology_chapter15_{i:03d}"
                                                     for i in range(1, 10)],
    ("science", "classification-of-organisms", 11): [
        "1.2 TAXONOMIC CATEGORIES", "1.2.1 Species", "1.2.2 Genus", "1.2.3 Family", "1.2.4 Order",
        "1.2.5 Class", "1.2.6 Phylum", "1.2.7 Kingdom"],
    ("maths", "measures-of-dispersion", 11): ["13.2 Measures of Dispersion", "13.3 Range",
                                              "g11_maths_chapter13_005", "g11_maths_chapter13_006",
                                              "g11_maths_chapter13_007"],
    # Removing rival concepts frees anchor slots, and these four then picked up a wrong
    # section (plant seeds for animal reproduction, friction for Newton's first law).
    ("science", "animal-reproduction", 12): ["2.3 GAMETOGENESIS", "2.5 FERTILISATION AND IMPLANTATION"],
    ("science", "human-reproductive-system", 10): ["7.3.3 (a) Male Reproductive System",
                                                   "7.3.3 (b) Female Reproductive System",
                                                   "7.3.3 Reproduction in Human Beings"],
    ("science", "newtons-first-law", 11): ["4.2 ARISTOTLE'S FALLACY", "4.3 THE LAW OF INERTIA",
                                           "4.4 NEWTON'S FIRST LAW OF MOTION"],
    ("science", "torque", 11): ["6.7.1 Moment of force (Torque)"],
    ("science", "solar-eclipse", 7): ["12.3 Eclipses", "12.3.1 Solar eclipse"],
    # Same-grade sibling concepts that retrieval fed IDENTICAL sections: give each its own.
    ("maths", "properties-of-triangles", 7): ["7.1 Equilateral Triangles",
                                              "7.2 Constructing a Triangle When its Sides are Given",
                                              "1.3 Angles of Isosceles and Equilateral Triangles"],
    ("maths", "substitution-method", 10): ["3.3 Algebraic Methods of Solving a Pair of Linear Equations"],
    ("maths", "elimination-method", 10): ["3.3.2 Elimination Method"],
    ("maths", "real-numbers", 9): ["1.1 Introduction", "1.4 Operations on Real Numbers"],
    ("maths", "laws-of-exponents-real", 9): ["1.5 Laws of Exponents for Real Numbers"],
    ("maths", "surface-area-cone", 9): ["11.1 Surface Area of a Right Circular Cone"],
    ("maths", "surface-area-sphere", 9): ["11.2 Surface Area of a Sphere"],
    ("maths", "types-of-functions", 12): ["1.3 Types of Functions"],
    ("maths", "composition-of-functions", 12): ["1.4 Composition of Functions and Invertible Function"],
    ("science", "five-kingdom-classification", 11): [
        "g11_biology_chapter2_000", "g11_biology_chapter2_001", "g11_biology_chapter2_002",
        "g11_biology_chapter2_003", "2.1 KINGDOM MONERA", "2.2 KINGDOM PROTISTA",
        "2.3 KINGDOM FUNGI", "2.4 KINGDOM PLANTAE", "2.5 KINGDOM ANIMALIA"],
}
# Pairs whose own chapter retrieval missed (scored under the 0.78 cutoff); kept with a pin.
RESCUE = {
    ("maths", "prime-numbers", 6): ["5.2 Prime Numbers"],
    ("maths", "prime-factorisation", 6): ["5.4 Prime Factorisation"],
    ("science", "nervous-system", 10): ["6.1 ANIMALS - NERVOUS SYSTEM", "6.1.2 Human Brain",
                                        "6.1.4 How does the Nervous Tissue cause Action?"],
    ("science", "photosynthesis", 10): [f"g10_science_chapter5_{i:03d}" for i in range(7, 12)],
    ("science", "conservation-of-energy", 11): ["5.8 THE CONSERVATION OF MECHANICAL ENERGY"],
    ("science", "reactions-of-hydrocarbons", 11): ["9.3.5 Properties"],
}

# Kept pairs whose anchors were mostly the wrong section (found 2026-10-17 while reading
# every unused section of the Grade 9-12 books): pin the section the page is about.
# Several of these also hand a section to a pair in ADD below, so the two do not overlap.
PIN.update({
    ("maths", "introduction-3d-geometry", 11): [
        "11.1 Introduction", "11.2 Coordinate Axes and Coordinate Planes in Three Dimensional Space",
        "11.3 Coordinates of a Point in Space"],                      # was: three chapter intros
    ("maths", "conic-sections", 11): ["10.1 Introduction", "10.2 Sections of a Cone"],
    ("maths", "distance-point-to-line", 11): ["9.4 Distance of a Point From a Line",
                                              "9.4.1 Distance between two"],
    # The 12.3 text is filed as kind "summary" after its first three passages.
    ("maths", "limits-intuitive", 11): ["12.3 Limits"] + [f"g11_maths_chapter12_{i:03d}"
                                                          for i in range(9, 15)],
    ("maths", "permutations", 11): ["6.3 Permutations",
                                    "6.3.1 Permutations when all the objects are distinct",
                                    "g11_maths_chapter6_012", "g11_maths_chapter6_013"],
    ("maths", "matrices", 12): ["3.1 Introduction", "3.2 Matrix", "3.2.1 Order of a matrix"],
    ("maths", "transpose-of-matrix", 12): ["3.5.1 Properties of transpose of the matrices"],
    ("maths", "vectors", 12): ["10.1 Introduction", "10.2 Some Basic Concepts"],
    ("maths", "scalar-multiplication-vectors", 12): ["10.5 Multiplication of a Vector by a Scalar",
                                                     "10.5.1 Components of a vector"],
    ("maths", "special-integrals", 12): ["7.4 Integrals of Some Particular Functions"],
    ("science", "human-respiratory-system", 11): ["14.1 RESPIRATORY ORGANS",
                                                  "14.1.1 Human Respiratory System",
                                                  "14.2 MECHANISM OF BREATHING",
                                                  "14.2.1 Respiratory Volumes and Capacities"],
    ("science", "cell-membrane", 11): ["8.5.1 Cell Membrane"],        # was: + gas exchange
    ("science", "nervous-system", 11): [
        "18.1 NEURAL SYSTEM", "18.2 HUMAN NEURAL SYSTEM",
        "18.3 NEURON AS STRUCTURAL AND FUNCTIONAL UNIT OF NEURAL SYSTEM",
        "18.3.1 Generation and Conduction of Nerve Impulse", "18.3.2 Transmission of Impulses"],
    ("science", "locomotion-and-movement-detail", 11): [
        "17.1 TYPES OF MOVEMENT", "17.2.2 Mechanism of Muscle Contraction", "17.4 JOINTS",
        "17.5 DISORDERS OF MUSCULAR AND SKELETAL SYSTEM"],
    ("science", "cellular-respiration", 11): ["12.4 AEROBIC RESPIRATION",
                                              "12.5 THE RESPIRATORY BALANCE SHEET",
                                              "12.6 AMPHIBOLIC PATHWAY",
                                              "12.7 RESPIRATORY QUOTIENT"],
    ("science", "chemical-thermodynamics-systems", 11): [             # was: equilibrium 6.4.1
        "5.1 THERMODYNAMIC TERMS", "5.1.1 The System and the Surroundings",
        "5.1.2 Types of the System", "5.1.3 The State of the System",
        "5.1.4 The Internal Energy as a State Function"],
    ("science", "molecular-formula-calculations", 11): ["1.9 PERCENTAGE COMPOSITION",
                                                        "1.9.1 Empirical Formula for Molecular Formula"],
    ("science", "reaction-mechanisms", 11): [                         # was: + redox 7.2
        "8.7 FUNDAMENTAL CONCEPTS IN ORGANIC REACTION MECHANISM",
        "8.7.1 Fission of a Covalent Bond", "8.7.2 Substrate and Reagent",
        "8.7.3 Electron Movement in Organic Reactions"],
    ("science", "emf-and-internal-resistance", 12): [                 # was: + inductance
        "3.10 CELLS, EMF, INTERNAL RESISTANCE", "3.11 CELLS IN SERIES AND IN PARALLEL"],
    ("science", "amperes-law", 12): ["4.6 AMPERE'S CIRCUITAL LAW", "4.7 THE SOLENOID"],
    ("science", "ohms-law", 12): ["3.4 Ohm's LAW", "3.6 LIMITATIONS OF OHM'S LAW"],
    ("science", "resistance-and-resistivity", 12): [                  # was: + AC phasors
        "3.5 DRIFT OF ELECTRONS AND THE ORIGIN OF RESISTIVITY",
        "3.8 TEMPERATURE DEPENDENCE OF RESISTIVITY"],
    ("science", "electric-generator", 12): ["6.8 AC GENERATOR"],      # was: + AC capacitor
    ("science", "displacement-current", 12): ["g12_physics_part1_chapter8_001",
                                              "g12_physics_part1_chapter8_002",
                                              "8.2 DISPLACEMENT CURRENT"],
    ("science", "polarisation", 12): ["10.7 POLARISATION"],           # was: + mirrors
    ("science", "magnetic-field", 12): ["g12_physics_part1_chapter5_000",
                                        "g12_physics_part1_chapter5_001",
                                        "5.2.1 The magnetic field lines"],
    ("science", "magnetic-properties-of-matter", 12): [               # was: + matter waves
        "5.4 MAGNETISATION AND MAGNETIC INTENSITY", "5.5 MAGNETIC PROPERTIES OF MATERIALS",
        "5.5.1 Diamagnetism", "5.5.2 Paramagnetism", "5.5.3 Ferromagnetism"],
    ("science", "semiconductor-basics", 12): ["14.3 INTRINSIC SEMICONDUCTOR",
                                              "14.4 EXTRINSIC SEMICONDUCTOR"],
    ("science", "recombinant-dna-technology", 12): [
        "9.2 TOOLS OF RECOMBINANT DNA TECHNOLOGY", "9.2.1 Restriction Enzymes",
        "9.2.2 Cloning Vectors",
        "9.2.3 Competent Host (For Transformation with Recombinant DNA)",
        "9.3 PROCESSES OF RECOMBINANT DNA TECHNOLOGY"],
    ("science", "biotechnology-principles", 12): ["9.1 PRINCIPLES OF BIOTECHNOLOGY"],
    # These two moved when the additions changed which rival concepts exist: excretion
    # lost "16.2 URINE FORMATION" and atomic models picked up de Broglie's postulate.
    ("science", "excretory-system", 11): ["16.1 HUMAN EXCRETORY SYSTEM", "16.2 URINE FORMATION",
                                          "16.3 FUNCTION OF THE TUBULES",
                                          "16.4 MECHANISM OF CONCENTRATION OF THE FILTRATE",
                                          "16.6 MICTURITION",
                                          "16.8 DISORDERS OF THE EXCRETORY SYSTEM"],
    ("science", "atomic-models-physics", 12): ["12.1 INTRODUCTION", "12.2 ALPHA-PARTICLE SCATTERING AND",
                                               "12.2.1 Alpha-particle trajectory"],
    # Moved when SCOPE cut their rivals and freed anchor slots (2026-10-17).
    ("science", "atomic-models-physics", 9): ["4.2 The Structure of an Atom",
                                              "4.2.1 THOMSON'S MODEL OF AN ATOM",
                                              "4.2.2 RUTHERFORD'S MODEL OF AN ATOM",
                                              "4.2.3 BOHR'S MODEL OF ATOM"],
    ("science", "valency-chemistry", 9): [
        "4.3 How are Electrons Distributed in Different Orbits (Shells)?", "4.4 Valency"],
    ("science", "newtons-second-law", 9): ["8.4 Second Law of Motion",
                                           "8.4.1 MATHEMATICAL FORMULATION OF SECOND LAW OF MOTION"],
    # law-of-constant-proportions was cut, so this page takes 3.1 whole
    ("science", "law-of-conservation-of-mass", 9): ["3.1 Laws of Chemical Combination",
                                                    "3.1.1 LAW OF CONSERVATION OF MASS",
                                                    "3.1.2 LAW OF CONSTANT PROPORTIONS"],
    ("science", "excretory-system", 10): ["5.5 EXCRETION", "5.5.1 Excretion in Human Beings"],
    ("science", "human-circulatory-system", 11): [
        "15.1 BLOOD", "15.1.1 Plasma", "15.1.2 Formed Elements", "15.3 CIRCULATORY PATHWAYS",
        "15.3.1 Human Circulatory System", "15.3.2 Cardiac Cycle", "15.4 DOUBLE CIRCULATION",
        "15.6 DISORDERS OF CIRCULATORY SYSTEM"],
    ("science", "first-law-of-thermodynamics", 11): ["11.4 HEAT, INTERNAL ENERGY AND WORK",
                                                     "11.5 FIRST LAW OF THERMODYNAMICS",
                                                     "11.8.2 Isothermal process",
                                                     "11.8.3 Adiabatic process"],
    ("science", "snells-law", 12): ["9.3 REFRACTION", "9.4 TOTAL INTERNAL REFLECTION",
                                    "9.4.1 Total internal reflection in nature and its "
                                    "technological applications"],
    ("science", "diffraction", 12): ["10.6 DIFFRACTION", "10.6.1 The single slit",
                                     "10.6.2 Seeing the single slit diffraction pattern"],
})

# Grade 6-8 pages already generated and hand-audited, kept although the rule drops them
# (borrowed-grade text, not in the book, part of a section, or a duplicate). Six of the
# Grade 8 ones are English only so far: linear-equations-one-variable, area-of-triangles,
# perpendicular-bisector, modular-arithmetic, electric-circuit, metals-nonmetals-properties.
GENERATED = {
    "maths": {
        6: ["area-rectangle-square", "composite-numbers", "estimation", "even-and-odd-numbers",
            "fibonacci-virahanka-sequence", "natural-numbers", "number-line", "place-value",
            "types-of-fractions", "whole-numbers"],
        7: ["angle-sum-property-triangle", "area-of-triangles", "circumference-of-circle",
            "conversion-fractions-decimals", "frequency-distribution", "ratios-and-proportions",
            "similar-triangles", "simple-equations", "simple-interest",
            "terms-coefficients-degree"],
        8: ["area-of-circle", "area-of-parallelogram", "area-of-trapezium", "area-of-triangles",
            "converse-of-pythagorean-theorem", "cube-roots", "direct-and-inverse-variation",
            "division-of-polynomials", "factorisation-expressions",
            "linear-equations-one-variable", "mean-median-mode", "modular-arithmetic",
            "number-line-rational", "perpendicular-bisector", "profit-loss-percentage", "range",
            "rational-number-operations", "rational-numbers", "square-roots", "tax-and-vat"],
    },
    "science": {
        6: ["earths-rotation-revolution", "fossil-fuels", "measurement-of-mass",
            "measurement-of-time", "physical-quantities", "rest-and-motion", "si-units",
            "states-of-matter-chemistry", "water-cycle"],
        7: ["classification-of-organisms", "diversity-of-organisms", "flower-structure",
            "heat-and-temperature", "human-digestive-system", "human-respiratory-system",
            "modes-of-nutrition", "plant-reproduction-asexual", "seed-formation", "transpiration"],
        8: ["air-pollution", "antibiotics-and-vaccines", "electric-circuit", "fluid-pressure",
            "friction", "metals-nonmetals-properties", "natural-disasters",
            "sustainable-development"],
    },
}
GENERATED_PAIRS = {(s, x, g) for s, by_grade in GENERATED.items()
                   for g, xs in by_grade.items() for x in xs}

# Grade 9-12 pairs added 2026-10-17 from sections of the books that no kept pair used.
# Each names its own section; several are grades the old graph never listed for that
# concept (equations of motion is taught again, from scratch, in Grade 11 physics 2.4).
# G9/G10 science explanations sit in "Activity" blocks, so those are pinned by passage id.
ADD = {
    # maths
    ("maths", "permutations-with-repetition", 11): [f"g11_maths_chapter6_{i:03d}"
                                                    for i in range(14, 22)],   # 6.3.4
    ("maths", "binomial-coefficients", 11): ["7.2 Binomial Theorem for Positive Integral Indices"],
    ("maths", "limits-algebra", 11): [f"g11_maths_chapter12_{i:03d}" for i in range(19, 26)],
    ("maths", "limits-standard", 11): ["g11_maths_chapter12_026", "g11_maths_chapter12_027",
                                       "12.4 Limits of Trigonometric Functions"],
    ("maths", "consistency-of-system", 12): [
        "4.6 Applications of Determinants and Matrices",
        "4.6.1 Solution of system of linear equations using inverse of a matrix"],
    ("maths", "section-formula", 12): ["10.5.2 Vector joining two points", "10.5.3 Section formula"],
    # science, Grade 9
    ("science", "force-concept", 9): ["8.1 Balanced and Unbalanced Forces"],
    ("science", "pressure-concept", 9): ["9.5 Thrust and Pressure", "9.5.1 PRESSURE IN FLUIDS"],
    ("science", "power-physics", 9): [f"g9_science_chapter10_{i:03d}" for i in (33, 34, 35, 36, 38)],
    ("science", "forms-of-energy", 9): [f"g9_science_chapter10_{i:03d}"
                                        for i in (11, 12, 13, 14, 28, 29)],
    ("science", "particle-nature-of-matter", 9): [f"g9_science_chapter1_{i:03d}" for i in range(1, 11)],
    ("science", "states-of-matter-chemistry", 9): [f"g9_science_chapter1_{i:03d}" for i in range(12, 18)],
    ("science", "wave-motion", 9): ["11.2 Propagation of Sound", "g9_science_chapter11_005",
                                    "g9_science_chapter11_006"],
    # science, Grade 10
    ("science", "resistance-and-resistivity", 10): [f"g10_science_chapter11_{i:03d}"
                                                    for i in range(14, 19)],
    ("science", "magnetic-field", 10): [f"g10_science_chapter12_{i:03d}" for i in range(2, 6)],
    ("science", "salts-and-their-properties", 10): [f"g10_science_chapter2_{i:03d}"
                                                    for i in (23, 24, 25, 30, 31)],
    ("science", "metals-nonmetals-properties", 10): [f"g10_science_chapter3_{i:03d}"
                                                     for i in (*range(1, 11), *range(12, 19))],
    ("science", "hydrocarbons-intro", 10): ["4.2.1 Saturated and Unsaturated Carbon Compounds",
                                            "4.2.2 Chains, Branches and Rings"],
    ("science", "functional-groups", 10): ["4.2.3 Will you be my Friend?", "4.2.4 Homologous Series"],
    ("science", "soaps-and-detergents", 10): [f"g10_science_chapter4_{i:03d}" for i in range(39, 43)],
    ("science", "human-digestive-system", 10): [f"g10_science_chapter5_{i:03d}" for i in range(14, 19)],
    ("science", "cellular-respiration", 10): ["g10_science_chapter5_020", "g10_science_chapter5_021"],
    ("science", "human-respiratory-system", 10): [f"g10_science_chapter5_{i:03d}"
                                                  for i in range(22, 27)],
    ("science", "human-circulatory-system", 10): [f"g10_science_chapter5_{i:03d}"
                                                  for i in range(28, 33)],
    ("science", "plant-hormones", 10): [f"g10_science_chapter6_{i:03d}" for i in range(14, 21)],
    ("science", "endocrine-system", 10): [f"g10_science_chapter6_{i:03d}" for i in range(22, 27)],
    ("science", "environmental-issues", 10): [f"g10_science_chapter13_{i:03d}"
                                              for i in (9, 10, 12, 13, 14, 17, 18)],
    # science, Grade 11
    ("science", "speed-and-velocity", 11): ["g11_physics_part1_chapter2_001",
                                            "2.2 INSTANTANEOUS VELOCITY AND SPEED"],
    ("science", "acceleration", 11): ["2.3 ACCELERATION"],
    ("science", "equations-of-motion", 11): ["2.4 KINEMATIC EQUATIONS FOR UNIFORMLY ACCELERATED MOTION"],
    ("science", "friction", 11): ["4.9 COMMON FORCES IN MECHANICS", "4.9.1 Friction"],
    ("science", "free-body-diagrams", 11): ["4.11 SOLVING PROBLEMS IN MECHANICS"],
    ("science", "atmospheric-pressure", 11): ["9.2.3 Atmospheric Pressure and Gauge Pressure",
                                              "1 torr = 133 Pa."],
    ("science", "heat-and-temperature", 11): ["10.2 TEMPERATURE AND HEAT",
                                              "10.3 MEASUREMENT OF TEMPERATURE",
                                              "11.2 THERMAL EQUILIBRIUM"],
    ("science", "change-of-state", 11): ["10.8 CHANGE OF STATE", "10.8.1 Latent Heat"],
    ("science", "heat-transfer-modes", 11): ["10.9 HEAT TRANSFER"] + [
        f"g11_physics_part2_chapter3_{i:03d}" for i in range(35, 40)] + [
        "10.9.2 Convection", "10.9.3 Radiation"],
    ("science", "wave-properties", 11): ["14.3 DISPLACEMENT RELATION IN A PROGRESSIVE WAVE",
                                         "14.3.1 Amplitude and Phase",
                                         "14.3.2 Wavelength and Angular Wave Number",
                                         "14.3.3 Period, Angular Frequency and Frequency"],
    ("science", "skeletal-and-muscular-system", 11): ["17.2 MUSCLE",
                                                      "17.2.1 Structure of Contractile Proteins",
                                                      "17.3 SKELETAL SYSTEM"],
    ("science", "neural-control-coordination", 11): ["18.4 CENTRAL NEURAL SYSTEM",
                                                     "18.4.1 Forebrain", "18.4.2 Midbrain",
                                                     "18.4.3 Hindbrain"],
    ("science", "breathing-and-gas-exchange", 11): ["14.3 EXCHANGE OF GASES",
                                                    "14.4 TRANSPORT OF GASES",
                                                    "14.4.1 Transport of Oxygen",
                                                    "14.4.2 Transport of Carbon dioxide",
                                                    "14.5 REGULATION OF RESPIRATION"],
    ("science", "plant-respiration", 11): ["12.1 Do PLANTS BREATHE?", "12.3 FERMENTATION"],
    ("science", "respiration-detail", 11): ["12.2 GLYCOLYSIS", "12.4.1 Tricarboxylic Acid Cycle",
                                            "12.4.2 Electron Transport System (ETS) and "
                                            "Oxidative Phosphorylation"],
    ("science", "flower-structure", 11): ["5.5 THE FLOWER", "5.5.1 Parts of a Flower",
                                          "5.5.1.1 Calyx", "5.5.1.2 Corolla",
                                          "5.5.1.3 Androectum", "5.5.1.4 Gynoecium"],
    ("science", "animal-morphology", 11): ["7.2 FROGS", "7.2.1 Morphology", "7.2.2 Anatomy"],
    ("science", "atomic-models-physics", 11): ["2.2 ATOMIC MODELS", "2.2.1 Thomson Model of Atom",
                                               "2.2.2 Rutherford's Nuclear Model of Atom",
                                               "2.2.5 Drawbacks of Rutherford Model"],
    ("science", "isotopes-isobars", 11): ["2.2.3 Atomic Number and Mass Number",
                                          "2.2.4 Isobars and Isotopes"],
    ("science", "electromagnetic-waves", 11): ["2.3.1 Wave Nature of Electromagnetic Radiation"],
    ("science", "photoelectric-effect", 11): [f"g11_chemistry_part1_chapter2_{i:03d}"
                                              for i in range(30, 38)],
    ("science", "dual-nature-of-matter", 11): ["2.5.1 Dual Behaviour of Matter",
                                               "2.5.2 Heisenberg's Uncertainty Principle"],
    ("science", "ph-scale", 11): ["6.11.2 The pH Scale"],
    ("science", "electrode-potential", 11): ["7.4 REDOX REACTIONS AND ELECTRODE PROCESSES"],
    ("science", "separation-techniques", 11): ["8.8 METHODS OF PURIFICATION OF ORGANIC COMPOUNDS",
                                               "8.8.1 Sublimation", "8.8.2 Crystallisation",
                                               "8.8.3 Distillation", "8.8.4 Differential Extraction",
                                               "8.8.5 Chromatography"],
    # science, Grade 12
    ("science", "seed-formation", 12): ["1.4 POST-FERTILISATION : STRUCTURES AND EVENTS",
                                        "1.4.3 Seed"],
    ("science", "human-health-diseases-detail", 12): ["7.3 AIDS", "7.5 DRUGS AND ALCOHOL ABUSE",
                                                      "7.5.3 Effects of Drug/Alcohol Abuse"],
    ("science", "bioprocessing", 12): ["9.3.5 Obtaining the Foreign Gene Product"],
    ("science", "carbohydrates", 12): ["10.1 Carbohydrates"],
    ("science", "nucleic-acids", 12): ["10.5 Nucleic Acids",
                                       "10.5.1 Chemical Composition of Nucleic Acids"],
    ("science", "electric-current", 12): ["3.2 ELECTRIC CURRENT", "3.3 ELECTRIC CURRENTS IN CONDUCTORS"],
    ("science", "magnets-and-magnetism", 12): ["5.2 THE BAR MAGNET",
                                               "5.2.2 Bar magnet as an equivalent solenoid",
                                               "5.2.3 The dipole in a uniform magnetic field",
                                               "5.2.4 The electrostatic analog"],
    ("science", "mirror-formula", 12): ["9.2.1 Sign convention",
                                        "9.2.2 Focal length of spherical mirrors",
                                        "9.2.3 The mirror equation"],
    ("science", "refraction-of-light", 12): ["9.3 REFRACTION"],
    ("science", "lens-formula", 12): ["9.5 REFRACTION AT SPHERICAL SURFACES AND BY LENSES",
                                      "9.5.2 Refraction by a lens"],
    ("science", "power-of-a-lens", 12): [f"g12_physics_part2_chapter1_{i:03d}"
                                         for i in range(29, 34)],              # 9.5.3-9.5.4
    ("science", "isotopes-isobars", 12): ["13.2 ATOMIC MASSES AND COMPOSITION OF NUCLEUS"],
    ("science", "band-theory", 12): ["14.2 CLASSIFICATION OF METALS, CONDUCTORS AND SEMICONDUCTORS"],
}

# Grade 8 science (Curiosity) chapters no page used, added 2026-10-17 on the user's
# request for "a bit more G8 science". The book files nearly all of it as Activity
# blocks, so every one is pinned by passage id.
def _g8(ch: int, nums) -> list[str]:
    return [f"g8_science_chapter{ch}_{i:03d}" for i in nums]


ADD.update({
    ("science", "spherical-mirrors", 8): _g8(10, (3, 4, 6, 7, 8)),          # 10.1-10.2
    ("science", "lenses", 8): _g8(10, range(20, 26)),                       # 10.4
    ("science", "solar-system", 8): _g8(13, (2, 3, 4, 5, 6, 8, 10, 12)),    # 13.1-13.3
    ("science", "organism-interactions", 8): _g8(12, (4, 5, 7, 8, 9, 10, 11, 12)),  # 12.2-12.4
    ("science", "diseases-types", 8): _g8(3, range(9, 18)),                 # 3.4-3.5
    ("science", "magnetic-effect-of-current", 8): _g8(4, (1, 2, 3, 4, 5, 6, 7, 8, 10)),  # 4.1
    ("science", "particle-nature-of-matter", 8): _g8(7, (1, 2, 4, 6, 7, 8, 9, 10,
                                                          13, 14, 15, 16)),  # 7.1-7.3
    ("science", "mixtures-types", 8): _g8(8, (1, 4, 6, 8)),                 # 8.1
    ("science", "pure-substances", 8): _g8(8, (9, 11, 15, 19, 25)),         # 8.2-8.4
    ("science", "solutions-chemistry", 8): _g8(9, (1, 3, 4, 8)),            # 9.1-9.3
})

# Grades 9-12: the user asked for 30-40 pairs per grade and subject (2026-10-17: "140 and
# 98 in grade 11 and 12 science are too much even 62 and 53"). Chosen by hand, chapter by
# chapter: roughly one or two pairs per chapter, the chapter's central topic first, and
# every pair that already has a page kept. Anything not listed here is dropped as
# "scope", which says nothing against its source — it is a size decision.
SCOPE = {
    ("maths", 9): ["algebraic-identities", "arc-chord-properties", "cartesian-coordinate-system",
                   "circle-theorems", "congruence-of-triangles", "cyclic-quadrilaterals",
                   "data-representation-grouped", "decimal-expansions-of-real-numbers",
                   "euclid-definitions-axioms-postulates", "factor-theorem",
                   "factorisation-of-polynomials", "heron-s-formula", "irrational-numbers",
                   "laws-of-exponents-real", "linear-equations-two-variables",
                   "lines-angles-theorems", "mid-point-theorem", "polynomials-in-one-variable",
                   "properties-of-parallelogram", "properties-of-triangles", "real-numbers",
                   "surds-and-rationalisation", "surface-area-cone", "surface-area-sphere",
                   "volume-cone", "volume-sphere", "zeroes-of-a-polynomial"],
    ("maths", 10): ["ap-nth-term", "ap-sum-of-n-terms", "area-of-sector-and-segment",
                    "arithmetic-progressions", "basic-proportionality-theorem", "distance-formula",
                    "elimination-method", "fundamental-theorem-of-arithmetic",
                    "heights-and-distances", "mean-of-grouped-data", "median-of-grouped-data",
                    "mode-of-grouped-data", "nature-of-roots", "pair-of-linear-equations",
                    "proof-irrationality", "quadratic-equations",
                    "representing-linear-equations-graphically", "section-formula",
                    "similar-triangles", "substitution-method",
                    "surface-area-volume-combinations", "tangent-properties",
                    "tangent-to-a-circle", "theoretical-probability", "trigonometric-identities",
                    "trigonometric-ratios", "trigonometric-ratios-specific-angles",
                    "zeroes-coefficients-relationship", "zeroes-of-a-polynomial"],
    ("maths", 11): ["argand-plane", "axiomatic-probability", "binomial-theorem",
                    "cartesian-product-of-sets", "circle-equation", "combinations",
                    "complex-numbers", "conic-sections", "derivatives-first-principles",
                    "derivatives-rules-basic", "distance-point-to-line", "ellipse", "functions",
                    "fundamental-principle-of-counting", "geometric-progressions", "hyperbola",
                    "introduction-3d-geometry", "limits-algebra", "limits-intuitive",
                    "linear-inequalities", "measures-of-dispersion", "modulus-and-argument",
                    "parabola", "permutations", "radian-measure", "relations",
                    "sample-space-events", "sequences-introduction", "series-introduction",
                    "set-operations", "sets", "slope-of-a-line", "special-functions",
                    "straight-lines", "subsets", "trigonometric-addition-formulas",
                    "trigonometric-functions", "variance-and-standard-deviation"],
    ("maths", 12): ["adjoint-and-inverse-matrix", "angle-between-lines-3d", "area-under-curves",
                    "area-using-determinants", "bayes-theorem", "chain-rule",
                    "conditional-probability", "continuity-of-functions", "cross-product",
                    "definite-integrals", "determinants", "differential-equations-intro",
                    "direction-cosines-ratios", "dot-product", "equation-of-line-3d",
                    "exponential-and-log-functions", "fundamental-theorem-of-calculus",
                    "implicit-differentiation", "increasing-decreasing-functions",
                    "independent-events", "integration-by-partial-fractions",
                    "integration-by-parts", "integration-by-substitution", "integration-indefinite",
                    "inverse-trigonometric-functions", "linear-differential-equations",
                    "linear-programming", "matrices", "matrix-operations", "maxima-and-minima",
                    "second-order-derivative", "shortest-distance-two-lines",
                    "total-probability-theorem", "types-of-functions", "types-of-matrices",
                    "types-of-relations", "types-of-vectors", "variable-separable",
                    "vector-addition", "vectors"],
    ("science", 9): [
        "states-of-matter-chemistry", "particle-nature-of-matter", "change-of-state",   # ch1
        "pure-substances", "solutions-chemistry",                                       # ch2
        "atoms-and-molecules", "chemical-formula-writing", "law-of-conservation-of-mass",  # ch3
        # electron-configuration left out: in this book 4.3 is 193 words and it and
        # valency would be handed the same two sections
        "atomic-models-physics", "atomic-number-mass-number",
        "valency-chemistry", "isotopes-isobars",                                        # ch4
        "cell-basic-unit", "cell-organelles", "tissue-types",                           # ch5-6
        "distance-and-displacement", "speed-and-velocity", "acceleration",
        "equations-of-motion",                                                          # ch7
        "force-concept", "newtons-first-law", "newtons-second-law", "newtons-third-law",  # ch8
        "gravitation-intro", "acceleration-due-to-gravity", "buoyancy-and-archimedes",
        "pressure-concept",                                                             # ch9
        "work-physics", "kinetic-energy", "potential-energy", "conservation-of-energy",
        "power-physics",                                                                # ch10
        "sound-production", "characteristics-of-sound", "echo-and-reverberation",
        "ultrasound-applications",                                                      # ch11
        "crop-improvement", "animal-husbandry"],                                        # ch12
    ("science", 10): [
        "chemical-equations", "types-of-chemical-reactions",                            # ch1
        "acids-bases-indicators", "properties-of-acids-bases", "ph-scale",              # ch2
        "metals-nonmetals-properties", "reactivity-series",                             # ch3
        "covalent-bonding", "carbon-and-its-compounds", "functional-groups",
        "reactions-of-hydrocarbons",                                                    # ch4
        "modes-of-nutrition", "photosynthesis", "human-digestive-system",
        "cellular-respiration", "human-circulatory-system", "excretory-system",          # ch5
        "nervous-system", "plant-hormones", "endocrine-system",                         # ch6
        "asexual-reproduction", "sexual-reproduction-overview",
        "human-reproductive-system",                                                    # ch7
        "heredity-and-variation", "mendels-laws",                                       # ch8
        # reflection-of-light left out: 9.1 is 296 words, under the floor (Grade 8 has it)
        "spherical-mirrors", "mirror-formula", "snells-law",
        "lenses", "lens-formula",                                                       # ch9
        "human-eye-defects", "dispersion-of-light",                                     # ch10
        "electric-current", "electric-potential", "ohms-law",
        "resistance-and-resistivity",                                                   # ch11
        "magnetic-field", "magnetic-effect-of-current",                                 # ch12
        "ecosystem-concept", "food-chains-and-webs"],                                   # ch13
    ("science", 11): [
        # biology
        "five-kingdom-classification", "plant-kingdom", "animal-kingdom", "cell-organelles",
        "biomolecules-intro", "cell-cycle", "photosynthesis", "cellular-respiration",
        "human-respiratory-system", "human-circulatory-system", "excretory-system",
        "nervous-system", "endocrine-system",
        # chemistry
        "mole-concept", "bohrs-model-chemistry", "quantum-mechanical-model",
        "periodic-properties", "chemical-bonding-intro", "vsepr-theory", "enthalpy-changes",
        "chemical-equilibrium", "ionic-equilibrium", "oxidation-reduction",
        "nomenclature-iupac", "hydrocarbons-intro",
        # physics
        "dimensional-analysis", "equations-of-motion", "projectile-motion",
        "newtons-second-law", "work-energy-theorem", "centre-of-mass", "torque",
        "gravitation-intro", "elasticity-physics", "bernoullis-principle", "thermal-expansion",
        "first-law-of-thermodynamics", "kinetic-theory-of-gases", "simple-harmonic-motion",
        "wave-motion"],
    ("science", 12): [
        # biology
        "pollination-and-fertilisation-plants", "human-reproductive-system", "reproductive-health",
        "mendels-laws", "dna-structure-replication", "darwins-theory", "infectious-diseases",
        "human-health-diseases-detail", "microbes-in-human-welfare",
        "recombinant-dna-technology", "applications-of-biotechnology",
        "population-interactions", "biodiversity",
        # chemistry
        "colligative-properties", "electrode-potential", "batteries-and-fuel-cells",
        "collision-theory", "d-and-f-block-elements", "coordination-compounds",
        "haloalkanes-haloarenes", "alcohols-phenols-ethers",
        "aldehydes-ketones-carboxylic-acids", "amines", "carbohydrates",
        # physics
        "coulombs-law", "electric-potential", "capacitance", "kirchhoffs-laws",
        "biot-savart-law", "electromagnetic-induction", "alternating-current",
        "ac-circuits-lcr", "snells-law", "lens-formula", "wave-optics-interference",
        "diffraction", "photoelectric-effect", "atomic-models-physics", "nuclear-structure",
        "band-theory"],
}


# Rewired edges that only survive as the residue of a chain through removed concepts and
# state no real dependency (decimals -> radian measure came via circumference of a circle;
# circulatory system -> endocrine system via blood composition).
BLOCK_EDGES = {
    "maths": {("decimals", "radian-measure"), ("decimals", "surface-area-cone"),
              ("decimals", "surface-area-sphere"), ("decimals", "area-of-sector-and-segment")},
    "science": {("water-and-its-properties", "biodiversity-conservation"),
                ("what-is-matter", "biodiversity-conservation"),
                ("human-circulatory-system", "endocrine-system"),
                ("electric-charge", "nuclear-fission-fusion"),
                ("living-vs-nonliving", "adolescence-and-puberty")},
}
# Edges added by hand for concepts the pruning left with no link at all. Each prerequisite
# is taught at the same grade or earlier.
ADD_EDGES = {
    # The last three: GENERATED pages re-added 2026-10-17 whose old links all ran to
    # concepts the pruning removed.
    "maths": {("ratios-and-proportions", "simple-interest")},
    "science": {("microorganisms", "antibiotics-and-vaccines"),
                # isolated once SCOPE cut their neighbours: neutralisation (G7) had only
                # led to salts G10; crop variety improvement (G9) breeds by cross-pollination
                ("neutralisation", "properties-of-acids-bases"),
                ("seed-formation", "crop-improvement"),
                ("plant-reproduction-asexual", "asexual-reproduction"),
                ("components-of-food", "animal-nutrition"),
                ("plant-respiration", "cellular-respiration"),
                ("pressure-concept", "atmospheric-pressure"),
                ("solutions-chemistry", "colloids"),
                ("what-is-matter", "separation-techniques"),
                ("tissue-types", "locomotion-and-movement-detail"),
                ("nuclear-structure", "nuclear-fission-fusion"),
                ("what-is-matter", "water-and-its-properties"),
                ("water-and-its-properties", "change-of-state")},
}


def ruling(subject: str, grade: int, slug: str) -> tuple[str, str] | None:
    if slug in NOT_IN_BOOK[subject].get(grade, []):
        return "not_in_book", "the grade's book does not teach it"
    if slug in PART_OF[subject].get(grade, []):
        return "part_of", "taught only inside a broader section"
    dup = DUPLICATE[subject].get(grade, {}).get(slug)
    if dup:
        return "duplicate", f"same section as {dup}"
    return None


def words(anchors: list[dict]) -> int:
    return sum(len(a["text"].split()) for a in anchors)


# The page needs at least enough source for its shortest allowed length at the
# pipeline's own expansion cap (build_context.MAX_EXPANSION): asking 2.5x more words
# than the extracts hold is what produced the invented "Types of Soil" section.
FLOOR = {g: math.ceil(lo / bc.MAX_EXPANSION) for g, (lo, _) in bc.GRADE_WORDS.items()}


def make_graphs(graphs: dict, keep: dict) -> tuple[dict, dict]:
    new_graphs = {}
    edge_log = {s: {"rewired": [], "dropped_late": []} for s in graphs}
    for s, old in graphs.items():
        oldc = old["concepts"]
        kept = {x: sorted(gs) for x, gs in keep[s].items() if gs}
        concepts = {}
        for x, gs in kept.items():
            c = copy.deepcopy(oldc[x])
            c["grades"] = gs
            pins = {k: v for k, v in (c.get("source_sections") or {}).items() if int(k) in gs}
            for (s2, x2, g2), entries in (list(PIN.items()) + list(RESCUE.items())
                                          + list(ADD.items())):
                if s2 == s and x2 == x and g2 in gs:
                    pins[str(g2)] = entries
            if pins:
                c["source_sections"] = dict(sorted(pins.items(), key=lambda kv: int(kv[0])))
            else:
                c.pop("source_sections", None)
            concepts[x] = c

        # A concept removed as a duplicate is replaced by the one that carries its section,
        # so whatever needed it now needs that one.
        stand_in = {dup: keeper for by_grade in DUPLICATE[s].values()
                    for dup, keeper in by_grade.items() if dup not in concepts}

        # Prerequisites, looking through removed concepts to the kept ones behind them.
        def kept_prereqs(x: str, seen: set[str]) -> set[str]:
            out = set()
            for p in oldc[x].get("prerequisites", []):
                if p in seen or p not in oldc:
                    continue
                seen.add(p)
                if p in concepts:
                    out.add(p)
                elif stand_in.get(p) in concepts and stand_in[p] != x:
                    out.add(stand_in[p])
                else:
                    out |= kept_prereqs(p, seen)
            return out

        direct = {x: {p for p in oldc[x].get("prerequisites", []) if p in concepts}
                  for x in concepts}
        first = {x: min(concepts[x]["grades"]) for x in concepts}
        prereqs = {}
        for x in concepts:
            ps = set()
            for p in kept_prereqs(x, {x}):
                if first[p] > first[x]:
                    edge_log[s]["dropped_late"].append(f"{p} (gr {concepts[p]['grades']}) -> "
                                                       f"{x} (gr {concepts[x]['grades']})")
                    continue
                ps.add(p)
            prereqs[x] = ps

        # Drop a rewired edge already implied by another path (keeps the graph sparse).
        def reaches(a: str, b: str, skip: tuple[str, str]) -> bool:
            stack, seen = [b], set()
            while stack:
                n = stack.pop()
                for p in prereqs[n]:
                    if (p, n) == skip or p in seen:
                        continue
                    if p == a:
                        return True
                    seen.add(p)
                    stack.append(p)
            return False

        for x in sorted(concepts):
            for p in sorted(prereqs[x] - direct[x]):
                if reaches(p, x, (p, x)):
                    prereqs[x].discard(p)
                elif (p, x) in BLOCK_EDGES[s]:
                    prereqs[x].discard(p)
                    edge_log[s].setdefault("blocked", []).append(f"{p} -> {x}")
                else:
                    edge_log[s]["rewired"].append(f"{p} -> {x}")

        for p, x in sorted(ADD_EDGES[s]):
            if p not in concepts or x not in concepts:
                # an end was cut for size (SCOPE); the link has nothing left to join
                edge_log[s].setdefault("added_skipped", []).append(f"{p} -> {x}")
                continue
            assert first[p] <= first[x], (s, p, x, "prerequisite taught later")
            prereqs[x].add(p)
            edge_log[s].setdefault("added", []).append(f"{p} -> {x}")

        leads = defaultdict(set)
        for x, ps in prereqs.items():
            for p in ps:
                leads[p].add(x)
        for x, c in concepts.items():
            c["prerequisites"] = sorted(prereqs[x])
            c["leads_to"] = sorted(leads[x])
        edges = [{"from": p, "to": x, "type": "prerequisite"}
                 for x in sorted(concepts) for p in concepts[x]["prerequisites"]]

        g_new = {k: v for k, v in old.items() if k not in ("concepts", "edges")}
        g_new["version"] = f"{old.get('version', '')}-v2-own-grade".lstrip("-")
        g_new["description"] = (old.get("description", "") + " — v2: only concept-grade pairs "
                                "whose own grade's book teaches them (see graph_v2_report.json)")
        g_new["total_concepts"] = len(concepts)
        g_new["total_edges"] = len(edges)
        g_new["concepts"] = dict(sorted(concepts.items()))
        g_new["edges"] = edges
        new_graphs[s] = g_new
    return new_graphs, edge_log


def main() -> dict | None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true", help="build and verify, write nothing")
    args = ap.parse_args()

    graphs, passages, evidence = bc.load()
    levels = bc.level_profile(passages)

    # build() and generate_pages.py --all both need an evidence row for every pair, and
    # match_concepts.py only writes rows for grades graph.json lists. An ADD grade the old
    # graph never had gets a row saying exactly what it is: hand-pinned, not retrieved.
    new_evidence = {s: [] for s in graphs}
    index = bc.section_index(passages)
    for (s, x, g), pins in ADD.items():
        if (s, x, g) in evidence:
            continue
        ids = []
        for entry in pins:
            if entry in passages:
                ids.append(entry)
            else:
                found = [k for k in index if k[0] == g and k[3] == entry
                         and (k[1] == "maths") == (s == "maths")]
                assert len(found) == 1, f"{x} grade {g}: pin {entry!r} matches {len(found)}"
                ids += [p["id"] for p in index[found[0]]]
        c = graphs[s]["concepts"][x]
        row = {"slug": x, "canonical_name": c["canonical_name"], "grade": g,
               "area": c.get("area", ""), "n_hits": 0, "best_cosine": 1.0,
               "evidence": "pinned", "hits": [], "covers": ids,
               "source_grade": g, "grade_delta": 0, "context_evidence": "pinned",
               "note": "written by build_graph_v2.py for an ADD pair: source is the "
                       "hand-pinned section, not a retrieval result"}
        evidence[(s, x, g)] = row
        new_evidence[s].append(row)

    # Sanity: every hand ruling must name a real (concept, grade) pair.
    for table in (NOT_IN_BOOK, PART_OF):
        for s, by_grade in table.items():
            for g, slugs in by_grade.items():
                for x in slugs:
                    c = graphs[s]["concepts"].get(x)
                    assert c and g in c["grades"], f"ruling names {s} {x} grade {g}, not in graph"
    for s, by_grade in DUPLICATE.items():
        for g, d in by_grade.items():
            for x, keeper in d.items():
                assert g in graphs[s]["concepts"][x]["grades"], (s, x, g)
                assert g in graphs[s]["concepts"][keeper]["grades"], (s, keeper, g)
    for (s, x, g) in list(PIN) + list(RESCUE):
        assert g in graphs[s]["concepts"][x]["grades"], (s, x, g)
    for (s, x, g) in GENERATED_PAIRS:
        assert g in graphs[s]["concepts"][x]["grades"], (s, x, g)
        stream = "maths" if s == "maths" else graphs[s]["concepts"][x]["subject"]
        assert (PAGES / stream / f"grade{g}" / f"{x}.md").exists(), f"no published page {x} {g}"
    for (s, x, g) in ADD:
        assert x in graphs[s]["concepts"] and (s, x, g) not in GENERATED_PAIRS, (s, x, g)
        assert 8 <= g <= 12, (s, x, g)
    for (s, g), xs in SCOPE.items():
        assert len(xs) == len(set(xs)), (s, g)

    # 1. Decide every pair against the ORIGINAL graph's retrieval.
    decisions = {}          # (subject, slug, grade) -> row
    keep: dict[str, dict[str, list[int]]] = {s: defaultdict(list) for s in graphs}
    for s, g_ in graphs.items():
        for slug, c in g_["concepts"].items():
            for grade in c["grades"]:
                ctx = bc.build(s, slug, grade, graphs, passages, evidence, levels)
                own = [a for a in ctx["anchors"] if a["grade"] == grade]
                same_grade = (ctx["same_source_as"] is None and ctx["grade_delta"] == 0
                              and len(own) == len(ctx["anchors"])
                              and words(own) >= bc.MIN_SOURCE_WORDS)
                row = {"subject": s, "slug": slug, "grade": grade, "name": c["canonical_name"]}
                r = ruling(s, grade, slug)
                if (s, slug, grade) in GENERATED_PAIRS:
                    row.update(decision="keep", category="generated",
                               why="already generated and hand-audited; kept as published"
                                   + (f" (ruling: {r[0]})" if r else ""))
                elif (s, slug, grade) in ADD:
                    row.update(decision="keep", category="added",
                               why="own-grade section found 2026-10-17; pinned")
                elif (s, slug, grade) in RESCUE:
                    row.update(decision="keep", why="own chapter, missed by retrieval; pinned")
                elif r:
                    row.update(decision="drop", category=r[0], why=r[1])
                elif (s, slug, grade) in PIN:
                    row.update(decision="keep", why="own-grade section; pinned")
                elif not same_grade:
                    why = (f"text borrowed from grade {ctx['source_grade']}" if ctx["grade_delta"]
                           else f"same extracts as its grade {ctx['same_source_as']} page"
                           if ctx["same_source_as"] else
                           f"only {words(own)} words of own-grade text")
                    row.update(decision="drop", category="no_own_grade_text", why=why)
                else:
                    row.update(decision="keep", why="own-grade section")
                if row["decision"] == "keep":
                    keep[s][slug].append(grade)
                decisions[(s, slug, grade)] = row
    # Added grades the old graph never listed for the concept.
    new_pairs = set()
    for (s, x, g) in ADD:
        if (s, x, g) not in decisions:
            new_pairs.add((s, x, g))
            keep[s][x].append(g)
            decisions[(s, x, g)] = {"subject": s, "slug": x, "grade": g,
                                    "name": graphs[s]["concepts"][x]["canonical_name"],
                                    "decision": "keep", "category": "added",
                                    "why": "own-grade section found 2026-10-17 (grade new to "
                                           "this concept); pinned"}
    # Size: Grades 9-12 keep only the hand-chosen SCOPE list. Every listed pair must be one
    # the rules above kept, so the list cannot smuggle a dropped pair back in.
    for s, by_slug in keep.items():
        for x, gs in by_slug.items():
            for g in list(gs):
                if g >= 9 and x not in SCOPE[(s, g)]:
                    gs.remove(g)
                    decisions[(s, x, g)].update(
                        decision="drop", category="scope",
                        why="not among the 30-40 pairs chosen for this grade and subject "
                            "(2026-10-17); a size decision, not a source problem")
    for (s, g), xs in SCOPE.items():
        for x in xs:
            assert g in keep[s].get(x, []), f"SCOPE names {s} {x} grade {g}, which is not kept"

    # 2. Build, then re-check every kept pair UNDER THE NEW GRAPH (removing rival concepts
    #    and adding pins changes which sections build() picks). A pair below its grade's
    #    floor is dropped and the graph rebuilt, until nothing changes.
    for _round in range(5):
        v2, edge_log = make_graphs(graphs, keep)
        pair_rows, thin, sources = [], [], {}
        for s, g_new in v2.items():
            for x, c in g_new["concepts"].items():
                for grade in c["grades"]:
                    ctx = bc.build(s, x, grade, v2, passages, evidence, levels)
                    own = [a for a in ctx["anchors"] if a["grade"] == grade]
                    ok = (ctx["generate"] and ctx["grade_delta"] == 0
                          and ctx["same_source_as"] is None and len(own) == len(ctx["anchors"]))
                    row = {"subject": s, "slug": x, "grade": grade, "source_words": words(own),
                           "floor": FLOOR[grade],
                           "pinned": bool((c.get("source_sections") or {}).get(str(grade))),
                           "sections": [a["section"] for a in ctx["anchors"]], "ok": ok}
                    if (s, x, grade) in GENERATED_PAIRS:
                        row["generated"] = True
                    pair_rows.append(row)
                    sources[(s, x, grade)] = frozenset(p for a in ctx["anchors"]
                                                       for p in a["passage_ids"])
                    # An ADD pair under its floor is a mistake in the table, not something
                    # to drop quietly: it stays, and step 3 reports it.
                    if (ok and words(own) < FLOOR[grade]
                            and (s, x, grade) not in GENERATED_PAIRS and (s, x, grade) not in ADD):
                        thin.append((s, x, grade, words(own)))
        if not thin:
            break
        for s, x, grade, w in thin:
            keep[s][x].remove(grade)
            decisions[(s, x, grade)].update(
                decision="drop", category="thin",
                why=f"{w} words of own-grade text, under the grade {grade} floor of {FLOOR[grade]}")

    # 3. Verify structure and grade order.
    problems = []
    for s, g_new in v2.items():
        problems += [f"{s}: {e}" for e in validate(g_new)]
        problems += [f"{s}: late prerequisite {e}" for e in late_prerequisites(g_new)]
    def written(s: str, x: str, g: int) -> bool:
        """A Grade 6-8 page that is already published (every Grade 6-8 pair is)."""
        stream = "maths" if s == "maths" else v2[s]["concepts"][x]["subject"]
        return g <= 8 and (PAGES / stream / f"grade{g}" / f"{x}.md").exists()

    # A GENERATED page is already written, so it is not held to the build checks; what
    # build() would hand it today is recorded, not enforced.
    generated_notes = []
    for r in pair_rows:
        if r.get("generated"):
            if not r["ok"] or r["source_words"] < r["floor"]:
                generated_notes.append(f"{r['subject']}: {r['slug']} grade {r['grade']} "
                                       f"(own-grade words now {r['source_words']})")
        elif not r["ok"]:
            problems.append(f"{r['subject']}: {r['slug']} grade {r['grade']} does not build from "
                            f"own-grade text ({r['source_words']} words)")
        elif r["source_words"] < r["floor"]:
            problems.append(f"{r['subject']}: {r['slug']} grade {r['grade']} under floor")
    # Two grades of one concept must not share a passage (that is the copy problem), and two
    # concepts in one grade must not be handed exactly the same sections. Between two
    # already-generated pages nothing can be done any more; a page still to be written
    # must not share with anything.
    for (s, x, a), ids in sources.items():
        for (s2, x2, b), ids2 in sources.items():
            both_done = written(s, x, a) and written(s2, x2, b)
            if s == s2 and x == x2 and a < b and ids & ids2 and not both_done:
                problems.append(f"{s}: {x} grades {a} and {b} share source passages")
            if s == s2 and a == b and x < x2 and ids == ids2 and not both_done:
                problems.append(f"{s}: {x} and {x2} (grade {a}) have identical sources")
    old_pairs = {(s, x, g) for s in graphs for x, c in graphs[s]["concepts"].items()
                 for g in c["grades"]}
    assert set(decisions) == old_pairs | new_pairs
    assert {(r["subject"], r["slug"], r["grade"]) for r in pair_rows} == \
        {k for k, d in decisions.items() if d["decision"] == "keep"}

    isolated = {s: sorted(x for x, c in v2[s]["concepts"].items()
                          if not c["prerequisites"] and not c["leads_to"]) for s in v2}
    print(f"floors by grade: {FLOOR}")
    print(f"kept pairs: {len(pair_rows)}  " + "  ".join(
        f"{s}: {v2[s]['total_concepts']} concepts / "
        f"{sum(len(c['grades']) for c in v2[s]['concepts'].values())} pairs / "
        f"{v2[s]['total_edges']} edges" for s in v2))
    for s in v2:
        print(f"{s}: rewired {len(edge_log[s]['rewired'])} edges, dropped "
              f"{len(edge_log[s]['dropped_late'])} late-prerequisite edges, "
              f"{len(isolated[s])} isolated concepts")
    cats: dict[str, int] = defaultdict(int)
    for d in decisions.values():
        cats[d.get("category", "keep") if d["decision"] == "keep" else d["category"]] += 1
    print("decisions:", dict(cats))
    print(f"generated pages kept outside the rule: {len(GENERATED_PAIRS)} "
          f"({len(generated_notes)} would not pass the build checks today)")
    print("problems:", len(problems))
    for p in problems[:40]:
        print("  ", p)

    report = {
        "rule": ("A concept-grade pair is kept only if its page can be written from that grade's "
                 "own book: own-grade extracts only, at least floor_words_by_grade words, and a "
                 "section that is about the concept (hand-checked). Exceptions: GENERATED "
                 "Grade 6-8 pages already written and audited are kept as published. "
                 "See scripts/build_graph_v2.py."),
        "floor_words_by_grade": FLOOR,
        "summary": {s: {"concepts": v2[s]["total_concepts"], "edges": v2[s]["total_edges"],
                        "pairs": sum(len(c["grades"]) for c in v2[s]["concepts"].values())}
                    for s in v2},
        "decision_counts": dict(cats),
        "pairs_kept": pair_rows,
        "pairs_dropped": [d for d in decisions.values() if d["decision"] == "drop"],
        "edges": edge_log,
        "isolated_concepts": isolated,
        "generated_outside_rule": sorted(f"{s}: {x} grade {g}" for s, x, g in GENERATED_PAIRS),
        "generated_failing_build_today": generated_notes,
        "problems": problems,
    }
    if args.check:
        return report
    if problems:
        raise SystemExit("not written: fix the problems above first")
    for s, g_new in v2.items():
        OUT[s].write_text(json.dumps(g_new, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("wrote", OUT[s].relative_to(BASE))
    REPORT.write_text(json.dumps(report, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print("wrote", REPORT.relative_to(BASE))
    # Append only: existing rows are match_concepts.py's and stay as they are.
    for s, rows in new_evidence.items():
        if rows:
            with (bc.EV_DIR / f"{s}.jsonl").open("a", encoding="utf-8") as f:
                for row in rows:
                    f.write(json.dumps(row, ensure_ascii=False) + "\n")
            print(f"appended {len(rows)} pinned evidence rows to "
                  f"{(bc.EV_DIR / f'{s}.jsonl').relative_to(BASE)}")


if __name__ == "__main__":
    main()
