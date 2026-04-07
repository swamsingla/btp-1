"""
NCERT Science Books — Heading Extractor (Negation Logic) v2

Strategy:
  1. For each PDF, find the "body text" font signature (most chars).
  2. Any text NOT matching the body signature is a candidate heading.
  3. Handle decorative PDF artifacts:
     - Repeated shadow-text spans (same text, same position, 3-5 copies)
     - Split headings: "1.1.1 M" + "ATTER IS MADE UP OF PARTICLES" 
     - First-letter-large + small-caps-rest patterns
  4. Filter noise (page numbers, footers, figure captions, etc.)
  5. Assign hierarchy levels based on font size.
  6. Output structured JSON per grade/subject.
"""

import fitz  # PyMuPDF
import os
import sys
import json
import re
from collections import Counter, defaultdict

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data', 'input')
OUTPUT_DIR = os.path.join(BASE_DIR, 'data', 'headings')

# ─── Noise filters ───────────────────────────────────────────────────────────

SKIP_PATTERNS = [
    re.compile(r'^Reprint\s+\d{4}', re.IGNORECASE),
    re.compile(r'^\d+$'),                         # bare page numbers
    re.compile(r'^[ivxlcdm]+$', re.IGNORECASE),   # roman numerals alone
    re.compile(r'^\(?\s*[a-e]\s*\)?$'),            # (a), (b), etc.
    re.compile(r'^\(?\s*[ivx]+\s*\)?$', re.IGNORECASE),
    re.compile(r'^Fig(\.|ure)\s*\d', re.IGNORECASE),
    re.compile(r'^©'),
    re.compile(r'^Textbook\s+of', re.IGNORECASE),
    re.compile(r'^Curiosity\s', re.IGNORECASE),
    re.compile(r'^\d{4}-\d{2,4}$'),               # year ranges
    re.compile(r'^[A-Z]{1,3}\d+$'),                # like "NO2", "CO2"
    re.compile(r'^\d+\s*/\s*\d+'),                 # fractions
]

# Fonts that are always noise (watermarks, headers, footers)
NOISE_FONTS = {'Arial', 'MyriadPro', 'Oswald', 'Poppins'}

MIN_HEADING_LEN = 4
MAX_HEADING_LEN = 150


def should_skip_text(text):
    """Check if cleaned text should be skipped."""
    text = text.strip()
    if len(text) < MIN_HEADING_LEN:
        return True
    if len(text) > MAX_HEADING_LEN:
        return True
    for pat in SKIP_PATTERNS:
        if pat.search(text):
            return True
    return False


def is_noise_font(font_name):
    """Check if a font is a known noise font."""
    for nf in NOISE_FONTS:
        if nf.lower() in font_name.lower():
            return True
    return False


def get_font_sig(span):
    """Create font signature tuple."""
    return (span['font'], round(span['size'], 1), span['flags'])


def extract_all_spans(pdf_path):
    """Extract all text spans from a PDF with position info."""
    doc = fitz.open(pdf_path)
    all_spans = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]
        
        for block in blocks:
            if block["type"] != 0:
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text:
                        continue
                    all_spans.append({
                        "text": text,
                        "font": span["font"],
                        "size": round(span["size"], 1),
                        "flags": span["flags"],
                        "color": span["color"],
                        "page": page_num + 1,
                        "bbox": list(span["bbox"]),
                        "y": round(span["origin"][1], 1),
                        "x": round(span["origin"][0], 1),
                    })
    
    doc.close()
    return all_spans


def deduplicate_shadow_spans(spans):
    """
    Remove duplicate shadow/overlay spans.
    Many NCERT PDFs have decorative text rendered 3-5 times at identical positions.
    Keep only one copy of each unique (page, text, y-position) combo.
    """
    seen = set()
    deduped = []
    
    for s in spans:
        # Key: page + text + approximate y position (within 1 pt)
        key = (s["page"], s["text"], round(s["y"] / 1.0))
        if key in seen:
            continue
        seen.add(key)
        deduped.append(s)
    
    return deduped


