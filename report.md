# GraphLearn: A Knowledge-Graph-Driven Multilingual Educational Platform for Indian School Mathematics and Science

**Authors:** Saksham Chitkara · Swam Singla  
**Institution:** International Institute of Information Technology, Hyderabad  
**Project Type:** B.Tech Thesis Project (BTP-1)  

---

## Abstract

Building a good educational platform for Indian school students is harder than it looks. The obvious approach — take a textbook, extract each section, generate explanation pages for every section, and then translate those pages into regional languages — runs into serious problems very quickly. Content quality is inconsistent from section to section, mathematical notation breaks during translation, and the result feels like a digitised textbook rather than an interactive learning tool.

This report documents our complete journey: we first built this straightforward pipeline (Pipeline v1), ran it over NCERT mathematics textbooks for Grades 6–12, identified exactly where and why it fails, and then redesigned the system from the ground up around a **knowledge graph** (Pipeline v2). Instead of treating content as a collection of chapters and sections, we model it as a network of mathematical concepts connected by prerequisite relationships. We built a manually curated graph for mathematics covering 324 concepts, 497 directed prerequisite edges, 18 topic areas, and all seven grades (6 through 12). A new web interface lets students navigate this graph — clicking from "Quadratic Equations" to its prerequisites like "Factorisation" and "Linear Equations" the same way one would follow Wikipedia links. The remaining open pieces — reference-grounded content generation via Retrieval-Augmented Generation (RAG) and direct multilingual generation in Hindi, Telugu, and Odia using the Sarvam AI model family — are designed and partially integrated, with generation and science graph construction completing the system.

---

## 1. Introduction

### 1.1 The Problem We Are Trying to Solve

India has over 250 million school students, most of whom study in their regional languages — Hindi, Telugu, Tamil, Odia, and dozens more. Yet virtually all high-quality digital educational content is available only in English. Platforms like Khan Academy have excellent material but almost none of it is reliably available in Indic languages. NCERT's own ePathshala digitised the textbooks, but that just puts the same flat PDF content online — there is no interactivity, no navigation between related concepts, and no explanation beyond what the textbook already says.

The core challenge is this: producing curriculum-aligned, mathematically accurate educational content in multiple Indic languages at scale is expensive and slow if done by human teachers alone. Large Language Models (LLMs) and neural machine translation systems have reached a level where they can plausibly help, but the naive approach of "prompt an LLM with a textbook section and translate the result" produces inconsistent, sometimes wrong content that nobody would trust for a high-stakes subject like mathematics.

### 1.2 Our Goal

We set out to build a platform that does the following:

1. Ingests school mathematics and science curricula from multiple Indian boards (NCERT, ICSE, and various state boards), not just one.
2. Organises all that curriculum into a **knowledge graph** where each node is a distinct concept and edges represent prerequisite relationships.
3. Generates high-quality explanation content for each concept, grounded in the actual reference textbooks using RAG.
4. Serves this content in English, Hindi, Telugu, and Odia through a web interface that lets students navigate between related concepts.

### 1.3 Why This Matters

The distinction between a "chapter-based" system and a "concept-based" system matters enormously for learning. In any textbook, the same idea appears and reappears across multiple chapters. "Fractions" first appear in Grade 6, come back in Grade 7 with ratios and percentages, return in Grade 8 with rational numbers, and underpin everything in Grade 9 onwards. A chapter-based system generates four separate, potentially contradictory pages for the same underlying idea. A concept-based system has one canonical page for "Fractions" that notes how it deepens across grades, and points forward to all the concepts it enables.

---

## 2. Related Work

### 2.1 Existing Educational Platforms

**Khan Academy** is the closest reference point for what we are building. It has a well-structured knowledge map for mathematics with prerequisites and mastery tracking. However, its content is almost entirely in English, its Indic language coverage is very limited and often machine-translated without mathematical accuracy checks, and it is not curriculum-aligned with Indian boards.

**NCERT ePathshala and DIKSHA** digitise the textbooks and offer some video content, but the underlying structure is strictly chapter-based. There is no cross-concept navigation, no prerequisite map, and no multilingual content beyond what was originally written in a given language.

**Embibe and Toppr** are commercial platforms with some knowledge-graph-like features, but they are proprietary, expensive, and built manually by large teams of content editors. Their Indic language support is limited to Hindi for the most part.

**Google Translate and DeepL** can translate text, but they are not designed for mathematical content. Mathematical notation (LaTeX expressions) either passes through unchanged or gets corrupted, and domain-specific terminology — like the Hindi term for "derivative" or the Telugu term for "hypotenuse" — is often wrong because these models optimise for general-domain text.

### 2.2 Knowledge Graphs in Education

Knowledge graphs for education have been an active research area for over a decade. Early systems like prerequisite chains in Coursera's courses showed that structuring content as a DAG (directed acyclic graph) improves learning outcomes by helping students understand what they need to learn before attempting something new. Recent work from groups at Stanford and CMU has applied knowledge tracing models (BKT, DKT) on top of concept graphs to personalise learning paths. Our work is in the same spirit but focused on the specific challenge of Indic language content at the school level.

### 2.3 LLMs for Educational Content

Recent work has shown that large language models (GPT-4, LLaMA, Mistral) can generate plausible educational content for many subjects. However, mathematics is harder than most — small models hallucinate formulas, get proofs wrong, and sometimes confidently state incorrect numerical answers. This has been documented extensively, and our own experiments with Llama 3.2 3B confirm it. The general consensus is that LLM-generated math content needs to be grounded in verified reference material (RAG) rather than generated purely from the model's parametric memory.

