"""
Content Generator — Llama-3.1-8B-Instruct (fp16)
═══════════════════════════════════════════════════════════════
Uses Meta-Llama-3.1-8B-Instruct (~8B params) on the remote HPC cluster.
Loaded in float16 — ~16 GB split across available GPUs.

Key points:
  - MODEL_ID: meta-llama/Llama-3.1-8B-Instruct
  - float16, device_map="auto"
  - Proper stop tokens so generation ends cleanly
  - Source-faithful: only expands on content from the given source chunk
  - Clean file output: just heading + content, no metadata

Usage:
  python3 content_gen_llama.py _all_chunks.json output_dir/
"""
import gc
import json
import os
import re
import time
from pathlib import Path
from typing import Dict, List, Optional

# Prevent CUDA memory fragmentation during generation
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")

import torch

# ═══════════ MODEL LOADING ═══════════

MODEL_ID = "meta-llama/Llama-3.1-8B-Instruct"

# Llama 3.1 stop tokens: <|eot_id|>=128009, <|end_of_text|>=128001
_STOP_TOKEN_IDS = [128001, 128009]

_model = None
_tokenizer = None


def load_model():
    """Load Llama-3.1-8B-Instruct in float16 across available GPUs."""
    global _model, _tokenizer
    if _model is not None:
        return _model, _tokenizer

    from transformers import AutoModelForCausalLM, AutoTokenizer

    # Count GPUs without initialising CUDA (device_count uses nvml, not CUDA)
    n_gpus = torch.cuda.device_count()
    print(f"Loading {MODEL_ID} (fp16) across {n_gpus} GPU(s)...")

    _tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
    _model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        torch_dtype=torch.float16,
        device_map="auto",
        trust_remote_code=True,
    )
    _model.eval()

    if _tokenizer.pad_token is None:
        _tokenizer.pad_token = _tokenizer.eos_token

    # Print GPU usage AFTER model load (CUDA is now properly initialised)
    try:
        used = sum(torch.cuda.memory_allocated(i) for i in range(n_gpus))
        for i in range(n_gpus):
            name = torch.cuda.get_device_name(i)
            alloc = torch.cuda.memory_allocated(i) // 1024**2
            total = torch.cuda.get_device_properties(i).total_memory // 1024**2
            print(f"  GPU {i}: {name} | {alloc}/{total} MB used")
        print(f"  Total GPU memory used: {used // 1024**2} MB")
    except Exception:
        print("  (GPU stats unavailable)")
    return _model, _tokenizer


# ═══════════ IMPORTANCE SCORING ═══════════

def unload_model():
    """Unload model from GPU to free memory for the next model."""
    global _model, _tokenizer
    if _model is not None:
        del _model
        _model = None
    if _tokenizer is not None:
        del _tokenizer
        _tokenizer = None
    gc.collect()
    torch.cuda.empty_cache()
    print("  Model unloaded, GPU memory freed.")


