"""
Fix related topic links in translated content.

Converts plain text [X.Y Topic Name] references to proper <a> tags
with correct MongoDB ObjectId hrefs. Also adds ?lang= parameter
so clicking a link preserves the current language.
"""
import os
import re
from pymongo import MongoClient

DUMP_DIR = "data/intermediate/translations_dump"
MONGO_URI = "mongodb+srv://sakshamchitkara:Saksham@cluster0.fx609kp.mongodb.net/btp-1"


def main():
    client = MongoClient(MONGO_URI)
    db = client["btp-1"]

    # Get all grade 9 topics
    topics = list(db.topics.find({"grade": 9}, {
        "title": 1, "chapter": 1, "order": 1, "translations": 1, "_id": 1
    }))
    print(f"Found {len(topics)} grade-9 topics")

    # Build mapping: (chapter, order) -> (ObjectId, title)
    topic_map = {}
    for t in topics:
        topic_map[(t["chapter"], t["order"])] = {
            "id": str(t["_id"]),
            "title": t["title"],
            "chapter": t["chapter"],
        }

    print("\nTopic mapping:")
    for (ch, order), info in sorted(topic_map.items()):
        print(f"  {ch}.{order} -> {info['id']}  {info['title']}")

    # Process each dumped file
    files = sorted(os.listdir(DUMP_DIR))
    fixed_count = 0
    uploaded_count = 0

    for fname in files:
        if not fname.endswith(".html"):
            continue

        m = re.match(r"ch(\d+)_t(\d+)_(\w+)\.html", fname)
        if not m:
            continue

        ch = int(m.group(1))
        order = int(m.group(2))
        lang = m.group(3)

        filepath = os.path.join(DUMP_DIR, fname)
        with open(filepath, "r", encoding="utf-8") as f:
            html = f.read()

        original = html

        # Find [X.Y Any Text] patterns and convert to proper links
        def replace_link(match):
            full = match.group(0)
            link_text = match.group(1)

            # Extract chapter.topic number from the beginning
            num_match = re.match(r"(\d+)\.(\d+)", link_text)
            if not num_match:
                return full  # Can't parse, leave as is

            ref_ch = int(num_match.group(1))
            ref_order = int(num_match.group(2))

            info = topic_map.get((ref_ch, ref_order))
            if not info:
                print(f"    WARNING: No topic found for {ref_ch}.{ref_order} in {fname}")
                return full

            href = f"/grade/9/maths/chapter/{ref_ch}/topic/{info['id']}?lang={lang}"
            return f'<a href="{href}" class="related-link">{link_text}</a>'

        # Replace [X.Y ...] patterns that appear inside <li> tags
        html = re.sub(r'\[(\d+\.\d+[^\]]*)\]', replace_link, html)

        if html != original:
            # Save fixed file
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            fixed_count += 1

            # Count links fixed
            links_added = len(re.findall(r'class="related-link"', html))
            print(f"  {fname}: {links_added} links fixed")

            # Upload to MongoDB
            topic_doc = topic_map.get((ch, order))
            if topic_doc:
                result = db.topics.update_one(
                    {"_id": topics[0]["_id"]},  # placeholder
                    {"$set": {f"translations.{lang}.content": html}}
                )
            # Find the actual topic doc
            for t in topics:
                if t["chapter"] == ch and t["order"] == order:
                    result = db.topics.update_one(
                        {"_id": t["_id"]},
                        {"$set": {f"translations.{lang}.content": html}}
                    )
                    if result.modified_count > 0:
                        uploaded_count += 1
                        print(f"    -> MongoDB updated")
                    break
        else:
            print(f"  {fname}: No [X.Y] links found to fix")

    print(f"\nSummary: {fixed_count} files fixed, {uploaded_count} uploads")
    client.close()


if __name__ == "__main__":
    main()
