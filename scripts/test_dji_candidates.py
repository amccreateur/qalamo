import asyncio
import edge_tts
import subprocess
import os
import base64

candidates = [
    ("dji_cand1", "جِي", "ar-SA-HamedNeural"),          # Ji (Ya)
    ("dji_cand2", "جِيْ", "ar-SA-HamedNeural"),         # Ji (Ya Sukun)
    ("dji_cand3", "جِـي", "ar-SA-HamedNeural"),         # Ji (tatweel + Ya)
    ("dji_cand4", "جِـ", "ar-SA-HamedNeural"),          # Ji (tatweel only)
    ("dji_cand5", "جِي", "ar-EG-ShakirNeural"),         # Shakir Ji
    ("dji_cand6", "جِـ", "ar-EG-ShakirNeural"),         # Shakir tatweel
    ("dji_cand7", "جِي", "ar-SA-ZariyahNeural"),        # Zariyah Ji
    ("dji_cand8", "جِدْ", "ar-SA-HamedNeural"),          # Jid
]

async def gen_candidates():
    os.makedirs("test_dji", exist_ok=True)
    html = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Test Dji Candidates</title>
    <style>body{font-family:sans-serif;padding:20px;background:#0f172a;color:#fff;}
    .card{background:#1e293b;padding:15px;margin:10px 0;border-radius:12px;}
    audio{margin-top:8px;}
    </style></head><body><h1>🔊 Test Candidats pour le son "Dji" (جِ)</h1>"""
    
    for name, text, voice in candidates:
        raw = f"test_dji/raw_{name}.mp3"
        clean = f"test_dji/{name}.mp3"
        tts = edge_tts.Communicate(text, voice, rate="-10%")
        await tts.save(raw)
        subprocess.run([
            "ffmpeg", "-y", "-i", raw,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=6dB,alimiter=limit=0.95",
            clean
        ], capture_output=True)
        
        with open(clean, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        html += f"""<div class="card">
            <h3>{name} | Texte: '{text}' | Voix: {voice}</h3>
            <audio controls src="data:audio/mp3;base64,{b64}"></audio>
        </div>"""
    
    html += "</body></html>"
    with open("test_dji_candidates.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("test_dji_candidates.html generated!")

if __name__ == "__main__":
    asyncio.run(gen_candidates())
