import json
import re
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Read curriculum.ts
with open('src/data/curriculum.ts', 'r', encoding='utf-8') as f:
    text = f.read()

m = re.search(r'export const WORLDS: World\[\] = (\[.*\]);', text, re.DOTALL)
if not m:
    print("Could not match WORLDS JSON")
    sys.exit(1)

worlds = json.loads(m.group(1))

# Exact 1-to-1 English translation mapping for every level ID 1 to 65
EXACT_LEVEL_TRANSLATIONS = {
    # WORLD 1 (1-10)
    1: {
        "titleEn": "Group 1: أ, ب, ت, ث",
        "descriptionEn": "Learn the first 4 letters with clear audio: Alif, Bā', Tā', and Thā'."
    },
    2: {
        "titleEn": "Group 2: ج, ح, خ, د",
        "descriptionEn": "Master deep throat and rasping sounds: Jeem, Ḥā', Khā', and Dāl."
    },
    3: {
        "titleEn": "Group 3: ذ, ر, ز, س",
        "descriptionEn": "Distinguish between interdental, rolled, and sharp whistling sounds."
    },
    4: {
        "titleEn": "Group 4: ش, ص, ض, ط",
        "descriptionEn": "Practice emphatic, deep mouth-filling consonants."
    },
    5: {
        "titleEn": "Group 5: ظ, ع, غ, ف",
        "descriptionEn": "Master guttural and throat consonants with clear native pronunciation."
    },
    6: {
        "titleEn": "Group 6: ق, ك, ل, م",
        "descriptionEn": "Distinguish the deep palate Qāf from the light, smiling Kāf."
    },
    7: {
        "titleEn": "Group 7: ن, هـ, و, ي",
        "descriptionEn": "Conclude the 28 alphabet letters with soft breath and glide sounds."
    },
    8: {
        "titleEn": "Dot Duel: ب, ت, ث, ن, ي",
        "descriptionEn": "Recognize identical boat shapes by their dot positions."
    },
    9: {
        "titleEn": "Emphatic & Guttural Duel",
        "descriptionEn": "Train your ear on the hardest contrasts: seen/ṣād, tā'/ṭā', dāl/ḍād."
    },
    10: {
        "titleEn": "Grand Alphabet Mastery Challenge",
        "descriptionEn": "Comprehensive test of all 28 Arabic letters in randomized audio tests."
    },

    # WORLD 2 (11-18)
    11: {
        "titleEn": "Initial Form (ـ...): Boat & Loop Family",
        "descriptionEn": "Identify letters reaching out their arm at the beginning of words."
    },
    12: {
        "titleEn": "Initial Form (ـ...): Whistling, Emphatics & Others",
        "descriptionEn": "Identify teeth and loop letters in initial connected position."
    },
    13: {
        "titleEn": "Medial Form (ـ...ـ): Boat & Loop Family",
        "descriptionEn": "Recognize letters that connect on both right and left sides."
    },
    14: {
        "titleEn": "Medial Form (ـ...ـ): Whistling, Emphatics & Others",
        "descriptionEn": "Spot intermediate connecting shapes in the middle of words."
    },
    15: {
        "titleEn": "Final Form (...ـ): Boat & Loop Family",
        "descriptionEn": "Recognize letters regaining their full tail at the end of words."
    },
    16: {
        "titleEn": "Final Form (...ـ): Closings & Tails",
        "descriptionEn": "Identify letters concluding the word with their distinctive final shape."
    },
    17: {
        "titleEn": "The 6 Non-Connecting Letters (أ د ذ ر ز و)",
        "descriptionEn": "Master the 6 letters that never attach to the left."
    },
    18: {
        "titleEn": "Grand Letter Positions Challenge (Initial, Medial, Final)",
        "descriptionEn": "Comprehensive test of letter shapes across all 4 positions in real time."
    },

    # WORLD 3 (19-26)
    19: {
        "titleEn": "Fatḥah (ـَ) - Basic Sounds",
        "descriptionEn": "Read short, crisp 'A' vowels on the first 14 alphabet letters."
    },
    20: {
        "titleEn": "Fatḥah (ـَ) - Emphatics & Gutturals",
        "descriptionEn": "Produce open, resonant 'A' sounds on heavy and throat consonants."
    },
    21: {
        "titleEn": "Ḍammah (ـُ) - Basic 'U' Sounds",
        "descriptionEn": "Round your lips for a crisp 1-beat 'U' (oo) sound on the first 14 letters."
    },
    22: {
        "titleEn": "Ḍammah (ـُ) - Advanced 'U' Sounds",
        "descriptionEn": "Produce rounded 'U' sounds on heavy and throat consonants."
    },
    23: {
        "titleEn": "Kasrah (ـِ) - Basic 'I' Sounds",
        "descriptionEn": "Produce a sharp, smiling 1-beat 'I' (ee) sound on the first 14 letters."
    },
    24: {
        "titleEn": "Kasrah (ـِ) - Advanced 'I' Sounds",
        "descriptionEn": "Produce smiling 'I' sounds on heavy and throat consonants."
    },
    25: {
        "titleEn": "3-Vowel Duel: A vs U vs I",
        "descriptionEn": "Instantly switch between the 3 short vowels on the same consonant."
    },
    26: {
        "titleEn": "Grand 3 Short Vowels Challenge (Harakāt)",
        "descriptionEn": "Ultimate speed and accuracy test for all short vowels across all 28 letters."
    },

    # WORLD 4 (27-32)
    27: {
        "titleEn": "Series A + A (Emphatics & Standard)",
        "descriptionEn": "Chain two open 'A' vowels in one smooth, uninterrupted breath."
    },
    28: {
        "titleEn": "Series A + U (Emphatics & Standard)",
        "descriptionEn": "Transition from an open mouth (A) to rounded lips (U) at steady tempo."
    },
    29: {
        "titleEn": "Series A + I (Throat, Emphatics & Whistling)",
        "descriptionEn": "Chain open (A) and smiling (I) vowels across difficult consonants."
    },
    30: {
        "titleEn": "Series U + I & U + A (Emphatics & Pronouns)",
        "descriptionEn": "Transition from rounded lips (U) to a smiling sound (I) or open mouth (A)."
    },
    31: {
        "titleEn": "Series I + A & Emphatic Discrimination Challenge",
        "descriptionEn": "Contrast light and heavy syllables with rapid 2-vowel transitions."
    },
    32: {
        "titleEn": "Grand 28-Letter & Emphatics Workshop",
        "descriptionEn": "Master rapid 2-beat syllable chaining across the entire Arabic alphabet."
    },

    # WORLD 5 (33-39)
    33: {
        "titleEn": "The Sukūn (ـْ) - Basic Syllables",
        "descriptionEn": "Lock consonants cleanly with zero vowel sound."
    },
    34: {
        "titleEn": "The Sukūn (ـْ) - Advanced Syllables",
        "descriptionEn": "Practice clean stops on heavy and throat consonants."
    },
    35: {
        "titleEn": "Madd Alif (ـَا) - Long 'Ā' Sound",
        "descriptionEn": "Elongate the open 'A' vowel over 2 full beats with Alif."
    },
    36: {
        "titleEn": "Madd Waw (ـُو) - Long 'Ū' Sound",
        "descriptionEn": "Elongate the rounded 'U' vowel over 2 full beats with Wāw."
    },
    37: {
        "titleEn": "Madd Ya (ـِي) - Long 'Ī' Sound",
        "descriptionEn": "Elongate the smiling 'I' vowel over 2 full beats with Yā'."
    },
    38: {
        "titleEn": "Short vs Long Duel: A & U Series",
        "descriptionEn": "Listen and contrast short vowels (1 beat) against long vowels (2 beats)."
    },
    39: {
        "titleEn": "Short vs Long Duel: I Series & Mixed",
        "descriptionEn": "Master the timing difference between short Kasrah and long Madd Yā'."
    },

    # WORLD 6 (40-45)
    40: {
        "titleEn": "The Shaddah (ـّ) : Doubled Stressed Consonant",
        "descriptionEn": "Hold a firm pause and stress the doubled consonant."
    },
    41: {
        "titleEn": "Tanwīn in -an (ـً) : Open Ending",
        "descriptionEn": "Read double Fatḥah with the crisp nunated end sound '-an'."
    },
    42: {
        "titleEn": "Tanwīn in -un (ـٌ) : Closed Ending",
        "descriptionEn": "Read double Ḍammah with the crisp nunated end sound '-un'."
    },
    43: {
        "titleEn": "Tanwīn in -in (ـٍ) & Grand 3-Tanwīn Duel",
        "descriptionEn": "Distinguish all three nunation sounds (-an, -un, -in) on noun endings."
    },
    44: {
        "titleEn": "Alif-Lām (الـ) : Lunar Letters (Pronounced Lām)",
        "descriptionEn": "Pronounce the definite article 'Al-' clearly before lunar letters."
    },
    45: {
        "titleEn": "Alif-Lām (الـ) : Solar Letters (Silent Lām + Shaddah)",
        "descriptionEn": "Assimilate the Lām directly into the following solar letter with Shaddah."
    },

    # WORLD 7 (46-55)
    46: {
        "titleEn": "3-Letter Base Action Verbs",
        "descriptionEn": "Assemble letters to build and read essential 3-letter Arabic verbs."
    },
    47: {
        "titleEn": "Daily Life Action Verbs",
        "descriptionEn": "Listen to and construct common daily action verbs."
    },
    48: {
        "titleEn": "Illustrated Words: House & Office",
        "descriptionEn": "Read and assemble everyday objects found around the house and desk."
    },
    49: {
        "titleEn": "Animals of the World",
        "descriptionEn": "Discover and write the names of popular animals in Arabic."
    },
    50: {
        "titleEn": "Nature & Elements",
        "descriptionEn": "Build words related to the sky, water, weather, and plants."
    },
    51: {
        "titleEn": "Family & People",
        "descriptionEn": "Read and recognize family members and everyday social roles."
    },
    52: {
        "titleEn": "Food & Delicious Drinks",
        "descriptionEn": "Assemble names of fruits, drinks, bread, and meals."
    },
    53: {
        "titleEn": "Complex Words: Madd, Sukūn & Shaddah",
        "descriptionEn": "Assemble rich words combining Madd, Sukūn, and Shaddah."
    },
    54: {
        "titleEn": "Listening & Spelling Word Challenge",
        "descriptionEn": "Listen to the pronounced word and burst the matching letter bubble!"
    },
    55: {
        "titleEn": "Grand Speed Reading Vocabulary Challenge",
        "descriptionEn": "The ultimate rapid word recognition test across all vocabulary themes!"
    },

    # WORLD 8 (56-65)
    56: {
        "titleEn": "Nominal Sentences 1: Subject & Description",
        "descriptionEn": "Read 2-word sentences describing everyday objects and qualities."
    },
    57: {
        "titleEn": "Nominal Sentences 2: Qualities & States",
        "descriptionEn": "Distinguish descriptions and characteristics in short sentences."
    },
    58: {
        "titleEn": "Verbal Sentences 1: Verb & Subject",
        "descriptionEn": "Read sentences describing actions performed by subjects."
    },
    59: {
        "titleEn": "Verbal Sentences 2: Actions & Movements",
        "descriptionEn": "Understand movements and travel in verbal sentences."
    },
    60: {
        "titleEn": "Complete Sentences 1: Action on an Object",
        "descriptionEn": "Read 3-element sentences: Subject + Verb + Direct Object."
    },
    61: {
        "titleEn": "Complete Sentences 2: Daily Life Actions",
        "descriptionEn": "Read concrete daily life sentences with accurate vowels."
    },
    62: {
        "titleEn": "Politeness & Common Expressions",
        "descriptionEn": "Recognize Arabic greetings, thanks, and polite everyday expressions."
    },
    63: {
        "titleEn": "Sentences with Prepositions (fee, ilā, 'alā, fawqa)",
        "descriptionEn": "Read sentences indicating locations and precise spatial positions."
    },
    64: {
        "titleEn": "Short Stories & Comprehension",
        "descriptionEn": "Read short paragraph stories enriched with descriptive adjectives."
    },
    65: {
        "titleEn": "🏆 Ultimate Fluent Reading Championship",
        "descriptionEn": "The supreme reading and comprehension championship in the Arabic language!"
    },
}

