import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets/audio/generated', exist_ok=True)

main_voice = 'ar-QA-MoazNeural'
jeem_voice = 'ar-KW-FahedNeural'
clear_voice = 'ar-SA-HamedNeural'

items_to_generate = [
    # Monde 5 : Shaddah
    ('rabba', 'رَبَّ', clear_voice, '-15%'),
    ('madda', 'مَدَّ', main_voice, '-15%'),
    ('allama', 'عَلَّمَ', main_voice, '-15%'),
    ('shadda', 'شَدَّ', main_voice, '-15%'),
    ('hassa', 'حَسَّ', main_voice, '-15%'),

    # Monde 5 : Tanwin
    ('kitaban', 'كِتَابًا', main_voice, '-15%'),
    ('kitabun', 'كِتَابٌ', main_voice, '-15%'),
    ('kitabin', 'كِتَابٍ', main_voice, '-15%'),
    ('waladan', 'وَلَدًا', main_voice, '-15%'),
    ('waladun', 'وَلَدٌ', main_voice, '-15%'),
    ('waladin', 'وَلَدٍ', main_voice, '-15%'),
    ('baytan', 'بَيْتًا', main_voice, '-15%'),
    ('baytun', 'بَيْتٌ', main_voice, '-15%'),
    ('baytin', 'بَيْتٍ', main_voice, '-15%'),

    # Monde 5 : Alif-Lam Solaire & Lunaire
    ('al_qamar', 'القَمَر', main_voice, '-15%'),
    ('ash_shams', 'الشَّمْس', main_voice, '-15%'),
    ('al_kitaab', 'الكِتَاب', main_voice, '-15%'),
    ('an_najm', 'النَّجْم', jeem_voice, '-15%'),
    ('al_walad', 'الوَلَد', main_voice, '-15%'),
    ('at_tayr', 'الطَّيْر', main_voice, '-15%'),

    # Monde 6 : Petites Phrases de lecture
    ('kataba_alwalad', 'كَتَبَ الوَلَدُ', main_voice, '-15%'),
    ('qaraa_attaalib', 'قَرَأَ الطَّالِبُ', main_voice, '-15%'),
    ('almaa_baarid', 'المَاءُ بَارِدٌ', main_voice, '-15%'),
    ('albayt_kabeer', 'البَيْتُ كَبِيرٌ', main_voice, '-15%'),
    ('ashshams_mushriqa', 'الشَّمْسُ مُشْرِقَةٌ', main_voice, '-15%'),
]

async def main():
    print("Generating complete 6-World audio files...")
    for wid, wtext, voice, rate in items_to_generate:
        fname = f"assets/audio/generated/{wid}.mp3"
        try:
            comm = edge_tts.Communicate(wtext, voice, rate=rate)
            await comm.save(fname)
            print(f"Generated {fname} ({wtext})")
        except Exception as e:
            print(f"Error {fname}: {e}")

    print("All 6-world audio files ready!")

if __name__ == '__main__':
    asyncio.run(main())
