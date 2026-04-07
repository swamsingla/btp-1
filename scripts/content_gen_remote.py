"""
Content Generator — Qwen2.5-Math-7B-Instruct (remote GPU server)
═══════════════════════════════════════════════════════════════════
Same pipeline as content_gen.py but uses Qwen2.5-Math-7B on multi-GPU setup.
Designed for gnode017 (2× GTX 1080 Ti, 22 GB total VRAM).

Usage:
  python3 content_gen_remote.py _all_chunks.json output_dir/
"""
import gc
import json
import os
import re
import time
import torch
from pathlib import Path
from typing import Dict, List, Optional

# Reduce CUDA memory fragmentation
os.environ.setdefault("PYTORCH_CUDA_ALLOC_CONF", "expandable_segments:True")


# ═══════════ MODEL LOADING ═══════════

MODEL_ID = "Qwen/Qwen2.5-Math-7B-Instruct"

_model = None
_tokenizer = None


def load_model():
    """Load Qwen2.5-Math-7B in fp16 distributed across all available GPUs.
    Reserves 2.5 GB headroom per GPU for KV cache and attention computation.
    """
    global _model, _tokenizer
    if _model is not None:
        return _model, _tokenizer

    from transformers import AutoModelForCausalLM, AutoTokenizer

    num_gpus = torch.cuda.device_count()

    # Clear any stale GPU memory before loading
    for i in range(num_gpus):
        torch.cuda.set_device(i)
        torch.cuda.empty_cache()

    # Reserve 2.5 GB per GPU for KV cache + attention during generation
    HEADROOM_MB = 2560
    max_memory = {}
    for i in range(num_gpus):
        total_mb = torch.cuda.get_device_properties(i).total_memory // (1024 * 1024)
        usable_mb = total_mb - HEADROOM_MB
        max_memory[i] = f"{usable_mb}MiB"
        print(f"  GPU {i}: {torch.cuda.get_device_name(i)} | {total_mb} MB total, {usable_mb} MB for model")

    print(f"Loading {MODEL_ID} (fp16, device_map=auto)...")
    _tokenizer = AutoTokenizer.from_pretrained(MODEL_ID, trust_remote_code=True)
    _model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        device_map="auto",
        dtype=torch.float16,
        max_memory=max_memory,
        trust_remote_code=True,
    )

    if _tokenizer.pad_token is None:
        _tokenizer.pad_token = _tokenizer.eos_token

    # Extend context window to 8192 (Qwen2.5 supports up to 128K)
    _model.config.max_position_embeddings = 8192
    if hasattr(_model, 'generation_config'):
        _model.generation_config.max_length = 8192

    total_used = sum(torch.cuda.memory_allocated(i) for i in range(num_gpus)) // (1024 * 1024)
    print(f"  Model loaded! Total GPU memory used: {total_used} MB")
    return _model, _tokenizer


# ═══════════ IMPORTANCE SCORING ═══════════

def score_topic_importance(chunks: List[Dict], chapter_title: str, grade: int) -> List[int]:
    topic_list = "\n".join(
        f"  {c['topic_number']} {c['topic_title']}" for c in chunks
    )
    prompt = f"""As an expert NCERT curriculum designer, look at this list of topics for Class {grade} '{chapter_title}'.
Assign an importance score from 1 to 5 to each topic based on how fundamental it is to the subject and its weightage in board exams.

Scoring guide:
  5 = Core concept, heavily tested, foundational for future learning
  4 = Important, frequently appears in exams
  3 = Moderate importance, supporting concept
  2 = Minor, rarely tested directly
  1 = Supplementary, enrichment only

Topics:
{topic_list}

Respond with ONLY the scores, one per line, in format:
topic_number: score

Example:
1.1: 4
1.2: 5
1.3: 3"""

    system = "You are an NCERT curriculum expert. Respond only with the requested scores, nothing else."
    try:
        result = generate_content(prompt, system, max_new_tokens=256)
        scores = {}
        for line in result.strip().split('\n'):
            line = line.strip()
            if ':' in line:
                parts = line.split(':')
                topic_num = parts[0].strip()
                try:
                    score = int(parts[1].strip())
                    score = max(1, min(5, score))
                    scores[topic_num] = score
                except ValueError:
                    pass
        result_scores = []
        for c in chunks:
            s = scores.get(c['topic_number'], 3)
            result_scores.append(s)
        return result_scores
    except Exception as e:
        print(f"  Warning: Scoring failed ({e}), using default scores")
        return [3] * len(chunks)


