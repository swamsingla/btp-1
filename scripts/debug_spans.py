"""Quick debug: examine raw spans from a problematic PDF to understand repeated text."""
import fitz
import os

pdf_path = "/home/swamsingla/btp-1/data/input/grade12/chemistry/part1/chapter1.pdf"
doc = fitz.open(pdf_path)

# Check first 3 pages
for pn in range(min(3, len(doc))):
    page = doc[pn]
    blocks = page.get_text("dict", flags=fitz.TEXT_PRESERVE_WHITESPACE)["blocks"]
    print(f"\n=== PAGE {pn+1} ===")
    for block in blocks:
        if block["type"] != 0:
            continue
        for line in block["lines"]:
            for span in line["spans"]:
                text = span["text"].strip()
                if not text:
                    continue
                size = round(span["size"], 1)
                font = span["font"]
                # Only show non-body-text spans (body is BookmanOldStyle at ~10.5)
                if "BookmanOldStyle" in font and 10.0 <= size <= 11.0:
                    continue
                print(f"  [{size:5.1f}] [{font:30s}] \"{text}\"")

doc.close()
