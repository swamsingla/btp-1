"""
translator.py — Translate generated educational content to Indian languages.

Supports 3 translation model families:
  1. ai4bharat/indictrans2-en-indic-1B  (indic1b, best for Indian langs, ~2 GB fp16)
  2. sarvamai/sarvam-translate           (sarvam, Gemma3-based, document-level, ~2.5 GB 4-bit)
  3. google/translategemma-4b-it         (tgemma, Google's translation model, ~2.5 GB 4-bit)

Target languages: Hindi, Telugu, Odia

LaTeX preservation: Text is split at LaTeX boundaries ($...$, $$...$$).
Only non-LaTeX text segments are sent to the translation model.
LaTeX is NEVER sent to the model, so no corruption can occur.

Usage:
  python translator.py test indic1b                              # Quick test IndicTrans2 1B
  python translator.py test sarvam                               # Quick test Sarvam Translate
  python translator.py test tgemma                               # Quick test TranslateGemma 4B
  python translator.py translate <grade> <ch> --model indic1b    # Translate with IndicTrans2
  python translator.py translate <grade> <ch> --model sarvam     # Translate with Sarvam
  python translator.py translate <grade> <ch> --model tgemma     # Translate with TranslateGemma
  python translator.py compare                                   # Compare all models side-by-side
"""

import json
import os
import re
import sys
import time
import gc
from pathlib import Path
from typing import List, Dict, Optional, Tuple

import torch

# ═══════════ LANGUAGE CONFIG ═══════════

LANGUAGES = {
    "hi": {"name": "Hindi",  "indic": "hin_Deva", "tgemma": "hi", "sarvam": "Hindi", "sarvam_api": "hi-IN"},
    "te": {"name": "Telugu", "indic": "tel_Telu", "tgemma": "te", "sarvam": "Telugu", "sarvam_api": "te-IN"},
    "od": {"name": "Odia",   "indic": "ory_Orya", "tgemma": "or", "sarvam": "Odia",   "sarvam_api": "od-IN"},
}

MODEL_ALIASES = {
    "indic1b":    "ai4bharat/indictrans2-en-indic-1B",
    "sarvam":     "sarvamai/sarvam-translate",
    "tgemma":     "google/translategemma-4b-it",
    "sarvam-api": "sarvamai/sarvam-translate:v1 (API)",
}

# API key for sarvam-api model — set via --api-key CLI flag or SARVAM_API_KEY env var
_sarvam_api_key = None  # str or None

DEFAULT_MODEL = "indic1b"

# ═══════════ MODEL LOADING ═══════════

_models = {}  # cache: model_key -> (model, tokenizer, extras)


def _free_gpu():
    """Free GPU memory."""
    gc.collect()
    if torch.cuda.is_available():
        torch.cuda.empty_cache()


def unload_model(model_key: str = None):
    """Unload model(s) from GPU to free VRAM."""
    global _models
    if model_key:
        if model_key in _models:
            del _models[model_key]
    else:
        _models.clear()
    _free_gpu()
    print(f"  GPU memory after unload: {torch.cuda.memory_allocated() // 1024**2} MB")


def load_indictrans(model_id: str = "ai4bharat/indictrans2-en-indic-1B") -> Tuple:
    """Load IndicTrans2 model (1B in fp16, ~2GB VRAM).
    
    NOTE: Requires transformers <= 4.45.x. Produces garbage output on transformers 5.x.
    If output looks wrong, downgrade: pip install transformers==4.39.3
    """
    key = "indictrans2"
    if key in _models:
        return _models[key]

    import transformers
    tv = transformers.__version__
    # Only hard-block on 5.x — confirmed incompatible (architecture cache format changed)
    if tv.startswith("5."):
        print(f"  ERROR: IndicTrans2 produces garbage output with transformers {tv}.")
        print(f"  Downgrade: pip install transformers==4.39.3")
        raise RuntimeError(f"IndicTrans2 incompatible with transformers {tv}")
    # Warn on 4.40+ (not tested, may work)
    major, minor = tv.split(".")[:2]
    if int(major) == 4 and int(minor) >= 40:
        print(f"  WARNING: IndicTrans2 was tested on 4.39.3. Current: {tv}. Output may degrade.")
        print(f"  If translations look wrong: pip install transformers==4.39.3")

    from transformers import AutoModelForSeq2SeqLM, AutoTokenizer

    print(f"  Loading {model_id}...")

    try:
        from IndicTransToolkit.processor import IndicProcessor
    except ImportError:
        print("  ERROR: IndicTransToolkit not installed.")
        print("  Run: pip install IndicTransToolkit")
        sys.exit(1)

    tokenizer = AutoTokenizer.from_pretrained(model_id, trust_remote_code=True)

    # Load in fp16 - fits in 4GB VRAM (~2GB for 1B model)
    model = AutoModelForSeq2SeqLM.from_pretrained(
        model_id,
        trust_remote_code=True,
        torch_dtype=torch.float16,
        device_map="auto",
        low_cpu_mem_usage=True,
    )

    processor = IndicProcessor(inference=True)

    print(f"  Loaded! VRAM: {torch.cuda.memory_allocated() // 1024**2} MB")
    _models[key] = (model, tokenizer, processor)
    return model, tokenizer, processor


