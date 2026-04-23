"""Dump all MongoDB translations to individual files for manual inspection."""
import json, os
from pymongo import MongoClient

client = MongoClient("mongodb+srv://sakshamchitkara:Saksham@cluster0.fx609kp.mongodb.net/btp-1")
db = client["btp-1"]
topics = list(db.topics.find({"grade": 9}, {"title": 1, "chapter": 1, "order": 1, "translations": 1, "_id": 1}))
print(f"Found {len(topics)} grade-9 topics")

dump_dir = "data/intermediate/translations_dump"
os.makedirs(dump_dir, exist_ok=True)

for t in sorted(topics, key=lambda x: (x["chapter"], x["order"])):
    ch = t["chapter"]
    order = t["order"]
    trans = t.get("translations", {})
    for lang in ["hi", "te", "od"]:
        if lang in trans:
            c = trans[lang].get("content", "")
            fname = f"ch{ch}_t{order}_{lang}.html"
            path = os.path.join(dump_dir, fname)
            with open(path, "w", encoding="utf-8") as f:
                f.write(c)
            print(f"  Wrote {fname} ({len(c)} chars)")

client.close()
print(f"\nDumped to {dump_dir}/")
