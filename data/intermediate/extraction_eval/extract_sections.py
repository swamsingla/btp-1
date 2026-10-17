"""Print the answer-key regions from one tool's output so every tool is scored on the same text.

Usage: python extract_sections.py <tool_output_dir> [section]
"""
import re
import sys
from pathlib import Path

# (name, pdf stem, start regex, end regex, chars of context before start)
SECTIONS = [
    ("maths_p8_p9", "g10_maths_ch4_quadratic", r"has\s+two\s+equal", r"Example\s*\**\s*10", 400),
    ("physics_p5_p6", "g11_physics_ch2_motion", r"curve\s+is\s+a\s+straight\s+line\s+parallel", r"methods\s+used", 300),
    ("chem_p5", "g10_science_ch1_chemical_reactions", r"Step\s*V\b|Step V:", r"Using these steps", 0),
    ("chem_p11", "g10_science_ch1_chemical_reactions", r"iron nail become", r"\(1\.27\)|1\.27", 0),
    ("fractions_p1", "g6_maths_ch7_fractions_2pages", r"roti", r"sugarcane juice", 200),
]


def region(text: str, start: str, end: str, before: int) -> str:
    s = re.search(start, text)
    if not s:
        return f"[start anchor {start!r} not found]"
    e = re.search(end, text[s.end():])
    stop = s.end() + e.end() + 250 if e else s.end() + 6000
    return text[max(0, s.start() - before):stop]


def main() -> None:
    out_dir = Path(sys.argv[1])
    only = sys.argv[2] if len(sys.argv) > 2 else None
    for name, stem, start, end, before in SECTIONS:
        if only and name != only:
            continue
        files = sorted(out_dir.rglob(f"{stem}*.md"))
        if not files:
            print(f"===== {name}: no output file for {stem}")
            continue
        text = files[0].read_text(encoding="utf-8")
        print(f"===== {name} ({files[0].name})")
        print(region(text, start, end, before))
        print()


if __name__ == "__main__":
    main()
