"""
Fix markdown table rendering in MongoDB translations.

Reads each dumped translation HTML file, converts <p>|...|</p> patterns
to proper <table> HTML, saves the fixed file, then updates MongoDB.

This does NOT re-run translation or any pipeline step. It only fixes
the table display issue in already-translated content.
"""
import os
import re
from pymongo import MongoClient


DUMP_DIR = "data/intermediate/translations_dump"
MONGO_URI = "mongodb+srv://sakshamchitkara:Saksham@cluster0.fx609kp.mongodb.net/btp-1"


def fix_tables_in_html(html: str) -> str:
    """Convert <p>|...|</p> sequences to proper <table> HTML."""

    # Split into lines (may be single-line with \n)
    lines = html.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Check if this line is a table row: <p>| ... |</p>
        if re.match(r'^<p>\|.*\|</p>$', line.strip()):
            # Collect all consecutive table rows
            table_rows = []
            while i < len(lines) and re.match(r'^<p>\|.*\|</p>$', lines[i].strip()):
                row_text = lines[i].strip()
                # Extract content between <p>| and |</p>
                inner = row_text[3:-4]  # Remove <p> and </p>
                table_rows.append(inner)
                i += 1

            # Build HTML table
            table_html = '<div class="table-wrap"><table class="key-formulas">'

            first_data = True
            for row in table_rows:
                # Skip separator rows like |--------|-------------|
                cells_raw = row.strip("|").split("|")
                cells = [c.strip() for c in cells_raw]

                # Check if this is a separator row
                if all(re.match(r'^[-:_\s]+$', c) for c in cells):
                    continue

                if first_data:
                    # First row = header
                    table_html += "<tr>" + "".join(f"<th>{c}</th>" for c in cells) + "</tr>"
                    first_data = False
                else:
                    table_html += "<tr>" + "".join(f"<td>{c}</td>" for c in cells) + "</tr>"

            table_html += "</table></div>"
            result.append(table_html)
        else:
            result.append(line)
            i += 1

    return "\n".join(result)


def main():
    # Connect to MongoDB
    client = MongoClient(MONGO_URI)
    db = client["btp-1"]
    topics_col = db["topics"]

    # Get all grade 9 topics
    topics = list(topics_col.find({"grade": 9}, {"title": 1, "chapter": 1, "order": 1, "translations": 1}))
    print(f"Found {len(topics)} grade-9 topics in MongoDB")

    # Build lookup by (ch, order)
    topic_lookup = {}
    for t in topics:
        topic_lookup[(t["chapter"], t["order"])] = t

    # Process each dumped file
    files = sorted(os.listdir(DUMP_DIR))
    fixed_count = 0
    uploaded_count = 0

    for fname in files:
        if not fname.endswith(".html"):
            continue

        # Parse filename: ch1_t1_hi.html
        m = re.match(r"ch(\d+)_t(\d+)_(\w+)\.html", fname)
        if not m:
            print(f"  SKIP: Cannot parse filename {fname}")
            continue

        ch = int(m.group(1))
        order = int(m.group(2))
        lang = m.group(3)

        filepath = os.path.join(DUMP_DIR, fname)
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()

        # Check if there are markdown tables to fix
        has_md_table = bool(re.search(r'<p>\|.*\|</p>', html))
        if not has_md_table:
            print(f"  {fname}: No markdown tables found (already clean)")
            continue

        # Fix tables
        fixed_html = fix_tables_in_html(html)

        # Verify fix worked
        still_has_md = bool(re.search(r'<p>\|.*\|</p>', fixed_html))
        has_html_table = "<table" in fixed_html

        if still_has_md:
            print(f"  WARNING {fname}: Still has markdown tables after fix!")
        if not has_html_table:
            print(f"  WARNING {fname}: No HTML table found after fix!")

        # Save fixed file
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(fixed_html)
        fixed_count += 1

        # Show table excerpt
        table_match = re.search(r'<div class="table-wrap">.*?</div>', fixed_html)
        if table_match:
            excerpt = table_match.group(0)[:150]
            print(f"  {fname}: FIXED ✓  table={excerpt}...")

        # Upload to MongoDB
        topic_doc = topic_lookup.get((ch, order))
        if topic_doc:
            result = topics_col.update_one(
                {"_id": topic_doc["_id"]},
                {"$set": {f"translations.{lang}.content": fixed_html}}
            )
            if result.modified_count > 0:
                uploaded_count += 1
                print(f"    → MongoDB updated ✓")
            else:
                print(f"    → MongoDB: no change (already up to date)")
        else:
            print(f"    → MongoDB: topic not found for ch{ch} t{order}")

    print(f"\nSummary: {fixed_count} files fixed, {uploaded_count} MongoDB docs updated")
    client.close()


if __name__ == "__main__":
    main()
