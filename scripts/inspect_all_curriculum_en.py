import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read curriculum.ts
with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Extract WORLDS json from curriculum.ts
m = re.search(r'export const WORLDS: World\[\] = (\[.*\]);', text, re.DOTALL)
if not m:
    print("Could not match WORLDS JSON")
    sys.exit(1)

worlds = json.loads(m.group(1))

print(f"Loaded {len(worlds)} worlds.")

for w in worlds:
    print(f"\n==========================================")
    print(f"WORLD {w['id']}: FR='{w['name']}' | EN='{w.get('nameEn')}'")
    print(f"DESC FR='{w['description']}' | EN='{w.get('descriptionEn')}'")
    print(f"==========================================")
    for l in w['levels']:
        print(f"  Level {l['id']:2d}: FR='{l['title']}' --> EN='{l.get('titleEn')}'")
        if l.get('description') or l.get('descriptionEn'):
            print(f"            Desc FR='{l.get('description')}' --> EN='{l.get('descriptionEn')}'")
        if l.get('wordItems'):
            for wi in l['wordItems']:
                print(f"            Word: {wi['word']} | FR='{wi.get('translationFr') or wi.get('meaning')}' | EN='{wi.get('translationEn')}'")

