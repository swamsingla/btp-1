"""
Content Generator — Llama 3.2 3B Instruct (4-bit quantized)
═══════════════════════════════════════════════════════════
Generates structured educational content for each topic in a chapter.
Uses extracted chunk text as context for accurate, curriculum-aligned content.

Output per topic:
  - Introduction
  - Key Concepts & Explanation (with formulas in LaTeX/KaTeX)
  - Worked Examples
  - Common Mistakes / Misconceptions
  - Practice Tips
  - Conclusion / Summary

Formulas use KaTeX-compatible LaTeX: inline $...$ and display $$...$$
"""
import gc
import json
import os
import re
import time
import torch
from pathlib import Path
from typing import Dict, List, Optional


# ═══════════ MODEL LOADING ═══════════

MODEL_ID = "meta-llama/Llama-3.2-3B-Instruct"

_model = None
_tokenizer = None


def load_model():
    """Load model with 4-bit quantization for RTX 3050 (4GB VRAM)."""
    global _model, _tokenizer
    if _model is not None:
        return _model, _tokenizer

    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

    print(f"Loading {MODEL_ID} with 4-bit quantization...")
    print(f"  GPU: {torch.cuda.get_device_name(0)}")
    print(f"  VRAM: {torch.cuda.get_device_properties(0).total_memory // 1024**2} MB")

    bnb_config = BitsAndBytesConfig(
        load_in_4bit=True,
        bnb_4bit_quant_type="nf4",
        bnb_4bit_compute_dtype=torch.float16,
        bnb_4bit_use_double_quant=True,  # saves extra memory
    )

    _tokenizer = AutoTokenizer.from_pretrained(MODEL_ID)
    _model = AutoModelForCausalLM.from_pretrained(
        MODEL_ID,
        quantization_config=bnb_config,
        device_map="auto",
        torch_dtype=torch.float16,
    )

    # Set pad token
    if _tokenizer.pad_token is None:
        _tokenizer.pad_token = _tokenizer.eos_token

    print(f"  Model loaded! Memory: {torch.cuda.memory_allocated() // 1024**2} MB")
    return _model, _tokenizer


# ═══════════ PROMPT ENGINEERING ═══════════

# ═══════════ IMPORTANCE SCORING ═══════════

def score_topic_importance(chunks: List[Dict], chapter_title: str, grade: int) -> List[int]:
    """Use the LLM to score each topic's importance from 1-5.

    Scoring criteria:
      5 = Core concept, heavily tested in board exams, foundational
      4 = Important concept, frequently appears in exams
      3 = Moderate importance, useful supporting concept
      2 = Minor topic, rarely tested directly
      1 = Supplementary/optional, historical context or enrichment
    """
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
                    score = max(1, min(5, score))  # Clamp 1-5
                    scores[topic_num] = score
                except ValueError:
                    pass

        # Map scores back to chunks
        result_scores = []
        for c in chunks:
            s = scores.get(c['topic_number'], 3)  # Default 3 if not found
            result_scores.append(s)
        return result_scores
    except Exception as e:
        print(f"  Warning: Scoring failed ({e}), using default scores")
        return [3] * len(chunks)


def _estimate_content_size(chunk: Dict, importance: int = 3) -> str:
    """Estimate desired content size based on importance score and content length."""
    content_len = chunk.get("content_length", 0)
    depth = chunk.get("depth", 2)

    if depth >= 3:
        return "concise (300-500 words)"

    # Scale content size by importance score
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
    """Build system prompt based on grade level."""
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


# No truncation — feed full source text to the model.
# Llama 3.2 3B has 128k context window; even the largest chunks fit easily.


def _build_topic_prompt(chunk: Dict, chapter_title: str, grade: int,
                         all_topics: List[str], importance: int = 3) -> str:
    """Build the generation prompt for a single topic."""
    size_hint = _estimate_content_size(chunk, importance)
    topic_title = chunk["topic_title"]
    topic_num = chunk["topic_number"]
    source_text = chunk.get("content", "")

    topics_list = "\n".join(f"  - {t}" for t in all_topics)

    # Build section instructions based on importance
    # High importance (4-5): all sections required, more depth
    # Medium importance (3): standard sections
    # Low importance (1-2): allow skipping non-essential sections
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
- Mark difficulty: 🟢 Easy, 🟡 Medium, 🔴 Hard
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
- Give 2-3 unsolved problems with difficulty markers (🟢 🟡 🔴)
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
**Importance Score:** {importance}/5 {'⭐' * importance}
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
    """Generate content using the loaded model."""
    model, tokenizer = load_model()

    # Build messages for chat template
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": prompt},
    ]

    # Apply chat template
    input_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )

    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
    input_len = inputs["input_ids"].shape[1]
    print(f"[{input_len} tokens] ", end="", flush=True)

    # Free fragmented GPU memory before generation
    gc.collect()
    torch.cuda.empty_cache()

    # Retry with reduced tokens on OOM
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
                    pad_token_id=tokenizer.pad_token_id,
                )
            break
        except (torch.cuda.OutOfMemoryError, RuntimeError) as e:
            if "out of memory" in str(e).lower() and attempt < 2:
                max_new_tokens = max_new_tokens // 2
                print(f"\n    OOM! Retrying with max_tokens={max_new_tokens}...", end=" ", flush=True)
                # Delete tensors to free VRAM, then re-create
                try:
                    del outputs
                except NameError:
                    pass
                del inputs
                gc.collect()
                torch.cuda.empty_cache()
                inputs = tokenizer(input_text, return_tensors="pt").to(model.device)
            else:
                raise

    # Decode only the generated part
    generated = outputs[0][input_len:]
    text = tokenizer.decode(generated, skip_special_tokens=True)

    return text.strip()


