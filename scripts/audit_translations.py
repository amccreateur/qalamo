import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's search for "Grand challenge"
for m in re.finditer(r'Grand [Cc]hallenge', text):
    start = max(0, m.start() - 150)
    end = min(len(text), m.end() + 250)
    print("--- FOUND IN CURRICULUM ---")
    print(text[start:end])

# Let's inspect all levels in curriculum.ts
print("\n--- ALL LEVEL TITLES AND EN TRANSLATIONS ---")
levels = re.findall(r'id:\s*(\d+),\s*worldId:\s*(\d+),\s*title:\s*[\'"`]([^\'"`]+)[\'"`],(?:\s*titleEn:\s*[\'"`]([^\'"`]+)[\'"`],)?', text)
for l in levels:
    print(f"Level {l[0]} (World {l[1]}): FR='{l[2]}' | EN='{l[3]}'")