def _estimate_content_size(chunk: Dict, importance: int = 3) -> str:
    content_len = chunk.get("content_length", 0)
    depth = chunk.get("depth", 2)
    if depth >= 3:
        return "concise (300-500 words)"
    if importance >= 5:
        return "comprehensive (1200-1800 words)"
    elif importance >= 4:
        if content_len < 500:
            return "moderate (500-800 words)"
        else:
            return "detailed (800-1200 words)"
    elif importance >= 3:
        if content_len < 500:
            return "brief (300-500 words)"
        else:
            return "moderate (500-800 words)"
    elif importance >= 2:
        return "brief (200-400 words)"
    else:
        return "concise (150-300 words)"


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

Your content must be:
- Accurate and faithfully aligned with the NCERT syllabus
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
    source_text = chunk.get("content", "")
    topics_list = "\n".join(f"  - {t}" for t in all_topics)

    # Truncate source text to ~3000 chars (~750 tokens) to keep total prompt
    # under ~2000 tokens, preventing SDPA attention OOM during generation.
    MAX_SOURCE_CHARS = 3000
    if len(source_text) > MAX_SOURCE_CHARS:
        source_text = source_text[:MAX_SOURCE_CHARS] + "\n[...source truncated, focus on key concepts above...]"

    if importance >= 4:
        section_instructions = """Generate the topic page with these sections. ALL sections are REQUIRED for this important topic:

## Introduction
- Start with a hook — a question, fun fact, or real-life scenario related to the topic
- Briefly state what the student will learn
- Connect to what they already know from previous topics in this chapter or earlier classes

## Explanation
- Explain the core concepts clearly and thoroughly — this is a HIGH-IMPORTANCE topic
- Define all key terms when first introduced (in **bold**)
- State all theorems, properties, and formulas in proper > blockquote format
- Use LaTeX for ALL mathematical expressions ($...$ inline, $$...$$ display)
- Build understanding step-by-step, from simpler to more complex ideas
- Include visual descriptions of any geometric diagrams or graphs
- Go into significant depth — students need to master this topic

## Solved Examples
- Provide 3-4 fully worked examples covering different problem types
- For each example: State the problem clearly, then solve step-by-step
- Show ALL intermediate steps — do not skip any calculation
- Use **Example 1:**, **Example 2:** numbering
- Start each solution with "**Solution:**" on its own line
- Progress from easy to hard examples

## Practice Problems
- Give 3-4 unsolved problems for the student to try
- Mark difficulty: Easy, Medium, Hard
- Provide final answers (but not full solutions) in a "Answers" subsection

## Summary
- 4-6 bullet point recap of the most important concepts and formulas
- Include all key formulas in one collected list
- Highlight what to remember for exams

## Student Corner
- **Common Mistakes:** 2-3 typical errors students make, with corrections
- **Exam Tips:** 1-2 board exam strategy tips specific to this topic
- **Memory Aid:** A mnemonic, trick, or shortcut if applicable
- **Did You Know?:** An interesting mathematical fact related to the topic"""
    elif importance >= 3:
        section_instructions = """Generate the topic page with these sections. Include all sections but keep depth moderate:

## Introduction
- Start with a hook — a question, fun fact, or real-life scenario
- Briefly state what the student will learn
- Connect to previous knowledge

## Explanation
- Explain the core concepts clearly
- Define key terms in **bold**
- State theorems and formulas in > blockquote format
- Use LaTeX for all math expressions
- Build understanding step-by-step

## Solved Examples
- Provide 2-3 worked examples
- Show all intermediate steps
- Progress from easy to hard

## Practice Problems
- Give 2-3 unsolved problems with difficulty markers (Easy/Medium/Hard)
- Include answers

## Summary
- 3-5 bullet point recap of key concepts and formulas

## Student Corner
- **Common Mistakes:** 1-2 typical errors with corrections
- Include any of: Exam Tips, Memory Aid, Did You Know? — but ONLY if genuinely useful for this topic. Skip any that would feel forced or low-value."""
    else:
        section_instructions = """Generate a CONCISE topic page. This is a lower-priority topic — keep it brief and focused.
Include ONLY the sections that are genuinely useful. Skip sections that would have thin or forced content.

REQUIRED sections:
## Introduction
- Brief hook and state what the student will learn (2-3 sentences)

## Explanation
- Explain the core concept concisely
- Define key terms, state important formulas
- Use LaTeX for math expressions

OPTIONAL — include ONLY if genuinely useful:
## Solved Examples (1-2 examples if the topic involves problem-solving)
## Practice Problems (1-2 problems if applicable)
## Summary (brief 2-3 point recap)
## Student Corner (only if there are common mistakes worth mentioning)

Do NOT pad content — if a section would be thin or repetitive, skip it entirely."""

    return f"""Generate a comprehensive, student-friendly topic page for the following mathematics topic.

**Chapter:** {chapter_title} (Grade {grade})
**Topic:** {topic_num} {topic_title}
**Importance Score:** {importance}/5 {'*' * importance}
**Target Length:** {size_hint}

**All topics in this chapter (for context):**
{topics_list}

**Source material from NCERT textbook:**
---
{source_text}
---

{section_instructions}

STRICT RULES:
- ALL math must be in LaTeX: inline $...$ or display $$...$$
- Display math $$...$$ MUST be on its OWN line with blank lines before and after
- Inline math $...$ MUST have spaces around it: "the value $x$ is" NOT "the value$x$is"
- NEVER put two $$...$$ blocks on the same line
- Be faithful to the NCERT content — do not introduce concepts not in the syllabus
- Every formula from the source material MUST appear in your content
- Use simple English — write as if explaining to a student studying alone
- If a section would have no meaningful content for this topic, SKIP it entirely rather than adding filler"""


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
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    input_len = inputs["input_ids"].shape[1]
    # Clamp max_new_tokens so total sequence stays within 8192
    max_new_tokens = min(max_new_tokens, max(512, 8192 - input_len))
    print(f"[{input_len} tokens] ", end="", flush=True)
    gc.collect()
    torch.cuda.empty_cache()

    for attempt in range(4):
        try:
            with torch.no_grad():
                outputs = model.generate(
                    **inputs,
                    max_new_tokens=max_new_tokens,
                    temperature=0.7,
                    top_p=0.9,
                    do_sample=True,
                    repetition_penalty=1.1,
                    pad_token_id=tokenizer.pad_token_id,
                )
            break
        except (torch.cuda.OutOfMemoryError, RuntimeError) as e:
            if "out of memory" in str(e).lower() and attempt < 3:
                try:
                    del outputs
                except NameError:
                    pass
                del inputs
                gc.collect()
                torch.cuda.empty_cache()
                if attempt < 2:
                    # First two retries: halve max_new_tokens
                    max_new_tokens = max(256, max_new_tokens // 2)
                    print(f"\n    OOM! Retrying with max_tokens={max_new_tokens}...", end=" ", flush=True)
                    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
                else:
                    # Last resort: truncate input to 1500 tokens + minimal output
                    max_new_tokens = 512
                    print(f"\n    OOM! Truncating input to 1500 tokens, max_tokens={max_new_tokens}...", end=" ", flush=True)
                    all_ids = tokenizer(input_text, return_tensors="pt")["input_ids"]
                    truncated_ids = all_ids[:, :1500].to(model.device)
                    inputs = {"input_ids": truncated_ids,
                              "attention_mask": torch.ones_like(truncated_ids)}
            else:
                raise

    generated = outputs[0][input_len:]
    text = tokenizer.decode(generated, skip_special_tokens=True)
    return text.strip()


# ═══════════ POST-PROCESSING ═══════════

def _clean_generated_content(text: str) -> str:
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


# ═══════════ MAIN ═══════════

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
    print(f"Generating: Grade {grade} Ch {chapter_num}: {chapter_title}")
    print(f"Model: {MODEL_ID}")
    print(f"Topics: {len(chunks)}")
    print(f"{'='*60}\n")

    print("  Scoring topic importance...", end=" ", flush=True)
    importance_scores = score_topic_importance(chunks, chapter_title, grade)
    for c, s in zip(chunks, importance_scores):
        print(f"    {c['topic_number']} {c['topic_title']}: {s}/5 {'*' * s}")
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
            print(f"  [{i+1}/{len(chunks)}] {topic_num} {topic_title} -- already exists, skipping")
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
            max_tokens = 3072
        elif importance >= 4:
            max_tokens = 2560
        elif importance >= 3:
            max_tokens = 2048
        elif importance >= 2:
            max_tokens = 1536
        else:
            max_tokens = 1024

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
        "grade": grade, "chapter_number": chapter_num,
        "chapter_title": chapter_title, "model": MODEL_ID,
        "topics": results,
        "total_content_length": sum(r["content_length"] for r in results),
        "total_generation_time": sum(r["generation_time"] for r in results),
    }
    with open(out_dir / "_index.json", 'w', encoding='utf-8') as f:
        json.dump(index, f, indent=2, ensure_ascii=False)

    print(f"\nDone! {len(results)} topics generated.")
    print(f"Total content: {index['total_content_length']} chars")
    print(f"Total time: {index['total_generation_time']:.1f}s")
    print(f"Output: {out_dir}")


if __name__ == "__main__":
    import sys
    if len(sys.argv) < 3:
        print("Usage: python3 content_gen_remote.py <chunks_file> <output_dir>")
        sys.exit(1)
    generate_chapter_content(sys.argv[1], sys.argv[2])
