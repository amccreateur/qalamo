import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "hamed_qi_long_15",
        "title": "Hamed — Classique Profond (-15%) ⭐ Recommandé",
        "voice": "ar-SA-HamedNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Claquement uvulaire authentique saoudien avec voyelle bien tenue",
        "border": "#22c55e",
        "btn_bg": "#16a34a"
    },
    {
        "id": "hamed_qi_short_15",
        "title": "Hamed — Bref & Percutant (-15%)",
        "voice": "ar-SA-HamedNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Qaf pur et sec, sans allongement",
        "border": "#3b82f6",
        "btn_bg": "#2563eb"
    },
    {
        "id": "fahed_qi_long_15",
        "title": "Fahed (Golfe) — Fort & Résonnant (-15%)",
        "voice": "ar-KW-FahedNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Prononciation koweïtienne très nette et puissante",
        "border": "#f59e0b",
        "btn_bg": "#d97706"
    },
    {
        "id": "fahed_qi_short_15",
        "title": "Fahed (Golfe) — Bref Authentique (-15%)",
        "voice": "ar-KW-FahedNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Format court bien distinct du Kaf",
        "border": "#a855f7",
        "btn_bg": "#9333ea"
    },
    {
        "id": "saleh_qi_15",
        "title": "Saleh (Yémen) — Tajweed Authentique (-15%)",
        "voice": "ar-YE-SalehNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Timbre yéménite traditionnel profond",
        "border": "#06b6d4",
        "btn_bg": "#0891b2"
    },
    {
        "id": "moaz_qi_15",
        "title": "Moaz (Qatar) — Posé & Clair (-15%)",
        "voice": "ar-QA-MoazNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Voix qatarie claire et posée",
        "border": "#ec4899",
        "btn_bg": "#db2777"
    },
    {
        "id": "zariyah_qi_15",
        "title": "Zariyah (Féminin) — Très Articulé (-15%)",
        "voice": "ar-SA-ZariyahNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Voix féminine saoudienne très nette",
        "border": "#e11d48",
        "btn_bg": "#be123c"
    },
    {
        "id": "shakir_qi_short_15",
        "title": "Shakir — Bref Standard (-15%)",
        "voice": "ar-EG-ShakirNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Format court direct (sans Ya)",
        "border": "#64748b",
        "btn_bg": "#475569"
    }
]

TEMP_DIR = "scripts/temp_audio/qi_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_qi_candidates():
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
    for r in res:
        cards.append(f'''        <div class="card" style="border-color:{r['border']};">
          <div class="ar-word">قِ</div>
          <div class="phonetic" style="color:#fcd34d;">{r['title']}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{r['desc']}</p>
          <button class="play-btn" style="background:{r['btn_bg']};" onclick="playAudio('data:audio/mp3;base64,{r['b64']}', this)">🔊 Écouter</button>
        </div>''')
        
    qi_box = f'''    <!-- SECTION SPECIAL CHOIX DU SON QI -->
    <div class="highlight-box" style="border-color:#f59e0b; background:#78350f22;">
      <div class="highlight-title" style="color:#fbbf24;">🎯 Choix du son « Qi » (قِ — Qāf avec Kasrah)</div>
      <p class="highlight-desc">Écoute ces différentes propositions pour <strong>قِ</strong> afin d'obtenir un claquement uvulaire bien distinct du <strong>كِ (Ki)</strong> :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION QI -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL CHOIX DU SON QI -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON QI -->.*?<!-- /SECTION QI -->', qi_box, content, flags=re.DOTALL)
    else:
        # Insert right after the opening container or header
        marker = '<!-- SECTION SPECIAL LETTRES EMPHATIQUES KASRA -->'
        if marker in content:
            content = content.replace(marker, qi_box + '\n\n    ' + marker)
        else:
            header_end = '</header>'
            content = content.replace(header_end, header_end + '\n\n' + qi_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with Qi candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_qi_candidates())
    update_html(res)
