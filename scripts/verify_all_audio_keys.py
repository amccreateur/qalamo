import re
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

with open('src/services/audioMap.ts', 'r', encoding='utf-8') as f:
    audio_map_content = f.read()

# Extract keys from ALL_AUDIO_ASSETS
audio_keys = set(re.findall(r'^\s*([a-zA-Z0-9_]+)\s*:\s*require\(', audio_map_content, re.MULTILINE))

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    curriculum_content = f.read()

# Find all items and wordItems ids in curriculum
item_ids = re.findall(r'\{\s*"id":\s*"([^"]+)"', curriculum_content)

print(f"Total Audio Keys in audioMap: {len(audio_keys)}")
print(f"Total Curriculum Item IDs: {len(item_ids)}")

missing_in_audio = []
for iid in set(item_ids):
    if iid not in audio_keys:
        missing_in_audio.append(iid)

print(f"\nMissing Audio IDs in audioMap ({len(missing_in_audio)}):")
for m in missing_in_audio:
    print(f" - {m}")
