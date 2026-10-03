import os
import base64

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return None

all_kasra_letters = [
    {"char": "إِ", "name": "Alif Kasrah", "sound": "'I", "type": "Voyelle pure", "file": "assets/audio/generated/alif_kasra.mp3", "color": "#38bdf8"},
    {"char": "بِ", "name": "Bā' Kasrah", "sound": "Bi", "type": "Labiale", "file": "assets/audio/generated/ba_kasra.mp3", "color": "#38bdf8"},
    {"char": "تِ", "name": "Tā' Kasrah", "sound": "Ti (Fin)", "type": "Dentale fine", "file": "assets/audio/generated/ta_kasra.mp3", "color": "#38bdf8"},
    {"char": "ثِ", "name": "Thā' Kasrah", "sound": "Thi", "type": "Interdentale", "file": "assets/audio/generated/tha_kasra.mp3", "color": "#38bdf8"},
    {"char": "جِ", "name": "Jeem Kasrah", "sound": "Dji (Shakir)", "type": "Palatale", "file": "assets/audio/generated/jeem_kasra.mp3", "color": "#f59e0b"},
    {"char": "حِ", "name": "Ḥā' Kasrah", "sound": "Ḥi", "type": "Pharyngale douce", "file": "assets/audio/generated/hha_kasra.mp3", "color": "#38bdf8"},
    {"char": "خِ", "name": "Khā' Kasrah", "sound": "Khi (Shakir)", "type": "Emphatique / Gutturale", "file": "assets/audio/generated/kha_kasra.mp3", "color": "#22c55e"},
    {"char": "دِ", "name": "Dāl Kasrah", "sound": "Di (Fin)", "type": "Dentale fine", "file": "assets/audio/generated/dal_kasra.mp3", "color": "#38bdf8"},
    {"char": "ذِ", "name": "Dhāl Kasrah", "sound": "Dhi", "type": "Interdentale", "file": "assets/audio/generated/dhal_kasra.mp3", "color": "#38bdf8"},
    {"char": "رِ", "name": "Rā' Kasrah", "sound": "Ri", "type": "Roulée fine", "file": "assets/audio/generated/ra_kasra.mp3", "color": "#38bdf8"},
    {"char": "زِ", "name": "Zāy Kasrah", "sound": "Zi", "type": "Sifflante sonore", "file": "assets/audio/generated/zay_kasra.mp3", "color": "#38bdf8"},
    {"char": "سِ", "name": "Sīn Kasrah", "sound": "Si (Fin)", "type": "Sifflante fine", "file": "assets/audio/generated/seen_kasra.mp3", "color": "#38bdf8"},
    {"char": "شِ", "name": "Shīn Kasrah", "sound": "Shi", "type": "Chuintante", "file": "assets/audio/generated/sheen_kasra.mp3", "color": "#38bdf8"},
    {"char": "صِ", "name": "Ṣād Kasrah", "sound": "Ṣi (Shakir)", "type": "Emphatique", "file": "assets/audio/generated/sad_kasra.mp3", "color": "#22c55e"},
    {"char": "ضِ", "name": "Ḍād Kasrah", "sound": "Ḍi (Shakir)", "type": "Emphatique", "file": "assets/audio/generated/dad_kasra.mp3", "color": "#22c55e"},
    {"char": "طِ", "name": "Ṭā' Kasrah", "sound": "Ṭi (Shakir)", "type": "Emphatique", "file": "assets/audio/generated/ttaa_kasra.mp3", "color": "#22c55e"},
    {"char": "ظِ", "name": "Ẓā' Kasrah", "sound": "Ẓi (Shakir)", "type": "Emphatique", "file": "assets/audio/generated/zha_kasra.mp3", "color": "#22c55e"},
    {"char": "عِ", "name": "ʿAyn Kasrah", "sound": "ʿI", "type": "Pharyngale profonde", "file": "assets/audio/generated/ayn_kasra.mp3", "color": "#38bdf8"},
    {"char": "غِ", "name": "Ghayn Kasrah", "sound": "Ghi (Shakir)", "type": "Emphatique", "file": "assets/audio/generated/ghayn_kasra.mp3", "color": "#22c55e"},
    {"char": "فِ", "name": "Fā' Kasrah", "sound": "Fi (Shakir)", "type": "Labio-dentale", "file": "assets/audio/generated/fa_kasra.mp3", "color": "#38bdf8"},
    {"char": "قِ", "name": "Qāf Kasrah", "sound": "Qi (Moaz)", "type": "Uvulaire profonde", "file": "assets/audio/generated/qaf_kasra.mp3", "color": "#22c55e"},
    {"char": "كِ", "name": "Kāf Kasrah", "sound": "Ki (Shakir)", "type": "Palatale fine", "file": "assets/audio/generated/kaf_kasra.mp3", "color": "#38bdf8"},
    {"char": "لِ", "name": "Lām Kasrah", "sound": "Li", "type": "Liquide", "file": "assets/audio/generated/lam_kasra.mp3", "color": "#38bdf8"},
    {"char": "مِ", "name": "Mīm Kasrah", "sound": "Mi", "type": "Nasale labiale", "file": "assets/audio/generated/meem_kasra.mp3", "color": "#38bdf8"},
    {"char": "نِ", "name": "Nūn Kasrah", "sound": "Ni (Amplifié)", "type": "Nasale dentale", "file": "assets/audio/generated/noon_kasra.mp3", "color": "#38bdf8"},
    {"char": "هِ", "name": "Hā' Kasrah", "sound": "Hi", "type": "Laryngale douce", "file": "assets/audio/generated/haa_kasra.mp3", "color": "#38bdf8"},
    {"char": "وِ", "name": "Wāw Kasrah", "sound": "Wi", "type": "Semi-voyelle", "file": "assets/audio/generated/waw_kasra.mp3", "color": "#38bdf8"},
    {"char": "يِ", "name": "Yā' Kasrah", "sound": "Yi", "type": "Semi-voyelle", "file": "assets/audio/generated/yaa_kasra.mp3", "color": "#38bdf8"},
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

kasra_cards = []
playlist_items = []
for idx, item in enumerate(all_kasra_letters):
    b64 = get_b64(item["file"])
    if b64:
        data_uri = f"data:audio/mp3;base64,{b64}"
        btn = f'<button id="btn-kasra-{idx}" class="play-btn" onclick="playAudio(\'{data_uri}\', this)">🔊 Écouter</button>'
        playlist_items.append(f"{{ id: 'btn-kasra-{idx}', src: '{data_uri}' }}")
    else:
        btn = '<button class="play-btn" style="background:#475569;" disabled>Absent</button>'
        
    badge_color = "#22c55e" if "Emphatique" in item["type"] else "#38bdf8"
    card = f'''        <div class="card" style="border-color:{item['color']};">
          <div class="badge" style="background:{badge_color}22; color:{badge_color}; border: 1px solid {badge_color}66;">{item['type']}</div>
          <div class="ar-word">{item['char']}</div>
          <div class="phonetic" style="color:#fcd34d;">{item['sound']}</div>
          <p style="font-size:12px; color:#94a3b8; margin-bottom:12px;">{item['name']}</p>
          {btn}
        </div>'''
    kasra_cards.append(card)

def render_simple_grid(items):
    cards = []
    for item in items:
        char, name, path = item
        b64 = get_b64(path)
        if b64:
            btn = f'<button class="play-btn" onclick="playAudio(\'data:audio/mp3;base64,{b64}\', this)">🔊 Écouter</button>'
        else:
            btn = '<button class="play-btn" style="background:#475569;" disabled>Absent</button>'
        cards.append(f'''        <div class="card">
          <div class="ar-word">{char}</div>
          <div class="phonetic">{name}</div>
          {btn}
        </div>''')
    return "\n".join(cards)

html = f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo — Console des 28 Sons avec Kasrah (Son "i")</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }}
    body {{ background: #0f172a; color: #f8fafc; padding: 30px 16px; display: flex; justify-content: center; }}
    .container {{ width: 100%; max-width: 1100px; }}
    header {{ text-align: center; margin-bottom: 24px; }}
    h1 {{ color: #38bdf8; font-size: 30px; margin-bottom: 8px; }}
    p.subtitle {{ color: #94a3b8; font-size: 15px; margin-bottom: 16px; }}

    .actions-bar {{ display: flex; gap: 12px; justify-content: center; margin-bottom: 24px; }}
    .action-btn {{ background: #0284c7; color: white; border: none; padding: 12px 24px; border-radius: 12px; font-size: 15px; font-weight: 800; cursor: pointer; transition: all 0.2s; display: flex; align-items: center; gap: 8px; box-shadow: 0 4px 14px rgba(2, 132, 199, 0.4); }}
    .action-btn:hover {{ background: #0369a1; transform: translateY(-1px); }}
    .action-btn.stop {{ background: #ef4444; box-shadow: 0 4px 14px rgba(239, 68, 68, 0.4); }}

    .highlight-box {{ background: #1e1b4b; border: 2px solid #818cf8; border-radius: 20px; padding: 22px; margin-bottom: 30px; }}
    .highlight-title {{ color: #38bdf8; font-size: 22px; font-weight: 800; margin-bottom: 6px; }}
    .highlight-desc {{ color: #c7d2fe; font-size: 14px; margin-bottom: 20px; }}

    .section-title {{ color: #a78bfa; font-size: 22px; font-weight: 800; margin: 36px 0 16px 0; border-bottom: 2px solid #334155; padding-bottom: 8px; display: flex; align-items: center; gap: 8px; }}
    .grid {{ display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 14px; }}
    .card {{ background: #1e293b; border: 2px solid #334155; border-radius: 16px; padding: 16px; text-align: center; transition: transform 0.1s, border-color 0.15s; position: relative; }}
    .card:hover {{ border-color: #38bdf8; transform: translateY(-2px); }}
    .badge {{ display: inline-block; font-size: 10px; font-weight: 800; text-transform: uppercase; padding: 3px 8px; border-radius: 20px; margin-bottom: 6px; }}
    .ar-word {{ font-family: 'Amiri', serif; font-size: 44px; font-weight: 700; color: #fde047; margin-bottom: 2px; line-height: 54px; }}
    .phonetic {{ font-size: 16px; font-weight: 800; color: #38bdf8; margin-bottom: 4px; }}
    .play-btn {{ width: 100%; background: #2563eb; color: white; border: none; padding: 10px; border-radius: 10px; font-size: 14px; font-weight: 800; cursor: pointer; transition: all 0.15s; }}
    .play-btn:hover {{ background: #3b82f6; }}
    .play-btn.playing {{ background: #10b981 !important; transform: scale(1.02); }}
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🎙️ Qalamo — Console des 28 Sons avec Kasrah (ـِ / "i")</h1>
      <p class="subtitle">Écoute et vérification directe de tout l'alphabet arabe avec la voyelle Kasrah</p>
      <div class="actions-bar">
        <button id="btn-play-all" class="action-btn" onclick="togglePlayAll()">▶️ Écouter les 28 Sons dans l'Ordre</button>
      </div>
    </header>

    <!-- SECTION PRINCIPALE DES 28 SONS AVEC KASRA -->
    <div class="highlight-box" style="border-color:#38bdf8; background:#0f172a;">
      <div class="highlight-title">💧 Les 28 Lettres avec Kasrah (Alif à Yaa)</div>
      <p class="highlight-desc">Clique sur n'importe quel son pour l'écouter instantanément ou lance la lecture automatique complète :</p>
      <div class="grid">
{chr(10).join(kasra_cards)}
      </div>
    </div>

    <div class="section-title">⚡ Voyelle Fatḥah (ـَ) — Les 28 Lettres</div>
    <div class="grid">
{render_simple_grid(fatha_items)}
    </div>

    <div class="section-title">🔔 Le Tanwīn (ـً ـٌ ـٍ)</div>
    <div class="grid">
{render_simple_grid(tanwin_items)}
    </div>
  </div>

  <script>
    let currentAudio = null;
    let currentButton = null;
    const playlist = [
      {",\n      ".join(playlist_items)}
    ];
    let isPlayingAll = false;
    let playlistIndex = 0;

    function playAudio(src, btn, onEndCallback) {{
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
        if (onEndCallback) onEndCallback();
      }};
    }}

    function togglePlayAll() {{
      const mainBtn = document.getElementById('btn-play-all');
      if (isPlayingAll) {{
        isPlayingAll = false;
        if (currentAudio) {{
          currentAudio.pause();
          currentAudio.currentTime = 0;
        }}
        if (currentButton) currentButton.classList.remove('playing');
        mainBtn.innerHTML = "▶️ Écouter les 28 Sons dans l'Ordre";
        mainBtn.classList.remove('stop');
      }} else {{
        isPlayingAll = true;
        playlistIndex = 0;
        mainBtn.innerHTML = "⏹️ Arrêter la Lecture";
        mainBtn.classList.add('stop');
        playNextInPlaylist();
      }}
    }}

    function playNextInPlaylist() {{
      if (!isPlayingAll || playlistIndex >= playlist.length) {{
        isPlayingAll = false;
        const mainBtn = document.getElementById('btn-play-all');
        mainBtn.innerHTML = "▶️ Écouter les 28 Sons dans l'Ordre";
        mainBtn.classList.remove('stop');
        return;
      }}

      const item = playlist[playlistIndex];
      const btn = document.getElementById(item.id);
      if (btn) {{
        btn.scrollIntoView({{ behavior: 'smooth', block: 'center' }});
      }}

      playAudio(item.src, btn, () => {{
        if (isPlayingAll) {{
          playlistIndex++;
          setTimeout(playNextInPlaylist, 600);
        }}
      }});
    }}
  </script>
</body>
</html>
'''

with open("test_audio.html", "w", encoding="utf-8") as f:
    f.write(html)

print("test_audio.html rebuilt with all 28 Kasrah sounds + Play All button!")