WORD_MAP_EN = {
    'كَتَبَ': 'To write',
    'دَرَسَ': 'To study',
    'قَرَأَ': 'To read',
    'رَسَمَ': 'To draw',
    'جَلَسَ': 'To sit',
    'ذَهَبَ': 'To go / To leave',
    'سَمِعَ': 'To hear / To listen',
    'أَكَلَ': 'To eat',
    'شَرِبَ': 'To drink',
    'فَتَحَ': 'To open',
    'بَاب': 'Door',
    'بَيْت': 'House',
    'كُرْسِيّ': 'Chair',
    'مَكْتَب': 'Desk / Office',
    'قَلَم': 'Pen / Pencil',
    'أَسَد': 'Lion',
    'جَمَل': 'Camel',
    'فِيل': 'Elephant',
    'طَيْر': 'Bird',
    'قِطّ': 'Cat',
    'كَلْب': 'Dog',
    'شَمْس': 'Sun',
    'قَمَر': 'Moon',
    'نَجْم': 'Star',
    'بَحْر': 'Sea',
    'سَمَاء': 'Sky',
    'شَجَرَة': 'Tree',
    'مَاء': 'Water',
    'حَلِيب': 'Milk',
    'خُبْز': 'Bread',
    'تَمْر': 'Dates',
    'عِنَب': 'Grapes',
    'تُفَّاح': 'Apple',
    'مَدْرَسَة': 'School',
    'حَدِيقَة': 'Garden',
    'عُصْفُور': 'Sparrow / Bird',
    'رُمَّان': 'Pomegranate',
}

