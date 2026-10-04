import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'export const WORLDS: World\[\] = (\[.*\]);', text, re.DOTALL)
worlds = json.loads(m.group(1))

for w in worlds:
    print(f"\n=== WORLD {w['id']} ({len(w['levels'])} levels): {w['name']} ===")
    for l in w['levels']:
        print(f"  ID {l['id']}: '{l['title']}'")
