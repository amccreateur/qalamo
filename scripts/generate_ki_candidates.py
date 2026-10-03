import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "shakir_ki_long_15",
        "title": "Shakir — Net & Articulé (-15%) ⭐ Recommandé",
        "voice": "ar-EG-ShakirNeural",
        "text": "كِي",
        "rate": "-15%",
        "desc": "Kaf fin bien distinct du Qaf, avec 'i' clair et souriant",
        "border": "#22c55e",
        "btn_bg": "#16a34a"
    },
    {
        "id": "hamed_ki_long_15",
        "title": "Hamed — Posé & Clair (-15%)",
        "voice": "ar-SA-HamedNeural",
        "text": "كِي",
        "rate": "-15%",
        "desc": "Prononciation saoudienne classique très propre",
        "border": "#3b82f6",
        "btn_bg": "#2563eb"
    },
    {
        "id": "moaz_ki_15",
        "title": "Moaz (Qatar) — Fluide & Net (-15%)",
        "voice": "ar-QA-MoazNeural",
        "text": "كِي",
        "rate": "-15%",
        "desc": "Timbre qatari posé et distinct",
        "border": "#f59e0b",
        "btn_bg": "#d97706"
    },
    {
        "id": "fahed_ki_15",
        "title": "Fahed (Golfe) — Dynamique (-15%)",
        "voice": "ar-KW-FahedNeural",
        "text": "كِي",
        "rate": "-15%",
        "desc": "Prononciation koweïtienne franche",
        "border": "#a855f7",
        "btn_bg": "#9333ea"
    },
    {
        "id": "shakir_ki_short_15",
        "title": "Shakir — Bref Direct (-15%)",
        "voice": "ar-EG-ShakirNeural",
        "text": "كِ",
        "rate": "-15%",
        "desc": "Format court standard sans Ya",
        "border": "#ec4899",
        "btn_bg": "#db2777"
    },
    {
        "id": "hamed_ki_short_15",
        "title": "Hamed — Bref Direct (-15%)",
        "voice": "ar-SA-HamedNeural",
        "text": "كِ",
        "rate": "-15%",
        "desc": "Format court saoudien direct",
        "border": "#06b6d4",
        "btn_bg": "#0891b2"
    },
    {
        "id": "zariyah_ki_15",
        "title": "Zariyah (Féminin) — Très Articulé (-15%)",
        "voice": "ar-SA-ZariyahNeural",
        "text": "كِي",
        "rate": "-15%",
        "desc": "Voix féminine saoudienne très claire",
        "border": "#e11d48",
        "btn_bg": "#be123c"
    }
]

TEMP_DIR = "scripts/temp_audio/ki_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_ki_candidates():
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
        
    ki_box = f'''    <!-- SECTION SPECIAL CHOIX DU SON KI -->
    <div class="highlight-box" style="border-color:#a855f7; background:#581c8722;">
      <div class="highlight-title" style="color:#c084fc;">🎯 Choix du son « Ki » (كِ — Kāf avec Kasrah)</div>
      <p class="highlight-desc">Voici les propositions pour <strong>كِ (Ki fin)</strong>, pour une parfaite distinction d'avec <strong>قِ (Qi profond)</strong> :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION KI -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL CHOIX DU SON KI -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON KI -->.*?<!-- /SECTION KI -->', ki_box, content, flags=re.DOTALL)
    else:
        # Insert right after the header
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + ki_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with Ki candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_ki_candidates())
    update_html(res)
