import asyncio
import os
import sys
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

os.makedirs('assets/audio/generated', exist_ok=True)

# Using HamedNeural (Saudi Standard Arabic) and FahedNeural for perfect classical Jeem (ج)
hamed_voice = 'ar-SA-HamedNeural'
fahed_voice = 'ar-KW-FahedNeural'

jeem_items = [
    # Jeem vowels & syllables
    ('jeem_fatha', 'جَ', hamed_voice, '-15%'),
    ('jeem_damma', 'جُ', hamed_voice, '-15%'),
    ('jeem_kasra', 'جِ', hamed_voice, '-15%'),
    ('jeem_sukun', 'جْ', hamed_voice, '-15%'),
    ('naj_sukun', 'نَجْ', hamed_voice, '-15%'),

    # Words with Jeem
    ('najm', 'نَجْمٌـ', hamed_voice, '-15%'),
    ('an_najm', 'النَّجْمُـ', hamed_voice, '-15%'),
    ('jalasa', 'جَلَسَـ', hamed_voice, '-15%'),
    ('jamal', 'جَمَلٌـ', hamed_voice, '-15%'),
    ('shajara', 'شَجَرَةٌـ', hamed_voice, '-15%'),
    ('hadeeqa', 'حَدِيقَةٌـ', hamed_voice, '-15%'),
    ('rajaa_alab', 'رَجَعَ الأَبُـ', hamed_voice, '-15%'),
    ('jalasa_alab', 'جَلَسَ الأَبُـ', hamed_voice, '-15%'),
    ('jalasa_alab_alal_kursiyy', 'جَلَسَ الأَبُ عَلَى الكُرْسِيِّـ', hamed_voice, '-15%'),
    ('dhahabat_fatima_ilal_hadeeqa', 'ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِـ', hamed_voice, '-15%'),
    ('azzahra_jameela', 'الزَّهْرَةُ جَمِيلَةٌـ', hamed_voice, '-15%'),
    ('shukran_jazeelan', 'شُكْرًا جَزِيلًاـ', hamed_voice, '-15%'),
]

async def main():
    print("Regenerating all words with Jeem (ج) with classical Hamed/Fahed studio voice...")
    for wid, wtext, voice, rate in jeem_items:
        fname = f"assets/audio/generated/{wid}.mp3"
        try:
            comm = edge_tts.Communicate(wtext, voice, rate=rate)
            await comm.save(fname)
            print(f"✓ Fixed Jeem: {fname} ({wtext})")
        except Exception as e:
            print(f"✗ Error {fname}: {e}")

    print("All Jeem words fixed!")

if __name__ == '__main__':
    asyncio.run(main())

