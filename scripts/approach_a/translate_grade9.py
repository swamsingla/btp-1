"""
translate_grade9.py — Translate Grade 9 Ch1 using Sarvam API with consistent terminology.

Strategy for consistent term translation:
1. Define a glossary of key mathematical terms for the chapter
2. Translate each term ONCE via Sarvam API
3. Before sending text to translation, replace terms with placeholders
4. After translation, substitute placeholders with the pre-translated terms

This ensures terms like "rational number", "irrational number" etc. always
get the same translation across all topics.

Usage:
    python scripts/translate_grade9.py --lang hi
    python scripts/translate_grade9.py --lang hi,te
"""

import json
import os
import re
import sys
import time
from pathlib import Path
from typing import List, Dict, Tuple

# ═══════════ CONFIG ═══════════

ROOT = Path(__file__).parent.parent

LANGUAGES = {
    "hi": {"name": "Hindi", "code": "hi-IN"},
    "te": {"name": "Telugu", "code": "te-IN"},
    "od": {"name": "Odia", "code": "od-IN"},
}

# Key mathematical terms for Grade 9 Chapter 1: Number Systems
# These MUST be translated consistently across all topics
CHAPTER_TERMS = [
    # Core concepts
    "natural numbers",
    "whole numbers",
    "integers",
    "rational numbers",
    "irrational numbers",
    "real numbers",
    "number line",
    "number system",
    # Operations & properties
    "decimal expansion",
    "terminating decimal",
    "non-terminating decimal",
    "recurring decimal",
    "non-recurring decimal",
    "prime factorisation",
    "rationalisation",
    "denominator",
    "numerator",
    # Exponents
    "exponent",
    "laws of exponents",
    "rational exponent",
    "base",
    "power",
    # Key phrases
    "successive magnification",
    "closure property",
    "commutative property",
    "associative property",
    "distributive property",
    "identity element",
    "inverse element",
    "square root",
    "cube root",
]


def get_sarvam_client():
    """Initialize Sarvam API client."""
    from sarvamai import SarvamAI

    api_key = os.environ.get("SARVAM_API_KEY", "")
    if not api_key:
        env_file = ROOT / "webapp" / ".env.local"
        if env_file.exists():
            for line in env_file.read_text().splitlines():
                if line.startswith("SARVAM_API_KEY="):
                    api_key = line.split("=", 1)[1].strip()
                    break
    if not api_key:
        print("ERROR: SARVAM_API_KEY not found. Set env var or add to webapp/.env.local")
        sys.exit(1)

    return SarvamAI(api_subscription_key=api_key)


def build_glossary(client, terms: List[str], tgt_lang_code: str) -> Dict[str, str]:
    """Translate all terms once to build a consistent glossary."""
    glossary = {}
    print(f"\n  Building glossary ({len(terms)} terms)...")

    for term in terms:
        for attempt in range(3):
            try:
                response = client.text.translate(
                    input=term,
                    source_language_code="en-IN",
                    target_language_code=tgt_lang_code,
                    model="sarvam-translate:v1",
                    mode="formal",
                    numerals_format="international",
                )
                translated = response.translated_text.strip()
                glossary[term] = translated
                time.sleep(0.3)
                break
            except Exception as e:
                if "429" in str(e):
                    time.sleep(2 ** attempt)
                else:
                    print(f"    WARNING: Failed to translate '{term}': {e}")
                    glossary[term] = term  # fallback to English
                    break

    # Print glossary
    print(f"  Glossary ({len(glossary)} terms):")
    for en, tr in sorted(glossary.items()):
        print(f"    {en} → {tr}")

    return glossary


# ═══════════ LATEX-SAFE TRANSLATION ═══════════

_LATEX_SPLIT = re.compile(r'(\$\$[^$]+\$\$|\$[^$]+\$)')

_SKIP_PATTERNS = [
    re.compile(r'^\s*$'),
    re.compile(r'^\s*---\s*$'),
    re.compile(r'^\s*```'),
    re.compile(r'^\$\$.*\$\$\s*$'),
    re.compile(r'^\s*!\['),
    re.compile(r'^\s*\[.*\]\(.*\)\s*$'),
]


def _should_skip(line: str) -> bool:
    for pat in _SKIP_PATTERNS:
        if pat.match(line):
            return True
    return False