# ═══════════ POST-PROCESSING ═══════════

def _clean_generated_content(text: str) -> str:
    """Clean up generated content with proper LaTeX formatting."""
    # Remove any repeated section headers
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

    # Fix double-escaped LaTeX
    text = text.replace('\\\\frac', '\\frac')
    text = text.replace('\\\\sqrt', '\\sqrt')
    text = text.replace('\\\\text', '\\text')
    text = text.replace('\\\\cdot', '\\cdot')
    text = text.replace('\\\\times', '\\times')

    # ── Fix LaTeX formatting ──
    text = _fix_latex_formatting(text)

    return text.strip()


def _fix_latex_formatting(text: str) -> str:
    """Ensure LaTeX is properly formatted for both Markdown and MathJax rendering.

    Fixes:
    1. Display math $$...$$ must be on its own line (not inline with text)
    2. Inline math $...$ must have spaces around it when next to text
    3. Multiple $$...$$ blocks on same line get split to separate lines
    """
    # Step 1: Split consecutive display math blocks onto separate lines.
    # Pattern: $$...$$$$...$$  → $$...$$ \n\n $$...$$
    text = re.sub(r'(\$\$[^$]+\$\$)(\s*)(\$\$)', r'\1\n\n\3', text)

    # Step 2: Ensure display math $$...$$ on its own line.
    # If text appears before $$, put $$ on new line.
    # Match: "some text$$formula$$" → "some text\n\n$$formula$$"
    text = re.sub(r'([^\n$])\s*(\$\$)(?!\$)', r'\1\n\n\2', text)
    # If text appears after $$...$$ (closing), put next text on new line.
    text = re.sub(r'(\$\$)([^\n$\s])', r'\1\n\n\2', text)

    # Step 3: Ensure spaces around inline $...$.
    # Add space before $ if preceded by a letter/digit (not another $)
    text = re.sub(r'([a-zA-Z0-9,;:})\]])\$(?!\$)', r'\1 $', text)
    # Add space after closing $ if followed by a letter/digit (not another $)
    text = re.sub(r'(?<!\$)\$([^$]+)\$([a-zA-Z0-9({\[])', lambda m: f'${m.group(1)}$ {m.group(2)}', text)

    # Step 4: Clean up excessive blank lines (max 2 consecutive)
    text = re.sub(r'\n{4,}', '\n\n\n', text)

    return text


# ═══════════ CHAPTER PROCESSING ═══════════

