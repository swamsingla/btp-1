#!/usr/bin/env python3
"""
Stage 4 — Wikipedia-Style Page Generation via Sarvam API
=========================================================
For each content plan produced by content_planner.py, generates a complete
Wikipedia-style educational article in multiple languages using Sarvam-30B.

Key design principles:
  • Direct multilingual generation (NOT translation) — one API call per language
  • Grade-appropriate depth controlled by the content plan's grade_note
  • LaTeX for math ($inline$, $$display$$), wikilinks for cross-references ([[Concept]])
  • Skip-existing for resumability (safe to kill and restart)
  • Exponential backoff on rate limits

Output: data/generated_pages/{language}/{concept_slug}_grade{N}.md
Index:  data/generated_pages/_index.json

Supported languages:
  en = English
  hi = Hindi
  te = Telugu
  od = Odia
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path
from typing import Any

import openai

# ─── Paths ───────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent
PLANS_DIR = BASE_DIR / "data" / "content_plans"
GRAPH_PATH = BASE_DIR / "data" / "knowledge_graph" / "graph.json"
OUTPUT_DIR = BASE_DIR / "data" / "generated_pages"
INDEX_PATH = OUTPUT_DIR / "_index.json"

# ─── Languages ────────────────────────────────────────────────────────────────
LANGUAGES: dict[str, dict[str, str]] = {
    "en": {
        "name": "English",
        "instruction": "Write in clear, fluent English.",
        "see_also_label": "See Also",
        "prerequisites_label": "Prerequisites",
    },
    "hi": {
        "name": "Hindi",
        "instruction": "Write entirely in Hindi (Devanagari script). Do not mix English prose. Technical terms may appear in brackets after the Hindi term on first use: e.g., जड़त्व (Inertia).",
        "see_also_label": "यह भी देखें",
        "prerequisites_label": "पूर्वापेक्षाएँ",
    },
    "te": {
        "name": "Telugu",
        "instruction": "Write entirely in Telugu (Telugu script). Do not mix English prose. Technical terms may appear in brackets after the Telugu term on first use.",
        "see_also_label": "ఇవి కూడా చూడండి",
        "prerequisites_label": "అవసరమైన అంశాలు",
    },
    "od": {
        "name": "Odia",
        "instruction": "Write entirely in Odia (Odia script). Do not mix English prose. Technical terms may appear in brackets after the Odia term on first use.",
        "see_also_label": "ଆହୁରି ଦେଖନ୍ତୁ",
        "prerequisites_label": "ପୂର୍ବ ଆବଶ୍ୟକ ବିଷୟ",
    },
}

# ─── Logging ─────────────────────────────────────────────────────────────────
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s  %(levelname)-8s  %(message)s",
    datefmt="%H:%M:%S",
)
log = logging.getLogger(__name__)

# ─── LLM helpers ─────────────────────────────────────────────────────────────

def make_client(api_key: str, base_url: str) -> openai.OpenAI:
    return openai.OpenAI(api_key=api_key, base_url=base_url)


def llm_call(
    client: openai.OpenAI,
    model: str,
    system: str,
    user: str,
    temperature: float = 0.7,
    max_tokens: int = 4096,
    retries: int = 6,
) -> str:
    for attempt in range(retries):
        try:
            resp = client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": system},
                    {"role": "user", "content": user},
                ],
                temperature=temperature,
                max_tokens=max_tokens,
            )
            return resp.choices[0].message.content.strip()
        except openai.RateLimitError:
            wait = 2 ** attempt * 10
            log.warning("Rate limit; waiting %ds (attempt %d/%d)", wait, attempt + 1, retries)
            time.sleep(wait)
        except openai.APIError as exc:
            log.error("API error: %s", exc)
            if attempt == retries - 1:
                raise
            time.sleep(10)
    raise RuntimeError("LLM call failed after all retries")


# ─── Prompt builder ───────────────────────────────────────────────────────────

SYSTEM_GENERATOR = """You are an expert educational writer creating Wikipedia-style articles
for Indian school students. Your articles are used on an online learning platform that
serves students studying in Hindi, Telugu, Odia, and English.

