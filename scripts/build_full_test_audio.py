import os
import base64

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

kasra_items = [
    ("إِ", "Alif Kasra ('I)", "assets/audio/generated/alif_kasra.mp3"),
    ("بِ", "Ba Kasra (Bi)", "assets/audio/generated/ba_kasra.mp3"),
    ("تِ", "Ta Kasra (Ti)", "assets/audio/generated/ta_kasra.mp3"),
    ("ثِ", "Tha Kasra (Thi)", "assets/audio/generated/tha_kasra.mp3"),
    ("جِ", "Jeem Kasra (Dji) ⭐ Corrigé", "assets/audio/generated/jeem_kasra.mp3"),
    ("حِ", "Ḥa Kasra (Ḥi)", "assets/audio/generated/hha_kasra.mp3"),
    ("خِ", "Kha Kasra (Khi)", "assets/audio/generated/kha_kasra.mp3"),
    ("دِ", "Dal Kasra (Di)", "assets/audio/generated/dal_kasra.mp3"),
    ("ذِ", "Dhal Kasra (Dhi)", "assets/audio/generated/dhal_kasra.mp3"),
    ("رِ", "Ra Kasra (Ri)", "assets/audio/generated/ra_kasra.mp3"),
    ("زِ", "Zay Kasra (Zi)", "assets/audio/generated/zay_kasra.mp3"),
    ("سِ", "Seen Kasra (Si)", "assets/audio/generated/seen_kasra.mp3"),
    ("شِ", "Sheen Kasra (Shi)", "assets/audio/generated/sheen_kasra.mp3"),
    ("صِ", "Ṣad Kasra (Ṣi - Emphatique)", "assets/audio/generated/sad_kasra.mp3"),
    ("ضِ", "Ḍad Kasra (Ḍi - Emphatique)", "assets/audio/generated/dad_kasra.mp3"),
    ("طِ", "Ṭa Kasra (Ṭi - Emphatique)", "assets/audio/generated/ttaa_kasra.mp3"),
    ("ظِ", "Ẓa Kasra (Ẓi - Emphatique)", "assets/audio/generated/zha_kasra.mp3"),
    ("عِ", "ʿAyn Kasra (ʿI - Gorge)", "assets/audio/generated/ayn_kasra.mp3"),
    ("غِ", "Ghayn Kasra (Ghi)", "assets/audio/generated/ghayn_kasra.mp3"),
    ("فِ", "Fa Kasra (Fi)", "assets/audio/generated/fa_kasra.mp3"),
    ("قِ", "Qaf Kasra (Qi - Fond palais)", "assets/audio/generated/qaf_kasra.mp3"),
    ("كِ", "Kaf Kasra (Ki)", "assets/audio/generated/kaf_kasra.mp3"),
    ("لِ", "Lam Kasra (Li)", "assets/audio/generated/lam_kasra.mp3"),
    ("مِ", "Meem Kasra (Mi)", "assets/audio/generated/meem_kasra.mp3"),
    ("نِ", "Noon Kasra (Ni) ⭐ Amplifié", "assets/audio/generated/noon_kasra.mp3"),
    ("هِ", "Haa Kasra (Hi)", "assets/audio/generated/haa_kasra.mp3"),
    ("وِ", "Waw Kasra (Wi)", "assets/audio/generated/waw_kasra.mp3"),
    ("يِ", "Yaa Kasra (Yi)", "assets/audio/generated/yaa_kasra.mp3"),
]

tanwin_items = [
    ("كِتَابًا", "Kitāban (Tanwīn Fatḥah -an)", "assets/audio/generated/kitaban.mp3"),
    ("كِتَابٌ", "Kitābun (Tanwīn Ḍammah -oun)", "assets/audio/generated/kitabun.mp3"),
    ("كِتَابٍ", "Kitābin (Tanwīn Kasrah -in)", "assets/audio/generated/kitabin.mp3"),
    ("وَلَدًا", "Waladan (-an)", "assets/audio/generated/waladan.mp3"),
    ("وَلَدٌ", "Waladun (-oun)", "assets/audio/generated/waladun.mp3"),
    ("وَلَدٍ", "Waladin (-in)", "assets/audio/generated/waladin.mp3"),
    ("بَيْتًا", "Baytan (-an)", "assets/audio/generated/baytan.mp3"),
    ("بَيْتٌ", "Baytun (-oun)", "assets/audio/generated/baytun.mp3"),
    ("بَيْتٍ", "Baytin (-in)", "assets/audio/generated/baytin.mp3"),
]

