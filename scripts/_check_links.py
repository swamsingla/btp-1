"""Check link format in English and translated content."""
import re
from pymongo import MongoClient

client = MongoClient("mongodb+srv://sakshamchitkara:Saksham@cluster0.fx609kp.mongodb.net/btp-1")
db = client["btp-1"]

topics = list(db.topics.find({"grade": 9}, {"content": 1, "title": 1, "chapter": 1, "order": 1, "translations": 1, "_id": 1}))

print("=== ENGLISH LINKS ===")
for t in sorted(topics, key=lambda x: (x["chapter"], x["order"])):
    links = re.findall(r'href="([^"]+)"', t["content"])
    related = [l for l in links if "topic" in l]
    print(f"Ch{t['chapter']} T{t['order']} {t['title'][:30]}: {related[:3]}")

print("\n=== TRANSLATED LINKS (hi) ===")
for t in sorted(topics, key=lambda x: (x["chapter"], x["order"])):
    hi = t.get("translations", {}).get("hi", {}).get("content", "")
    # Check for markdown-style links [text]
    md_links = re.findall(r'\[(\d+\.\d+[^\]]*)\]', hi)
    # Check for proper <a> links
    a_links = re.findall(r'href="([^"]+)"', hi)
    related = [l for l in a_links if "topic" in l]
    print(f"Ch{t['chapter']} T{t['order']}: md_links={md_links[:3]}  a_links={related[:3]}")

print("\n=== TOPIC ID MAPPING ===")
for t in sorted(topics, key=lambda x: (x["chapter"], x["order"])):
    print(f"Ch{t['chapter']} T{t['order']} -> {t['_id']}  {t['title'][:40]}")

client.close()
