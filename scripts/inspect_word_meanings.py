import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const WORLDS: World[] = '
start = text.find(prefix) + len(prefix)
end = text.rfind(';')
worlds = json.loads(text[start:end].strip())

phonetic_patterns = []

for w in worlds:
    for lvl in w.get('levels', []):
        for wd in lvl.get('wordItems', []):
            meaning = wd.get('meaning', '')
            transFr = wd.get('translationFr', '')
            phonDesc = wd.get('phonemeDesc', '')
            print(f"World {w['id']} | Lvl {lvl['id']:2} | {wd['id']:20} | word: {wd.get('word', ''):10} | meaning: '{meaning}' | transFr: '{transFr}' | phonDesc: '{phonDesc}'")