def score_topic_importance(chunks: List[Dict], chapter_title: str, grade: int) -> List[int]:
    topic_list = "\n".join(
        f"  {c['topic_number']} {c['topic_title']}" for c in chunks
    )

    # Build the expected output format as an example
    example_lines = "\n".join(f"{c['topic_number']}: <score>" for c in chunks)

    prompt = f"""As an expert NCERT curriculum designer, score each topic for Class {grade} '{chapter_title}'.

Score 1-5:
  5 = Core concept, heavily tested in board exams, foundational
  4 = Important, frequently appears in exams
  3 = Moderate importance, supporting concept
  2 = Minor, rarely tested directly
  1 = Supplementary / enrichment only

Topics to score:
{topic_list}

Reply with EXACTLY {len(chunks)} lines, one per topic, in this format:
{example_lines}

Replace <score> with a number 1-5. Output NOTHING else — no explanations, no headers, no extra text."""

    system = "You are an NCERT curriculum expert. Output ONLY the topic scores in the exact format requested. No thinking, no explanation, no extra text."

    max_attempts = 5
    for attempt in range(max_attempts):
        try:
            # Clear GPU cache before each attempt
            gc.collect()
            torch.cuda.empty_cache()

            result = generate_content(prompt, system, max_new_tokens=256)
            # Strip any thinking blocks
            result = re.sub(r'<think>.*?</think>', '', result, flags=re.DOTALL).strip()
            print(f"  [Scoring attempt {attempt+1}] Raw LLM output:\n{result}")
            scores = {}
            for line in result.strip().split('\n'):
                line = line.strip()
                if not line:
                    continue
                # Match patterns like "1.1: 4", "1.6.1: 5", "1.1 Introduction: 4"
                m = re.match(r'^(\d+\.\d+(?:\.\d+)?)\b.*?(\d)\s*$', line)
                if m:
                    topic_num = m.group(1)
                    score_val = int(m.group(2))
                    if 1 <= score_val <= 5:
                        scores[topic_num] = score_val

            # Check how many topics we got scores for
            matched = sum(1 for c in chunks if c['topic_number'] in scores)
            print(f"  [Scoring attempt {attempt+1}] Matched {matched}/{len(chunks)} topics")

            if matched >= len(chunks) * 0.7:  # At least 70% matched
                result_scores = []
                for c in chunks:
                    s = scores.get(c['topic_number'], 3)
                    result_scores.append(s)
                return result_scores
            else:
                print(f"  [Scoring attempt {attempt+1}] Too few matches, retrying...")
        except Exception as e:
            print(f"  [Scoring attempt {attempt+1}] Error: {e}")
            # If model failed to load, clear and retry
            gc.collect()
            torch.cuda.empty_cache()
            import time as _t
            _t.sleep(2)

    # FAIL HARD — user demanded no heuristic fallback
    raise RuntimeError(
        f"Importance scoring failed after {max_attempts} attempts. "
        "Check GPU memory (nvidia-smi) and ensure no other processes are using GPUs."
    )


def _estimate_content_size(chunk: Dict, importance: int = 3) -> str:
    content_len = chunk.get("content_length", 0)

    if importance >= 5:
        return "comprehensive (1500-2200 words)"
    elif importance >= 4:
        if content_len < 500:
            return "detailed (800-1200 words)"
        else:
            return "comprehensive (1200-1800 words)"
    elif importance >= 3:
        if content_len < 500:
            return "moderate (600-900 words)"
        else:
            return "detailed (800-1200 words)"
    elif importance >= 2:
        return "moderate (500-800 words)"
    else:
        return "brief (400-600 words)"


def _build_system_prompt(grade: int) -> str:
    if grade <= 8:
        level = "middle school"
        tone = "friendly, encouraging, and accessible. Use simple language and relatable everyday examples."
        extras = """- Include "Did You Know?" fun fact boxes to spark curiosity
- Include "Think About It" questions to encourage critical thinking
- Use analogies from daily life (sports, cooking, games) to explain concepts
- Add encouraging phrases like "Great job!" or "Let's explore!" throughout"""
    elif grade <= 10:
        level = "high school (Class 9-10)"
        tone = "clear and educational. Balance mathematical rigor with accessibility."
        extras = """- Include "Important Theorem" boxes with formal statements and intuitive explanations
- Add "Real-World Connection" sections showing practical applications
- Include "Exam Tip" boxes with board exam strategy hints
- Use step-by-step reasoning that students can follow"""
    else:
        level = "senior secondary (Class 11-12)"
        tone = "rigorous and precise. Use proper mathematical terminology and formal proofs."
        extras = """- Include "Theorem" boxes with formal proofs or proof sketches
- Add "JEE/Competitive Exam Corner" tips where relevant
- Include "Mathematical Insight" remarks connecting to advanced concepts
- Emphasize rigorous definitions and logical reasoning"""

    return f"""You are an expert mathematics teacher creating comprehensive, student-friendly educational content for {level} students (Grade {grade}, Indian NCERT curriculum).

CRITICAL LANGUAGE RULE: You MUST write ENTIRELY in English. Every single word, sentence, and character must be in English. Do NOT use any other language (no Chinese, Hindi, or any other script). If you ever feel the urge to write in another language, switch back to English immediately.

Your content must be:
- Accurate and faithful to the provided NCERT source material
- STRICTLY LIMITED to the content of the given source text — do NOT add concepts from other topics or sections
- Written in a {tone}
- Rich with mathematical formulas using LaTeX notation (inline: $...$, display: $$...$$)
- Structured with clear, well-organized sections
- Engaging and helpful for self-study

FORMATTING RULES (strictly follow):
- Use Markdown: ## for main sections, ### for subsections, **bold** for key terms
- ALL math formulas MUST use LaTeX: inline $x^2$ or display $$\\frac{{a}}{{b}}$$
- CRITICAL: Display math ($$...$$) MUST be on its own line, with a blank line before and after:
  Correct:
    some text

    $$x = \\frac{{-b \\pm \\sqrt{{b^2-4ac}}}}{{2a}}$$

    more text
  Wrong: some text$$x = 5$$more text
- CRITICAL: Inline math ($...$) MUST have a space before and after: "the value $x$ is" NOT "the value$x$is"
- NEVER put two $$...$$ blocks on the same line
- Use numbered steps for procedures and solutions
- Use bullet points for lists of properties or key points
- Use > blockquotes for important definitions, theorems, and tips
- Separate sections with --- horizontal rules

STUDENT-FRIENDLY additions:
{extras}
- Add a "Key Vocabulary" list defining important mathematical terms
- Include "Practice Problems" (2-3 unsolved problems with difficulty ratings: Easy/Medium/Hard)
- Add "Memory Aid" mnemonics or tricks where applicable
- Include visual descriptions (describe diagrams in words when helpful)"""