# Apply to all worlds
for w in worlds:
    if w['id'] == 1:
        w['nameEn'] = "World 1: The Alphabet & 28 Sounds"
        w['descriptionEn'] = "Discover the clear studio sound of each fundamental Arabic letter."
    elif w['id'] == 2:
        w['nameEn'] = "World 2: The 4 Letter Shapes"
        w['descriptionEn'] = "Learn the 4 positions of letters: Isolated, Initial, Medial, and Final."
    elif w['id'] == 3:
        w['nameEn'] = "World 3: Short Vowels (Harakāt)"
        w['descriptionEn'] = "Master the 3 short vowel signs: Fatḥah (A), Ḍammah (U), and Kasrah (I)."
    elif w['id'] == 4:
        w['nameEn'] = "World 4: 2-Vowel Combinations"
        w['descriptionEn'] = "Chain two short vowels smoothly across all 28 Arabic letters."
    elif w['id'] == 5:
        w['nameEn'] = "World 5: Sukūn & Long Vowels (Madd)"
        w['descriptionEn'] = "Master consonant stops with Sukūn and 2-beat vowel elongations with Madd."
    elif w['id'] == 6:
        w['nameEn'] = "World 6: Shaddah, Tanwīn & Alif-Lām"
        w['descriptionEn'] = "Master doubled consonants, nunation endings, and solar/lunar reading rules."
    elif w['id'] == 7:
        w['nameEn'] = "World 7: Vocabulary & Everyday Words"
        w['descriptionEn'] = "Read and assemble everyday nouns, action verbs, and illustrated vocabulary."
    elif w['id'] == 8:
        w['nameEn'] = "World 8: Short Sentences & Fluency"
        w['descriptionEn'] = "Read nominal and verbal sentences with prepositions and fluent reading speed."

    for l in w['levels']:
        lid = l['id']
        if lid in EXACT_LEVEL_TRANSLATIONS:
            l['titleEn'] = EXACT_LEVEL_TRANSLATIONS[lid]['titleEn']
            l['descriptionEn'] = EXACT_LEVEL_TRANSLATIONS[lid]['descriptionEn']
        else:
            print(f"ERROR: Level {lid} missing from translation map!")

        if l.get('wordItems'):
            for wi in l['wordItems']:
                w_word = wi['word']
                if w_word in WORD_MAP_EN:
                    wi['translationEn'] = WORD_MAP_EN[w_word]

new_ts = f"""import {{ World }} from '../types/game';

export const WORLDS: World[] = {json.dumps(worlds, ensure_ascii=False, indent=2)};
"""

with open('src/data/curriculum.ts', 'w', encoding='utf-8') as f:
    f.write(new_ts)

print("SUCCESS: curriculum.ts updated with 100% exact 1-to-1 translations for all 65 levels!")
