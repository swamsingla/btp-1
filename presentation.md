# GraphLearn
### A Knowledge-Graph-Driven Multilingual Educational Platform for School Mathematics and Science

**Saksham Chitkara** · Roll No. ___________
**Swam Singla** · Roll No. ___________

International Institute of Information Technology, Hyderabad
BTP-1

---

## Previous Approach — Pipeline v1 Flowchart

```
PDF Textbooks (Grades 6–12)
           │
           ▼
   Stage 1: PDF Parsing
   Heading & Topic Extraction
           │
           ▼
   Stage 2: LLM Content Generation
   (Llama 3.2 3B, 4-bit quantized)
   One page per chapter section
           │
           ▼
   Stage 3: Translation Pipeline
   English → Hindi, Telugu, Odia
   (IndicTrans2 / Sarvam / TranslateGemma)
           │
           ▼
   Stage 4: Database Upload
   MongoDB Atlas
           │
           ▼
   Web Interface
   /grade/9/maths/chapter/1/topic/2
```

---

## Problems with Pipeline v1

**Problem 1: Content tied to chapter numbers, not concepts**
"Irrational Numbers" in Grade 9 had no connection to its Grade 10 and Grade 11 treatments — three separate disconnected pages.

**Problem 2: Inconsistency across topics**
The LLM generated content independently for each topic with no memory of what it had said before — definitions, notation, and conventions differed across sections.

**Problem 3: Hallucination in mathematical content**
Llama 3.2 3B occasionally made errors in multi-step reasoning — proofs and derivations that look plausible but are mathematically wrong — with no verification step.

**Problem 4: Translation inconsistency across batches**
The Hindi term for "derivative" in Chapter 1 was sometimes different from the one in Chapter 5 — the model made an independent choice each time.

**Problem 5: LaTeX corruption in edge cases**
The placeholder approach for preserving LaTeX failed when expressions were embedded in complex ways — sentence boundaries broke and the translation model saw grammatically incoherent fragments.

**Problem 6: No concept-level navigation**
A student reading about "Real Numbers" had no way to navigate to "Rational Numbers" or "Integers" — the structure was linear and flat, exactly like a digitised textbook.

**Problem 7: Repeated work across chapters**
"Polynomials" appears in Grade 9 Chapter 2 and Grade 10 Chapter 2 — the pipeline generated separate, inconsistent pages for both with no shared content or cross-referencing.

---

## New Approach — Pipeline v2 Flowchart

```
PDF Textbooks + ICSE + State Board Syllabi
           │
           ▼
   Stage 1: Multi-Source Topic Ingestion
   (topic_ingestion.py + Llama 8B)
           │
           ▼
   Stage 2: Canonical Concept Discovery
   (graph_builder.py + Llama 8B)
   LLM output → manually reviewed and edited
           │
           ▼
   Stage 3: Manual Graph Construction & Validation
   (NetworkX DAG validation, 4 revision cycles)
   324 concepts · 497 edges · 18 areas
           │
           ▼
   Stage 4: Graph-RAG Context Assembly
   (graph_rag.py)
   Graph edges + textbook chunks + Wikipedia
           │
           ▼
   Stage 5: Direct Multilingual Generation
   (Sarvam-30B API)
   English · Hindi · Telugu · Odia — no translation step
           │
           ▼
   Web Platform
   /maths/9/quadratic-equations
   Prerequisites ← · Leads To →
```

---

## Stage 1 — Multi-Source Topic Ingestion

- Collected topics from multiple curriculum sources: textbook headings (already extracted), ICSE syllabus, and selected state board syllabi (Karnataka and Maharashtra)
- Raw topics from all sources merged and stored as JSON files per grade per subject
- Produced 11 raw topic files — Grade 6 Maths: 86 topics, Grade 12 Maths: 56 topics (Grade 12 lower as subtopics consolidated later)
- Each topic entry includes: raw name, subtopics, source boards, and curriculum reference

---

## Stage 2 — Canonical Concept Discovery with LLM Assistance