verb_items = [
    ("كَتَبَ", "Kataba (Fatḥah finale -ba prononcée)", "assets/audio/generated/kataba.mp3"),
    ("دَرَسَ", "Darasa (Fatḥah finale -sa prononcée)", "assets/audio/generated/darasa.mp3"),
    ("قَرَأَ", "Qara'a (Fatḥah finale prononcée)", "assets/audio/generated/qaraa.mp3"),
    ("جَلَسَ", "Jalasa (Fatḥah finale prononcée)", "assets/audio/generated/jalasa.mp3"),
    ("رَسَمَ", "Rasama (Fatḥah finale prononcée)", "assets/audio/generated/rasama.mp3"),
]

html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo - Console d'Écoute et Vérification Audio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background: #0f172a; color: #f8fafc; padding: 30px 16px; display: flex; justify-content: center; }
    .container { width: 100%; max-width: 1050px; }
    header { text-align: center; margin-bottom: 30px; }
    h1 { color: #38bdf8; font-size: 28px; margin-bottom: 8px; }
    p.subtitle { color: #94a3b8; font-size: 15px; }
    .section-title { color: #a78bfa; font-size: 22px; font-weight: 800; margin: 28px 0 14px 0; border-bottom: 2px solid #334155; padding-bottom: 8px; display: flex; align-items: center; gap: 8px; }
    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }
    .card { background: #1e293b; border: 2px solid #334155; border-radius: 16px; padding: 16px; text-align: center; transition: transform 0.1s, border-color 0.15s; }
    .card:hover { border-color: #38bdf8; transform: translateY(-2px); }
    .ar-word { font-family: 'Amiri', serif; font-size: 40px; font-weight: 700; color: #fde047; margin-bottom: 4px; line-height: 52px; }
    .phonetic { font-size: 14px; font-weight: 800; color: #38bdf8; margin-bottom: 10px; }
    .play-btn { width: 100%; background: #2563eb; color: white; border: none; padding: 10px; border-radius: 10px; font-size: 14px; font-weight: 800; cursor: pointer; transition: all 0.15s; }
    .play-btn:hover { background: #3b82f6; }
    .play-btn.playing { background: #10b981 !important; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🎙️ Qalamo — Console de Vérification Audio</h1>
      <p class="subtitle">Écoute directe de tous les sons de l'application (Hamed Studio / 0ms latence)</p>
    </header>

    <div class="section-title">✨ 1. Les 28 Sons de la Kasrah (ـِ) — Exercice 23 & 24</div>
    <div class="grid">
"""

for ar, desc, path in kasra_items:
    b64 = get_b64(path)
    if b64:
        html += f"""      <div class="card">
        <div class="ar-word">{ar}</div>
        <div class="phonetic">{desc}</div>
        <button class="play-btn" onclick="playAudio('data:audio/mp3;base64,{b64}', this)">🔊 Écouter</button>
      </div>\n"""

html += """    </div>

    <div class="section-title">✨ 2. Les 3 Tanwīns (-an, -oun, -in) — Monde 5</div>
    <div class="grid">
"""

for ar, desc, path in tanwin_items:
    b64 = get_b64(path)
    if b64:
        html += f"""      <div class="card" style="border-color:#e11d48;">
        <div class="ar-word">{ar}</div>
        <div class="phonetic" style="color:#fb7185;">{desc}</div>
        <button class="play-btn" style="background:#be123c;" onclick="playAudio('data:audio/mp3;base64,{b64}', this)">🔊 Écouter</button>
      </div>\n"""

html += """    </div>

    <div class="section-title">✨ 3. Les Verbes avec Fatḥah Finale (Sans Waqf) — Monde 6</div>
    <div class="grid">
"""

for ar, desc, path in verb_items:
    b64 = get_b64(path)
    if b64:
        html += f"""      <div class="card" style="border-color:#10b981;">
        <div class="ar-word">{ar}</div>
        <div class="phonetic" style="color:#34d399;">{desc}</div>
        <button class="play-btn" style="background:#059669;" onclick="playAudio('data:audio/mp3;base64,{b64}', this)">🔊 Écouter</button>
      </div>\n"""

html += """    </div>
  </div>

  <script>
    let currentAudio = null;
    let currentBtn = null;

    function playAudio(dataUri, btn) {
      if (currentAudio) {
        currentAudio.pause();
        if (currentBtn) currentBtn.classList.remove('playing');
      }

      currentAudio = new Audio(dataUri);
      currentBtn = btn;
      btn.classList.add('playing');

      currentAudio.play().catch(e => console.error("Playback error:", e));

      currentAudio.onended = () => {
        btn.classList.remove('playing');
        currentAudio = null;
        currentBtn = null;
      };
    }
  </script>
</body>
</html>
"""

with open("test_audio.html", "w", encoding="utf-8") as f:
    f.write(html)

print("test_audio.html successfully written!")