def generate_chapter_content(chunks_dir: str, output_dir: str,
                              grade: int = None, chapter_num: int = None):
    """Generate content for all topics in a chapter.

    Args:
        chunks_dir: Path to _all_chunks.json or directory with chunk files
        output_dir: Where to save generated markdown files
    """
    chunks_path = Path(chunks_dir)

    # Load chunks
    if chunks_path.is_file():
        with open(chunks_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        chunks = data["chunks"]
        grade = grade or data.get("grade", 10)
        chapter_num = chapter_num or data.get("chapter_number", 1)
        chapter_title = data.get("chapter_title", "Unknown")
    else:
        # Load from directory
        all_chunks_file = chunks_path / "_all_chunks.json"
        with open(all_chunks_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        chunks = data["chunks"]
        grade = grade or data.get("grade", 10)
        chapter_num = chapter_num or data.get("chapter_number", 1)
        chapter_title = data.get("chapter_title", "Unknown")

    out_dir = Path(output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    # Get all topic titles for context
    all_topics = [f"{c['topic_number']} {c['topic_title']}" for c in chunks]

    system_prompt = _build_system_prompt(grade)

    print(f"\n{'='*60}")
    print(f"Generating content for: Grade {grade} - Ch {chapter_num}: {chapter_title}")
    print(f"Topics: {len(chunks)}")
    print(f"{'='*60}\n")

    # Score topic importance using LLM
    print("  Scoring topic importance...", end=" ", flush=True)
    importance_scores = score_topic_importance(chunks, chapter_title, grade)
    for c, s in zip(chunks, importance_scores):
        print(f"    {c['topic_number']} {c['topic_title']}: {s}/5 {'⭐' * s}")
    print()

    # Free GPU memory after scoring before content generation
    gc.collect()
    torch.cuda.empty_cache()

    results = []
    for i, chunk in enumerate(chunks):
        topic_num = chunk["topic_number"]
        topic_title = chunk["topic_title"]
        importance = importance_scores[i]

        # Skip already-generated topics (resume support)
        safe_title = re.sub(r'[^\w\s-]', '', topic_title)
        safe_title = re.sub(r'\s+', '_', safe_title)[:50]
        filename = f"{topic_num}_{safe_title}.md"
        filepath = out_dir / filename
        if filepath.exists() and filepath.stat().st_size > 100:
            print(f"  [{i+1}/{len(chunks)}] {topic_num} {topic_title} — already exists, skipping")
            results.append({
                "topic_number": topic_num, "topic_title": topic_title,
                "file": filename, "importance": importance,
                "content_length": filepath.stat().st_size,
                "generation_time": 0, "skipped": True,
            })
            continue

        print(f"  [{i+1}/{len(chunks)}] {topic_num} {topic_title} (importance: {importance}/5)...", end=" ", flush=True)

        start = time.time()

        # Build prompt with importance-aware sections
        prompt = _build_topic_prompt(chunk, chapter_title, grade, all_topics, importance)

        # Scale max tokens by importance
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

        # Generate
        raw_content = generate_content(prompt, system_prompt, max_tokens)
        content = _clean_generated_content(raw_content)

        elapsed = time.time() - start
        print(f"({len(content)} chars, {elapsed:.1f}s)")

        # Save individual topic file
        with open(filepath, 'w', encoding='utf-8') as f:
            # Write header
            f.write(f"# {topic_num} {topic_title}\n\n")
            f.write(f"> **Grade {grade}** | **Chapter {chapter_num}: {chapter_title}**\n\n")
            f.write("---\n\n")
            f.write(content)
            f.write("\n")

        result = {
            "topic_number": topic_num,
            "topic_title": topic_title,
            "file": filename,
            "importance": importance,
            "content_length": len(content),
            "generation_time": round(elapsed, 1),
        }
        results.append(result)

        # Free GPU memory between topics to prevent OOM
        gc.collect()
        torch.cuda.empty_cache()

    # Save chapter index
    index = {
        "grade": grade,
        "chapter_number": chapter_num,
        "chapter_title": chapter_title,
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

    return index


# ═══════════ CLI ═══════════

if __name__ == "__main__":
    import sys

    base = Path(__file__).parent.parent

    if len(sys.argv) > 1 and sys.argv[1] == "test":
        # Quick model test
        print("Testing model loading and generation...")
        model, tokenizer = load_model()
        result = generate_content(
            "Explain the Pythagorean theorem in 3 sentences using LaTeX formulas.",
            "You are a math teacher. Use LaTeX for formulas: $...$ inline, $$...$$ display.",
            max_new_tokens=256,
        )
        print("\nGenerated:")
        print(result)

    elif len(sys.argv) > 2:
        # Generate for specific chapter: python content_gen.py <grade> <chapter> [--subject maths|science]
        grade = int(sys.argv[1])
        ch = int(sys.argv[2])

        # Parse --subject flag (default: maths)
        subject = "maths"
        if "--subject" in sys.argv:
            idx = sys.argv.index("--subject")
            subject = sys.argv[idx + 1]

        # Find chunks
        chunks_base = base / "data" / "intermediate" / "chunks"
        grade_dir = chunks_base / f"grade{grade}" / subject

        # Check for parts
        ch_dir = grade_dir / f"chapter{ch}"
        if not ch_dir.exists():
            # Try part1/part2
            for part in ["part1", "part2"]:
                ch_dir = grade_dir / part / f"chapter{ch}"
                if ch_dir.exists():
                    break

        if not ch_dir.exists():
            print(f"Chunks not found for grade {grade} {subject} chapter {ch}")
            sys.exit(1)

        chunks_file = ch_dir / "_all_chunks.json"
        output_dir = base / "data" / "output" / f"grade{grade}" / subject / f"chapter{ch}"

        generate_chapter_content(str(chunks_file), str(output_dir))

    else:
        # Default: generate for Grade 10 Chapter 1 (Real Numbers)
        chunks_file = base / "data" / "intermediate" / "chunks" / "grade10" / "maths" / "chapter1" / "_all_chunks.json"
        output_dir = base / "data" / "output" / "grade10" / "maths" / "chapter1"

        generate_chapter_content(str(chunks_file), str(output_dir))
