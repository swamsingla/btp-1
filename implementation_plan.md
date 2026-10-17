# Wikipedia-Style Knowledge Graph Pipeline for Multi-Board Indian Education

## Problem & Background

The current pipeline extracts headings linearly from NCERT PDFs (e.g., `1.1 Real Numbers → 1.2 Euclid's Division Lemma → 1.3 ...`), generates content per-section, and translates it. The professor wants a fundamentally different approach:

**Core Mission**: Quality educational content is not available in regional Indian languages. A student studying a topic in Hindi or Odia from our platform should gain **the same depth of understanding** as someone who studies it in English from any source (textbook, coaching, etc.). We are not tied to any particular board — NCERT, ICSE, state boards are all just **reference inputs**. The output must be **complete, self-sufficient knowledge**.

1. **Not a flat list** — instead a **knowledge graph** like Khan Academy, where each concept is a node with prerequisite edges
2. **Not board-specific** — topics should cover the **union** of all Indian curricula; the LLM knows what topics exist across boards
3. **Not section-numbered pages** — instead **true Wikipedia-style pages** per concept (e.g., "Newton's First Law" is its own page, not "Chapter 5, Section 5.1")
4. **No translation** — prefer direct generation in target languages. Use LLaMA-8B for ALL intermediate generation tasks (topic discovery, canonicalization, summarization, plan-building) AND for final English page generation. Reserve Sarvam-30B **only** for the final multilingual page generation step (Stage 4) where highest multilingual fluency is required.
5. **Same topic, different depth per grade** — "Newton's Third Law" has separate grade-appropriate pages for Grade 8 vs Grade 11
6. **Model usage**: LLaMA-8B handles everything (Stages 1–3 and English generation). Sarvam-30B is used **only** in Stage 4 for generating pages in Hindi, Telugu, Odia and other Indian languages.

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────────┐
│                    STAGE 1: MULTI-SOURCE INGESTION              │
│  NCERT PDFs + ICSE syllabi + State Board syllabi (web/PDFs)     │
│  → Extract raw topic lists per grade/subject/board              │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│              STAGE 2: CANONICAL TOPIC GRAPH (LLM-ASSISTED)      │
│  Deduplicate + merge topics across boards                       │
│  → Create canonical concept nodes                               │
│  → Build prerequisite edges (directed acyclic graph)            │
│  → Tag concepts with grade levels + boards                      │
│  Output: knowledge_graph.json                                   │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│           STAGE 3: CONTENT PLANNING (PER PAGE)                  │
│  For each (concept × grade) pair:                               │
│  → Gather relevant source chunks from all boards                │
│  → Build a focused context summary (fits in token window)       │
│  → Decide page depth/structure based on importance              │
│  Output: page_plans.json                                        │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│         STAGE 4: CONTENT GENERATION (SARVAM MODELS)             │
│  For each page plan:                                            │
│  → Generate Wikipedia-style page in target language             │
│  → Cross-link to prerequisite/successor pages via wikilinks     │
│  → Generate in English + directly in Hindi/Odia/etc.            │
│  Output: generated_pages/{lang}/{concept_slug}_{grade}.md       │
└──────────────────────────┬──────────────────────────────────────┘
                           ▼
