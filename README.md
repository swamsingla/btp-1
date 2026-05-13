
# Multilingual Educational Knowledge Platform

A knowledge-graph-driven platform that generates educational content for students in **grades 6–12** (Maths and Science) directly in **English, Hindi, Telugu, and Odia** — without any translation step. Content is grounded in a prerequisite-aware knowledge graph built from NCERT, ICSE, and state board curricula.

---

## How It Works

The pipeline has four stages followed by a web delivery layer:

```
NCERT PDFs + board syllabi
        │
        ▼
[Stage 1] topic_ingestion.py  — discover all topics across boards (LLaMA 3.1 8B)
        │
        ▼
[Stage 2] graph_builder.py    — build canonical concept graph + prerequisite DAG (LLaMA 3.1 8B + NetworkX)
        │
        ▼
[Stage 3] approach_b/graph_rag.py  — assemble context per concept×grade
          (graph structure + NCERT text chunks + Wikipedia)
        │
        ▼
[Stage 4] approach_b/generate.py   — generate articles in 4 languages (Sarvam AI API)
        │
        ▼
[Web]   server/ (Express API)  +  webapp/ (Next.js frontend)  ←  MongoDB Atlas
```

**Stage 1 — Topic Ingestion:**  
`topic_ingestion.py` uses LLaMA 3.1 8B to comprehensively discover every topic a student should learn at each grade × subject combination, cross-referencing NCERT headings already parsed from PDFs with a broader LLM-powered survey of NCERT, ICSE, and state board syllabi. Output is one JSON per `grade_subject` in `data/intermediate/raw_topics/`.

**Stage 2 — Knowledge Graph Construction:**  
`graph_builder.py` takes the raw per-grade topic lists and uses LLaMA 3.1 8B to extract a canonical four-level concept hierarchy (Domain → Area → Concept → Sub-concept), establish prerequisite edges between concepts, and validate the result is a DAG (no cycles) using NetworkX. The final graph is saved to `data/knowledge_graph/` and also copied to `webapp/public/` for the frontend.

**Stage 3 — Graph-RAG Context Assembly:**  
`approach_b/graph_rag.py` assembles a content plan for every (concept, grade) pair by pulling from three sources: (1) the knowledge graph — prerequisites, related concepts, leads-to links; (2) NCERT textbook chunks fuzzy-matched from parsed PDFs; (3) Wikipedia summaries fetched in parallel. Output is one JSON content plan per (concept, grade) in `data/content_plans/`.

**Stage 4 — Multilingual Content Generation:**  
`approach_b/generate.py` reads each content plan and calls the Sarvam AI API to generate a Wikipedia-style educational article **natively** in all four languages — no translation involved. Output is Markdown files in `data/generated_pages/{language}/`.

---

## Project Structure

```
scripts/
├── topic_ingestion.py        # Stage 1 — multi-board topic discovery
├── graph_builder.py          # Stage 2 — knowledge graph construction
├── approach_b/
│   ├── graph_rag.py          # Stage 3 — Graph-RAG context assembly
│   └── generate.py           # Stage 4 — Sarvam multilingual generation
├── llm_local.py              # LLaMA 3.1 8B inference wrapper (HuggingFace)
├── download_llama.py         # Downloads LLaMA model to cluster scratch space
├── batch_orchestrate.py      # SSH orchestrator — transfers chunks and runs jobs on ADA cluster
├── run_pipeline.sh           # SLURM job script for ADA cluster (stages 1–4)
├── maths_extractor.py        # Extracts text chunks from maths PDFs
├── science_extractor.py      # Extracts text chunks from science PDFs
├── headings_extractor.py     # Parses chapter headings from PDFs
├── build_science_kg.py       # Builds the science knowledge graph
├── check_graph_quality.py    # Audits the built knowledge graph for coverage gaps
└── approach_a/               # Phase 1 pipeline (archived)

data/
├── input/                    # NCERT PDFs organized by grade and subject
│   ├── grade6/maths/
│   ├── grade6/science/
│   └── ...
├── intermediate/
│   ├── headings/             # Parsed chapter headings (JSON)
│   ├── raw_topics/           # Stage 1 output — topic lists per grade+subject
│   └── chunks/               # NCERT text chunks used for RAG
├── knowledge_graph/          # Stage 2 output
│   ├── maths/
│   │   ├── graph.json               # Full maths graph (324 concepts)
│   │   ├── maths_visual.html        # Interactive vis-network visualisation
│   │   ├── graph_by_subject/
│   │   │   └── maths.json
│   │   └── graph_by_grade/
│   │       └── grade6_maths.json … grade12_maths.json
│   └── science/
│       ├── graph.json               # Combined science graph (114 concepts)
│       ├── science_visual.html      # Interactive vis-network visualisation
│       ├── graph_by_subject/
│       │   ├── biology.json
│       │   ├── chemistry.json
│       │   ├── physics.json
│       │   └── science.json
│       └── graph_by_grade/
│           └── grade6_biology.json … grade12_physics.json  (26 files)
├── content_plans/            # Stage 3 output — per-concept content plans
└── generated_pages/          # Stage 4 output — articles per language
    ├── en/
    ├── hi/
    ├── te/
    └── od/

webapp/                       # Next.js 16 frontend
├── src/app/                  # App router pages
├── src/components/           # React components
├── public/                   # Static assets including knowledge graph JSONs
└── package.json

server/                       # Express API server
├── server.js                 # Entry point (port 5000)
├── routes/
│   ├── catalog.js            # GET /api/catalog — list grades/subjects/concepts
│   ├── content.js            # GET /api/content — fetch article by concept+grade+lang
│   └── search.js             # GET /api/search — full-text search
└── utils/

report/                       # BTP report (LaTeX source)
└── main.tex
```

