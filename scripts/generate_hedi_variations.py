import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "hedi_qaf_clean_10",
        "title": "Hedi — Punchy & Ferme (-10%) ⭐",
        "voice": "ar-TN-HediNeural",
        "text": "قِ",
        "rate": "-10%",
        "desc": "Attaque ferme et claquante, cadence dynamique"
    },
    {
        "id": "hedi_qaf_pose_20",
        "title": "Hedi — Plus Posé (-20%) ⭐⭐",
        "voice": "ar-TN-HediNeural",
        "text": "قِ",
        "rate": "-20%",
        "desc": "Même fermeté, mais ralenti de 20% pour donner plus de corps au son"
    },
    {
        "id": "hedi_qaf_soutenu_25",
        "title": "Hedi — Bien Soutenu (-25%)",
        "voice": "ar-TN-HediNeural",
        "text": "قِ",
        "rate": "-25%",
        "desc": "Cadence lente d'apprentissage, voyelle bien audible"
    },
    {
        "id": "hedi_qaf_ya_15",
        "title": "Hedi — Voyelle Tenue (-15%) ⭐",
        "voice": "ar-TN-HediNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Attaque ferme de Hedi avec voyelle 'i' un peu plus longue"
    },
    {
        "id": "hedi_qaf_ya_20",
        "title": "Hedi — Voyelle Tenue & Posée (-20%)",
        "voice": "ar-TN-HediNeural",
        "text": "قِي",
        "rate": "-20%",
        "desc": "Format long avec voyelle pleine"
    },
    {
        "id": "jamal_morocco_qaf_15",
        "title": "Jamal (Maroc) — Ferme & Traditionnel (-15%)",
        "voice": "ar-MA-JamalNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Attaque ferme maghrébine avec timbre chaleureux"
    },
    {
        "id": "reem_tunisia_qaf_15",
        "title": "Reem (Tunisie Féminin) — Ciselé & Net (-15%)",
        "voice": "ar-TN-ReemNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Version féminine tunisienne très précise"
    }
]

TEMP_DIR = "scripts/temp_audio/hedi_qaf_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_hedi_qaf():
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
    colors = ["#22c55e", "#3b82f6", "#f59e0b", "#a855f7", "#06b6d4", "#ec4899", "#e11d48"]
    btn_bgs = ["#16a34a", "#2563eb", "#d97706", "#9333ea", "#0891b2", "#db2777", "#be123c"]
    
    for idx, r in enumerate(res):
        c_border = colors[idx % len(colors)]
        c_btn = btn_bgs[idx % len(btn_bgs)]
        cards.append(f'''        <div class="card" style="border-color:{c_border};">
          <div class="ar-word">قِ</div>
          <div class="phonetic" style="color:#fcd34d;">{r['title']}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{r['desc']}</p>
          <button class="play-btn" style="background:{c_btn};" onclick="playAudio('data:audio/mp3;base64,{r['b64']}', this)">🔊 Écouter</button>
        </div>''')
        
    qaf_box = f'''    <!-- SECTION SPECIAL AMELIORATIONS HEDI QAF -->
    <div class="highlight-box" style="border-color:#22c55e; background:#064e3b22;">
      <div class="highlight-title" style="color:#4ade80;">🎯 Améliorations de « Hedi » (قِ — Attaque Ferme & Précise)</div>
      <p class="highlight-desc">Voici les déclinaisons optimisées basées sur le timbre ferme de <strong>Hedi</strong> (différents tempos et tenues de voyelle) :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION AMELIORATIONS HEDI QAF -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL AMELIORATIONS HEDI QAF -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL AMELIORATIONS HEDI QAF -->.*?<!-- /SECTION AMELIORATIONS HEDI QAF -->', qaf_box, content, flags=re.DOTALL)
    elif '<!-- SECTION SPECIAL NOUVELLES PROPOSITIONS QAF -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL NOUVELLES PROPOSITIONS QAF -->.*?<!-- /SECTION NOUVELLES PROPOSITIONS QAF -->', qaf_box, content, flags=re.DOTALL)
    else:
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + qaf_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with Hedi optimized Qaf candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_hedi_qaf())
    update_html(res)
