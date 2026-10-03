import os
import base64
import subprocess

kasra_list = [
    ("alif_kasra", "إِ (Alif Kasra)"),
    ("ba_kasra", "بِ (Ba Kasra)"),
    ("ta_kasra", "تِ (Ta Kasra)"),
    ("tha_kasra", "ثِ (Tha Kasra)"),
    ("jeem_kasra", "جِ (Jeem Kasra)"),
    ("hha_kasra", "حِ (Ḥa Kasra)"),
    ("kha_kasra", "خِ (Kha Kasra)"),
    ("dal_kasra", "دِ (Dal Kasra)"),
    ("dhal_kasra", "ذِ (Dhal Kasra)"),
    ("ra_kasra", "رِ (Ra Kasra)"),
    ("zay_kasra", "زِ (Zay Kasra)"),
    ("seen_kasra", "سِ (Seen Kasra)"),
    ("sheen_kasra", "شِ (Sheen Kasra)"),
    ("sad_kasra", "صِ (Ṣad Kasra)"),
    ("dad_kasra", "ضِ (Ḍad Kasra)"),
    ("ttaa_kasra", "طِ (Ṭa Kasra)"),
    ("zha_kasra", "ظِ (Ẓa Kasra)"),
    ("ayn_kasra", "عِ (ʿAyn Kasra)"),
    ("ghayn_kasra", "غِ (Ghayn Kasra)"),
    ("fa_kasra", "فِ (Fa Kasra)"),
    ("qaf_kasra", "قِ (Qaf Kasra)"),
    ("kaf_kasra", "كِ (Kaf Kasra)"),
    ("lam_kasra", "لِ (Lam Kasra)"),
    ("meem_kasra", "مِ (Meem Kasra)"),
    ("noon_kasra", "نِ (Noon Kasra)"),
    ("haa_kasra", "هِ (Haa Kasra)"),
    ("waw_kasra", "وِ (Waw Kasra)"),
    ("yaa_kasra", "يِ (Yaa Kasra)"),
]

html = """<!DOCTYPE html><html><head><meta charset="utf-8"><title>Audit Kasrah Audio</title>
<style>
body{font-family:sans-serif;padding:20px;background:#0f172a;color:#fff;}
.grid{display:grid;grid-template-columns:repeat(auto-fill, minmax(280px, 1fr));gap:15px;}
.card{background:#1e293b;padding:15px;border-radius:12px;border:1px solid #334155;}
h3{margin:0 0 10px 0;font-size:16px;}
audio{width:100%;margin-top:6px;}
</style></head><body><h1>🔊 Audit des 28 Sons Kasrah (ـِ)</h1><div class="grid">"""

for key, label in kasra_list:
    path = f"assets/audio/generated/{key}.mp3"
    if os.path.exists(path):
        with open(path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
        html += f"""<div class="card">
            <h3>{label}</h3>
            <audio controls src="data:audio/mp3;base64,{b64}"></audio>
        </div>"""
    else:
        html += f"""<div class="card" style="border-color:#ef4444;">
            <h3>{label} (MANQUANT)</h3>
        </div>"""

html += "</div></body></html>"
with open("test_all_kasra.html", "w", encoding="utf-8") as f:
    f.write(html)
print("test_all_kasra.html written successfully.")
