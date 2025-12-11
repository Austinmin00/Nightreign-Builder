import csv

with open('postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Deep Relic Effects - Expanded-Fixed.csv', 'r', encoding='utf-8') as f:
    rows = [r for r in csv.DictReader(f) if '/' in r['Effect'] and any(c.isdigit() for c in r['Effect'])]
    
print(f'Rows with slashes in Effect column: {len(rows)}')
for i, row in enumerate(rows[:15]):
    print(f"Row {i+1}: {row['Relic Description'][:50]} -> {row['Effect'][:60]}")