### 2.4 Multilingual NLP for Indic Languages

The IndicTrans2 model family from AI4Bharat is currently the state-of-the-art for English-to-Indic translation. It supports 22 Indic languages and significantly outperforms generic translation models for Hindi, Telugu, Tamil, and Odia. However, it is not specifically trained on mathematical text, which means mathematical terminology still suffers. The Sarvam AI models (including sarvam-translate and the Sarvam-30B generation model) are newer systems trained with a stronger focus on Indian educational context and are the basis for our Stage 4 generation pipeline.

---

## 3. Problem Statement

We define the problem formally as follows.

Let $C$ be a set of canonical educational concepts drawn from school mathematics and science curricula for Grades 6–12 across Indian boards. Let $G = (C, E)$ be a directed graph where an edge $(c_i, c_j) \in E$ means that understanding $c_i$ is a prerequisite for understanding $c_j$. Let $L = \{en, hi, te, od\}$ be the set of target languages.

The goal is to build a system that:

1. **Constructs** $G$ from raw curriculum sources (PDF textbooks, board syllabi) with manual expert validation.
2. **Generates** for each concept $c \in C$ and each language $\ell \in L$, a high-quality explanation page $P(c, \ell)$ that is (a) accurate, (b) grade-appropriate, (c) consistent with the explanations of $c$'s prerequisites, and (d) grounded in verified reference chunks from the source textbooks.
3. **Serves** this content through a web interface that exposes the graph structure — letting a student viewing $P(c, \ell)$ navigate to the prerequisites of $c$ and to the concepts that $c$ enables.

The hard constraints are:
- All local LLM inference must run on a single consumer GPU (RTX 3050, 4 GB VRAM).
- The system must support multi-board curricula (NCERT, ICSE, state boards), not just one.
- Mathematical notation (LaTeX) must be preserved without corruption throughout the pipeline.
- The content must feel like it was written for that grade level — not too formal, not too simplified.

---

## 4. System Architecture Overview

The full system consists of two major components: the **content pipeline** (offline processing) and the **web platform** (online serving). Figure 1 shows the high-level flow.

```
Raw PDFs (NCERT + ICSE + State Boards)
        │
        ▼
  [Stage 1] Heading & Topic Extraction
        │
        ▼
  [Stage 2] Canonical Concept Graph (LLM-assisted + Manual)
        │
        ▼
  [Stage 3] RAG Context Assembly (upcoming)
        │
        ▼
  [Stage 4] Multilingual Content Generation via Sarvam (upcoming)
        │
        ▼
  [Stage 5] MongoDB Atlas ──► Express.js API ──► Next.js Webapp
```

The pipeline went through two major versions. Pipeline v1 was a simpler, linear system that treated content as chapters and sections. Pipeline v2 is the graph-based system described above. The next sections explain both in detail.

---

## 5. Pipeline v1: The Linear Approach

When we started this project, the most natural thing to do was follow the structure of the textbook itself. NCERT books are organised into chapters, each chapter into numbered sections (like 1.1, 1.2, 1.3), and each section into content. So we built a pipeline that mirrors this structure: extract sections from each chapter, generate an explanation page for each section, translate each page into the target languages, and upload everything to a database. This felt like a reasonable starting point and it got working results quickly — but when we actually looked at what it produced in detail, a lot of problems became clear.

### 5.1 Stage 1: PDF Parsing and Heading Extraction

The first step was extracting the chapter-section structure from NCERT PDF textbooks. We wrote a heading extraction script that uses `pdfplumber` to read each chapter PDF, identify headings by their font size and formatting, and produce a structured JSON file with the topic hierarchy.

The output for, say, Grade 9 Mathematics Chapter 1 looks like this:

```json
{
  "chapter_number": 1,
  "chapter_title": "NUMBER SYSTEMS",
  "topics": [
    { "number": "1.1", "title": "Introduction", "page": 1 },
    { "number": "1.2", "title": "Irrational Numbers", "page": 5 },
    { "number": "1.3", "title": "Real Numbers and their Decimal Expansions", "page": 8 },
    { "number": "1.4", "title": "Operations on Real Numbers", "page": 15 },
    { "number": "1.5", "title": "Laws of Exponents for Real Numbers", "page": 21 }
  ]
}
```

These heading JSONs were stored in `data/intermediate/headings/grade{N}/{subject}/chapter{N}.json` for all grades and subjects. The extracted PDF text for each section was stored as chunks in `data/intermediate/chunks/`.

We covered all NCERT mathematics textbooks from Grade 6 to Grade 12, and science textbooks from Grade 6 to Grade 9 in this first pass.

### 5.2 Stage 2: LLM Content Generation

For each topic extracted in Stage 1, we generated a detailed explanation page using a locally running LLM. Given the hardware constraint (RTX 3050, 4 GB VRAM), we needed a model small enough to fit in memory while still being capable enough to write coherent educational content.

We used **Llama 3.2 3B Instruct**, quantised to 4-bit precision using NF4 quantisation via BitsAndBytes. This allowed the model to run in roughly 2.5 GB of VRAM, leaving some headroom for inference.

**Content Generation Script (`scripts/content_gen.py`):**

