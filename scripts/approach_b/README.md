# Approach B — Knowledge Graph → Graph-RAG → Direct Multilingual Generation

## Pipeline Overview

```
maths_v2.json (324 concepts, 497 edges)
        │
        ▼
┌─────────────────────┐
│  1. graph_rag.py     │  Gathers context from:
│     (Content Plans)  │    • Knowledge graph edges (prereqs, leads_to, related)
│                      │    • NCERT textbook chunks (fuzzy-matched)
│                      │    • Wikipedia summaries (optional)
└──────────┬──────────┘
           │  → data/content_plans/*.json
           ▼
┌─────────────────────┐
│  2. generate.py      │  For each (concept, grade, language):
│     (Sarvam API)     │    • Builds prompt with graph context
│                      │    • Calls Sarvam API (en, hi, te, od)
│                      │    • Post-processes + smoke tests
└──────────┬──────────┘
           │  → data/generated_pages/{lang}/{slug}_grade{N}.md
           ▼
       Web App reads generated markdown
```

## Quick Start

```bash
# Step 1: Install dependencies
pip install thefuzz requests openai

# Step 2: Create content plans (no API needed)
python scripts/approach_b/graph_rag.py

# Step 3: Verify all plans were created
python scripts/approach_b/graph_rag.py --check-coverage

# Step 4: Generate content (requires Sarvam API key)
export SARVAM_API_KEY="your_key_here"
python scripts/approach_b/generate.py --api-key $SARVAM_API_KEY

# Or: generate just one concept to test
python scripts/approach_b/generate.py --concept fractions --grade 6 --languages en --test
```

## Key Design Decisions

1. **No translation step** — content is generated directly in all 4 languages
2. **Graph-RAG context** — each prompt includes prerequisite descriptions, successor topics, and related concepts from the knowledge graph
3. **No local LLM needed** — `graph_rag.py` does pure data assembly; only `generate.py` calls the API
4. **Skip-existing** — safe to kill and restart; already-generated pages are skipped
5. **Source of truth** — uses `webapp/public/maths_v2.json` (the same file the frontend reads)

## Filtering Options

```bash
# Grade filter
python scripts/approach_b/graph_rag.py --grade 6
python scripts/approach_b/generate.py --grade 6

# Concept filter
python scripts/approach_b/graph_rag.py --concept quadratic-equations
python scripts/approach_b/generate.py --concept quadratic-equations

# Language filter
python scripts/approach_b/generate.py --languages en,hi

# Skip Wikipedia (faster, offline)
python scripts/approach_b/graph_rag.py --no-wiki

# Dry run (shows what would be generated, no API calls)
python scripts/approach_b/generate.py --dry-run
```
