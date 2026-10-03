import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "moaz_ki_clean_15",
        "title": "Moaz (Qatar) — Fluide & Naturel (-15%) ⭐ Recommandé",
        "voice": "ar-QA-MoazNeural",
        "text": "كِ",
        "rate": "-15%",
        "desc": "Même voix que le 'I et le Qi : très propre, naturel et sans traîner",
        "border": "#22c55e",
        "btn_bg": "#16a34a"
    },
    {
        "id": "hamed_ki_court_15",
        "title": "Hamed — Court & Naturel (-15%) ⭐",
        "voice": "ar-SA-HamedNeural",
        "text": "كِ",
        "rate": "-15%",
        "desc": "Vrai son court 'Ki' de Hamed sans allongement artificiel",
        "border": "#3b82f6",
        "btn_bg": "#2563eb"
    },
    {
        "id": "fahed_ki_clean_15",
        "title": "Fahed (Golfe) — Net & Percutant (-15%)",
        "voice": "ar-KW-FahedNeural",
        "text": "كِ",
        "rate": "-15%",
        "desc": "Prononciation koweïtienne franche et claire",
        "border": "#f59e0b",
        "btn_bg": "#d97706"
    },
    {
        "id": "shakir_ki_court_15",
        "title": "Shakir — Bref Classique (-15%)",
        "voice": "ar-EG-ShakirNeural",
        "text": "كِ",
        "rate": "-15%",
        "desc": "Format court standard égyptien classique",
        "border": "#a855f7",
        "btn_bg": "#9333ea"
    },
    {
        "id": "saleh_ki_15",
        "title": "Saleh (Yémen) — Tajweed Posé (-15%)",
        "voice": "ar-YE-SalehNeural",
        "text": "كِ",
        "rate": "-15%",
        "desc": "Prononciation traditionnelle yéménite",
        "border": "#06b6d4",
        "btn_bg": "#0891b2"
    },
    {
        "id": "zariyah_ki_clean_15",
        "title": "Zariyah (Féminin) — Cristallin (-15%)",
        "voice": "ar-SA-ZariyahNeural",
        "text": "كِ",
        "rate": "-15%",
        "desc": "Voix féminine saoudienne très distincte",
        "border": "#ec4899",
        "btn_bg": "#db2777"
    }
]

TEMP_DIR = "scripts/temp_audio/ki_final_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_ki_final():
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
          <div class="ar-word">كِ</div>
          <div class="phonetic" style="color:#fcd34d;">{r['title']}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{r['desc']}</p>
          <button class="play-btn" style="background:{r['btn_bg']};" onclick="playAudio('data:audio/mp3;base64,{r['b64']}', this)">🔊 Écouter</button>
        </div>''')
        
    ki_box = f'''    <!-- SECTION SPECIAL CHOIX DU SON KI FINAL -->
    <div class="highlight-box" style="border-color:#22c55e; background:#064e3b22;">
      <div class="highlight-title" style="color:#4ade80;">🎯 Choix du son « Ki » (كِ — Vrai Son Court Naturel & Net)</div>
      <p class="highlight-desc">Voici les versions naturelles pour <strong>كِ (Kāf Kasrah court)</strong> sans voyelle étirée artificielle :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION KI FINAL -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL CHOIX DU SON KI FINAL -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON KI FINAL -->.*?<!-- /SECTION KI FINAL -->', ki_box, content, flags=re.DOTALL)
    elif '<!-- SECTION SPECIAL CHOIX DU SON KI HAMED -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON KI HAMED -->.*?<!-- /SECTION KI HAMED -->', ki_box, content, flags=re.DOTALL)
    else:
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + ki_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with clean natural Ki candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_ki_final())
    update_html(res)