def _split_text_and_latex(text: str) -> List[Tuple[str, bool]]:
    segments = []
    last_end = 0
    for match in _LATEX_SPLIT.finditer(text):
        start, end = match.span()
        if start > last_end:
            segments.append((text[last_end:start], False))
        segments.append((match.group(0), True))
        last_end = end
    if last_end < len(text):
        segments.append((text[last_end:], False))
    return segments if segments else [(text, False)]


def _extract_markdown_prefix(line: str) -> Tuple[str, str]:
    m = re.match(r'^(#{1,6}\s+)', line)
    if m:
        return m.group(1), line[m.end():]
    m = re.match(r'^(>\s*)', line)
    if m:
        return m.group(1), line[m.end():]
    m = re.match(r'^(\s*[-*]\s+|\s*\d+\.\s+)', line)
    if m:
        return m.group(1), line[m.end():]
    m = re.match(r'^(\s*[\U0001F534\U0001F7E0\U0001F7E1\U0001F7E2\U0001F7E3\U0001F535]\s*)', line)
    if m:
        return m.group(1), line[m.end():]
    m = re.match(r'^(\*\*[^*]+:\*\*\s*)', line)
    if m:
        return m.group(1), line[m.end():]
    return "", line


def translate_with_glossary(client, text: str, tgt_lang_code: str,
                             glossary: Dict[str, str]) -> str:
    """Translate text using Sarvam API with glossary-based consistency.

    Strategy:
    1. In the source text, replace glossary terms with 'TERM_N' placeholders
    2. Send to Sarvam for translation
    3. Replace placeholders in translated text with pre-translated terms
    """
    if not text.strip():
        return text

    # Sort terms by length (longest first) to avoid partial matches
    sorted_terms = sorted(glossary.keys(), key=len, reverse=True)

    # Build placeholder map
    placeholders = {}
    modified_text = text
    for i, term in enumerate(sorted_terms):
        placeholder = f"GTERM{i:03d}"
        # Case-insensitive replacement but preserve surrounding spacing
        pattern = re.compile(re.escape(term), re.IGNORECASE)
        if pattern.search(modified_text):
            modified_text = pattern.sub(placeholder, modified_text)
            placeholders[placeholder] = glossary[term]

    # Translate the modified text
    for attempt in range(3):
        try:
            response = client.text.translate(
                input=modified_text,
                source_language_code="en-IN",
                target_language_code=tgt_lang_code,
                model="sarvam-translate:v1",
                mode="formal",
                numerals_format="international",
            )
            translated = response.translated_text
            break
        except Exception as e:
            if "429" in str(e):
                time.sleep(2 ** attempt)
            else:
                print(f"\n    WARNING: Translation failed: {e}")
                return text
    else:
        return text

    # Replace placeholders with glossary translations
    for placeholder, translation in placeholders.items():
        translated = translated.replace(placeholder, translation)

    return translated


def translate_markdown_with_glossary(content: str, tgt_lang_code: str,
                                      client, glossary: Dict[str, str]) -> str:
    """Translate markdown while preserving LaTeX and using glossary for consistency."""
    lines = content.split('\n')
    result_lines = list(lines)

    translatable_entries = []
    text_segments_flat = []
    seg_to_flat = {}

    in_math_block = False

    for idx, line in enumerate(lines):
        stripped = line.strip()
        if stripped == '$$':
            in_math_block = not in_math_block
            continue
        if in_math_block:
            continue
        if _should_skip(line):
            continue
        if stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4:
            continue

        prefix, text = _extract_markdown_prefix(line)
        if not text.strip():
            continue

        segments = _split_text_and_latex(text)
        text_only = ''.join(s for s, is_latex in segments if not is_latex).strip()
        if not text_only:
            continue
        if re.match(r'^[\d\s\.,;:!?()\-–—|/\\]+$', text_only):
            continue

        entry_idx = len(translatable_entries)
        translatable_entries.append((idx, prefix, segments))

        for seg_idx, (seg_text, is_latex) in enumerate(segments):
            if not is_latex and seg_text.strip():
                seg_to_flat[(entry_idx, seg_idx)] = len(text_segments_flat)
                text_segments_flat.append(seg_text)

    if not text_segments_flat:
        return content

    print(f" ({len(text_segments_flat)} segments)", end="", flush=True)

    # Translate all segments using glossary
    translated_flat = []
    for seg in text_segments_flat:
        translated = translate_with_glossary(client, seg, tgt_lang_code, glossary)
        translated_flat.append(translated)
        time.sleep(0.3)

    # Reassemble
    for entry_idx, (line_idx, prefix, segments) in enumerate(translatable_entries):
        rebuilt_parts = []
        prev_is_latex = False
        for seg_idx, (seg_text, is_latex) in enumerate(segments):
            if is_latex:
                if rebuilt_parts and not rebuilt_parts[-1].rstrip().endswith((' ', '\t', '(', '[')):
                    text_before = rebuilt_parts[-1].rstrip()
                    if text_before and text_before[-1] not in ' \t([':
                        rebuilt_parts[-1] = rebuilt_parts[-1].rstrip() + ' '
                rebuilt_parts.append(seg_text)
                prev_is_latex = True
            elif (entry_idx, seg_idx) in seg_to_flat:
                flat_idx = seg_to_flat[(entry_idx, seg_idx)]
                if flat_idx < len(translated_flat):
                    trans_text = translated_flat[flat_idx]
                    if prev_is_latex and trans_text and trans_text[0] not in ' \t,.;:!?)]\n':
                        trans_text = ' ' + trans_text.lstrip()
                    rebuilt_parts.append(trans_text)
                else:
                    rebuilt_parts.append(seg_text)
                prev_is_latex = False
            else:
                rebuilt_parts.append(seg_text)
                prev_is_latex = False

        result_lines[line_idx] = prefix + ''.join(rebuilt_parts)

    return '\n'.join(result_lines)