def _build_topic_prompt(chunk: Dict, chapter_title: str, grade: int,
                        all_topics: List[str], importance: int = 3) -> str:
    size_hint = _estimate_content_size(chunk, importance)
    topic_title = chunk["topic_title"]
    topic_num = chunk["topic_number"]
    source_text = chunk.get("content", "").strip()

    # Truncate very long source to avoid prompt overflow (keep ~2500 chars)
    if len(source_text) > 2500:
        source_text = source_text[:2500] + "\n[...source continues...]"

    # Build the related topics list (exclude current topic)
    related_topics_str = "\n".join(f"  - {t}" for t in all_topics if not t.startswith(topic_num + " "))

    if importance >= 4:
        section_instructions = f"""Write the topic page with these sections (ALL required, in this exact order):

## Prerequisites
- List 2-3 concepts the student should already know before studying this topic
- Be specific (e.g., "Understanding of set notation and element membership")

## Introduction
- Open with a hook — a question, real-life connection, or motivating observation
- State what the student will learn from THIS specific topic
- Connect to what they already know

## Explanation
- Explain ONLY the concepts present in the source text above — do NOT add material from other topics
- Define all key terms in **bold** when first introduced
- State all definitions, theorems, and properties in > blockquote format
- EVERY mathematical expression, symbol, set notation, number reference, or formula MUST be in LaTeX: inline $x$ or display $$...$$ (display math MUST be on its own line with blank lines around it)
- Even simple things like set names ($A$, $B$), membership ($\\in$), subset ($\\subset$), element references must be in LaTeX
- Build understanding step-by-step, from simple to complex

## Solved Examples
- 4-5 fully worked examples based ONLY on THIS topic's concepts from the source material
- Number as **Example 1:**, **Example 2:**, etc.
- Begin each solution with "**Solution:**"
- Show EVERY intermediate step — do not skip any reasoning
- VERIFY each answer is mathematically correct before writing it
- All math in LaTeX

## Practice Problems
- 4-5 unsolved problems (mark difficulty: 🟢 Easy, 🟡 Medium, 🔴 Hard)
- Problems MUST be directly related to THIS topic only — do not use concepts from other topics
- In the "**Answers:**" subsection, provide DETAILED step-by-step solutions for EACH problem, not just final answers
- DOUBLE-CHECK every answer is correct — verify by solving the problem yourself step by step
- All math in LaTeX

## Summary
- 5-7 bullet points summarising the key concepts and formulas from this topic
- All math in LaTeX

## Key Formulas
- A markdown table listing every important formula, definition, or property introduced in this topic
- Format: | Formula | Description |
- All formulas in LaTeX

## Exam-Style Questions
- 2-3 questions in the style of CBSE board exams or JEE for this topic
- Include expected marks (1-mark, 2-mark, 5-mark) and brief solution approach

## Student Corner
- **Common Mistakes:** 2-3 typical errors with corrections
- **Exam Tips:** 1-2 tips specific to this topic
- **Memory Aid:** A mnemonic or shortcut if applicable

## Related Topics
List 2-4 topics from this chapter that are conceptually connected to this topic:
{related_topics_str}
Format as: - [Topic Number Topic Title] — one line explaining the connection"""

    elif importance >= 3:
        section_instructions = f"""Write the topic page with these sections (ALL required, in this exact order):

## Prerequisites
- List 2-3 concepts the student should already know before studying this topic

## Introduction
- Brief hook and state what the student will learn (2-3 sentences)

## Explanation
- Explain ONLY the concepts present in the source text above — do NOT add material from other topics
- Define key terms in **bold**
- State formulas and properties in > blockquote format
- EVERY mathematical expression, symbol, set notation, or formula MUST be in LaTeX: inline $x$ or display $$...$$
- Even simple things like set names ($A$, $B$), membership ($\\in$), subset ($\\subset$) must be in LaTeX

## Solved Examples
- 3-4 worked examples based ONLY on THIS topic's concepts
- Show ALL steps, number them **Example 1:**, etc.
- Begin each with "**Solution:**"
- VERIFY each answer is mathematically correct
- All math in LaTeX

## Practice Problems
- 3-4 unsolved problems with difficulty markers (🟢 🟡 🔴)
- Problems MUST be directly related to THIS topic only
- In "**Answers:**" subsection, provide DETAILED step-by-step solutions, not just final answers
- DOUBLE-CHECK every answer is correct
- All math in LaTeX

## Summary
- 4-6 bullet points of key concepts and formulas (all math in LaTeX)

## Key Formulas
- A markdown table: | Formula | Description |
- All formulas in LaTeX

## Student Corner
- **Common Mistakes:** 1-2 errors worth flagging
- Include Memory Aid or Exam Tips only if directly relevant

## Related Topics
List 2-3 related topics from this chapter:
{related_topics_str}
Format as: - [Topic Number Topic Title] — one line explaining the connection"""

    else:
        section_instructions = f"""Write a topic page with these sections:

## Prerequisites
- List 1-2 concepts the student should already know

## Introduction
- 2-3 sentences: hook + what the student will learn

## Explanation
- Explain ONLY the concepts present in the source text above — do NOT add material from other topics
- Define key terms, state important formulas
- EVERY mathematical expression MUST be in LaTeX: inline $x$ or display $$...$$

## Solved Examples
- 2-3 worked examples with full step-by-step solutions
- VERIFY each answer is mathematically correct
- All math in LaTeX

## Practice Problems
- 2-3 problems with difficulty markers (🟢 🟡 🔴)
- In "**Answers:**", provide step-by-step solutions
- DOUBLE-CHECK correctness
- All math in LaTeX

## Summary
- 3-5 bullet points (all math in LaTeX)

## Key Formulas
- Markdown table: | Formula | Description |

## Related Topics
List 2-3 related topics:
{related_topics_str}
Format as: - [Topic Number Topic Title] — one line explaining the connection"""

    return f"""Create a student-friendly educational page for the following NCERT topic. Write ENTIRELY in English.

Topic: {topic_num} {topic_title}
Chapter: {chapter_title} (Grade {grade})
Target length: {size_hint}

All topics in this chapter (for context — do NOT cover content from these other topics):
{chr(10).join('  - ' + t for t in all_topics)}

SOURCE TEXT (from the NCERT textbook for THIS specific topic section):
---
{source_text}
---

IMPORTANT RULES:
1. Base your content EXCLUSIVELY on the SOURCE TEXT above. Do not add concepts from other parts of the chapter.
2. Do not mention topic numbers, importance scores, or any internal metadata in your output.
3. Every word must be in English — absolutely no Chinese, Hindi, or any other language.
4. CRITICAL — ALL math MUST be in LaTeX without exception:
   - Set names: $A$, $B$, $U$ (never plain A, B, U when referring to sets)
   - Symbols: $\\in$, $\\notin$, $\\subset$, $\\subseteq$, $\\cup$, $\\cap$, $\\emptyset$, $\\phi$
   - Numbers in math context: $x = 2$, $n(A) = 5$
   - Display math on its own line with blank lines before and after
   - Even simple expressions like "element a belongs to set A" should be "$a \\in A$"
5. Solved examples and practice problem answers MUST be verified for correctness. Show every step.

{section_instructions}

STRICT OUTPUT RULES:
- Do NOT start your response with the topic title (it will be added automatically)
- Do NOT include any preamble like "Here is the content" or "Sure, I will..."
- Start directly with the first ## heading (## Prerequisites)
- Write ENTIRELY in English
- Every mathematical symbol, set name, or formula MUST be in LaTeX"""


