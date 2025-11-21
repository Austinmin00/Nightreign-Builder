-- Create tables for Nightreign data
-- Run this script in pgAdmin Query Tool

-- 1. Character Stats Table
CREATE TABLE IF NOT EXISTS character_stats (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    base_hp INTEGER,
    base_fp INTEGER,
    base_stam INTEGER,
    vigor INTEGER,
    mind INTEGER,
    endurance INTEGER,
    strength INTEGER,
    dexterity INTEGER,
    intelligence INTEGER,
    faith INTEGER,
    arcane INTEGER,
    phys_neg VARCHAR(10),
    slash_neg VARCHAR(10),
    strike_neg VARCHAR(10),
    thrust_neg VARCHAR(10),
    magic_neg VARCHAR(10),
    fire_neg VARCHAR(10),
    ltng_neg VARCHAR(10),
    holy_neg VARCHAR(10),
    poison_resist INTEGER,
    rot_resist INTEGER,
    bleed_resist INTEGER,
    frost_resist INTEGER,
    sleep_resist INTEGER,
    madness_resist INTEGER,
    blight_resist INTEGER,
    poise INTEGER
);

-- 2. Relics Table
CREATE TABLE IF NOT EXISTS relics (
    id SERIAL PRIMARY KEY,
    category VARCHAR(50),
    relic_description TEXT,
    effect TEXT,
    stackable_with_self VARCHAR(10),
    notes TEXT
);

-- 3. Deep Relics Table
CREATE TABLE IF NOT EXISTS deep_relics (
    id SERIAL PRIMARY KEY,
    category VARCHAR(50),
    relic_description TEXT,
    effect TEXT,
    stackable_with_self VARCHAR(10),
    notes TEXT
);

-- 4. Dormant Power Table
CREATE TABLE IF NOT EXISTS dormant_power (
    id SERIAL PRIMARY KEY,
    category VARCHAR(50),
    dormant_power TEXT,
    effect_description_in_game TEXT,
    effect TEXT,
    stackable_with_self VARCHAR(10),
    notes TEXT
);

-- 5. Guaranteed Relics Table (complex structure - may need manual adjustment)
CREATE TABLE IF NOT EXISTS guaranteed_relics (
    id SERIAL PRIMARY KEY,
    col1 TEXT,
    col2 TEXT,
    col3 TEXT,
    col4 TEXT,
    col5 TEXT,
    col6 TEXT,
    col7 TEXT,
    col8 TEXT,
    col9 TEXT,
    col10 TEXT
);

-- 6. Level Up Cost Table
CREATE TABLE IF NOT EXISTS level_up_cost (
    id SERIAL PRIMARY KEY,
    level INTEGER NOT NULL,
    runes_to_next VARCHAR(20),
    cost_increase VARCHAR(20),
    total_runes VARCHAR(20)
);

-- Import data from CSV files
-- Note: Use /data/ path since that's where files are mounted in the container

-- Import Character Stats
COPY character_stats(name, base_hp, base_fp, base_stam, vigor, mind, endurance, strength, 
                     dexterity, intelligence, faith, arcane, phys_neg, slash_neg, strike_neg, 
                     thrust_neg, magic_neg, fire_neg, ltng_neg, holy_neg, poison_resist, 
                     rot_resist, bleed_resist, frost_resist, sleep_resist, madness_resist, 
                     blight_resist, poise)
FROM '/data/Nightreign Useful Info (Version 1.02.3) - Character Stats [Level 15].csv'
DELIMITER ','
CSV HEADER;

-- Import Relics
COPY relics(category, relic_description, effect, stackable_with_self, notes)
FROM '/data/Nightreign Useful Info (Version 1.02.3) - Effect - Relics.csv'
DELIMITER ','
CSV HEADER;

-- Import Deep Relics
COPY deep_relics(category, relic_description, effect, stackable_with_self, notes)
FROM '/data/Nightreign Useful Info (Version 1.02.3) - Effect - Deep Relics.csv'
DELIMITER ','
CSV HEADER;

-- Import Dormant Power
COPY dormant_power(category, dormant_power, effect_description_in_game, effect, stackable_with_self, notes)
FROM '/data/Nightreign Useful Info (Version 1.02.3) - Effects - Dormant Power.csv'
DELIMITER ','
CSV HEADER;

-- Import Level Up Cost
COPY level_up_cost(level, runes_to_next, cost_increase, total_runes)
FROM '/data/Nightreign Useful Info (Version 1.02.3) - Level Up Cost.csv'
DELIMITER ','
CSV HEADER;

-- Import Guaranteed Relics
COPY guaranteed_relics(col1, col2, col3, col4, col5, col6, col7, col8, col9, col10)
FROM '/data/Nightreign Useful Info (Version 1.02.3) - Guaranteed Relics.csv'
DELIMITER ','
CSV HEADER;

-- Verify imports
SELECT 'Character Stats Count:' as table_name, COUNT(*) as records FROM character_stats
UNION ALL
SELECT 'Relics Count:', COUNT(*) FROM relics
UNION ALL
SELECT 'Deep Relics Count:', COUNT(*) FROM deep_relics
UNION ALL
SELECT 'Dormant Power Count:', COUNT(*) FROM dormant_power
UNION ALL
SELECT 'Guaranteed Relics Count:', COUNT(*) FROM guaranteed_relics
UNION ALL
SELECT 'Level Up Cost Count:', COUNT(*) FROM level_up_cost;
