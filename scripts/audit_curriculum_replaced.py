import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

terms_to_check = [
    'طَفِ', 'tafi',
    'صُرِ', 'suri_emph',
    'ضُرِ', 'duri_emph',
    'قُرِ', 'quri',
    'قِفَ', 'qifa',
    'غِلَ', 'ghila',
]

print("=== AUDIT DES ANCIENNES COMBINAISONS DANS CURRICULUM.TS ===\n")
for term in terms_to_check:
    matches = [m.start() for m in re.finditer(re.escape(term), text)]
    print(f'Terme "{term}": {len(matches)} occurrence(s)')
    for pos in matches:
        start = max(0, pos - 100)
        end = min(len(text), pos + 100)
        snippet = text[start:end].replace('\n', ' ')
        print(f'   -> ...{snippet}...\n')