- Raw topic lists contain duplicates, overlapping topics, and topics at inconsistent levels of granularity
- Llama used as a "curriculum expert" — prompted with full raw topic list for a grade and asked to propose canonical concept names and groupings
- Model identified which topics refer to the same underlying concept and assigned Wikipedia-style names (e.g., "3.2 Equivalent Fractions" → "Fractions")
- LLM output was then manually reviewed and edited — prerequisite edge suggestions verified against actual curriculum sequence

---

## Stage 3 — Manual Graph Construction and Validation

- Built the actual knowledge graph manually — each concept defined with: slug, canonical name, grades it appears in, mathematical area, prerequisite concepts, and description
- Graph validated on every build: all prerequisite slugs must exist; no cycles allowed — graph must be a valid DAG; `leads_to` edges computed automatically as the reverse of prerequisite edges
- LLM output was too sparse — missed many prerequisite relationships and could not link concepts across grades; required a significant amount of manual addition and verification which took a lot of time
- Went through 4 complete revision cycles before the graph was reliable
- **Final: 324 concepts · 497 directed prerequisite edges · 18 mathematical areas · 0 cycles**

---

## Stage 4 — RAG-Based Content Generation

- For each concept, retrieve reference chunks from the relevant textbook sections using vector similarity search — retrieved chunks provide verified, curriculum-aligned grounding material
- Assemble prerequisite context: for each prerequisite of the concept, include a summary of that prerequisite's content in the prompt
- Call the generation model with: concept name, grade level, retrieved reference chunks, summaries of prerequisite concepts, and generation instruction
- Verify the output with a lightweight pass that checks for mathematical consistency and flags potential hallucinations

---

## Stage 5 — Direct Multilingual Generation via Sarvam

- Translation step from Pipeline v1 replaced entirely by direct multilingual generation — generate in Hindi, Telugu, and Odia directly, no translation involved
- Sarvam-30B model trained on large corpora of Indian educational content — handles mathematical terminology in Indic languages significantly better than a general-purpose model followed by translation
- No LaTeX corruption risk — the model generates LaTeX natively, it does not need to translate through it
- Consistent terminology — the model has a fixed internal vocabulary for mathematical terms in each language, so "derivative" maps to the same Hindi term throughout
- Single model call instead of generate + translate (two passes)

---

## Thank You

**GraphLearn — BTP-1**
Saksham Chitkara · Swam Singla
International Institute of Information Technology, Hyderabad


### A Knowledge-Graph-Driven Educational Platform for School Mathematics and Science

**The core idea:**
> Instead of treating a textbook as a collection of chapters and sections, we model the entire curriculum as a **network of concepts** — where every concept is a node, and a directed edge from A → B means "you must understand A before B makes sense."

**What the platform does:**
- Student visits a concept page (e.g., *Quadratic Equations*)
- Sees **what they need to know first** (prerequisites) — each one is a clickable link
- Sees **what this concept unlocks** (next topics they can learn)
- Navigates the full curriculum like Wikipedia — following links between ideas, not flipping through chapters

**Scope of the current system:**
| Subject | Concepts | Prerequisite Links | Grades |
|---|---|---|---|
| Mathematics | 324 | 497 | 6 – 12 |
| Science | 382 | 552 | 6 – 12 |

**Target:** Multi-board coverage (NCERT, ICSE, state boards) in English, Hindi, Telugu, and Odia.

---

## SLIDE 2 — Past Approach: Pipeline v1 Flowchart

