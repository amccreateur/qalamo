import json
import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find all levels in World 4 (26 to 32)
levels = [26, 27, 28, 29, 30, 31, 32]

for lvl in levels:
    print(f"\n==================== LEÇON {lvl} ====================")
    # find level chunk
    m = re.search(rf'"id":\s*{lvl},[\s\S]*?"id":\s*{lvl+1},' if lvl < 32 else rf'"id":\s*32,[\s\S]*?\]\s*;\s*export', text)
    if m:
        chunk = m.group(0)
        # title
        t = re.search(r'"title":\s*"([^"]+)"', chunk)
        tar = re.search(r'"titleAr":\s*"([^"]+)"', chunk)
        if t: print(f"Titre: {t.group(1)} | {tar.group(1) if tar else ''}")
        
        # items
        items = re.findall(r'\{\s*"id":\s*"([^"]+)",\s*"grapheme":\s*"([^"]+)"', chunk)
        if items:
            print("Items (Target / Bubble) :", " , ".join([f"{gid} ({grapheme})" for gid, grapheme in items]))
        
        # wordItems
        word_items = re.findall(r'\{\s*"id":\s*"([^"]+)",\s*"word":\s*"([^"]+)"', chunk)
        if word_items:
            print("WordItems (Atelier / Builder) :", " , ".join([f"{wid} ({word})" for wid, word in word_items]))