def translate_chapter(grade: int, chapter: int, lang_codes: List[str],
                       subject: str = "maths"):
    """Translate a full chapter with consistent glossary-based translation."""
    input_dir = ROOT / "data" / "output" / f"grade{grade}" / subject / f"chapter{chapter}"
    if not input_dir.exists():
        print(f"ERROR: no content at {input_dir}")
        sys.exit(1)

    md_files = sorted(input_dir.glob("*.md"))
    if not md_files:
        print(f"ERROR: No .md files in {input_dir}")
        sys.exit(1)

    # Also translate chapter intro if it exists
    intro_file = input_dir / "_chapter_intro.txt"

    print(f"\n{'='*60}")
    print(f"Translating: Grade {grade} Ch {chapter}")
    print(f"Files: {len(md_files)} topics")
    print(f"Languages: {', '.join(LANGUAGES[l]['name'] for l in lang_codes)}")
    print(f"{'='*60}")

    client = get_sarvam_client()
    total_time = 0

    for lang_code in lang_codes:
        lang_name = LANGUAGES[lang_code]["name"]
        tgt_code = LANGUAGES[lang_code]["code"]
        print(f"\n--- {lang_name} ({lang_code}) ---")

        # Build glossary for this language
        glossary = build_glossary(client, CHAPTER_TERMS, tgt_code)

        # Save glossary for reference
        out_dir = input_dir / "sarvam-api" / lang_code
        out_dir.mkdir(parents=True, exist_ok=True)

        glossary_file = out_dir / "_glossary.json"
        with open(glossary_file, 'w', encoding='utf-8') as f:
            json.dump(glossary, f, ensure_ascii=False, indent=2)
        print(f"  Glossary saved to {glossary_file}")

        # Translate chapter intro
        if intro_file.exists():
            print(f"  [chapter_intro]", end="", flush=True)
            start = time.time()
            intro_text = intro_file.read_text(encoding='utf-8')
            translated_intro = translate_with_glossary(client, intro_text, tgt_code, glossary)
            (out_dir / "_chapter_intro.txt").write_text(translated_intro, encoding='utf-8')
            elapsed = time.time() - start
            total_time += elapsed
            print(f" ({elapsed:.1f}s)")

        # Translate each topic
        for md_file in md_files:
            print(f"  [{md_file.stem}]", end="", flush=True)
            start = time.time()

            content = md_file.read_text(encoding='utf-8')
            translated = translate_markdown_with_glossary(content, tgt_code, client, glossary)

            out_file = out_dir / md_file.name
            out_file.write_text(translated, encoding='utf-8')

            elapsed = time.time() - start
            total_time += elapsed
            print(f" ({elapsed:.1f}s)")

    print(f"\nDone! Total time: {total_time:.1f}s")
    print(f"Output: {input_dir / 'sarvam-api'}")


if __name__ == "__main__":
    lang_list = ["hi"]  # Default to Hindi

    if "--lang" in sys.argv:
        idx = sys.argv.index("--lang")
        lang_list = [l.strip() for l in sys.argv[idx + 1].split(",")]

    translate_chapter(grade=9, chapter=1, lang_codes=lang_list)
