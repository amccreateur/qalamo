import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "fahed_qaf_court_15",
        "title": "Fahed (Golfe) — Claquant & Percutant (-15%) ⭐ Recommandé",
        "voice": "ar-KW-FahedNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Claquement uvulaire très fort et franc, impossible à confondre avec le K"
    },
    {
        "id": "fahed_qaf_long_15",
        "title": "Fahed (Golfe) — Soutenu & Profond (-15%) ⭐",
        "voice": "ar-KW-FahedNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Qaf uvulaire profond avec voyelle bien marquée"
    },
    {
        "id": "hamed_qaf_court_15",
        "title": "Hamed — Saoudien Net & Grave (-15%)",
        "voice": "ar-SA-HamedNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Attaque uvulaire pure et sèche classique"
    },
    {
        "id": "hamed_qaf_long_15",
        "title": "Hamed — Saoudien Posé (-15%)",
        "voice": "ar-SA-HamedNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Format plus posé et soutenu"
    },
    {
        "id": "saleh_qaf_15",
        "title": "Saleh (Yémen) — Tajweed Authentique (-15%)",
        "voice": "ar-YE-SalehNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Articulé au fond du palais dans la tradition yéménite"
    },
    {
        "id": "bassel_qaf_15",
        "title": "Bassel (Irak) — Profond & Net (-15%)",
        "voice": "ar-IQ-BasselNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Timbre irakien avec Qaf très appuyé"
    },
    {
        "id": "zariyah_qaf_15",
        "title": "Zariyah (Féminin) — Tranchant & Net (-15%)",
        "voice": "ar-SA-ZariyahNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Attaque féminine très vive et distincte"
    }
]

TEMP_DIR = "scripts/temp_audio/deep_qaf_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_deep_qaf():
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
        
    qaf_box = f'''    <!-- SECTION SPECIAL CHOIX DU SON QAF PROFOND -->
    <div class="highlight-box" style="border-color:#f59e0b; background:#78350f22;">
      <div class="highlight-title" style="color:#fbbf24;">🎯 Choix du son « Qi » (قِ — Qāf Uvulaire Profond & Claquant)</div>
      <p class="highlight-desc">Voici les versions avec un vrai claquement uvulaire profond au fond de la gorge, pour une distinction absolue avec <strong>كِ (Ki)</strong> :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION QAF PROFOND -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL CHOIX DU SON QAF PROFOND -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON QAF PROFOND -->.*?<!-- /SECTION QAF PROFOND -->', qaf_box, content, flags=re.DOTALL)
    elif '<!-- SECTION SPECIAL CHOIX DU SON KI FINAL -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON KI FINAL -->.*?<!-- /SECTION KI FINAL -->', qaf_box, content, flags=re.DOTALL)
    else:
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + qaf_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with deep Qaf candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_deep_qaf())
    update_html(res)
