#!/usr/bin/env python3
"""
Multilingual Content Generator — Sarvam API
=============================================
Generates educational content directly in 4 languages (English, Hindi,
Telugu, Odia) using Sarvam's OpenAI-compatible API. NO translation step.

Reads content plans from data/content_plans/ (produced by graph_rag.py)
and generates Wikipedia-style articles for each (concept, grade, language).

Output: data/generated_pages/{language}/{concept_slug}_grade{N}.md

Usage:
  python generate.py --api-key YOUR_KEY              # generate all
  python generate.py --grade 6 --languages en,hi     # grade 6, en + hi only
  python generate.py --concept fractions             # one concept, all langs
  python generate.py --dry-run                       # show what would be generated
  python generate.py --test                          # run smoke tests on output
"""

import argparse
import json
import logging
import os
import re
import sys
import time
from pathlib import Path

import openai

# ─── Paths ───────────────────────────────────────────────────────────────────
BASE_DIR = Path(__file__).resolve().parent.parent.parent
PLANS_DIR = BASE_DIR / "data" / "content_plans"
OUTPUT_DIR = BASE_DIR / "data" / "generated_pages"
INDEX_PATH = OUTPUT_DIR / "_index.json"

# ─── Language Configuration ──────────────────────────────────────────────────
LANGUAGES: dict[str, dict[str, str]] = {
    "en": {
        "name": "English",
        "instruction": "Write in clear, fluent English.",
        "see_also_label": "See Also",
        "prerequisites_label": "Prerequisites",
    },
    "hi": {
        "name": "Hindi",
        "instruction": (
            "Write entirely in Hindi (Devanagari script). Do not mix English prose. "
            "Technical mathematical terms may appear in brackets after the Hindi term "
            "on first use: e.g., जड़ (Root), भिन्न (Fraction). "
            "Keep all LaTeX expressions in English/Latin script."
        ),
        "see_also_label": "यह भी देखें",
        "prerequisites_label": "पूर्वापेक्षाएँ",
    },
    "te": {
        "name": "Telugu",
        "instruction": (
            "Write entirely in Telugu (Telugu script). Do not mix English prose. "
            "Technical terms may appear in brackets after the Telugu term on first use. "
            "Keep all LaTeX expressions in English/Latin script."
        ),
        "see_also_label": "ఇవి కూడా చూడండి",
        "prerequisites_label": "అవసరమైన అంశాలు",
    },
    "od": {
        "name": "Odia",
        "instruction": (
            "Write entirely in Odia (Odia script). Do not mix English prose. "
            "Technical terms may appear in brackets after the Odia term on first use. "
            "Keep all LaTeX expressions in English/Latin script."
        ),
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
log = logging.getLogger("generate")


# ══════════════════════════════════════════════════════════════════════════════
# LLM Client
# ══════════════════════════════════════════════════════════════════════════════

def make_client(api_key: str, base_url: str = "https://api.sarvam.ai/v1") -> openai.OpenAI:
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
    """Call the Sarvam API with exponential backoff on rate limits."""
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
            log.warning("Rate limit — waiting %ds (attempt %d/%d)", wait, attempt + 1, retries)
            time.sleep(wait)
        except openai.APIError as exc:
            log.error("API error: %s", exc)
            if attempt == retries - 1:
                raise
            time.sleep(10)
    raise RuntimeError("LLM call failed after all retries")


# ══════════════════════════════════════════════════════════════════════════════
# Prompt Builder
# ══════════════════════════════════════════════════════════════════════════════

SYSTEM_PROMPT = """You are an expert educational writer creating Wikipedia-style articles
for Indian school students studying NCERT Mathematics (Grades 6-12).
Your articles appear on an online learning platform serving students in English,
Hindi, Telugu, and Odia.

Quality standard: A student reading your article should fully understand the topic —
as well as someone who studied from the best textbooks (NCERT, RD Sharma, RS Aggarwal).

Formatting rules (STRICT):
1. Start with a lead paragraph defining the concept clearly and self-containedly.
2. Use ## for main sections, ### for subsections. NO numbered section headings.
3. Use LaTeX for ALL mathematics: $inline$ for in-text, $$displayed$$ for equations.
   Display math must be on its own line with blank lines before and after.
4. Link to related concepts using [[Concept Name]] notation (always use the English
   canonical name — the platform resolves these automatically).
5. Include at least 2 worked examples with step-by-step solutions.
6. Include a "Common Mistakes" section warning about typical student errors.
7. End with a "See Also" section listing prerequisites, next topics, and related
   concepts as [[wikilinks]].
8. The article MUST be fully self-contained — the student should not need the textbook.
9. Keep LaTeX expressions in English/Latin script even when writing in other languages."""


def build_prompt(plan: dict, lang_code: str) -> str:
    """Build the user prompt from a content plan."""
    lang = LANGUAGES[lang_code]

    # Prerequisites with descriptions (so the model knows what students already know)
    prereq_descs = plan.get("prerequisites_descriptions", {})
    if plan.get("prerequisites_to_link"):
        prereq_lines = []
        for name in plan["prerequisites_to_link"]:
            desc = prereq_descs.get(name, "")
            if desc:
                prereq_lines.append(f"  - [[{name}]]: {desc}")
            else:
                prereq_lines.append(f"  - [[{name}]]")
        prereq_str = "\n".join(prereq_lines)
    else:
        prereq_str = "  (none — this is a foundational concept)"

    # Successors
    successors = plan.get("successors_to_link", [])
    next_str = "\n".join(f"  - [[{s}]]" for s in successors) if successors else "  (none)"

    # Related
    related = plan.get("related_to_link", [])
    related_str = "\n".join(f"  - [[{r}]]" for r in related) if related else "  (none)"

    # All see-also links (deduplicated)
    all_see_also = list(dict.fromkeys(plan.get("see_also", [])))
    see_also_str = "\n".join(f"  - [[{s}]]" for s in all_see_also[:12]) if all_see_also else "  (none)"

    # Sections
    sections_str = "\n".join(f"  - {s}" for s in plan.get("sections", []))

    # Aliases
    aliases = plan.get("aliases", [])
    alias_str = f"\nAlso known as: {', '.join(aliases)}" if aliases else ""

    return f"""ARTICLE TO WRITE: {plan['canonical_name']}{alias_str}
MATHEMATICAL AREA: {plan.get('area', '')}
GRADE LEVEL: Grade {plan['grade']}
DESCRIPTION: {plan.get('description', '')}

LANGUAGE INSTRUCTION: {lang['instruction']}

GRADE-APPROPRIATE DEPTH:
{plan.get('grade_note', '')}

KNOWLEDGE GRAPH CONTEXT:
Prerequisites (student has already studied these — reference without re-explaining):
{prereq_str}

What this concept enables (briefly foreshadow where appropriate):
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


# ══════════════════════════════════════════════════════════════════════════════
# Post-processing
# ══════════════════════════════════════════════════════════════════════════════

def postprocess(text: str) -> str:
    """Clean and standardise generated article markdown."""
    # Strip code fences wrapping entire article
    text = re.sub(r"^```(?:markdown)?\s*\n", "", text)
    text = re.sub(r"\n```\s*$", "", text)

    # Normalise LaTeX delimiters
    text = re.sub(r"\\\((.+?)\\\)", r"$\1$", text)
    text = re.sub(r"\\\[(.+?)\\\]", r"$$\1$$", text, flags=re.DOTALL)

    # Normalise wikilinks whitespace
    text = re.sub(r"\[\[\s+(.+?)\s+\]\]", r"[[\1]]", text)

    # Remove numbered section headings
    text = re.sub(r"(#{1,4})\s+\d+[\.)\-]\s+", r"\1 ", text)

    return text.strip()


def build_frontmatter(plan: dict, lang_code: str) -> str:
    """Build YAML frontmatter for the generated markdown."""
    return (
        f"---\n"
        f"concept: {plan['concept_slug']}\n"
        f"canonical_name: \"{plan['canonical_name']}\"\n"
        f"subject: {plan.get('subject', 'maths')}\n"
        f"area: \"{plan.get('area', '')}\"\n"
        f"grade: {plan['grade']}\n"
        f"language: {lang_code}\n"
        f"language_name: {LANGUAGES[lang_code]['name']}\n"
        f"generated_at: {time.strftime('%Y-%m-%dT%H:%M:%SZ', time.gmtime())}\n"
        f"---\n\n"
    )


# ══════════════════════════════════════════════════════════════════════════════
# Quality Checks
# ══════════════════════════════════════════════════════════════════════════════

def smoke_test(text: str, plan: dict) -> list[str]:
    """Basic quality checks on generated content."""
    issues: list[str] = []

    lines = text.splitlines()
    # Lead paragraph before first heading
    heading_idx = next((i for i, l in enumerate(lines) if l.startswith("##")), None)
    if heading_idx == 0:
        issues.append("No lead paragraph before first heading")

    # Must have See Also section
    if not re.search(r"See Also|यह भी देखें|ఇవి కూడా|ଆହୁରି", text):
        issues.append("Missing See Also section")

    # Must have at least one wikilink
    if not re.search(r"\[\[.+?\]\]", text):
        issues.append("No wikilinks found")

    # Should have LaTeX for grade 7+
    if plan.get("grade", 6) >= 7 and not re.search(r"\$", text):
        issues.append("No LaTeX expressions found (expected for grade 7+)")

    # Minimum length check
    if len(text) < 300:
        issues.append(f"Content too short ({len(text)} chars)")

    return issues


# ══════════════════════════════════════════════════════════════════════════════
# Index Management
# ══════════════════════════════════════════════════════════════════════════════

def load_index() -> dict:
    if INDEX_PATH.exists():
        try:
            return json.loads(INDEX_PATH.read_text(encoding="utf-8"))
        except Exception:
            pass
    return {"pages": {}, "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}


def save_index(index: dict) -> None:
    index["updated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    INDEX_PATH.write_text(json.dumps(index, ensure_ascii=False, indent=2), encoding="utf-8")


# ══════════════════════════════════════════════════════════════════════════════
# Single Page Generator
# ══════════════════════════════════════════════════════════════════════════════

def generate_page(
    client: openai.OpenAI,
    model: str,
    plan: dict,
    lang_code: str,
) -> Path:
    """Generate one page for (plan, language). Returns the output path."""
    slug = plan["concept_slug"]
    grade = plan["grade"]
    lang_dir = OUTPUT_DIR / lang_code
    lang_dir.mkdir(parents=True, exist_ok=True)
    out_path = lang_dir / f"{slug}_grade{grade}.md"

    log.info("  %-40s grade=%-2d lang=%s", plan["canonical_name"], grade, lang_code)

    prompt = build_prompt(plan, lang_code)
    article = llm_call(client, model, SYSTEM_PROMPT, prompt,
                       temperature=0.7, max_tokens=4096)
    article = postprocess(article)

    full_content = build_frontmatter(plan, lang_code) + article
    out_path.write_text(full_content, encoding="utf-8")

    return out_path


# ══════════════════════════════════════════════════════════════════════════════
# Main Runner
# ══════════════════════════════════════════════════════════════════════════════

def run(
    client: openai.OpenAI,
    model: str,
    plan_files: list[Path],
    languages: list[str],
    *,
    skip_existing: bool = True,
    test_mode: bool = False,
    dry_run: bool = False,
) -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    index = load_index()

    generated = 0
    skipped = 0
    failed = 0
    smoke_issues: list[str] = []

    total_tasks = len(plan_files) * len(languages)
    log.info("Processing %d plans × %d languages = %d pages", len(plan_files), len(languages), total_tasks)

    for plan_path in plan_files:
        try:
            plan = json.loads(plan_path.read_text(encoding="utf-8"))
        except Exception as exc:
            log.error("Cannot read plan %s: %s", plan_path, exc)
            continue

        for lang_code in languages:
            slug = plan["concept_slug"]
            grade = plan["grade"]
            out_path = OUTPUT_DIR / lang_code / f"{slug}_grade{grade}.md"

            if skip_existing and out_path.exists():
                skipped += 1
                continue

            if dry_run:
                log.info("  [DRY-RUN] Would generate: %s grade=%d lang=%s",
                         plan["canonical_name"], grade, lang_code)
                continue

            try:
                result_path = generate_page(client, model, plan, lang_code)

                # Update index
                key = f"{slug}_grade{grade}_{lang_code}"
                index["pages"][key] = {
                    "concept_slug": slug,
                    "canonical_name": plan["canonical_name"],
                    "grade": grade,
                    "language": lang_code,
                    "area": plan.get("area", ""),
                    "path": str(result_path.relative_to(BASE_DIR)),
                    "prerequisites": plan.get("prerequisites_to_link", []),
                    "leads_to": plan.get("successors_to_link", []),
                }
                generated += 1

                # Smoke test
                if test_mode:
                    content = result_path.read_text(encoding="utf-8")
                    issues = smoke_test(content, plan)
                    if issues:
                        msg = f"{result_path.name}: {issues}"
                        smoke_issues.append(msg)
                        log.warning("  Smoke: %s", msg)

                # Save index periodically
                if generated % 10 == 0:
                    save_index(index)

            except Exception as exc:
                log.error("Failed %s lang=%s: %s", slug, lang_code, exc)
                failed += 1

    save_index(index)
    log.info("═" * 60)
    log.info("Generation complete:")
    log.info("  Generated: %d", generated)
    log.info("  Skipped:   %d (already existed)", skipped)
    log.info("  Failed:    %d", failed)
    log.info("  Index:     %s (%d total entries)", INDEX_PATH, len(index["pages"]))
    if smoke_issues:
        log.warning("  Smoke test issues: %d", len(smoke_issues))


# ══════════════════════════════════════════════════════════════════════════════
# CLI
# ══════════════════════════════════════════════════════════════════════════════

def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(
        description="Multilingual Content Generator — direct generation via Sarvam API",
    )
    p.add_argument("--concept", help="Process only this concept slug")
    p.add_argument("--grade", type=int, help="Process only this grade")
    p.add_argument(
        "--languages", default="en,hi,te,od",
        help="Comma-separated language codes (default: en,hi,te,od)",
    )
    p.add_argument("--model", default="sarvam-m", help="Model name (default: sarvam-m)")
    p.add_argument("--base-url", default="https://api.sarvam.ai/v1")
    p.add_argument("--api-key", default=os.environ.get("SARVAM_API_KEY", ""))
    p.add_argument("--plans-dir", default=str(PLANS_DIR))
    p.add_argument("--skip-existing", action="store_true", default=True)
    p.add_argument("--no-skip-existing", dest="skip_existing", action="store_false")
    p.add_argument("--test", action="store_true", help="Run smoke tests on generated content")
    p.add_argument("--dry-run", action="store_true", help="Show what would be generated without calling API")
    return p.parse_args()


def main() -> None:
    args = parse_args()

    if not args.dry_run and not args.api_key:
        log.error("Set SARVAM_API_KEY env var or pass --api-key")
        sys.exit(1)

    plans_dir = Path(args.plans_dir)
    if not plans_dir.exists():
        log.error("Plans directory not found: %s — run graph_rag.py first", plans_dir)
        sys.exit(1)

    # Collect plan files
    all_plans = sorted(plans_dir.glob("*.json"))
    if args.concept:
        all_plans = [p for p in all_plans if args.concept in p.stem]
    if args.grade:
        all_plans = [p for p in all_plans if f"_grade{args.grade}" in p.name]
    if not all_plans:
        log.error("No content plans found matching filters.")
        sys.exit(1)

    log.info("Found %d content plan(s)", len(all_plans))

    # Validate languages
    languages = [lang.strip() for lang in args.languages.split(",")]
    invalid = [l for l in languages if l not in LANGUAGES]
    if invalid:
        log.error("Unknown language codes: %s. Valid: %s", invalid, list(LANGUAGES.keys()))
        sys.exit(1)

    client = make_client(args.api_key, args.base_url) if not args.dry_run else None
    run(
        client,
        args.model,
        all_plans,
        languages,
        skip_existing=args.skip_existing,
        test_mode=args.test,
        dry_run=args.dry_run,
    )


if __name__ == "__main__":
    main()
