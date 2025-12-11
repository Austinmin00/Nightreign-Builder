import csv

def swap_effect_notes_columns(input_file, output_file):
    """Swap the Effect and Notes columns in the CSV"""
    
    with open(input_file, 'r', encoding='utf-8') as infile:
        reader = csv.DictReader(infile)
        fieldnames = reader.fieldnames
        
        rows = []
        for row in reader:
            # Swap Effect and Notes columns
            effect_value = row['Effect']
            notes_value = row['Notes']
            
            row['Effect'] = notes_value
            row['Notes'] = effect_value
            
            rows.append(row)
    
    # Write corrected rows to file
    with open(output_file, 'w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
    
    print(f"Fixed CSV written to {output_file}")
    print(f"Total rows processed: {len(rows)}")

if __name__ == "__main__":
    input_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Relic Effects.csv"
    output_file = "postgres-docker/data/Nightreign Useful Info (Version 1.03.1) (+ DLC) - Relic Effects - Fixed.csv"
    swap_effect_notes_columns(input_file, output_file)
