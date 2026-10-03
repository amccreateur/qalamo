import asyncio
import edge_tts
import os
import subprocess
import shutil

emphatic_kasra_letters = [
    {
        "char": "طِ",
        "name": "Taa (Taa Kasra)",
        "text": "طِي",
        "filenames": ["ttaa_kasra.mp3"]
    },
    {
        "char": "صِ",
        "name": "Saad (Sad Kasra)",
        "text": "صِي",
        "filenames": ["sad_kasra.mp3"]
    },
    {
        "char": "ضِ",
        "name": "Daad (Dad Kasra)",
        "text": "ضِي",
        "filenames": ["dad_kasra.mp3"]
    },
    {
        "char": "ظِ",
        "name": "Zhaa (Zha Kasra)",
        "text": "ظِي",
        "filenames": ["zha_kasra.mp3"]
    },
    {
        "char": "قِ",
        "name": "Qaf (Qaf Kasra)",
        "text": "قِي",
        "filenames": ["qaf_kasra.mp3"]
    },
    {
        "char": "خِ",
        "name": "Khaa (Kha Kasra)",
        "text": "خِي",
        "filenames": ["kha_kasra.mp3", "khi_kasra.mp3"]
    },
    {
        "char": "غِ",
        "name": "Ghayn (Ghayn Kasra)",
        "text": "غِي",
        "filenames": ["ghayn_kasra.mp3"]
    }
]

VOICE = "ar-EG-ShakirNeural"
RATE = "-15%"
OUTPUT_DIR = "assets/audio/generated"
TEMP_DIR = "scripts/temp_audio"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_all_emphatic_kasra():
    for item in emphatic_kasra_letters:
        primary_name = item["filenames"][0]
        temp_raw = os.path.join(TEMP_DIR, f"{primary_name}_raw.mp3")
        temp_clean = os.path.join(TEMP_DIR, primary_name)
        
        print(f"Synthesizing {item['name']} with {VOICE} at {RATE}...")
        communicate = edge_tts.Communicate(item["text"], VOICE, rate=RATE)
        await communicate.save(temp_raw)
        
        # ffmpeg silence remove & 6dB boost
        cmd = [
            "ffmpeg", "-y", "-i", temp_raw,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=6dB",
            temp_clean
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        # Copy to destination files in assets/audio/generated
        for fn in item["filenames"]:
            dst = os.path.join(OUTPUT_DIR, fn)
            shutil.copy2(temp_clean, dst)
            print(f"  -> Saved {dst}")

if __name__ == "__main__":
    asyncio.run(generate_all_emphatic_kasra())
    print("\nAll 7 emphatic letters with Kasrah generated successfully!")
