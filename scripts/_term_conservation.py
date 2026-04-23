#!/usr/bin/env python3
"""
Per-page technical term conservation extractor using Qwen3-8B.
Runs ON gnode047. Reads .md topic files and extracts detailed technical terms
that must be conserved (kept consistent) during translation.

For each page/topic, produces:
  - mathematical_terms: core math vocabulary (e.g. "polynomial", "coefficient")
  - theorems_and_laws: named theorems/properties (e.g. "Remainder Theorem")
  - notation_terms: standard notation references (e.g. "p(x)", "degree")
  - formulas: key formulas that should be preserved as-is
  - domain_phrases: multi-word domain phrases (e.g. "non-terminating recurring decimal")

Usage:
  python3 _term_conservation.py <input_json> <output_json>

  input_json: {"chapter1/1.1_Introduction.md": "<full md content>", ...}
  output_json: per-page categorized term lists
"""
import gc
import json
import os
import re
import sys
from pathlib import Path

import torch

MODEL_ID = "Qwen/Qwen3-8B"
HF_HOME = os.environ.get("HF_HOME", "/ssd_scratch/shubhamcvit/venv/hf_models")

CONSERVATION_PROMPT = """\
You are an expert mathematics educator and translator. Analyze the following educational content and extract ALL technical terms that must be CONSERVED (kept consistent) when translating this content to Indian languages (Hindi, Telugu, Odia).

Categorize the terms into:

1. **mathematical_terms**: Core mathematical vocabulary that needs consistent translation across all pages.
   Examples: "rational number", "polynomial", "coefficient", "square root", "prime factorization"

2. **theorems_and_laws**: Named theorems, laws, properties, algorithms, or definitions.
   Examples: "Remainder Theorem", "Factor Theorem", "Euclid's division lemma", "Fundamental Theorem of Arithmetic"

3. **notation_terms**: Mathematical notation or symbolic references used in the text.
   Examples: "p(x)", "degree of polynomial", "leading coefficient", "zero of polynomial"

4. **domain_phrases**: Multi-word technical phrases specific to the topic.
   Examples: "non-terminating recurring decimal", "decimal expansion", "coprime integers", "linear polynomial"

5. **conserve_in_english**: Terms that should be kept in English even in translated text (universally recognized).
   Examples: names of mathematicians, standard abbreviations, formula variables

Rules:
- Extract terms EXACTLY as they appear in the content (preserve casing for proper nouns)
- Include ALL occurrences — do not skip any technical term
- For multi-word terms, include both the full phrase AND individual technical words if meaningful
- Be thorough: scan every section including examples, practice problems, and summaries

Content to analyze:
---
{content}
---

Output ONLY valid JSON (no markdown, no explanation):
{{
  "mathematical_terms": ["term1", "term2"],
  "theorems_and_laws": ["theorem1"],
  "notation_terms": ["notation1"],
  "domain_phrases": ["phrase1"],
  "conserve_in_english": ["name1"]
}}
"""


def load_model():
    """Load Qwen3-8B in float16 across available GPUs."""
    from transformers import AutoModelForCausalLM, AutoTokenizer

    n_gpus = torch.cuda.device_count()
    print(f"Loading {MODEL_ID} (fp16) across {n_gpus} GPU(s)...", flush=True)

    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_ID, trust_remote_code=True,
        cache_dir=HF_HOME
    )
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
        cache_dir=HF_HOME,
    )
    model.eval()

    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    if n_gpus > 0:
        for i in range(n_gpus):
            alloc = torch.cuda.memory_allocated(i) // 1024**2
            total = torch.cuda.get_device_properties(i).total_memory // 1024**2
            print(f"  GPU {i}: {torch.cuda.get_device_name(i)} | {alloc}/{total} MB", flush=True)

    return model, tokenizer


def extract_conservation_terms(model, tokenizer, content: str) -> dict:
    """Extract categorized technical terms from content using Qwen3-8B."""
    # Use up to 4000 chars to get good coverage per page
    content_truncated = content[:4000]
    prompt_text = CONSERVATION_PROMPT.format(content=content_truncated)

    messages = [{"role": "user", "content": prompt_text}]

    text = tokenizer.apply_chat_template(
        messages,
        tokenize=False,
        add_generation_prompt=True,
        enable_thinking=False,
    )

    inputs = tokenizer(text, return_tensors="pt").to(model.device)
    input_len = inputs["input_ids"].shape[1]

    with torch.inference_mode():
        outputs = model.generate(
            **inputs,
            max_new_tokens=1024,
            temperature=0.1,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated = outputs[0][input_len:]
    result_text = tokenizer.decode(generated, skip_special_tokens=True).strip()

    # Find JSON object in the output
    match = re.search(r"\{.*\}", result_text, re.DOTALL)
    if match:
        try:
            data = json.loads(match.group(0))
            # Validate structure
            categories = [
                "mathematical_terms", "theorems_and_laws",
                "notation_terms", "domain_phrases", "conserve_in_english"
            ]
            result = {}
            for cat in categories:
                terms = data.get(cat, [])
                if isinstance(terms, list):
                    result[cat] = [t.strip() for t in terms if isinstance(t, str) and t.strip()]
                else:
                    result[cat] = []
            return result
        except json.JSONDecodeError:
            pass

    # Fallback: return empty categories
    return {
        "mathematical_terms": [],
        "theorems_and_laws": [],
        "notation_terms": [],
        "domain_phrases": [],
        "conserve_in_english": [],
    }


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 _term_conservation.py <input_json> <output_json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = Path(sys.argv[2])

    with open(input_file, encoding="utf-8") as f:
        files = json.load(f)

    print(f"Processing {len(files)} topic pages for term conservation...", flush=True)

    model, tokenizer = load_model()

    all_results = {}
    all_flat_terms = set()

    for key, content in files.items():
        topic_name = Path(key).stem
        print(f"\n  [{topic_name}]", end="", flush=True)

        try:
            terms = extract_conservation_terms(model, tokenizer, content)
            all_results[key] = terms

            total = sum(len(v) for v in terms.values())
            print(f" → {total} terms", flush=True)

            for cat, term_list in terms.items():
                if term_list:
                    print(f"    {cat}: {', '.join(term_list[:5])}"
                          f"{'...' if len(term_list) > 5 else ''}", flush=True)
                    all_flat_terms.update(term_list)

        except Exception as e:
            print(f" ERROR: {e}", flush=True)
            all_results[key] = {
                "mathematical_terms": [],
                "theorems_and_laws": [],
                "notation_terms": [],
                "domain_phrases": [],
                "conserve_in_english": [],
            }

        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    # Build summary
    summary = {
        "per_page": all_results,
        "all_unique_terms": sorted(all_flat_terms),
        "total_unique": len(all_flat_terms),
        "pages_processed": len(all_results),
    }

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2, ensure_ascii=False)

    print(f"\n{'='*60}", flush=True)
    print(f"Done! {len(all_flat_terms)} unique terms across {len(all_results)} pages", flush=True)
    print(f"Saved to {output_file}", flush=True)


if __name__ == "__main__":
    main()
