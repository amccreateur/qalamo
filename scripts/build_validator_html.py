import os
import base64

def get_b64(path):
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ''

words = [
    {
        'title': 'بَبُ (Ba - Bou) — Série Fatḥah + Ḍammah',
        'wordAr': 'بَبُ',
        'desc': 'Le son "OU" final doit être distinct et complet sans être coupé en Sukūn (Waqf)',
        'variants': [
            {'label': '1. Hamed (Direct)', 'sub': 'ar-SA-Hamed | بَبُ', 'file': 'scripts/test_proposals/babu_direct.mp3', 'badge': 'Standard'},
            {'label': '2. Hamed (Syllabé)', 'sub': 'ar-SA-Hamed | بَ بُ (évite le waqf)', 'file': 'scripts/test_proposals/babu_spaced.mp3', 'badge': 'Recommandé'},
            {'label': '3. Hamed (Virgule)', 'sub': 'ar-SA-Hamed | بَبُ،', 'file': 'scripts/test_proposals/babu_comma.mp3', 'badge': 'Wasl'},
            {'label': '4. Shakir (Égypte)', 'sub': 'ar-EG-Shakir | Articulation ferme', 'file': 'scripts/test_proposals/babu_shakir.mp3', 'badge': 'Égypte'},
            {'label': '5. Hedi (Tunisie)', 'sub': 'ar-TN-Hedi | Attaque nette', 'file': 'scripts/test_proposals/babu_hedi.mp3', 'badge': 'Tunisie'},
            {'label': '6. Moaz (Qatar)', 'sub': 'ar-QA-Moaz | Posé', 'file': 'scripts/test_proposals/babu_moaz.mp3', 'badge': 'Qatar'},
            {'label': '7. Zariyah (Féminine)', 'sub': 'ar-SA-Zariyah | Voix claire', 'file': 'scripts/test_proposals/babu_zariyah.mp3', 'badge': 'Féminin'},
        ]
    },
    {
        'title': 'كَتُ (Ka - Tou) — Série Fatḥah + Ḍammah',
        'wordAr': 'كَتُ',
        'desc': 'Le son "Tou" final doit être bien audible sans amortissement',
        'variants': [
            {'label': '1. Hamed (Direct)', 'sub': 'ar-SA-Hamed | كَتُ', 'file': 'scripts/test_proposals/katu_direct.mp3', 'badge': 'Standard'},
            {'label': '2. Hamed (Syllabé)', 'sub': 'ar-SA-Hamed | كَ تُ', 'file': 'scripts/test_proposals/katu_spaced.mp3', 'badge': 'Recommandé'},
            {'label': '3. Hamed (Virgule)', 'sub': 'ar-SA-Hamed | كَتُ،', 'file': 'scripts/test_proposals/katu_comma.mp3', 'badge': 'Wasl'},
            {'label': '4. Shakir (Égypte)', 'sub': 'ar-EG-Shakir | Ferme', 'file': 'scripts/test_proposals/katu_shakir.mp3', 'badge': 'Égypte'},
            {'label': '5. Hedi (Tunisie)', 'sub': 'ar-TN-Hedi | Net', 'file': 'scripts/test_proposals/katu_hedi.mp3', 'badge': 'Tunisie'},
            {'label': '6. Moaz (Qatar)', 'sub': 'ar-QA-Moaz | Posé', 'file': 'scripts/test_proposals/katu_moaz.mp3', 'badge': 'Qatar'},
            {'label': '7. Zariyah (Féminine)', 'sub': 'ar-SA-Zariyah | Féminin', 'file': 'scripts/test_proposals/katu_zariyah.mp3', 'badge': 'Féminin'},
        ]
    },
    {
        'title': 'بَتَ (Ba - Ta) — Série Fatḥah + Fatḥah',
        'wordAr': 'بَتَ',
        'desc': 'Enchaînement de 2 Fatḥah vives',
        'variants': [
            {'label': '1. Hamed (Direct)', 'sub': 'ar-SA-Hamed | بَتَ', 'file': 'scripts/test_proposals/bata_direct.mp3', 'badge': 'Standard'},
            {'label': '2. Hamed (Syllabé)', 'sub': 'ar-SA-Hamed | بَ تَ', 'file': 'scripts/test_proposals/bata_spaced.mp3', 'badge': 'Recommandé'},
            {'label': '3. Hamed (Virgule)', 'sub': 'ar-SA-Hamed | بَتَ،', 'file': 'scripts/test_proposals/bata_comma.mp3', 'badge': 'Wasl'},
            {'label': '4. Shakir (Égypte)', 'sub': 'ar-EG-Shakir | Ferme', 'file': 'scripts/test_proposals/bata_shakir.mp3', 'badge': 'Égypte'},
            {'label': '5. Zariyah (Féminine)', 'sub': 'ar-SA-Zariyah | Féminin', 'file': 'scripts/test_proposals/bata_zariyah.mp3', 'badge': 'Féminin'},
        ]
    },
    {
        'title': 'بَرِ (Ba - Ri) — Série Fatḥah + Kasrah',
        'wordAr': 'بَرِ',
        'desc': 'La Kasrah "Ri" finale doit sonner pleinement',
        'variants': [
            {'label': '1. Hamed (Direct)', 'sub': 'ar-SA-Hamed | بَرِ', 'file': 'scripts/test_proposals/bari_direct.mp3', 'badge': 'Standard'},
            {'label': '2. Hamed (Syllabé)', 'sub': 'ar-SA-Hamed | بَ رِ', 'file': 'scripts/test_proposals/bari_spaced.mp3', 'badge': 'Recommandé'},
            {'label': '3. Hamed (Virgule)', 'sub': 'ar-SA-Hamed | بَرِ،', 'file': 'scripts/test_proposals/bari_comma.mp3', 'badge': 'Wasl'},
            {'label': '4. Shakir (Égypte)', 'sub': 'ar-EG-Shakir | Ferme', 'file': 'scripts/test_proposals/bari_shakir.mp3', 'badge': 'Égypte'},
            {'label': '5. Hedi (Tunisie)', 'sub': 'ar-TN-Hedi | Net', 'file': 'scripts/test_proposals/bari_hedi.mp3', 'badge': 'Tunisie'},
            {'label': '6. Zariyah (Féminine)', 'sub': 'ar-SA-Zariyah | Féminin', 'file': 'scripts/test_proposals/bari_zariyah.mp3', 'badge': 'Féminin'},
        ]
    },
    {
        'title': 'كُتِ (Kou - Ti) — Série Ḍammah + Kasrah',
        'wordAr': 'كُتِ',
        'desc': 'Le passage de "Kou" à "Ti" distincts',
        'variants': [
            {'label': '1. Hamed (Direct)', 'sub': 'ar-SA-Hamed | كُتِ', 'file': 'scripts/test_proposals/kuti_direct.mp3', 'badge': 'Standard'},
            {'label': '2. Hamed (Syllabé)', 'sub': 'ar-SA-Hamed | كُ تِ', 'file': 'scripts/test_proposals/kuti_spaced.mp3', 'badge': 'Recommandé'},
            {'label': '3. Hamed (Virgule)', 'sub': 'ar-SA-Hamed | كُتِ،', 'file': 'scripts/test_proposals/kuti_comma.mp3', 'badge': 'Wasl'},
            {'label': '4. Shakir (Égypte)', 'sub': 'ar-EG-Shakir | Ferme', 'file': 'scripts/test_proposals/kuti_shakir.mp3', 'badge': 'Égypte'},
            {'label': '5. Zariyah (Féminine)', 'sub': 'ar-SA-Zariyah | Féminin', 'file': 'scripts/test_proposals/kuti_zariyah.mp3', 'badge': 'Féminin'},
        ]
    },
    {
        'title': 'هُوَ (Hou - Wa) — Série Ḍammah + Fatḥah',
        'wordAr': 'هُوَ',
        'desc': 'Prononciation fluide du pronom "Il"',
        'variants': [
            {'label': '1. Hamed (Direct)', 'sub': 'ar-SA-Hamed | هُوَ', 'file': 'scripts/test_proposals/huwa_direct.mp3', 'badge': 'Standard'},
            {'label': '2. Hamed (Syllabé)', 'sub': 'ar-SA-Hamed | هُ وَ', 'file': 'scripts/test_proposals/huwa_spaced.mp3', 'badge': 'Recommandé'},
            {'label': '3. Shakir (Égypte)', 'sub': 'ar-EG-Shakir | Ferme', 'file': 'scripts/test_proposals/huwa_shakir.mp3', 'badge': 'Égypte'},
            {'label': '4. Hedi (Tunisie)', 'sub': 'ar-TN-Hedi | Net', 'file': 'scripts/test_proposals/huwa_hedi.mp3', 'badge': 'Tunisie'},
        ]
    },
    {
        'title': 'هِيَ (Hi - Ya) — Série Kasrah + Fatḥah',
        'wordAr': 'هِيَ',
        'desc': 'Prononciation fluide du pronom "Elle"',
        'variants': [
            {'label': '1. Hamed (Direct)', 'sub': 'ar-SA-Hamed | هِيَ', 'file': 'scripts/test_proposals/hiya_direct.mp3', 'badge': 'Standard'},
            {'label': '2. Hamed (Syllabé)', 'sub': 'ar-SA-Hamed | هِ يَ', 'file': 'scripts/test_proposals/hiya_spaced.mp3', 'badge': 'Recommandé'},
            {'label': '3. Shakir (Égypte)', 'sub': 'ar-EG-Shakir | Ferme', 'file': 'scripts/test_proposals/hiya_shakir.mp3', 'badge': 'Égypte'},
            {'label': '4. Hedi (Tunisie)', 'sub': 'ar-TN-Hedi | Net', 'file': 'scripts/test_proposals/hiya_hedi.mp3', 'badge': 'Tunisie'},
        ]
    }
]

