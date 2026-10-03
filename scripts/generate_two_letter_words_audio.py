import asyncio
import edge_tts
import os
import subprocess
import shutil

two_letter_words = [
    {"key": "ab", "text": "أَبْ", "voice": "ar-SA-HamedNeural", "file": "ab.mp3"},
    {"key": "akh", "text": "أَخْ", "voice": "ar-SA-HamedNeural", "file": "akh.mp3"},
    {"key": "yad", "text": "يَدْ", "voice": "ar-SA-HamedNeural", "file": "yad.mp3"},
    {"key": "fam", "text": "فَمْ", "voice": "ar-SA-HamedNeural", "file": "fam.mp3"},
    {"key": "dam", "text": "دَمْ", "voice": "ar-SA-HamedNeural", "file": "dam.mp3"},
    {"key": "qul", "text": "قُلْ", "voice": "ar-SA-HamedNeural", "file": "qul_sukun.mp3"},
    {"key": "kun", "text": "كُنْ", "voice": "ar-SA-HamedNeural", "file": "kun.mp3"},
    {"key": "khudh", "text": "خُذْ", "voice": "ar-SA-HamedNeural", "file": "khudh.mp3"},
    {"key": "qum", "text": "قُمْ", "voice": "ar-SA-HamedNeural", "file": "qum_sukun.mp3"},
    {"key": "min", "text": "مِنْ", "voice": "ar-SA-HamedNeural", "file": "min_sukun.mp3"},
    {"key": "qif", "text": "قِفْ", "voice": "ar-SA-HamedNeural", "file": "qif.mp3"},
    {"key": "sir", "text": "سِرْ", "voice": "ar-SA-HamedNeural", "file": "sir.mp3"},
    {"key": "zir", "text": "زِرْ", "voice": "ar-SA-HamedNeural", "file": "zir.mp3"},
    {"key": "an", "text": "عَنْ", "voice": "ar-SA-HamedNeural", "file": "an_sukun.mp3"},
    {"key": "hal", "text": "هَلْ", "voice": "ar-SA-HamedNeural", "file": "hal_sukun.mp3"},
    {"key": "bal", "text": "بَلْ", "voice": "ar-SA-HamedNeural", "file": "bal_sukun.mp3"},
    {"key": "lam", "text": "لَمْ", "voice": "ar-SA-HamedNeural", "file": "lam_word.mp3"},
    {"key": "law", "text": "لَوْ", "voice": "ar-SA-HamedNeural", "file": "law_word.mp3"},
    {"key": "qad", "text": "قَدْ", "voice": "ar-SA-HamedNeural", "file": "qad_sukun.mp3"},
]

OUTPUT_DIR = "assets/audio/generated"
TEMP_DIR = "scripts/temp_audio/two_letter_words"
os.makedirs(TEMP_DIR, exist_ok=True)
os.makedirs(OUTPUT_DIR, exist_ok=True)

async def generate_words():
    for item in two_letter_words:
        raw = os.path.join(TEMP_DIR, f"{item['key']}_raw.mp3")
        clean = os.path.join(TEMP_DIR, item['file'])
        dst = os.path.join(OUTPUT_DIR, item['file'])
        
        communicate = edge_tts.Communicate(item["text"], item["voice"], rate="-10%")
        await communicate.save(raw)
        
        cmd = [
            "ffmpeg", "-y", "-i", raw,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=5dB",
            clean
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        shutil.copy2(clean, dst)
        print(f"Generated {item['file']}")

if __name__ == "__main__":
    asyncio.run(generate_words())
    print("All 2-letter word audios generated successfully!")
