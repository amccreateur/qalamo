import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets/audio/generated', exist_ok=True)

letters = [
    ('alif', 'أَ', 'أُ', 'إِ', 'أْ'),
    ('ba', 'بَ', 'بُ', 'بِ', 'بْ'),
    ('ta', 'تَ', 'تُ', 'تِ', 'تْ'),
    ('tha', 'ثَ', 'ثُ', 'ثِ', 'ثْ'),
    ('jeem', 'جَ', 'جُ', 'جِ', 'جْ'),
    ('hha', 'حَ', 'حُ', 'حِ', 'حْ'),
    ('kha', 'خَ', 'خُ', 'خِ', 'خْ'),
    ('dal', 'دَ', 'دُ', 'دِ', 'دْ'),
    ('dhal', 'ذَ', 'ذُ', 'ذِ', 'ذْ'),
    ('ra', 'رَ', 'رُ', 'رِ', 'رْ'),
    ('zay', 'زَ', 'زُ', 'زِ', 'زْ'),
    ('seen', 'سَ', 'سُ', 'سِ', 'سْ'),
    ('sheen', 'شَ', 'شُ', 'شِ', 'شْ'),
    ('sad', 'صَ', 'صُ', 'صِ', 'صْ'),
    ('dad', 'ضَ', 'ضُ', 'ضِ', 'ضْ'),
    ('ttaa', 'طَ', 'طُ', 'طِ', 'طْ'),
    ('zha', 'ظَ', 'ظُ', 'ظِ', 'ظْ'),
    ('ayn', 'عَ', 'عُ', 'عِ', 'عْ'),
    ('ghayn', 'غَ', 'غُ', 'غِ', 'غْ'),
    ('fa', 'فَ', 'فُ', 'فِ', 'فْ'),
    ('qaf', 'قَ', 'قُ', 'قِ', 'قْ'),
    ('kaf', 'كَ', 'كُ', 'كِ', 'كْ'),
    ('lam', 'لَ', 'لُ', 'لِ', 'لْ'),
    ('meem', 'مَ', 'مُ', 'مِ', 'مْ'),
    ('noon', 'نَ', 'نُ', 'نِ', 'نْ'),
    ('haa', 'هَ', 'هُ', 'هِ', 'هْ'),
    ('waw', 'وَ', 'وُ', 'وِ', 'وْ'),
    ('yaa', 'يَ', 'يُ', 'يِ', 'يْ'),
]

vowel_names = ['fatha', 'damma', 'kasra', 'sukun']

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

async def generate_file(text: str, filename: str, voice: str, rate: str = '-20%'):
    try:
        comm = edge_tts.Communicate(text, voice, rate=rate)
        await comm.save(filename)
        return True
    except Exception as e:
        # Fallback with alternative male voice
        fallback_voice = 'ar-SA-HamedNeural' if voice == 'ar-SA-ShakirNeural' else 'ar-SA-ShakirNeural'
        try:
            comm = edge_tts.Communicate(text, fallback_voice, rate=rate)
            await comm.save(filename)
            return True
        except Exception as e2:
            print(f"Error generating {filename} for {text}: {e2}")
            return False

async def main():
    voice = 'ar-SA-ShakirNeural'
    rate = '-22%'  # Slower, clearer, avoids cutting off at the end
    
    print("Generating vowels for all letters with rate=-22%...")
    for item in letters:
        lid = item[0]
        vtexts = item[1:]
        # Use Hamed for ttaa to guarantee precision
        chosen_voice = 'ar-SA-HamedNeural' if lid == 'ttaa' else voice
        for vname, vtext in zip(vowel_names, vtexts):
            fname = f"assets/audio/generated/{lid}_{vname}.mp3"
            success = await generate_file(vtext, fname, chosen_voice, rate)
            if success:
                print(f"Generated: {fname}")

    print("\nGenerating words & syllables with rate=-18%...")
    for wid, wtext in words_and_syllables:
        fname = f"assets/audio/generated/{wid}.mp3"
        success = await generate_file(wtext, fname, voice, rate='-18%')
        if success:
            print(f"Generated: {fname}")

    print("\nAll audio clips regenerated with elongated duration and smooth sound!")

if __name__ == '__main__':
    asyncio.run(main())