```
╔══════════════════════════════════════════════════════════════════╗
║                    PIPELINE v1  (Linear / Chapter-Based)         ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  INPUT:  PDF Textbooks (Grade 6–12)      │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  STEP 1 — Heading Extractor              │                   ║
║  │  (pdfplumber + font-size heuristics)     │                   ║
║  │  Output: chapter → section JSON          │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  STEP 2 — LLM Content Generation         │                   ║
║  │  (Llama 3.2 3B, 4-bit quantized)         │                   ║
║  │  One page generated per chapter section  │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  STEP 3 — Translation Pipeline           │                   ║
║  │  (IndicTrans2 / Sarvam / TranslateGemma) │                   ║
║  │  EN → Hindi, Telugu, Odia               │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  STEP 4 — Database Upload                │                   ║
║  │  (MongoDB Atlas via db_uploader.py)      │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  OUTPUT: Web App                         │                   ║
║  │  /grade/9/maths/chapter/1/topic/2        │                   ║
║  └─────────────────────────────────────────┘                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## SLIDE 3 — Past Approach: Pipeline v1 — Steps in Detail

### Step 1 — PDF Parsing and Heading Extraction
Script: `extract_headings.py` using **PyMuPDF** and **pdfplumber**

- Each PDF chapter is scanned; headings are identified by their **font size and style** (anything not matching the "body text" font signature is treated as a heading candidate).
- Noise is filtered out (page numbers, figure captions, roman numerals, copyright text).
- Output: a structured JSON per chapter listing all section numbers and titles.
- Example: Grade 9 Chapter 1 → `[{1.1 Introduction}, {1.2 Irrational Numbers}, ...]`

### Step 2 — LLM Content Generation
Script: `approach_a/content_gen.py` using **Llama 3.2 3B Instruct (4-bit, NF4 quantized)**

- For each extracted section, the model first runs an **importance scoring pass** (rate 1–5 for this grade) — more important sections get longer, richer content.
- Then generates a **7-part structured page**: Prerequisites → Introduction → Explanation → Solved Examples → Common Mistakes → Practice Tips → Summary.
- Prompts are **grade-aware**: Grade 6 uses simple friendly language; Grade 12 uses rigorous, JEE-level treatment.
- Math notation is written in **KaTeX-compatible LaTeX** ($...$ inline, $$...$$ display).

### Step 3 — Translation Pipeline
Script: `approach_a/translator.py` — three models tested:

- **IndicTrans2** (`ai4bharat/indictrans2-en-indic-1B`) — best for Hindi/Telugu; needs transformers ≤ 4.45 (separate venv required)
- **Sarvam Translate** — Gemma3-based; stronger on educational vocabulary
- **TranslateGemma** (Google) — comparable quality, 4-bit quantized
- **LaTeX protection**: Before translation, all `$...$` and `$$...$$` segments are extracted, replaced with placeholders, translated text is assembled, then LaTeX is reinserted.
- Terminology conservation files stored per chapter to keep domain terms consistent.

### Step 4 — Database Upload
Script: `approach_a/db_uploader.py` — upsert to **MongoDB Atlas**

- Two collections: `chapters` (metadata) and `topics` (content with fields `content_en`, `content_hi`, `content_te`, `content_od`)
- Pages served at URLs: `/grade/{N}/{subject}/chapter/{N}/topic/{N}`
- **Completed**: Full Grade 9 Mathematics (Chapters 1–3) generated, translated, and uploaded

---

## SLIDE 4 — What Went Wrong: The 7 Problems

> *"We built the whole thing, ran it end-to-end, looked at the output carefully — and found that the fundamental design was wrong."*

### Problem 1 — Chapter sections, not concepts ❌
"Irrational Numbers" lived at `/grade/9/chapter/1/topic/2`. But irrational numbers appear again in Grade 10 and underpin Grade 12 calculus. Three separate, disconnected pages with no link between them. **Zero cross-grade navigation.**

### Problem 2 — No prerequisite structure ❌
A student on "Real Numbers" had no way to know they needed "Rational Numbers" first. The platform was as flat and linear as the printed textbook — no added value for discoverability.

### Problem 3 — LLM hallucinations in math ❌
Llama 3.2 3B occasionally generated **plausible-looking but mathematically wrong** proofs and derivations — especially for multi-step content like proving √2 is irrational. No verification step meant errors went live.

### Problem 4 — Content inconsistency across topics ❌
Each section was generated in isolation. The definition of "irrational number" in section 1.2 sometimes differed from how section 1.4 described it — different wording, notation, conventions.

### Problem 5 — Terminology drift in translation ❌
The Hindi word for "derivative" was different in Chapter 1 versus Chapter 5. The model made an independent choice each time. **Mathematical terminology in Indic languages is not standardized**, so the model picked different valid translations across batches.

### Problem 6 — LaTeX corruption (~8% failure rate) ❌
The placeholder approach worked 92% of the time. The remaining 8% had broken braces, translated subscripts, or split delimiters — producing corrupted formulas in the translated output.

### Problem 7 — Wrong fundamental abstraction ❌
The root cause of all the above: **we built around chapters, not concepts.** Chapters are a publishing artifact — how textbooks are printed. Concepts are what students actually learn. The same concept (e.g., Fractions) appears across 4 grades — we generated 4 inconsistent, unlinked pages for it.

> **Core insight:** The first-class unit of the system must be the **concept**, not the chapter section.

---

## SLIDE 5 — New Approach: Pipeline v2 Flowchart

```
╔══════════════════════════════════════════════════════════════════╗
║              PIPELINE v2  (Knowledge-Graph Based)                ║
╠══════════════════════════════════════════════════════════════════╣
║                                                                  ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  INPUT:  PDFs + Multi-Board Syllabi      │                   ║
║  │  (NCERT, ICSE, state boards)             │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  STEP 1 — Topic Ingestion                │                   ║
║  │  (topic_ingestion.py + Llama 8B)         │                   ║
║  │  Output: raw_topics JSONs per grade      │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  STEP 2 — Canonical Concept Hierarchy    │                   ║
║  │  (graph_builder.py + Llama 8B)           │                   ║
║  │  Flat topics → Domain > Area > Concept  │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  STEP 3 — Manual Graph Construction      │ ◄── ⚠️ HEAVY      ║
║  │  (Python + NetworkX DAG validation)      │      MANUAL WORK  ║
║  │  Llama output too sparse → full manual   │                   ║
║  │  addition, edge-by-edge verification     │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  OUTPUT: maths_v2.json                   │                   ║
║  │  324 concepts · 497 edges · 18 areas    │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  STEP 4 — Graph-RAG Context Assembly     │                   ║
║  │  (graph_rag.py)                          │                   ║
║  │  Per concept: graph edges + textbook     │                   ║
║  │  chunks + Wikipedia → content_plan.json  │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  STEP 5 — Direct Multilingual Generation │                   ║
║  │  (generate.py + Sarvam API)              │                   ║
║  │  One API call → EN + HI + TE + OD        │                   ║
║  │  No translation step at all              │                   ║
║  └────────────────────┬────────────────────┘                    ║
║                       ▼                                          ║
║  ┌─────────────────────────────────────────┐                    ║
║  │  OUTPUT: Web App                         │                   ║
║  │  /maths/9/quadratic-equations            │                   ║
║  │  Prerequisites ← · Leads To →           │                   ║
║  └─────────────────────────────────────────┘                    ║
║                                                                  ║
╚══════════════════════════════════════════════════════════════════╝
```

---

## SLIDE 6 — Step 1: Topic Ingestion

**Goal:** Build a comprehensive, multi-board list of *all topics* a student should learn, per grade per subject.

**Script:** `scripts/topic_ingestion.py`

### How it works:
1. **From the PDFs** — heading extraction (already done in Pipeline v1) gives us the NCERT chapter structure for each grade. These are loaded from `data/intermediate/headings/`.

2. **LLM-powered expansion** — Llama 8B is prompted with the NCERT headings and asked:
   *"What other topics from ICSE and state board syllabi belong at this grade level? What subtopics sit under each heading?"*
   
3. The model returns a structured list with `subtopics`, `source_boards`, and curriculum references.

### Output — one JSON file per grade per subject:
```
data/intermediate/raw_topics/
  grade6_maths.json     (86 topics, each with 4-6 subtopics)
  grade7_maths.json     (71 topics)
  grade8_maths.json     (78 topics)
  grade9_maths.json     (68 topics)
  ...
  grade6_science.json
  grade7_science.json
  ...
