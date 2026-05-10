import json
import glob
import sys

def check_edges():
    files = sorted(glob.glob('/ssd_scratch/btp-1/data/knowledge_graph/.checkpoints/maths_edges_grade*.json'))
    for f in files:
        print(f"=== {f} ===")
        try:
            d = json.load(open(f))
            print(f'  Records: {len(d)}')
            total_prereqs = sum(len(e.get("prerequisites",[])) for e in d)
            print(f'  Total prereq links: {total_prereqs}')
            sample = [e for e in d if e.get("prerequisites")]
            if sample:
                print(f'  Sample with prereqs: {json.dumps(sample[0], indent=2)[:300]}')
            else:
                print('  ALL EMPTY PREREQUISITES')
        except Exception as e:
            print(f"  Error: {e}")

def check_concepts():
    ckpts = sorted(glob.glob('/ssd_scratch/btp-1/data/knowledge_graph/.checkpoints/maths_concepts_batch*.json'))
    all_concepts = []
    for f in ckpts:
        try:
            all_concepts.extend(json.load(open(f)))
        except:
            pass
    print(f'\nTotal concepts: {len(all_concepts)}')
    print('Sample slugs:')
    for c in all_concepts[:20]:
        print(f'  slug={repr(c.get("slug"))}  name={repr(c.get("canonical_name"))}  grades={c.get("grades")}')

print("--- EDGE CHECKPOINTS ---")
check_edges()
print("\n--- CONCEPTS ---")
check_concepts()
