import json

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

# Find `export const WORLDS: World[] = `
prefix = "export const WORLDS: World[] = "
start = text.find(prefix) + len(prefix)
end = text.rfind(';')
json_str = text[start:end].strip()

worlds = json.loads(json_str)
world4 = [w for w in worlds if w.get('id') == 4][0]

print(f"World 4: {world4.get('name')}")
print(f"Total levels in World 4: {len(world4.get('levels', []))}")

with open('scripts/world4_data.json', 'w', encoding='utf-8') as out_f:
    json.dump(world4, out_f, ensure_ascii=False, indent=2)
print("Saved scripts/world4_data.json successfully!")
