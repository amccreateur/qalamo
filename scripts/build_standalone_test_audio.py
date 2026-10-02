import base64
import os
import sys

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')

def get_b64(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return f"data:audio/mp3;base64,{base64.b64encode(f.read()).decode('utf-8')}"
    return ""

html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo - Test Prononciation Tanwīn (-oun & -in)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    body {{ background: #0f172a; color: #f8fafc; padding: 30px 16px; display: flex; justify-content: center; }}
    .container {{ width: 100%; max-width: 960px; }}
    header {{ text-align: center; margin-bottom: 24px; }}
    h1 {{ color: #38bdf8; font-size: 26px; margin-bottom: 6px; }}
    p.subtitle {{ color: #94a3b8; font-size: 15px; margin-bottom: 12px; }}

    .card-box {{ background: #1e293b; border-radius: 20px; padding: 24px; margin-bottom: 24px; border: 1.5px solid #334155; }}
    .card-title {{ color: #38bdf8; font-size: 20px; font-weight: 800; margin-bottom: 14px; display: flex; align-items: center; gap: 8px; }}

    .tanwin-grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 16px; margin-bottom: 20px; }}
    .tanwin-card {{ background: #0f172a; border: 2px solid #334155; border-radius: 16px; padding: 18px; text-align: center; transition: all 0.2s; }}
    .tanwin-card:hover {{ border-color: #38bdf8; transform: translateY(-3px); }}

    .ar-word {{ font-family: 'Amiri', serif; font-size: 40px; font-weight: 700; color: #fde047; margin-bottom: 4px; line-height: 1.2; }}
    .phonetic {{ font-size: 16px; font-weight: 800; color: #38bdf8; margin-bottom: 4px; }}
    .desc {{ font-size: 13px; color: #94a3b8; margin-bottom: 14px; }}

    .play-btn {{ width: 100%; background: #0284c7; color: white; border: none; padding: 12px; border-radius: 12px; font-size: 15px; font-weight: 800; cursor: pointer; display: flex; align-items: center; justify-content: center; gap: 8px; transition: all 0.15s; margin-bottom: 8px; }}
    .play-btn:hover {{ background: #0ea5e9; }}
    .play-btn.playing {{ background: #10b981 !important; }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🎙️ Test Comparatif : Terminaisons -OUN et -IN</h1>
      <p class="subtitle">Écoutez les différentes versions phonétiques pour trouver la terminaison exacte</p>
    </header>

    <!-- SECTION 1 : KITABOUN (-OUN) -->
    <div class="card-box">
      <div class="card-title">📖 1. Prononciation de كِتَابٌ (Kitābun / -oun)</div>
      <div class="tanwin-grid">
        
        <div class="tanwin-card">
          <div class="ar-word">كِتَابٌ</div>
          <div class="phonetic">Kitāboon (Hamed)</div>
          <div class="desc">Phonétique continue avec terminaison -oon</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_phonetic_variations/kitaboon_hamed.mp3")}', this)">
            <span>🔊 Écouter (Hamed)</span>
          </button>
        </div>

        <div class="tanwin-card">
          <div class="ar-word">كِتَابٌ</div>
          <div class="phonetic">Kitāboon (Zariyah)</div>
          <div class="desc">Voix féminine avec terminaison -oon</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_phonetic_variations/kitaboon_zariyah.mp3")}', this)">
            <span>🔊 Écouter (Zariyah)</span>
          </button>
        </div>

        <div class="tanwin-card">
          <div class="ar-word">كِتَابٌ</div>
          <div class="phonetic">Kitāboon (Moaz)</div>
          <div class="desc">Voix masculine avec terminaison -oon</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_phonetic_variations/kitaboon_moaz.mp3")}', this)">
            <span>🔊 Écouter (Moaz)</span>
          </button>
        </div>

        <div class="tanwin-card">
          <div class="ar-word">كِتَابٌ</div>
          <div class="phonetic">Kitābu-N (Hamed)</div>
          <div class="desc">Syllabe Nūn détachée</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_phonetic_variations/kitabu_nun_hamed.mp3")}', this)">
            <span>🔊 Écouter (Kitabu-N)</span>
          </button>
        </div>

      </div>
    </div>

    <!-- SECTION 2 : KITABIN (-IN) -->
    <div class="card-box">
      <div class="card-title">📖 2. Prononciation de كِتَابٍ (Kitābin / -in)</div>
      <div class="tanwin-grid">
        
        <div class="tanwin-card">
          <div class="ar-word">كِتَابٍ</div>
          <div class="phonetic">Kitābeen (Hamed)</div>
          <div class="desc">Phonétique continue avec terminaison -een</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_phonetic_variations/kitabeen_hamed.mp3")}', this)">
            <span>🔊 Écouter (Hamed)</span>
          </button>
        </div>

        <div class="tanwin-card">
          <div class="ar-word">كِتَابٍ</div>
          <div class="phonetic">Kitābeen (Zariyah)</div>
          <div class="desc">Voix féminine avec terminaison -een</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_phonetic_variations/kitabeen_zariyah.mp3")}', this)">
            <span>🔊 Écouter (Zariyah)</span>
          </button>
        </div>

        <div class="tanwin-card">
          <div class="ar-word">كِتَابٍ</div>
          <div class="phonetic">Kitābeen (Moaz)</div>
          <div class="desc">Voix masculine avec terminaison -een</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_phonetic_variations/kitabeen_moaz.mp3")}', this)">
            <span>🔊 Écouter (Moaz)</span>
          </button>
        </div>

        <div class="tanwin-card">
          <div class="ar-word">كِتَابٍ</div>
          <div class="phonetic">Kitābi-N (Hamed)</div>
          <div class="desc">Syllabe Nūn détachée</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_phonetic_variations/kitabi_nun_hamed.mp3")}', this)">
            <span>🔊 Écouter (Kitabi-N)</span>
          </button>
        </div>

      </div>
    </div>

    <!-- SECTION 3 : KITABAN (-AN) POUR COMPARAISON -->
    <div class="card-box">
      <div class="card-title">📖 3. Référence : كِتَابًا (Kitāban / -an)</div>
      <div class="tanwin-grid">
        <div class="tanwin-card">
          <div class="ar-word">كِتَابًا</div>
          <div class="phonetic">Kitāban (Hamed)</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_voices_tanwin/Hamed_kitaban.mp3")}', this)">
            <span>🔊 Écouter Kitāban</span>
          </button>
        </div>
        <div class="tanwin-card">
          <div class="ar-word">كِتَابًا</div>
          <div class="phonetic">Kitāban (Zariyah)</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_voices_tanwin/Zariyah_kitaban.mp3")}', this)">
            <span>🔊 Écouter Kitāban</span>
          </button>
        </div>
      </div>
    </div>

  </div>

  <script>
    let globalAudio = null;

    function playAudio(base64Src, btn) {{
      if (!base64Src) {{
        alert("Fichier audio non trouvé");
        return;
      }}
      if (globalAudio) {{
        globalAudio.pause();
        globalAudio.currentTime = 0;
        document.querySelectorAll('.play-btn').forEach(b => b.classList.remove('playing'));
      }}
      globalAudio = new Audio(base64Src);
      btn.classList.add('playing');
      globalAudio.onended = () => btn.classList.remove('playing');
      globalAudio.play();
    }}
  </script>
</body>
</html>
"""

with open('test_audio.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("test_audio.html updated with phonetic comparison!")
