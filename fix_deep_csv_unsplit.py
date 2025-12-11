import csv
import re

def fix_unsplit_tiers(input_file, output_file):
    """Fix rows that still have combined tier values and expand +0/+1 patterns"""
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        fixed_rows = []
        
        for row in reader:
            description = row['Relic Description']
            effect = row['Effect']
            notes = row['Notes']
            
            # Handle +0/+1 pattern that wasn't split at all
            if re.search(r'\+0/\+1', description):
                # Create two rows for +0 and +1
                # Find the tier pattern and split
                
                # Row for +0
                row_0 = row.copy()
                row_0['Relic Description'] = description.replace('+0/+1', '+0')
                # Split effect values if they contain slashes
                if '/' in effect:
                    # Extract first value (e.g., "1.12x" from "1.12x/1.22x")
                    match = re.search(r'([\d.]+x)/([\d.]+x)', effect)
                    if match:
                        row_0['Effect'] = effect.replace(match.group(0), match.group(1))
                fixed_rows.append(row_0)
                
                # Row for +1
                row_1 = row.copy()
                row_1['Relic Description'] = description.replace('+0/+1', '+1')
                if '/' in effect:
                    match = re.search(r'([\d.]+x)/([\d.]+x)', effect)
                    if match:
                        row_1['Effect'] = effect.replace(match.group(0), match.group(2))
                fixed_rows.append(row_1)
                continue
            
            # For already-split rows, fix any remaining combined values
            # Extract tier number
            tier_match = re.search(r'\+(\d+)(?:\s|$)', description)
            if tier_match:
                tier_num = int(tier_match.group(1))
                
                # Fix effect if it has combined values
                # Pattern: "10.5%/12%" or "1.12x/1.22x" or "25%/35%"
                slash_pattern = re.search(r'([\d.]+)(%?)\s*/\s*([\d.]+)(%?)', effect)
                if slash_pattern:
                    val1 = slash_pattern.group(1) + slash_pattern.group(2)
                    val2 = slash_pattern.group(3) + slash_pattern.group(4)
                    
                    # For +1/+2 splits: +1 gets first value, +2 gets second
                    if tier_num == 1:
                        effect = effect.replace(slash_pattern.group(0), val1)
                    elif tier_num == 2:
                        effect = effect.replace(slash_pattern.group(0), val2)
                    
                    row['Effect'] = effect
                
                # Fix notes if it has combined values
                slash_pattern = re.search(r'([\d.]+)(%?)\s*/\s*([\d.]+)(%?)', notes)
                if slash_pattern:
                    val1 = slash_pattern.group(1) + slash_pattern.group(2)
                    val2 = slash_pattern.group(3) + slash_pattern.group(4)
                    
                    if tier_num == 1:
                        notes = notes.replace(slash_pattern.group(0), val1)
                    elif tier_num == 2:
                        notes = notes.replace(slash_pattern.group(0), val2)
                    
                    row['Notes'] = notes
            
            fixed_rows.append(row)
    
    # Write fixed rows
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(fixed_rows)
    
    print(f"Fixed CSV written to {output_file}")
    print(f"Total rows: {len(fixed_rows)}")

if __name__ == "__main__":
    input_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Deep Relic Effects - Expanded.csv"
    output_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Deep Relic Effects - Expanded-Fixed.csv"
    fix_unsplit_tiers(input_file, output_file)
