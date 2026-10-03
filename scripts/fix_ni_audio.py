import asyncio
import edge_tts
import os
import subprocess

async def generate_candidates():
    candidates = [
        ("ni_hamed_std", "نِ", "ar-SA-HamedNeural", "-10%"),
        ("ni_hamed_comma", "نِ،", "ar-SA-HamedNeural", "-10%"),
        ("ni_hamed_tatweel", "نِـ", "ar-SA-HamedNeural", "-10%"),
        ("ni_shakir_std", "نِ", "ar-EG-ShakirNeural", "-10%"),
        ("ni_shakir_comma", "نِ،", "ar-EG-ShakirNeural", "-10%"),
        ("ni_moaz_std", "نِ", "ar-SA-MoazNeural", "-10%"),
        ("ni_moaz_comma", "نِ،", "ar-SA-MoazNeural", "-10%"),
        ("ni_zariyah_std", "نِ", "ar-SA-ZariyahNeural", "-10%"),
    ]
    
    os.makedirs("test_ni", exist_ok=True)
    for name, text, voice, rate in candidates:
        raw_path = f"test_ni/{name}_raw.mp3"
        clean_path = f"test_ni/{name}.mp3"
        tts = edge_tts.Communicate(text, voice, rate=rate)
        await tts.save(raw_path)
        # Trim silence with ffmpeg
        subprocess.run([
            "ffmpeg", "-y", "-i", raw_path,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=2.0",
            clean_path
        ], capture_output=True)
        print(f"Generated {clean_path} ({os.path.getsize(clean_path)} bytes)")

if __name__ == "__main__":
    asyncio.run(generate_candidates())