def load_translategemma(model_id: str = "google/translategemma-4b-it") -> Tuple:
    """Load TranslateGemma 4B with 4-bit quantization."""
    key = "translategemma"
    if key in _models:
        return _models[key]

    from transformers import AutoModelForImageTextToText, AutoProcessor, BitsAndBytesConfig

    print(f"  Loading {model_id}...")

    processor = AutoProcessor.from_pretrained(model_id)

    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,
    )

    model = AutoModelForImageTextToText.from_pretrained(
        model_id,
        quantization_config=quant_config,
        device_map={"": 0},  # Force all on GPU — BnB 4-bit doesn't allow CPU offload
    )

    print(f"  Loaded! VRAM: {torch.cuda.memory_allocated() // 1024**2} MB")
    _models[key] = (model, processor, None)
    return model, processor, None


def load_sarvam(model_id: str = "sarvamai/sarvam-translate") -> Tuple:
    """Load Sarvam Translate (Gemma3-4B based, 4-bit quantized, ~2.5GB VRAM).
    
    NOTE: Requires transformers >= 4.50 (Gemma3 architecture added in 4.50).
    Upgrade: pip install "transformers>=4.50"
    """
    key = "sarvam"
    if key in _models:
        return _models[key]

    import transformers
    tv = transformers.__version__
    major, minor = tv.split(".")[:2]
    if int(major) < 4 or (int(major) == 4 and int(minor) < 50):
        print(f"  ERROR: Sarvam Translate requires transformers >= 4.50 (Gemma3 support).")
        print(f"  Current: {tv}. Upgrade: pip install transformers --upgrade")
        raise RuntimeError(f"Sarvam requires transformers >= 4.50, got {tv}")

    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    print(f"  Loading {model_id}...")

    tokenizer = AutoTokenizer.from_pretrained(model_id)

    quant_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.bfloat16,
        bnb_4bit_use_double_quant=True,
    )

    model = AutoModelForCausalLM.from_pretrained(
        model_id,
        quantization_config=quant_config,
        device_map={"": 0},  # Force all on GPU — BnB 4-bit doesn't allow CPU offload
        torch_dtype=torch.bfloat16,
    )

    print(f"  Loaded! VRAM: {torch.cuda.memory_allocated() // 1024**2} MB")
    _models[key] = (model, tokenizer, None)
    return model, tokenizer, None


# ═══════════ TRANSLATION FUNCTIONS ═══════════

