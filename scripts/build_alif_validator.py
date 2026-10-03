import asyncio
import os
import subprocess
import base64
import edge_tts

OUTPUT_DIR = "scripts/test_proposals/alif_vowels"
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Generate pairs and cut first syllable helper
async def generate_sliced_first_syllable(text_pair, voice, out_name, rate="-8%"):
    raw_file = f"scripts/temp_audio/raw_pair_{out_name}.mp3"
    comm = edge_tts.Communicate(text_pair, voice, rate=rate)
    await comm.save(raw_file)
    
    trimmed_start = f"scripts/temp_audio/trimmed_start_{out_name}.mp3"
    subprocess.run([
        "ffmpeg", "-y", "-i", raw_file,
        "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB",
        trimmed_start
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    
    detect_res = subprocess.run([
        "ffmpeg", "-i", trimmed_start,
        "-af", "silencedetect=noise=-25dB:d=0.04",
        "-f", "null", "-"
    ], capture_output=True, text=True)
    
    end_time = 0.45
    for line in detect_res.stderr.splitlines():
        if "silence_start:" in line:
            parts = line.split("silence_start:")
            if len(parts) > 1:
                val = float(parts[1].strip().split()[0])
                if val > 0.15:
                    end_time = val
                    break
    
    final_out = os.path.join(OUTPUT_DIR, f"{out_name}.mp3")
    subprocess.run([
        "ffmpeg", "-y", "-i", trimmed_start,
        "-t", str(end_time + 0.05),
        "-af", "areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-45dB,areverse,loudnorm=I=-16:TP=-1.5:LRA=7",
        "-ar", "44100", "-b:a", "128k",
        final_out
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[OK] Sliced {out_name} (cut at {end_time:.3f}s)")

async def generate_direct(text, voice, out_name, rate="-8%"):
    raw = f"scripts/temp_audio/raw_direct_{out_name}.mp3"
    comm = edge_tts.Communicate(text, voice, rate=rate)
    await comm.save(raw)
    final_out = os.path.join(OUTPUT_DIR, f"{out_name}.mp3")
    subprocess.run([
        "ffmpeg", "-y", "-i", raw,
        "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,areverse,loudnorm=I=-16:TP=-1.5:LRA=7",
        "-ar", "44100", "-b:a", "128k",
        final_out
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[OK] Direct {out_name}")

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

async def generate_all_audio():
    print("Generating pure Alif proposals...")
    # FATHA
    await generate_direct("ءَ", "ar-SA-HamedNeural", "fatha_hamed_hamza")
    await generate_sliced_first_syllable("أَ بَ", "ar-SA-HamedNeural", "fatha_hamed_sliced")
    await generate_direct("ءَ", "ar-EG-ShakirNeural", "fatha_shakir_hamza")
    await generate_sliced_first_syllable("أَ بَ", "ar-EG-ShakirNeural", "fatha_shakir_sliced")
    await generate_direct("ءَ", "ar-TN-HediNeural", "fatha_hedi_hamza")
    await generate_sliced_first_syllable("أَ بَ", "ar-TN-HediNeural", "fatha_hedi_sliced")
    await generate_direct("ءَ", "ar-QA-MoazNeural", "fatha_moaz_hamza")
    await generate_direct("ءَ", "ar-SA-ZariyahNeural", "fatha_zariyah_hamza")
    
    # DAMMA
    await generate_direct("أُ", "ar-SA-HamedNeural", "damma_hamed")
    await generate_direct("أُ", "ar-EG-ShakirNeural", "damma_shakir")
    await generate_direct("أُ", "ar-TN-HediNeural", "damma_hedi")
    await generate_direct("أُ", "ar-QA-MoazNeural", "damma_moaz")
    await generate_direct("أُ", "ar-SA-ZariyahNeural", "damma_zariyah")
    
    # KASRA
    await generate_direct("إِ", "ar-SA-HamedNeural", "kasra_hamed")
    await generate_direct("إِ", "ar-EG-ShakirNeural", "kasra_shakir")
    await generate_direct("إِ", "ar-TN-HediNeural", "kasra_hedi")
    await generate_direct("إِ", "ar-QA-MoazNeural", "kasra_moaz")
    await generate_direct("إِ", "ar-SA-ZariyahNeural", "kasra_zariyah")

def build_html():
    fatha_cards = [
        {
            "id": "curr",
            "title": "Version Actuelle (Problème 'An')",
            "voice": "assets/audio/generated/alif_fatha.mp3",
            "file": "assets/audio/generated/alif_fatha.mp3",
            "badge": "Projet Actuel",
            "badge_type": "curr",
            "desc": "Son actuellement dans l'application"
        },
        {
            "id": "hamed_hamza",
            "title": "1. Hamed — Hamza Fatḥah",
            "voice": "ar-SA-Hamed | ء + َ",
            "file": os.path.join(OUTPUT_DIR, "fatha_hamed_hamza.mp3"),
            "badge": "Recommandé (Court & Net)",
            "badge_type": "rec",
            "desc": "Son 'A' court, franc, sans aucune nasalisation 'an'"
        },
        {
            "id": "hamed_sliced",
            "title": "2. Hamed — Syllabé Extrait",
            "voice": "ar-SA-Hamed | [أَ] بَ",
            "file": os.path.join(OUTPUT_DIR, "fatha_hamed_sliced.mp3"),
            "badge": "Recommandé (Ouvert & Pur)",
            "badge_type": "rec",
            "desc": "Extrait naturel de la syllabe ouverte 'A'"
        },
        {
            "id": "shakir_hamza",
            "title": "3. Shakir — Hamza Fatḥah",
            "voice": "ar-EG-Shakir | ء + َ",
            "file": os.path.join(OUTPUT_DIR, "fatha_shakir_hamza.mp3"),
            "badge": "Shakir Direct",
            "badge_type": "voice",
            "desc": "Attaque ferme et claire, zéro 'an'"
        },
        {
            "id": "shakir_sliced",
            "title": "4. Shakir — Syllabé Extrait",
            "voice": "ar-EG-Shakir | [أَ] بَ",
            "file": os.path.join(OUTPUT_DIR, "fatha_shakir_sliced.mp3"),
            "badge": "Shakir Syllabé",
            "badge_type": "voice",
            "desc": "Syllabe 'A' posée et bien audible"
        },
        {
            "id": "hedi_hamza",
            "title": "5. Hedi — Hamza Fatḥah",
            "voice": "ar-TN-Hedi | ء + َ",
            "file": os.path.join(OUTPUT_DIR, "fatha_hedi_hamza.mp3"),
            "badge": "Hedi Direct",
            "badge_type": "voice",
            "desc": "Son très net et concis"
        },
        {
            "id": "hedi_sliced",
            "title": "6. Hedi — Syllabé Extrait",
            "voice": "ar-TN-Hedi | [أَ] بَ",
            "file": os.path.join(OUTPUT_DIR, "fatha_hedi_sliced.mp3"),
            "badge": "Hedi Syllabé",
            "badge_type": "voice",
            "desc": "Syllabe 'A' fluide et claire"
        },
        {
            "id": "moaz_hamza",
            "title": "7. Moaz — Hamza Fatḥah",
            "voice": "ar-QA-Moaz | ء + َ",
            "file": os.path.join(OUTPUT_DIR, "fatha_moaz_hamza.mp3"),
            "badge": "Moaz (Qatar)",
            "badge_type": "voice",
            "desc": "Son doux et direct"
        },
        {
            "id": "zariyah_hamza",
            "title": "8. Zariyah — Hamza Fatḥah",
            "voice": "ar-SA-Zariyah | ء + َ",
            "file": os.path.join(OUTPUT_DIR, "fatha_zariyah_hamza.mp3"),
            "badge": "Zariyah (Féminin)",
            "badge_type": "voice",
            "desc": "Voix féminine saoudienne"
        },
    ]

    damma_cards = [
        {
            "id": "curr",
            "title": "Version Actuelle",
            "voice": "assets/audio/generated/alif_damma.mp3",
            "file": "assets/audio/generated/alif_damma.mp3",
            "badge": "Projet Actuel",
            "badge_type": "curr",
            "desc": "Son 'OU' dans l'application"
        },
        {
            "id": "damma_hamed",
            "title": "Hamed (Arabie Saoudite)",
            "voice": "ar-SA-HamedNeural",
            "file": os.path.join(OUTPUT_DIR, "damma_hamed.mp3"),
            "badge": "Recommandé",
            "badge_type": "rec",
            "desc": "Son 'OU' standard pur"
        },
        {
            "id": "damma_shakir",
            "title": "Shakir (Égypte)",
            "voice": "ar-EG-ShakirNeural",
            "file": os.path.join(OUTPUT_DIR, "damma_shakir.mp3"),
            "badge": "Shakir",
            "badge_type": "voice",
            "desc": "Son 'OU' ferme"
        },
        {
            "id": "damma_hedi",
            "title": "Hedi (Tunisie)",
            "voice": "ar-TN-HediNeural",
            "file": os.path.join(OUTPUT_DIR, "damma_hedi.mp3"),
            "badge": "Hedi",
            "badge_type": "voice",
            "desc": "Son 'OU' net"
        },
        {
            "id": "damma_moaz",
            "title": "Moaz (Qatar)",
            "voice": "ar-QA-MoazNeural",
            "file": os.path.join(OUTPUT_DIR, "damma_moaz.mp3"),
            "badge": "Moaz",
            "badge_type": "voice",
            "desc": "Son 'OU' posé"
        },
    ]

    kasra_cards = [
        {
            "id": "curr",
            "title": "Version Actuelle",
            "voice": "assets/audio/generated/alif_kasra.mp3",
            "file": "assets/audio/generated/alif_kasra.mp3",
            "badge": "Projet Actuel",
            "badge_type": "curr",
            "desc": "Son 'I' dans l'application"
        },
        {
            "id": "kasra_hamed",
            "title": "Hamed (Arabie Saoudite)",
            "voice": "ar-SA-HamedNeural",
            "file": os.path.join(OUTPUT_DIR, "kasra_hamed.mp3"),
            "badge": "Recommandé",
            "badge_type": "rec",
            "desc": "Son 'I' standard pur"
        },
        {
            "id": "kasra_shakir",
            "title": "Shakir (Égypte)",
            "voice": "ar-EG-ShakirNeural",
            "file": os.path.join(OUTPUT_DIR, "kasra_shakir.mp3"),
            "badge": "Shakir",
            "badge_type": "voice",
            "desc": "Son 'I' ferme"
        },
        {
            "id": "kasra_hedi",
            "title": "Hedi (Tunisie)",
            "voice": "ar-TN-HediNeural",
            "file": os.path.join(OUTPUT_DIR, "kasra_hedi.mp3"),
            "badge": "Hedi",
            "badge_type": "voice",
            "desc": "Son 'I' net"
        },
        {
            "id": "kasra_moaz",
            "title": "Moaz (Qatar)",
            "voice": "ar-QA-MoazNeural",
            "file": os.path.join(OUTPUT_DIR, "kasra_moaz.mp3"),
            "badge": "Moaz",
            "badge_type": "voice",
            "desc": "Son 'I' posé"
        },
    ]

    def render_section(title, arabic_char, desc, cards, is_highlight=False):
        section_style = "border: 2px solid #38bdf8; background: #0f1f38;" if is_highlight else "background: #131d31; border: 2px solid #1e293b;"
        tag_highlight = "<span style='background: #ef4444; color: white; padding: 4px 10px; border-radius: 8px; font-size: 13px; font-weight: bold; margin-left: 10px;'>Correction 'An' → 'A' Pur</span>" if is_highlight else ""
        
        sec_html = f"""
        <div class="category-section" style="{section_style}">
          <div class="category-header">
            <div class="category-title">
              <span>{title}</span>
              {tag_highlight}
            </div>
            <div class="category-char">{arabic_char}</div>
          </div>
          <div class="category-desc">{desc}</div>
          <div class="grid">
        """
        for card in cards:
            b64 = get_b64(card["file"])
            card_class = "card current" if card["badge_type"] == "curr" else ("card rec" if card["badge_type"] == "rec" else "card")
            badge_class = f"badge-{card['badge_type']}"
            sec_html += f"""
            <div class="{card_class}">
              <div class="badge {badge_class}">{card["badge"]}</div>
              <div class="card-title">{card["title"]}</div>
              <div class="card-sub">{card["voice"]}</div>
              <div style="font-size: 11px; color: #94a3b8; margin-bottom: 12px; min-height: 28px;">{card["desc"]}</div>
              <button class="play-btn" onclick="playAudio('data:audio/mp3;base64,{b64}', this)">🔊 Écouter</button>
            </div>
            """
        sec_html += """
          </div>
        </div>
        """
        return sec_html

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo — Console de Validation des Sons Alif (Fatḥah, Ḍammah, Kasrah)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    body {{ background: #0b0f19; color: #f8fafc; padding: 30px 16px; display: flex; justify-content: center; }}
    .container {{ width: 100%; max-width: 1150px; }}
    header {{ text-align: center; margin-bottom: 28px; }}
    h1 {{ color: #38bdf8; font-size: 28px; margin-bottom: 8px; }}
    p.subtitle {{ color: #94a3b8; font-size: 15px; margin-bottom: 20px; }}

    .notice-box {{ background: #1e293b; border-left: 4px solid #f59e0b; padding: 14px 18px; border-radius: 8px; margin-bottom: 24px; color: #cbd5e1; font-size: 14px; line-height: 1.5; }}
    .notice-box strong {{ color: #fcd34d; }}

    .category-section {{ border-radius: 20px; padding: 22px; margin-bottom: 28px; }}
    .category-header {{ display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid #334155; padding-bottom: 10px; }}
    .category-title {{ color: #f59e0b; font-size: 22px; font-weight: 800; display: flex; align-items: center; flex-wrap: wrap; gap: 8px; }}
    .category-char {{ font-family: 'Amiri', serif; font-size: 52px; color: #fde047; line-height: 56px; }}
    .category-desc {{ color: #94a3b8; font-size: 14px; margin-bottom: 18px; }}

    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }}
    .card {{ background: #0b0f19; border: 2px solid #334155; border-radius: 16px; padding: 16px; text-align: center; transition: all 0.15s; display: flex; flex-direction: column; justify-content: space-between; }}
    .card:hover {{ border-color: #38bdf8; transform: translateY(-2px); }}
    .card.current {{ border-color: #ef4444; background: #7f1d1d15; }}
    .card.rec {{ border-color: #10b981; background: #064e3b15; }}

    .badge {{ display: inline-block; font-size: 10px; font-weight: 800; text-transform: uppercase; padding: 4px 10px; border-radius: 12px; margin-bottom: 10px; align-self: center; }}
    .badge-curr {{ background: #ef444422; color: #f87171; border: 1px solid #ef444466; }}
    .badge-rec {{ background: #10b98122; color: #34d399; border: 1px solid #10b98166; }}
    .badge-voice {{ background: #334155; color: #cbd5e1; }}

    .card-title {{ font-size: 15px; font-weight: 800; color: #f8fafc; margin-bottom: 4px; }}
    .card-sub {{ font-size: 11px; color: #64748b; margin-bottom: 8px; word-break: break-all; }}

    .play-btn {{ width: 100%; background: #2563eb; color: white; border: none; padding: 10px; border-radius: 10px; font-size: 14px; font-weight: 800; cursor: pointer; transition: all 0.15s; display: flex; align-items: center; justify-content: center; gap: 6px; margin-top: auto; }}
    .play-btn:hover {{ background: #3b82f6; }}
    .play-btn.playing {{ background: #10b981 !important; transform: scale(1.02); }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🎙️ Console de Validation des Sons de l'Alif (أ)</h1>
      <p class="subtitle">Validation comparative des 3 voyelles courtes avec élimination du son 'An' (Tanwīn) sur l'Alif Fatḥah</p>
    </header>

    <div class="notice-box">
      🔍 <strong>Diagnostic du son 'An' :</strong> Les moteurs TTS arabes synthétisent souvent <code>أَ</code> isolé comme une nunation (Tanwīn Fatḥ <code>أً</code> / "An").<br>
      Ci-dessous, la section <strong>Alif Fatḥah</strong> propose les solutions 100% nettes sans nasalisation (Hamza <code>ءَ</code> directe ou extraction syllabique pure <code>[أَ] بَ</code>).
    </div>

    {render_section("Alif Fatḥah — Son 'A' Pur (Sans 'An')", "أَ", "Toutes les options ci-dessous suppriment la nasalisation pour donner le son voyelle pure 'A'", fatha_cards, is_highlight=True)}

    {render_section("Alif Ḍammah — Son 'OU' Pur", "أُ", "Sons pour la voyelle courte Ḍammah (OU)", damma_cards, is_highlight=False)}

    {render_section("Alif Kasrah — Son 'I' Pur", "إِ", "Sons pour la voyelle courte Kasrah (I)", kasra_cards, is_highlight=False)}
  </div>

  <script>
    let currentAudio = null;
    let currentBtn = null;

    function playAudio(src, btn) {{
      if (currentAudio) {{
        currentAudio.pause();
        if (currentBtn) currentBtn.classList.remove('playing');
      }}
      currentAudio = new Audio(src);
      currentBtn = btn;
      btn.classList.add('playing');
      currentAudio.play().catch(e => console.error("Audio error:", e));
      currentAudio.onended = () => {{
        btn.classList.remove('playing');
      }};
    }}
  </script>
</body>
</html>
"""
    with open("test_alif_vowels.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("test_alif_vowels.html built successfully!")

async def main():
    await generate_all_audio()
    build_html()

if __name__ == "__main__":
    asyncio.run(main())
