import os
import json
import base64
import sys

sys.stdout.reconfigure(encoding='utf-8')

# Load World 4 curriculum data
with open('scripts/world4_data.json', 'r', encoding='utf-8') as f:
    w4 = json.load(f)

def get_b64(key):
    path = f'assets/audio/generated/{key}.mp3'
    if os.path.exists(path):
        with open(path, 'rb') as f:
            return base64.b64encode(f.read()).decode('utf-8')
    return ''

# Let's organize by levels and series
levels_data = []

for lvl in w4['levels']:
    lvl_info = {
        'id': lvl['id'],
        'title': lvl['title'],
        'titleAr': lvl.get('titleAr', ''),
        'gameType': lvl['gameType'],
        'desc': lvl.get('description', ''),
        'cards': []
    }
    
    # Items (for bubble/target)
    for it in lvl.get('items', []):
        lvl_info['cards'].append({
            'key': it['id'],
            'word': it.get('grapheme', ''),
            'audioText': it.get('audioText', ''),
            'desc': it.get('phonemeDesc', ''),
            'type': 'Bulle / Cible'
        })
        
    # WordItems (for wordBuilder)
    for w in lvl.get('wordItems', []):
        lvl_info['cards'].append({
            'key': w['id'],
            'word': w.get('word', ''),
            'audioText': w.get('audioText', ''),
            'desc': w.get('meaning', w.get('phonemeDesc', '')),
            'type': 'Construction de mot'
        })
        
    levels_data.append(lvl_info)

# Also extra 2-vowel words from generate_all_28_two_vowels
EXTRA_WORDS = [
    ("dara", "دَرَ", "دَ رَ", "Syllabes A + A"),
    ("kata", "كَتَ", "كَ تَ", "Syllabes A + A"),
    ("sama", "سَمَ", "سَ مَ", "Syllabes A + A"),
    ("rasa", "رَسَ", "رَ سَ", "Syllabes A + A"),
    ("katu", "كَتُ", "كَ تُ", "Syllabes A + OU"),
    ("daru", "دَرُ", "دَ رُ", "Syllabes A + OU"),
    ("samu", "سَمُ", "سَ مُ", "Syllabes A + OU"),
    ("bari", "بَرِ", "بَ رِ", "Syllabes A + I"),
    ("dari", "دَرِ", "دَ رِ", "Syllabes A + I"),
    ("sami_short", "سَمِ", "سَ مِ", "Syllabes A + I"),
    ("kati", "كَتِ", "كَ تِ", "Syllabes A + I"),
    ("kuti", "كُتِ", "كُ تِ", "Syllabes OU + I"),
    ("sumi", "سُمِ", "سُ مِ", "Syllabes OU + I"),
    ("duri", "دُرِ", "دُ رِ", "Syllabes OU + I"),
    ("rusi", "رُسِ", "رُ سِ", "Syllabes OU + I"),
    ("kuta", "كُتَ", "كُ تَ", "Syllabes OU + A"),
    ("dura", "دُرَ", "دُ رَ", "Syllabes OU + A"),
    ("sura", "سُرَ", "سُ رَ", "Syllabes OU + A"),
    ("bita", "بِتَ", "بِ تَ", "Syllabes I + A"),
    ("dina", "دِنَ", "دِ نَ", "Syllabes I + A"),
    ("sima", "سِمَ", "سِ مَ", "Syllabes I + A"),
]

extra_section = {
    'id': 99,
    'title': 'Mots & Syllabes Complémentaires à 2 Voyelles',
    'titleAr': 'مَقَاطِعُ إِضَافِيَّةٌ لِلتَّدْرِيب',
    'gameType': 'bonus',
    'desc': 'Combinaisons supplémentaires générées pour la banque de sons',
    'cards': [
        {
            'key': key,
            'word': word,
            'audioText': audioText,
            'desc': desc,
            'type': 'Syllabes 2 voyelles'
        }
        for key, word, audioText, desc in EXTRA_WORDS
    ]
}
levels_data.append(extra_section)

