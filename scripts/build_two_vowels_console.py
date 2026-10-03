import os
import base64

def get_b64(name):
    path = f'assets/audio/generated/{name}.mp3'
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ''

sections = [
    {
        'title': '1. Série A + A (Fatḥah — Fatḥah)',
        'badge': 'Niveau 27',
        'items': [
            ('bata', 'بَتَ', 'بَ + تَ', 'Combinaison A + A'),
            ('dara', 'دَرَ', 'دَ + رَ', 'Combinaison A + A'),
            ('kata', 'كَتَ', 'كَ + تَ', 'Combinaison A + A'),
            ('sama', 'سَمَ', 'سَ + مَ', 'Combinaison A + A'),
            ('rasa', 'رَسَ', 'رَ + سَ', 'Combinaison A + A'),
            ('maa_particle', 'مَعَ', 'مَ + عَ', 'Mot "Avec"'),
            ('laka', 'لَكَ', 'لَ + كَ', 'Mot "Pour toi"'),
        ]
    },
    {
        'title': '2. Série A + OU (Fatḥah — Ḍammah)',
        'badge': 'Niveau 28',
        'items': [
            ('babu', 'بَبُ', 'بَ + بُ', 'Combinaison A + OU'),
            ('katu', 'كَتُ', 'كَ + تُ', 'Combinaison A + OU'),
            ('daru', 'دَرُ', 'دَ + رُ', 'Combinaison A + OU'),
            ('samu', 'سَمُ', 'سَ + مُ', 'Combinaison A + OU'),
            ('qatu', 'قَتُ', 'قَ + تُ', 'Combinaison A + OU'),
            ('nabu', 'نَبُ', 'نَ + بُ', 'Combinaison A + OU'),
            ('tadu', 'تَدُ', 'تَ + دُ', 'Combinaison A + OU'),
        ]
    },
    {
        'title': '3. Série A + I (Fatḥah — Kasrah)',
        'badge': 'Niveau 29',
        'items': [
            ('bari', 'بَرِ', 'بَ + رِ', 'Combinaison A + I'),
            ('dari', 'دَرِ', 'دَ + رِ', 'Combinaison A + I'),
            ('sami_short', 'سَمِ', 'سَ + مِ', 'Combinaison A + I'),
            ('kati', 'كَتِ', 'كَ + تِ', 'Combinaison A + I'),
            ('shari_short', 'شَرِ', 'شَ + رِ', 'Combinaison A + I'),
            ('ali_short', 'عَلِ', 'عَ + لِ', 'Combinaison A + I'),
        ]
    },
    {
        'title': '4. Série OU + I (Ḍammah — Kasrah)',
        'badge': 'Niveau 30',
        'items': [
            ('kuti', 'كُتِ', 'كُ + تِ', 'Combinaison OU + I'),
            ('quri', 'قُرِ', 'قُ + رِ', 'Combinaison OU + I'),
            ('sumi', 'سُمِ', 'سُ + مِ', 'Combinaison OU + I'),
            ('duri', 'دُرِ', 'دُ + رِ', 'Combinaison OU + I'),
            ('rusi', 'رُسِ', 'رُ + سِ', 'Combinaison OU + I'),
        ]
    },
    {
        'title': '5. Série OU + A (Ḍammah — Fatḥah)',
        'badge': 'Niveau 30',
        'items': [
            ('huwa', 'هُوَ', 'هُ + وَ', 'Pronom "Il"'),
            ('ruba', 'رُبَ', 'رُ + بَ', 'Mot "Peut-être"'),
            ('kuta', 'كُتَ', 'كُ + تَ', 'Combinaison OU + A'),
            ('dura', 'دُرَ', 'دُ + رَ', 'Combinaison OU + A'),
            ('sura', 'سُرَ', 'سُ + رَ', 'Combinaison OU + A'),
        ]
    },
    {
        'title': '6. Série I + A (Kasrah — Fatḥah)',
        'badge': 'Niveau 31',
        'items': [
            ('hiya', 'هِيَ', 'هِ + يَ', 'Pronom "Elle"'),
            ('lima', 'لِمَ', 'لِ + مَ', 'Mot "Pourquoi"'),
            ('bika', 'بِكَ', 'بِ + كَ', 'Mot "Par toi"'),
            ('bita', 'بِتَ', 'بِ + تَ', 'Combinaison I + A'),
            ('dina', 'دِنَ', 'دِ + نَ', 'Combinaison I + A'),
            ('sima', 'سِمَ', 'سِ + مَ', 'Combinaison I + A'),
        ]
    }
]

html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo — Monde 4 : Combinaisons de 2 Voyelles Courtes</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background: #0b0f19; color: #f8fafc; padding: 30px 16px; display: flex; justify-content: center; }
    .container { width: 100%; max-width: 1050px; }
    header { text-align: center; margin-bottom: 28px; }
    h1 { color: #f59e0b; font-size: 28px; margin-bottom: 8px; }
    p.subtitle { color: #94a3b8; font-size: 15px; margin-bottom: 20px; }

    .category-section { background: #131d31; border: 2px solid #1e293b; border-radius: 20px; padding: 20px; margin-bottom: 24px; }
    .category-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; border-bottom: 1px solid #334155; padding-bottom: 10px; }
    .category-title { color: #38bdf8; font-size: 20px; font-weight: 800; }
    .category-badge { background: #f59e0b22; color: #f59e0b; border: 1px solid #f59e0b66; font-size: 11px; font-weight: 800; text-transform: uppercase; padding: 4px 10px; border-radius: 20px; }

    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(190px, 1fr)); gap: 14px; }
    .card { background: #0b0f19; border: 2px solid #334155; border-radius: 16px; padding: 14px; text-align: center; transition: transform 0.15s, border-color 0.15s; }
    .card:hover { border-color: #f59e0b; transform: translateY(-2px); }
    
    .ar-word { font-family: 'Amiri', serif; font-size: 42px; font-weight: 700; color: #fde047; margin-bottom: 2px; line-height: 52px; }
    .phonetic { font-size: 18px; font-weight: 700; color: #38bdf8; margin-bottom: 4px; font-family: 'Amiri', serif; }
    .meaning { font-size: 13px; color: #94a3b8; margin-bottom: 12px; }
    .play-btn { width: 100%; background: #2563eb; color: white; border: none; padding: 9px; border-radius: 10px; font-size: 14px; font-weight: 800; cursor: pointer; transition: all 0.15s; }
    .play-btn:hover { background: #3b82f6; }
    .play-btn.playing { background: #10b981 !important; transform: scale(1.02); }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🔤 Qalamo — Monde 4 : Combinaisons de 2 Voyelles Courtes</h1>
      <p class="subtitle">36 Sons Générés avec la méthode Hamed (Syllabé) — Sans phonétique latine</p>
    </header>
"""

for s in sections:
    html += f"""
    <div class="category-section">
      <div class="category-header">
        <div class="category-title">{s['title']}</div>
        <div class="category-badge">{s['badge']}</div>
      </div>
      <div class="grid">
    """
    for key, ar, phon, desc in s['items']:
        b64 = get_b64(key)
        html += f"""
        <div class="card">
          <div class="ar-word">{ar}</div>
          <div class="phonetic">{phon}</div>
          <div class="meaning">{desc}</div>
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

with open('test_two_vowels.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('test_two_vowels.html updated successfully!')
