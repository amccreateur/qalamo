import asyncio
import edge_tts
import subprocess
import os
import base64

candidates = [
    ("dji_hamed_slow20", "جِي", "ar-SA-HamedNeural", "-20%", "Hamed - Slower (-20%)"),
    ("dji_hamed_slow30", "جِي", "ar-SA-HamedNeural", "-30%", "Hamed - Extra Slow (-30%)"),
    ("dji_hamed_madd", "جِـيـ", "ar-SA-HamedNeural", "-15%", "Hamed - Prolongé (-15%)"),
    ("dji_shakir_slow15", "جِي", "ar-EG-ShakirNeural", "-15%", "Shakir - Net et Posé (-15%)"),
    ("dji_shakir_slow25", "جِي", "ar-EG-ShakirNeural", "-25%", "Shakir - Plus Long (-25%)"),
    ("dji_fahed_slow15", "جِي", "ar-KW-FahedNeural", "-15%", "Fahed - Golfe (-15%)"),
    ("dji_zariyah_slow15", "جِي", "ar-SA-ZariyahNeural", "-15%", "Zariyah (-15%)"),
]

async def make_dji_tests():
    os.makedirs("test_dji_long", exist_ok=True)
    html = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Comparatif Dji Long</title>
    <style>body{font-family:sans-serif;padding:25px;background:#0f172a;color:#fff;}
    .card{background:#1e293b;padding:16px;margin:12px 0;border-radius:14px;border:1.5px solid #334155;}
    .ar{font-family:'Amiri',serif;font-size:36px;color:#fde047;margin-bottom:4px;}
    audio{margin-top:10px;width:100%;max-width:400px;}
    </style></head><body><h1>🔊 Comparatif Dji (جِ) - Sons Plus Longs & Plus Clairs</h1>"""
    
    for name, text, voice, rate, label in candidates:
        raw = f"test_dji_long/raw_{name}.mp3"
        clean = f"test_dji_long/{name}.mp3"
        tts = edge_tts.Communicate(text, voice, rate=rate)
        await tts.save(raw)
        subprocess.run([
            "ffmpeg", "-y", "-i", raw,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=6dB,alimiter=limit=0.95",
            clean
        ], capture_output=True)
        
        with open(clean, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        html += f"""<div class="card">
            <div class="ar">جِ</div>
            <h3>{label} ({voice} / {rate})</h3>
            <audio controls src="data:audio/mp3;base64,{b64}"></audio>
        </div>"""
    
    html += "</body></html>"
    with open("test_dji_long.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("test_dji_long.html created!")

if __name__ == "__main__":
    asyncio.run(make_dji_tests())