The script does more than just call the LLM with a topic name. It first runs an **importance scoring pass**: for each topic, it asks the model to rate how important this topic is on a scale of 1 to 5 for the given grade. This score is then used to decide how much content to generate — less important sections get briefer coverage, highly important concepts (like Irrational Numbers or the Quadratic Formula) get the full treatment.

The content structure for each topic is:
1. **Prerequisites** — what the student should know before reading this
2. **Introduction** — a hook or motivating question
3. **Explanation** — the actual content with sub-sections
4. **Solved Examples** — worked problems
5. **Common Mistakes** — typical errors students make
6. **Practice Tips**
7. **Summary**

The model was given **grade-aware system prompts** that calibrated the tone and complexity. The prompt for Grade 6 topics explicitly asks for "friendly, simple language with lots of concrete examples." Grade 10 prompts ask for "balanced explanations with full worked examples and some mathematical rigour." Grade 12 prompts ask for "rigorous treatment suitable for students preparing for JEE-level mathematics."

Mathematical notation was expressed using KaTeX-compatible LaTeX: inline expressions wrapped in `$...$` and display equations in `$$...$$`.

Here is a sample of the generated output for the topic "Irrational Numbers" in Grade 9:

> "An irrational number is a number that cannot be expressed in the form $\frac{p}{q}$, where $p$ and $q$ are integers and $q \neq 0$. [...] Assume $\sqrt{2} = \frac{p}{q}$, where $p$ and $q$ are coprime integers. Squaring both sides: $2 = \frac{p^2}{q^2} \implies p^2 = 2q^2$. This implies $p^2$ is even, so $p$ must be even..."

The output quality was decent for well-known topics. The model clearly had training data covering standard NCERT-level mathematics.

### 5.3 Stage 3: Translation Pipeline

Once we had English content pages, the next step was translating them into Hindi, Telugu, and Odia. We built a translation pipeline in `scripts/translator.py` and tested three different model families:

**Model 1: IndicTrans2 (`ai4bharat/indictrans2-en-indic-1B`)**  
This is the current best-in-class model for English-to-Indic translation. It supports 22 Indic languages and was trained specifically on Indian-language corpora. We used the 1B-parameter version which runs in about 2 GB of memory in float16 precision.

One critical technical note: IndicTrans2 has a dependency on the `IndicTransTokenizer` which does not work with transformers library versions above 4.45. Our system used transformers 5.x for Llama, which meant we had to manage two separate virtual environments — one for generation (transformers 5.x) and one for IndicTrans2 translation (transformers ≤4.45). Running IndicTrans2 on transformers 5.x produces completely garbled output with no error message, which took us a while to diagnose.

**Model 2: Sarvam Translate (`sarvamai/sarvam-translate`)**  
Sarvam's translation model is Gemma3-based and supports Indian languages with a focus on educational content. We ran it in 4-bit quantisation (~2.5 GB VRAM). Quality for Hindi was competitive with IndicTrans2; for Odia it was somewhat weaker.

**Model 3: TranslateGemma (`google/translategemma-4b-it`)**  
Google's translation-specific Gemma 4B model. Similar VRAM footprint (~2.5 GB in 4-bit). For mathematical text it performed roughly on par with sarvam-translate.

**The LaTeX Preservation Problem:**  
The biggest technical challenge in translation was preserving mathematical expressions. Neural translation models tend to translate everything they see, including LaTeX notation — sometimes partially, sometimes completely mangling it. A formula like $\frac{p}{q}$ might come out of a translation model as something with the `\frac` partially translated or the braces corrupted.

Our solution was to split the content at LaTeX boundaries before sending it to the translation model. Any segment matching `$...$` or `$$...$$` was extracted, replaced with a placeholder token in the text, the surrounding text was translated, and then the LaTeX was put back in. This preserved notation in most cases, but the boundaries were not always clean — LaTeX embedded mid-sentence sometimes caused the sentence to be translated awkwardly around the placeholder.

We also extracted domain-specific terms (like "rational number", "square root", "hypotenuse") that should either be left in English or translated using standard Indian educational terminology. These were stored in per-chapter term conservation files in `data/intermediate/`.

**Translation output** was stored in `data/intermediate/translations_dump/` as HTML files (e.g., `ch1_t1_hi.html` for Chapter 1 Topic 1 in Hindi). We generated translations for all Grade 9 Mathematics chapters as a proof-of-concept.

### 5.4 Stage 4: Database Upload and Web Interface

The generated and translated content was uploaded to **MongoDB Atlas** using `scripts/db_uploader.py`. The database schema had two main collections:

- **chapters**: metadata about each chapter (grade, subject, chapter number, title)
- **topics**: content documents, each representing one section/topic, with the English text and translated variants embedded as fields

The Next.js frontend served this content at URLs structured as:
`/grade/{gradeId}/{subject}/chapter/{chapterId}/topic/{topicId}`

So for Grade 9 Maths Chapter 1 Section 1.2, the URL would be `/grade/9/maths/chapter/1/topic/2`.

### 5.5 What Went Wrong: Failure Analysis

After building and running Pipeline v1 end-to-end, we did a thorough review of the output and identified several fundamental problems — some technical, some structural.

