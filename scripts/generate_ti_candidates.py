import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "hamed_ti_long_20",
        "title": "Hamed — Posé & Emphatique (-20%) ⭐",
        "voice": "ar-SA-HamedNeural",
        "text": "طِي",
        "rate": "-20%"
    },
    {
        "id": "shakir_ti_clear_15",
        "title": "Shakir — Net & Articulé (-15%) ⭐",
        "voice": "ar-EG-ShakirNeural",
        "text": "طِي",
        "rate": "-15%"
    },
    {
        "id": "shakir_ti_long_25",
        "title": "Shakir — Bien Soutenu (-25%)",
        "voice": "ar-EG-ShakirNeural",
        "text": "طِي",
        "rate": "-25%"
    },
    {
        "id": "hamed_ti_short_15",
        "title": "Hamed — Bref & Grave (-15%)",
        "voice": "ar-SA-HamedNeural",
        "text": "طِ",
        "rate": "-15%"
    },
    {
        "id": "shakir_ti_short_15",
        "title": "Shakir — Naturel court (-15%)",
        "voice": "ar-EG-ShakirNeural",
        "text": "طِ",
        "rate": "-15%"
    },
    {
        "id": "fahed_ti_15",
        "title": "Fahed (Golfe) — Profond (-15%)",
        "voice": "ar-KW-FahedNeural",
        "text": "طِي",
        "rate": "-15%"
    },
    {
        "id": "zariyah_ti_15",
        "title": "Zariyah (Féminin) — Clair (-15%)",
        "voice": "ar-SA-ZariyahNeural",
        "text": "طِي",
        "rate": "-15%"
    }
]

os.makedirs("scripts/temp_audio", exist_ok=True)

async def generate_all():
    results = []
    for c in candidates:
        raw_path = f"scripts/temp_audio/{c['id']}_raw.mp3"
        clean_path = f"scripts/temp_audio/{c['id']}.mp3"
        
        communicate = edge_tts.Communicate(c["text"], c["voice"], rate=c["rate"])
        await communicate.save(raw_path)
        
        # Process with ffmpeg: trim silence, amplify
        cmd = [
            "ffmpeg", "-y", "-i", raw_path,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=6dB",
            clean_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with open(clean_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        
        results.append({
            "id": c["id"],
            "title": c["title"],
            "b64": b64
        })
        print(f"Generated {c['id']}")
    return results

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(generate_all())
    
    # Print HTML cards snippet
    print("\n--- HTML SNIPPET ---\n")
    for r in res:
        print(f'''        <div class="card" style="border-color:#f59e0b;">
          <div class="ar-word">طِ</div>
          <div class="phonetic" style="color:#fcd34d;">{r['title']}</div>
          <button class="play-btn" style="background:#d97706;" onclick="playAudio('data:audio/mp3;base64,{r['b64']}', this)">🔊 Écouter</button>
        </div>''')
