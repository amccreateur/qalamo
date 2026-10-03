import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "shakir_alif_long_15",
        "title": "Shakir — Net & Articulé (-15%) ⭐",
        "voice": "ar-EG-ShakirNeural",
        "text": "إِي",
        "rate": "-15%",
        "desc": "Coup de glotte 'Hamzah' franc suivi du son 'i' bien tenu",
        "border": "#22c55e",
        "btn_bg": "#16a34a"
    },
    {
        "id": "hamed_alif_long_15",
        "title": "Hamed — Posé & Clair (-15%) ⭐",
        "voice": "ar-SA-HamedNeural",
        "text": "إِي",
        "rate": "-15%",
        "desc": "Attaque classique saoudienne très propre et posée",
        "border": "#3b82f6",
        "btn_bg": "#2563eb"
    },
    {
        "id": "hamed_alif_slow25",
        "title": "Hamed — Plus Long (-25%)",
        "voice": "ar-SA-HamedNeural",
        "text": "إِي",
        "rate": "-25%",
        "desc": "Format plus lent, voyelle bien prolongée",
        "border": "#f59e0b",
        "btn_bg": "#d97706"
    },
    {
        "id": "moaz_alif_15",
        "title": "Moaz (Qatar) — Fluide & Net (-15%)",
        "voice": "ar-QA-MoazNeural",
        "text": "إِي",
        "rate": "-15%",
        "desc": "Timbre qatari très distinct",
        "border": "#a855f7",
        "btn_bg": "#9333ea"
    },
    {
        "id": "fahed_alif_15",
        "title": "Fahed (Golfe) — Dynamique (-15%)",
        "voice": "ar-KW-FahedNeural",
        "text": "إِي",
        "rate": "-15%",
        "desc": "Prononciation koweïtienne franche",
        "border": "#06b6d4",
        "btn_bg": "#0891b2"
    },
    {
        "id": "shakir_alif_short_15",
        "title": "Shakir — Bref Direct (-15%)",
        "voice": "ar-EG-ShakirNeural",
        "text": "إِ",
        "rate": "-15%",
        "desc": "Format court standard sans Ya",
        "border": "#ec4899",
        "btn_bg": "#db2777"
    },
    {
        "id": "hamed_alif_short_15",
        "title": "Hamed — Bref Direct (-15%)",
        "voice": "ar-SA-HamedNeural",
        "text": "إِ",
        "rate": "-15%",
        "desc": "Format court saoudien direct",
        "border": "#64748b",
        "btn_bg": "#475569"
    },
    {
        "id": "zariyah_alif_15",
        "title": "Zariyah (Féminin) — Cristallin (-15%)",
        "voice": "ar-SA-ZariyahNeural",
        "text": "إِي",
        "rate": "-15%",
        "desc": "Voix féminine saoudienne très claire",
        "border": "#e11d48",
        "btn_bg": "#be123c"
    }
]

TEMP_DIR = "scripts/temp_audio/alif_kasra_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_alif_kasra():
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
          <div class="ar-word">إِ</div>
          <div class="phonetic" style="color:#fcd34d;">{r['title']}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{r['desc']}</p>
          <button class="play-btn" style="background:{r['btn_bg']};" onclick="playAudio('data:audio/mp3;base64,{r['b64']}', this)">🔊 Écouter</button>
        </div>''')
        
    alif_box = f'''    <!-- SECTION SPECIAL CHOIX DU SON ALIF KASRA -->
    <div class="highlight-box" style="border-color:#38bdf8; background:#0284c722;">
      <div class="highlight-title" style="color:#38bdf8;">🎯 Choix du son « 'I » (إِ — Alif / Hamzah avec Kasrah)</div>
      <p class="highlight-desc">Voici les propositions pour <strong>إِ ('I)</strong> avec une attaque glottique nette et une voyelle bien audible :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION ALIF KASRA -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL CHOIX DU SON ALIF KASRA -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON ALIF KASRA -->.*?<!-- /SECTION ALIF KASRA -->', alif_box, content, flags=re.DOTALL)
    else:
        # Insert right after header
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + alif_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with Alif Kasrah candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_alif_kasra())
    update_html(res)
