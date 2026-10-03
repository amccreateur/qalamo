import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "hamed_ki_slow20",
        "title": "Hamed — Doux & Posé (-20%) ⭐",
        "voice": "ar-SA-HamedNeural",
        "text": "كِ",
        "rate": "-20%",
        "desc": "Timbre très doux de Hamed, ralenti de 20% pour bien tenir le son"
    },
    {
        "id": "hamed_ki_slow25",
        "title": "Hamed — Bien Soutenu (-25%) ⭐⭐",
        "voice": "ar-SA-HamedNeural",
        "text": "كِ",
        "rate": "-25%",
        "desc": "Plus long et très posé, attaque fine et voyelle claire"
    },
    {
        "id": "hamed_ki_slow30",
        "title": "Hamed — Très Long & Posé (-30%)",
        "voice": "ar-SA-HamedNeural",
        "text": "كِ",
        "rate": "-30%",
        "desc": "Cadence lente d'apprentissage, très doux"
    },
    {
        "id": "hamed_ki_ya_slow20",
        "title": "Hamed — Voyelle Tenue (-20%)",
        "voice": "ar-SA-HamedNeural",
        "text": "كِي",
        "rate": "-20%",
        "desc": "Avec voyelle 'i' tenue et adoucie"
    },
    {
        "id": "hamed_ki_ya_slow25",
        "title": "Hamed — Voyelle Tenue (-25%)",
        "voice": "ar-SA-HamedNeural",
        "text": "كِي",
        "rate": "-25%",
        "desc": "Format long avec voyelle étirée douce"
    }
]

TEMP_DIR = "scripts/temp_audio/hamed_ki_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_hamed_ki():
    results = []
    for c in candidates:
        raw_path = os.path.join(TEMP_DIR, f"{c['id']}_raw.mp3")
        clean_path = os.path.join(TEMP_DIR, f"{c['id']}.mp3")
        
        communicate = edge_tts.Communicate(c["text"], c["voice"], rate=c["rate"])
        await communicate.save(raw_path)
        
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
    colors = ["#22c55e", "#3b82f6", "#f59e0b", "#a855f7", "#06b6d4"]
    btn_bgs = ["#16a34a", "#2563eb", "#d97706", "#9333ea", "#0891b2"]
    
    for idx, r in enumerate(res):
        c_border = colors[idx % len(colors)]
        c_btn = btn_bgs[idx % len(btn_bgs)]
        cards.append(f'''        <div class="card" style="border-color:{c_border};">
          <div class="ar-word">كِ</div>
          <div class="phonetic" style="color:#fcd34d;">{r['title']}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{r['desc']}</p>
          <button class="play-btn" style="background:{c_btn};" onclick="playAudio('data:audio/mp3;base64,{r['b64']}', this)">🔊 Écouter</button>
        </div>''')
        
    ki_box = f'''    <!-- SECTION SPECIAL CHOIX DU SON KI HAMED -->
    <div class="highlight-box" style="border-color:#f59e0b; background:#78350f22;">
      <div class="highlight-title" style="color:#fbbf24;">✨ Choix du son « Ki » (Hamed — Doux & Fin, Versions Plus Longues)</div>
      <p class="highlight-desc">Voici les versions de <strong>Hamed (Doux & Fin)</strong> ralenties pour que le son dure plus longtemps sans perdre sa douceur :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION KI HAMED -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL CHOIX DU SON KI HAMED -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON KI HAMED -->.*?<!-- /SECTION KI HAMED -->', ki_box, content, flags=re.DOTALL)
    elif '<!-- SECTION SPECIAL CHOIX DU SON KI LEGER -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON KI LEGER -->.*?<!-- /SECTION KI LEGER -->', ki_box, content, flags=re.DOTALL)
    else:
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + ki_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with Hamed long Ki candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_hamed_ki())
    update_html(res)
