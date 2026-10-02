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

# We use the explicit connecting anchor 'ـ' or full Wasl vocalic markers
# to force the TTS engine to voice the final vowel/tanwin 100% of the time (no Waqf/pausal Sukun).

master_wasl_items = [
    # Monde 5 : Shaddah
    ('rabba', 'رَبَّـ', clear_voice, '-15%'),
    ('madda', 'مَدَّـ', main_voice, '-15%'),
    ('allama', 'عَلَّمَـ', main_voice, '-15%'),
    ('shadda', 'شَدَّـ', main_voice, '-15%'),
    ('hassa', 'حَسَّـ', main_voice, '-15%'),

    # Monde 5 : Tanwin
    ('kitaban', 'كِتَابًاـ', main_voice, '-15%'),
    ('kitabun', 'كِتَابٌـ', main_voice, '-15%'),
    ('kitabin', 'كِتَابٍـ', main_voice, '-15%'),
    ('waladan', 'وَلَدًاـ', main_voice, '-15%'),
    ('waladun', 'وَلَدٌـ', main_voice, '-15%'),
    ('waladin', 'وَلَدٍـ', main_voice, '-15%'),
    ('baytan', 'بَيْتًاـ', main_voice, '-15%'),
    ('baytun', 'بَيْتٌـ', main_voice, '-15%'),
    ('baytin', 'بَيْتٍـ', main_voice, '-15%'),

    # Monde 5 : Alif-Lam Solaire & Lunaire
    ('al_qamar', 'القَمَرُـ', main_voice, '-15%'),
    ('ash_shams', 'الشَّمْسُـ', main_voice, '-15%'),
    ('al_kitaab', 'الكِتَابُـ', main_voice, '-15%'),
    ('an_najm', 'النَّجْمُـ', jeem_voice, '-15%'),
    ('al_walad', 'الوَلَدُـ', main_voice, '-15%'),
    ('at_tayr', 'الطَّيْرُـ', main_voice, '-15%'),

    # Monde 6 : Verbes
    ('kataba', 'كَتَبَـ', main_voice, '-15%'),
    ('darasa', 'دَرَسَـ', main_voice, '-15%'),
    ('qaraa', 'قَرَأَـ', main_voice, '-15%'),
    ('rasama', 'رَسَمَـ', main_voice, '-15%'),
    ('jalasa', 'جَلَسَـ', main_voice, '-15%'),
    ('dhahaba', 'ذَهَبَـ', main_voice, '-15%'),
    ('samia', 'سَمِعَـ', main_voice, '-15%'),
    ('akala', 'أَكَلَـ', main_voice, '-15%'),
    ('shariba', 'شَرِبَـ', main_voice, '-15%'),
    ('fataha', 'فَتَحَـ', main_voice, '-15%'),
    ('dakhala', 'دَخَلَـ', main_voice, '-15%'),
    ('kharaja', 'خَرَجَـ', main_voice, '-15%'),
    ('naama', 'نَامَـ', main_voice, '-15%'),

    # Monde 6 : Noms
    ('bab', 'بَابٌـ', main_voice, '-15%'),
    ('bayt', 'بَيْتٌـ', main_voice, '-15%'),
    ('kursiy', 'كُرْسِيٌّـ', main_voice, '-15%'),
    ('maktab', 'مَكْتَبٌـ', main_voice, '-15%'),
    ('qalam', 'قَلَمٌـ', main_voice, '-15%'),
    ('asad', 'أَسَدٌـ', main_voice, '-15%'),
    ('jamal', 'جَمَلٌـ', main_voice, '-15%'),
    ('feel', 'فِيلٌـ', main_voice, '-15%'),
    ('tayr', 'طَيْرٌـ', main_voice, '-15%'),
    ('qitt', 'قِطٌّـ', main_voice, '-15%'),
    ('kalb', 'كَلْبٌـ', main_voice, '-15%'),
    ('dubb', 'دُبٌّـ', main_voice, '-15%'),
    ('zahra', 'زَهْرَةٌـ', main_voice, '-15%'),
    ('shajara', 'شَجَرَةٌـ', main_voice, '-15%'),
    ('shams', 'شَمْسٌـ', main_voice, '-15%'),
    ('qamar', 'قَمَرٌـ', main_voice, '-15%'),
    ('najm', 'نَجْمٌـ', main_voice, '-15%'),
    ('bahr', 'بَحْرٌـ', main_voice, '-15%'),
    ('samaa', 'سَمَاءٌـ', main_voice, '-15%'),
    ('maa', 'مَاءٌـ', main_voice, '-15%'),
    ('nahr', 'نَهْرٌـ', main_voice, '-15%'),
    ('ab', 'أَبٌـ', main_voice, '-15%'),
    ('umm', 'أُمٌّـ', main_voice, '-15%'),
    ('akh', 'أَخٌـ', main_voice, '-15%'),
    ('ukht', 'أُخْتٌـ', main_voice, '-15%'),
    ('walad', 'وَلَدٌـ', main_voice, '-15%'),
    ('bint', 'بِنْتٌـ', main_voice, '-15%'),
    ('tifl', 'طِفْلٌـ', main_voice, '-15%'),
    ('muallim', 'مُعَلِّمٌـ', main_voice, '-15%'),
    ('haleeb', 'حَلِيبٌـ', main_voice, '-15%'),
    ('khubz', 'خُبْزٌـ', main_voice, '-15%'),
    ('tamr', 'تَمْرٌـ', main_voice, '-15%'),
    ('inab', 'عِنَبٌـ', main_voice, '-15%'),
    ('tuffah', 'تُفَّاحٌـ', main_voice, '-15%'),
    ('madrasa', 'مَدْرَسَةٌـ', main_voice, '-15%'),
    ('hadeeqa', 'حَدِيقَةٌـ', main_voice, '-15%'),
    ('ousfoor', 'عُصْفُورٌـ', main_voice, '-15%'),
    ('rumman', 'رُمَّانٌـ', main_voice, '-15%'),
    ('kitab', 'كِتَابٌـ', main_voice, '-15%'),

    # Monde 7 : Phrases Nominales
    ('albayt_kabeer', 'البَيْتُ كَبِيرٌـ', main_voice, '-15%'),
    ('almaa_baarid', 'المَاءُ بَارِدٌـ', main_voice, '-15%'),
    ('alkitaab_mufeed', 'الكِتَابُ مُفِيدٌـ', main_voice, '-15%'),
    ('ashshams_mushriqa', 'الشَّمْسُ مُشْرِقَةٌـ', main_voice, '-15%'),
    ('alqamar_muneer', 'القَمَرُ مُنِيرٌـ', main_voice, '-15%'),
    ('alwalad_nasheet', 'الوَلَدُ نَشِيطٌـ', main_voice, '-15%'),
    ('albint_dhakiyya', 'البِنْتُ ذَكِيَّةٌـ', main_voice, '-15%'),
    ('alqalam_jadeed', 'القَلَمُ جَدِيدٌـ', main_voice, '-15%'),
    ('albaab_maftooh', 'البَابُ مَفْتُوحٌـ', main_voice, '-15%'),
    ('azzahra_jameela', 'الزَّهْرَةُ جَمِيلَةٌـ', main_voice, '-15%'),

    # Monde 7 : Phrases Verbales
    ('kataba_alwalad', 'كَتَبَ الوَلَدُـ', main_voice, '-15%'),
    ('qaraa_attaalib', 'قَرَأَ الطَّالِبُـ', main_voice, '-15%'),
    ('jalasa_alab', 'جَلَسَ الأَبُـ', main_voice, '-15%'),
    ('akala_attifl', 'أَكَلَ الطِّفْلُـ', main_voice, '-15%'),
    ('shariba_alwalad', 'شَرِبَ الوَلَدُـ', main_voice, '-15%'),
    ('naama_attifl', 'نَامَ الطِّفْلُـ', main_voice, '-15%'),
    ('dhahaba_alwalad', 'ذَهَبَ الوَلَدُـ', main_voice, '-15%'),
    ('rajaa_alab', 'رَجَعَ الأَبُـ', main_voice, '-15%'),
    ('kharaja_almuallim', 'خَرَجَ المُعَلِّمُـ', main_voice, '-15%'),
    ('dakhala_attaalib', 'دَخَلَ الطَّالِبُـ', main_voice, '-15%'),
    ('taara_alousfoor', 'طَارَ العُصْفُورُـ', main_voice, '-15%'),

    # Monde 7 : Phrases Complètes (Verbe + Sujet + Objet)
    ('qaraa_alwalad_alkitaab', 'قَرَأَ الوَلَدُ الكِتَابَـ', main_voice, '-15%'),
    ('kataba_attaalib_addars', 'كَتَبَ الطَّالِبُ الدَّرْسَـ', main_voice, '-15%'),
    ('shariba_attifl_alhaleeb', 'شَرِبَ الطِّفْلُ الحَلِيبَـ', main_voice, '-15%'),
    ('fataha_alab_albaab', 'فَتَحَ الأَبُ البَابَـ', main_voice, '-15%'),
    ('akala_alwalad_attamr', 'أَكَلَ الوَلَدُ التَّمْرَـ', main_voice, '-15%'),
    ('rasama_alwalad_ashshajara', 'رَسَمَ الوَلَدُ الشَّجَرَةَـ', main_voice, '-15%'),

    # Monde 7 : Politesse & Expressions
    ('assalamu_alaykum', 'السَّلَامُ عَلَيْكُمْ', main_voice, '-15%'),
    ('ahlan_wa_sahlan', 'أَهْلًا وَسَهْلًاـ', main_voice, '-15%'),
    ('shukran_jazeelan', 'شُكْرًا جَزِيلًاـ', main_voice, '-15%'),
    ('sabahu_alkhayr', 'صَبَاحُ الخَيْرِـ', main_voice, '-15%'),
    ('masau_alkhayr', 'مَسَاءُ الخَيْرِـ', main_voice, '-15%'),

    # Monde 7 : Prépositions & Mini-Histoires
    ('dhahaba_alwalad_ilal_madrasa', 'ذَهَبَ الوَلَدُ إِلَى المَدْرَسَةِـ', main_voice, '-15%'),
    ('jalasa_alab_alal_kursiyy', 'جَلَسَ الأَبُ عَلَى الكُرْسِيِّـ', main_voice, '-15%'),
    ('alkitaab_fil_haqeeba', 'الكِتَابُ فِي الحَقِيبَةِـ', main_voice, '-15%'),
    ('alousfoor_fawqa_ashshajara', 'العُصْفُورُ فَوْقَ الشَّجَرَةِـ', main_voice, '-15%'),
    ('qaraa_ahmad_kitaaban_mufeedan', 'قَرَأَ أَحْمَدُ كِتَابًا مُفِيدًاـ', main_voice, '-15%'),
    ('dhahabat_fatima_ilal_hadeeqa', 'ذَهَبَتْ فَاطِمَةُ إِلَى الحَدِيقَةِـ', main_voice, '-15%'),
    ('akala_alwalad_tuffahatan', 'أَكَلَ الوَلَدُ تُفَّاحَةً لَذِيذَةًـ', main_voice, '-15%'),
]

async def main():
    print(f"Generating {len(master_wasl_items)} strictly vocalized Wasl audio files...")
    for wid, wtext, voice, rate in master_wasl_items:
        fname = f"assets/audio/generated/{wid}.mp3"
        try:
            comm = edge_tts.Communicate(wtext, voice, rate=rate)
            await comm.save(fname)
            print(f"✓ Wasl OK: {fname} ({wtext})")
        except Exception as e:
            print(f"✗ Error {fname}: {e}")

    print("All master Wasl files generated successfully!")

if __name__ == '__main__':
    asyncio.run(main())

