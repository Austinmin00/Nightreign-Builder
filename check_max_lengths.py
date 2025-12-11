import csv

files = [
    'postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Relic Effects - Expanded.csv',
    'postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Deep Relic Effects - Expanded.csv'
]

for filepath in files:
    print(f"\n{filepath.split('/')[-1]}:")
    with open(filepath, 'r', encoding='utf-8') as f:
        rows = list(csv.DictReader(f))
    
    max_type = max(len(r['Category']) for r in rows)
    max_desc = max(len(r['Relic Description']) for r in rows)
    max_effect = max(len(r['Effect']) for r in rows)
    max_stackable = max(len(r['Stackable with self?']) if r['Stackable with self?'] else 0 for r in rows)
    max_notes = max(len(r['Notes']) if r['Notes'] else 0 for r in rows)
    
    print(f"  Max Category: {max_type}")
    print(f"  Max Description: {max_desc}")
    print(f"  Max Effect: {max_effect}")
    print(f"  Max Stackable: {max_stackable}")
    print(f"  Max Notes: {max_notes}")
