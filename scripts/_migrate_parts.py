"""
Migrate local files to part folders and update MongoDB with part info.

Grades with parts (maths):
  - Grade 7: part1 (ch1-8), part2 (ch1-7)
  - Grade 8: part1 (ch1-7), part2 (ch1-7)  
  - Grade 12: part1 (ch1-6), part2 (ch1-7 → mapped to ch7-13)

Currently generated: only ch1-3 for each grade (all from part1).
"""
import json
import os
import shutil
import sys
from pathlib import Path

try:
    from pymongo import MongoClient
except ImportError:
    print("pymongo not installed")
    sys.exit(1)

ROOT = Path(__file__).parent.parent

# Grades with part structure for maths
PART_GRADES = {7, 8, 12}

# Chapter ranges for part1 (all current chapters fall in part1)
PART1_CHAPTERS = {
    7: range(1, 9),    # ch1-8
    8: range(1, 8),    # ch1-7
    12: range(1, 7),   # ch1-6
}


def get_mongo_uri():
    env_file = ROOT / 'webapp' / '.env.local'
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.startswith('MONGODB_URI='):
                return line.split('=', 1)[1].strip()
    raise RuntimeError("No MONGODB_URI found")


def move_files():
    """Move output and generated files into part folders for grades with parts."""
    for grade in PART_GRADES:
        for folder in ['output', 'generated']:
            base = ROOT / 'data' / folder / f'grade{grade}' / 'maths'
            if not base.exists():
                continue

            # Find chapter folders directly under maths/ (not already in a part folder)
            for item in sorted(base.iterdir()):
                if item.is_dir() and item.name.startswith('chapter'):
                    ch_num = int(item.name.replace('chapter', ''))
                    # Determine which part
                    if ch_num in PART1_CHAPTERS.get(grade, []):
                        part = 'part1'
                    else:
                        part = 'part2'

                    dest = base / part / item.name
                    if dest.exists():
                        print(f"  SKIP {folder}/grade{grade}/maths/{item.name} → already at {part}/")
                        continue

                    dest.parent.mkdir(parents=True, exist_ok=True)
                    print(f"  MOVE {folder}/grade{grade}/maths/{item.name} → {part}/{item.name}")
                    shutil.move(str(item), str(dest))


def update_db():
    """Update MongoDB chapters and topics with part info."""
    uri = get_mongo_uri()
    client = MongoClient(uri)
    db = client['btp-1']

    print(f"\nConnected to MongoDB")

    # Drop old unique index and recreate with part
    try:
        db.chapters.drop_index('grade_1_subject_1_chapter_1')
        print("  Dropped old chapter index")
    except Exception:
        pass

    # Update chapters for part grades
    for grade in PART_GRADES:
        chapters = list(db.chapters.find({'grade': grade, 'subject': 'maths'}))
        for ch in chapters:
            ch_num = ch['chapter']
            if ch_num in PART1_CHAPTERS.get(grade, []):
                part = 1
            else:
                part = 2

            db.chapters.update_one(
                {'_id': ch['_id']},
                {'$set': {'part': part}}
            )
            print(f"  Chapter grade{grade}/ch{ch_num} → part={part}")

    # Update topics for part grades
    for grade in PART_GRADES:
        topics = list(db.topics.find({'grade': grade, 'subject': 'maths'}))
        for t in topics:
            ch_num = t['chapter']
            if ch_num in PART1_CHAPTERS.get(grade, []):
                part = 1
            else:
                part = 2

            db.topics.update_one(
                {'_id': t['_id']},
                {'$set': {'part': part}}
            )
        print(f"  Updated {len(topics)} topics for grade {grade}")

    # Set part=null explicitly for non-part grades
    for grade in [6, 9, 10, 11]:
        db.chapters.update_many(
            {'grade': grade, 'part': {'$exists': False}},
            {'$set': {'part': None}}
        )
        db.topics.update_many(
            {'grade': grade, 'part': {'$exists': False}},
            {'$set': {'part': None}}
        )

    # Recreate indexes
    db.chapters.create_index(
        [('grade', 1), ('subject', 1), ('chapter', 1), ('part', 1)],
        unique=True
    )
    db.topics.create_index(
        [('grade', 1), ('subject', 1), ('chapter', 1), ('part', 1), ('order', 1)]
    )
    print("  Indexes recreated")

    client.close()


def main():
    print("=== Step 1: Move local files to part folders ===")
    move_files()

    print("\n=== Step 2: Update MongoDB with part info ===")
    update_db()

    print("\n=== Done ===")


if __name__ == '__main__':
    main()
