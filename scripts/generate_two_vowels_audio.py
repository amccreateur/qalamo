import asyncio
import os
import subprocess
import edge_tts

# Words list: (key, arabic_text, transcription, translation_or_desc)
TWO_VOWEL_WORDS = [
    # Série 1: Fatḥah + Fatḥah (A - A)
    ("bata", "بَتَ", "Ba-Ta", "Syllabes A + A"),
    ("dara", "دَرَ", "Da-Ra", "Syllabes A + A"),
    ("kata", "كَتَ", "Ka-Ta", "Syllabes A + A"),
    ("sama", "سَمَ", "Sa-Ma", "Syllabes A + A"),
    ("rasa", "رَسَ", "Ra-Sa", "Syllabes A + A"),
    ("maa_particle", "مَعَ", "Ma-ʿa", "Avec (mot réel)"),
    ("laka", "لَكَ", "La-Ka", "À toi (mot réel)"),

    # Série 2: Fatḥah + Ḍammah (A - OU)
    ("babu", "بَبُ", "Ba-Bou", "Syllabes A + OU"),
    ("katu", "كَتُ", "Ka-Tou", "Syllabes A + OU"),
    ("daru", "دَرُ", "Da-Rou", "Syllabes A + OU"),
    ("samu", "سَمُ", "Sa-Mou", "Syllabes A + OU"),
    ("qatu", "قَتُ", "Qa-Tou", "Syllabes A + OU"),
    ("nabu", "نَبُ", "Na-Bou", "Syllabes A + OU"),
    ("tadu", "تَدُ", "Ta-Dou", "Syllabes A + OU"),

    # Série 3: Fatḥah + Kasrah (A - I)
    ("bari", "بَرِ", "Ba-Ri", "Syllabes A + I"),
    ("dari", "دَرِ", "Da-Ri", "Syllabes A + I"),
    ("sami_short", "سَمِ", "Sa-Mi", "Syllabes A + I"),
    ("kati", "كَتِ", "Ka-Ti", "Syllabes A + I"),
    ("shari_short", "شَرِ", "Sha-Ri", "Syllabes A + I"),
    ("ali_short", "عَلِ", "ʿA-Li", "Syllabes A + I"),

    # Série 4: Ḍammah + Kasrah (OU - I)
    ("kuti", "كُتِ", "Kou-Ti", "Syllabes OU + I"),
    ("quri", "قُرِ", "Qou-Ri", "Syllabes OU + I"),
    ("sumi", "سُمِ", "Sou-Mi", "Syllabes OU + I"),
    ("duri", "دُرِ", "Dou-Ri", "Syllabes OU + I"),
    ("rusi", "رُسِ", "Rou-Si", "Syllabes OU + I"),

    # Série 5: Ḍammah + Fatḥah (OU - A)
    ("huwa", "هُوَ", "Hou-Wa", "Lui (mot réel)"),
    ("ruba", "رُبَ", "Rou-Ba", "Peut-être (mot réel)"),
    ("kuta", "كُتَ", "Kou-Ta", "Syllabes OU + A"),
    ("dura", "دُرَ", "Dou-Ra", "Syllabes OU + A"),
    ("sura", "سُرَ", "Sou-Ra", "Syllabes OU + A"),

    # Série 6: Kasrah + Fatḥah (I - A)
    ("hiya", "هِيَ", "Hi-Ya", "Elle (mot réel)"),
    ("lima", "لِمَ", "Li-Ma", "Pourquoi (mot réel)"),
    ("bika", "بِكَ", "Bi-Ka", "Par toi (mot réel)"),
    ("bita", "بِتَ", "Bi-Ta", "Syllabes I + A"),
    ("dina", "دِنَ", "Di-Na", "Syllabes I + A"),
    ("sima", "سِمَ", "Si-Ma", "Syllabes I + A"),
]

TEMP_DIR = "scripts/temp_audio/two_vowels"
TARGET_DIR = "assets/audio/generated"

os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(TARGET_DIR, exist_ok=True)

async def generate_all():
    print(f"Generating {len(TWO_VOWEL_WORDS)} 2-letter 2-vowel audio files...")
    
    for key, text, trans, desc in TWO_VOWEL_WORDS:
        raw_path = os.path.join(TEMP_DIR, f"{key}_raw.mp3")
        target_path = os.path.join(TARGET_DIR, f"{key}.mp3")
        
        # We use ar-SA-HamedNeural for crystal clear short syllables
        # SSML with clear pronunciation and natural pace
        ssml = f"""<speak version='1.0' xmlns='http://www.w3.org/2001/10/synthesis' xml:lang='ar-SA'>
            <voice name='ar-SA-HamedNeural'>
                <prosody rate='-8%' pitch='+0Hz'>{text}</prosody>
            </voice>
        </speak>"""
        
        communicate = edge_tts.Communicate(text, "ar-SA-HamedNeural", rate="-8%")
        await communicate.save(raw_path)
        
        # Normalize and pad slightly with ffmpeg
        cmd = [
            "ffmpeg", "-y",
            "-i", raw_path,
            "-af", "apad=pad_dur=0.08,loudnorm=I=-16:TP=-1.5:LRA=11",
            target_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        print(f"[OK] {key}")

if __name__ == "__main__":
    asyncio.run(generate_all())
    print("All 2-vowel audio files successfully generated and normalized!")
