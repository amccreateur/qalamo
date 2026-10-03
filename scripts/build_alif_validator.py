import asyncio
import os
import subprocess
import base64
import edge_tts

OUTPUT_DIR = "scripts/test_proposals/alif_vowels"
os.makedirs(OUTPUT_DIR, exist_ok=True)

VOICES = [
    ("hamed", "Hamed (Arabie Saoudite)", "ar-SA-HamedNeural", "-8%"),
    ("shakir", "Shakir (Égypte - Ferme)", "ar-EG-ShakirNeural", "-8%"),
    ("hedi", "Hedi (Tunisie - Net)", "ar-TN-HediNeural", "-8%"),
    ("moaz", "Moaz (Qatar - Posé)", "ar-QA-MoazNeural", "-8%"),
    ("zariyah", "Zariyah (Arabie S. - Féminin)", "ar-SA-ZariyahNeural", "-8%"),
    ("salma", "Salma (Égypte - Féminin)", "ar-EG-SalmaNeural", "-8%"),
]

ALIF_ITEMS = [
    ("fatha", "أَ", "Alif Fatḥah", "Son 'A' ouvert et net"),
    ("damma", "أُ", "Alif Ḍammah", "Son 'OU' arrondi et pur"),
    ("kasra", "إِ", "Alif Kasrah", "Son 'I' tiré et franc"),
]

def get_b64(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ''

async def generate_audio():
    print("Generating Alif variations for Fatha, Damma, Kasra...")
    for item_key, arabic_char, title, desc in ALIF_ITEMS:
        for voice_key, voice_label, voice_code, rate in VOICES:
            raw_file = os.path.join(OUTPUT_DIR, f"alif_{item_key}_{voice_key}_raw.mp3")
            out_file = os.path.join(OUTPUT_DIR, f"alif_{item_key}_{voice_key}.mp3")
            
            communicate = edge_tts.Communicate(arabic_char, voice_code, rate=rate)
            await communicate.save(raw_file)
            
            subprocess.run([
                "ffmpeg", "-y",
                "-i", raw_file,
                "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,areverse,loudnorm=I=-16:TP=-1.5:LRA=7",
                "-ar", "44100",
                "-b:a", "128k",
                out_file
            ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            print(f"[OK] alif_{item_key}_{voice_key}")

def build_html():
    html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo — Validation des Sons Alif (Fatḥah, Ḍammah, Kasrah)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background: #0b0f19; color: #f8fafc; padding: 30px 16px; display: flex; justify-content: center; }
    .container { width: 100%; max-width: 1100px; }
    header { text-align: center; margin-bottom: 28px; }
    h1 { color: #38bdf8; font-size: 28px; margin-bottom: 8px; }
    p.subtitle { color: #94a3b8; font-size: 15px; margin-bottom: 20px; }

    .category-section { background: #131d31; border: 2px solid #1e293b; border-radius: 20px; padding: 22px; margin-bottom: 28px; }
    .category-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid #334155; padding-bottom: 10px; }
    .category-title { color: #f59e0b; font-size: 22px; font-weight: 800; display: flex; align-items: center; gap: 12px; }
    .category-char { font-family: 'Amiri', serif; font-size: 48px; color: #fde047; line-height: 56px; }
    .category-desc { color: #94a3b8; font-size: 13px; margin-bottom: 16px; }

    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 14px; }
    .card { background: #0b0f19; border: 2px solid #334155; border-radius: 16px; padding: 16px; text-align: center; transition: all 0.15s; }
    .card:hover { border-color: #38bdf8; transform: translateY(-2px); }
    .card.current { border-color: #3b82f6; background: #1e3a8a15; }
    .card.rec { border-color: #10b981; background: #064e3b15; }

    .badge { display: inline-block; font-size: 10px; font-weight: 800; text-transform: uppercase; padding: 3px 8px; border-radius: 12px; margin-bottom: 8px; }
    .badge-curr { background: #3b82f622; color: #60a5fa; border: 1px solid #3b82f666; }
    .badge-rec { background: #10b98122; color: #34d399; border: 1px solid #10b98166; }
    .badge-voice { background: #334155; color: #cbd5e1; }

    .card-title { font-size: 15px; font-weight: 800; color: #f8fafc; margin-bottom: 4px; }
    .card-sub { font-size: 12px; color: #64748b; margin-bottom: 14px; }

    .play-btn { width: 100%; background: #2563eb; color: white; border: none; padding: 10px; border-radius: 10px; font-size: 14px; font-weight: 800; cursor: pointer; transition: all 0.15s; display: flex; align-items: center; justify-content: center; gap: 6px; }
    .play-btn:hover { background: #3b82f6; }
    .play-btn.playing { background: #10b981 !important; transform: scale(1.02); }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🎙️ Console de Validation des Sons de l'Alif (أ)</h1>
      <p class="subtitle">Écoute et compare les différentes voix pour Alif Fatḥah (أَ), Alif Ḍammah (أُ) et Alif Kasrah (إِ)</p>
    </header>
"""

    for item_key, arabic_char, title, desc in ALIF_ITEMS:
        html += f"""
    <div class="category-section">
      <div class="category-header">
        <div class="category-title">
          <span>{title}</span>
        </div>
        <div class="category-char">{arabic_char}</div>
      </div>
      <div class="category-desc">{desc}</div>
      <div class="grid">
        <!-- Version actuelle du projet -->
        <div class="card current">
          <div class="badge badge-curr">Projet Actuel</div>
          <div class="card-title">Version Actuelle</div>
          <div class="card-sub">assets/audio/generated/alif_{item_key}.mp3</div>
          <button class="play-btn" onclick="playAudio('data:audio/mp3;base64,{get_b64(f'assets/audio/generated/alif_{item_key}.mp3')}', this)">🔊 Écouter Actuel</button>
        </div>
        """
        for voice_key, voice_label, voice_code, rate in VOICES:
            b64 = get_b64(os.path.join(OUTPUT_DIR, f"alif_{item_key}_{voice_key}.mp3"))
            is_rec = voice_key == "hamed"
            card_class = "card rec" if is_rec else "card"
            badge_class = "badge-rec" if is_rec else "badge-voice"
            badge_text = "Recommandé" if is_rec else voice_key.capitalize()
            html += f"""
        <div class="{card_class}">
          <div class="badge {badge_class}">{badge_text}</div>
          <div class="card-title">{voice_label}</div>
          <div class="card-sub">{voice_code}</div>
          <button class="play-btn" onclick="playAudio('data:audio/mp3;base64,{b64}', this)">🔊 Écouter</button>
        </div>
            """
        html += """
      </div>
    </div>
        """

    html += """
  </div>

  <script>
    let currentAudio = null;
    let currentBtn = null;

    function playAudio(src, btn) {
      if (currentAudio) {
        currentAudio.pause();
        if (currentBtn) currentBtn.classList.remove('playing');
      }
      currentAudio = new Audio(src);
      currentBtn = btn;
      btn.classList.add('playing');
      currentAudio.play().catch(e => console.error("Audio error:", e));
      currentAudio.onended = () => {
        btn.classList.remove('playing');
      };
    }
  </script>
</body>
</html>
"""
    with open("test_alif_vowels.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("test_alif_vowels.html generated successfully!")

async def main():
    await generate_audio()
    build_html()

if __name__ == "__main__":
    asyncio.run(main())
