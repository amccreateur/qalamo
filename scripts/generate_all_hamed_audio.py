import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets/audio/generated', exist_ok=True)

# 28 letters definition with sustained phonetic representations for Hamed (ar-SA-HamedNeural)
# Format: (key, raw_char, fatha_text, damma_text, kasra_text, sukun_text)
letters_vowels = [
    ('alif', 'أ', 'أَ', 'أُو', 'إِي', 'أَبْ'),
    ('ba', 'ب', 'بَا', 'بُو', 'بِي', 'أَبْ'),
    ('ta', 'ت', 'تَا', 'تُو', 'تِي', 'أَتْ'),
    ('tha', 'ث', 'ثَا', 'ثُو', 'ثِي', 'أَثْ'),
    ('jeem', 'ج', 'جَا', 'جُو', 'جِي', 'أَجْ'),
    ('hha', 'ح', 'حَا', 'حُو', 'حِي', 'أَحْ'),
    ('kha', 'خ', 'خَا', 'خُو', 'خِي', 'أَخْ'),
    ('dal', 'د', 'دَا', 'دُو', 'دِي', 'أَدْ'),
    ('dhal', 'ذ', 'ذَا', 'ذُو', 'ذِي', 'أَذْ'),
    ('ra', 'ر', 'رَا', 'رُو', 'رِي', 'أَرْ'),
    ('zay', 'ز', 'زَا', 'زُو', 'زِي', 'أَزْ'),
    ('seen', 'س', 'سَا', 'سُو', 'سِي', 'أَسْ'),
    ('sheen', 'ش', 'شَا', 'شُو', 'شِي', 'أَشْ'),
    ('sad', 'ص', 'صَا', 'صُو', 'صِي', 'أَصْ'),
    ('dad', 'ض', 'ضَا', 'ضُو', 'ضِي', 'أَضْ'),
    ('ttaa', 'ط', 'طَا', 'طُو', 'طِي', 'أَطْ'),
    ('zha', 'ظ', 'ظَا', 'ظُو', 'ظِي', 'أَظْ'),
    ('ayn', 'ع', 'عَا', 'عُو', 'عِي', 'أَعْ'),
    ('ghayn', 'غ', 'غَا', 'غُو', 'غِي', 'أَغْ'),
    ('fa', 'ف', 'فَا', 'فُو', 'فِي', 'أَفْ'),
    ('qaf', 'ق', 'قَا', 'قُو', 'قِي', 'أَقْ'),
    ('kaf', 'ك', 'كَا', 'كُو', 'كِي', 'أَكْ'),
    ('lam', 'ل', 'لَا', 'لُو', 'لِي', 'أَلْ'),
    ('meem', 'م', 'مَا', 'مُو', 'مِي', 'أَمْ'),
    ('noon', 'ن', 'نَا', 'نُو', 'نِي', 'أَنْ'),
    ('haa', 'هـ', 'هَا', 'هُو', 'هِي', 'أَهْ'),
    ('waw', 'و', 'وَا', 'وُو', 'وِي', 'أَوْ'),
    ('yaa', 'ي', 'يَا', 'يُو', 'يِي', 'أَيْ'),
]

vowel_types = ['fatha', 'damma', 'kasra', 'sukun']

words_and_syllables = [
    # Madd
    ('baa_long', 'بَا'), ('taa_long', 'تَا'), ('daa_long', 'دَا'), ('raa_long', 'رَا'),
    ('boo_long', 'بُو'), ('too_long', 'تُو'), ('doo_long', 'دُو'), ('soo_long', 'سُو'),
    ('bee_long', 'بِي'), ('tee_long', 'تِي'), ('dee_long', 'دِي'), ('see_long', 'سِي'),
    ('shoo_long', 'شُو'), ('shee_long', 'شِي'), ('ree_long', 'رِي'),
    # Syllables with sukun
    ('ab_sukun', 'أَبْ'), ('bar_sukun', 'بَرْ'), ('qul_sukun', 'قُلْ'), ('min_sukun', 'مِنْ'),
    ('at_sukun', 'أَتْ'), ('bal_sukun', 'بَلْ'), ('kul_sukun', 'كُلْ'), ('an_sukun', 'عَنْ'),
    ('bay_sukun', 'بَيْ'), ('sham_sukun', 'شَمْ'), ('naj_sukun', 'نَجْ'),
    # Words
    ('kataba', 'كَتَبَ'), ('darasa', 'دَرَسَ'), ('qaraa', 'قَرَأَ'), ('rasama', 'رَسَمَ'),
    ('bab', 'بَاب'), ('bayt', 'بَيْت'), ('shams', 'شَمْس'), ('qamar', 'قَمَر'), ('najm', 'نَجْم')
]

async def generate(text: str, filename: str, voice: str = 'ar-SA-HamedNeural', rate: str = '-15%'):
    try:
        comm = edge_tts.Communicate(text, voice, rate=rate)
        await comm.save(filename)
        return True
    except Exception as e:
        print(f"Error {filename} ({text}): {e}")
        return False

async def main():
    voice = 'ar-SA-HamedNeural'
    print(f"Generating all audio clips with {voice}...")
    
    # 1. Letters x 4 Vowels
    for item in letters_vowels:
        key = item[0]
        vtexts = item[2:] # fatha, damma, kasra, sukun
        for vname, vtext in zip(vowel_types, vtexts):
            fname = f"assets/audio/generated/{key}_{vname}.mp3"
            await generate(vtext, fname, voice, rate='-15%')

    # 2. Madd, Syllables, Words
    for wid, wtext in words_and_syllables:
        fname = f"assets/audio/generated/{wid}.mp3"
        await generate(wtext, fname, voice, rate='-15%')

    print(f"All audio files generated successfully with {voice}!")

if __name__ == '__main__':
    asyncio.run(main())