html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo — Console de Validation des Sons à 2 Voyelles</title>
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
    
    .guide-banner { background: #1e1b4b; border: 2px solid #818cf8; border-radius: 16px; padding: 18px; margin-bottom: 28px; font-size: 14px; line-height: 1.6; color: #c7d2fe; }
    .guide-banner b { color: #fde047; }

    .section { background: #131d31; border: 2px solid #1e293b; border-radius: 20px; padding: 22px; margin-bottom: 28px; }
    .section-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1px solid #334155; padding-bottom: 10px; }
    .section-title { font-size: 20px; font-weight: 800; color: #f59e0b; display: flex; align-items: center; gap: 10px; }
    .section-word { font-family: 'Amiri', serif; font-size: 36px; font-weight: 700; color: #fde047; }
    .section-desc { font-size: 13px; color: #94a3b8; margin-bottom: 16px; }

    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 14px; }
    .card { background: #0b0f19; border: 2px solid #334155; border-radius: 16px; padding: 16px; text-align: center; transition: all 0.15s; }
    .card:hover { border-color: #38bdf8; transform: translateY(-2px); }
    .card.recommended { border-color: #10b981; background: #064e3b15; }

    .badge { display: inline-block; font-size: 11px; font-weight: 800; text-transform: uppercase; padding: 3px 8px; border-radius: 12px; margin-bottom: 8px; }
    .badge-std { background: #334155; color: #94a3b8; }
    .badge-rec { background: #10b98122; color: #34d399; border: 1px solid #10b98166; }
    .badge-eg { background: #f59e0b22; color: #fbbf24; border: 1px solid #f59e0b66; }
    .badge-tn { background: #a855f722; color: #c084fc; border: 1px solid #a855f766; }

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
      <h1>🎙️ Validation des Sons à 2 Voyelles Courtes</h1>
      <p class="subtitle">Comparatif direct des solutions pour que la 2ème voyelle soit 100% nette et complète</p>
    </header>

    <div class="guide-banner">
      💡 <b>Pourquoi la 2ème voyelle paraissait coupée / atténuée ?</b><br>
      En arabe standard (TTS), un mot prononcé isolément subit automatiquement la règle phonétique du <b>Waqf</b> (la dernière voyelle courte s'atténue en silence / Sukūn).<br>
      Pour entendre la 2ème voyelle avec <b>une clarté totale et un tempo régulier</b>, compare les options ci-dessous :
      <ul style="margin-left: 20px; margin-top: 8px;">
        <li><b>Option 2 (Syllabé) :</b> Généré en syllabes liées (ex: <code>بَ بُ</code>) -> neutralise le Waqf et donne 2 temps égaux et nets.</li>
        <li><b>Option 4 & 5 (Shakir / Hedi) :</b> Moteurs à attaque plus percutante.</li>
      </ul>
    </div>
"""

for w in words:
    html += f"""
    <div class="section">
      <div class="section-header">
        <div class="section-title">
          <span>{w['title']}</span>
        </div>
        <div class="section-word">{w['wordAr']}</div>
      </div>
      <div class="section-desc">{w['desc']}</div>
      <div class="grid">
    """
    for v in w['variants']:
        b64 = get_b64(v['file'])
        badge_class = 'badge-rec' if 'Recommandé' in v['badge'] else ('badge-eg' if 'Égypte' in v['badge'] else ('badge-tn' if 'Tunisie' in v['badge'] else 'badge-std'))
        card_class = 'card recommended' if 'Recommandé' in v['badge'] else 'card'
        html += f"""
        <div class="{card_class}">
          <div class="badge {badge_class}">{v['badge']}</div>
          <div class="card-title">{v['label']}</div>
          <div class="card-sub">{v['sub']}</div>
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

with open('test_two_vowels_validator.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Generated test_two_vowels_validator.html successfully!')
