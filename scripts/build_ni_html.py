import base64
import os

clips = [
    ("Hamed - نِ (Loud + Clear)", "test_ni_hamed.mp3"),
    ("Shakir - نِ (Loud + Clear)", "test_ni_shakir.mp3"),
    ("Original - assets/noon_kasra.mp3", "assets/audio/generated/noon_kasra.mp3"),
]

html = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Test Ni (نِ)</title>
<style>body{font-family:sans-serif;padding:20px;background:#0f172a;color:#fff;}
.card{background:#1e293b;padding:15px;margin:10px 0;border-radius:12px;border:1px solid #334155;}
audio{margin-top:8px;}
</style></head><body><h1>🔊 Test Son Ni (نِ - Kasrah)</h1>"""

for label, path in clips:
    if os.path.exists(path):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        html += f"""<div class="card">
            <h3>{label}</h3>
            <audio controls src="data:audio/mp3;base64,{b64}"></audio>
        </div>"""

html += "</body></html>"
with open("test_ni_audio.html", "w", encoding="utf-8") as f:
    f.write(html)
print("HTML generated at test_ni_audio.html")
