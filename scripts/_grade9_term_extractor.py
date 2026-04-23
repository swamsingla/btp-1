#!/usr/bin/env python3
"""
Term extractor for grade 9 topics using Qwen3-8B.
Runs ON gnode047. Reads .md files and extracts technical/domain-specific terms.

Usage:
  python3 _grade9_term_extractor.py <input_json> <output_json>
  
  input_json: {"grade9/maths/chapter1/1.1_Introduction.md": "<content>", ...}
  output_json: {"grade9/maths/chapter1/1.1_Introduction.md": ["term1", "term2"], ...}
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

EXTRACT_PROMPT = """\
You are an expert in mathematics education. Your task is to identify technical and domain-specific terms from the given educational content that need CONSISTENT translation.

These are terms that:
1. Are mathematical subject-specific terms (e.g., "irrational number", "polynomial", "coefficient", "decimal expansion", "arithmetic progression")
2. Are named concepts, theorems, definitions, or properties used in the text
3. Would confuse students if translated inconsistently from topic to topic

Rules:
- Return ONLY lowercase English strings
- Include multi-word terms like "non-terminating decimal" or "fundamental theorem"
- Do NOT include generic words like "number", "find", "example", "solution", "equation" (unless very specific like "quadratic equation")
- Be specific: prefer "irrational number" over just "irrational"

Content:
{content}

Think through the content carefully, then output ONLY a JSON array:
["term1", "term2", "term3"]
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


def extract_terms(model, tokenizer, content: str) -> list:
    """Extract technical terms from content using Qwen3-8B."""
    content_truncated = content[:3000]
    prompt_text = EXTRACT_PROMPT.format(content=content_truncated)

    messages = [{"role": "user", "content": prompt_text}]

    # Qwen3 chat template with thinking disabled
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
            max_new_tokens=512,
            temperature=0.1,
            do_sample=True,
            pad_token_id=tokenizer.eos_token_id,
        )

    generated = outputs[0][input_len:]
    result_text = tokenizer.decode(generated, skip_special_tokens=True).strip()

    # Find JSON array in the output
    match = re.search(r"\[.*?\]", result_text, re.DOTALL)
    if match:
        try:
            terms = json.loads(match.group(0))
            # Clean: lowercase, strip, remove junk
            terms = [t.lower().strip() for t in terms if isinstance(t, str)]
            terms = [t for t in terms if len(t) > 2]
            terms = [t for t in terms if not re.match(r"^[\d\s.,;:()\-]+$", t)]
            return terms
        except json.JSONDecodeError:
            pass

    # Fallback: try to parse line-by-line if JSON failed
    lines = result_text.split("\n")
    terms = []
    for line in lines:
        line = line.strip().strip('"').strip("'").strip(",").strip()
        if line and len(line) > 2 and not line.startswith("[") and not line.startswith("]"):
            terms.append(line.lower())
    return terms[:30]  # cap at 30 terms per topic


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 _grade9_term_extractor.py <input_json> <output_json>")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = Path(sys.argv[2])

    with open(input_file, encoding="utf-8") as f:
        files = json.load(f)

    print(f"Processing {len(files)} topic files...", flush=True)

    model, tokenizer = load_model()

    all_terms = {}

    for key, content in files.items():
        topic_name = Path(key).stem
        print(f"  [{topic_name}]...", end="", flush=True)

        try:
            terms = extract_terms(model, tokenizer, content)
            all_terms[key] = terms
            print(f" {len(terms)} terms", flush=True)
            if terms:
                print(f"    → {', '.join(terms[:8])}", flush=True)
        except Exception as e:
            print(f" ERROR: {e}", flush=True)
            all_terms[key] = []

        # Free GPU memory between topics
        gc.collect()
        if torch.cuda.is_available():
            torch.cuda.empty_cache()

    # Summary
    all_unique = list(set(t for terms in all_terms.values() for t in terms))
    print(f"\nDone! {len(all_unique)} unique terms across all topics", flush=True)

    output_file.parent.mkdir(parents=True, exist_ok=True)
    with open(output_file, "w", encoding="utf-8") as f:
        json.dump(all_terms, f, indent=2, ensure_ascii=False)

    print(f"Saved to {output_file}", flush=True)


if __name__ == "__main__":
    main()