```

### Example entry (Grade 6 Maths):
```json
{
  "raw_name": "Patterns in Numbers",
  "ncert_refs": ["chapter1"],
  "subtopics": [
    "Identifying and writing number patterns using variables",
    "Creating and extending number patterns",
    "Triangular numbers, square numbers, cube numbers"
  ],
  "source_boards": ["NCERT", "ICSE"]
}
```

**Key point:** At this stage, topics are *raw* — duplicated, at inconsistent granularity, and not yet connected to each other. The next step cleans this up.

---

## SLIDE 7 — Step 2: Canonical Concept Hierarchy (LLM-Assisted)

**Goal:** Convert the messy raw topic lists into clean, canonical concept names — the kind a student would search for on Wikipedia.

**Script:** `scripts/graph_builder.py` — uses **Llama 8B locally** (fits in 4 GB VRAM at 4-bit quantization)

### What "canonical" means:
- "3.2 Equivalent Fractions" (a NCERT section heading) → **"Fractions"** (the concept)
- "1.1 Introduction to Irrational Numbers" → **"Irrational Numbers"**
- Topics that refer to the same concept across boards are merged into one

### Two LLM passes:

**Pass 1 — Hierarchy extraction:**
The model sees the full raw topic list for a grade and produces a 4-level hierarchy:

```
Domain
  └── Area  (e.g., Algebra)
        └── Concept  (e.g., Quadratic Equations)
              └── Sub-concept  (e.g., Completing the Square)
