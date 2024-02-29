import json
import sys
from tabulate import tabulate

# Load data from characters.json
with open('data/json/characters.json', 'r') as file:
    characters_data = json.load(file)

# Function to search for a character by name
def search_character(name):
    for character in characters_data:
        if character['name'].lower() == name.lower():
            return character
    return None

# Function to convert character data into a table
def character_to_table(character):
    table_data = []
    table_data.append(['Name', character['name']])
    table_data.append(['ID', character['id']])
    table_data.append(['Color', character['color']])
    table_data.append(['Rarity', character['rarity']])
    table_data.append(['Tags', ', '.join(character['tags'])])
    table_data.append(['Main Ability', character['main_ability']['name']])
    table_data.append(['Main Ability Effect', character['main_ability']['effect']])
    table_data.append(['Unique Ability', character['unique_ability']['start_abilities'][0]['ability_name']])
    table_data.append(['Unique Ability Effect', character['unique_ability']['start_abilities'][0]['ability_effect']])
    table_data.append(['Ultra Ability', character['ultra_ability']['name']])
    table_data.append(['Ultra Ability Effect', character['ultra_ability']['effect']])
    table_data.append(['Base Stats', ''])
    table_data.append(['Power', character['base_stats']['power']])
    table_data.append(['Health', character['base_stats']['health']])
    table_data.append(['Strike ATK', character['base_stats']['strike_atk']])
    table_data.append(['Strike DEF', character['base_stats']['strike_def']])
    table_data.append(['Blast ATK', character['base_stats']['blast_atk']])
    table_data.append(['Blast DEF', character['base_stats']['blast_def']])
    table_data.append(['Strike', character['strike']])
    table_data.append(['Shot', character['shot']])
    table_data.append(['Special Move', character['special_move']['name']])
    table_data.append(['Special Move Effect', character['special_move']['effect']])
    table_data.append(['Special Skill', character['special_skill']['name']])
    table_data.append(['Special Skill Effect', character['special_skill']['effect']])
    table_data.append(['Ultimate Skill', character['ultimate_skill']['name']])
    table_data.append(['Ultimate Skill Effect', character['ultimate_skill']['effect']])
    table_data.append(['Z Ability', ''])
    table_data.append(['One', character['z_ability']['one']['effect']])
    table_data.append(['Two', character['z_ability']['two']['effect']])
    table_data.append(['Three', character['z_ability']['three']['effect']])
    table_data.append(['Four', character['z_ability']['four']['effect']])
    table_data.append(['Is LF', character['is_lf']])
    table_data.append(['Is Tag', character['is_tag']])
    table_data.append(['Has Zenkai', character['has_zenkai']])
    return table_data

# Check if character name is provided as argument
if len(sys.argv) < 2:
    print("Usage: python api.py [Character Name]")
    sys.exit(1)

# Get character name from command line argument
character_name = " ".join(sys.argv[1:])

# Search for character
character = search_character(character_name)
if character:
    table_data = character_to_table(character)
    print(tabulate(table_data, headers=['Attribute', 'Value'], tablefmt='ascii'))
else:
    print(f"Character '{character_name}' not found.")