def translate_indictrans(texts: List[str], tgt_lang_code: str,
                         model, tokenizer, processor,
                         max_length: int = 256) -> List[str]:
    """Translate a batch of texts using IndicTrans2 model."""
    if not texts:
        return []

    src_lang = "eng_Latn"

    results = []
    batch_size = 8
    for i in range(0, len(texts), batch_size):
        batch = texts[i:i + batch_size]
        # Filter out empty strings
        non_empty = [(j, t) for j, t in enumerate(batch) if t.strip()]
        if not non_empty:
            results.extend(batch)
            continue

        indices, actual_texts = zip(*non_empty)
        actual_texts = list(actual_texts)

        preprocessed = processor.preprocess_batch(
            actual_texts, src_lang=src_lang, tgt_lang=tgt_lang_code
        )
        inputs = tokenizer(
            preprocessed, truncation=True, padding="longest",
            return_tensors="pt", max_length=max_length
        ).to(model.device)

        with torch.no_grad():
            outputs = model.generate(
                **inputs,
                use_cache=True,
                min_length=0,
                max_length=max_length,
                num_beams=1,  # Use greedy decoding for memory efficiency
                do_sample=False,
            )

        decoded = tokenizer.batch_decode(
            outputs, skip_special_tokens=True,
            clean_up_tokenization_spaces=True
        )
        translations = processor.postprocess_batch(decoded, lang=tgt_lang_code)

        # Reconstruct batch with original positions
        batch_result = list(batch)
        for j, idx in enumerate(indices):
            if j < len(translations):
                batch_result[idx] = translations[j]
        results.extend(batch_result)

    return results


def translate_tgemma(texts: List[str], src_lang: str, tgt_lang: str,
                     model, processor) -> List[str]:
    """Translate texts one-by-one using TranslateGemma model."""
    if not texts:
        return []

    results = []
    for text in texts:
        if not text.strip():
            results.append(text)
            continue

        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "source_lang_code": src_lang,
                        "target_lang_code": tgt_lang,
                        "text": text,
                    }
                ],
            }
        ]

        try:
            inputs = processor.apply_chat_template(
                messages, tokenize=True, add_generation_prompt=True,
                return_dict=True, return_tensors="pt"
            ).to(model.device, dtype=torch.float16)
            input_len = len(inputs['input_ids'][0])

            with torch.inference_mode():
                generation = model.generate(
                    **inputs, max_new_tokens=512, do_sample=False
                )

            generation = generation[0][input_len:]
            decoded = processor.decode(generation, skip_special_tokens=True)
            results.append(decoded.strip())
        except Exception as e:
            print(f"\n    WARNING: TranslateGemma error for '{text[:50]}...': {e}")
            results.append(text)  # fallback to original

    return results


def translate_sarvam(texts: List[str], tgt_lang: str,
                     model, tokenizer) -> List[str]:
    """Translate texts using Sarvam Translate model (chat-based)."""
    if not texts:
        return []

    results = []
    for text in texts:
        if not text.strip():
            results.append(text)
            continue

        messages = [
            {"role": "system", "content": f"Translate the text below to {tgt_lang}. Preserve all formatting, markdown, and LaTeX math expressions exactly as they are."},
            {"role": "user", "content": text},
        ]

        try:
            input_text = tokenizer.apply_chat_template(
                messages, tokenize=False, add_generation_prompt=True
            )
            model_inputs = tokenizer(
                [input_text], return_tensors="pt"
            ).to(model.device)
            input_len = len(model_inputs['input_ids'][0])

            with torch.inference_mode():
                generated_ids = model.generate(
                    **model_inputs,
                    max_new_tokens=1024,
                    do_sample=True,
                    temperature=0.01,
                    num_return_sequences=1,
                )

            output_ids = generated_ids[0][input_len:].tolist()
            output_text = tokenizer.decode(output_ids, skip_special_tokens=True)
            results.append(output_text.strip())

            # Free intermediate tensors
            del model_inputs, generated_ids, output_ids
            _free_gpu()
        except Exception as e:
            print(f"\n    WARNING: Sarvam error for '{text[:50]}...': {e}")
            results.append(text)  # fallback to original
            _free_gpu()

    return results


def translate_sarvam_api(texts: List[str], tgt_lang_code: str, api_key: str) -> List[str]:
    """Translate texts via Sarvam cloud API — fast, no local GPU needed."""
    if not texts:
        return []

    try:
        from sarvamai import SarvamAI
    except ImportError:
        print("  ERROR: sarvamai package not installed. Run: pip install sarvamai")
        sys.exit(1)

    client = SarvamAI(api_subscription_key=api_key)
    results = []

    for text in texts:
        if not text.strip():
            results.append(text)
            continue
        # Retry up to 5 times on rate limit (429) with exponential backoff
        for attempt in range(5):
            try:
                response = client.text.translate(
                    input=text,
                    source_language_code="en-IN",
                    target_language_code=tgt_lang_code,
                    model="sarvam-translate:v1",
                )
                results.append(response.translated_text)
                time.sleep(0.3)  # 300ms between requests to stay under rate limit
                break
            except Exception as e:
                err_str = str(e)
                if "429" in err_str or "rate_limit" in err_str:
                    wait = 2 ** attempt  # 1, 2, 4, 8, 16 seconds
                    print(f"\n    Rate limit hit, waiting {wait}s...", end="", flush=True)
                    time.sleep(wait)
                else:
                    print(f"\n    WARNING: Sarvam API error for '{text[:50]}...': {e}")
                    results.append(text)
                    break
        else:
            # All retries exhausted
            print(f"\n    WARNING: Sarvam API failed after 5 retries for '{text[:50]}...'")
            results.append(text)

    return results