┌─────────────────────────────────────────────────────────────────┐
│            STAGE 5: ASSEMBLY & DATABASE UPLOAD                  │
│  → Build final page JSON with metadata + cross-references       │
│  → Upload to DB with graph edges for navigation                 │
│  → Update webapp to support graph-based browsing                │
└─────────────────────────────────────────────────────────────────┘
```

---

## Decisions (Confirmed)

- **Languages**: English + **Hindi** + **Telugu** + **Odia** (via direct Sarvam-30B generation, not translation)
- **Sources**: Source-agnostic. NCERT PDFs = grounding references. LLM + online content = primary sources. Not limited to any board.
- **Priority**: The **knowledge graph** is the most critical piece. Getting every hierarchy level right matters most. Generation is straightforward Sarvam API usage after the graph is solid.

> [!NOTE]
> **Content sourcing**: For each concept, we pull relevant content from **any online source** (Wikipedia, NCERT textbooks, Khan Academy, Byju's articles, open educational resources). This grounds the LLM generation with real reference material. NCERT chunks we already have are one signal, but not the only one.

---

## Proposed Changes

### Stage 1: Multi-Source Topic Ingestion

#### [MODIFY] [extract_headings.py](file:///home/swamsingla/btp-1/scripts/extract_headings.py)
- Keep as-is — still used to extract headings from NCERT PDFs as grounding references
- Its output feeds into the graph builder as one reference signal

#### [NEW] [topic_ingestion.py](file:///home/swamsingla/btp-1/scripts/topic_ingestion.py)

**Purpose**: Discover the **complete set of topics** a student should learn at each grade+subject — not limited to any board.

**Two-pronged approach:**

1. **NCERT reference extraction** (existing [extract_headings.py](file:///home/swamsingla/btp-1/scripts/extract_headings.py)):
   - Provides grounded topic names from actual textbooks we have
   - Already works for grades 6–12, maths + science

2. **LLM-powered comprehensive topic discovery** (the primary source):
   - For each grade+subject, prompt **LLaMA-8B** (local):
     *"List ALL important topics and concepts that an Indian student in Grade {X} should learn in {Subject}. Cover topics from NCERT, ICSE, all major state boards, and any universally important concepts. The goal is completeness — a student who masters all these topics should have world-class understanding at this grade level."*
   - Cross-reference with NCERT headings to ensure nothing is missed
   - The LLM output is the primary topic source; NCERT headings are validation

**Output**: `data/intermediate/raw_topics/{grade}_{subject}.json`
```json
{
  "grade": 10,
  "subject": "science",
  "topics": [
    {
      "raw_name": "Chemical Reactions and Equations",
      "ncert_refs": ["chapter1"],
      "subtopics": ["Combination Reactions", "Decomposition Reactions", ...]
    },
    {
      "raw_name": "Analytical Chemistry Basics",
      "ncert_refs": [],
      "subtopics": ["Qualitative Analysis", "Flame Tests", ...],
      "note": "Covered in ICSE/state boards, not in NCERT"
    }
  ]
}
```

---

### Stage 2: Knowledge Graph Construction

#### [NEW] [graph_builder.py](file:///home/swamsingla/btp-1/scripts/graph_builder.py)

**This is the most critical part of the entire pipeline.** Converts raw topic lists into a deep, multi-level knowledge graph.

**Step 2a: Canonical Concept Extraction with Full Hierarchy**

Use **LLaMA-8B** (local) to process the merged topic lists and identify **canonical concepts** at EVERY hierarchy level — the actual knowledge atoms that should become Wikipedia pages.

**Key insight: How to decide what gets its own page?**

Real Wikipedia has pages at multiple granularity levels, and so should we. The hierarchy is:

```
Subject (e.g., Physics)
 └── Domain (e.g., Mechanics)
     └── Area (e.g., Newton's Laws of Motion)        ← gets a PAGE (overview)
         └── Concept (e.g., Newton's First Law)       ← gets a PAGE (detailed)
             └── Sub-concept (e.g., Inertia)          ← gets a PAGE (focused)
                 └── Application (e.g., Seatbelts)    ← may get a PAGE or section
```

Every level that represents a **distinct, searchable knowledge unit** gets its own page:
- **Area pages**: "Newton's Laws of Motion" — overview, links to all three laws
- **Concept pages**: "Newton's First Law" — full explanation, examples, math
- **Sub-concept pages**: "Inertia" — deep dive into one aspect
- **NOT micro-level**: "Step 3 of solving force problems" — too fine, belongs as section within a page

**LLM Prompt for hierarchical concept extraction:**
```
For Grade {X} {Subject}, create a complete hierarchical knowledge map.

Rules:
1. Organize ALL topics into a tree: Domain > Area > Concept > Sub-concept
2. Each node should be a self-contained, searchable knowledge unit
3. Use proper names (like Wikipedia titles): "Newton's First Law of Motion", not "1.1 First Law"
4. Include topics from ALL Indian boards (NCERT, ICSE, state boards) — not just one
5. Every node that a student might search for should exist
6. A concept like "Chemical Bonding" should have sub-concepts like "Ionic Bonding", "Covalent Bonding", "Metallic Bonding" as separate child nodes

Output as nested JSON:
{
  "domain": "Mechanics",
  "areas": [
    {
      "name": "Newton's Laws of Motion",
      "concepts": [
        {
          "name": "Newton's First Law of Motion",
          "aliases": ["Law of Inertia"],
          "sub_concepts": ["Inertia", "Balanced and Unbalanced Forces"],
          "grades": [8, 9, 11]
        }
      ]
    }
  ]
}
```

**Step 2b: Prerequisite Edge Construction**

For each subject+grade cluster, prompt **LLaMA-8B** (local):
```
Here are the canonical concepts for {Subject} relevant to Grade {X}:
{concept_list}

For each concept, list:
1. DIRECT prerequisites (must understand BEFORE this one)
2. Related concepts (useful to read alongside)
3. "See also" concepts (interesting connections)

Output as JSON: {"concept": "...", "prerequisites": [...], "related": [...], "see_also": [...]}
```

**Step 2c: Grade-Wise Graph Layering**

The graph is structured in layers:
- **Global concept graph**: All concepts across all grades, with prerequisite edges
- **Grade views**: For each grade, a subgraph containing only the concepts relevant to that grade
- **Cross-grade links**: "See also: Advanced treatment in Grade 11" / "Review basics from Grade 8"

**Output**: `data/knowledge_graph/graph.json`
```json
{
  "concepts": {
    "newtons-first-law": {
      "canonical_name": "Newton's First Law of Motion",
      "slug": "newtons-first-law",
      "aliases": ["Law of Inertia"],
      "subject": "physics",
      "category": "Mechanics",
      "grades": [8, 9, 11],
      "prerequisites": ["force-and-motion", "types-of-forces"],
      "leads_to": ["newtons-second-law", "newtons-third-law", "momentum"],
      "related": ["friction", "inertia"],
      "ncert_refs": ["grade9/science/chapter9"],
      "importance_by_grade": {"8": 4, "9": 5, "11": 3}
    }
  },
  "edges": [
    {"from": "force-and-motion", "to": "newtons-first-law", "type": "prerequisite"},
    {"from": "newtons-first-law", "to": "newtons-second-law", "type": "prerequisite"}
  ],
  "grade_views": {
    "8": {"concepts": ["newtons-first-law", "force-and-motion", ...], "entry_points": ["force-and-motion"]},
    "9": {"concepts": [...], "entry_points": [...]},
  }
}
```

---

### Stage 3: Content Planning & Context Assembly

#### [NEW] [content_planner.py](file:///home/swamsingla/btp-1/scripts/content_planner.py)

**The core problem**: For each [(concept, grade)](file:///home/swamsingla/btp-1/scripts/extract_headings.py#407-482) page, we need relevant reference material as context for generation, but we can't dump entire textbooks into the prompt.

**Solution: Multi-step context assembly from all available sources**

1. **Find relevant NCERT chunks** (we already have these parsed):
   - Fuzzy match concept name against chunk topic_titles
   - Also search chunk content text for concept name mentions
   - Pull best-matching chunks from the corresponding chapter/section

2. **Web content retrieval** (NEW — the "any relevant content online" approach):
   - For each concept, search for high-quality reference content:
     - Wikipedia article on the concept
     - Khan Academy / BYJU's / Toppr if publicly accessible
     - Open educational resources (NROER, DIKSHA portal)
   - Scrape/fetch the relevant text
   - This gives us **board-agnostic, comprehensive reference text**
   - Tool: use `requests` + `BeautifulSoup` or a search API

3. **Summarize all references**: Combine NCERT chunks + web content, then:
   - Use **LLaMA-8B** (local): *"Summarize the key content about {concept} for Grade {X}, keeping all formulas and definitions."*
   - Compress to ~3000 chars to fit in generation prompt

4. **Determine page structure from hierarchy level**:
   - **Area page** (e.g., "Newton's Laws of Motion"): Overview page (~800-1000 words)
     - Brief intro to the area, links to all child concepts
   - **Concept page** (e.g., "Newton's First Law"): Full page (~1200-2000 words)
     - Lead section, explanation, mathematical formulation, examples, see also
   - **Sub-concept page** (e.g., "Inertia"): Focused page (~500-1000 words)
     - Deep dive on one aspect, links back to parent

5. **Grade-appropriate depth**: Same concept at different grades:
   - **Grade 8 "Newton's First Law"**: Everyday examples, qualitative, no calculus
   - **Grade 9 "Newton's First Law"**: Semi-quantitative, simple numerical problems
   - **Grade 11 "Newton's First Law"**: Rigorous, inertial frames, mathematical treatment

**Output**: `data/content_plans/` — one JSON per concept-grade pair
```json
{
  "concept_slug": "newtons-first-law",
  "grade": 9,
  "canonical_name": "Newton's First Law of Motion",
  "page_depth": "standard",
  "target_words": 1000,
  "context_summary": "... (compressed source material) ...",
  "prerequisites_to_link": ["force-and-motion"],
  "successors_to_link": ["newtons-second-law"],
  "related_to_link": ["inertia", "friction"],
  "sections": ["Lead", "Explanation", "Examples", "Practice", "See Also"],
  "grade_note": "Semi-quantitative treatment. Use simple numerical examples. No calculus."
}
```

---

### Stage 4: Content Generation via Sarvam

#### [NEW] [generate_pages.py](file:///home/swamsingla/btp-1/scripts/generate_pages.py)

**Uses LLaMA-8B (local) for English pages, and Sarvam-30B API for multilingual pages** (Hindi, Telugu, Odia, etc.).

**Generation prompt design:**

```
You are writing a Wikipedia-style educational article for Indian Grade {grade} students.

ARTICLE: {canonical_name}
SUBJECT: {subject}
GRADE LEVEL: {grade} ({grade_note})

PREREQUISITES (the student has already studied these — you can reference them):
{prerequisites_list}

RELATED CONCEPTS (link to these with [[wikilinks]]):
{related_list}

SOURCE MATERIAL (textbook excerpts for accuracy):
---
{context_summary}
---

Write a complete, self-contained Wikipedia-style article. Follow these rules:
1. Start with a lead paragraph that defines the concept clearly
2. Use ## headers for main sections, ### for subsections
3. Link to related concepts using [[Concept Name]] notation
4. Use LaTeX for math: $inline$ and $$display$$
5. Include at least 2 real-world examples
6. Write at a {grade_note} level — adjust vocabulary and complexity accordingly
7. Include a "See Also" section at the end linking to prerequisites and related concepts
8. DO NOT number sections as "1.1", "1.2" — use descriptive headers like Wikipedia
9. The article should be self-contained — a student should be able to understand it
   without needing to read the source textbook

Target length: ~{target_words} words
Language: {language}
```

**For multilingual generation** (the key change — no translation):
- For each page, call **LLaMA-8B locally for English** generation first
- Then call **Sarvam-30B API** separately for each target Indian language (Hindi, Telugu, Odia, etc.)
- Sarvam-30B is used **exclusively for multilingual output** — not for any intermediate steps

**API integration:**
```python
# --- English generation: LLaMA-8B (local) ---
from llm_local import generate_text

english_page = generate_text(prompt=generation_prompt, max_new_tokens=2500)

# --- Multilingual generation: Sarvam-30B API ---
import openai

client = openai.OpenAI(
    base_url="https://api.sarvam.ai/v1",
    api_key=os.environ["SARVAM_API_KEY"]
)

response = client.chat.completions.create(
    model="sarvam-30b",   # only for non-English languages
    messages=[
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": generation_prompt}
    ],
    temperature=0.7,
    max_tokens=4096
)
```

**Output**: `data/generated_pages/{language}/{concept_slug}_grade{N}.md`

---

### Stage 5: Page Assembly & Database

#### [MODIFY] [db_uploader.py](file:///home/swamsingla/btp-1/scripts/db_uploader.py)

Update the database schema to support:
```sql
-- Canonical concepts (the nodes)
CREATE TABLE concepts (
    id SERIAL PRIMARY KEY,
    slug VARCHAR(200) UNIQUE NOT NULL,
    canonical_name VARCHAR(500) NOT NULL,
    subject VARCHAR(100) NOT NULL,
    category VARCHAR(200),
    aliases TEXT[],  -- array of alternative names
    source_boards TEXT[]
);

-- Grade-specific pages (the actual content)
CREATE TABLE pages (
    id SERIAL PRIMARY KEY,
    concept_id INTEGER REFERENCES concepts(id),
    grade INTEGER NOT NULL,
    language VARCHAR(10) NOT NULL,  -- 'en', 'hi', 'or', etc.
    title VARCHAR(500) NOT NULL,
    content TEXT NOT NULL,
    importance INTEGER DEFAULT 3,
    target_words INTEGER,
    created_at TIMESTAMP DEFAULT NOW(),
    UNIQUE(concept_id, grade, language)
);

-- Knowledge graph edges
CREATE TABLE concept_edges (
    id SERIAL PRIMARY KEY,
    from_concept_id INTEGER REFERENCES concepts(id),
    to_concept_id INTEGER REFERENCES concepts(id),
    edge_type VARCHAR(50) NOT NULL,  -- 'prerequisite', 'related', 'see_also'
    UNIQUE(from_concept_id, to_concept_id, edge_type)
);

-- Grade views (which concepts appear in which grade)
CREATE TABLE grade_views (
    id SERIAL PRIMARY KEY,
    grade INTEGER NOT NULL,
    subject VARCHAR(100) NOT NULL,
    concept_id INTEGER REFERENCES concepts(id),
    is_entry_point BOOLEAN DEFAULT FALSE,
    display_order INTEGER,
    UNIQUE(grade, subject, concept_id)
);
```

---

### Webapp Updates

#### [MODIFY] Webapp navigation

The current webapp shows linear chapter/section lists. Update to:

1. **Graph view**: Interactive DAG visualization per grade/subject
   - Use a library like `react-force-graph` or `d3-force` 
   - Nodes = concepts, edges = prerequisites
   - Color-code by category (Mechanics=blue, Optics=green, etc.)
   - Click node → navigate to concept page

2. **Concept page**: Wikipedia-style article page
   - Breadcrumb: `Grade 9 > Physics > Mechanics > Newton's First Law`
   - Content from the generated markdown
   - Sidebar: Prerequisites, Related concepts, "See in other grades"
   - Language switcher (generated, not translated)

3. **Browse by grade**: Grid/list of all concepts for a grade+subject
   - Shows prerequisite path
   - Mastery indicators (future feature)

---

## Detailed Script Specifications

### `topic_ingestion.py` — What it does precisely

```python
# Input:
#   data/input/grade{N}/{subject}/*.pdf        (NCERT PDFs - existing)
#   data/input/syllabi/{board}/grade{N}.json   (curated syllabus files - new)
#
# Output:
#   data/intermediate/raw_topics/grade{N}_{subject}.json

# Algorithm:
# 1. For each grade+subject:
#    a. Extract headings from NCERT PDFs (reuse extract_headings.py logic)
#    b. Load any curated syllabus files for ICSE/state boards
#    c. Call LLaMA-8B (local) to discover additional topics across boards
#    d. Merge all into a unified raw topic list with source attribution
```

### `graph_builder.py` — The core intelligence

```python
# Input:
#   data/intermediate/raw_topics/grade{N}_{subject}.json (all grades+subjects)
#
# Output:
#   data/knowledge_graph/graph.json
#   data/knowledge_graph/graph_by_subject/{subject}.json
#   data/knowledge_graph/graph_by_grade/grade{N}_{subject}.json

# Algorithm:
# 1. Load all raw topics across all grades and boards
# 2. For each subject (maths, physics, chemistry, biology):
#    a. Batch all raw topics for this subject
#    b. Prompt LLaMA-8B (local) in batches of ~20 topics:
#       "Here are topics from multiple boards. Extract canonical concepts."
#    c. Deduplicate the extracted concepts (fuzzy match on names)
#    d. For each grade, prompt LLaMA-8B (local):
#       "What are the prerequisite relationships between these concepts?"
#    e. Build DAG, validate no cycles (topological sort check)
#    f. Identify entry points per grade (concepts with no prerequisites in that grade)
#    g. Compute importance scores per concept per grade
# 3. Save complete graph
```

### `content_planner.py` — Context assembly

```python
# Input:
#   data/knowledge_graph/graph.json
#   data/intermediate/chunks/  (existing NCERT chunks from chunker.py)
#
# Output:
#   data/content_plans/{concept_slug}_grade{N}.json

# Algorithm:
# For each (concept, grade) in the graph:
# 1. Find matching NCERT chunks:
#    - Fuzzy match concept name against chunk topic_titles
#    - Also search chunk content for concept name mentions
#    - Take top 3-5 matching chunks
# 2. If total matched content > 3000 chars:
#    - Summarize using LLaMA-8B (local): "Summarize about {concept} from this text"
# 3. Determine page structure based on importance score
# 4. List cross-reference links (prerequisites, related, next-grade)
# 5. Write page plan JSON
```

### `generate_pages.py` — Sarvam-powered generation

```python
# Input:
#   data/content_plans/{concept_slug}_grade{N}.json
#
# Output:
#   data/generated_pages/{lang}/{concept_slug}_grade{N}.md
#   data/generated_pages/_index.json

# Algorithm:
# For each page plan:
# 1. Build the Wikipedia-style generation prompt
# 2. Call LLaMA-8B (local) → generate English page
# 3. For each non-English target language:
#    a. Call Sarvam-30B API (OpenAI-compatible) — ONLY for multilingual output
#    b. Post-process: fix LaTeX, add wikilinks, clean formatting
#    c. Save markdown file
# 4. Update index with metadata
#
# Rate limiting: Sarvam free tier may have rate limits (multilingual calls only)
# → Implement exponential backoff + resume support (skip existing files)
```

---

## How the same topic works across grades (the key question)

**Example: "Newton's Third Law of Motion"**

| Grade | Depth | What to write | Context source |
|-------|-------|---------------|----------------|
| 8 | Introductory | Everyday examples (swimming, walking, rocket). Qualitative only. "For every action there is an equal and opposite reaction." Simple activities. | NCERT Grade 8 chunks + LLM knowledge |
| 9 | Standard | Formal statement, action-reaction pairs, distinguish from balanced forces. Simple F=ma context. Numerical problems. | NCERT Grade 9 chunks + LLM knowledge |
| 11 | Advanced | Mathematical treatment, Newton's notation, momentum conservation, internal/external forces, collision analysis, center of mass frame. | NCERT Grade 11 chunks + LLM knowledge |

**Quality target**: A student reading our Grade 9 page in Hindi should understand Newton's Third Law just as well as a student who studied it from Resnick-Halliday or HC Verma in English.

The **content_planner** determines this by:
1. Looking at the `importance_by_grade` from the graph
2. Selecting grade-matched source chunks from different textbooks
3. Setting `grade_note` in the plan that tells the generator the appropriate depth

---

## How to get content when there's no direct parsed source

**Problem**: We're not using section-wise content anymore. How do we know what to write for "Exothermic Reactions" at Grade 10 if we don't have that exact section parsed? And how do we ensure the content is as good as the best English textbooks?

**Solution (3-pronged approach):**

1. **Fuzzy chunk matching**: The existing NCERT chunks from [chunker.py](file:///home/swamsingla/btp-1/scripts/chunker.py) contain actual textbook text. Search through ALL chunks for content relevant to each concept:
   - Match by topic title similarity (e.g., "Exothermic Reactions" ≈ "1.2 Types of Chemical Reactions")
   - Match by content text search (grep for "exothermic" in all Grade 10 science chunks)
   - This gives us grounded textbook content as context

2. **Cross-board aggregation**: If ICSE syllabus for Grade 10 also lists "Exothermic and Endothermic Reactions", note this — it tells the generator this is an important topic across boards

3. **LLM knowledge as primary content engine**: The LLM is not a "fallback" — it is the primary content author. The textbook chunks are **grounding references** to ensure accuracy and curriculum alignment, but the LLM should produce content that matches or exceeds textbook quality. The prompt says:
   *"Write as if you are the best teacher in India explaining this concept. A student reading this in {language} should understand the topic as well as someone who studied from the best English textbooks."*
   
   **English pages use LLaMA-8B (local)**. For Indian language pages, Sarvam-30B takes the English page as reference and generates natively in the target language (it supports 22 Indian languages).

---

## Verification Plan

### Automated Tests

1. **Graph integrity test** — run after Stage 2:
   ```bash
   python scripts/graph_builder.py --validate
   ```
   - Check: No cycles in prerequisite DAG (topological sort succeeds)
   - Check: Every concept has at least one grade
   - Check: No orphan nodes (concepts with no edges at all)
   - Check: Entry points exist for each grade

2. **Content plan coverage test** — run after Stage 3:
   ```bash
   python scripts/content_planner.py --check-coverage
   ```
   - Check: Every (concept, grade) pair in the graph has a content plan
   - Check: Every plan has non-empty context or explicit "no-source" flag
   - Check: All cross-reference slugs resolve to real concepts

3. **Page generation smoke test** — run after Stage 4:
   ```bash
   python scripts/generate_pages.py --test --concept newtons-first-law --grade 9
   ```
   - Check: Generated page has required sections (Lead, Explanation, See Also)
   - Check: Wikilinks `[[...]]` resolve to known concept slugs
   - Check: LaTeX is properly formatted

### Manual Verification

1. **Graph visual inspection**: After Stage 2, open the generated graph JSON and verify ~ 5-10 concepts manually:
   - Does "Quadratic Formula" correctly list "Quadratic Equations" as prerequisite?
   - Are grade assignments sensible?

2. **Content quality check**: After Stage 4, read 3-4 generated pages and verify:
   - Grade-appropriate language and depth
   - Mathematical accuracy
   - No hallucinated concepts outside curriculum
   - Cross-links make sense

3. **Multilingual quality**: Compare English and Hindi versions of the same concept page — are they both high quality, not just translated?

---

## Implementation Order

1. **`topic_ingestion.py`** — Start here, build on existing [extract_headings.py](file:///home/swamsingla/btp-1/scripts/extract_headings.py)
2. **`graph_builder.py`** — The most important and novel script
3. **`content_planner.py`** — Bridges graph to generation
4. **`generate_pages.py`** — Sarvam API integration
5. **DB schema update + [db_uploader.py](file:///home/swamsingla/btp-1/scripts/db_uploader.py)** — Updated upload
6. **Webapp graph navigation** — Frontend changes

Each stage is independently testable and produces intermediate files that can be inspected.

---

## Dependencies

```
# New Python packages needed
pip install openai          # For Sarvam API (OpenAI-compatible)
pip install networkx        # For DAG operations (cycle detection, topological sort)
pip install thefuzz         # For fuzzy string matching (topic deduplication)
```

## Environment Variables

```env
SARVAM_API_KEY=your_sarvam_api_key   # Get from sarvam.ai dashboard
```
