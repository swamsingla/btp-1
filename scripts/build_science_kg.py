#!/usr/bin/env python3
"""
Build grade-wise science knowledge graphs (grades 6-10)
matching the exact format of the existing maths KGs.

Uses curated NCERT science curriculum data — no LLM needed.
Output: data/knowledge_graph/graph_by_grade/grade{N}_science.json
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
KG_DIR = BASE_DIR / "data" / "knowledge_graph"
GRADE_DIR = KG_DIR / "graph_by_grade"
SUBJECT_DIR = KG_DIR / "graph_by_subject"

def slugify(name: str) -> str:
    s = name.lower().strip()
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s.strip("-")

# ── NCERT Science curriculum: grades 6-10 ─────────────────────────────────────
# Each entry: (concept_name, domain, area, importance, prerequisites[], related[])

SCIENCE_CURRICULUM = {
    6: [
        # Food
        ("Sources of Food", "Biology", "Food", 5, [], ["components-of-food"]),
        ("Components of Food", "Biology", "Food", 5, ["sources-of-food"], ["balanced-diet"]),
        ("Balanced Diet", "Biology", "Food", 4, ["components-of-food"], []),
        # Materials
        ("Sorting Materials into Groups", "Chemistry", "Materials", 4, [], ["separation-of-substances"]),
        ("Separation of Substances", "Chemistry", "Materials", 5, ["sorting-materials-into-groups"], ["methods-of-separation"]),
        ("Methods of Separation", "Chemistry", "Materials", 5, ["separation-of-substances"], []),
        # Living World
        ("The Living and Non-Living", "Biology", "Living World", 5, [], ["parts-of-a-plant"]),
        ("Parts of a Plant", "Biology", "Living World", 5, ["the-living-and-non-living"], ["body-movements"]),
        ("Body Movements", "Biology", "Living World", 4, ["the-living-and-non-living"], ["habitat-and-adaptation"]),
        ("Habitat and Adaptation", "Biology", "Living World", 5, ["the-living-and-non-living"], []),
        # Motion and Measurement
        ("Motion and Measurement of Distances", "Physics", "Motion", 5, [], ["types-of-motion"]),
        ("Types of Motion", "Physics", "Motion", 4, ["motion-and-measurement-of-distances"], []),
        ("Standard Units of Measurement", "Physics", "Motion", 4, ["motion-and-measurement-of-distances"], []),
        # Light and Shadows
        ("Light Shadows and Reflections", "Physics", "Light", 5, [], ["transparent-translucent-and-opaque-objects"]),
        ("Transparent Translucent and Opaque Objects", "Physics", "Light", 4, ["light-shadows-and-reflections"], []),
        # Electricity
        ("Electricity and Circuits", "Physics", "Electricity", 5, [], ["electric-cell-and-bulb"]),
        ("Electric Cell and Bulb", "Physics", "Electricity", 4, ["electricity-and-circuits"], []),
        ("Conductors and Insulators", "Physics", "Electricity", 4, ["electricity-and-circuits"], []),
        # Magnets
        ("Fun with Magnets", "Physics", "Magnetism", 5, [], ["properties-of-magnets"]),
        ("Properties of Magnets", "Physics", "Magnetism", 4, ["fun-with-magnets"], []),
        # Water and Air
        ("Water", "Chemistry", "Water", 5, [], ["water-cycle"]),
        ("Water Cycle", "Chemistry", "Water", 5, ["water"], []),
        ("Air Around Us", "Chemistry", "Air", 4, [], ["composition-of-air"]),
        ("Composition of Air", "Chemistry", "Air", 4, ["air-around-us"], []),
        # Waste
        ("Garbage In Garbage Out", "Biology", "Environment", 4, [], []),
        # Changes
        ("Changes Around Us", "Chemistry", "Changes", 4, [], ["reversible-and-irreversible-changes"]),
        ("Reversible and Irreversible Changes", "Chemistry", "Changes", 5, ["changes-around-us"], []),
    ],
    7: [
        # Nutrition
        ("Nutrition in Plants", "Biology", "Nutrition", 5, ["components-of-food", "parts-of-a-plant"], ["nutrition-in-animals"]),
        ("Photosynthesis", "Biology", "Nutrition", 5, ["nutrition-in-plants"], []),
        ("Nutrition in Animals", "Biology", "Nutrition", 5, ["nutrition-in-plants"], ["digestive-system"]),
        ("Digestive System", "Biology", "Nutrition", 4, ["nutrition-in-animals"], []),
        # Fibre to Fabric
        ("Fibre to Fabric", "Chemistry", "Materials", 4, ["sorting-materials-into-groups"], ["animal-fibres"]),
        ("Animal Fibres", "Chemistry", "Materials", 4, ["fibre-to-fabric"], []),
        # Heat
        ("Heat and Temperature", "Physics", "Heat", 5, [], ["conduction-convection-and-radiation"]),
        ("Conduction Convection and Radiation", "Physics", "Heat", 5, ["heat-and-temperature"], []),
        # Acids Bases
        ("Acids Bases and Salts", "Chemistry", "Acids and Bases", 5, ["separation-of-substances"], ["indicators"]),
        ("Indicators", "Chemistry", "Acids and Bases", 4, ["acids-bases-and-salts"], []),
        # Physical and Chemical Changes
        ("Physical and Chemical Changes", "Chemistry", "Changes", 5, ["changes-around-us", "reversible-and-irreversible-changes"], ["rusting-and-crystallisation"]),
        ("Rusting and Crystallisation", "Chemistry", "Changes", 4, ["physical-and-chemical-changes"], []),
        # Weather and Climate
        ("Weather Climate and Adaptations", "Biology", "Environment", 5, ["habitat-and-adaptation"], []),
        # Wind Storms Cyclones
        ("Wind Storms and Cyclones", "Physics", "Weather", 4, ["air-around-us", "heat-and-temperature"], []),
        # Soil
        ("Soil", "Chemistry", "Earth", 4, [], ["soil-profile-and-types"]),
        ("Soil Profile and Types", "Chemistry", "Earth", 4, ["soil"], []),
        # Respiration and Transport
        ("Respiration in Organisms", "Biology", "Life Processes", 5, ["nutrition-in-animals"], ["breathing-and-cellular-respiration"]),
        ("Breathing and Cellular Respiration", "Biology", "Life Processes", 4, ["respiration-in-organisms"], []),
        ("Transportation in Animals and Plants", "Biology", "Life Processes", 5, ["respiration-in-organisms", "nutrition-in-plants"], ["circulatory-system"]),
        ("Circulatory System", "Biology", "Life Processes", 4, ["transportation-in-animals-and-plants"], []),
        # Reproduction
        ("Reproduction in Plants", "Biology", "Reproduction", 5, ["parts-of-a-plant"], []),
        # Motion and Time
        ("Motion and Time", "Physics", "Motion", 5, ["motion-and-measurement-of-distances", "types-of-motion"], ["speed-and-velocity"]),
        ("Speed and Velocity", "Physics", "Motion", 5, ["motion-and-time"], []),
        # Electric Current
        ("Electric Current and Its Effects", "Physics", "Electricity", 5, ["electricity-and-circuits"], ["heating-effect-of-current"]),
        ("Heating Effect of Current", "Physics", "Electricity", 4, ["electric-current-and-its-effects"], []),
        # Light
        ("Light", "Physics", "Light", 5, ["light-shadows-and-reflections"], ["reflection-of-light"]),
        ("Reflection of Light", "Physics", "Light", 4, ["light"], []),
        # Water
        ("Water A Precious Resource", "Chemistry", "Water", 4, ["water", "water-cycle"], []),
        # Forests
        ("Forests Our Lifeline", "Biology", "Environment", 4, ["habitat-and-adaptation"], []),
        # Waste Water
        ("Wastewater Story", "Biology", "Environment", 3, ["water-a-precious-resource"], []),
    ],
    8: [
        # Crop Production
        ("Crop Production and Management", "Biology", "Agriculture", 4, ["nutrition-in-plants"], ["irrigation-and-harvesting"]),
        ("Irrigation and Harvesting", "Biology", "Agriculture", 3, ["crop-production-and-management"], []),
        # Microorganisms
        ("Microorganisms Friend and Foe", "Biology", "Microorganisms", 5, ["the-living-and-non-living"], ["bacteria-viruses-and-fungi"]),
        ("Bacteria Viruses and Fungi", "Biology", "Microorganisms", 5, ["microorganisms-friend-and-foe"], []),
        # Synthetic Fibres and Plastics
        ("Synthetic Fibres and Plastics", "Chemistry", "Materials", 5, ["fibre-to-fabric"], ["types-of-synthetic-fibres"]),
        ("Types of Synthetic Fibres", "Chemistry", "Materials", 4, ["synthetic-fibres-and-plastics"], []),
        # Metals and Non-Metals
        ("Metals and Non-Metals", "Chemistry", "Materials", 5, ["sorting-materials-into-groups"], ["physical-properties-of-metals"]),
        ("Physical Properties of Metals", "Chemistry", "Materials", 4, ["metals-and-non-metals"], []),
        # Coal and Petroleum
        ("Coal and Petroleum", "Chemistry", "Natural Resources", 5, [], ["fossil-fuels"]),
        ("Fossil Fuels", "Chemistry", "Natural Resources", 4, ["coal-and-petroleum"], []),
        # Combustion and Flame
        ("Combustion and Flame", "Chemistry", "Chemical Reactions", 5, ["physical-and-chemical-changes"], ["types-of-combustion"]),
        ("Types of Combustion", "Chemistry", "Chemical Reactions", 4, ["combustion-and-flame"], []),
        # Cell Structure
        ("Cell Structure and Functions", "Biology", "Cell Biology", 5, ["the-living-and-non-living"], ["cell-organelles"]),
        ("Cell Organelles", "Biology", "Cell Biology", 5, ["cell-structure-and-functions"], []),
        ("Plant and Animal Cells", "Biology", "Cell Biology", 4, ["cell-structure-and-functions"], []),
        # Reproduction
        ("Reproduction in Animals", "Biology", "Reproduction", 5, ["reproduction-in-plants"], ["sexual-and-asexual-reproduction"]),
        ("Sexual and Asexual Reproduction", "Biology", "Reproduction", 5, ["reproduction-in-animals"], []),
        ("Reaching the Age of Adolescence", "Biology", "Human Biology", 4, ["reproduction-in-animals"], []),
        # Force and Pressure
        ("Force and Pressure", "Physics", "Force", 5, ["motion-and-time"], ["types-of-forces"]),
        ("Types of Forces", "Physics", "Force", 5, ["force-and-pressure"], ["friction"]),
        ("Friction", "Physics", "Force", 5, ["types-of-forces"], []),
        ("Pressure in Fluids", "Physics", "Force", 4, ["force-and-pressure"], []),
        # Sound
        ("Sound", "Physics", "Sound", 5, [], ["vibration-and-sound-production"]),
        ("Vibration and Sound Production", "Physics", "Sound", 4, ["sound"], ["characteristics-of-sound"]),
        ("Characteristics of Sound", "Physics", "Sound", 4, ["vibration-and-sound-production"], []),
        # Chemical Effects of Current
        ("Chemical Effects of Electric Current", "Physics", "Electricity", 5, ["electric-current-and-its-effects"], ["electroplating"]),
        ("Electroplating", "Physics", "Electricity", 4, ["chemical-effects-of-electric-current"], []),
        # Light (advanced)
        ("Reflection and Refraction", "Physics", "Light", 5, ["reflection-of-light"], ["laws-of-reflection"]),
        ("Laws of Reflection", "Physics", "Light", 5, ["reflection-and-refraction"], []),
        ("Dispersion of Light", "Physics", "Light", 4, ["reflection-and-refraction"], []),
        # Stars and Solar System
        ("Stars and the Solar System", "Physics", "Astronomy", 4, [], ["planets-and-satellites"]),
        ("Planets and Satellites", "Physics", "Astronomy", 4, ["stars-and-the-solar-system"], []),
        # Pollution
        ("Pollution of Air and Water", "Chemistry", "Environment", 4, ["composition-of-air", "water"], []),
        # Conservation
        ("Conservation of Plants and Animals", "Biology", "Environment", 4, ["forests-our-lifeline", "habitat-and-adaptation"], []),
    ],
    9: [
        # Matter
        ("Matter in Our Surroundings", "Chemistry", "Matter", 5, ["sorting-materials-into-groups"], ["states-of-matter"]),
        ("States of Matter", "Chemistry", "Matter", 5, ["matter-in-our-surroundings"], ["change-of-state"]),
        ("Change of State", "Chemistry", "Matter", 5, ["states-of-matter"], []),
        ("Is Matter Around Us Pure", "Chemistry", "Matter", 5, ["matter-in-our-surroundings"], ["mixtures-and-solutions"]),
        ("Mixtures and Solutions", "Chemistry", "Matter", 5, ["is-matter-around-us-pure"], ["types-of-solutions"]),
        ("Types of Solutions", "Chemistry", "Matter", 4, ["mixtures-and-solutions"], []),
        # Atoms and Molecules
        ("Atoms and Molecules", "Chemistry", "Atomic Structure", 5, ["is-matter-around-us-pure"], ["laws-of-chemical-combination"]),
        ("Laws of Chemical Combination", "Chemistry", "Atomic Structure", 4, ["atoms-and-molecules"], []),
        ("Structure of the Atom", "Chemistry", "Atomic Structure", 5, ["atoms-and-molecules"], ["atomic-number-and-mass-number"]),
        ("Atomic Number and Mass Number", "Chemistry", "Atomic Structure", 4, ["structure-of-the-atom"], []),
        ("Electron Configuration", "Chemistry", "Atomic Structure", 4, ["structure-of-the-atom"], []),
        # Cell Biology
        ("The Fundamental Unit of Life", "Biology", "Cell Biology", 5, ["cell-structure-and-functions"], ["cell-division"]),
        ("Cell Division", "Biology", "Cell Biology", 5, ["the-fundamental-unit-of-life"], []),
        # Tissues
        ("Tissues", "Biology", "Structural Organisation", 5, ["the-fundamental-unit-of-life"], ["plant-tissues"]),
        ("Plant Tissues", "Biology", "Structural Organisation", 4, ["tissues"], ["animal-tissues"]),
        ("Animal Tissues", "Biology", "Structural Organisation", 4, ["plant-tissues"], []),
        # Diversity in Living Organisms
        ("Diversity in Living Organisms", "Biology", "Classification", 5, ["the-living-and-non-living"], ["classification-of-organisms"]),
        ("Classification of Organisms", "Biology", "Classification", 5, ["diversity-in-living-organisms"], ["five-kingdom-classification"]),
        ("Five Kingdom Classification", "Biology", "Classification", 4, ["classification-of-organisms"], []),
        # Motion
        ("Motion", "Physics", "Mechanics", 5, ["motion-and-time", "speed-and-velocity"], ["distance-and-displacement"]),
        ("Distance and Displacement", "Physics", "Mechanics", 5, ["motion"], ["uniform-and-non-uniform-motion"]),
        ("Uniform and Non-Uniform Motion", "Physics", "Mechanics", 5, ["distance-and-displacement"], ["acceleration"]),
        ("Acceleration", "Physics", "Mechanics", 5, ["uniform-and-non-uniform-motion"], ["equations-of-motion"]),
        ("Equations of Motion", "Physics", "Mechanics", 5, ["acceleration"], []),
        ("Graphical Representation of Motion", "Physics", "Mechanics", 4, ["distance-and-displacement", "uniform-and-non-uniform-motion"], []),
        # Force and Laws of Motion
        ("Force and Laws of Motion", "Physics", "Mechanics", 5, ["force-and-pressure", "motion"], ["newtons-first-law"]),
        ("Newtons First Law", "Physics", "Mechanics", 5, ["force-and-laws-of-motion"], ["newtons-second-law"]),
        ("Newtons Second Law", "Physics", "Mechanics", 5, ["newtons-first-law"], ["newtons-third-law"]),
        ("Newtons Third Law", "Physics", "Mechanics", 5, ["newtons-second-law"], []),
        ("Conservation of Momentum", "Physics", "Mechanics", 4, ["newtons-second-law", "newtons-third-law"], []),
        # Gravitation
        ("Gravitation", "Physics", "Mechanics", 5, ["force-and-laws-of-motion"], ["universal-law-of-gravitation"]),
        ("Universal Law of Gravitation", "Physics", "Mechanics", 5, ["gravitation"], []),
        ("Free Fall and Acceleration Due to Gravity", "Physics", "Mechanics", 5, ["gravitation", "equations-of-motion"], []),
        ("Buoyancy and Archimedes Principle", "Physics", "Mechanics", 4, ["pressure-in-fluids", "gravitation"], []),
        # Work and Energy
        ("Work and Energy", "Physics", "Energy", 5, ["force-and-laws-of-motion"], ["kinetic-and-potential-energy"]),
        ("Kinetic and Potential Energy", "Physics", "Energy", 5, ["work-and-energy"], ["law-of-conservation-of-energy"]),
        ("Law of Conservation of Energy", "Physics", "Energy", 5, ["kinetic-and-potential-energy"], []),
        # Sound
        ("Sound", "Physics", "Sound", 5, ["vibration-and-sound-production"], ["propagation-of-sound"]),
        ("Propagation of Sound", "Physics", "Sound", 4, ["sound"], ["echo-and-reverberation"]),
        ("Echo and Reverberation", "Physics", "Sound", 4, ["propagation-of-sound"], []),
        # Health and Disease
        ("Why Do We Fall Ill", "Biology", "Health", 5, [], ["infectious-and-non-infectious-diseases"]),
        ("Infectious and Non-Infectious Diseases", "Biology", "Health", 4, ["why-do-we-fall-ill", "microorganisms-friend-and-foe"], []),
        # Natural Resources
        ("Natural Resources", "Biology", "Environment", 4, ["pollution-of-air-and-water"], ["biogeochemical-cycles"]),
        ("Biogeochemical Cycles", "Biology", "Environment", 4, ["natural-resources"], []),
        # Improvement in Food Resources
        ("Improvement in Food Resources", "Biology", "Agriculture", 4, ["crop-production-and-management"], []),
    ],
    10: [
        # Chemical Reactions
        ("Chemical Reactions and Equations", "Chemistry", "Chemical Reactions", 5, ["physical-and-chemical-changes", "atoms-and-molecules"], ["types-of-chemical-reactions"]),
        ("Types of Chemical Reactions", "Chemistry", "Chemical Reactions", 5, ["chemical-reactions-and-equations"], ["oxidation-and-reduction"]),
        ("Oxidation and Reduction", "Chemistry", "Chemical Reactions", 5, ["types-of-chemical-reactions"], []),
        ("Balancing Chemical Equations", "Chemistry", "Chemical Reactions", 4, ["chemical-reactions-and-equations"], []),
        # Acids Bases Salts
        ("Acids Bases and Salts", "Chemistry", "Acids and Bases", 5, ["acids-bases-and-salts", "chemical-reactions-and-equations"], ["ph-scale"]),
        ("pH Scale", "Chemistry", "Acids and Bases", 5, ["acids-bases-and-salts"], []),
        ("Salts and Their Properties", "Chemistry", "Acids and Bases", 4, ["acids-bases-and-salts"], []),
        # Metals and Non-Metals
        ("Metals and Non-Metals", "Chemistry", "Materials", 5, ["metals-and-non-metals", "chemical-reactions-and-equations"], ["reactivity-series"]),
        ("Reactivity Series", "Chemistry", "Materials", 5, ["metals-and-non-metals"], ["extraction-of-metals"]),
        ("Extraction of Metals", "Chemistry", "Materials", 4, ["reactivity-series"], []),
        # Carbon Compounds
        ("Carbon and Its Compounds", "Chemistry", "Organic Chemistry", 5, ["atoms-and-molecules"], ["hydrocarbons"]),
        ("Hydrocarbons", "Chemistry", "Organic Chemistry", 5, ["carbon-and-its-compounds"], ["functional-groups"]),
        ("Functional Groups", "Chemistry", "Organic Chemistry", 4, ["hydrocarbons"], []),
        ("Soaps and Detergents", "Chemistry", "Organic Chemistry", 3, ["carbon-and-its-compounds"], []),
        # Periodic Classification
        ("Periodic Classification of Elements", "Chemistry", "Periodic Table", 5, ["structure-of-the-atom", "electron-configuration"], ["modern-periodic-table"]),
        ("Modern Periodic Table", "Chemistry", "Periodic Table", 5, ["periodic-classification-of-elements"], ["periodic-trends"]),
        ("Periodic Trends", "Chemistry", "Periodic Table", 4, ["modern-periodic-table"], []),
        # Life Processes
        ("Life Processes", "Biology", "Life Processes", 5, ["the-fundamental-unit-of-life"], ["nutrition-in-human-beings"]),
        ("Nutrition in Human Beings", "Biology", "Life Processes", 5, ["life-processes", "digestive-system"], ["respiration-in-human-beings"]),
        ("Respiration in Human Beings", "Biology", "Life Processes", 5, ["nutrition-in-human-beings", "breathing-and-cellular-respiration"], []),
        ("Transportation in Human Beings", "Biology", "Life Processes", 5, ["life-processes", "circulatory-system"], []),
        ("Excretion in Human Beings", "Biology", "Life Processes", 4, ["transportation-in-human-beings"], []),
        # Control and Coordination
        ("Control and Coordination", "Biology", "Human Biology", 5, ["tissues", "life-processes"], ["nervous-system"]),
        ("Nervous System", "Biology", "Human Biology", 5, ["control-and-coordination"], ["reflex-action"]),
        ("Reflex Action", "Biology", "Human Biology", 4, ["nervous-system"], []),
        ("Hormones and Endocrine System", "Biology", "Human Biology", 4, ["control-and-coordination"], []),
        # Reproduction
        ("How Do Organisms Reproduce", "Biology", "Reproduction", 5, ["sexual-and-asexual-reproduction", "cell-division"], ["reproductive-system"]),
        ("Reproductive System", "Biology", "Reproduction", 4, ["how-do-organisms-reproduce"], []),
        # Heredity and Evolution
        ("Heredity and Evolution", "Biology", "Genetics", 5, ["how-do-organisms-reproduce", "diversity-in-living-organisms"], ["mendels-laws"]),
        ("Mendels Laws", "Biology", "Genetics", 5, ["heredity-and-evolution"], ["natural-selection-and-speciation"]),
        ("Natural Selection and Speciation", "Biology", "Genetics", 4, ["mendels-laws"], []),
        # Light
        ("Light Reflection and Refraction", "Physics", "Optics", 5, ["reflection-and-refraction", "laws-of-reflection"], ["mirror-formula-and-magnification"]),
        ("Mirror Formula and Magnification", "Physics", "Optics", 4, ["light-reflection-and-refraction"], []),
        ("Refraction Through Glass Slab", "Physics", "Optics", 4, ["light-reflection-and-refraction"], ["lens-formula"]),
        ("Lens Formula", "Physics", "Optics", 4, ["refraction-through-glass-slab"], []),
        # Human Eye
        ("Human Eye and Colourful World", "Physics", "Optics", 5, ["light-reflection-and-refraction", "dispersion-of-light"], ["defects-of-vision"]),
        ("Defects of Vision", "Physics", "Optics", 4, ["human-eye-and-colourful-world"], []),
        ("Scattering of Light", "Physics", "Optics", 3, ["human-eye-and-colourful-world"], []),
        # Electricity
        ("Electricity", "Physics", "Electricity", 5, ["chemical-effects-of-electric-current"], ["ohms-law"]),
        ("Ohms Law", "Physics", "Electricity", 5, ["electricity"], ["resistance-and-resistivity"]),
        ("Resistance and Resistivity", "Physics", "Electricity", 5, ["ohms-law"], ["series-and-parallel-circuits"]),
        ("Series and Parallel Circuits", "Physics", "Electricity", 5, ["resistance-and-resistivity"], []),
        ("Electric Power and Energy", "Physics", "Electricity", 4, ["ohms-law"], []),
        # Magnetic Effects
        ("Magnetic Effects of Electric Current", "Physics", "Electromagnetism", 5, ["electricity", "properties-of-magnets"], ["electromagnetic-induction"]),
        ("Electromagnetic Induction", "Physics", "Electromagnetism", 5, ["magnetic-effects-of-electric-current"], []),
        ("Electric Motor and Generator", "Physics", "Electromagnetism", 4, ["magnetic-effects-of-electric-current"], []),
        # Energy Sources
        ("Sources of Energy", "Physics", "Energy", 4, ["work-and-energy", "law-of-conservation-of-energy"], ["renewable-and-non-renewable-energy"]),
        ("Renewable and Non-Renewable Energy", "Physics", "Energy", 4, ["sources-of-energy", "fossil-fuels"], []),
        # Environment
        ("Our Environment", "Biology", "Environment", 4, ["natural-resources"], ["food-chains-and-webs"]),
        ("Food Chains and Webs", "Biology", "Environment", 4, ["our-environment"], []),
        ("Management of Natural Resources", "Biology", "Environment", 3, ["our-environment", "conservation-of-plants-and-animals"], []),
    ],
}


def build_grade_graph(grade: int, concepts_data: list) -> dict:
    """Build a single grade's knowledge graph in the exact maths KG format."""
    concepts = {}
    edges = []
    entry_points = []

    for name, domain, area, importance, prereqs, related in concepts_data:
        slug = slugify(name)
        concept = {
            "canonical_name": name,
            "slug": slug,
            "aliases": [],
            "domain": domain,
            "area": area,
            "parent": None,
            "grades": [grade],
            "importance_by_grade": {str(grade): importance},
            "source_boards": ["NCERT", "ICSE"],
            "subject": "science",
            "prerequisites": prereqs,
            "leads_to": [],
            "related": related,
            "see_also": [],
        }
        concepts[slug] = concept

        # Build edges from prerequisites
        for prereq in prereqs:
            edges.append({
                "from": prereq,
                "to": slug,
                "type": "prerequisite",
            })

        # Entry points = concepts with no prerequisites within this grade
        if not prereqs:
            entry_points.append(slug)

    # Compute leads_to from prerequisites
    for slug, concept in concepts.items():
        for prereq_slug in concept["prerequisites"]:
            if prereq_slug in concepts:
                concepts[prereq_slug]["leads_to"].append(slug)

    # Recompute entry_points: concepts that no other concept in this grade has as prerequisite target
    targets = set()
    for e in edges:
        if e["from"] in concepts:
            targets.add(e["to"])
    grade_entry = [s for s in concepts if s not in targets]
    if grade_entry:
        entry_points = grade_entry

    return {
        "grade": grade,
        "subject": "science",
        "concepts": concepts,
        "edges": edges,
        "entry_points": entry_points,
    }