def find_body_signatures(spans):
    """
    Find body text font signatures — the formatting covering most characters.
    Include closely related variants (same font base, slightly different sizes,
    italic versions of the same family) as body text too.
    """
    sig_chars = Counter()
    sig_to_info = {}
    
    for s in spans:
        sig = get_font_sig(s)
        sig_chars[sig] += len(s["text"])
        if sig not in sig_to_info:
            sig_to_info[sig] = {"font": s["font"], "size": s["size"], "flags": s["flags"]}
    
    if not sig_chars:
        return set(), 10.0
    
    total_chars = sum(sig_chars.values())
    primary_sig = sig_chars.most_common(1)[0][0]
    primary_info = sig_to_info[primary_sig]
    primary_font_base = re.split(r'[-,]', primary_info["font"])[0].lower()
    
    body_sigs = {primary_sig}
    
    for sig, chars in sig_chars.items():
        info = sig_to_info[sig]
        font_base = re.split(r'[-,]', info["font"])[0].lower()
        size_diff = abs(info["size"] - primary_info["size"])
        
        # Same font family, size ≤ body size (or barely larger): body text
        if font_base == primary_font_base and info["size"] <= primary_info["size"] + 0.5:
            body_sigs.add(sig)
        # Symbol font at body size → inline math, not a heading
        elif info["font"] == "Symbol" and size_diff <= 2.0:
            body_sigs.add(sig)
    
    return body_sigs, primary_info["size"]


def merge_heading_line_spans(candidate_spans):
    """
    Merge spans that form a single heading line.
    
    Handles:
    - "1.1.1 M" + "ATTER IS MADE UP OF PARTICLES" (first-letter-large + small-caps)
    - Consecutive spans of same font on same line
    - Multi-line headings with same decorative font on consecutive lines
    """
    if not candidate_spans:
        return []
    
    # Sort by page, then y position, then x position
    sorted_spans = sorted(candidate_spans, key=lambda s: (s["page"], s["y"], s["x"]))
    
    merged = []
    current_group = [sorted_spans[0]]
    
    for span in sorted_spans[1:]:
        prev = current_group[-1]
        same_page = span["page"] == prev["page"]
        
        # Same font family (base name)
        prev_base = re.split(r'[-,]', prev["font"])[0].lower()
        span_base = re.split(r'[-,]', span["font"])[0].lower()
        same_family = prev_base == span_base
        
        # Same line: y-origins within 3pt
        same_line = same_page and abs(span["y"] - prev["y"]) <= 3.0
        
        # Adjacent line: y within 25pt from group start (multi-line heading)
        adjacent_line = same_page and abs(span["y"] - current_group[0]["y"]) <= 30.0
        
        if same_page and same_family and (same_line or adjacent_line):
            current_group.append(span)
        elif same_page and same_line:
            # Different font family but on same line — likely first-letter-large pattern
            current_group.append(span)
        else:
            merged.append(current_group)
            current_group = [span]
    
    merged.append(current_group)
    
    # Convert groups to single heading entries
    result = []
    for group in merged:
        texts = [s["text"] for s in group]
        combined = " ".join(texts)
        max_size = max(s["size"] for s in group)
        main_span = max(group, key=lambda s: s["size"])
        
        result.append({
            "text": combined,
            "font": main_span["font"],
            "size": max_size,
            "flags": main_span["flags"],
            "page": group[0]["page"],
            "y": group[0]["y"],
        })
    
    return result


def reconstruct_small_caps_heading(text):
    """
    Reconstruct headings split by first-letter-large + rest-small-caps.
    E.g. "M ATTER IS MADE UP OF" → "MATTER IS MADE UP OF"
    """
    # Pattern: single uppercase letter + space + uppercase word
    text = re.sub(r'\b([A-Z])\s+([A-Z]{2,})\b', lambda m: m.group(1) + m.group(2), text)
    return text


