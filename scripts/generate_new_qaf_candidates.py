import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "abdullah_oman_qaf_15",
        "title": "Abdullah (Oman) — Fusha Classique Pur (-15%) ⭐",
        "voice": "ar-OM-AbdullahNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Prononciation omanaise de référence, Qaf classique très pur et posé"
    },
    {
        "id": "ali_bahrain_qaf_15",
        "title": "Ali (Bahreïn) — Net & Distinct (-15%) ⭐",
        "voice": "ar-BH-AliNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Timbre du Golfe très soigné avec Qaf franc"
    },
    {
        "id": "laith_syria_qaf_15",
        "title": "Laith (Syrie) — Fusha Élégant (-15%)",
        "voice": "ar-SY-LaithNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Prononciation shamie classique très équilibrée"
    },
    {
        "id": "taim_jordan_qaf_15",
        "title": "Taim (Jordanie) — Clair & Posé (-15%)",
        "voice": "ar-JO-TaimNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Timbre jordanien avec articulation soignée"
    },
    {
        "id": "ismael_algeria_qaf_15",
        "title": "Ismaël (Algérie) — Posé & Profond (-15%)",
        "voice": "ar-DZ-IsmaelNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Qaf maghrébin classique bien résonnant"
    },
    {
        "id": "hedi_tunisia_qaf_15",
        "title": "Hedi (Tunisie) — Ferme & Net (-15%)",
        "voice": "ar-TN-HediNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Attaque ferme et précise"
    },
    {
        "id": "omar_libya_qaf_15",
        "title": "Omar (Libye) — Traditionnel & Fort (-15%)",
        "voice": "ar-LY-OmarNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Timbre libyen traditionnel"
    },
    {
        "id": "hamdan_uae_qaf_15",
        "title": "Hamdan (Émirats) — Dynamique (-15%)",
        "voice": "ar-AE-HamdanNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Prononciation émiratie moderne et claire"
    },
    {
        "id": "abdullah_oman_qaf_long_15",
        "title": "Abdullah (Oman) — Format Soutenu (-15%)",
        "voice": "ar-OM-AbdullahNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Version plus longue d'Abdullah avec voyelle étirée"
    },
    {
        "id": "ali_bahrain_qaf_long_15",
        "title": "Ali (Bahreïn) — Format Soutenu (-15%)",
        "voice": "ar-BH-AliNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Version plus longue d'Ali avec voyelle étirée"
    }
]

TEMP_DIR = "scripts/temp_audio/new_qaf_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_new_qaf():
    results = []
    for c in candidates:
        raw_path = os.path.join(TEMP_DIR, f"{c['id']}_raw.mp3")
        clean_path = os.path.join(TEMP_DIR, f"{c['id']}.mp3")
        
        communicate = edge_tts.Communicate(c["text"], c["voice"], rate=c["rate"])
        await communicate.save(raw_path)
        
        cmd = [
            "ffmpeg", "-y", "-i", raw_path,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=6dB",
            clean_path
        ]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with open(clean_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            
        results.append({**c, "b64": b64})
        print(f"Generated {c['id']}")
    return results

def update_html(res):
    cards = []
    colors = ["#22c55e", "#3b82f6", "#f59e0b", "#a855f7", "#06b6d4", "#ec4899", "#e11d48", "#10b981", "#6366f1", "#8b5cf6"]
    btn_bgs = ["#16a34a", "#2563eb", "#d97706", "#9333ea", "#0891b2", "#db2777", "#be123c", "#059669", "#4f46e5", "#7c3aed"]
    
    for idx, r in enumerate(res):
        c_border = colors[idx % len(colors)]
        c_btn = btn_bgs[idx % len(btn_bgs)]
        cards.append(f'''        <div class="card" style="border-color:{c_border};">
          <div class="ar-word">قِ</div>
          <div class="phonetic" style="color:#fcd34d;">{r['title']}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{r['desc']}</p>
          <button class="play-btn" style="background:{c_btn};" onclick="playAudio('data:audio/mp3;base64,{r['b64']}', this)">🔊 Écouter</button>
        </div>''')
        
    qaf_box = f'''    <!-- SECTION SPECIAL NOUVELLES PROPOSITIONS QAF -->
    <div class="highlight-box" style="border-color:#38bdf8; background:#0284c722;">
      <div class="highlight-title" style="color:#38bdf8;">🎯 Nouvelles Propositions Variées pour « Qi » (قِ — Qāf Kasrah)</div>
      <p class="highlight-desc">Voici 10 nouvelles voix de référence à travers le monde arabe pour trouver le Qāf parfait :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION NOUVELLES PROPOSITIONS QAF -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL NOUVELLES PROPOSITIONS QAF -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL NOUVELLES PROPOSITIONS QAF -->.*?<!-- /SECTION NOUVELLES PROPOSITIONS QAF -->', qaf_box, content, flags=re.DOTALL)
    elif '<!-- SECTION SPECIAL CHOIX DU SON QAF PROFOND -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON QAF PROFOND -->.*?<!-- /SECTION QAF PROFOND -->', qaf_box, content, flags=re.DOTALL)
    else:
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + qaf_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with 10 new Qaf candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_new_qaf())
    update_html(res)
