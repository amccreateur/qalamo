import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const WORLDS: World[] = '
start = text.find(prefix) + len(prefix)
end = text.rfind(';')
worlds = json.loads(text[start:end].strip())

print("Analyzing all worlds in curriculum.ts...")

for w in worlds:
    print(f"\n--- World {w['id']}: {w['name']} ---")
    for lvl in w.get('levels', []):
        desc = lvl.get('description', '')
        # Check if description has latin phonetics like "Dha, Ra, Za"
        has_phonetic_in_desc = any(char.isupper() and len(word) <= 4 for word in desc.split() for char in word if char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
        items = lvl.get('items', [])
        word_items = lvl.get('wordItems', [])
        
        sample_items = [(it.get('id'), it.get('grapheme'), it.get('phonemeDesc'), it.get('transliteration')) for it in items[:2]]
        sample_words = [(wd.get('id'), wd.get('word'), wd.get('meaning'), wd.get('translationFr')) for wd in word_items[:2]]
        
        print(f"  Level {lvl['id']:2} ({lvl['gameType']:11}): {lvl['title']}")
        if desc:
            print(f"    desc: {desc}")
        if sample_items:
            print(f"    items: {sample_items}")
        if sample_words:
            print(f"    wordItems: {sample_words}")