def clean_heading_text(text):
    """Clean heading text: normalize whitespace, fix artifacts."""
    text = re.sub(r'\s+', ' ', text).strip()
    
    # Remove decorative underscores/dashes
    text = re.sub(r'[_]{2,}\s*', ' ', text)
    text = re.sub(r'^[_\-=]+\s*', '', text)
    text = re.sub(r'\s*[_\-=]+$', '', text)
    
    # Reconstruct small-caps headings
    text = reconstruct_small_caps_heading(text)
    
    # Remove trailing lone punctuation
    text = re.sub(r'\s+[?.]$', '', text)
    
    # Remove lone numbers at end (page numbers that snuck in)
    text = re.sub(r'\s+\d{1,3}$', '', text)
    
    return text.strip()


def extract_headings_from_pdf(pdf_path):
    """
    Main extraction logic for a single PDF.
    Returns list of heading dicts: {text, level, page, font_size}
    """
    spans = extract_all_spans(pdf_path)
    if not spans:
        return []
    
    # Step 1: Deduplicate shadow/overlay spans
    spans = deduplicate_shadow_spans(spans)
    
    # Step 2: Remove noise font spans
    spans = [s for s in spans if not is_noise_font(s["font"])]
    
    # Step 3: Find body text signatures
    body_sigs, body_size = find_body_signatures(spans)
    
    # Step 4: Everything NOT body → candidate heading
    candidates = []
    for s in spans:
        sig = get_font_sig(s)
        if sig not in body_sigs:
            candidates.append(s)
    
    if not candidates:
        return []
    
    # Step 5: Merge related spans into heading lines
    merged = merge_heading_line_spans(candidates)
    
    # Step 6: Clean and filter
    headings = []
    for h in merged:
        text = clean_heading_text(h["text"])
        
        if should_skip_text(text):
            continue
        
        # Skip if font size is much smaller than body (footnotes/captions at unusual font)
        if h["size"] < body_size - 2.0:
            continue
        
        h["text"] = text
        headings.append(h)
    
    if not headings:
        return []
    
    # Step 7: Assign heading levels based on font size
    heading_sizes = sorted(set(h["size"] for h in headings), reverse=True)
    
    size_to_level = {}
    for i, size in enumerate(heading_sizes):
        if i == 0:
            size_to_level[size] = 1
        elif i == 1:
            size_to_level[size] = 2
        elif i == 2:
            size_to_level[size] = 3
        else:
            size_to_level[size] = 4
    
    results = []
    seen_texts = set()
    
    for h in headings:
        text = h["text"]
        
        # Skip exact duplicate headings
        text_key = re.sub(r'\s+', '', text.lower())
        if text_key in seen_texts:
            continue
        seen_texts.add(text_key)
        
        level = size_to_level.get(h["size"], 4)
        
        results.append({
            "text": text,
            "level": level,
            "page": h["page"],
            "font_size": h["size"],
        })
    
    return results


