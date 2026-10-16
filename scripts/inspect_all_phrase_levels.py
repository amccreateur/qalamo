import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = "export const WORLDS: World[] = "
idx = text.find(prefix)
if idx != -1:
    json_str = text[idx + len(prefix):].rstrip()
    if json_str.endswith(';'):
        json_str = json_str[:-1]
    worlds = json.loads(json_str)
    
    for w in worlds:
        for lvl in w['levels']:
            if lvl['id'] >= 50:
                print(f"\n--- Level {lvl['id']} [{lvl['gameType']}]: {lvl['title']} ---")
                for it in lvl.get('items', []):
                    print(f"  Target: '{it['grapheme']}' ({it.get('phonemeDesc','')})")
                    print(f"    Distractors: {it.get('distractors', [])}")

