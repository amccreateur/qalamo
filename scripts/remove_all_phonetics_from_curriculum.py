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

print(f"Processing {len(worlds)} worlds...")

# Clean descriptions containing phonetic lists
desc_replacements = {
    "Écoute le son phonétique et attrape la bonne lettre.": "Écoute le son et attrape la bonne lettre.",
    "Écoute bien les sons Dha, Ra, Za et Sa.": "Écoute attentivement chaque son et attrape la bonne lettre.",
    "Écoute les sons fins et appuyés (Ṣad, Ḍad, Ṭa, Ẓa).": "Écoute la nuance entre les sons fins et les sons emphatiques.",
    "Les sons profonds de la gorge (ʿAyn, Ghayn, Fa, Qaf).": "Écoute les sons profonds de la gorge et attrape la bonne lettre.",
    "Les sons doux et fluides (Kaf, Lam, Meem, Noon).": "Écoute attentivement et attrape la bonne lettre.",
    "Dernières lettres fondamentales (Haa, Waw, Yaa).": "Écoute attentivement et attrape la bonne lettre.",
    "Le son \"A\" ouvert et dynamique en 1 temps vif.": "La voyelle courte Fatḥah (ـَ) en 1 temps vif.",
    "Le son \"OU\" arrondi et court en 1 temps vif.": "La voyelle courte Ḍammah (ـُ) en 1 temps vif.",
    "Le son \"I\" tiré et souriant en 1 temps vif.": "La voyelle courte Kasrah (ـِ) en 1 temps vif.",
    "Distingue instantanément le son \"A\" vs le son \"OU\".": "Distingue instantanément la Fatḥah de la Ḍammah.",
    "Distingue instantanément le son \"A\" vs le son \"I\".": "Distingue instantanément la Fatḥah de la Kasrah.",
    "Distingue instantanément le son \"OU\" vs le son \"I\".": "Distingue instantanément la Ḍammah de la Kasrah.",
    "Distingue les 3 voyelles fondamentales à vitesse grand V !": "Distingue instantanément les 3 voyelles fondamentales !",
    "Écoute la terminaison nasalisée en \"-an\".": "Écoute la terminaison avec Tanwīn Fatḥ (ـً).",
    "Écoute la terminaison nasalisée en \"-oun\".": "Écoute la terminaison avec Tanwīn Ḍamm (ـٌ).",
    "Distingue instantanément -an, -oun et -in !": "Distingue instantanément les 3 formes de Tanwīn !",
}

for w in worlds:
    w_id = w.get('id')
    
    for lvl in w.get('levels', []):
        lvl_id = lvl.get('id')
        
        # Clean level description
        cur_desc = lvl.get('description', '')
        if cur_desc in desc_replacements:
            lvl['description'] = desc_replacements[cur_desc]
        else:
            # General cleanup of "(Da, Ra...)" in descriptions
            clean_desc = re.sub(r'\s*\([A-Za-z0-9\s,\'\-—_]+\)', '', cur_desc)
            clean_desc = clean_desc.replace('phonétique', 'sonore')
            lvl['description'] = clean_desc

        # Clean Items
        for it in lvl.get('items', []):
            # Always empty transliteration in exercises
            it['transliteration'] = ''
            
            pdesc = it.get('phonemeDesc', '')
            if not pdesc:
                pdesc = ''
                
            # World 2 : Letter positions (Début, Milieu, Fin)
            if w_id == 2:
                lower = pdesc.lower()
                if 'début' in lower:
                    it['phonemeDesc'] = 'Début de mot'
                elif 'milieu' in lower:
                    it['phonemeDesc'] = 'Milieu de mot'
                elif 'fin' in lower:
                    it['phonemeDesc'] = 'Fin de mot'
                elif 'isol' in lower:
                    it['phonemeDesc'] = 'Forme isolée'
                else:
                    it['phonemeDesc'] = ''
            # World 7 & 8 : Vocabulary / Phrase meanings
            elif w_id in [7, 8]:
                # If phonemeDesc is just a transliteration of the Arabic word (e.g. "Kataba", "Darasa", "Asad")
                # replace it with empty or translation
                if pdesc in ['Kataba', 'Darasa', 'Asad', 'Kitab', 'Qalam', 'Kursiy']:
                    it['phonemeDesc'] = ''
                # otherwise keep real French translation
            else:
                # Worlds 1, 3, 4, 5, 6 : Remove all phonemeDesc (e.g. "Ba (Fatḥah)", "Seen", "Ab", "Rabba")
                it['phonemeDesc'] = ''

        # Clean WordItems
        for wd in lvl.get('wordItems', []):
            meaning = wd.get('meaning', '')
            transFr = wd.get('translationFr', '')
            
            # If meaning/transFr is just phonetic romanization (e.g. "Ba-Ta", "Ṣa-Da", "Ka-Tou")
            if re.match(r'^[A-Za-z\s\-\'\(\)]+$', meaning) and any(syll in meaning.lower() for syll in ['-ta', '-da', '-ou', '-bi', '-ri', '-ka', '-ma', '-ni', '-li', '-wa', '-ya']):
                wd['meaning'] = ''
                wd['translationFr'] = ''
            if 'phonemeDesc' in wd:
                wd['phonemeDesc'] = ''

# Serialize back to curriculum.ts format
new_json = json.dumps(worlds, ensure_ascii=False, indent=2)
new_curriculum_text = f"import {{ World }} from '../types/game';\n\nexport const WORLDS: World[] = {new_json};\n"

with open('src/data/curriculum.ts', 'w', encoding='utf-8') as f:
    f.write(new_curriculum_text)

print("src/data/curriculum.ts successfully cleaned of all phonetic romanizations in exercises!")
