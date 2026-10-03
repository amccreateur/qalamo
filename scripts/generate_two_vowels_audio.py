import asyncio
import os
import subprocess
import edge_tts

# Words list: (key, arabic_display, arabic_spoken_syllabic, transcription, desc)
TWO_VOWEL_WORDS = [
    # Série 1: Fatḥah + Fatḥah (A - A)
    ("bata", "بَتَ", "بَ تَ", "Ba-Ta", "Syllabes A + A"),
    ("dara", "دَرَ", "دَ رَ", "Da-Ra", "Syllabes A + A"),
    ("kata", "كَتَ", "كَ تَ", "Ka-Ta", "Syllabes A + A"),
    ("sama", "سَمَ", "سَ مَ", "Sa-Ma", "Syllabes A + A"),
    ("rasa", "رَسَ", "رَ سَ", "Ra-Sa", "Syllabes A + A"),
    ("maa_particle", "مَعَ", "مَ عَ", "Ma-ʿa", "Avec (mot réel)"),
    ("laka", "لَكَ", "لَ كَ", "La-Ka", "À toi (mot réel)"),

    # Série 2: Fatḥah + Ḍammah (A - OU)
    ("babu", "بَبُ", "بَ بُ", "Ba-Bou", "Syllabes A + OU"),
    ("katu", "كَتُ", "كَ تُ", "Ka-Tou", "Syllabes A + OU"),
    ("daru", "دَرُ", "دَ رُ", "Da-Rou", "Syllabes A + OU"),
    ("samu", "سَمُ", "سَ مُ", "Sa-Mou", "Syllabes A + OU"),
    ("qatu", "قَتُ", "قَ تُ", "Qa-Tou", "Syllabes A + OU"),
    ("nabu", "نَبُ", "نَ بُ", "Na-Bou", "Syllabes A + OU"),
    ("tadu", "تَدُ", "تَ دُ", "Ta-Dou", "Syllabes A + OU"),

    # Série 3: Fatḥah + Kasrah (A - I)
    ("bari", "بَرِ", "بَ رِ", "Ba-Ri", "Syllabes A + I"),
    ("dari", "دَرِ", "دَ رِ", "Da-Ri", "Syllabes A + I"),
    ("sami_short", "سَمِ", "سَ مِ", "Sa-Mi", "Syllabes A + I"),
    ("kati", "كَتِ", "كَ تِ", "Ka-Ti", "Syllabes A + I"),
    ("shari_short", "شَرِ", "شَ رِ", "Sha-Ri", "Syllabes A + I"),
    ("ali_short", "عَلِ", "عَ لِ", "ʿA-Li", "Syllabes A + I"),

    # Série 4: Ḍammah + Kasrah (OU - I)
    ("kuti", "كُتِ", "كُ تِ", "Kou-Ti", "Syllabes OU + I"),
    ("quri", "قُرِ", "قُ رِ", "Qou-Ri", "Syllabes OU + I"),
    ("sumi", "سُمِ", "سُ مِ", "Sou-Mi", "Syllabes OU + I"),
    ("duri", "دُرِ", "دُ رِ", "Dou-Ri", "Syllabes OU + I"),
    ("rusi", "رُسِ", "رُ سِ", "Rou-Si", "Syllabes OU + I"),

    # Série 5: Ḍammah + Fatḥah (OU - A)
    ("huwa", "هُوَ", "هُ وَ", "Hou-Wa", "Lui (mot réel)"),
    ("ruba", "رُبَ", "رُ بَ", "Rou-Ba", "Peut-être (mot réel)"),
    ("kuta", "كُتَ", "كُ تَ", "Kou-Ta", "Syllabes OU + A"),
    ("dura", "دُرَ", "دُ رَ", "Dou-Ra", "Syllabes OU + A"),
    ("sura", "سُرَ", "سُ رَ", "Sou-Ra", "Syllabes OU + A"),

    # Série 6: Kasrah + Fatḥah (I - A)
    ("hiya", "هِيَ", "هِ يَ", "Hi-Ya", "Elle (mot réel)"),
    ("lima", "لِمَ", "لِ مَ", "Li-Ma", "Pourquoi (mot réel)"),
    ("bika", "بِكَ", "بِ كَ", "Bi-Ka", "Par toi (mot réel)"),
    ("bita", "بِتَ", "بِ تَ", "Bi-Ta", "Syllabes I + A"),
    ("dina", "دِنَ", "دِ نَ", "Di-Na", "Syllabes I + A"),
    ("sima", "سِمَ", "سِ مَ", "Si-Ma", "Syllabes I + A"),
]

TEMP_DIR = "scripts/temp_audio/two_vowels"
TARGET_DIR = "assets/audio/generated"

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(TARGET_DIR, exist_ok=True)

async def generate_all():
    print(f"Generating {len(TWO_VOWEL_WORDS)} 2-letter 2-vowel audio files with Hamed (Syllabé)...")
    
    for key, display, spoken, trans, desc in TWO_VOWEL_WORDS:
        raw_path = os.path.join(TEMP_DIR, f"{key}_raw.mp3")
        target_path = os.path.join(TARGET_DIR, f"{key}.mp3")
        
        # ar-SA-HamedNeural with syllabic spacing to prevent Waqf on final vowel
        communicate = edge_tts.Communicate(spoken, "ar-SA-HamedNeural", rate="-5%")
        await communicate.save(raw_path)
        
        # Clean silence and normalize with loudnorm
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
    print("All 36 2-vowel audio files successfully regenerated with Hamed (Syllabe)!")
