"""
PDF Font Analysis Script
Analyzes font usage across NCERT science PDFs to identify:
1. What formatting "normal body text" uses consistently
2. What formatting differs (i.e., headings)
"""

import fitz  # PyMuPDF
import os
import sys
from collections import Counter, defaultdict

DATA_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data', 'input')


def analyze_pdf_fonts(pdf_path, max_pages=10):
    """Extract all text spans with their font info from a PDF."""
    doc = fitz.open(pdf_path)
    spans_info = []
    
    for page_num in range(min(len(doc), max_pages)):
        page = doc[page_num]
        blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]
        
        for block in blocks:
            if block["type"] != 0:  # text blocks only
                continue
            for line in block["lines"]:
                for span in line["spans"]:
                    text = span["text"].strip()
                    if not text or len(text) < 2:
                        continue
                    spans_info.append({
                        "text": text[:80],
                        "font": span["font"],
                        "size": round(span["size"], 1),
                        "flags": span["flags"],  # bold=16, italic=2, etc.
                        "color": span["color"],
                        "page": page_num + 1,
                        "len": len(text),
                    })
    
    doc.close()
    return spans_info


def classify_flags(flags):
    """Decode font flags into readable format."""
    parts = []
    if flags & 16:
        parts.append("BOLD")
    if flags & 2:
        parts.append("ITALIC")
    if flags & 1:
        parts.append("SUPERSCRIPT")
    if flags & 4:
        parts.append("SERIF")
    if flags & 8:
        parts.append("MONO")
    return "+".join(parts) if parts else "REGULAR"


def get_font_signature(span):
    """Create a signature string for a span's formatting."""
    return f"{span['font']}|{span['size']}|{classify_flags(span['flags'])}"


def analyze_single_pdf(pdf_path, label=""):
    """Analyze one PDF and return font distribution."""
    spans = analyze_pdf_fonts(pdf_path, max_pages=15)
    if not spans:
        return None
    
    # Count characters per font signature
    sig_chars = Counter()
    sig_examples = defaultdict(list)
    
    for s in spans:
        sig = get_font_signature(s)
        sig_chars[sig] += s["len"]
        if len(sig_examples[sig]) < 3:
            sig_examples[sig].append(s["text"][:60])
    
    return sig_chars, sig_examples, spans


def main():
    # Collect science PDFs across grades
    pdfs_to_check = []
    
    for grade_dir in sorted(os.listdir(DATA_DIR)):
        grade_path = os.path.join(DATA_DIR, grade_dir)
        if not os.path.isdir(grade_path):
            continue
        
        for subject in ['science']:
            subject_path = os.path.join(grade_path, subject)
            if not os.path.isdir(subject_path):
                continue
            
            files = sorted([f for f in os.listdir(subject_path) if f.endswith('.pdf')])
            # Take first 2 and last 1 chapter from each grade
            selected = files[:2] + files[-1:]
            for f in selected:
                pdfs_to_check.append((
                    os.path.join(subject_path, f),
                    f"{grade_dir}/{subject}/{f}"
                ))
    
    # Also check a few physics/chemistry if they exist (grade 11/12)
    for grade_dir in ['grade11', 'grade12']:
        for subject in ['physics', 'biology', 'chemistry']:
            for part in ['', 'part1', 'part2']:
                subject_path = os.path.join(DATA_DIR, grade_dir, subject, part) if part else os.path.join(DATA_DIR, grade_dir, subject)
                if not os.path.isdir(subject_path):
                    continue
                files = sorted([f for f in os.listdir(subject_path) if f.endswith('.pdf')])
                if files:
                    pdfs_to_check.append((
                        os.path.join(subject_path, files[0]),
                        f"{grade_dir}/{subject}/{part + '/' if part else ''}{files[0]}"
                    ))
                    break  # one per subject per grade
    
    print("=" * 90)
    print("NCERT PDF FONT ANALYSIS — Finding 'Normal Body Text' Signature")
    print("=" * 90)
    
    # Global tracking: which font signature has the MOST text across ALL PDFs
    global_sig_chars = Counter()
    per_pdf_dominant = {}
    
    for pdf_path, label in pdfs_to_check:
        result = analyze_single_pdf(pdf_path, label)
        if not result:
            print(f"\n⚠️  {label}: Could not analyze")
            continue
        
        sig_chars, sig_examples, spans = result
        
        # Find dominant (body) font: the one with most characters
        dominant_sig = sig_chars.most_common(1)[0][0]
        total_chars = sum(sig_chars.values())
        dominant_pct = sig_chars[dominant_sig] / total_chars * 100
        
        per_pdf_dominant[label] = dominant_sig
        
        for sig, chars in sig_chars.items():
            global_sig_chars[sig] += chars
        
        print(f"\n{'─' * 90}")
        print(f"📄 {label}")
        print(f"   Total spans analyzed: {len(spans)}, Total chars: {total_chars}")
        print(f"   DOMINANT (body) font: {dominant_sig} ({dominant_pct:.1f}% of text)")
        print(f"   All font signatures (by char count):")
        
        for sig, chars in sig_chars.most_common(10):
            pct = chars / total_chars * 100
            is_body = "◀ BODY" if sig == dominant_sig else ""
            examples = sig_examples[sig]
            print(f"     {pct:5.1f}% │ {chars:6d} chars │ {sig}")
            for ex in examples[:2]:
                print(f"           │          │   \"{ex}\"")
    
    # Summary
    print(f"\n{'═' * 90}")
    print(f"SUMMARY: Dominant font per PDF")
    print(f"{'═' * 90}")
    
    body_sigs = Counter()
    for label, sig in per_pdf_dominant.items():
        body_sigs[sig] += 1
        print(f"  {label:55s} → {sig}")
    
    print(f"\n{'═' * 90}")
    print(f"BODY FONT CONSISTENCY CHECK")
    print(f"{'═' * 90}")
    for sig, count in body_sigs.most_common():
        print(f"  {count:3d} PDFs use: {sig}")
    
    # The key insight
    print(f"\n{'═' * 90}")
    print(f"CONCLUSION: NON-BODY = HEADING APPROACH")
    print(f"{'═' * 90}")
    most_common_body = body_sigs.most_common(1)[0][0]
    body_font, body_size, body_style = most_common_body.split("|")
    print(f"  Most common body text format:")
    print(f"    Font:  {body_font}")
    print(f"    Size:  {body_size}")
    print(f"    Style: {body_style}")
    print(f"\n  → Any text NOT matching this signature is likely a HEADING")
    print(f"  → This 'negation logic' approach should work if body text is consistent!")


if __name__ == "__main__":
    main()