Quality standard: A student reading your article should understand the topic just as well
as someone who studied it from the best English-language textbooks (Resnick-Halliday,
NCERT, HC Verma, RD Sharma, etc.) — but in their own language.

Formatting rules (STRICT):
1. Start with a lead paragraph that defines the concept clearly and self-containedly.
2. Use ## for main sections, ### for subsections. DO NOT use numbered section headings.
3. Use LaTeX for all mathematics: $inline$ for in-text math, $$displayed$$ for equations.
4. Link to related concepts using [[Concept Name]] notation (use the English concept name
   even in non-English articles — the platform resolves these).
5. Include at least 2 concrete real-world examples or worked problems.
6. End with a "See Also" / equivalent section listing prerequisites, next topics,
   and related concepts as [[wikilinks]].
7. DO NOT start any section with "Section 1" or numbered style.
8. The article must be fully self-contained — the student should not need the textbook."""


def build_generation_prompt(plan: dict, lang_code: str) -> str:
    lang = LANGUAGES[lang_code]
    prereqs = plan.get("prerequisites_to_link", [])
    successors = plan.get("successors_to_link", [])
    related = plan.get("related_to_link", [])
    see_also_all = list({*prereqs, *successors, *related, *plan.get("see_also", [])})
    aliases = plan.get("aliases", [])

    prereq_str = (
        "\n".join(f"  - [[{s}]]" for s in prereqs)
        if prereqs
        else "  (none at this grade)"
    )
    next_str = (
        "\n".join(f"  - [[{s}]]" for s in successors) if successors else "  (none)"
    )
    related_str = (
        "\n".join(f"  - [[{s}]]" for s in related) if related else "  (none)"
    )
    see_also_str = (
        "\n".join(f"  - [[{s}]]" for s in see_also_all) if see_also_all else "  (none)"
    )
    alias_str = f"\nAlso known as: {', '.join(aliases)}" if aliases else ""

    sections_str = "\n".join(f"  - {s}" for s in plan.get("sections", []))

    return f"""ARTICLE TO WRITE: {plan['canonical_name']}{alias_str}
SUBJECT: {plan.get('subject', '').title()}
GRADE LEVEL: Grade {plan['grade']}

LANGUAGE INSTRUCTION: {lang['instruction']}

GRADE-APPROPRIATE DEPTH:
{plan.get('grade_note', '')}

KNOWLEDGE GRAPH CONTEXT:
Prerequisites (student has already studied these — you may reference without re-explaining):
{prereq_str}

What this concept leads to (briefly foreshadow where appropriate):
{next_str}

Related concepts to cross-link with [[wikilinks]]:
{related_str}

All See Also links to include in the final section:
{see_also_str}

SUGGESTED ARTICLE STRUCTURE:
{sections_str}

REFERENCE MATERIAL (use for accuracy; do not copy verbatim):
---
{plan.get('context_summary', 'No source material — use curriculum knowledge.')}
---

TARGET LENGTH: approximately {plan.get('target_words', 1000)} words