# Build comprehensive interactive HTML
html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo — Validation Complète des Mots du Monde 4</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background: #0b0f19; color: #f8fafc; padding: 24px 16px; display: flex; justify-content: center; }
    .container { width: 100%; max-width: 1200px; }
    
    header { text-align: center; margin-bottom: 24px; position: sticky; top: 0; background: #0b0f19ee; backdrop-filter: blur(10px); padding: 14px 0; z-index: 100; border-bottom: 1px solid #1e293b; }
    h1 { color: #f59e0b; font-size: 26px; margin-bottom: 6px; }
    p.subtitle { color: #94a3b8; font-size: 14px; margin-bottom: 12px; }

    .toolbar { display: flex; gap: 10px; justify-content: center; align-items: center; flex-wrap: wrap; margin-bottom: 10px; }
    .stat-badge { background: #1e293b; color: #38bdf8; border: 1px solid #334155; padding: 6px 12px; border-radius: 20px; font-size: 12px; font-weight: 700; }
    .export-btn { background: #10b981; color: white; border: none; padding: 7px 14px; border-radius: 8px; font-size: 13px; font-weight: 700; cursor: pointer; transition: all 0.15s; }
    .export-btn:hover { background: #059669; }

    .level-section { background: #131d31; border: 2px solid #1e293b; border-radius: 18px; padding: 18px; margin-bottom: 22px; }
    .level-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; border-bottom: 1px solid #334155; padding-bottom: 8px; flex-wrap: wrap; gap: 8px; }
    .level-title { color: #38bdf8; font-size: 18px; font-weight: 800; }
    .level-badge { background: #f59e0b22; color: #f59e0b; border: 1px solid #f59e0b66; font-size: 11px; font-weight: 800; text-transform: uppercase; padding: 4px 8px; border-radius: 12px; }

    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 14px; }
    .card { background: #0b0f19; border: 2px solid #334155; border-radius: 14px; padding: 14px; text-align: center; transition: all 0.15s; display: flex; flex-direction: column; justify-content: space-between; position: relative; }
    .card:hover { border-color: #f59e0b; transform: translateY(-2px); }
    .card.status-ok { border-color: #10b981; background: #064e3b10; }
    .card.status-issue { border-color: #ef4444; background: #7f1d1d15; }

    .ar-word { font-family: 'Amiri', serif; font-size: 40px; font-weight: 700; color: #fde047; margin-bottom: 2px; line-height: 48px; }
    .audio-text { font-family: 'Amiri', serif; font-size: 20px; font-weight: 700; color: #38bdf8; margin-bottom: 4px; }
    .key-info { font-size: 11px; color: #64748b; margin-bottom: 10px; font-family: monospace; }
    
    .play-btn { width: 100%; background: #2563eb; color: white; border: none; padding: 9px; border-radius: 8px; font-size: 13px; font-weight: 800; cursor: pointer; transition: all 0.15s; display: flex; align-items: center; justify-content: center; gap: 6px; margin-bottom: 8px; }
    .play-btn:hover { background: #3b82f6; }
    .play-btn.playing { background: #10b981 !important; transform: scale(1.02); }

    .val-actions { display: flex; gap: 4px; }
    .val-btn { flex: 1; border: 1px solid #334155; background: #1e293b; color: #cbd5e1; padding: 5px; border-radius: 6px; font-size: 11px; font-weight: 700; cursor: pointer; transition: all 0.1s; }
    .val-btn.ok-btn.active { background: #10b981; color: white; border-color: #10b981; }
    .val-btn.bad-btn.active { background: #ef4444; color: white; border-color: #ef4444; }
    .val-note { width: 100%; margin-top: 6px; background: #1e293b; border: 1px solid #334155; color: #f8fafc; font-size: 11px; padding: 4px 6px; border-radius: 4px; display: none; }
    .card.status-issue .val-note { display: block; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🎙️ Console de Validation Complète — Monde 4</h1>
      <p class="subtitle">Écoutez et validez tous les mots et combinaisons de 2 voyelles (Niveaux 27 à 32)</p>
      <div class="toolbar">
        <span class="stat-badge" id="totalCount">Total: 0 mots</span>
        <span class="stat-badge" style="color: #10b981;" id="okCount">✅ Validés: 0</span>
        <span class="stat-badge" style="color: #ef4444;" id="issueCount">❌ À corriger: 0</span>
        <button class="export-btn" onclick="copyReport()">📋 Copier le rapport de validation</button>
      </div>
    </header>
"""

total_words = 0

for lvl in levels_data:
    if not lvl['cards']:
        continue
    html += f"""
    <div class="level-section">
      <div class="level-header">
        <div class="level-title">Niveau {lvl['id']} : {lvl['title']}</div>
        <div class="level-badge">{lvl['gameType']} • {len(lvl['cards'])} sons</div>
      </div>
      <div class="grid">
    """
    for card in lvl['cards']:
        total_words += 1
        b64 = get_b64(card['key'])
        html += f"""
        <div class="card" id="card_{card['key']}" data-key="{card['key']}" data-word="{card['word']}">
          <div>
            <div class="ar-word">{card['word']}</div>
            <div class="audio-text">{card['audioText']}</div>
            <div class="key-info">{card['key']}.mp3</div>
          </div>
          <div>
            <button class="play-btn" onclick="playAudio('data:audio/mp3;base64,{b64}', this)">🔊 Écouter</button>
            <div class="val-actions">
              <button class="val-btn ok-btn" onclick="setValidation('{card['key']}', 'ok')">✅ Valide</button>
              <button class="val-btn bad-btn" onclick="setValidation('{card['key']}', 'issue')">❌ Erreur</button>
            </div>
            <input type="text" class="val-note" id="note_{card['key']}" placeholder="Ex: son coupé, mauvaise lettre..." oninput="saveState()">
          </div>
        </div>
        """
    html += """
      </div>
    </div>
    """

html += f"""
  </div>

  <script>
    let currentAudio = null;
    let currentBtn = null;
    const totalWords = {total_words};

    const state = JSON.parse(localStorage.getItem('qalamo_world4_val') || '{{}}');

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

    function setValidation(key, status) {{
      const card = document.getElementById('card_' + key);
      const okBtn = card.querySelector('.ok-btn');
      const badBtn = card.querySelector('.bad-btn');
      
      if (state[key] && state[key].status === status) {{
        // toggle off
        delete state[key];
        card.classList.remove('status-ok', 'status-issue');
        okBtn.classList.remove('active');
        badBtn.classList.remove('active');
      }} else {{
        state[key] = {{
          status: status,
          word: card.dataset.word,
          note: document.getElementById('note_' + key).value || ''
        }};
        card.classList.remove('status-ok', 'status-issue');
        okBtn.classList.remove('active');
        badBtn.classList.remove('active');

        if (status === 'ok') {{
          card.classList.add('status-ok');
          okBtn.classList.add('active');
        }} else {{
          card.classList.add('status-issue');
          badBtn.classList.add('active');
        }}
      }}
      saveState();
      updateCounters();
    }}

    function saveState() {{
      // update notes
      for (const key in state) {{
        const noteInput = document.getElementById('note_' + key);
        if (noteInput) {{
          state[key].note = noteInput.value;
        }}
      }}
      localStorage.setItem('qalamo_world4_val', JSON.stringify(state));
    }}

    function loadState() {{
      for (const key in state) {{
        const card = document.getElementById('card_' + key);
        if (card) {{
          const item = state[key];
          const okBtn = card.querySelector('.ok-btn');
          const badBtn = card.querySelector('.bad-btn');
          const noteInput = document.getElementById('note_' + key);
          
          if (item.status === 'ok') {{
            card.classList.add('status-ok');
            okBtn.classList.add('active');
          }} else if (item.status === 'issue') {{
            card.classList.add('status-issue');
            badBtn.classList.add('active');
          }}
          if (noteInput && item.note) {{
            noteInput.value = item.note;
          }}
        }}
      }}
      updateCounters();
    }}

    function updateCounters() {{
      let ok = 0;
      let issue = 0;
      for (const key in state) {{
        if (state[key].status === 'ok') ok++;
        if (state[key].status === 'issue') issue++;
      }}
      document.getElementById('totalCount').innerText = `Total: ${{totalWords}} mots`;
      document.getElementById('okCount').innerText = `✅ Validés: ${{ok}}`;
      document.getElementById('issueCount').innerText = `❌ À corriger: ${{issue}}`;
    }}

    function copyReport() {{
      const issues = [];
      for (const key in state) {{
        if (state[key].status === 'issue') {{
          issues.push(`- **${{state[key].word}}** (\`${{key}}\`): ${{state[key].note || 'Son à corriger'}}`);
        }}
      }}
      let text = `### Rapport de Validation Monde 4\\n\\n`;
      if (issues.length === 0) {{
        text += `Tous les sons testés sont validés ✅ (Aucune erreur signalée)`;
      }} else {{
        text += `Voici les sons à corriger (${{issues.length}}):\\n` + issues.join('\\n');
      }}
      navigator.clipboard.writeText(text).then(() => {{
        alert("Rapport copié dans le presse-papier ! Vous pouvez le coller directement dans le chat.");
      }});
    }}

    loadState();
  </script>
</body>
</html>
"""

with open('test_monde4_validation.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f"test_monde4_validation.html generated successfully with {total_words} words & audio files!")
