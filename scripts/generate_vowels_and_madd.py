import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets/audio/generated', exist_ok=True)
os.makedirs('assets/audio/compare', exist_ok=True)

main_voice = 'ar-QA-MoazNeural'
jeem_voice = 'ar-KW-FahedNeural'

# 1. SHORT VOWELS (Monde 2 : Harakat - 1 temps / nettes et courtes)
# Format: (key, fatha_txt, damma_txt, kasra_txt, sukun_txt)
short_letters = [
    ('alif', 'أَ', 'أُ', 'إِ', 'أَبْ'),
    ('ba', 'بَ', 'بُ', 'بِ', 'أَبْ'),
    ('ta', 'تَ', 'تُ', 'تِ', 'أَتْ'),
    ('tha', 'ثَ', 'ثُ', 'ثِ', 'أَثْ'),
    ('jeem', 'جَ', 'جُ', 'جِ', 'أَجْ'),
    ('hha', 'حَ', 'حُ', 'حِ', 'أَحْ'),
    ('kha', 'خَ', 'خُ', 'خِ', 'أَخْ'),
    ('dal', 'دَ', 'دُ', 'دِ', 'أَدْ'),
    ('dhal', 'ذَ', 'ذُ', 'ذِ', 'أَذْ'),
    ('ra', 'رَ', 'رُ', 'رِ', 'أَرْ'),
    ('zay', 'زَ', 'زُ', 'زِ', 'أَزْ'),
    ('seen', 'سَ', 'سُ', 'سِ', 'أَسْ'),
    ('sheen', 'شَ', 'شُ', 'شِ', 'أَشْ'),
    ('sad', 'صَ', 'صُ', 'صِ', 'أَصْ'),
    ('dad', 'ضَ', 'ضُ', 'ضِ', 'أَضْ'),
    ('ttaa', 'طَ', 'طُ', 'طِ', 'أَطْ'),
    ('zha', 'ظَ', 'ظُ', 'ظِ', 'أَظْ'),
    ('ayn', 'عَ', 'عُ', 'عِ', 'أَعْ'),
    ('ghayn', 'غَ', 'غُ', 'غِ', 'أَغْ'),
    ('fa', 'فَ', 'فُ', 'فِ', 'أَفْ'),
    ('qaf', 'قَ', 'قُ', 'قِ', 'أَقْ'),
    ('kaf', 'كَ', 'كُ', 'كِ', 'أَكْ'),
    ('lam', 'لَ', 'لُ', 'لِ', 'أَلْ'),
    ('meem', 'مَ', 'مُ', 'مِ', 'أَمْ'),
    ('noon', 'نَ', 'نُ', 'نِ', 'أَنْ'),
    ('haa', 'هَ', 'هُ', 'هِ', 'أَهْ'),
    ('waw', 'وَ', 'وُ', 'وِ', 'أَوْ'),
    ('yaa', 'يَ', 'يُ', 'يِ', 'أَيْ'),
]

vowel_names = ['fatha', 'damma', 'kasra', 'sukun']

# 2. LONG VOWELS (Monde 3 : Madd - 2 temps prolongés / étirés)
madd_items = [
    ('baa_long', 'بَا'), ('taa_long', 'تَا'), ('daa_long', 'دَا'), ('raa_long', 'رَا'),
    ('boo_long', 'بُو'), ('too_long', 'تُو'), ('doo_long', 'دُو'), ('soo_long', 'سُو'),
    ('bee_long', 'بِي'), ('tee_long', 'تِي'), ('dee_long', 'دِي'), ('see_long', 'سِي'),
    ('shoo_long', 'شُو'), ('shee_long', 'شِي'), ('ree_long', 'رِي'),
]

# 3. SYLLABLES WITH SUKUN & WORDS
syllables_and_words = [
    ('ab_sukun', 'أَبْ'), ('bar_sukun', 'بَرْ'), ('qul_sukun', 'قُلْ'), ('min_sukun', 'مِنْ'),
    ('at_sukun', 'أَتْ'), ('bal_sukun', 'بَلْ'), ('kul_sukun', 'كُلْ'), ('an_sukun', 'عَنْ'),
    ('bay_sukun', 'بَيْ'), ('sham_sukun', 'شَمْ'), ('naj_sukun', 'نَجْ'),
    ('kataba', 'كَتَبَ'), ('darasa', 'دَرَسَ'), ('qaraa', 'قَرَأَ'), ('rasama', 'رَسَمَ'),
    ('bab', 'بَاب'), ('bayt', 'بَيْت'), ('shams', 'شَمْس'), ('qamar', 'قَمَر'), ('najm', 'نَجْم')
]

async def generate_file(text: str, filename: str, voice: str, rate: str):
    try:
        comm = edge_tts.Communicate(text, voice, rate=rate)
        await comm.save(filename)
        return True
    except Exception as e:
        print(f"Error {filename} ({text}): {e}")
        return False

async def main():
    print("1. Generating SHORT vowels (Harakat - rate=-5%, snappy & short)...")
    for item in short_letters:
        key = item[0]
        vtexts = item[1:]
        chosen_voice = jeem_voice if key == 'jeem' else main_voice
        for vname, vtext in zip(vowel_names, vtexts):
            fname = f"assets/audio/generated/{key}_{vname}.mp3"
            # Short vowel rate
            await generate_file(vtext, fname, chosen_voice, rate='-5%')

    print("\n2. Generating LONG vowels (Madd - rate=-40%, clearly elongated & sustained)...")
    for mid, mtext in madd_items:
        fname = f"assets/audio/generated/{mid}.mp3"
        # Long vowel rate with Madd prolongation
        await generate_file(mtext, fname, main_voice, rate='-40%')

    print("\n3. Generating Syllables & Words...")
    for wid, wtext in syllables_and_words:
        fname = f"assets/audio/generated/{wid}.mp3"
        chosen_voice = jeem_voice if 'ج' in wtext else main_voice
        await generate_file(wtext, fname, chosen_voice, rate='-15%')

    print("\nAll audio clips generated with sharp contrast between short vowels and Madd!")

if __name__ == '__main__':
    asyncio.run(main())

