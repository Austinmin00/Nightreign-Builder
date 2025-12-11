import csv
import re

input_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Relic Effects - Expanded.csv"
output_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Relic Effects - Fixed-Swapped.csv"

with open(input_file, 'r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    fieldnames = reader.fieldnames
    
    fixed_rows = []
    
    for row in reader:
        # Only swap Effect and Notes if Notes is NOT "Self-explanatory"
        effect_value = row['Effect']
        notes_value = row['Notes']
        
        if notes_value and 'self-explanatory' not in notes_value.lower():
            # Swap the columns
            row['Effect'] = notes_value
            row['Notes'] = effect_value
        # else: keep them as-is (Effect and Notes stay in their original positions)
        
        # Now check if the new Effect column has tier values that need splitting
        description = row['Relic Description']
        effect = row['Effect']
        
        # Extract tier number from description
        tier_match = re.search(r'\+(\d+)(?:\s|$)', description)
        if tier_match and '/' in effect:
            tier_num = int(tier_match.group(1))
            
            # Check for patterns like "0.95x/0.9x/0.85x" or "30/40/50/60" or "33/44/55/66"
            # Pattern for 3 values (for +1/2/3 tiers)
            pattern_3 = re.search(r'(\+?)(\d+(?:\.\d+)?)(x?)(?:%?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)(?:%?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)(%?)', effect)
            # Pattern for 4 values (for some special cases)
            pattern_4 = re.search(r'(\+?)(\d+(?:\.\d+)?)(x?)(?:%?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)(?:%?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)(?:%?)\s*/\s*(\+?)(\d+(?:\.\d+)?)(x?)(%?)', effect)
            
            if pattern_4:
                # 4 values: tier 1 gets first, tier 2 gets second, tier 3 gets third (ignore 4th for now)
                values = [
                    pattern_4.group(1) + pattern_4.group(2) + pattern_4.group(3),
                    pattern_4.group(4) + pattern_4.group(5) + pattern_4.group(6),
                    pattern_4.group(7) + pattern_4.group(8) + pattern_4.group(9)
                ]
                suffix = pattern_4.group(13)  # % if present
                
                if tier_num >= 1 and tier_num <= 3:
                    new_val = values[tier_num - 1]
                    if suffix:
                        new_val = new_val + suffix
                    effect = effect.replace(pattern_4.group(0), new_val)
                    row['Effect'] = effect
                    
            elif pattern_3:
                # 3 values: tier 1 gets first, tier 2 gets second, tier 3 gets third
                values = [
                    pattern_3.group(1) + pattern_3.group(2) + pattern_3.group(3),
                    pattern_3.group(4) + pattern_3.group(5) + pattern_3.group(6),
                    pattern_3.group(7) + pattern_3.group(8) + pattern_3.group(9)
                ]
                suffix = pattern_3.group(10)  # % if present
                
                if tier_num >= 1 and tier_num <= 3:
                    new_val = values[tier_num - 1]
                    if suffix:
                        new_val = new_val + suffix
                    effect = effect.replace(pattern_3.group(0), new_val)
                    row['Effect'] = effect
        
        fixed_rows.append(row)

with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
    writer = csv.DictWriter(outfile, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(fixed_rows)

print(f"Fixed and swapped CSV written to {output_file}")
print(f"Total rows: {len(fixed_rows)}")