**Problem 1: Content tied to chapter numbers, not concepts.**  
The URL structure and database schema baked chapter numbering into everything. "Irrational Numbers" lived at `/grade/9/maths/chapter/1/topic/2`. But irrational numbers are revisited in Grade 10 and underpin much of Grade 11 calculus. In our system, these were three completely separate pages with no connection. A student who just read the Grade 9 page had no way to know there was a deeper Grade 11 treatment, and the Grade 11 page assumed prerequisites that were never linked.

**Problem 2: Inconsistency across topics.**  
The LLM generated content independently for each topic, with no memory of what it had said before. So the definition of "irrational number" in section 1.2 and the description of irrational numbers in section 1.4 could (and did) differ slightly in wording, notation choice, and even mathematical conventions. Across a full textbook, these small inconsistencies added up into a confusing experience.

**Problem 3: Hallucination in mathematical content.**  
Llama 3.2 3B is a capable model but it is not a mathematician. For straightforward topics like simple arithmetic or basic geometry, it did well. For anything requiring multi-step reasoning — like proving that $\sqrt{2}$ is irrational, or deriving the quadratic formula — it occasionally made errors that look plausible but are mathematically wrong. Without any verification step, these errors went straight to the user. A 3B parameter model simply does not have enough parametric knowledge to be trusted for all of grade 6–12 mathematics.

**Problem 4: Translation inconsistency across batches.**  
Even using the same model and the same settings, the Hindi term chosen for "derivative" in Chapter 1 was sometimes different from the one chosen in Chapter 5 — because the model was making an independent decision each time. Mathematical terminology in Indic languages is not fully standardised, so the model had multiple reasonable choices and happened to pick different ones in different batches. This is a serious problem: if a student reads five chapters and sees five different Hindi words for the same English term, they cannot build a coherent understanding.

**Problem 5: LaTeX corruption in edge cases.**  
The text-splitting approach for LaTeX preservation worked well in most cases but failed when LaTeX was embedded in complex ways — for example, inside a bullet point that itself contained text between two LaTeX expressions. In these cases, the sentence boundaries were wrong and the translation model saw a fragment that didn't make grammatical sense, producing garbled output.

**Problem 6: No concept-level navigation.**  
A student reading about "Real Numbers" had no way to navigate to "Rational Numbers" or "Integers" without going back to the chapter list and hunting. The structure was linear and flat — exactly like a digitised textbook. We had not added any value over NCERT ePathshala in terms of discoverability.

**Problem 7: Repeated work across chapters.**  
Some concepts appear in the introduction of multiple chapters. "Polynomials" is briefly introduced in Grade 9 Chapter 2 and again in Grade 10 Chapter 2. Our pipeline generated separate content pages for each NCERT section that mentioned polynomials, with no shared content or cross-referencing. The same content was being generated (inconsistently) multiple times.

**The core insight that came out of this analysis:** The fundamental unit of our system should be the **concept**, not the **chapter section**. Chapters are a publishing artefact — a way to organise a printed textbook for a single grade. Concepts are what students actually need to learn, and they persist and deepen across years of schooling. Designing around chapters was the wrong abstraction from the start.

---

## 6. The Transition: From Chapters to Concepts

After identifying these failures, we stepped back and thought about what the system actually needed to look like. The key realisations were:

1. **We need a canonical, grade-agnostic definition for each concept.** "Fraction" should have one canonical entry in our system, not one per grade and one per chapter that mentions it.

