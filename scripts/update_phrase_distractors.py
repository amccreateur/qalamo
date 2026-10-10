import json
import sys
sys.stdout.reconfigure(encoding='utf-8')

FILE_PATH = 'src/data/curriculum.ts'

with open(FILE_PATH, 'r', encoding='utf-8') as f:
    text = f.read()

prefix = "export const WORLDS: World[] = "
idx = text.find(prefix)
if idx == -1:
    print("Prefix not found!")
    sys.exit(1)

json_str = text[idx + len(prefix):].rstrip()
if json_str.endswith(';'):
    json_str = json_str[:-1]

worlds = json.loads(json_str)

# Mapping of level_id -> dict of item_id -> list of close distractors
CLOSE_DISTRACTORS = {
    # Level 56 (Nominal Sentences 1: Subject & Description)
    56: {
        "albayt_kabeer": ["البَيْتُ صَغِيرٌ", "البَابُ كَبِيرٌ", "بَيْتٌ كَبِيرٌ"],
        "almaa_baarid": ["المَاءُ حَارٌّ", "الحَلِيبُ بَارِدٌ", "مَاءٌ بَارِدٌ"],
        "alkitaab_mufeed": ["الكِتَابُ جَدِيدٌ", "القَلَمُ مُفِيدٌ", "كِتَابٌ مُفِيدٌ"],
        "ashshams_mushriqa": ["الشَّمْسُ حَارَّةٌ", "السَّمَاءُ مُشْرِقَةٌ", "شَمْسٌ مُشْرِقَةٌ"],
        "alqamar_muneer": ["القَمَرُ بَعِيدٌ", "النَّجْمُ مُنِيرٌ", "قَمَرٌ مُنِيرٌ"]
    },
    # Level 57 (Nominal Sentences 2: Qualities & States)
    57: {
        "alwalad_nasheet": ["الوَلَدُ ذَكِيٌّ", "الطَّالِبُ نَشِيطٌ", "وَلَدٌ نَشِيطٌ"],
        "albint_dhakiyya": ["البِنْتُ نَشِيطَةٌ", "المُعَلِّمَةُ ذَكِيَّةٌ", "بِنْتٌ ذَكِيَّةٌ"],
        "alqalam_jadeed": ["القَلَمُ صَغِيرٌ", "الكِتَابُ جَدِيدٌ", "قَلَمٌ جَدِيدٌ"],
        "albaab_maftooh": ["البَابُ مُغْلَقٌ", "البَيْتُ مَفْتُوحٌ", "بَابٌ مَفْتُوحٌ"],
        "azzahra_jameela": ["الزَّهْرَةُ حَمْرَاءُ", "الحَدِيقَةُ جَمِيلَةٌ", "زَهْرَةٌ جَمِيلَةٌ"]
    },
    # Level 58 (Verbal Sentences 1: Subject & Verb)
    58: {
        "kataba_alwalad": ["قَرَأَ الوَلَدُ", "كَتَبَ الطَّالِبُ", "كَتَبَتِ البِنْتُ"],
        "qaraa_attaalib": ["كَتَبَ الطَّالِبُ", "قَرَأَ المُعَلِّمُ", "قَرَأَتِ الطَّالِبَةُ"],
        "jalasa_alab": ["قَامَ الأَبُ", "جَلَسَ الوَلَدُ", "جَلَسَتِ الأُمُّ"],
        "akala_attifl": ["شَرِبَ الطِّفْلُ", "أَكَلَ الوَلَدُ", "أَكَلَتِ البِنْتُ"],
        "shariba_alwalad": ["أَكَلَ الوَلَدُ", "شَرِبَ الطِّفْلُ", "شَرِبَتِ البِنْتُ"],
        "naama_attifl": ["قَامَ الطِّفْلُ", "نَامَ الوَلَدُ", "نَامَتِ البِنْتُ"]
    },
    # Level 59 (Verbal Sentences 2: Actions & Movements)
    59: {
        "dhahaba_alwalad": ["رَجَعَ الوَلَدُ", "ذَهَبَ الطَّالِبُ", "ذَهَبَتِ البِنْتُ"],
        "rajaa_alab": ["ذَهَبَ الأَبُ", "رَجَعَ الوَلَدُ", "رَجَعَتِ الأُمُّ"],
        "kharaja_almuallim": ["دَخَلَ المُعَلِّمُ", "خَرَجَ الطَّالِبُ", "خَرَجَتِ المُعَلِّمَةُ"],
        "dakhala_attaalib": ["خَرَجَ الطَّالِبُ", "دَخَلَ المُعَلِّمُ", "دَخَلَتِ الطَّالِبَةُ"],
        "taara_alousfoor": ["حَطَّ العُصْفُورُ", "طَارَ الطَّيْرُ", "طَارَتِ الحَمَامَةُ"]
    },
    # Level 60 (Complete Sentences 1: Verb + Subject + Object)
    60: {
        "qaraa_alwalad_alkitaab": ["كَتَبَ الوَلَدُ الكِتَابَ", "قَرَأَ الوَلَدُ الدَّرْسَ", "قَرَأَ الطَّالِبُ الكِتَابَ"],
        "kataba_attaalib_addars": ["قَرَأَ الطَّالِبُ الدَّرْسَ", "كَتَبَ الطَّالِبُ الكِتَابَ", "كَتَبَ الوَلَدُ الدَّرْسَ"],
        "shariba_attifl_alhaleeb": ["شَرِبَ الطِّفْلُ المَاءَ", "أَكَلَ الطِّفْلُ الحَلِيبَ", "شَرِبَ الوَلَدُ الحَلِيبَ"],
        "akala_alwalad_attamr": ["أَكَلَ الوَلَدُ التُّفَّاحَ", "شَرِبَ الوَلَدُ التَّمْرَ", "أَكَلَ الطِّفْلُ التَّمْرَ"]
    },
    # Level 61 (Complete Sentences 2: Daily Life Actions)
    61: {
        "fataha_alab_albaab": ["أَغْلَقَ الأَبُ البَابَ", "فَتَحَ الأَبُ الكِتَابَ", "فَتَحَ الوَلَدُ البَابَ"],
        "rasama_alwalad_ashshajara": ["رَسَمَ الوَلَدُ الزَّهْرَةَ", "قَطَفَ الوَلَدُ الشَّجَرَةَ", "رَسَمَتِ البِنْتُ الشَّجَرَةَ"],
        "qaraa_alwalad_alkitaab": ["فَتَحَ الوَلَدُ الكِتَابَ", "قَرَأَ الوَلَدُ الدَّرْسَ", "قَرَأَتِ البِنْتُ الكِتَابَ"],
        "kataba_attaalib_addars": ["فَهِمَ الطَّالِبُ الدَّرْسَ", "كَتَبَ الطَّالِبُ القِصَّةَ", "كَتَبَتِ الطَّالِبَةُ الدَّرْسَ"]
    },
    # Level 62 (Politeness & Greetings)
    62: {
        "assalamu_alaykum": ["السَّلَامُ عَلَيْكَ", "السَّلَامُ عَلَيْكِ", "عَلَيْكُمُ السَّلَامُ"],
        "ahlan_wa_sahlan": ["أَهْلًا بِكُمْ", "أَهْلًا بِكَ", "سَهْلًا وَأَهْلًا"],
        "shukran_jazeelan": ["شُكْرًا لَكُمْ", "عَفْوًا جَزِيلًا", "شُكْرًا كَثِيرًا"],
        "sabahu_alkhayr": ["صَبَاحُ النُّورِ", "مَسَاءُ الخَيْرِ", "صَبَاحُ الوَرْدِ"],
        "masau_alkhayr": ["مَسَاءُ النُّورِ", "صَبَاحُ الخَيْرِ", "مَسَاءُ الوَرْدِ"]
    },
    # Level 63 (Prepositions)
    63: {
        "dhahaba_alwalad_ilal_madrasa": ["ذَهَبَ الوَلَدُ إِلَى الحَدِيقَةِ", "رَجَعَ الوَلَدُ مِنَ المَدْرَسَةِ", "ذَهَبَ الطَّالِبُ إِلَى المَدْرَسَةِ"],
        "jalasa_alab_alal_kursiyy": ["جَلَسَ الوَلَدُ عَلَى الكُرْسِيِّ", "قَامَ الأَبُ عَنِ الكُرْسِيِّ", "جَلَسَ الأَبُ فِي البَيْتِ"],
        "alkitaab_fil_haqeeba": ["القَلَمُ فِي الحَقِيبَةِ", "الكِتَابُ عَلَى المَكْتَبِ", "كِتَابٌ فِي الحَقِيبَةِ"],
        "alousfoor_fawqa_ashshajara": ["العُصْفُورُ عَلَى الشَّجَرَةِ", "القِطُّ تَحْتَ الشَّجَرَةِ", "الطَّيْرُ فَوْقَ الشَّجَرَةِ"]
    },
    # Level 64 (Mini Stories)
    64: {
        "qaraa_ahmad_kitaaban_mufeedan": ["قَرَأَ أَحْمَدُ كِتَابًا جَدِيدًا", "كَتَبَ أَحْمَدُ كِتَابًا مُفِيدًا", "قَرَأَ عُمَرُ كِتَابًا مُفِيدًا"],
        "dhahabat_fatima_ilal_hadeeqa": ["ذَهَبَتْ فَاطِمَةُ إِلَى المَدْرَسَةِ", "رَجَعَتْ فَاطِمَةُ مِنَ الحَدِيقَةِ", "ذَهَبَتْ مَرْيَمُ إِلَى الحَدِيقَةِ"],
        "akala_alwalad_tuffahatan": ["أَكَلَ الوَلَدُ تُفَّاحَةً حَمْرَاءَ", "أَكَلَتِ البِنْتُ تُفَّاحَةً لَذِيذَةً", "شَرِبَ الوَلَدُ عَصِيرًا لَذِيذًا"]
    },
    # Level 65 (Grand Championship)
    65: {
        "qaraa_alwalad_alkitaab": ["قَرَأَ الوَلَدُ الدَّرْسَ", "كَتَبَ الوَلَدُ الكِتَابَ", "قَرَأَ الطَّالِبُ الكِتَابَ"],
        "dhahaba_alwalad_ilal_madrasa": ["ذَهَبَ الوَلَدُ إِلَى الحَدِيقَةِ", "رَجَعَ الوَلَدُ مِنَ المَدْرَسَةِ", "ذَهَبَ الطَّالِبُ إِلَى المَدْرَسَةِ"],
        "ashshams_mushriqa": ["الشَّمْسُ حَارَّةٌ", "السَّمَاءُ مُشْرِقَةٌ", "شَمْسٌ مُشْرِقَةٌ"],
        "assalamu_alaykum": ["السَّلَامُ عَلَيْكَ", "السَّلَامُ عَلَيْكِ", "عَلَيْكُمُ السَّلَامُ"],
        "qaraa_ahmad_kitaaban_mufeedan": ["قَرَأَ أَحْمَدُ كِتَابًا جَدِيدًا", "كَتَبَ أَحْمَدُ كِتَابًا مُفِيدًا", "قَرَأَ عُمَرُ كِتَابًا مُفِيدًا"]
    }
}

count_updated = 0
for w in worlds:
    for lvl in w.get('levels', []):
        lvl_id = lvl['id']
        if lvl_id in CLOSE_DISTRACTORS:
            for item in lvl.get('items', []):
                item_id = item['id']
                if item_id in CLOSE_DISTRACTORS[lvl_id]:
                    old_dist = item.get('distractors', [])
                    new_dist = CLOSE_DISTRACTORS[lvl_id][item_id]
                    item['distractors'] = new_dist
                    count_updated += 1
                    print(f"Updated Level {lvl_id} item '{item_id}' ({item['grapheme']}):")
                    print(f"   OLD: {old_dist}")
                    print(f"   NEW: {new_dist}")

new_content = f"import {{ World }} from '../types/game';\n\nexport const WORLDS: World[] = {json.dumps(worlds, ensure_ascii=False, indent=2)};\n"

with open(FILE_PATH, 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\nSUCCESS: Updated {count_updated} items across phrase levels 56-65!")