# ═══════════ GENERATION ═══════════

def generate_content(prompt: str, system_prompt: str,
                     max_new_tokens: int = 2048) -> str:
    model, tokenizer = load_model()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    input_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

    # Move inputs to the same device as the embedding layer (avoids hard-coding cuda:0)
    embed_device = model.get_input_embeddings().weight.device
    inputs = tokenizer(input_text, return_tensors="pt").to(embed_device)
    input_len = inputs["input_ids"].shape[1]

    # Guard: never request more new tokens than the model's context allows
    max_ctx = getattr(model.config, "max_position_embeddings", 32768)
    max_new_tokens = min(max_new_tokens, max_ctx - input_len - 16)
    if max_new_tokens <= 0:
        # Input already too long — truncate and retry with half
        max_new_tokens = 1024

    print(f"[{input_len} tokens] ", end="", flush=True)

    gc.collect()
    torch.cuda.empty_cache()

    for attempt in range(3):
        try:
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=0.7,
                    top_p=0.9,
                    do_sample=True,
                    repetition_penalty=1.1,
                    eos_token_id=_STOP_TOKEN_IDS,
                    pad_token_id=tokenizer.pad_token_id,
                )
            break
        except (torch.cuda.OutOfMemoryError, RuntimeError) as e:
            if "out of memory" in str(e).lower() and attempt < 2:
                max_new_tokens = max_new_tokens // 2
                print(f"\n    OOM! Retrying with max_tokens={max_new_tokens}...", end=" ", flush=True)
                try:
                    del outputs
                except NameError:
                    pass
                del inputs
                gc.collect()
                torch.cuda.empty_cache()
                inputs = tokenizer(input_text, return_tensors="pt").to("cuda:0")
            else:
                raise

    generated = outputs[0][input_len:]
    text = tokenizer.decode(generated, skip_special_tokens=True)
    return text.strip()


