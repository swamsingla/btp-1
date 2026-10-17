# PDF extraction evaluation — choosing the text extractor

The old pipeline read NCERT PDFs with PyMuPDF's text layer. That text breaks
mathematics (`1/5` → `1 5`, `7²` → `72`, `13²` → `132`) and silently misses
equations that are not in the text layer. Every later stage (concept–passage
linking, grounding, generation) inherits these errors, so the extractor was
re-chosen by measuring accuracy on real textbook pages.

## Test set (43 pages)

| File | Pages | Why |
|---|---|---|
| Grade 10 Maths ch 4 — Quadratic Equations | 11 | Inline and display algebra, fractions, radicals |
| Grade 11 Physics ch 2 — Motion in a Straight Line | 14 | Two-column layout, calculus, equation numbers, units |
| Grade 10 Science ch 1 — Chemical Reactions and Equations | 16 | Chemical equations, state symbols, conditions over arrows, tables |
| Grade 6 Maths ch 7 — Fractions (2 pages) | 2 | The known `1/5 → 1 5` failure |

## Method

1. Every answer-key page was rendered to an image and read by eye to write
   `answer_key.json`: 41 checks (formulas, equations, a table, reading order,
   headings, fractions).
2. Each tool converted the same PDFs (`outputs/<tool>/`).
3. `extract_sections.py <outputs/tool>` pulls the same page regions from every
   output, so each tool is scored on identical text.
4. Each check is scored 2 = correct, 1 = minor defect with meaning intact,
   0 = wrong or missing (`scores.json`, with a note for every non-2 score).
5. `katex_check.js <file.md>` renders every formula with KaTeX (the renderer the
   web app uses) and lists the ones that fail.

## Results

| Section | PyMuPDF (old) | Marker 2.0 (balanced) | MinerU 4.0 (standard) |
|---|---|---|---|
| Maths — Quadratic Equations | 3/22 | 11/22 | **21/22** |
| Physics — Motion | 3/28 | 19/28 | **26/28** |
| Chemistry — Reactions | 4/20 | 11/20 | **18/20** |
| Grade 6 fractions | 0/12 | 4/12 | **12/12** |
| **Total** | **10/82 (12%)** | **45/82 (55%)** | **77/82 (94%)** |

Speed on an RTX 3050 Laptop GPU (4 GB), 41 pages including model start-up:
MinerU 18.2 s/page, Marker 14.1 s/page. At those rates the 5,089 NCERT pages
take about 26 h with MinerU and 20 h with Marker.

**Decision: MinerU 4.0, standard tier, run fully locally** (`scripts/extract_markdown.py`).
Marker is faster but leaves most inline fractions as `<sup>1</sup> 5`, drops
factors inside derivations, and scrambles reading order on the chemistry pages.

## What went wrong in each tool

- **PyMuPDF:** superscripts flattened (`b2`, `132`), every fraction and radical
  shattered across lines, chemistry equations 1.8–1.12 missing entirely,
  decorative headings repeated five times.
- **Marker 2.0:** inline fractions as HTML `<sup>` fragments; minus signs turned
  into bullet points; `v̄` lost its bar; `dx/dt` factor dropped; `³Fe` for `3Fe`;
  Step VI placed before Step V; raw HTML leaked into one table cell.
- **MinerU 4.0 (defects to clean up when splitting into passages):**
  - running headers, page numbers and `Reprint 2025-26` kept as separate lines;
  - one equation with two `\tag` commands (KaTeX refuses to render it);
  - three `$a$$b$` pairs in a table (ambiguous for Markdown math parsers);
  - an equation label occasionally separated from its equation;
  - figures replaced by `![Image block](doc:…)` placeholders (captions kept).

## Privacy

MinerU 4 can parse through a remote API. The extraction script refuses to run
unless `parse_server.local.mode = managed` (local parsing) and telemetry is
disabled, so no document leaves the machine.
