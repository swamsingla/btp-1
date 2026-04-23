"""Fix the remaining ch1_t5 files that have different link formats."""
import re, os
from pymongo import MongoClient

DUMP_DIR = "data/intermediate/translations_dump"
MONGO_URI = "mongodb+srv://sakshamchitkara:Saksham@cluster0.fx609kp.mongodb.net/btp-1"

# Topic ID mapping for chapter 1
TOPIC_IDS = {
    (1, 1): "69d627ac50a9caef8096975b",
    (1, 2): "69d627ac50a9caef8096975c",
    (1, 3): "69d627ac50a9caef8096975d",
    (1, 4): "69d627ac50a9caef8096975e",
    (1, 5): "69d627ac50a9caef8096975f",
}

client = MongoClient(MONGO_URI)
db = client["btp-1"]

for lang in ["hi", "te", "od"]:
    fname = f"ch1_t5_{lang}.html"
    filepath = os.path.join(DUMP_DIR, fname)
    
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()

    # Find the Related Topics section (last <h2> to end)
    last_h2 = html.rfind("<h2>")
    before = html[:last_h2]
    section = html[last_h2:]

    # Rebuild the Related Topics section with proper links
    # Extract each <li> item
    items = re.findall(r'<li>(.*?)</li>', section, re.DOTALL)
    
    new_items = []
    for item in items:
        # Try to extract X.Y number from the item
        num_match = re.search(r'(\d+)\.(\d+)', item)
        if num_match:
            ref_ch = int(num_match.group(1))
            ref_order = int(num_match.group(2))
            topic_id = TOPIC_IDS.get((ref_ch, ref_order))
            
            if topic_id:
                # Clean up the text: remove <strong>, **, etc.
                clean = item
                clean = re.sub(r'</?strong>', '', clean)
                clean = re.sub(r'\*\*', '', clean)
                clean = clean.strip()
                
                # Split into link text and description at " — "
                parts = clean.split(' — ', 1)
                link_text = parts[0].strip()
                desc = f" — {parts[1].strip()}" if len(parts) > 1 else ""
                
                href = f"/grade/9/maths/chapter/{ref_ch}/topic/{topic_id}?lang={lang}"
                new_item = f'<a href="{href}" class="related-link">{link_text}</a>{desc}'
                new_items.append(new_item)
                continue
        
        new_items.append(item)

    # Rebuild section
    # Get the h2 line
    h2_match = re.match(r'(<h2>.*?</h2>)', section)
    h2_line = h2_match.group(1) if h2_match else "<h2>Related Topics</h2>"
    
    new_section = f"{h2_line}\n<ul>\n"
    for item in new_items:
        new_section += f"<li>{item}</li>\n"
    new_section += "</ul>"

    html = before + new_section

    with open(filepath, "w", encoding="utf-8") as f:
        f.write(html)

    # Upload to MongoDB
    topic = db.topics.find_one({"grade": 9, "chapter": 1, "order": 5})
    result = db.topics.update_one(
        {"_id": topic["_id"]},
        {"$set": {f"translations.{lang}.content": html}}
    )
    status = "updated" if result.modified_count > 0 else "no change"
    
    # Count links
    link_count = len(re.findall(r'related-link', html))
    print(f"  {fname}: {link_count} links, MongoDB {status}")

client.close()
print("Done!")
