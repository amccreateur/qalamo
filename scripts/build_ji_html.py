import base64
import os

clips = [
    ("Hamed - جِ (ji_hamed.mp3)", "ji_hamed.mp3"),
    ("Hamed Tatweel - جِـ (ji_hamed_tatweel.mp3)", "ji_hamed_tatweel.mp3"),
    ("Fahed - جِ (ji_fahed.mp3)", "ji_fahed.mp3"),
    ("Fahed Tatweel - جِـ (ji_fahed_tatweel.mp3)", "ji_fahed_tatweel.mp3"),
    ("Shakir - جِ (ji_shakir.mp3)", "ji_shakir.mp3"),
    ("Current File in App (assets/jeem_kasra.mp3)", "assets/audio/generated/jeem_kasra.mp3"),
]

html = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Test Ji (جِ)</title>
<style>body{font-family:sans-serif;padding:20px;background:#0f172a;color:#fff;}
.card{background:#1e293b;padding:15px;margin:10px 0;border-radius:12px;border:1px solid #334155;}
audio{margin-top:8px;}
</style></head><body><h1>🔊 Test Son Ji (جِ - Kasrah)</h1>"""

for label, path in clips:
    if os.path.exists(path):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        html += f"""<div class="card">
            <h3>{label}</h3>
            <audio controls src="data:audio/mp3;base64,{b64}"></audio>
        </div>"""

html += "</body></html>"
with open("test_ji_audio.html", "w", encoding="utf-8") as f:
    f.write(html)
print("HTML generated at test_ji_audio.html")
