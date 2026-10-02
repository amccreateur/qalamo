"""
GraphoArabe - Edge TTS Audio Generator
Generates clean, studio-quality neural Arabic audio files for all letters, phonemes, and words.
Voice options:
- ar-SA-HamedNeural (Male, standard classical Arabic)
- ar-SA-ZariyahNeural (Female, clear articulation)
"""
import os
import sys
import json
import asyncio
import edge_tts

sys.stdout.reconfigure(encoding='utf-8')

VOICE = "ar-SA-HamedNeural"
OUTPUT_DIR = os.path.join(os.path.dirname(__file__), "..", "assets", "audio")
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Complete list of phonemes and words for the GraphoGame curriculum
AUDIO_ITEMS = [
    # World 1: 28 Base Letter sounds
    {"id": "a_fatha", "text": "أَ", "filename": "phoneme_alif.mp3"},
    {"id": "ba_fatha", "text": "بَ", "filename": "phoneme_ba.mp3"},
    {"id": "ta_fatha", "text": "تَ", "filename": "phoneme_ta.mp3"},
    {"id": "tha_fatha", "text": "ثَ", "filename": "phoneme_tha.mp3"},
    {"id": "ja_fatha", "text": "جَ", "filename": "phoneme_jeem.mp3"},
    {"id": "hha_fatha", "text": "حَ", "filename": "phoneme_hha.mp3"},
    {"id": "kha_fatha", "text": "خَ", "filename": "phoneme_kha.mp3"},
    {"id": "da_fatha", "text": "دَ", "filename": "phoneme_dal.mp3"},
    {"id": "dha_fatha", "text": "ذَ", "filename": "phoneme_dhal.mp3"},
    {"id": "ra_fatha", "text": "رَ", "filename": "phoneme_ra.mp3"},
    {"id": "za_fatha", "text": "زَ", "filename": "phoneme_zay.mp3"},
    {"id": "sa_fatha", "text": "سَ", "filename": "phoneme_seen.mp3"},
    {"id": "sha_fatha", "text": "شَ", "filename": "phoneme_sheen.mp3"},
    {"id": "sad_fatha", "text": "صَ", "filename": "phoneme_sad.mp3"},
    {"id": "dad_fatha", "text": "ضَ", "filename": "phoneme_dad.mp3"},
    {"id": "taa_fatha", "text": "طَ", "filename": "phoneme_ttaa.mp3"},
    {"id": "zha_fatha", "text": "ظَ", "filename": "phoneme_zha.mp3"},
    {"id": "ayn_fatha", "text": "عَ", "filename": "phoneme_ayn.mp3"},
    {"id": "ghayn_fatha", "text": "غَ", "filename": "phoneme_ghayn.mp3"},
    {"id": "fa_fatha", "text": "فَ", "filename": "phoneme_fa.mp3"},
    {"id": "qa_fatha", "text": "قَ", "filename": "phoneme_qaf.mp3"},
    {"id": "ka_fatha", "text": "كَ", "filename": "phoneme_kaf.mp3"},
    {"id": "la_fatha", "text": "لَ", "filename": "phoneme_lam.mp3"},
    {"id": "ma_fatha", "text": "مَ", "filename": "phoneme_meem.mp3"},
    {"id": "na_fatha", "text": "نَ", "filename": "phoneme_noon.mp3"},
    {"id": "ha_fatha", "text": "هَ", "filename": "phoneme_haa.mp3"},
    {"id": "wa_fatha", "text": "وَ", "filename": "phoneme_waw.mp3"},
    {"id": "ya_fatha", "text": "يَ", "filename": "phoneme_yaa.mp3"},

    # World 2: Dammah (OU)
    {"id": "bu_damma", "text": "بُ", "filename": "phoneme_bu.mp3"},
    {"id": "tu_damma", "text": "تُ", "filename": "phoneme_tu.mp3"},
    {"id": "du_damma", "text": "دُ", "filename": "phoneme_du.mp3"},
    {"id": "ru_damma", "text": "رُ", "filename": "phoneme_ru.mp3"},
    {"id": "su_damma", "text": "سُ", "filename": "phoneme_su.mp3"},
    {"id": "mu_damma", "text": "مُ", "filename": "phoneme_mu.mp3"},
    {"id": "ku_damma", "text": "كُ", "filename": "phoneme_ku.mp3"},
    {"id": "lu_damma", "text": "لُ", "filename": "phoneme_lu.mp3"},

    # World 2: Kasrah (I)
    {"id": "bi_kasra", "text": "بِ", "filename": "phoneme_bi.mp3"},
    {"id": "ti_kasra", "text": "تِ", "filename": "phoneme_ti.mp3"},
    {"id": "di_kasra", "text": "دِ", "filename": "phoneme_di.mp3"},
    {"id": "ri_kasra", "text": "رِ", "filename": "phoneme_ri.mp3"},
    {"id": "si_kasra", "text": "سِ", "filename": "phoneme_si.mp3"},
    {"id": "mi_kasra", "text": "مِ", "filename": "phoneme_mi.mp3"},
    {"id": "ki_kasra", "text": "كِ", "filename": "phoneme_ki.mp3"},
    {"id": "li_kasra", "text": "لِ", "filename": "phoneme_li.mp3"},

    # World 2: Sukūn
    {"id": "ab_sukun", "text": "أَبْ", "filename": "phoneme_ab.mp3"},
    {"id": "bar_sukun", "text": "بَرْ", "filename": "phoneme_bar.mp3"},
    {"id": "qul_sukun", "text": "قُلْ", "filename": "phoneme_qul.mp3"},
    {"id": "min_sukun", "text": "مِنْ", "filename": "phoneme_min.mp3"},

    # World 3: Madd (Long Vowels)
    {"id": "baa_long", "text": "بَا", "filename": "phoneme_baa_long.mp3"},
    {"id": "taa_long", "text": "تَا", "filename": "phoneme_taa_long.mp3"},
    {"id": "daa_long", "text": "دَا", "filename": "phoneme_daa_long.mp3"},
    {"id": "raa_long", "text": "رَا", "filename": "phoneme_raa_long.mp3"},
    {"id": "boo_long", "text": "بُو", "filename": "phoneme_boo_long.mp3"},
    {"id": "too_long", "text": "تُو", "filename": "phoneme_too_long.mp3"},
    {"id": "doo_long", "text": "دُو", "filename": "phoneme_doo_long.mp3"},
    {"id": "soo_long", "text": "سُو", "filename": "phoneme_soo_long.mp3"},
    {"id": "bee_long", "text": "بِي", "filename": "phoneme_bee_long.mp3"},
    {"id": "tee_long", "text": "تِي", "filename": "phoneme_tee_long.mp3"},
    {"id": "dee_long", "text": "دِي", "filename": "phoneme_dee_long.mp3"},
    {"id": "see_long", "text": "سِي", "filename": "phoneme_see_long.mp3"},

    # World 4: Words
    {"id": "kataba", "text": "كَتَبَ", "filename": "word_kataba.mp3"},
    {"id": "darasa", "text": "دَرَسَ", "filename": "word_darasa.mp3"},
    {"id": "qaraa", "text": "قَرَأَ", "filename": "word_qaraa.mp3"},
    {"id": "rasama", "text": "رَسَمَ", "filename": "word_rasama.mp3"},
    {"id": "bab", "text": "بَاب", "filename": "word_bab.mp3"},
    {"id": "bayt", "text": "بَيْت", "filename": "word_bayt.mp3"},
    {"id": "shams", "text": "شَمْس", "filename": "word_shams.mp3"},
    {"id": "qamar", "text": "قَمَر", "filename": "word_qamar.mp3"},
    {"id": "najm", "text": "نَجْم", "filename": "word_najm.mp3"},
]

async def generate_single(item, voice=VOICE):
    out_path = os.path.join(OUTPUT_DIR, item["filename"])
    if os.path.exists(out_path):
        print(f"Skipping existing: {item['filename']}")
        return

    communicate = edge_tts.Communicate(item["text"], voice=voice, rate="-10%")
    await communicate.save(out_path)
    print(f"Generated: {item['text']} -> {item['filename']}")

async def main():
    print(f"=== Starting Edge TTS generation for GraphoArabe ({len(AUDIO_ITEMS)} items) ===")
    print(f"Voice: {VOICE}")
    print(f"Output: {OUTPUT_DIR}\n")

    for item in AUDIO_ITEMS:
        try:
            await generate_single(item)
            await asyncio.sleep(0.1) # slight delay to prevent rate limits
        except Exception as e:
            print(f"Error on {item['text']}: {e}")

    # Write manifest
    manifest_path = os.path.join(OUTPUT_DIR, "manifest.json")
    with open(manifest_path, "w", encoding="utf-8") as f:
        json.dump(AUDIO_ITEMS, f, ensure_ascii=False, indent=2)

    print("\n✅ All audio files generated successfully!")

if __name__ == "__main__":
    asyncio.run(main())

