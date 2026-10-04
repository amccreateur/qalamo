import asyncio
import os
import subprocess
import edge_tts

# Complete 2-letter 2-vowel words covering all 28 letters with strong emphasis on emphatics & gutturals
ALL_TWO_VOWEL_WORDS = [
    # --- Série 1 : Fatḥah + Fatḥah (A - A) ---
    ("sada", "صَدَ", "صَ دَ", "Ṣa-Da", "Ṣād emphatique"),
    ("tala", "طَلَ", "طَ لَ", "Ṭa-La", "Ṭā' emphatique"),
    ("ghafa", "غَفَ", "غَ فَ", "Gha-Fa", "Ghayn emphatique"),
    ("khala", "خَلَ", "خَ لَ", "Kha-La", "Khā' emphatique"),
    ("bata", "بَتَ", "بَ تَ", "Ba-Ta", "Syllabes A + A"),
    ("dara", "دَرَ", "دَ رَ", "Da-Ra", "Syllabes A + A"),
    ("kata", "كَتَ", "كَ تَ", "Ka-Ta", "Syllabes A + A"),
    ("sama", "سَمَ", "سَ مَ", "Sa-Ma", "Syllabes A + A"),
    ("rasa", "رَسَ", "رَ سَ", "Ra-Sa", "Syllabes A + A"),
    ("maa_particle", "مَعَ", "مَ عَ", "Ma-ʿA", "Avec"),
    ("laka", "لَكَ", "لَ كَ", "La-Ka", "Pour toi"),

    # --- Série 2 : Fatḥah + Ḍammah (A - OU) ---
    ("daru_emph", "ضَرُ", "ضَ رُ", "Ḍa-Rou", "Ḍād emphatique"),
    ("zhafu", "ظَفُ", "ظَ فُ", "Ẓa-Fou", "Ẓā' emphatique"),
    ("qatu", "قَتُ", "قَ تُ", "Qa-Tou", "Qāf emphatique"),
    ("hasu", "حَسُ", "حَ سُ", "Ḥa-Sou", "Ḥā' de la gorge"),
    ("babu", "بَبُ", "بَ بُ", "Ba-Bou", "Syllabes A + OU"),
    ("katu", "كَتُ", "كَ تُ", "Ka-Tou", "Syllabes A + OU"),
    ("daru", "دَرُ", "دَ رُ", "Da-Rou", "Syllabes A + OU"),
    ("samu", "سَمُ", "سَ مُ", "Sa-Mou", "Syllabes A + OU"),
    ("nabu", "نَبُ", "نَ بُ", "Na-Bou", "Syllabes A + OU"),
    ("tadu", "تَدُ", "تَ دُ", "Ta-Dou", "Syllabes A + OU"),

    # --- Série 3 : Fatḥah + Kasrah (A - I) ---
    ("sahi", "صَحِ", "صَ حِ", "Ṣa-Ḥi", "Ṣād emphatique + Ḥā'"),
    ("tafi", "طَفِ", "طَ فِ", "Ṭa-Fi", "Ṭā' emphatique"),
    ("ghani", "غَنِ", "غَ نِ", "Gha-Ni", "Ghayn emphatique"),
    ("khashi", "خَشِ", "خَ شِ", "Kha-Shi", "Khā' emphatique + Shīn"),
    ("ali_short", "عَلِ", "عَ لِ", "ʿA-Li", "ʿAyn de la gorge"),
    ("jali", "جَلِ", "جَ لِ", "Ja-Li", "Jeem"),
    ("dhari", "ذَرِ", "ذَ رِ", "Dha-Ri", "Dhāl"),
    ("zami", "زَمِ", "زَ مِ", "Za-Mi", "Zāy"),
    ("bari", "بَرِ", "بَ رِ", "Ba-Ri", "Syllabes A + I"),
    ("dari", "دَرِ", "دَ رِ", "Da-Ri", "Syllabes A + I"),
    ("sami_short", "سَمِ", "سَ مِ", "Sa-Mi", "Syllabes A + I"),
    ("kati", "كَتِ", "كَ تِ", "Ka-Ti", "Syllabes A + I"),

    # --- Série 4 : Ḍammah + Kasrah (OU - I) ---
    ("suri_emph", "صُرِ", "صُ رِ", "Ṣou-Ri", "Ṣād emphatique"),
    ("duri_emph", "ضُرِ", "ضُ رِ", "Ḍou-Ri", "Ḍād emphatique"),
    ("tubi", "طُبِ", "طُ بِ", "Ṭou-Bi", "Ṭā' emphatique"),
    ("zhuli", "ظُلِ", "ظُ لِ", "Ẓou-Li", "Ẓā' emphatique"),
    ("quri", "قُرِ", "قُ رِ", "Qou-Ri", "Qāf emphatique"),
    ("ghufi", "غُفِ", "غُ فِ", "Ghou-Fi", "Ghayn emphatique"),
    ("khuli", "خُلِ", "خُ لِ", "Khou-Li", "Khā' emphatique"),
    ("humi", "حُمِ", "حُ مِ", "Ḥou-Mi", "Ḥā' de la gorge"),
    ("thubi", "ثُبِ", "ثُ بِ", "Thou-Bi", "Thā'"),
    ("kuti", "كُتِ", "كُ تِ", "Kou-Ti", "Syllabes OU + I"),
    ("sumi", "سُمِ", "سُ مِ", "Sou-Mi", "Syllabes OU + I"),
    ("duri", "دُرِ", "دُ رِ", "Dou-Ri", "Syllabes OU + I"),
    ("rusi", "رُسِ", "رُ سِ", "Rou-Si", "Syllabes OU + I"),

    # --- Série 5 : Ḍammah + Fatḥah (OU - A) ---
    ("huwa", "هُوَ", "هُ وَ", "Hou-Wa", "Il (pronom)"),
    ("ruba", "رُبَ", "رُ بَ", "Rou-Ba", "Peut-être"),
    ("kuta", "كُتَ", "كُ تَ", "Kou-Ta", "Syllabes OU + A"),
    ("dura", "دُرَ", "دُ رَ", "Dou-Ra", "Syllabes OU + A"),
    ("sura", "سُرَ", "سُ رَ", "Sou-Ra", "Syllabes OU + A"),

    # --- Série 6 : Kasrah + Fatḥah (I - A) ---
    ("tiba", "طِبَ", "طِ بَ", "Ṭi-Ba", "Ṭā' emphatique"),
    ("zhima", "ظِمَ", "ظِ مَ", "Ẓi-Ma", "Ẓā' emphatique"),
    ("sifa", "صِفَ", "صِ فَ", "Ṣi-Fa", "Ṣād emphatique"),
    ("dia", "ضِعَ", "ضِ عَ", "Ḍi-ʿA", "Ḍād emphatique + ʿAyn"),
    ("qifa", "قِفَ", "قِ فَ", "Qi-Fa", "Qāf emphatique"),
    ("ghila", "غِلَ", "غِ لَ", "Ghi-La", "Ghayn emphatique"),
    ("khifa", "خِفَ", "خِ فَ", "Khi-Fa", "Khā' emphatique"),
    ("hiya", "هِيَ", "هِ يَ", "Hi-Ya", "Elle (pronom)"),
    ("lima", "لِمَ", "لِ مَ", "Li-Ma", "Pourquoi"),
    ("bika", "بِكَ", "بِ كَ", "Bi-Ka", "Par toi"),
    ("bita", "بِتَ", "بِ تَ", "Bi-Ta", "Syllabes I + A"),
    ("dina", "دِنَ", "دِ نَ", "Di-Na", "Syllabes I + A"),
    ("sima", "سِمَ", "سِ مَ", "Si-Ma", "Syllabes I + A"),
]

TEMP_DIR = "scripts/temp_audio/two_vowels"
TARGET_DIR = "assets/audio/generated"

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(TARGET_DIR, exist_ok=True)

async def generate_all():
    print(f"Generating {len(ALL_TWO_VOWEL_WORDS)} 2-letter 2-vowel audio files with all 28 letters + emphatics...")
    
    for key, display, spoken, trans, desc in ALL_TWO_VOWEL_WORDS:
        raw_path = os.path.join(TEMP_DIR, f"{key}_raw.mp3")
        target_path = os.path.join(TARGET_DIR, f"{key}.mp3")
        
        communicate = edge_tts.Communicate(spoken, "ar-SA-HamedNeural", rate="-5%")
        await communicate.save(raw_path)
        
        cmd = [
            "ffmpeg", "-y",
            "-i", raw_path,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,areverse,loudnorm=I=-16:TP=-1.5:LRA=7",
            "-ar", "44100",
            "-b:a", "128k",
            target_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[OK] {key}")

if __name__ == "__main__":
    asyncio.run(generate_all())
    print("All audio files for all 28 letters + emphatics generated successfully!")

