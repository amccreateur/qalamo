import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

prefix = 'export const WORLDS: World[] = '
start = text.find(prefix) + len(prefix)
end = text.rfind(';')
worlds = json.loads(text[start:end].strip())

print(f"Loaded {len(worlds)} worlds.")

# Translation maps for Worlds
world_translations = {
    1: {
        "nameEn": "World 1: The Alphabet & 28 Sounds",
        "descriptionEn": "Discover the clear studio sound of each fundamental Arabic letter."
    },
    2: {
        "nameEn": "World 2: The 4 Letter Shapes",
        "descriptionEn": "Learn the 4 positions of letters: Isolated, Initial, Medial, and Final."
    },
    3: {
        "nameEn": "World 3: Short Vowels (Harakāt)",
        "descriptionEn": "Master the 3 short vowel signs: Fatḥah (A), Ḍammah (U), and Kasrah (I)."
    },
    4: {
        "nameEn": "World 4: 2-Vowel Combinations",
        "descriptionEn": "Chain two consecutive short vowels smoothly across all 28 letters and emphatic sounds."
    },
    5: {
        "nameEn": "World 5: Sukūn & Long Vowels (Madd)",
        "descriptionEn": "Contrast consonant stops (Sukūn) with sustained 2-beat long vowels (Alif, Waw, Ya)."
    },
    6: {
        "nameEn": "World 6: Shaddah, Tanwīn & Alif-Lām",
        "descriptionEn": "Double consonants (Shaddah), nunations (Tanwīn), and Solar vs Lunar letters (الـ)."
    },
    7: {
        "nameEn": "World 7: Vocabulary & Everyday Words",
        "descriptionEn": "Read and assemble everyday nouns, action verbs, and illustrated vocabulary."
    },
    8: {
        "nameEn": "World 8: Short Sentences & Fluency",
        "descriptionEn": "Read nominal and verbal sentences with prepositions and fluent reading."
    }
}

# Vocabulary translation map (French -> English)
word_translations_en = {
    "Porte": "Door",
    "Maison": "House",
    "Chaise": "Chair",
    "Bureau": "Desk",
    "Stylo": "Pen",
    "Lion": "Lion",
    "Chameau": "Camel",
    "Éléphant": "Elephant",
    "Oiseau": "Bird",
    "Chat": "Cat",
    "Chien": "Dog",
    "Soleil": "Sun",
    "Lune": "Moon",
    "Étoile": "Star",
    "Mer": "Sea",
    "Ciel": "Sky",
    "Arbre": "Tree",
    "Eau": "Water",
    "Lait": "Milk",
    "Pain": "Pain / Bread",
    "Dattes": "Dates",
    "Raisin": "Grapes",
    "Pomme": "Apple",
    "École": "School",
    "Jardin": "Garden",
    "Petit oiseau": "Little bird",
    "Grenade": "Pomegranate",
    "Livre": "Book",
    "Père": "Father",
    "Mère": "Mother",
    "Frère": "Brother",
    "Avec": "With",
    "Pour toi": "For you",
    "Il": "He",
    "Elle": "She",
    "Peut-être": "Maybe",
    "Pourquoi": "Why",
    "Par toi": "By you",
    "Écrire": "Write",
    "Étudier": "Study",
    "Lire": "Read",
    "Dessiner": "Draw",
    "S'asseoir": "Sit",
    "Partir": "Leave",
    "Écouter": "Listen",
    "Manger": "Eat",
    "Boire": "Drink",
    "Ouvrir": "Open",
    "Il a écrit": "He wrote",
    "Il a étudié": "He studied",
    "Il a lu": "He read",
    "Il a dessiné": "He drew",
    "Il s'est assis": "He sat",
    "Il est parti": "He left",
    "Il a écouté": "He listened",
    "Il a mangé": "He ate",
    "Il a bu": "He drank",
    "Il a ouvert": "He opened"
}