def discover_science_pdfs():
    """Find all science-related PDFs organized by grade/subject."""
    pdfs = []
    
    for grade_dir in sorted(os.listdir(DATA_DIR)):
        grade_path = os.path.join(DATA_DIR, grade_dir)
        if not os.path.isdir(grade_path):
            continue
        
        grade_num = grade_dir.replace('grade', '')
        
        for subject in ['science', 'physics', 'chemistry', 'biology']:
            subject_path = os.path.join(grade_path, subject)
            if not os.path.isdir(subject_path):
                continue
            
            subdirs = [d for d in os.listdir(subject_path)
                       if os.path.isdir(os.path.join(subject_path, d)) and d.startswith('part')]
            
            if subdirs:
                for part in sorted(subdirs):
                    part_path = os.path.join(subject_path, part)
                    files = sorted(
                        [f for f in os.listdir(part_path) if f.endswith('.pdf')],
                        key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0
                    )
                    for f in files:
                        ch_num = re.search(r'chapter(\d+)', f)
                        pdfs.append({
                            "path": os.path.join(part_path, f),
                            "grade": grade_num,
                            "subject": subject,
                            "part": part,
                            "chapter": ch_num.group(1) if ch_num else f,
                            "label": f"{grade_dir}/{subject}/{part}/{f}",
                        })
            else:
                files = sorted(
                    [f for f in os.listdir(subject_path) if f.endswith('.pdf')],
                    key=lambda x: int(re.search(r'\d+', x).group()) if re.search(r'\d+', x) else 0
                )
                for f in files:
                    ch_num = re.search(r'chapter(\d+)', f)
                    pdfs.append({
                        "path": os.path.join(subject_path, f),
                        "grade": grade_num,
                        "subject": subject,
                        "part": None,
                        "chapter": ch_num.group(1) if ch_num else f,
                        "label": f"{grade_dir}/{subject}/{f}",
                    })
    
    return pdfs


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    
    pdfs = discover_science_pdfs()
    print(f"Found {len(pdfs)} science PDFs to process\n")
    
    all_results = {}
    total_headings = 0
    errors = []
    
    for i, pdf_info in enumerate(pdfs):
        label = pdf_info["label"]
        sys.stdout.write(f"\r[{i+1:3d}/{len(pdfs)}] Processing {label:<60s}")
        sys.stdout.flush()
        
        try:
            headings = extract_headings_from_pdf(pdf_info["path"])
        except Exception as e:
            errors.append(f"{label}: {str(e)}")
            headings = []
        
        grade_key = f"grade{pdf_info['grade']}"
        subject_key = pdf_info["subject"]
        if pdf_info["part"]:
            subject_key = f"{subject_key}_{pdf_info['part']}"
        
        if grade_key not in all_results:
            all_results[grade_key] = {}
        if subject_key not in all_results[grade_key]:
            all_results[grade_key][subject_key] = {}
        
        chapter_key = f"chapter{pdf_info['chapter']}"
        all_results[grade_key][subject_key][chapter_key] = headings
        total_headings += len(headings)
    
    print(f"\n\nDone! Extracted {total_headings} headings from {len(pdfs)} PDFs")
    
    if errors:
        print(f"\n⚠️  Errors ({len(errors)}):")
        for e in errors:
            print(f"   {e}")
    
    # Save full JSON
    output_file = os.path.join(OUTPUT_DIR, "all_science_headings.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(all_results, f, indent=2, ensure_ascii=False)
    print(f"\n📄 Full results saved to: {output_file}")
    
    # Save per-grade files
    for grade, subjects in sorted(all_results.items()):
        grade_file = os.path.join(OUTPUT_DIR, f"{grade}_headings.json")
        with open(grade_file, 'w', encoding='utf-8') as f:
            json.dump(subjects, f, indent=2, ensure_ascii=False)
    
    # Print readable summary
    print(f"\n{'═' * 100}")
    print(f"EXTRACTION SUMMARY")
    print(f"{'═' * 100}")
    
    for grade in sorted(all_results.keys(), key=lambda g: int(g.replace('grade', ''))):
        subjects = all_results[grade]
        for subject in sorted(subjects.keys()):
            chapters = subjects[subject]
            for ch_key in sorted(chapters.keys(), key=lambda c: int(c.replace('chapter', ''))):
                headings = chapters[ch_key]
                count = len(headings)
                if count > 0:
                    print(f"\n  📘 {grade}/{subject}/{ch_key} — {count} headings:")
                    for h in headings:
                        lvl = h["level"]
                        indent = "  " * lvl
                        marker = "■" if lvl == 1 else "▪" if lvl == 2 else "●" if lvl == 3 else "○"
                        print(f"    {indent}{marker} {h['text'][:90]}")
                else:
                    print(f"\n  ⚠️  {grade}/{subject}/{ch_key} — 0 headings")


if __name__ == "__main__":
    main()
