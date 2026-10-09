import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    content = f.read()

# Let's find level 54 to 60
print("--- Searching for alkitaab_mufeed ---")
for m in re.finditer(r'\{\s*"id":\s*(\d+).*?"alkitaab_mufeed"', content, re.DOTALL):
    print("Found level ID match around alkitaab_mufeed")

# Let's extract the exact JSON for levels 50 to 60
lines = content.split('\n')
capturing = False
cur_level_id = None
level_lines = []

for idx, line in enumerate(lines):
    if '"id": 5' in line or '"id": 6' in line:
        if '"worldId"' in lines[min(len(lines)-1, idx+1)]:
            capturing = True
            print(f"\n==================== LINE {idx} ====================")
    if capturing:
        level_lines.append(line)
        if 'titleEn' in line or 'descriptionEn' in line:
            print('\n'.join(level_lines[:25]))
            level_lines = []
            capturing = False
