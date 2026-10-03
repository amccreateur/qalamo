import os
import base64

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

emphatic_letters = [
    ("طِ", "Ṭi (طِ — Ṭaa)", "assets/audio/generated/ttaa_kasra.mp3", "Emphatique pur, bien rond en bouche"),
    ("صِ", "Ṣi (صِ — Ṣaad)", "assets/audio/generated/sad_kasra.mp3", "Sifflement sourd et plein d'air"),
    ("ضِ", "Ḍi (ضِ — Ḍaad)", "assets/audio/generated/dad_kasra.mp3", "Impact latéral de la langue, grave"),
    ("ظِ", "Ẓi (ظِ — Ẓaa)", "assets/audio/generated/zha_kasra.mp3", "Interdentale sonore emphatique"),
    ("قِ", "Qi (قِ — Qāf)", "assets/audio/generated/qaf_kasra.mp3", "Claquement uvulaire net et clair (Moaz)"),
    ("خِ", "Khi (خِ — Khā')", "assets/audio/generated/kha_kasra.mp3", "Frottement guttural raclé"),
    ("غِ", "Ghi (غِ — Ghayn)", "assets/audio/generated/ghayn_kasra.mp3", "Vibration gutturale postérieure"),
]

dji_variations = [
    ("Shakir - Très Clair (-15%) ⭐ Actuel", "test_dji_long/dji_shakir_slow15.mp3"),
    ("Hamed - Posé (-20%)", "test_dji_long/dji_hamed_slow20.mp3"),
    ("Shakir - Plus Long (-25%)", "test_dji_long/dji_shakir_slow25.mp3"),
    ("Hamed - Plus Long (-30%)", "test_dji_long/dji_hamed_slow30.mp3"),
    ("Fahed - Golfe (-15%)", "test_dji_long/dji_fahed_slow15.mp3"),
]