# Phrases translation map (for World 8)
phrases_en = {
    "La maison est grande": "The house is big",
    "L'eau est fraîche": "The water is cold",
    "Le livre est utile": "The book is useful",
    "Le garçon est énergique": "The boy is energetic",
    "La fille est intelligente": "The girl is smart",
    "Le stylo est neuf": "The pen is new",
    "L'enfant a écrit": "The child wrote",
    "L'élève a lu": "The student read",
    "Le père s'est assis": "The father sat down",
    "Le garçon est parti": "The boy left",
    "Le père est revenu": "The father returned",
    "Le maître est sorti": "The teacher went out",
    "L'enfant a lu le livre": "The child read the book",
    "L'élève a écrit la leçon": "The student wrote the lesson",
    "L'enfant a bu le lait": "The child drank the milk",
    "Le père a ouvert la porte": "The father opened the door",
    "L'enfant a dessiné l'arbre": "The child drew the tree",
    "Que la paix soit sur vous": "Peace be upon you",
    "Bienvenue": "Welcome",
    "Merci beaucoup": "Thank you very much",
    "L'enfant est allé à l'école": "The child went to school",
    "Le père s'est assis sur la chaise": "The father sat on the chair",
    "Le livre est dans le cartable": "The book is in the schoolbag",
    "Ahmad a lu un livre instructif": "Ahmad read an instructive book",
    "Fatima est allée au jardin": "Fatima went to the garden",
    "Le garçon a mangé une délicieuse pomme": "The boy ate a delicious apple",
    "Le soleil brille": "The sun is shining"
}