---

## Prerequisites

| Requirement | Version |
|---|---|
| Python | 3.10+ |
| Node.js | 18+ |
| GPU (for stages 1–3) | ~10 GB VRAM (or use ADA cluster) |
| Sarvam AI API key | Required for stage 4 |
| MongoDB Atlas URI | Required for web server |

---

## Setup

### 1. Python environment

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# Linux / macOS
source .venv/bin/activate

pip install -r requirements.txt
```

Additional packages used by the pipeline (install as needed):

```bash
pip install transformers accelerate bitsandbytes networkx thefuzz requests paramiko
```

### 2. Environment variables

Create a `.env` file in the project root:

```env
# Path to LLaMA 3.1 8B model weights (stages 1–3)
LLAMA_MODEL_PATH=/path/to/models/llama-8b

# Sarvam AI — used for stage 4 content generation
SARVAM_API_KEY=your_sarvam_key

# MongoDB Atlas — used by the Express server
MONGO_URI=mongodb+srv://user:password@cluster.mongodb.net/ncert_wiki
```

For the webapp, create `webapp/.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:5000
```

### 3. LLaMA model (for stages 1–3)

```bash
python scripts/download_llama.py
```

This downloads `meta-llama/Meta-Llama-3.1-8B-Instruct` to the path set in `LLAMA_MODEL_PATH`. On the ADA cluster it places the model in `/ssd_scratch/models/llama-8b`.

---

## Running the Pipeline

### On the ADA cluster (recommended — SLURM)

Stages 1–3 run on GPU nodes. Submit as a SLURM job:

```bash
sbatch scripts/run_pipeline.sh
```

To transfer data and orchestrate jobs remotely from your local machine (configure SSH credentials in `batch_orchestrate.py` first):

```bash
python scripts/batch_orchestrate.py
```

### Locally (requires GPU with ~10 GB VRAM)

Run each stage individually. Use `--grade` and `--subject` flags to process a subset:

```bash
# Stage 1 — topic ingestion
python scripts/topic_ingestion.py --grade 6 --subject maths

# Stage 2 — knowledge graph
python scripts/graph_builder.py --subject maths

# Stage 3 — Graph-RAG context plans
python scripts/approach_b/graph_rag.py --grade 6 --no-wiki   # --no-wiki skips Wikipedia (faster)

# Stage 4 — generate content (no GPU needed, uses Sarvam API)
python scripts/approach_b/generate.py --grade 6 --languages en,hi
```

Check graph quality after stage 2:

```bash
python scripts/check_graph_quality.py
```

---

## Running the Web Application

### Backend (Express API)

```bash
cd server
npm install
npm run dev        # starts on http://localhost:5000
```

### Frontend (Next.js)

```bash
cd webapp
npm install
npm run dev        # starts on http://localhost:3000
```

Open `http://localhost:3000` in your browser.

For a production build:

```bash
cd webapp
npm run build
npm start
```

---

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/api/health` | Server health check |
| GET | `/api/catalog` | List all grades, subjects, and concepts |
| GET | `/api/content` | Fetch article for a concept, grade, and language |
| GET | `/api/search` | Full-text search across all content |

---

## Key Design Decisions

- **No translation.** Content is generated directly in each language by Sarvam AI, which produces far more natural output than translating English articles.
- **Knowledge graph as curriculum.** The DAG structure captures prerequisite relationships, enabling graph-based navigation and ensuring content is presented in a pedagogically sound order.
- **Multi-board coverage.** Topics are discovered across NCERT, ICSE, and state boards and mapped to canonical concepts, so the platform is not tied to any single syllabus.
- **Stages 1–3 are GPU-bound; stage 4 is API-only.** The split allows stage 4 to be run or re-run without cluster access.

---

## Report

The full project report is in [`report/main.tex`](report/main.tex) (LaTeX). Compile with `pdflatex` or any standard LaTeX distribution.
