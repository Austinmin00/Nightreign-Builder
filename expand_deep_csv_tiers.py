import csv
import re

def expand_tiers(input_file, output_file):
    """Expand rows with tier notation into separate rows"""
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        expanded_rows = []
        
        for row in reader:
            description = row['Relic Description']
            effect = row['Effect']
            notes = row.get('Notes', '')
            
            # Check for various tier patterns: +3/4, +0/1/2, +1/2, +1/2/3
            tier_patterns = [
                (r'\+(\d+)/(\d+)/(\d+)', 3),  # +1/2/3
                (r'\+(\d+)/(\d+)', 2),          # +3/4 or +1/2
            ]
            
            matched = False
            for pattern, num_tiers in tier_patterns:
                desc_match = re.search(pattern, description)
                if desc_match:
                    matched = True
                    tiers = desc_match.groups()
                    
                    # Create separate rows for each tier
                    for i, tier in enumerate(tiers):
                        new_row = row.copy()
                        
                        # Update description with single tier
                        new_desc = re.sub(pattern, f'+{tier}', description)
                        new_row['Relic Description'] = new_desc
                        
                        # Update effect with corresponding value
                        new_effect = effect
                        # Match patterns like: 1.105x / 1.12x or 1.05x/1.08x/1.1x
                        if num_tiers == 2:
                            effect_pattern = r'(\+?)(\d+(?:\.\d+)?)(x?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)'
                            def replace_effect_2(match):
                                prefix1, val1, suffix1, prefix2, val2, suffix2 = match.groups()
                                values = [(prefix1, val1, suffix1), (prefix2, val2, suffix2)]
                                return values[i][0] + values[i][1] + values[i][2]
                            new_effect = re.sub(effect_pattern, replace_effect_2, new_effect)
                        else:  # 3 tiers
                            effect_pattern = r'(\+?)(\d+(?:\.\d+)?)(x?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)'
                            def replace_effect_3(match):
                                groups = match.groups()
                                values = [(groups[0], groups[1], groups[2]), 
                                         (groups[3], groups[4], groups[5]),
                                         (groups[6], groups[7], groups[8])]
                                return values[i][0] + values[i][1] + values[i][2]
                            new_effect = re.sub(effect_pattern, replace_effect_3, new_effect)
                        
                        new_row['Effect'] = new_effect
                        
                        # Update notes with corresponding value
                        new_notes = notes
                        if num_tiers == 2:
                            notes_pattern = r'(\+?)(\d+(?:\.\d+)?)(x?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)'
                            def replace_notes_2(match):
                                prefix1, val1, suffix1, prefix2, val2, suffix2 = match.groups()
                                values = [(prefix1, val1, suffix1), (prefix2, val2, suffix2)]
                                return values[i][0] + values[i][1] + values[i][2]
                            new_notes = re.sub(notes_pattern, replace_notes_2, new_notes)
                        else:  # 3 tiers
                            notes_pattern = r'(\+?)(\d+(?:\.\d+)?)(x?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)'
                            def replace_notes_3(match):
                                groups = match.groups()
                                values = [(groups[0], groups[1], groups[2]), 
                                         (groups[3], groups[4], groups[5]),
                                         (groups[6], groups[7], groups[8])]
                                return values[i][0] + values[i][1] + values[i][2]
                            new_notes = re.sub(notes_pattern, replace_notes_3, new_notes)
                        
                        new_row['Notes'] = new_notes
                        expanded_rows.append(new_row)
                    break
            
            if not matched:
                # No tiers, keep as-is
                expanded_rows.append(row)
    
    # Write expanded rows to new file
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(expanded_rows)
    
    print(f"Expanded CSV written to {output_file}")
    print(f"Total rows after expansion: {len(expanded_rows)}")

if __name__ == "__main__":
    input_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Deep Relic Effects.csv"
    output_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Deep Relic Effects - Expanded.csv"
    expand_tiers(input_file, output_file)