# ═══════════ POST-PROCESSING ═══════════

def _clean_generated_content(text: str) -> str:
    # Strip Qwen3 chain-of-thought <think>...</think> blocks (they appear as plain text)
    text = re.sub(r'<think>.*?</think>', '', text, flags=re.DOTALL).strip()

    lines = text.split('\n')
    seen_headers = set()
    cleaned = []
    for line in lines:
        if line.startswith('## '):
            header = line.strip()
            if header in seen_headers:
                continue
            seen_headers.add(header)
        cleaned.append(line)

    text = '\n'.join(cleaned)

    text = text.replace('\\\\frac', '\\frac')
    text = text.replace('\\\\sqrt', '\\sqrt')
    text = text.replace('\\\\text', '\\text')
    text = text.replace('\\\\cdot', '\\cdot')
    text = text.replace('\\\\times', '\\times')

    text = _fix_latex_formatting(text)
    return text.strip()


def _fix_latex_formatting(text: str) -> str:
    text = re.sub(r'(\$\$[^$]+\$\$)(\s*)(\$\$)', r'\1\n\n\3', text)
    text = re.sub(r'([^\n$])\s*(\$\$)(?!\$)', r'\1\n\n\2', text)
    text = re.sub(r'(\$\$)([^\n$\s])', r'\1\n\n\2', text)
    text = re.sub(r'([a-zA-Z0-9,;:})\]])\$(?!\$)', r'\1 $', text)
    text = re.sub(r'(?<!\$)\$([^$]+)\$([a-zA-Z0-9({\[])', lambda m: f'${m.group(1)}$ {m.group(2)}', text)
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    return text