# ═══════════════════════════════════════════════════════════════
# LATEX-SAFE MARKDOWN TRANSLATION
#
# KEY INSIGHT: Never send LaTeX to the translation model.
# Instead split text into [text, latex, text, latex, text]
# segments, only translate the text parts, then reassemble.
# This way LaTeX can NEVER be corrupted.
# ═══════════════════════════════════════════════════════════════

# Combined pattern to split text at LaTeX boundaries.
# Matches $$...$$ first (greedy), then $...$ (non-greedy).
_LATEX_SPLIT = re.compile(r'(\$\$[^$]+\$\$|\$[^$]+\$)')

# Patterns that should NOT be translated (skip entire line)
_SKIP_PATTERNS = [
    re.compile(r'^\s*$'),                          # empty lines
    re.compile(r'^\s*---\s*$'),                     # horizontal rules
    re.compile(r'^\s*```'),                         # code fences
    re.compile(r'^\$\$.*\$\$\s*$'),                # display math on one line
    re.compile(r'^\s*!\['),                         # images
    re.compile(r'^\s*\[.*\]\(.*\)\s*$'),           # standalone links
]


def _should_skip(line: str) -> bool:
    """Check if a line should be kept as-is (not translated)."""
    for pat in _SKIP_PATTERNS:
        if pat.match(line):
            return True
    return False


def _is_display_math_block(line: str) -> bool:
    """Check if the line is a standalone display math line: $$...$$"""
    stripped = line.strip()
    return stripped.startswith('$$') and stripped.endswith('$$') and len(stripped) > 4


def _split_text_and_latex(text: str) -> List[Tuple[str, bool]]:
    """Split text into segments of (content, is_latex).

    Example: "Find $x^2$ and $y$" ->
        [("Find ", False), ("$x^2$", True), (" and ", False), ("$y$", True)]
    """
    segments = []
    last_end = 0

    for match in _LATEX_SPLIT.finditer(text):
        start, end = match.span()
        # Text before this LaTeX
        if start > last_end:
            segments.append((text[last_end:start], False))
        # The LaTeX itself
        segments.append((match.group(0), True))
        last_end = end

    # Remaining text after last LaTeX
    if last_end < len(text):
        segments.append((text[last_end:], False))

    return segments if segments else [(text, False)]


def _extract_markdown_prefix(line: str) -> Tuple[str, str]:
    """Extract markdown prefix (headers, bullets, etc.) from content."""
    # Headers: ## , ### , etc.
    m = re.match(r'^(#{1,6}\s+)', line)
    if m:
        return m.group(1), line[m.end():]

    # Blockquotes: >
    m = re.match(r'^(>\s*)', line)
    if m:
        return m.group(1), line[m.end():]

    # Bullet points: - , * , numbered 1.
    m = re.match(r'^(\s*[-*]\s+|\s*\d+\.\s+)', line)
    if m:
        return m.group(1), line[m.end():]

    # Emoji bullets: 🟢, 🟡, 🔴 etc
    m = re.match(r'^(\s*[\U0001F534\U0001F7E0\U0001F7E1\U0001F7E2\U0001F7E3\U0001F535]\s*)', line)
    if m:
        return m.group(1), line[m.end():]

    # Bold prefix like **Common Mistake:**
    m = re.match(r'^(\*\*[^*]+:\*\*\s*)', line)
    if m:
        return m.group(1), line[m.end():]

    return "", line