```

Each concept gets:
- A **slug** (URL-safe name: `quadratic-equations`)
- **Grade assignments** (only grades where it appears in the input)
- An **importance score** (1–5) per grade

**Pass 2 — Prerequisite edge proposal:**
The model is given the concept list and asked to identify which concepts are prerequisites for which others. It outputs a list of directed edges: `A → B` meaning "A must be learned before B."

### The manual review that follows
→ **Every single LLM-proposed edge was checked by hand against the actual curriculum.** Wrong edges removed. Missing edges added.

This is where the real work began — and where the model fell short.

---

## SLIDE 8 — Step 3: Manual Graph Construction ⚠️ The Hard Part

**Goal:** Produce a dense, accurate, validated knowledge graph where every edge is correct.

**The problem with the Llama 8B output:**

The model processed grade-by-grade raw topics and proposed concept hierarchies and prerequisite edges — but the results were **too sparse and incomplete**:

- It missed many prerequisite relationships that are obvious to a human (e.g., it didn't connect "Fractions" → "Ratio and Proportion" reliably)
- It couldn't link concepts **across grades** well (e.g., it didn't know that Grade 12 "Integration by Parts" requires Grade 11 "Integration by Substitution" requires Grade 11 "Chain Rule of Differentiation")
- It sometimes hallucinated prerequisite edges that don't exist in the curriculum
- The per-grade processing meant cross-grade connections were almost entirely missing

**What was actually required:**

We had to **manually go through every concept**, one by one, and:
1. Verify the concept name and description were accurate
2. Check every proposed prerequisite edge — keep, remove, or correct
3. Add all the missing edges the model didn't catch
4. Add missing concepts the model had lumped together or skipped entirely
5. Resolve naming conflicts between grades (same concept, different names used by different boards)
6. Run cycle detection after every batch of additions to catch circular dependencies immediately

This process went through **4 complete revision cycles** (v1 → v2 → v3 → v4 of the graph).

**How the builder works technically:**
```python
# Each concept defined as a tuple:
("quadratic-equations", "Quadratic Equations", [9, 10], "Algebra",
 ["linear-equations", "factorisation", "square-roots"],
 "Polynomial equations of degree 2; solving by factorisation, ...")
```

- **NetworkX** is used to build a DiGraph and run `nx.find_cycle()` after every change — any cycle fails the build immediately with the exact cycle path shown.
- `leads_to` edges are **automatically computed** as the reverse of prerequisite edges — no manual entry needed.
- Per-grade subgraphs (entry points, concept sets) are derived automatically from the main graph.

**Time investment:** The manual graph construction phase was by far the most time-consuming part of the entire project. The LLM gave us a rough scaffold; turning that scaffold into a reliable educational artifact required significant expert effort.

**Final output:**
```
maths_v2.json (v4)
  ├── 324 concepts  (Grades 6–12)
  ├── 497 directed prerequisite edges
  ├── 18 mathematical areas
  └── 0 cycles (validated)

science.json
  ├── 382 concepts  (Grades 6–12)
  └── 552 directed prerequisite edges
