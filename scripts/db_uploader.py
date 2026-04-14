"""
db_uploader.py — Upload generated content JSON files to MongoDB.

Usage:
    python scripts/db_uploader.py                              # Upload all en.json files
    python scripts/db_uploader.py data/generated/grade11/maths/chapter1/en.json  # Upload specific file

The script reads the en.json files produced by md_to_json.py and upserts
Chapter + Topic documents into MongoDB.

MongoDB connection: reads from MONGODB_URI env var or webapp/.env.local
Database: btp-1
"""

import json
import os
import re
import sys
from pathlib import Path

try:
    from pymongo import MongoClient, UpdateOne
except ImportError:
    print("pymongo not installed. Run: pip install pymongo[srv]")
    sys.exit(1)

ROOT = Path(__file__).parent.parent


def extract_headings(html_content: str) -> str:
    """Extract all h2 and h3 text from HTML content as newline-separated string."""
    headings = re.findall(r'<h[23][^>]*>(.*?)</h[23]>', html_content, re.IGNORECASE)
    return '\n'.join(headings)


def get_mongo_uri():
    """Read MongoDB URI from env or webapp/.env.local."""
    uri = os.environ.get('MONGODB_URI')
    if uri:
        return uri

    env_file = ROOT / 'webapp' / '.env.local'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith('MONGODB_URI='):
                return line.split('=', 1)[1].strip()

    raise RuntimeError("No MONGODB_URI found. Set env var or create webapp/.env.local")


def upload_json(json_path: Path, db):
    """Upload a single en.json file to MongoDB."""
    with open(json_path, encoding='utf-8') as f:
        data = json.load(f)

    grade = data['grade']
    chapter_num = data['chapter']
    subject_raw = data.get('subject', 'Mathematics')
    # Normalize subject to lowercase key
    subject = subject_raw.lower()
    if subject == 'mathematics':
        subject = 'maths'

    print(f"\n  Uploading: Grade {grade} {subject} Chapter {chapter_num}")
    print(f"    Title: {data['title']}")
    print(f"    Topics: {len(data.get('topics', []))}")

    # Upsert chapter
    chapter_doc = {
        'title': data['title'],
        'subject': subject,
        'grade': grade,
        'chapter': chapter_num,
        'language': data.get('language', 'en'),
        'model': data.get('model', ''),
        'summary': data.get('summary', ''),
        'topicCount': len(data.get('topics', [])),
    }

    result = db.chapters.update_one(
        {'grade': grade, 'subject': subject, 'chapter': chapter_num},
        {'$set': chapter_doc},
        upsert=True
    )

    # Get the chapter _id
    ch = db.chapters.find_one({'grade': grade, 'subject': subject, 'chapter': chapter_num})
    chapter_id = ch['_id']

    if result.upserted_id:
        print(f"    Chapter: created (id={chapter_id})")
    else:
        print(f"    Chapter: updated (id={chapter_id})")

    # Delete existing topics for this chapter, then insert fresh
    del_result = db.topics.delete_many({
        'grade': grade, 'subject': subject, 'chapter': chapter_num
    })
    if del_result.deleted_count:
        print(f"    Deleted {del_result.deleted_count} old topics")

    topic_docs = []
    for i, topic in enumerate(data.get('topics', [])):
        topic_docs.append({
            'chapterId': chapter_id,
            'title': topic['title'],
            'topicNumber': topic['topicNumber'],
            'importance': topic.get('importance', 3),
            'content': topic['content'],
            'searchText': topic.get('searchText', ''),
            'headings': extract_headings(topic['content']),
            'grade': grade,
            'subject': subject,
            'chapter': chapter_num,
            'order': i + 1,
        })

    if topic_docs:
        db.topics.insert_many(topic_docs)
        print(f"    Inserted {len(topic_docs)} topics")

    # Now update Related Topics links with real MongoDB ObjectIds
    # The HTML has placeholder links like /grade/{g}/{s}/chapter/{c}/topic/TOPICID_{order}
    # We need to replace TOPICID_{order} with the actual MongoDB _id
    topics_in_db = list(db.topics.find(
        {'grade': grade, 'subject': subject, 'chapter': chapter_num},
        {'_id': 1, 'order': 1}
    ).sort('order', 1))

    order_to_id = {t['order']: str(t['_id']) for t in topics_in_db}

    ops = []
    for t in topics_in_db:
        topic_full = db.topics.find_one({'_id': t['_id']})
        content = topic_full['content']
        updated = False
        for order, real_id in order_to_id.items():
            placeholder = f"TOPICID_{order}"
            if placeholder in content:
                content = content.replace(placeholder, real_id)
                updated = True
        if updated:
            ops.append(UpdateOne(
                {'_id': t['_id']},
                {'$set': {'content': content}}
            ))

    if ops:
        db.topics.bulk_write(ops)
        print(f"    Updated {len(ops)} topics with real topic links")

    return len(topic_docs)


def main():
    uri = get_mongo_uri()
    client = MongoClient(uri)
    db = client['btp-1']

    print(f"Connected to MongoDB: {uri.split('@')[1].split('/')[0] if '@' in uri else 'local'}")

    # Ensure indexes
    db.chapters.create_index([('grade', 1), ('subject', 1), ('chapter', 1)], unique=True)
    db.topics.create_index([('grade', 1), ('subject', 1), ('chapter', 1), ('order', 1)])
    db.topics.create_index([('chapterId', 1)])
    print("Indexes ensured")

    if len(sys.argv) > 1:
        # Upload specific file(s)
        for arg in sys.argv[1:]:
            p = Path(arg)
            if p.is_file():
                upload_json(p, db)
            else:
                print(f"File not found: {p}")
    else:
        # Upload all en.json files from data/generated/
        generated_dir = ROOT / 'data' / 'generated'
        json_files = sorted(generated_dir.rglob('en.json'))
        if not json_files:
            print("No en.json files found in data/generated/")
            sys.exit(1)

        total_topics = 0
        for jf in json_files:
            total_topics += upload_json(jf, db)

        print(f"\n{'='*50}")
        print(f"Done! Uploaded {len(json_files)} chapters, {total_topics} topics total")

    client.close()


if __name__ == '__main__':
    main()
