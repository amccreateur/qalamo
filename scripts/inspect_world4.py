import json
import re

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    curriculum_text = f.read()

# Find all JSON-like objects or lessons in curriculum.ts
print("Curriculum length:", len(curriculum_text))

# Let's find "worldId": 4 or worldId: 4
matches = [m.start() for m in re.finditer(r'worldId["\']?\s*:\s*4\b', curriculum_text)]
print(f"Found {len(matches)} lessons for World 4 in curriculum.ts")

for idx, m in enumerate(matches):
    print(f"\n=== Match {idx+1} at char {m} ===")
    print(curriculum_text[m-60:m+600])