```

---

## SLIDE 9 — Step 4: Graph-RAG Context Assembly

**Goal:** For each concept, gather everything an LLM would need to write a great explanation page — from three sources simultaneously.

**Script:** `scripts/approach_b/graph_rag.py`

### What is Graph-RAG?

RAG = **Retrieval-Augmented Generation** — instead of asking the LLM to generate content from memory alone (where it might hallucinate), we first *retrieve* relevant reference material and include it in the prompt.

"Graph-RAG" = RAG + **knowledge graph context**. The graph itself tells us what related concepts exist, what the student already knows (prerequisites), and what they'll learn next.

### Three sources assembled per concept × grade:

```
┌────────────────────────────────────────────────────────┐
│          CONTEXT ASSEMBLY  for  "Quadratic Equations"  │
│                            Grade 9                     │
├────────────────────────────────────────────────────────┤
│  SOURCE 1 — Knowledge Graph structure                  │
│  • Prerequisites: Linear Equations, Factorisation,     │
│    Square Roots                                        │
│  • Leads to: Completing the Square, Quadratic Formula, │
│    Complex Roots of Quadratic                          │
│  • Same-area concepts: Polynomial Expressions, etc.   │
├────────────────────────────────────────────────────────┤
│  SOURCE 2 — Textbook chunks (fuzzy-matched)            │
│  • Top 5 chunks from parsed PDFs that match this       │
│    concept (using fuzzy string matching, threshold 62) │
│  • Actual curriculum text the explanation must align to│
├────────────────────────────────────────────────────────┤
│  SOURCE 3 — Wikipedia summary (optional)               │
│  • First ~2500 chars of the Wikipedia article          │
│  • Provides definitions and broader context            │
└────────────────────────────────────────────────────────┘
               │
               ▼
  data/content_plans/maths/quadratic-equations_grade9.json
```

### Output: one content plan per concept × grade
The content plan contains everything pre-assembled — graph edges, text chunks, Wikipedia summary — as a single JSON file. The generator reads this and builds the prompt without needing to query anything at generation time.

**Scale:** For 324 maths concepts across 7 grades, this produces up to ~500 content plan files. The process is parallelized (12 Wikipedia fetch threads simultaneously).

---

## SLIDE 10 — Step 5: Direct Multilingual Generation

**Goal:** Generate polished, curriculum-aligned explanation pages in all 4 languages in a single step — no translation involved.

**Script:** `scripts/approach_b/generate.py` — calls **Sarvam AI API**

### Why direct generation instead of translate?

| Translate approach (v1) | Direct generation (v2) |
|---|---|
| Generate in English, then translate | Generate in target language directly |
| LaTeX expressions can get corrupted | LaTeX is never "translated" — generated natively |
| Terminology inconsistent across batches | Model has fixed vocabulary for math terms |
| Two API/model calls per page | One API call per language per page |
| Hindi term for "derivative" varies | Consistent Indic terminology throughout |

### What the Sarvam API receives:
A single rich prompt containing:
- Concept name, grade level, and area
- Prerequisite concept descriptions (from graph)
- "What this unlocks" successor concepts
- Retrieved textbook chunks (grounding)
- Wikipedia context
- Language instruction: *"Write entirely in Hindi (Devanagari script). Keep all LaTeX expressions in Latin script."*

### Output structure (7-section page):
```
1. Prerequisites (with links back to graph concepts)
2. Introduction  
3. Core Explanation (with LaTeX formulas)
4. Worked Examples
5. Common Mistakes
6. See Also (leads_to concepts)
7. Summary
```

### Output location:
```
data/generated_pages/
  en/fractions_grade6.md
  hi/fractions_grade6.md
  te/fractions_grade6.md
  od/fractions_grade6.md
