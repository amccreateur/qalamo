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
    # Monde 6 : Mots supplémentaires
    ('kursiy', 'كُرْسِيٌّ', main_voice, '-15%'),
    ('maktab', 'مَكْتَبٌ', main_voice, '-15%'),
    ('qitt', 'قِطٌّ', main_voice, '-15%'),
    ('kalb', 'كَلْبٌ', main_voice, '-15%'),
    ('dubb', 'دُبٌّ', main_voice, '-15%'),
    ('zahra', 'زَهْرَةٌ', main_voice, '-15%'),
    ('ab', 'أَبٌ', main_voice, '-15%'),
    ('umm', 'أُمٌّ', main_voice, '-15%'),
    ('akh', 'أَخٌ', main_voice, '-15%'),
    ('ukht', 'أُخْتٌ', main_voice, '-15%'),
    ('walad', 'وَلَدٌ', main_voice, '-15%'),
    ('bint', 'بِنْتٌ', main_voice, '-15%'),
    ('tifl', 'طِفْلٌ', main_voice, '-15%'),
    ('muallim', 'مُعَلِّمٌ', main_voice, '-15%'),
    ('haleeb', 'حَلِيبٌ', main_voice, '-15%'),
    ('khubz', 'خُبْزٌ', main_voice, '-15%'),
    ('tamr', 'تَمْرٌ', main_voice, '-15%'),
    ('inab', 'عِنَبٌ', main_voice, '-15%'),
    ('tuffah', 'تُفَّاحٌ', main_voice, '-15%'),
    ('madrasa', 'مَدْرَسَةٌ', main_voice, '-15%'),
    ('hadeeqa', 'حَدِيقَةٌ', main_voice, '-15%'),
    ('ousfoor', 'عُصْفُورٌ', main_voice, '-15%'),
    ('rumman', 'رُمَّانٌ', main_voice, '-15%'),
    ('dakhala', 'دَخَلَ', main_voice, '-15%'),
    ('kharaja', 'خَرَجَ', main_voice, '-15%'),
    ('naama', 'نَامَ', main_voice, '-15%'),

    # Monde 7 : Phrases Nominales
    ('alkitaab_mufeed', 'الكِتَابُ مُفِيدٌ', main_voice, '-15%'),
    ('alqamar_muneer', 'القَمَرُ مُنِيرٌ', main_voice, '-15%'),
    ('alwalad_nasheet', 'الوَلَدُ نَشِيطٌ', main_voice, '-15%'),
    ('albint_dhakiyya', 'البِنْتُ ذَكِيَّةٌ', main_voice, '-15%'),
    ('alqalam_jadeed', 'القَلَمُ جَدِيدٌ', main_voice, '-15%'),
    ('albaab_maftooh', 'البَابُ مَفْتُوحٌ', main_voice, '-15%'),
    ('azzahra_jameela', 'الزَّهْرَةُ جَمِيلَةٌ', main_voice, '-15%'),

    # Monde 7 : Phrases Verbales
    ('jalasa_alab', 'جَلَسَ الأَبُ', main_voice, '-15%'),
    ('akala_attifl', 'أَكَلَ الطِّفْلُ', main_voice, '-15%'),
    ('shariba_alwalad', 'شَرِبَ الوَلَدُ', main_voice, '-15%'),
    ('naama_attifl', 'نَامَ الطِّفْلُ', main_voice, '-15%'),
    ('dhahaba_alwalad', 'ذَهَبَ الوَلَدُ', main_voice, '-15%'),
    ('rajaa_alab', 'رَجَعَ الأَبُ', main_voice, '-15%'),
    ('kharaja_almuallim', 'خَرَجَ المُعَلِّمُ', main_voice, '-15%'),
    ('dakhala_attaalib', 'دَخَلَ الطَّالِبُ', main_voice, '-15%'),
    ('taara_alousfoor', 'طَارَ العُصْفُورُ', main_voice, '-15%'),

    # Monde 7 : Phrases Complètes (Verbe + Sujet + Objet)
    ('qaraa_alwalad_alkitaab', 'قَرَأَ الوَلَدُ الكِتَابَ', main_voice, '-15%'),
    ('kataba_attaalib_addars', 'كَتَبَ الطَّالِبُ الدَّرْسَ', main_voice, '-15%'),
    ('shariba_attifl_alhaleeb', 'شَرِبَ الطِّفْلُ الحَلِيبَ', main_voice, '-15%'),
    ('fataha_alab_albaab', 'فَتَحَ الأَبُ البَابَ', main_voice, '-15%'),
    ('akala_alwalad_attamr', 'أَكَلَ الوَلَدُ التَّمْرَ', main_voice, '-15%'),
    ('rasama_alwalad_ashshajara', 'رَسَمَ الوَلَدُ الشَّجَرَةَ', main_voice, '-15%'),

    # Monde 7 : Politesse & Expressions
    ('assalamu_alaykum', 'السَّلَامُ عَلَيْكُمْ', main_voice, '-15%'),
    ('ahlan_wa_sahlan', 'أَهْلًا وَسَهْلًا', main_voice, '-15%'),
    ('shukran_jazeelan', 'شُكْرًا جَزِيلًا', main_voice, '-15%'),
    ('sabahu_alkhayr', 'صَبَاحُ الخَيْرِ', main_voice, '-15%'),
    ('masau_alkhayr', 'مَسَاءُ الخَيْرِ', main_voice, '-15%'),

    # Monde 7 : Prépositions & Mini-Histoires
    ('dhahaba_alwalad_ilal_madrasa', 'ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِ', main_voice, '-15%'),
    ('jalasa_alab_alal_kursiyy', 'جَلَسَ الأَبُ عَلَى الكُرْسِيِّ', main_voice, '-15%'),
    ('alkitaab_fil_haqeeba', 'الكِتَابُ فِي الحَقِيبَةِ', main_voice, '-15%'),
    ('alousfoor_fawqa_ashshajara', 'العُصْفُورُ فَوْقَ الشَّجَرَةِ', main_voice, '-15%'),
    ('qaraa_ahmad_kitaaban_mufeedan', 'قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًا', main_voice, '-15%'),
    ('dhahabat_fatima_ilal_hadeeqa', 'ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِ', main_voice, '-15%'),
    ('akala_alwalad_tuffahatan', 'أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةً', main_voice, '-15%'),
]

async def main():
    print(f"Generating {len(items_to_generate)} audio files for World 6 & World 7...")
    for wid, wtext, voice, rate in items_to_generate:
        fname = f"assets/audio/generated/{wid}.mp3"
        try:
            comm = edge_tts.Communicate(wtext, voice, rate=rate)
            await comm.save(fname)
            print(f"✓ Generated {fname} ({wtext})")
        except Exception as e:
            print(f"✗ Error {fname}: {e}")

    print("Generation complete!")

if __name__ == '__main__':
    asyncio.run(main())

