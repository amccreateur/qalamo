import asyncio
import edge_tts
import os
import subprocess
import base64

os.makedirs("scripts/temp_audio/ultimate_qaf", exist_ok=True)

# We will generate both direct syllables and word-extracted pure Qaf syllables
word_tests = [
    {
        "id": "shakir_qaf_from_word",
        "title": "Studio Shakir — Extrait Mot Fusha ⭐⭐",
        "voice": "ar-EG-ShakirNeural",
        "text": "قِطَار",
        "trim_end": 0.45,  # keep the initial Qi
        "rate": "-10%",
        "desc": "Extrait d'un mot classique : claquement uvulaire 100% naturel et fluide"
    },
    {
        "id": "hamed_qaf_from_word",
        "title": "Studio Hamed — Extrait Mot Fusha ⭐⭐",
        "voice": "ar-SA-HamedNeural",
        "text": "قِطَار",
        "trim_end": 0.48,
        "rate": "-10%",
        "desc": "Extrait d'un mot saoudien classique : Qaf très net et voyelle pure"
    },
    {
        "id": "hedi_qaf_from_word",
        "title": "Studio Hedi — Extrait Mot Fusha ⭐",
        "voice": "ar-TN-HediNeural",
        "text": "قِطَار",
        "trim_end": 0.45,
        "rate": "-10%",
        "desc": "Attaque ferme de Hedi issue d'un mot naturel"
    },
    {
        "id": "shakir_qaf_qeela",
        "title": "Shakir — Issu de 'Qeela' (قِيلَ)",
        "voice": "ar-EG-ShakirNeural",
        "text": "قِيلَ",
        "trim_end": 0.52,
        "rate": "-10%",
        "desc": "Format avec voyelle 'i' tenue issue du mot classique قيل"
    },
    {
        "id": "hamed_qaf_qeela",
        "title": "Hamed — Issu de 'Qeela' (قِيلَ)",
        "voice": "ar-SA-HamedNeural",
        "text": "قِيلَ",
        "trim_end": 0.55,
        "rate": "-10%",
        "desc": "Format saoudien issu du mot classique قيل"
    },
    {
        "id": "abdullah_qaf_clean",
        "title": "Abdullah (Oman) — Fusha Studio",
        "voice": "ar-OM-AbdullahNeural",
        "text": "قِـ",
        "trim_end": None,
        "rate": "-10%",
        "desc": "Syllabe directe avec tatweel pour une tenue parfaite"
    },
    {
        "id": "salma_qaf_clean",
        "title": "Salma (Égypte) — Ciselé & Net",
        "voice": "ar-EG-SalmaNeural",
        "text": "قِ",
        "trim_end": None,
        "rate": "-10%",
        "desc": "Voix féminine avec un Qaf très bien placé"
    },
    {
        "id": "laila_qaf_clean",
        "title": "Laila (Bahreïn) — Doux & Distinct",
        "voice": "ar-BH-LailaNeural",
        "text": "قِ",
        "trim_end": None,
        "rate": "-10%",
        "desc": "Voix féminine très soignée"
    }
]

async def generate_ultimate():
    results = []
    for item in word_tests:
        raw_path = f"scripts/temp_audio/ultimate_qaf/{item['id']}_raw.mp3"
        clean_path = f"scripts/temp_audio/ultimate_qaf/{item['id']}.mp3"
        
        communicate = edge_tts.Communicate(item["text"], item["voice"], rate=item["rate"])
        await communicate.save(raw_path)
        
        filters = "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB"
        if item.get("trim_end"):
            # Trim after the syllable and add soft fadeout
            filters += f",atrim=0:{item['trim_end']},afade=t=out:st={item['trim_end']-0.08}:d=0.08"
        filters += ",volume=6dB"
        
        cmd = ["ffmpeg", "-y", "-i", raw_path, "-af", filters, clean_path]
        subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        
        with open(clean_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            
        results.append({**item, "b64": b64})
        print(f"Generated {item['id']}")
    return results

def update_html(res):
    cards = []
    colors = ["#22c55e", "#3b82f6", "#f59e0b", "#a855f7", "#06b6d4", "#ec4899", "#e11d48", "#10b981"]
    btn_bgs = ["#16a34a", "#2563eb", "#d97706", "#9333ea", "#0891b2", "#db2777", "#be123c", "#059669"]
    
    for idx, r in enumerate(res):
        c_border = colors[idx % len(colors)]
        c_btn = btn_bgs[idx % len(btn_bgs)]
        cards.append(f'''        <div class="card" style="border-color:{c_border};">
          <div class="ar-word">قِ</div>
          <div class="phonetic" style="color:#fcd34d;">{r['title']}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{r['desc']}</p>
          <button class="play-btn" style="background:{c_btn};" onclick="playAudio('data:audio/mp3;base64,{r['b64']}', this)">🔊 Écouter</button>
        </div>''')
        
    qaf_box = f'''    <!-- SECTION SPECIAL ULTIMATE QAF -->
    <div class="highlight-box" style="border-color:#f59e0b; background:#78350f22;">
      <div class="highlight-title" style="color:#fbbf24;">🎯 Propositions Studio / Haute Qualité pour « Qi » (قِ — Qāf Kasrah)</div>
      <p class="highlight-desc">Extractions de syllabes à partir de mots réels pour obtenir un <strong>قِ</strong> 100% naturel, sans artéfact de synthèse :</p>
      <div class="grid">
{chr(10).join(cards)}
      </div>
    </div>
    <!-- /SECTION ULTIMATE QAF -->'''

    with open("test_audio.html", "r", encoding="utf-8") as f:
        content = f.read()

    if '<!-- SECTION SPECIAL ULTIMATE QAF -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL ULTIMATE QAF -->.*?<!-- /SECTION ULTIMATE QAF -->', qaf_box, content, flags=re.DOTALL)
    elif '<!-- SECTION SPECIAL AMELIORATIONS HEDI QAF -->' in content:
        import re
        content = re.sub(r'<!-- SECTION SPECIAL AMELIORATIONS HEDI QAF -->.*?<!-- /SECTION AMELIORATIONS HEDI QAF -->', qaf_box, content, flags=re.DOTALL)
    else:
        header_end = '</header>'
        content = content.replace(header_end, header_end + '\n\n' + qaf_box)

    with open("test_audio.html", "w", encoding="utf-8") as f:
        f.write(content)

    print("test_audio.html updated with Ultimate Qaf candidates!")

if __name__ == "__main__":
    res = asyncio.run(generate_ultimate())
    update_html(res)