def main():
    GRADE_DIR.mkdir(parents=True, exist_ok=True)
    SUBJECT_DIR.mkdir(parents=True, exist_ok=True)

    all_concepts = {}
    all_edges = []

    for grade in sorted(SCIENCE_CURRICULUM.keys()):
        data = SCIENCE_CURRICULUM[grade]
        graph = build_grade_graph(grade, data)

        out_path = GRADE_DIR / f"grade{grade}_science.json"
        out_path.write_text(json.dumps(graph, ensure_ascii=False, indent=2))

        n_concepts = len(graph["concepts"])
        n_edges = len(graph["edges"])
        n_entry = len(graph["entry_points"])
        print(f"✓ grade{grade}_science.json: {n_concepts} concepts, {n_edges} edges, {n_entry} entry_points")

        # Merge into subject graph
        all_concepts.update(graph["concepts"])
        all_edges.extend(graph["edges"])

    # Build subject-level graph
    subject_graph = {
        "subject": "science",
        "total_concepts": len(all_concepts),
        "total_edges": len(all_edges),
        "concepts": all_concepts,
        "edges": all_edges,
        "grade_views": {},
    }
    for grade in sorted(SCIENCE_CURRICULUM.keys()):
        grade_path = GRADE_DIR / f"grade{grade}_science.json"
        g = json.loads(grade_path.read_text())
        subject_graph["grade_views"][str(grade)] = {
            "concepts": list(g["concepts"].keys()),
            "entry_points": g["entry_points"],
            "count": len(g["concepts"]),
        }

    subject_path = SUBJECT_DIR / "science.json"
    subject_path.write_text(json.dumps(subject_graph, ensure_ascii=False, indent=2))
    print(f"\n✓ science.json: {subject_graph['total_concepts']} concepts, {subject_graph['total_edges']} edges")
    print(f"\nAll files saved to {KG_DIR}")


if __name__ == "__main__":
    main()