# Apply translations to all worlds
for w in worlds:
    w_id = w['id']
    if w_id in world_translations:
        w['nameEn'] = world_translations[w_id]['nameEn']
        w['descriptionEn'] = world_translations[w_id]['descriptionEn']
        
    for lvl in w.get('levels', []):
        lvl_title = lvl.get('title', '')
        lvl_desc = lvl.get('description', '')
        
        # Translate Level titles & descriptions into English
        title_en = lvl_title
        desc_en = lvl_desc
        
        if "Groupe 1" in lvl_title: title_en = lvl_title.replace("Groupe 1", "Group 1")
        elif "Groupe 2" in lvl_title: title_en = lvl_title.replace("Groupe 2", "Group 2")
        elif "Groupe 3" in lvl_title: title_en = lvl_title.replace("Groupe 3", "Group 3")
        elif "Groupe 4" in lvl_title: title_en = lvl_title.replace("Groupe 4", "Group 4")
        elif "Groupe 5" in lvl_title: title_en = lvl_title.replace("Groupe 5", "Group 5")
        elif "Groupe 6" in lvl_title: title_en = lvl_title.replace("Groupe 6", "Group 6")
        elif "Groupe 7" in lvl_title: title_en = lvl_title.replace("Groupe 7", "Group 7")
        elif "Groupe 8" in lvl_title: title_en = lvl_title.replace("Groupe 8", "Group 8")
        elif "Duel Final" in lvl_title: title_en = lvl_title.replace("Duel Final", "Final Duel")
        elif "Grand Défi" in lvl_title: title_en = lvl_title.replace("Grand Défi", "Grand Challenge")
        elif "Championnat" in lvl_title: title_en = lvl_title.replace("Championnat", "Championship")
        elif "Série A + A" in lvl_title: title_en = "Series A + A (Emphatic & Simple)"
        elif "Série A + OU" in lvl_title: title_en = "Series A + U (Emphatic & Simple)"
        elif "Série A + I" in lvl_title: title_en = "Series A + I (Throat & Emphatics)"
        elif "Séries OU + I" in lvl_title: title_en = "Series U + I & U + A (Emphatics & Pronouns)"
        elif "Série I + A" in lvl_title: title_en = "Series I + A & Discrimination Challenge"
        elif "Grand Atelier" in lvl_title: title_en = "Grand Workshop: All 28 Letters"
        elif "Formes en Début" in lvl_title: title_en = "Initial Forms (At the beginning)"
        elif "Formes au Milieu" in lvl_title: title_en = "Medial Forms (In the middle)"
        elif "Formes en Fin" in lvl_title: title_en = "Final Forms (At the end)"
        elif "Les 6 Lettres Sans Attache" in lvl_title: title_en = "The 6 Non-Connecting Letters"
        elif "La Fatḥah" in lvl_title: title_en = "The Fatḥah (ـَ) : Short 'A' sound"
        elif "La Ḍammah" in lvl_title: title_en = "The Ḍammah (ـُ) : Short 'U' sound"
        elif "La Kasrah" in lvl_title: title_en = "The Kasrah (ـِ) : Short 'I' sound"
        elif "Le Sukūn" in lvl_title: title_en = "The Sukūn (ـْ) : The Consonant Stop"
        elif "Madd Alif" in lvl_title: title_en = "Madd Alif (ـَا) : 2-Beat Long 'AA'"
        elif "Madd Waw" in lvl_title: title_en = "Madd Waw (ـُو) : 2-Beat Long 'UU'"
        elif "Madd Ya" in lvl_title: title_en = "Madd Ya (ـِي) : 2-Beat Long 'II'"
        elif "La Shaddah" in lvl_title: title_en = "The Shaddah (ـّ) : Doubled Consonant"
        elif "Le Tanwīn en -an" in lvl_title: title_en = "Tanwīn -an (ـً) : Open Nunation"
        elif "Le Tanwīn en -oun" in lvl_title: title_en = "Tanwīn -un (ـٌ) : Closed Nunation"
        elif "Le Tanwīn en -in" in lvl_title: title_en = "Tanwīn -in (ـٍ) & The 3 Tanwīns Duel"
        elif "Alif-Lām" in lvl_title and "Lunaires" in lvl_title: title_en = "Alif-Lām (الـ) : Moon Letters"
        elif "Alif-Lām" in lvl_title and "Solaires" in lvl_title: title_en = "Alif-Lām (الـ) : Sun Letters"
        elif "Verbes à 3 lettres" in lvl_title: title_en = "3-Letter Base Verbs"
        elif "Verbes d'action" in lvl_title: title_en = "Daily Action Verbs"
        elif "Maison & Bureau" in lvl_title: title_en = "Illustrated Words: House & Office"
        elif "Les Animaux" in lvl_title: title_en = "Animals of the World"
        elif "La Nature" in lvl_title: title_en = "Nature & Elements"
        elif "La Famille" in lvl_title: title_en = "Family & People"
        elif "Les Aliments" in lvl_title: title_en = "Food & Drinks"
        elif "Mots complexes" in lvl_title: title_en = "Complex Words: Madd, Sukūn & Shaddah"
        elif "Phrases Nominales 1" in lvl_title: title_en = "Nominal Sentences 1: Subject & Description"
        elif "Phrases Nominales 2" in lvl_title: title_en = "Nominal Sentences 2: Qualities & States"
        elif "Phrases Verbales 1" in lvl_title: title_en = "Verbal Sentences 1: Verb & Subject"
        elif "Phrases Verbales 2" in lvl_title: title_en = "Verbal Sentences 2: Actions & Movements"
        elif "Phrases Complètes 1" in lvl_title: title_en = "Complete Sentences 1: Action on an Object"
        elif "Phrases Complètes 2" in lvl_title: title_en = "Complete Sentences 2: Daily Life Actions"
        elif "Politesse" in lvl_title: title_en = "Politeness & Common Expressions"
        elif "Phrases avec Prépositions" in lvl_title: title_en = "Sentences with Prepositions (fee, ilā, 'alā)"
        elif "Mini-Histoires" in lvl_title: title_en = "Short Stories & Comprehension"

        # English descriptions
        desc_en = "Listen attentively and select the corresponding letter or sign."
        if "Écoute le son" in lvl_desc: desc_en = "Listen to the sound and catch the correct letter."
        elif "Distingue" in lvl_desc: desc_en = "Listen carefully and distinguish the subtle sound differences."
        elif "Assemble" in lvl_desc or "Écris" in lvl_desc or "construis" in lvl_desc: desc_en = "Listen and assemble the letters in the correct order."
        elif "Lis" in lvl_desc: desc_en = "Listen and read the complete sentence with accuracy."
        elif "Reconnais" in lvl_desc: desc_en = "Recognize the correct Arabic phrase and meaning."

        lvl['titleEn'] = title_en
        lvl['descriptionEn'] = desc_en
        
        # WordItems translations
        for wd in lvl.get('wordItems', []):
            meaning_fr = wd.get('translationFr', wd.get('meaning', ''))
            if meaning_fr in word_translations_en:
                wd['translationEn'] = word_translations_en[meaning_fr]
            else:
                wd['translationEn'] = meaning_fr
                
        # Items translations for World 7/8
        for it in lvl.get('items', []):
            pdesc = it.get('phonemeDesc', '')
            if pdesc in phrases_en:
                it['phonemeDescEn'] = phrases_en[pdesc]
            elif pdesc in word_translations_en:
                it['phonemeDescEn'] = word_translations_en[pdesc]

new_json = json.dumps(worlds, ensure_ascii=False, indent=2)
new_curriculum_text = f"import {{ World }} from '../types/game';\n\nexport const WORLDS: World[] = {new_json};\n"

with open('src/data/curriculum.ts', 'w', encoding='utf-8') as f:
    f.write(new_curriculum_text)

print("src/data/curriculum.ts successfully enriched with English translations!")