Write the complete article now. Start directly with the lead paragraph.
Remember: {lang['instruction']}"""


# ─── Post-processing ──────────────────────────────────────────────────────────

def postprocess_article(text: str, lang_code: str) -> str:
    """
    Clean and standardise generated article markdown.
      - Ensure wikilinks use consistent format
      - Fix common LaTeX formatting issues
      - Remove accidental markdown fences around the whole article
    """
    # Strip surrounding code fences if the model wrapped the article
    text = re.sub(r"^```(?:markdown)?\s*\n", "", text)
    text = re.sub(r"\n```\s*$", "", text)

    # Normalise LaTeX: ensure \( → $ and \[ → $$
    text = re.sub(r"\\\((.+?)\\\)", r"$\1$", text)
    text = re.sub(r"\\\[(.+?)\\\]", r"$$\1$$", text, flags=re.DOTALL)

    # Normalise wikilinks: [[  Foo Bar  ]] → [[Foo Bar]]
    text = re.sub(r"\[\[\s+(.+?)\s+\]\]", r"[[\1]]", text)

    # Remove section numbering (e.g., "## 1. Introduction" → "## Introduction")
    text = re.sub(r"(#{1,4})\s+\d+[\.\)]\s+", r"\1 ", text)

    return text.strip()


def build_frontmatter(plan: dict, lang_code: str) -> str:
    """Build YAML frontmatter for the generated markdown file."""
    lang_name = LANGUAGES[lang_code]["name"]
    return (
        f"---\n"
        f"concept: {plan['concept_slug']}\n"
        f"canonical_name: \"{plan['canonical_name']}\"\n"
        f"subject: {plan.get('subject', '')}\n"
        f"grade: {plan['grade']}\n"
        f"language: {lang_code}\n"
        f"language_name: {lang_name}\n"
        f"page_depth: {plan.get('page_depth', 'standard')}\n"
        f"generated_at: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n"
        f"---\n\n"
    )


# ─── Index management ─────────────────────────────────────────────────────────

def load_index() -> dict:
    if INDEX_PATH.exists():
        try:
            return json.loads(INDEX_PATH.read_text())
        except Exception:
            pass
    return {"pages": {}}


def save_index(index: dict) -> None:
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2))


def update_index(index: dict, plan: dict, lang_code: str, out_path: Path) -> None:
    key = f"{plan['concept_slug']}_grade{plan['grade']}_{lang_code}"
    index["pages"][key] = {
        "concept_slug": plan["concept_slug"],
        "canonical_name": plan["canonical_name"],
        "subject": plan.get("subject", ""),
        "grade": plan["grade"],
        "language": lang_code,
        "path": str(out_path.relative_to(BASE_DIR)),
        "page_depth": plan.get("page_depth", "standard"),
        "prerequisites": plan.get("prerequisites_to_link", []),
        "leads_to": plan.get("successors_to_link", []),
    }


# ─── Single page generator ────────────────────────────────────────────────────

def generate_page(
    client: openai.OpenAI,
    model: str,
    plan: dict,
    lang_code: str,
    index: dict,
    skip_existing: bool,
) -> bool:
    """
    Generate one page for (plan, language). Returns True if generated (or already exists).
    """
    slug = plan["concept_slug"]
    grade = plan["grade"]
    lang_dir = OUTPUT_DIR / lang_code
    lang_dir.mkdir(parents=True, exist_ok=True)
    out_path = lang_dir / f"{slug}_grade{grade}.md"

    if skip_existing and out_path.exists():
        log.debug("Skip existing: %s", out_path)
        return True

    log.info("  Generating %s | grade=%d | lang=%s", plan["canonical_name"], grade, lang_code)

    prompt = build_generation_prompt(plan, lang_code)
    article_text = llm_call(
        client, model, SYSTEM_GENERATOR, prompt,
        temperature=0.7, max_tokens=4096
    )
    article_text = postprocess_article(article_text, lang_code)

    full_content = build_frontmatter(plan, lang_code) + article_text
    out_path.write_text(full_content, encoding="utf-8")

    update_index(index, plan, lang_code, out_path)
    return True


# ─── Smoke test ───────────────────────────────────────────────────────────────

def smoke_test(text: str, plan: dict) -> list[str]:
    """Basic quality checks on a generated article. Returns list of issues."""
    issues: list[str] = []

    # Must have a lead paragraph (non-heading text before first ##)
    lines = text.splitlines()
    heading_idx = next((i for i, l in enumerate(lines) if l.startswith("##")), None)
    if heading_idx == 0:
        issues.append("No lead paragraph before first heading")

    # Must have a See Also section
    if "See Also" not in text and "यह भी देखें" not in text and "ఇవి కూడా" not in text and "ଆହୁରି" not in text:
        issues.append("Missing See Also section")

    # Must have at least one wikilink
    if not re.search(r"\[\[.+?\]\]", text):
        issues.append("No wikilinks found")

    # Math concepts should have at least one LaTeX expression
    math_subjects = {"maths", "physics", "chemistry"}
    if plan.get("subject") in math_subjects and "grade" in plan and plan["grade"] >= 9:
        if not re.search(r"\$", text):
            issues.append("Math concept with no LaTeX expressions")

    return issues


# ─── Main runner ──────────────────────────────────────────────────────────────

def run(
    client: openai.OpenAI,
    model: str,
    plan_files: list[Path],
    languages: list[str],
    skip_existing: bool,
    test_mode: bool,
) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index = load_index()

    generated = 0
    skipped = 0
    failed = 0

    for plan_path in plan_files:
        try:
            plan = json.loads(plan_path.read_text())
        except Exception as exc:
            log.error("Cannot read plan %s: %s", plan_path, exc)
            continue

        for lang_code in languages:
            out_path = OUTPUT_DIR / lang_code / f"{plan['concept_slug']}_grade{plan['grade']}.md"

            if skip_existing and out_path.exists():
                skipped += 1
                continue

            try:
                success = generate_page(client, model, plan, lang_code, index, skip_existing=False)
                if success:
                    generated += 1
                    # Smoke-test in English
                    if lang_code == "en" and test_mode:
                        content = out_path.read_text()
                        issues = smoke_test(content, plan)
                        if issues:
                            log.warning("Smoke test issues in %s: %s", out_path.name, issues)
            except Exception as exc:
                log.error("Failed %s lang=%s: %s", plan_path.stem, lang_code, exc)
                failed += 1

    save_index(index)
    log.info(
        "Generation complete: %d pages generated, %d skipped, %d failed",
        generated, skipped, failed,
    )
    log.info("Index saved: %s (%d total entries)", INDEX_PATH, len(index["pages"]))


# ─── CLI ──────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="Stage 4 — Generate Wikipedia-style pages via Sarvam API")
    p.add_argument("--concept", help="Process only this concept slug")
    p.add_argument("--grade", type=int, help="Process only this grade")
    p.add_argument("--subject", help="Filter by subject")
    p.add_argument(
        "--languages",
        default="en,hi,te,od",
        help="Comma-separated language codes (default: en,hi,te,od)",
    )
    p.add_argument(
        "--model",
        default="sarvam-30b",
        help="Model for final generation (default: sarvam-30b)",
    )
    p.add_argument("--base-url", default="https://api.sarvam.ai/v1")
    p.add_argument("--api-key", default=os.environ.get("SARVAM_API_KEY", ""))
    p.add_argument("--plans-dir", default=str(PLANS_DIR))
    p.add_argument("--skip-existing", action="store_true", default=True)
    p.add_argument("--no-skip-existing", dest="skip_existing", action="store_false")
    p.add_argument("--test", action="store_true", help="Run smoke tests on generated content")
    return p.parse_args()


def main() -> None:
    args = parse_args()
    if not args.api_key:
        log.error("Set SARVAM_API_KEY or pass --api-key.")
        sys.exit(1)

    plans_dir = Path(args.plans_dir)
    if not plans_dir.exists():
        log.error("Plans directory not found: %s — run content_planner.py first", plans_dir)
        sys.exit(1)

    # Collect plan files
    all_plans = sorted(plans_dir.glob("*.json"))
    if args.concept:
        all_plans = [p for p in all_plans if p.stem.startswith(args.concept)]
    if args.grade:
        all_plans = [p for p in all_plans if f"_grade{args.grade}.json" in p.name]
    if args.subject:
        # Filter by loading each plan's subject field (or use the graph)
        graph_path = GRAPH_PATH
        if graph_path.exists():
            graph = json.loads(graph_path.read_text())
            subject_slugs = {
                slug for slug, c in graph.get("concepts", {}).items()
                if c.get("subject") == args.subject
            }
            all_plans = [p for p in all_plans if any(p.stem.startswith(s) for s in subject_slugs)]

    if not all_plans:
        log.error("No content plans found matching filters.")
        sys.exit(1)

    log.info("Found %d content plan(s) to process", len(all_plans))

    languages = [lang.strip() for lang in args.languages.split(",")]
    invalid_langs = [l for l in languages if l not in LANGUAGES]
    if invalid_langs:
        log.error("Unknown language codes: %s. Valid: %s", invalid_langs, list(LANGUAGES.keys()))
        sys.exit(1)

    client = make_client(args.api_key, args.base_url)
    run(
        client,
        args.model,
        all_plans,
        languages,
        skip_existing=args.skip_existing,
        test_mode=args.test,
    )


if __name__ == "__main__":
    main()