```

### Current status:
The pipeline is **built and tested** on individual concepts. Full generation for all 324 × 7 grade × 4 language combinations requires Sarvam API credits — generation is in progress.

---

## SLIDE 11 — The Web Platform (What You Can See Now)

**Stack:** Next.js 16.2 (App Router, React Server Components) + Tailwind CSS

### What's live today at localhost:3000:

```
/                           ← Home: both subjects, stats, grade cards
/maths                      ← Mathematics hub (324 concepts, 497 links)
/maths/{grade}              ← All concepts for that grade, grouped by area
/maths/{grade}/{slug}       ← Individual concept page
/science                    ← Science hub (382 concepts, 552 links)
/science/{grade}            ← Grade view for science
/science/{grade}/{slug}     ← Individual science concept page
```

**405 static pages pre-rendered** from the knowledge graph — every page is served as static HTML (fast, no DB hit needed).

### What the concept page shows:
```
┌─────────────────────────────────────────────────┐
│  [Algebra]   Quadratic Equations   [Gr. 9, 10]  │
│                                                  │
│  Polynomial equations of degree 2...            │
│                                                  │
│  ◄ Prerequisites                                 │
│    [Linear Equations] [Factorisation]            │
│    [Square Roots]                                │
│                                                  │
│  ═══ Content Placeholder ═══                    │
│  (Generated pages will appear here)             │
│                                                  │
│  ► What this unlocks                             │
│    [Completing the Square] [Quadratic Formula]   │
│    [Complex Roots] [Vieta's Formulas]            │
└─────────────────────────────────────────────────┘
```

### Key feature: Wikipedia-style navigation
A student who doesn't understand "Factorisation" can click it, land on that page, see *its* prerequisites, and keep walking back through the graph until they find a concept they know — then build forward from there.

---

## SLIDE 12 — Summary and What's Next

### What we built:

| Component | Status |
|---|---|
| PDF heading extractor | ✅ Complete |
| Multi-board topic ingestion (v1 & v2) | ✅ Complete |
| Canonical knowledge graph — Maths (324 concepts, 497 edges) | ✅ Complete |
| Canonical knowledge graph — Science (382 concepts, 552 edges) | ✅ Complete |
| Graph-RAG context assembler | ✅ Complete |
| Direct multilingual generation pipeline | ✅ Built, in progress |
| Pipeline v1 content (Grade 9 Maths, 3 chapters, 3 languages) | ✅ Complete (comparison baseline) |
| Web platform — Maths + Science pages | ✅ Live |

### What's remaining:

1. **Run generation at scale** — all 324 maths + 382 science concepts in 4 languages via Sarvam API
2. **Science graph densification** — same manual verification pass as maths
3. **Cross-subject prerequisites** — Vectors (Maths) → Electric Fields (Physics)
4. **Personalized learning paths** — shortest path through the DAG from current knowledge to learning goal

### The big picture:

> We didn't just build an educational website. We built a **structured representation of school curriculum knowledge** — a graph that captures what depends on what, across subjects, across grades, across boards. That graph is the asset. The web platform and content generation are built on top of it.

---

## THANK YOU

**GraphLearn — BTP-1**  
Saksham Chitkara · Swam Singla  
International Institute of Information Technology, Hyderabad  

*Questions?*

---

## APPENDIX — Pipeline Comparison

| | Pipeline v1 | Pipeline v2 |
|---|---|---|
| Unit of content | Chapter section | Concept |
| Navigation | Linear (prev/next section) | Graph (prerequisites + leads-to) |
| Content generation | Llama 3.2 3B, no grounding | Sarvam API, RAG-grounded |
| Multilingual | Translate after English generation | Generate directly in target language |
| Cross-grade links | None | Yes — multi-grade concept tracking |
| Board coverage | NCERT only | NCERT + ICSE + state boards |
| Duplicate handling | Multiple pages for same concept | One canonical page per concept |
| LaTeX preservation | ~92% success via placeholders | Native — model generates LaTeX |
| Prerequisite structure | None | 497 validated edges (maths) |

---

## APPENDIX — Graph Statistics Deep Dive (Maths v4)

```
Grade    Concepts    Entry Points (no prereqs)
──────────────────────────────────────────────
  6         52              8
  7         48              4
  8         55              3
  9         61              2
 10         58              2
 11         74              1
 12         89              1

Area               Concepts
──────────────────────────────────
Number Systems         28
Algebra                52
Geometry               41
Trigonometry           18
Coordinate Geometry    22
Calculus (Diff.)       29
Calculus (Int.)        17
Statistics             14
Probability            10
Mensuration            12
...and 8 more areas
```

---

*This document was generated from the BTP-1 codebase and report.md.*  
*Convert to PowerPoint using any Markdown → PPTX tool (e.g., Marp, Slidev, pandoc).*