kasra_items = [
    ("إِ", "Alif Kasra ('I)", "assets/audio/generated/alif_kasra.mp3"),
    ("بِ", "Ba Kasra (Bi)", "assets/audio/generated/ba_kasra.mp3"),
    ("تِ", "Ta Kasra (Ti - Fin)", "assets/audio/generated/ta_kasra.mp3"),
    ("ثِ", "Tha Kasra (Thi)", "assets/audio/generated/tha_kasra.mp3"),
    ("جِ", "Jeem Kasra (Dji - Shakir)", "assets/audio/generated/jeem_kasra.mp3"),
    ("حِ", "Ḥa Kasra (Ḥi)", "assets/audio/generated/hha_kasra.mp3"),
    ("خِ", "Kha Kasra (Khi - Shakir)", "assets/audio/generated/kha_kasra.mp3"),
    ("دِ", "Dal Kasra (Di - Fin)", "assets/audio/generated/dal_kasra.mp3"),
    ("ذِ", "Dhal Kasra (Dhi)", "assets/audio/generated/dhal_kasra.mp3"),
    ("رِ", "Ra Kasra (Ri)", "assets/audio/generated/ra_kasra.mp3"),
    ("زِ", "Zay Kasra (Zi)", "assets/audio/generated/zay_kasra.mp3"),
    ("سِ", "Seen Kasra (Si - Fin)", "assets/audio/generated/seen_kasra.mp3"),
    ("شِ", "Sheen Kasra (Shi)", "assets/audio/generated/sheen_kasra.mp3"),
    ("صِ", "Ṣad Kasra (Ṣi - Shakir)", "assets/audio/generated/sad_kasra.mp3"),
    ("ضِ", "Ḍad Kasra (Ḍi - Shakir)", "assets/audio/generated/dad_kasra.mp3"),
    ("طِ", "Ṭa Kasra (Ṭi - Shakir)", "assets/audio/generated/ttaa_kasra.mp3"),
    ("ظِ", "Ẓa Kasra (Ẓi - Shakir)", "assets/audio/generated/zha_kasra.mp3"),
    ("عِ", "ʿAyn Kasra (ʿI - Gorge)", "assets/audio/generated/ayn_kasra.mp3"),
    ("غِ", "Ghayn Kasra (Ghi - Shakir)", "assets/audio/generated/ghayn_kasra.mp3"),
    ("فِ", "Fa Kasra (Fi - Shakir)", "assets/audio/generated/fa_kasra.mp3"),
    ("قِ", "Qaf Kasra (Qi - Moaz)", "assets/audio/generated/qaf_kasra.mp3"),
    ("كِ", "Kaf Kasra (Ki - Fin)", "assets/audio/generated/kaf_kasra.mp3"),
    ("لِ", "Lam Kasra (Li)", "assets/audio/generated/lam_kasra.mp3"),
    ("مِ", "Meem Kasra (Mi)", "assets/audio/generated/meem_kasra.mp3"),
    ("نِ", "Noon Kasra (Ni - Amplifié)", "assets/audio/generated/noon_kasra.mp3"),
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

fatha_items = [
    ("أَ", "Alif Fatha (A)", "assets/audio/generated/alif_fatha.mp3"),
    ("بَ", "Ba Fatha (Ba)", "assets/audio/generated/ba_fatha.mp3"),
    ("تَ", "Ta Fatha (Ta)", "assets/audio/generated/ta_fatha.mp3"),
    ("ثَ", "Tha Fatha (Tha)", "assets/audio/generated/tha_fatha.mp3"),
    ("جَ", "Jeem Fatha (Dja)", "assets/audio/generated/jeem_fatha.mp3"),
    ("حَ", "Ḥa Fatha (Ḥa)", "assets/audio/generated/hha_fatha.mp3"),
    ("خَ", "Kha Fatha (Kha)", "assets/audio/generated/kha_fatha.mp3"),
    ("دَ", "Dal Fatha (Da)", "assets/audio/generated/dal_fatha.mp3"),
    ("ذَ", "Dhal Fatha (Dha)", "assets/audio/generated/dhal_fatha.mp3"),
    ("رَ", "Ra Fatha (Ra)", "assets/audio/generated/ra_fatha.mp3"),
    ("زَ", "Zay Fatha (Za)", "assets/audio/generated/zay_fatha.mp3"),
    ("سَ", "Seen Fatha (Sa)", "assets/audio/generated/seen_fatha.mp3"),
    ("شَ", "Sheen Fatha (Sha)", "assets/audio/generated/sheen_fatha.mp3"),
    ("صَ", "Ṣad Fatha (Ṣa)", "assets/audio/generated/sad_fatha.mp3"),
    ("ضَ", "Ḍad Fatha (Ḍa)", "assets/audio/generated/dad_fatha.mp3"),
    ("طَ", "Ṭa Fatha (Ṭa)", "assets/audio/generated/ttaa_fatha.mp3"),
    ("ظَ", "Ẓa Fatha (Ẓa)", "assets/audio/generated/zha_fatha.mp3"),
    ("عَ", "ʿAyn Fatha (ʿA)", "assets/audio/generated/ayn_fatha.mp3"),
    ("غَ", "Ghayn Fatha (Gha)", "assets/audio/generated/ghayn_fatha.mp3"),
    ("فَ", "Fa Fatha (Fa)", "assets/audio/generated/fa_fatha.mp3"),
    ("قَ", "Qaf Fatha (Qa)", "assets/audio/generated/qaf_fatha.mp3"),
    ("كَ", "Kaf Fatha (Ka)", "assets/audio/generated/kaf_fatha.mp3"),
    ("لَ", "Lam Fatha (La)", "assets/audio/generated/lam_fatha.mp3"),
    ("مَ", "Meem Fatha (Ma)", "assets/audio/generated/meem_fatha.mp3"),
    ("نَ", "Noon Fatha (Na)", "assets/audio/generated/noon_fatha.mp3"),
    ("هَ", "Haa Fatha (Ha)", "assets/audio/generated/haa_fatha.mp3"),
    ("وَ", "Waw Fatha (Wa)", "assets/audio/generated/waw_fatha.mp3"),
    ("يَ", "Yaa Fatha (Ya)", "assets/audio/generated/yaa_fatha.mp3"),
]

def render_grid(items):
    cards = []
    for item in items:
        if len(item) == 4:
            char, name, path, desc = item
            extra = f'<p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{desc}</p>'
        else:
            char, name, path = item
            extra = ''
            
        b64 = get_b64(path)
        if b64:
            btn = f'<button class="play-btn" onclick="playAudio(\'data:audio/mp3;base64,{b64}\', this)">🔊 Écouter</button>'
        else:
            btn = '<button class="play-btn" style="background:#475569;" disabled>Fichier absent</button>'
        cards.append(f'''        <div class="card">
          <div class="ar-word">{char}</div>
          <div class="phonetic">{name}</div>
          {extra}
          {btn}
        </div>''')
    return "\n".join(cards)

html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo - Console d'Écoute et Vérification Audio</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    body {{ background: #0f172a; color: #f8fafc; padding: 30px 16px; display: flex; justify-content: center; }}
    .container {{ width: 100%; max-width: 1050px; }}
    header {{ text-align: center; margin-bottom: 24px; }}
    h1 {{ color: #38bdf8; font-size: 28px; margin-bottom: 8px; }}
    p.subtitle {{ color: #94a3b8; font-size: 15px; }}

    .highlight-box {{ background: #1e1b4b; border: 2px solid #818cf8; border-radius: 20px; padding: 20px; margin-bottom: 30px; }}
    .highlight-title {{ color: #fcd34d; font-size: 20px; font-weight: 800; margin-bottom: 6px; }}
    .highlight-desc {{ color: #c7d2fe; font-size: 14px; margin-bottom: 16px; }}

    .section-title {{ color: #a78bfa; font-size: 22px; font-weight: 800; margin: 28px 0 14px 0; border-bottom: 2px solid #334155; padding-bottom: 8px; display: flex; align-items: center; gap: 8px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(220px, 1fr)); gap: 14px; }}
    .card {{ background: #1e293b; border: 2px solid #334155; border-radius: 16px; padding: 16px; text-align: center; transition: transform 0.1s, border-color 0.15s; }}
    .card:hover {{ border-color: #38bdf8; transform: translateY(-2px); }}
    .ar-word {{ font-family: 'Amiri', serif; font-size: 40px; font-weight: 700; color: #fde047; margin-bottom: 4px; line-height: 52px; }}
    .phonetic {{ font-size: 14px; font-weight: 800; color: #38bdf8; margin-bottom: 10px; }}
    .play-btn {{ width: 100%; background: #2563eb; color: white; border: none; padding: 10px; border-radius: 10px; font-size: 14px; font-weight: 800; cursor: pointer; transition: all 0.15s; }}
    .play-btn:hover {{ background: #3b82f6; }}
    .play-btn.playing {{ background: #10b981 !important; }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🎙️ Qalamo — Console de Vérification Audio</h1>
      <p class="subtitle">Écoute directe de tous les sons de l'application (0ms latence)</p>
    </header>

    <!-- SECTION SPECIAL LETTRES EMPHATIQUES KASRA -->
    <div class="highlight-box" style="border-color:#22c55e; background:#064e3b22;">
      <div class="highlight-title" style="color:#4ade80;">✨ Les 7 Lettres Emphatiques avec Kasrah (Shakir -15% — Net & Articulé)</div>
      <p class="highlight-desc">Toutes les 7 lettres d'emphase (حروف الاستعلاء) avec Kasrah ont été harmonisées avec la voix Shakir (-15%) pour une clarté et distinction parfaites :</p>
      <div class="grid">
{render_grid(emphatic_letters)}
      </div>
    </div>

    <!-- SECTION SPECIAL CHOIX DU SON DJI -->
    <div class="highlight-box">
      <div class="highlight-title">🎯 Choix du son « Dji » (جِ) — Versions Plus Longues & Claires</div>
      <p class="highlight-desc">La version Shakir (-15%) est actuellement active dans l'application :</p>
      <div class="grid">
{render_grid([("جِ", title, path) for title, path in dji_variations])}
      </div>
    </div>

    <div class="section-title">💧 Voyelle Kasrah (ـِ) — Les 28 Lettres</div>
    <div class="grid">
{render_grid(kasra_items)}
    </div>

    <div class="section-title">⚡ Voyelle Fatḥah (ـَ) — Les 28 Lettres</div>
    <div class="grid">
{render_grid(fatha_items)}
    </div>

    <div class="section-title">🔔 Le Tanwīn (ـً ـٌ ـٍ)</div>
    <div class="grid">
{render_grid(tanwin_items)}
    </div>
  </div>

  <script>
    let currentAudio = null;
    let currentButton = null;

    function playAudio(src, btn) {{
      if (currentAudio) {{
        currentAudio.pause();
        currentAudio.currentTime = 0;
        if (currentButton) currentButton.classList.remove('playing');
      }}

      if (btn) {{
        btn.classList.add('playing');
        currentButton = btn;
      }}

      currentAudio = new Audio(src);
      currentAudio.play().catch(e => console.error(e));
      currentAudio.onended = () => {{
        if (btn) btn.classList.remove('playing');
      }};
    }}
  </script>
</body>
</html>
'''

with open("test_audio.html", "w", encoding="utf-8") as f:
    f.write(html)

print("test_audio.html fully rebuilt!")