def translate_markdown(content: str, tgt_lang: str, model_key: str = None) -> str:
    """Translate markdown while perfectly preserving LaTeX and formatting.

    Strategy:
    1. Split into lines
    2. Skip non-translatable lines (math, empty, code fences, ...)
    3. For translatable lines: split into [text, latex, text, ...] segments
    4. ONLY translate the text segments — LaTeX NEVER touches the model
    5. Reassemble everything
    """
    if model_key is None:
        model_key = DEFAULT_MODEL

    lines = content.split('\n')
    result_lines = list(lines)  # copy; we'll overwrite translated lines

    # ── Phase 1: Collect text segments to translate ──
    # Each entry: (line_idx, prefix, segments)
    translatable_entries = []
    text_segments_flat = []  # flat list of text-only segments for batch translation
    # Map: (entry_idx, seg_idx) -> index in text_segments_flat
    seg_to_flat = {}

    in_math_block = False  # for multi-line $$ blocks

    for idx, line in enumerate(lines):
        stripped = line.strip()

        # Track multi-line display math blocks: $$ alone on a line
        if stripped == '$$':
            in_math_block = not in_math_block
            continue
        if in_math_block:
            continue

        if _should_skip(line):
            continue
        if _is_display_math_block(line):
            continue

        prefix, text = _extract_markdown_prefix(line)
        if not text.strip():
            continue

        # Split text into [text, latex, text, ...] segments
        segments = _split_text_and_latex(text)

        # Check if there's any meaningful translatable text
        text_only = ''.join(s for s, is_latex in segments if not is_latex).strip()
        if not text_only:
            continue
        # Skip if only digits/punctuation
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

    # ── Phase 2: Batch translate all text segments ──
    model_id = MODEL_ALIASES.get(model_key, model_key)

    print(f"  ({len(text_segments_flat)} text segments)", end="", flush=True)

    if model_key == "sarvam-api":
        api_key = _sarvam_api_key or os.environ.get("SARVAM_API_KEY", "")
        if not api_key:
            raise RuntimeError("Sarvam API key not set. Use --api-key flag or set SARVAM_API_KEY env var.")
        tgt_code = LANGUAGES[tgt_lang]["sarvam_api"]
        translated_flat = translate_sarvam_api(text_segments_flat, tgt_code, api_key)
    elif "indictrans" in model_id.lower():
        lang_code = LANGUAGES[tgt_lang]["indic"]
        model, tokenizer, processor = load_indictrans(model_id)
        translated_flat = translate_indictrans(
            text_segments_flat, lang_code, model, tokenizer, processor
        )
    elif "sarvam" in model_id.lower():
        tgt_name = LANGUAGES[tgt_lang]["sarvam"]
        model, tokenizer, _ = load_sarvam(model_id)
        translated_flat = translate_sarvam(
            text_segments_flat, tgt_name, model, tokenizer
        )
    else:
        # TranslateGemma
        tgt_code = LANGUAGES[tgt_lang]["tgemma"]
        model, processor, _ = load_translategemma(model_id)
        translated_flat = translate_tgemma(
            text_segments_flat, "en", tgt_code, model, processor
        )

    # ── Phase 3: Reassemble lines with proper spacing ──
    for entry_idx, (line_idx, prefix, segments) in enumerate(translatable_entries):
        rebuilt_parts = []
        prev_is_latex = False
        for seg_idx, (seg_text, is_latex) in enumerate(segments):
            if is_latex:
                # Keep LaTeX exactly as-is — it was never sent to model
                # Add space before LaTeX if previous text doesn't end with space/punctuation
                if rebuilt_parts and not rebuilt_parts[-1].rstrip().endswith((' ', '\t', '(', '[')):
                    text_before = rebuilt_parts[-1].rstrip()
                    if text_before and not text_before[-1] in ' \t([':
                        rebuilt_parts[-1] = rebuilt_parts[-1].rstrip() + ' '
                rebuilt_parts.append(seg_text)
                prev_is_latex = True
            elif (entry_idx, seg_idx) in seg_to_flat:
                flat_idx = seg_to_flat[(entry_idx, seg_idx)]
                if flat_idx < len(translated_flat):
                    trans_text = translated_flat[flat_idx]
                    # Add space after LaTeX if translated text doesn't start with space/punctuation
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


