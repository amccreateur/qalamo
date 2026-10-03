import asyncio
import edge_tts
import os
import subprocess
import base64

candidates = [
    {
        "id": "hedi_pure_qi_short",
        "title": "Hedi (Tunisie) — 'Qi' Bref Pur (-15%) ⭐",
        "voice": "ar-TN-HediNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' pure avec l'attaque ferme de Hedi"
    },
    {
        "id": "hedi_pure_qi_long",
        "title": "Hedi (Tunisie) — 'Qi' Soutenu Pur (-15%) ⭐",
        "voice": "ar-TN-HediNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' tenue avec l'attaque ferme de Hedi"
    },
    {
        "id": "shakir_pure_qi_short",
        "title": "Shakir (Égypte) — 'Qi' Bref Pur (-15%) ⭐",
        "voice": "ar-EG-ShakirNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' pure avec la voix Shakir"
    },
    {
        "id": "shakir_pure_qi_long",
        "title": "Shakir (Égypte) — 'Qi' Soutenu Pur (-15%)",
        "voice": "ar-EG-ShakirNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' tenue avec la voix Shakir"
    },
    {
        "id": "hamed_pure_qi_short",
        "title": "Hamed (Saoudien) — 'Qi' Bref Pur (-15%)",
        "voice": "ar-SA-HamedNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' pure avec la voix Hamed"
    },
    {
        "id": "hamed_pure_qi_long",
        "title": "Hamed (Saoudien) — 'Qi' Soutenu Pur (-15%)",
        "voice": "ar-SA-HamedNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' tenue avec la voix Hamed"
    },
    {
        "id": "fahed_pure_qi_short",
        "title": "Fahed (Golfe) — 'Qi' Bref Pur (-15%)",
        "voice": "ar-KW-FahedNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' pure claquante de Fahed"
    },
    {
        "id": "fahed_pure_qi_long",
        "title": "Fahed (Golfe) — 'Qi' Soutenu Pur (-15%)",
        "voice": "ar-KW-FahedNeural",
        "text": "قِي",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' tenue claquante de Fahed"
    },
    {
        "id": "abdullah_pure_qi_short",
        "title": "Abdullah (Oman) — 'Qi' Bref Pur (-15%)",
        "voice": "ar-OM-AbdullahNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' pure d'Abdullah"
    },
    {
        "id": "ismael_pure_qi_short",
        "title": "Ismaël (Algérie) — 'Qi' Bref Pur (-15%)",
        "voice": "ar-DZ-IsmaelNeural",
        "text": "قِ",
        "rate": "-15%",
        "desc": "Syllabe isolée 'Qi' pure d'Ismaël"
    }
]

TEMP_DIR = "scripts/temp_audio/pure_qi_candidates"
os.makedirs(TEMP_DIR, exist_ok=True)

async def generate_pure_qi():
    results = []
    for c in candidates:
        raw_path = os.path.join(TEMP_DIR, f"{c['id']}_raw.mp3")
        clean_path = os.path.join(TEMP_DIR, f"{c['id']}.mp3")
        
        communicate = edge_tts.Communicate(c["text"], c["voice"], rate=c["rate"])
        await communicate.save(raw_path)
        
        # ffmpeg: strictly clean silence removal (no word trimming, only pure syllable)
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
        
    qaf_box = f'''    <!-- SECTION SPECIAL PURE QI SEUL -->
    <div class="highlight-box" style="border-color:#22c55e; background:#064e3b22;">
      <div class="highlight-title" style="color:#4ade80;">🎯 Choix du son « Qi » Isolé Uniquement (قِ — Syllabe Pure Seule)</div>
      <p class="highlight-desc">Voici les versions contenant <strong>strictement et uniquement la syllabe isolée « Qi »</strong> :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION PURE QI SEUL -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL PURE QI SEUL -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL PURE QI SEUL -->.*?<!-- /SECTION PURE QI SEUL -->', qaf_box, content, flags=re.DOTALL)
    elif '<!-- SECTION SPECIAL ULTIMATE QAF -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL ULTIMATE QAF -->.*?<!-- /SECTION ULTIMATE QAF -->', qaf_box, content, flags=re.DOTALL)
    else:
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + qaf_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with pure isolated Qi candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_pure_qi())
    update_html(res)