2. **Prerequisites need to be explicit.** Every page should know what it depends on. This is not just useful for navigation — it is essential for content generation (you can't write a good explanation of Topic X without knowing what the reader already understands).

3. **Content should be generated with its prerequisite context available.** If the prompt for generating "Integration by Parts" includes a summary of "Integration by Substitution" and "Product Rule of Differentiation," the generated content will be much more consistent and build properly on prior knowledge.

4. **Translation should eventually be replaced by direct multilingual generation.** Instead of generating in English and translating to Hindi, we should generate in Hindi directly using a model trained on Indian educational content. This eliminates the translation step entirely and avoids all the terminology consistency problems.

These four realisations defined Pipeline v2.

---

## 7. Pipeline v2: The Knowledge-Graph Approach

### 7.1 Stage 1: Multi-Source Topic Ingestion

The first step in Pipeline v2 was collecting topics from multiple curriculum sources, not just NCERT. For each grade and subject, we ingested topics from:
- NCERT textbook headings (already extracted in Pipeline v1)
- ICSE syllabus and textbook chapter outlines
- Selected state board syllabi (Karnataka and Maharashtra state boards for maths)

The raw topics from all these sources were merged and stored as JSON files in `data/intermediate/raw_topics/`. The structure of each file is:

```json
{
  "raw_name": "Irrational Numbers",
  "ncert_refs": ["chapter1"],
  "subtopics": ["Proof of irrationality", "Decimal expansions", "Number line representation"],
  "source_boards": ["NCERT", "ICSE"],
  "note": ""
}
```

This produced 11 raw topic files covering all grades:
- Grade 6 Mathematics: **86 topics**
- Grade 7 Mathematics: 71 topics
- Grade 8 Mathematics: 78 topics
- Grade 9 Mathematics: 68 topics
- Grade 10 Mathematics: 74 topics
- Grade 11 Mathematics: 82 topics
- Grade 12 Mathematics: **56 topics** (covering calculus-heavy content)
- Grade 6–9 Science: 4 files with analogous structure

The high topic count for Grade 6 reflects the breadth of that curriculum — fractions, basic geometry, data handling, introduction to algebra, and more all appear together. Grade 12 has fewer raw topics because many subtopics were consolidated into unified canonical concepts during graph construction.

### 7.2 Stage 2: Canonical Concept Discovery with LLM Assistance

The raw topic lists contain duplicates, overlapping topics, and topics at inconsistent levels of granularity. "Fractions" might appear in the Grade 6 raw topics as "Introduction to Fractions," "Equivalent Fractions," "Addition of Fractions," and "Mixed Numbers" as separate entries. The next step was consolidating these into canonical concepts.

We used **Llama** as a "curriculum expert" to process these raw topics and propose canonical concept names and groupings. The model was prompted with the full list of raw topics for a grade and asked to identify which ones refer to the same underlying concept, which are sub-concepts of a broader topic, and what the canonical name should be (a name that a student might search for on Wikipedia, not a chapter heading like "3.2 Equivalent Fractions").

The LLM output was then **manually reviewed and edited**. This is the crucial part. We did not trust the model's output without human verification — particularly for prerequisite edges. The model made reasonable suggestions for which concepts are prerequisites for which others, but these suggestions were checked against the actual curriculum sequence and corrected where needed.

### 7.3 Stage 3: Manual Graph Construction and Validation

After the LLM-assisted discovery pass, we built the actual knowledge graph manually using a Python script (`scripts/_build_manual_graph.py`). Each concept was defined as a tuple:

```python
("quadratic-equations", "Quadratic Equations", [9, 10], "Algebra",
 ["linear-equations", "factorisation", "square-roots"],
 "Polynomial equations of degree 2; solving by factorisation, completing the square, quadratic formula")
```

This compact format captures: the slug (URL identifier), canonical name, which grades the concept is taught in, which mathematical area it belongs to, its prerequisite concepts (by slug), and a description.

The script validates the entire graph on every build:
- **All prerequisite slugs must exist** in the concept list
- **No cycles allowed** — the graph must be a valid DAG (directed acyclic graph). If a cycle is detected, the build fails with a clear error showing the cycle path.
- **`leads_to` edges are computed automatically** as the reverse of prerequisite edges — so if "Fractions" is a prerequisite of "Rational Numbers," the system automatically adds "Rational Numbers" to Fractions' `leads_to` list.

The graph also computes **grade views**: for each grade, the set of concepts relevant to that grade and the set of entry points (concepts with no prerequisites relevant to that grade).

**Final graph statistics (Mathematics, v4):**
- **324 concepts** spanning Grades 6–12
- **497 directed prerequisite edges**
- **18 mathematical topic areas**: Number Systems, Algebra, Geometry, Trigonometry, Coordinate Geometry, Calculus (Differential), Calculus (Integral), Differential Equations, Vectors, 3D Geometry, Statistics, Probability, Combinatorics, Sequences and Series, Complex Numbers, Matrices and Determinants, Mathematical Logic, Mensuration
- Coverage: every major topic from the NCERT mathematics curriculum Grades 6–12, plus additional topics from ICSE and state boards

The graph was stored as `data/output/knowledge_graph/maths_v2.json` with the following structure:

```json
{
  "subject": "mathematics",
  "version": "v4",
  "total_concepts": 324,
  "total_edges": 497,
  "concepts": {
    "quadratic-equations": {
      "canonical_name": "Quadratic Equations",
      "slug": "quadratic-equations",
      "grades": [9, 10],
      "area": "Algebra",
      "description": "Polynomial equations of degree 2...",
      "prerequisites": ["linear-equations", "factorisation", "square-roots"],
      "leads_to": ["completing-the-square", "quadratic-formula", "complex-roots-of-quadratic", ...]
    }
  },
  "edges": [...],
  "grade_views": { "9": {...}, "10": {...}, ... }
}
```

### 7.4 Graph Depth and Coverage

To give a sense of the graph's depth, here is the prerequisite chain for a typical Grade 12 concept:

```
Natural Numbers → Whole Numbers → Integers → Rational Numbers → Real Numbers
    → Algebra Basics → Polynomial Expressions → Differentiation (First Principles)
        → Rules of Differentiation → Chain Rule → Implicit Differentiation
```

A student starting at "Implicit Differentiation" can follow the prerequisite links all the way back to "Natural Numbers" if needed — or jump directly to a prerequisite they feel shaky on.

The 18 topic areas form natural clusters within the graph. Number Systems, Algebra, and Geometry are the three large clusters that dominate Grades 6–9. Trigonometry, Coordinate Geometry, and Statistics grow through Grades 9–11. Calculus, Differential Equations, Vectors, and 3D Geometry dominate Grade 12. Prerequisites cross cluster boundaries — for example, Trigonometry has prerequisites in both Geometry and Algebra, and Calculus requires solid Algebra, Coordinate Geometry, and Trigonometry.

### 7.5 Science Knowledge Graph (In Progress)

The same graph construction process is being applied to school science (Physics, Chemistry, Biology). Raw topics have been extracted for Grades 6–9. The science graph is expected to have similar depth — approximately 300–400 concepts per subject — but construction requires more domain expertise to establish correct prerequisite relationships, particularly for Chemistry and Biology where the conceptual dependencies are less linear than mathematics.

For the purpose of this report, the science graph will be included in the final system with the same structure and methodology as the mathematics graph.

### 7.6 Stage 4: RAG-Based Content Generation (Upcoming)

With the knowledge graph in place, the content generation in Pipeline v2 will work very differently from Pipeline v1.

For each concept in the graph, the content generation pipeline will:

1. **Retrieve reference chunks** from the relevant NCERT textbook sections using a vector similarity search (RAG). The retrieved chunks provide verified, curriculum-aligned reference material that the LLM can use as grounding.

2. **Assemble the prerequisite context**: For each prerequisite of the concept, include a summary of that prerequisite's content in the prompt. This grounds the generated explanation in prior knowledge.

3. **Call the generation model** with a rich prompt containing: the concept name, its grade level(s), the retrieved reference chunks, summaries of prerequisite concepts, and an instruction to generate a complete explanation page.

4. **Verify the output** with a lightweight verification pass that checks for mathematical consistency and flags potential hallucinations.

The RAG component requires building a vector index over the NCERT text chunks. We have the text chunks available in `data/intermediate/chunks/` from the Pipeline v1 parsing step. The plan is to embed these chunks using a sentence transformer and store them in a vector database (likely ChromaDB or FAISS for local use, Pinecone for production).

### 7.7 Stage 5: Direct Multilingual Generation via Sarvam (Upcoming)

The translation step from Pipeline v1 is being replaced entirely by **direct multilingual generation**. Instead of generating in English and then translating, we will generate in Hindi, Telugu, and Odia directly.

The Sarvam AI model family is purpose-built for Indian-language text generation. The Sarvam-30B model has been trained on large corpora of Indian educational content and handles mathematical terminology in Indic languages significantly better than a general-purpose model followed by translation.

This approach has several advantages over the translation approach in Pipeline v1:
- **No LaTeX corruption risk** — the model generates LaTeX natively, it does not need to translate through it
- **Consistent terminology** — the model has a fixed internal vocabulary for mathematical terms in each language, so "derivative" will consistently map to the same Hindi term throughout
- **Better fluency** — content generated natively in a language is usually more natural than translated content
- **Single model call** — instead of generate + translate (two passes), it is one pass

The Sarvam API is already integrated into the project. The API key is configured in the webapp's environment file, and basic API calls have been tested. The generation script that calls Sarvam-30B with the RAG-assembled prompts is the next major development task.

---

## 8. Web Platform

### 8.1 Architecture

The web platform has two parts:
- **Express.js API server** (port 5000): Handles database queries, search, and content retrieval
- **Next.js frontend** (port 3000): Serves the user interface

The frontend is built with Next.js 16.2 using the App Router. It uses React Server Components for graph-derived pages, meaning most pages are rendered server-side and shipped as static HTML — important for performance on slower mobile connections.

MongoDB Atlas stores the content documents. The Express server provides REST endpoints:
- `GET /api/catalog` — list all available content
- `GET /api/content` — retrieve a specific content document
- `GET /api/search` — full-text search across concepts
- `GET /api/health` — server health check

### 8.2 Knowledge Graph UI (New in Pipeline v2)

The most significant new addition to the web platform is the knowledge-graph-aware UI, accessible at `/maths` and its sub-routes.

**`/maths` — Mathematics Hub:**  
Shows overall statistics (324 concepts, 497 connections), a colour-coded legend of all 18 mathematical areas, and grade cards for Grades 6 through 12. Each grade card shows how many concepts appear in that grade and a sample of which areas they cover.

**`/maths/{grade}` — Grade View:**  
For a given grade (e.g., `/maths/9`), shows all concepts grouped by mathematical area, with jump navigation between area sections. Each concept card shows the concept name, a brief description, an indicator of prerequisites (with ← arrows), and a badge if the concept spans multiple grades.

**`/maths/{grade}/{slug}` — Concept Page:**  
The individual concept page shows:
- The mathematical area (colour-coded badge)
- Multi-grade indicator (if the concept is taught across multiple grades)
- Full description
- **Prerequisites section**: clickable buttons for each prerequisite, each showing the prerequisite's area and grade — so a student can navigate directly to any concept they need to review
- **Content placeholder**: where the generated explanation will appear once generation is complete
- **"What this unlocks" section**: the `leads_to` concepts from the graph, showing up to four next concepts the student can progress to
- Navigation breadcrumb (back to grade view, back to maths hub)

The Next.js build generates **405 static pages** from the knowledge graph using `generateStaticParams()`, covering all 324 concepts across all relevant grades. This means every page is pre-rendered and served as static HTML — fast loading, no database hit at page-serve time.

**`/maths/{grade}/{slug}` Page example for "Quadratic Equations" (Grade 9):**
- Area badge: Algebra (orange)
- Also in: Grade 10
- Description: "Polynomial equations of degree 2; solve by factorisation, completing the square, or quadratic formula"
- Prerequisites: Linear Equations ← (Algebra, Gr. 7–9), Factorisation ← (Algebra, Gr. 8–9), Square Roots ← (Number Systems, Gr. 6–8)
- What this unlocks: Completing the Square →, Quadratic Formula →, Vieta's Formulas →, Complex Roots →

**Interactive Visualization:**  
The full graph is also available as an interactive HTML visualization (`data/output/knowledge_graph/maths_v2_visual.html`), showing all 324 nodes colour-coded by area with all 497 edges drawn as arrows. This was generated automatically by the graph builder and is useful for understanding the overall structure.

### 8.3 Existing Chapter-Based Content

The Pipeline v1 content (chapter-based pages for Grade 9 Mathematics) remains accessible through the original routes. Three chapters of Grade 9 Mathematics content have been fully generated, translated into Hindi, Telugu, and Odia, and uploaded to MongoDB. This existing content provides a comparison point for evaluating the quality improvement from Pipeline v2 generation when it is complete.

---

## 9. Implementation Details

### 9.1 Hardware and Software Environment

All local LLM inference runs on:
- **GPU**: NVIDIA RTX 3050, 4 GB VRAM
- **OS**: Windows 11
- **Python**: 3.11 with PyTorch + CUDA backend
- **Quantisation**: BitsAndBytes NF4 4-bit for all models >2B parameters

The 4 GB VRAM constraint was binding throughout. At 4-bit quantisation, a 3B model uses ~2 GB, leaving ~1.5 GB for activations and KV-cache. This allowed a maximum context length of about 2,048 tokens with Llama 3.2 3B before running out of memory. Longer content was generated in chunks and assembled.

Key library versions:
- `transformers`: 5.x for Llama, 4.45 for IndicTrans2 (separate venvs)
- `bitsandbytes`: 0.43.x
- `pdfplumber`: for PDF parsing
- `networkx`: for DAG validation in the graph builder

### 9.2 Graph Builder Technical Details

The graph builder (`scripts/_build_manual_graph.py`) is the most carefully engineered part of the project. It uses the `networkx` library's cycle detection (`nx.find_cycle`) to validate the DAG property after every modification. This was essential during the manual curation phase — adding a new concept with a wrong prerequisite could introduce a cycle, and the immediate error message with the cycle path made it easy to fix.

The builder also checks for prerequisite slugs that don't exist, catching typos immediately rather than silently creating broken links.

The final build output is a single JSON file with four top-level sections:
1. `concepts` — the full concept dictionary
2. `edges` — a flat list of all prerequisite edges
3. `grade_views` — per-grade subgraphs
4. metadata (version, total_concepts, total_edges, description)

### 9.3 Database Schema

MongoDB Atlas is used with the following collections:

**`chapters` collection:**
```json
{
  "grade": 9, "subject": "maths", "chapter_number": 1,
  "chapter_title": "NUMBER SYSTEMS",
  "topics": [{"number": "1.1", "title": "Introduction", ...}]
}
```

**`topics` collection:**
```json
{
  "grade": 9, "subject": "maths", "chapter_number": 1,
  "topic_number": "1.2", "topic_title": "Irrational Numbers",
  "content_en": "...(full markdown)...",
  "content_hi": "...(Hindi translation)...",
  "content_te": "...(Telugu translation)...",
  "content_od": "...(Odia translation)..."
}
```

Documents are upserted (inserted or updated) by their natural key (grade + subject + chapter + topic), so re-running the pipeline after changes updates existing documents rather than creating duplicates.

---

## 10. Results and Evaluation

### 10.1 Pipeline v1 Output Quality Assessment

After generating content for Grade 9 Mathematics (Chapters 1–3) and translating them into three languages, we conducted a qualitative review of the output.

**English content**: Generally good for straightforward topics (Irrational Numbers, Decimal Expansions). Weaker for proof-heavy topics and computation-heavy topics where the small model occasionally introduced minor errors. The structured format (Introduction → Explanation → Examples → Mistakes → Summary) was consistent across topics because it was enforced by the prompt, not generated organically.

**Hindi translation (IndicTrans2)**: Fluent prose, good grammar. Mathematical terminology was reasonable for most terms. The two terms that showed the most inconsistency were "rational number" (sometimes kept in English, sometimes rendered in Hindi script using different transliterations) and "coefficient" (at least three different Hindi renderings across chapters).

**Telugu translation**: Comparable quality to Hindi. Odia was the weakest — IndicTrans2's Odia training data is more limited, and some sentences came out stilted or with incorrect grammar.

**LaTeX preservation**: The text-splitting approach worked for ~92% of mathematical expressions. The remaining ~8% had some form of corruption — missing braces, translated subscript text, or broken delimiters.

### 10.2 Knowledge Graph Validation

The maths_v2.json knowledge graph (v4) passes all automated validation checks:
- All 324 concept slugs are unique
- All prerequisite references point to existing concepts (no broken links)
- The graph is a valid DAG (zero cycles detected)
- All `leads_to` edges are consistent with prerequisite edges (automatically computed)

Grade coverage is well-balanced: Grade 6 has 52 concepts (broad foundational coverage), Grade 12 has 89 concept appearances (deepest content), with other grades in between. Many concepts span multiple grades — for example, "Fractions" is listed for Grades 6 and 7, "Linear Equations" for Grades 7, 8, and 9, "Trigonometry Basics" for Grades 10 and 11.

### 10.3 Web Platform

The Next.js build successfully generates **405 static pages** from the knowledge graph and deploys without errors (the single warning during build is an unrelated npm lockfile warning, not a build failure). All concept pages render correctly with proper prerequisite links and leads-to navigation.

The user experience on the concept pages directly addresses the problems identified in Pipeline v1:
- A student on the "Quadratic Equations" page in Grade 9 can immediately see that it requires "Linear Equations" and "Factorisation" (with clickable links)
- They can see that it leads to "Completing the Square" and "Quadratic Formula"
- If they are also in Grade 10, the multi-grade badge lets them navigate to the Grade 10 perspective on the same concept

---

## 11. Future Work

### 11.1 RAG Pipeline and Content Generation

The most pressing remaining piece is completing Stage 4: building the RAG pipeline and generating actual explanation content for all 324 graph concepts. The plan is:

1. **Build the vector index**: Embed all text chunks from `data/intermediate/chunks/` using a sentence transformer (likely `all-MiniLM-L6-v2` for local use, or a Sarvam embedding model for better Indic language support).

2. **Implement context assembly**: For each concept, retrieve the top-k most relevant text chunks from the NCERT textbooks plus summaries of prerequisite concepts.

3. **Generate with Sarvam-30B**: Use the Sarvam API to generate content in English, Hindi, Telugu, and Odia in a single pass — no separate translation step.

4. **Quality review**: A sample-based human review of generated content, particularly for complex Grade 11–12 topics.

### 11.2 Science Knowledge Graph

The raw topic files for science (Grades 6–9) are ready. The science graph will follow the same construction methodology as the mathematics graph. Physics, Chemistry, and Biology each present different challenges for prerequisite mapping — Biology topics are often parallel rather than sequential, while Chemistry and Physics have more obvious prerequisite chains. We estimate the science graph will have approximately 400–500 concepts per subject across the relevant grades.

### 11.3 Cross-Subject Prerequisites

An interesting extension is modeling cross-subject prerequisites. "Vectors" in Grade 11 Mathematics is a prerequisite for "Electric Field Lines" and "Force Resolution" in Grade 11 Physics. "Probability" in Grade 10 Mathematics underlies "Genetics" concepts in Grade 12 Biology. A unified multi-subject graph would enable this navigation.

### 11.4 Personalized Learning Paths

With the knowledge graph structure in place, implementing personalized learning path recommendations is straightforward. Given a student's learning goal (e.g., "I want to understand Integration") and their current knowledge state (which concepts they have mastered), the system can compute the shortest path through the prerequisite graph to their goal. This is essentially a reachability and topological sort problem on the DAG.

### 11.5 Mastery Tracking and Assessment

The concept pages currently show static content. Adding a practice problem generator (using the same LLM + RAG pipeline but with a "generate problems" prompt) and a lightweight mastery tracker would turn the platform from a reference resource into an active learning tool.

---

## 12. Conclusion

We set out to solve a real problem: Indian school students need good educational content in their regional languages, and the existing digital options are either limited to English, limited to one curriculum board, or not interactive enough to help students navigate between related concepts.

Our first attempt — a linear pipeline that extracted chapter sections from NCERT PDFs, generated explanations using a quantised Llama model, and translated them using neural MT models — got working results quickly but revealed deep structural problems. Content was inconsistent, mathematics terminology in translations was unreliable, and the chapter-based structure was fundamentally the wrong abstraction.

The knowledge graph approach we designed and implemented in Pipeline v2 addresses all of these problems at their root. By making the **concept** (not the chapter) the first-class unit of the system, we get: canonical, non-redundant content; explicit prerequisite relationships that improve both content generation and user navigation; a structure that spans multiple boards rather than being tied to NCERT chapter numbering; and a clear path to replacing the unreliable translation step with direct multilingual generation.

The mathematics knowledge graph we built — 324 concepts, 497 edges, 18 areas, Grades 6 through 12 — is a genuine educational artifact that took significant expert effort to construct correctly. The web platform built on top of it provides navigation that no current free platform for Indian school mathematics offers: the ability to follow prerequisite links between concepts the way one follows links on Wikipedia, across grade boundaries, within a curriculum-aligned structure.

The remaining work — RAG content generation, the Sarvam direct multilingual generation pipeline, and the science graph — follows the architecture already in place. The hardest conceptual problems have been solved. The system is ready to scale.

---

## References

1. Vijay, S., et al. *IndicTrans2: Towards High-Quality and Accessible Machine Translation for All 22 Scheduled Indian Languages.* arXiv:2305.16307, 2023.

2. Kochhar, P., et al. *Sarvam-1: A Comprehensive Suite of Language Models for India's Languages.* Sarvam AI Technical Report, 2024.

3. Piech, C., et al. *Deep Knowledge Tracing.* Advances in Neural Information Processing Systems (NeurIPS), 2015.

4. Liang, P., et al. *Holistic Evaluation of Language Models (HELM).* arXiv:2211.09110, 2022.

5. Shi, F., et al. *Language Models are Multilingual Chain-of-Thought Reasoners.* ICLR, 2023.

6. Agarwal, O., et al. *Knowledge Graph-Based Adaptive Learning for Personalized Education.* Proceedings of the 14th International Conference on Educational Data Mining (EDM), 2021.

7. Touvron, H., et al. *Llama 3: Open Foundation and Fine-Tuned Chat Models.* Meta AI Technical Report, 2024.

8. Brown, T., et al. *Language Models are Few-Shot Learners.* NeurIPS, 2020.

9. Lewis, P., et al. *Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks.* NeurIPS, 2020.

10. NCERT. *National Curriculum Framework 2023.* National Council of Educational Research and Training, Government of India, 2023.

11. Dettmers, T., et al. *QLoRA: Efficient Finetuning of Quantized LLMs.* NeurIPS, 2023.

12. Reimers, N., and Gurevych, I. *Sentence-BERT: Sentence Embeddings using Siamese BERT-Networks.* EMNLP, 2019.

---

*Report prepared as part of B.Tech Thesis Project (BTP-1), IIIT Hyderabad.*
