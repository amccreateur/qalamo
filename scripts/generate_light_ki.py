import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "shakir_ki_light_court_10",
        "title": "Shakir — Léger & Court (-10%) ⭐",
        "voice": "ar-EG-ShakirNeural",
        "text": "كِ",
        "rate": "-10%",
        "desc": "Son bref, fin et délicat, sans traîner sur la voyelle",
        "border": "#22c55e",
        "btn_bg": "#16a34a"
    },
    {
        "id": "shakir_ki_light_naturel_0",
        "title": "Shakir — Ultra Léger & Naturel (0%) ⭐",
        "voice": "ar-EG-ShakirNeural",
        "text": "كِ",
        "rate": "+0%",
        "desc": "Rythme naturel vif, très léger et précis",
        "border": "#3b82f6",
        "btn_bg": "#2563eb"
    },
    {
        "id": "hamed_ki_light_10",
        "title": "Hamed — Doux & Fin (-10%)",
        "voice": "ar-SA-HamedNeural",
        "text": "كِ",
        "rate": "-10%",
        "desc": "Attaque très douce du Kaf, très fin",
        "border": "#f59e0b",
        "btn_bg": "#d97706"
    },
    {
        "id": "moaz_ki_light_10",
        "title": "Moaz (Qatar) — Léger & Posé (-10%)",
        "voice": "ar-QA-MoazNeural",
        "text": "كِ",
        "rate": "-10%",
        "desc": "Timbre posé et soyeux",
        "border": "#a855f7",
        "btn_bg": "#9333ea"
    },
    {
        "id": "zariyah_ki_light_10",
        "title": "Zariyah (Féminin) — Cristallin & Léger (-10%)",
        "voice": "ar-SA-ZariyahNeural",
        "text": "كِ",
        "rate": "-10%",
        "desc": "Voix féminine très claire et fine",
        "border": "#ec4899",
        "btn_bg": "#db2777"
    },
    {
        "id": "noura_ki_light_10",
        "title": "Noura (Golfe Féminin) — Très Doux (-10%)",
        "voice": "ar-KW-NouraNeural",
        "text": "كِ",
        "rate": "-10%",
        "desc": "Prononciation féminine koweïtienne très délicate",
        "border": "#06b6d4",
        "btn_bg": "#0891b2"
    }
]

TEMP_DIR = "scripts/temp_audio/light_ki_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_light_ki():
    results = []
    for c in candidates:
        raw_path = os.path.join(TEMP_DIR, f"{c['id']}_raw.mp3")
        clean_path = os.path.join(TEMP_DIR, f"{c['id']}.mp3")
        
        communicate = edge_tts.Communicate(c["text"], c["voice"], rate=c["rate"])
        await communicate.save(raw_path)
        
        # ffmpeg: clean trim, volume normalisé
        cmd = [
            "ffmpeg", "-y", "-i", raw_path,
            "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=4dB",
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
          <div class="ar-word">كِ</div>
          <div class="phonetic" style="color:#fcd34d;">{r['title']}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{r['desc']}</p>
          <button class="play-btn" style="background:{r['btn_bg']};" onclick="playAudio('data:audio/mp3;base64,{r['b64']}', this)">🔊 Écouter</button>
        </div>''')
        
    ki_box = f'''    <!-- SECTION SPECIAL CHOIX DU SON KI LEGER -->
    <div class="highlight-box" style="border-color:#34d399; background:#064e3b33;">
      <div class="highlight-title" style="color:#34d399;">🪶 Choix du son « Ki » Plus Léger & Fin (كِ — Kāf Kasrah)</div>
      <p class="highlight-desc">Voici des versions plus légères, fines et sans lourdeur pour <strong>كِ (Ki fin)</strong> :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION KI LEGER -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL CHOIX DU SON KI LEGER -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON KI LEGER -->.*?<!-- /SECTION KI LEGER -->', ki_box, content, flags=re.DOTALL)
    else:
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + ki_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with light Ki candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_light_ki())
    update_html(res)