# ═══════════ CHAPTER TRANSLATION ═══════════

def translate_chapter(input_dir: str, output_base: str,
                       model_key: str = None,
                       langs: List[str] = None):
    """Translate all topic .md files in a chapter directory."""
    if model_key is None:
        model_key = DEFAULT_MODEL

    in_dir = Path(input_dir)
    if not in_dir.exists():
        print(f"ERROR: Input directory not found: {in_dir}")
        return

    langs = langs or list(LANGUAGES.keys())

    # Find all .md files (skip _index.json)
    md_files = sorted(in_dir.glob("*.md"))
    if not md_files:
        print(f"ERROR: No .md files found in {in_dir}")
        return

    # Load index for metadata
    index_file = in_dir / "_index.json"
    if index_file.exists():
        with open(index_file, 'r', encoding='utf-8') as f:
            index = json.load(f)
        grade = index.get("grade", "?")
        ch_num = index.get("chapter_number", "?")
        ch_title = index.get("chapter_title", "?")
    else:
        grade = ch_num = ch_title = "?"

    model_display = MODEL_ALIASES.get(model_key, model_key)
    model_label = model_key  # short label for output subdirectory

    print(f"\n{'='*60}")
    print(f"Translating: Grade {grade} Ch {ch_num}: {ch_title}")
    print(f"Model: {model_display}")
    print(f"Files: {len(md_files)} | Languages: {', '.join(LANGUAGES[l]['name'] for l in langs)}")
    print(f"{'='*60}\n")

    total_time = 0

    for lang_code in langs:
        lang_name = LANGUAGES[lang_code]["name"]
        print(f"\n--- {lang_name} ({lang_code}) ---")

        for md_file in md_files:
            print(f"  [{md_file.stem}]", end="", flush=True)
            start = time.time()

            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()

            translated = translate_markdown(content, lang_code, model_key)

            # Output: <output_base>/grade10/maths/chapter1/<model_label>/<lang>/file.md
            # We need to compute the relative path from standard output structure
            # input_dir is like: data/output/grade10/maths/chapter1
            # We want: data/output/grade10/maths/chapter1/<model_label>/<lang>/file.md
            out_dir = in_dir / model_label / lang_code
            out_dir.mkdir(parents=True, exist_ok=True)

            out_file = out_dir / md_file.name
            with open(out_file, 'w', encoding='utf-8') as f:
                f.write(translated)

            elapsed = time.time() - start
            total_time += elapsed
            print(f" ({elapsed:.1f}s)")

    unload_model()

    print(f"\nDone! Total translation time: {total_time:.1f}s")
    print(f"Output: {in_dir / model_label}")


# ═══════════ MODEL COMPARISON ═══════════

def compare_models(sample_text: str = None):
    """Compare both translation models side-by-side on the same text."""
    if sample_text is None:
        sample_text = (
            "The Fundamental Theorem of Arithmetic states that every integer "
            "greater than 1 can be expressed as a product of prime numbers in "
            "a unique way. For example, $12 = 2^2 \\times 3$ and "
            "$30 = 2 \\times 3 \\times 5$. This factorisation is unique."
        )

    print("=" * 70)
    print("TRANSLATION MODEL COMPARISON")
    print("=" * 70)
    print(f"\nSource (English):\n  {sample_text}\n")

    results = {}
    for model_key, model_name in MODEL_ALIASES.items():
        print(f"\n{'─'*50}")
        print(f"Model: {model_name}")
        print(f"{'─'*50}")

        try:
            for lang_code, lang_info in LANGUAGES.items():
                lang_name = lang_info["name"]
                start = time.time()

                translated = translate_markdown(
                    sample_text, lang_code, model_key
                )

                elapsed = time.time() - start
                print(f"  {lang_name}: {translated}")
                print(f"    ({elapsed:.1f}s)")

                results.setdefault(model_key, {})[lang_code] = translated
        except Exception as e:
            print(f"  ERROR: {e}")
            import traceback
            traceback.print_exc()

        unload_model()

    print(f"\nComparison complete!")
    return results


# ═══════════ QUICK TEST ═══════════

