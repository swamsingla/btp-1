"""Verify all translations have proper related-link anchors in MongoDB."""
import re
from pymongo import MongoClient

client = MongoClient("mongodb+srv://sakshamchitkara:Saksham@cluster0.fx609kp.mongodb.net/btp-1")
db = client["btp-1"]
topics = list(db.topics.find({"grade": 9}, {"chapter": 1, "order": 1, "translations": 1, "title": 1}))

all_ok = True
for t in sorted(topics, key=lambda x: (x["chapter"], x["order"])):
    ch = t["chapter"]
    order = t["order"]
    for lang in ["hi", "te", "od"]:
        c = t.get("translations", {}).get(lang, {}).get("content", "")
        has_links = "related-link" in c
        link_count = c.count("related-link")
        # Check for remaining broken refs
        bracket_refs = re.findall(r'\[(\d+\.\d+[^\]]*)\]', c)
        status = "OK" if has_links else "NO LINKS"
        if not has_links:
            all_ok = False
        extra = ""
        if bracket_refs:
            extra = f" STILL_BROKEN={bracket_refs}"
            all_ok = False
        print(f"  Ch{ch} T{order} [{lang}] {status} ({link_count} links){extra}")

print()
print("ALL GOOD!" if all_ok else "SOME ISSUES REMAIN")

# Also upload ch1_t1 files since they weren't uploaded in first run
import os
DUMP_DIR = "data/intermediate/translations_dump"
for lang in ["hi", "te", "od"]:
    fname = f"ch1_t1_{lang}.html"
    filepath = os.path.join(DUMP_DIR, fname)
    with open(filepath, "r", encoding="utf-8") as f:
        html = f.read()
    if "related-link" in html:
        topic = db.topics.find_one({"grade": 9, "chapter": 1, "order": 1})
        # Check if MongoDB content differs
        db_content = topic.get("translations", {}).get(lang, {}).get("content", "")
        if "related-link" not in db_content:
            db.topics.update_one(
                {"_id": topic["_id"]},
                {"$set": {f"translations.{lang}.content": html}}
            )
            print(f"  Uploaded {fname} to MongoDB")

client.close()
