import csv
import re

def expand_tiers(input_file, output_file):
    """Expand rows with +1/2/3 tiers into separate rows"""
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        expanded_rows = []
        
        for row in reader:
            description = row['Relic Description']
            effect = row['Effect']
            notes = row.get('Notes', '')
            
            # Check if this row has tier notation (+1/2/3 or +0/1/2)
            tier_pattern = r'\+(\d+)/(\d+)/(\d+)'
            desc_match = re.search(tier_pattern, description)
            
            if desc_match:
                # Extract tier numbers from description
                tier1, tier2, tier3 = desc_match.groups()
                tiers = [tier1, tier2, tier3]
                
                # Find all tier values in effect and notes
                effect_values = re.findall(r'(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)', effect)
                notes_values = re.findall(r'(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)\s*/\s*(\d+(?:\.\d+)?)', notes)
                
                # Create three separate rows
                for i, tier in enumerate(tiers):
                    new_row = row.copy()
                    
                    # Update description with single tier
                    new_desc = re.sub(tier_pattern, f'+{tier}', description)
                    new_row['Relic Description'] = new_desc
                    
                    # Update effect with corresponding value
                    new_effect = effect
                    # Replace all patterns with / separators (with and without spaces), handle + prefix
                    effect_pattern = r'(\+?)(\d+(?:\.\d+)?)\s*/\s*(\+?)(\d+(?:\.\d+)?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)'
                    def replace_effect(match):
                        prefix1, val1, prefix2, val2, prefix3, val3, suffix = match.groups()
                        values = [(prefix1, val1), (prefix2, val2), (prefix3, val3)]
                        return values[i][0] + values[i][1] + suffix
                    new_effect = re.sub(effect_pattern, replace_effect, new_effect)
                    new_row['Effect'] = new_effect
                    
                    # Update notes with corresponding value  
                    new_notes = notes
                    notes_pattern = r'(\+?)(\d+(?:\.\d+)?)\s*/\s*(\+?)(\d+(?:\.\d+)?)\s*/\s*(\+?)(\d+(?:\.\d+)?)'
                    def replace_notes(match):
                        prefix1, val1, prefix2, val2, prefix3, val3 = match.groups()
                        values = [(prefix1, val1), (prefix2, val2), (prefix3, val3)]
                        return values[i][0] + values[i][1]
                    new_notes = re.sub(notes_pattern, replace_notes, new_notes)
                    new_row['Notes'] = new_notes
                    
                    expanded_rows.append(new_row)
            else:
                # No tiers, keep as-is
                expanded_rows.append(row)
    
    # Write expanded rows to new file
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expanded_rows)
    
    print(f"Expanded CSV written to {output_file}")
    print(f"Original rows: {len(expanded_rows) - sum(1 for r in expanded_rows if '+1/2/3' in str(r) or '+0/1/2' in str(r))}")
    print(f"Total rows after expansion: {len(expanded_rows)}")

if __name__ == "__main__":
    input_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Relic Effects - Fixed.csv"
    output_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Relic Effects - Expanded.csv"
    expand_tiers(input_file, output_file)
