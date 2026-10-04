import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const WORLDS: World[] = '
start = text.find(prefix) + len(prefix)
end = text.rfind(';')
worlds = json.loads(text[start:end].strip())

print(f"Total worlds: {len(worlds)}")

for w in worlds:
    w_id = w.get('id')
    w_name = w.get('name')
    print(f"\n==================== WORLD {w_id}: {w_name} ====================")
    for lvl in w.get('levels', []):
        lvl_id = lvl.get('id')
        lvl_title = lvl.get('title')
        game_type = lvl.get('gameType')
        print(f"\n  -- Level {lvl_id}: {lvl_title} ({game_type}) --")
        
        items = lvl.get('items', [])
        if items:
            for it in items[:3]:
                print(f"    Item: id={it.get('id')} | graph={it.get('grapheme')} | translit={it.get('transliteration')} | phonemeDesc={it.get('phonemeDesc')}")
        
        word_items = lvl.get('wordItems', [])
        if word_items:
            for wd in word_items[:3]:
                print(f"    WordItem: id={wd.get('id')} | word={wd.get('word')} | phonemeDesc={wd.get('phonemeDesc')} | meaning={wd.get('meaning')} | translationFr={wd.get('translationFr')}")
