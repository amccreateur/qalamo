import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('scripts/world4_data.json', 'r', encoding='utf-8') as f:
    w4 = json.load(f)

print("=" * 60)
print(f"MONDE 4 : {w4['name']}")
print("=" * 60)

total_items = 0
total_word_items = 0
missing_audio = []

for lvl in w4['levels']:
    print(f"\n--- Niveau {lvl['id']}: {lvl['title']} (Jeu: {lvl['gameType']}) ---")
    items = lvl.get('items', [])
    word_items = lvl.get('wordItems', [])
    total_items += len(items)
    total_word_items += len(word_items)
    
    if items:
        print(f"  [Items / Bulles] ({len(items)}) :")
        for it in items:
            audio_path = f"assets/audio/generated/{it['id']}.mp3"
            exists = os.path.exists(audio_path)
            if not exists:
                missing_audio.append((it['id'], it.get('grapheme'), it.get('audioText', '')))
            status = "✓ OK" if exists else "❌ MANQUANT"
            print(f"    - {it['id']:20} | Grapheme: {it.get('grapheme', ''):5} | AudioText: {it.get('audioText', ''):6} | {status}")

    if word_items:
        print(f"  [WordItems / Mots] ({len(word_items)}) :")
        for w in word_items:
            audio_path = f"assets/audio/generated/{w['id']}.mp3"
            exists = os.path.exists(audio_path)
            if not exists:
                missing_audio.append((w['id'], w.get('word'), w.get('audioText', '')))
            status = "✓ OK" if exists else "❌ MANQUANT"
            print(f"    - {w['id']:20} | Mot: {w.get('word', ''):8} | Segments: {str(w.get('segments', '')):20} | {status}")

print("\n" + "=" * 60)
print(f"TOTAL Items: {total_items} | TOTAL WordItems: {total_word_items}")
print(f"TOTAL Fichiers Audio Manquants: {len(missing_audio)}")
if missing_audio:
    print("Détail des manquants:", missing_audio)
print("=" * 60)