# ═══════════ CHAPTER PROCESSING ═══════════

def generate_chapter_content(chunks_file: str, output_dir: str):
    with open(chunks_file, 'r', encoding='utf-8') as f:
        data = json.load(f)

    chunks = data["chunks"]
    grade = data.get("grade", 11)
    chapter_num = data.get("chapter_number", 1)
    chapter_title = data.get("chapter_title", "Unknown")

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    all_topics = [f"{c['topic_number']} {c['topic_title']}" for c in chunks]
    system_prompt = _build_system_prompt(grade)

    print(f"\n{'='*60}")
    print(f"Model: {MODEL_ID}")
    print(f"Generating: Grade {grade} Ch {chapter_num}: {chapter_title}")
    print(f"Topics: {len(chunks)} | GPUs: {torch.cuda.device_count()}")
    print(f"{'='*60}\n")

    print("  Scoring topic importance...", flush=True)
    importance_scores = score_topic_importance(chunks, chapter_title, grade)
    for c, s in zip(chunks, importance_scores):
        print(f"    {c['topic_number']} {c['topic_title']}: {s}/5 {'⭐' * s}")
    print()

    gc.collect()
    torch.cuda.empty_cache()

    results = []
    for i, chunk in enumerate(chunks):
        topic_num = chunk["topic_number"]
        topic_title = chunk["topic_title"]
        importance = importance_scores[i]

        safe_title = re.sub(r'[^\w\s-]', '', topic_title)
        safe_title = re.sub(r'\s+', '_', safe_title)[:50]
        filename = f"{topic_num}_{safe_title}.md"
        filepath = out_dir / filename

        if filepath.exists() and filepath.stat().st_size > 100:
            print(f"  [{i+1}/{len(chunks)}] {topic_num} {topic_title} — skipping (exists)")
            results.append({
                "topic_number": topic_num, "topic_title": topic_title,
                "file": filename, "importance": importance,
                "content_length": filepath.stat().st_size,
                "generation_time": 0, "skipped": True,
            })
            continue

        print(f"  [{i+1}/{len(chunks)}] {topic_num} {topic_title} (importance: {importance}/5)...", end=" ", flush=True)
        start = time.time()

        prompt = _build_topic_prompt(chunk, chapter_title, grade, all_topics, importance)

        if importance >= 5:
            max_tokens = 6144
        elif importance >= 4:
            max_tokens = 5120
        elif importance >= 3:
            max_tokens = 4096
        elif importance >= 2:
            max_tokens = 3072
        else:
            max_tokens = 2560

        raw_content = generate_content(prompt, system_prompt, max_tokens)
        content = _clean_generated_content(raw_content)

        elapsed = time.time() - start
        print(f"({len(content)} chars, {elapsed:.1f}s)")

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {topic_num} {topic_title}\n\n")
            f.write(f"> **Grade {grade}** | **Chapter {chapter_num}: {chapter_title}**\n\n")
            f.write("---\n\n")
            f.write(content)
            f.write("\n")

        results.append({
            "topic_number": topic_num, "topic_title": topic_title,
            "file": filename, "importance": importance,
            "content_length": len(content),
            "generation_time": round(elapsed, 1),
        })

        gc.collect()
        torch.cuda.empty_cache()

    index = {
        "model": MODEL_ID,
        "grade": grade, "chapter_number": chapter_num, "chapter_title": chapter_title,
        "topics": results,
        "total_content_length": sum(r["content_length"] for r in results),
        "total_generation_time": sum(r["generation_time"] for r in results),
    }

    with open(out_dir / "_index.json", 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"\nDone! {len(results)} topics | {index['total_content_length']} chars | {index['total_generation_time']:.1f}s")
    print(f"Output: {out_dir}")
    return index


# ═══════════ CLI ═══════════

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 3:
        print("Usage: python content_gen_llama.py <chunks_json> <output_dir>")
        print("Example: python content_gen_llama.py chunks/grade11/maths/chapter1/_all_chunks.json output/grade11/maths/chapter1/llama")
        sys.exit(1)

    chunks_file = sys.argv[1]
    output_dir = sys.argv[2]
    generate_chapter_content(chunks_file, output_dir)
