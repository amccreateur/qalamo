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
  <title>Qalamo - Test Vocalisation des Verbes (Kataba)</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    body {{ background: #0f172a; color: #f8fafc; padding: 30px 16px; display: flex; justify-content: center; }}
    .container {{ width: 100%; max-width: 900px; }}
    header {{ text-align: center; margin-bottom: 24px; }}
    h1 {{ color: #38bdf8; font-size: 26px; margin-bottom: 6px; }}
    p.subtitle {{ color: #94a3b8; font-size: 15px; margin-bottom: 12px; }}

    .card-box {{ background: #1e293b; border-radius: 20px; padding: 24px; margin-bottom: 24px; border: 1.5px solid #334155; }}
    .card-title {{ color: #38bdf8; font-size: 20px; font-weight: 800; margin-bottom: 14px; }}

    .grid {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 16px; margin-bottom: 20px; }}
    .card {{ background: #0f172a; border: 2px solid #334155; border-radius: 16px; padding: 18px; text-align: center; }}
    .card:hover {{ border-color: #38bdf8; }}

    .ar-word {{ font-family: 'Amiri', serif; font-size: 42px; font-weight: 700; color: #fde047; margin-bottom: 4px; }}
    .phonetic {{ font-size: 16px; font-weight: 800; color: #38bdf8; margin-bottom: 4px; }}
    .desc {{ font-size: 13px; color: #94a3b8; margin-bottom: 14px; }}

    .play-btn {{ width: 100%; background: #0284c7; color: white; border: none; padding: 12px; border-radius: 12px; font-size: 15px; font-weight: 800; cursor: pointer; transition: all 0.15s; }}
    .play-btn:hover {{ background: #0ea5e9; }}
    .play-btn.playing {{ background: #10b981 !important; }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🎙️ Test Comparatif : كَتَبَ (Kataba vs Katab)</h1>
      <p class="subtitle">Comparaison de la prononciation du verbe avec et sans Fatḥah finale</p>
    </header>

    <div class="card-box">
      <div class="card-title">🔍 Comparaison directe du mot كَتَبَ</div>
      <div class="grid">
        
        <!-- ANCIEN : KATAB (AVEC SUKUN DE PAUSE) -->
        <div class="card" style="border-color:#ef4444;">
          <div class="ar-word">كَتَبَ</div>
          <div class="phonetic" style="color:#ef4444;">Katab (avec pause)</div>
          <div class="desc">La voix coupait la dernière lettre (Sukūn)</div>
          <button class="play-btn" style="background:#dc2626;" onclick="playAudio('{get_b64("test_verbs/kataba_std.mp3")}', this)">
            <span>🔊 Écouter l'ancien Katab</span>
          </button>
        </div>

        <!-- NOUVEAU : KATABA (AVEC FATHAH COMPLETE) -->
        <div class="card" style="border-color:#10b981;">
          <div class="ar-word">كَتَبَ</div>
          <div class="phonetic" style="color:#10b981;">Kataba (Vocalisé - Hamed)</div>
          <div class="desc">La Fatḥah finale (-ba) est 100% prononcée</div>
          <button class="play-btn" style="background:#059669;" onclick="playAudio('{get_b64("test_verbs/kataba_alif.mp3")}', this)">
            <span>🔊 Écouter le vrai Kataba (Hamed)</span>
          </button>
        </div>

        <!-- NOUVEAU : KATABA (ZARIYAH) -->
        <div class="card" style="border-color:#38bdf8;">
          <div class="ar-word">كَتَبَ</div>
          <div class="phonetic" style="color:#38bdf8;">Kataba (Vocalisé - Zariyah)</div>
          <div class="desc">Version voix féminine claire</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_verbs/kataba_zariyah_alif.mp3")}', this)">
            <span>🔊 Écouter le vrai Kataba (Zariyah)</span>
          </button>
        </div>

      </div>
    </div>

    <!-- AUTRES VERBES VOCALISES -->
    <div class="card-box">
      <div class="card-title">📚 Autres verbes avec voyelle finale complète (-a)</div>
      <div class="grid">
        
        <div class="card">
          <div class="ar-word">دَرَسَ</div>
          <div class="phonetic">Darasa</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_verbs/darasa_alif.mp3")}', this)">
            <span>🔊 Écouter Darasa</span>
          </button>
        </div>

        <div class="card">
          <div class="ar-word">جَلَسَ</div>
          <div class="phonetic">Jalasa</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_verbs/jalasa_alif.mp3")}', this)">
            <span>🔊 Écouter Jalasa</span>
          </button>
        </div>

        <div class="card">
          <div class="ar-word">قَرَأَ</div>
          <div class="phonetic">Qara'a</div>
          <button class="play-btn" onclick="playAudio('{get_b64("test_verbs/qaraa_alif.mp3")}', this)">
            <span>🔊 Écouter Qara'a</span>
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

print("test_audio.html updated with verb vocalization comparison!")