def quick_test(model_key: str = None):
    """Quick test of a translation model with diverse examples."""
    if model_key is None:
        model_key = DEFAULT_MODEL

    test_texts = [
        "The Pythagorean theorem states that $a^2 + b^2 = c^2$.",
        "## Introduction to Real Numbers",
        "Find the HCF of 96 and 404 by the prime factorisation method.",
        "**Common Mistake:** Students often forget to check all prime factors.",
        "Since the reduced fraction $\\dfrac{24}{36}$ simplifies to $\\dfrac{2}{3}$, the decimal is non-terminating.",
        "- 🟢 Easy: Compute $2 + 3$",
    ]

    model_name = MODEL_ALIASES.get(model_key, model_key)
    print(f"\n{'='*50}")
    print(f"Testing: {model_name}")
    print(f"{'='*50}")

    for lang_code, lang_info in LANGUAGES.items():
        print(f"\n  --- {lang_info['name']} ---")
        for text in test_texts:
            translated = translate_markdown(text, lang_code, model_key)
            print(f"  EN: {text}")
            print(f"  {lang_code.upper()}: {translated}")
            print()

    unload_model()


# ═══════════ CLI ═══════════

if __name__ == "__main__":
    base = Path(__file__).parent.parent

    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1].lower()

    if cmd == "test":
        model_key = sys.argv[2] if len(sys.argv) > 2 else None
        quick_test(model_key)

    elif cmd == "compare":
        compare_models()

    elif cmd == "translate":
        if len(sys.argv) < 4:
            print("Usage: python translator.py translate <grade> <chapter> [--model indic1b|sarvam|tgemma|all] [--lang hi|te|od] [--subject maths|science]")
            sys.exit(1)

        grade = int(sys.argv[2])
        ch = int(sys.argv[3])

        model_key = DEFAULT_MODEL
        if "--model" in sys.argv:
            idx = sys.argv.index("--model")
            model_key = sys.argv[idx + 1]

        # Parse --lang flag (comma-separated or single)
        lang_list = None
        if "--lang" in sys.argv:
            idx = sys.argv.index("--lang")
            lang_list = [l.strip() for l in sys.argv[idx + 1].split(",")]

        # Parse --api-key flag (for sarvam-api model)
        if "--api-key" in sys.argv:
            idx = sys.argv.index("--api-key")
            _sarvam_api_key = sys.argv[idx + 1]
        elif os.environ.get("SARVAM_API_KEY"):
            _sarvam_api_key = os.environ["SARVAM_API_KEY"]

        # Parse --subject flag (default: maths)
        subject = "maths"
        if "--subject" in sys.argv:
            idx = sys.argv.index("--subject")
            subject = sys.argv[idx + 1]

        # Support --model all to run all 3 models
        if model_key == "all":
            model_keys = list(MODEL_ALIASES.keys())
        else:
            model_keys = [model_key]

        # Find input directory (English content from content_gen.py)
        input_dir = base / "data" / "output" / f"grade{grade}" / subject / f"chapter{ch}"
        if not input_dir.exists():
            print(f"ERROR: No content found at {input_dir}")
            print("Run content_gen.py first to generate English content.")
            sys.exit(1)

        output_base = str(base / "data" / "output")
        for mk in model_keys:
            try:
                translate_chapter(str(input_dir), output_base, mk, langs=lang_list)
            except Exception as e:
                print(f"\nERROR with model {mk}: {e}")
                import traceback
                traceback.print_exc()
            unload_model()

    elif cmd == "batch":
        model_key = DEFAULT_MODEL
        if "--model" in sys.argv:
            idx = sys.argv.index("--model")
            model_key = sys.argv[idx + 1]

        if model_key == "all":
            batch_models = list(MODEL_ALIASES.keys())
        else:
            batch_models = [model_key]

        output_dir = base / "data" / "output"
        for grade_dir in sorted(output_dir.glob("grade*")):
            maths_dir = grade_dir / "maths"
            if not maths_dir.exists():
                continue
            for ch_dir in sorted(maths_dir.glob("chapter*")):
                md_files = list(ch_dir.glob("*.md"))
                if md_files:
                    for mk in batch_models:
                        try:
                            translate_chapter(str(ch_dir), str(output_dir), mk)
                        except Exception as e:
                            print(f"\nERROR with model {mk} for {ch_dir.name}: {e}")
                        unload_model()

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)
