import asyncio
import edge_tts
import subprocess
import os

async def generate_jeem():
    voice = "ar-SA-HamedNeural"
    items = [
        ("jeem_fatha.mp3", "جَ"),
        ("jeem_damma.mp3", "جُ"),
        ("jeem_kasra.mp3", "جِ"),
        ("ju_damma.mp3", "جُ"),
        ("ji_kasra.mp3", "جِ"),
        ("ja_fatha.mp3", "جَ"),
    ]
    
    for filename, text in items:
        raw = f"raw_{filename}"
        tts = edge_tts.Communicate(text, voice, rate="-10%")
        await tts.save(raw)
        dest = f"assets/audio/generated/{filename}"
        subprocess.run([
            "ffmpeg", "-y", "-i", raw,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=6dB,alimiter=limit=0.95",
            dest
        ], capture_output=True)
        if os.path.exists(raw):
            os.remove(raw)
        print(f"Generated {dest} ({os.path.getsize(dest)} bytes)")

if __name__ == "__main__":
    asyncio.run(generate_jeem())
