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

# New rich words & syllables
rich_items = [
    # Fixed Najm
    ('najm', 'نَجْم', jeem_voice, '-12%'),
    ('naj_sukun', 'نَجْ', jeem_voice, '-12%'),

    # Verbs (Monde 4)
    ('jalasa', 'جَلَسَ', jeem_voice, '-15%'),
    ('dhahaba', 'ذَهَبَ', main_voice, '-15%'),
    ('samia', 'سَمِعَ', main_voice, '-15%'),
    ('akala', 'أَكَلَ', main_voice, '-15%'),
    ('shariba', 'شَرِبَ', main_voice, '-15%'),
    ('kharaja', 'خَرَجَ', jeem_voice, '-15%'),
    ('fataha', 'فَتَحَ', main_voice, '-15%'),

    # Illustrated Words (Monde 4)
    ('kitab', 'كِتَاب', main_voice, '-15%'),
    ('qalam', 'قَلَم', main_voice, '-15%'),
    ('asad', 'أَسَد', main_voice, '-15%'),
    ('jamal', 'جَمَل', jeem_voice, '-15%'),
    ('feel', 'فِيل', main_voice, '-15%'),
    ('tayr', 'طَيْر', main_voice, '-15%'),
    ('zahra', 'زَهْرَة', main_voice, '-15%'),
    ('shajara', 'شَجَرَة', jeem_voice, '-15%'),
    ('bahr', 'بَحْر', main_voice, '-15%'),
    ('samaa', 'سَمَاء', main_voice, '-15%'),
    ('maa', 'مَاء', main_voice, '-15%'),
    ('nahr', 'نَهْر', main_voice, '-15%'),

    # Extra Syllables & Shaddah
    ('kat_sukun', 'كَتْ', main_voice, '-15%'),
    ('qum_sukun', 'قُمْ', main_voice, '-15%'),
    ('qad_sukun', 'قَدْ', main_voice, '-15%'),
    ('hal_sukun', 'هَلْ', main_voice, '-15%'),
    ('zah_sukun', 'زَهْ', main_voice, '-15%'),
    ('bah_sukun', 'بَحْ', main_voice, '-15%'),
    ('nah_sukun', 'نَهْ', main_voice, '-15%'),
    ('tay_sukun', 'طَيْ', main_voice, '-15%'),
    ('taa_marbouta', 'ة', main_voice, '-15%'),
    ('hamza_alone', 'ء', main_voice, '-15%'),
]

async def generate():
    print("Generating rich curriculum audio clips...")
    for wid, wtext, voice, rate in rich_items:
        fname = f"assets/audio/generated/{wid}.mp3"
        try:
            comm = edge_tts.Communicate(wtext, voice, rate=rate)
            await comm.save(fname)
            print(f"Generated {fname} ({wtext})")
        except Exception as e:
            print(f"Error {fname}: {e}")

    print("All rich audio clips generated successfully!")

if __name__ == '__main__':
    asyncio.run(generate())

