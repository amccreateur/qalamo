import asyncio
import os
import subprocess
import base64
import edge_tts
import sys

sys.stdout.reconfigure(encoding='utf-8')

PROPOSALS_DIR = "scripts/test_proposals/world4_fixes"
os.makedirs(PROPOSALS_DIR, exist_ok=True)
os.makedirs("scripts/temp_audio", exist_ok=True)

WORDS_TO_FIX = [
    ("zhafu", "ظَفُ", "ظَ + فُ", "Ẓā' Emphatique (Fatḥah) + Fā' (Ḍammah)"),
    ("hasu", "حَسُ", "حَ + سُ", "Ḥā' de la Gorge (Fatḥah) + Seen (Ḍammah)"),
    ("duri_emph", "ضُرِ", "ضُ + رِ", "Ḍād Emphatique (Ḍammah) + Rā' (Kasrah)"),
    ("tubi", "طُبِ", "طُ + بِ", "Ṭā' Emphatique (Ḍammah) + Bā' (Kasrah)"),
    ("thubi", "ثُبِ", "ثُ + بِ", "Thā' Interdentale (Ḍammah) + Bā' (Kasrah)"),
    ("ruba", "رُبَ", "رُ + بَ", "Rā' (Ḍammah) + Bā' (Fatḥah)"),
    ("zhima", "ظِمَ", "ظِ + مَ", "Ẓā' Emphatique (Kasrah) + Meem (Fatḥah)"),
    ("khifa", "خِفَ", "خِ + فَ", "Khā' Emphatique (Kasrah) + Fā' (Fatḥah)"),
    ("ghani", "غَنِ", "غَ + نِ", "Ghayn Emphatique (Fatḥah) + Noon (Kasrah)"),
]

# Variations to test for each word:
# 1. Hamed - Espace syllabique ("ظَ فُ", rate="-5%")
# 2. Hamed - Connecté ("ظَفُ", rate="-8%")
# 3. Shakir - Espace syllabique ("ظَ فُ", rate="-8%")
# 4. Shakir - Connecté ("ظَفُ", rate="-8%")
# 5. Hedi - Espace syllabique ("ظَ فُ", rate="-8%")
# 6. Moaz - Espace syllabique ("ظَ فُ", rate="-8%")

VARIANTS = [
    ("hamed_spaced", "Hamed (Syllabé)", "ar-SA-HamedNeural", "spaced", "-5%"),
    ("hamed_connected", "Hamed (Lié)", "ar-SA-HamedNeural", "connected", "-8%"),
    ("shakir_spaced", "Shakir (Syllabé - Égypte)", "ar-EG-ShakirNeural", "spaced", "-8%"),
    ("shakir_connected", "Shakir (Lié - Égypte)", "ar-EG-ShakirNeural", "connected", "-8%"),
    ("hedi_spaced", "Hedi (Syllabé - Tunisie)", "ar-TN-HediNeural", "spaced", "-8%"),
    ("moaz_spaced", "Moaz (Syllabé - Qatar)", "ar-QA-MoazNeural", "spaced", "-8%"),
]

async def generate_candidate(key, word, var_id, voice, mode, rate):
    out_file = os.path.join(PROPOSALS_DIR, f"{key}_{var_id}.mp3")
    raw_file = f"scripts/temp_audio/raw_{key}_{var_id}.mp3"
    
    # Text preparation
    # if spaced: split chars by space: e.g. "ظَفُ" -> "ظَ فُ"
    if mode == "spaced":
        # extract the two syllables with vowels
        # word is 2 chars + harakat
        # let's split into components
        text = " ".join([c for c in word]) # this might split harakat from base, so let's do proper syllabification
        # better:
        chars = []
        cur = ""
        for ch in word:
            if ch in ['\u064e', '\u064f', '\u0650', '\u0652', '\u0651']: # fatha, damma, kasra, sukun, shaddah
                cur += ch
            else:
                if cur:
                    chars.append(cur)
                cur = ch
        if cur:
            chars.append(cur)
        text = " ".join(chars)
    else:
        text = word
        
    comm = edge_tts.Communicate(text, voice, rate=rate)
    await comm.save(raw_file)
    
    subprocess.run([
        "ffmpeg", "-y", "-i", raw_file,
        "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,areverse,silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,areverse,loudnorm=I=-16:TP=-1.5:LRA=7",
        "-ar", "44100", "-b:a", "128k",
        out_file
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    print(f"[OK] {key} - {var_id} ('{text}' via {voice})")

async def generate_all():
    print("Generating proposals for the 9 flagged words...")
    for key, word, syll, desc in WORDS_TO_FIX:
        for var_id, label, voice, mode, rate in VARIANTS:
            await generate_candidate(key, word, var_id, voice, mode, rate)

def get_b64(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

def build_html():
    html = """<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Qalamo — Correction des 9 Sons du Monde 4</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap" rel="stylesheet">
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; }
    body { background: #0b0f19; color: #f8fafc; padding: 24px 16px; display: flex; justify-content: center; }
    .container { width: 100%; max-width: 1200px; }
    
    header { text-align: center; margin-bottom: 24px; }
    h1 { color: #f59e0b; font-size: 26px; margin-bottom: 6px; }
    p.subtitle { color: #94a3b8; font-size: 14px; margin-bottom: 20px; }

    .word-section { background: #131d31; border: 2px solid #334155; border-radius: 18px; padding: 20px; margin-bottom: 24px; }
    .word-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 14px; border-bottom: 1px solid #334155; padding-bottom: 10px; }
    .word-title { display: flex; align-items: center; gap: 14px; }
    .word-ar { font-family: 'Amiri', serif; font-size: 46px; font-weight: 700; color: #fde047; line-height: 50px; }
    .word-syll { font-family: 'Amiri', serif; font-size: 22px; color: #38bdf8; font-weight: 700; }
    .word-desc { font-size: 13px; color: #94a3b8; }
    .word-key { background: #1e293b; color: #f59e0b; border: 1px solid #f59e0b66; font-size: 12px; font-weight: 700; padding: 4px 10px; border-radius: 10px; font-family: monospace; }

    .grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(210px, 1fr)); gap: 12px; }
    .card { background: #0b0f19; border: 2px solid #334155; border-radius: 14px; padding: 14px; text-align: center; display: flex; flex-direction: column; justify-content: space-between; transition: all 0.15s; }
    .card:hover { border-color: #38bdf8; transform: translateY(-2px); }
    .card.current { border-color: #ef4444; background: #7f1d1d15; }
    .card.selected { border-color: #10b981; background: #064e3b25; }

    .badge { display: inline-block; font-size: 10px; font-weight: 800; text-transform: uppercase; padding: 3px 8px; border-radius: 10px; margin-bottom: 8px; align-self: center; }
    .badge-curr { background: #ef444422; color: #f87171; border: 1px solid #ef444466; }
    .badge-var { background: #334155; color: #cbd5e1; }
    .badge-shakir { background: #0284c722; color: #38bdf8; border: 1px solid #0284c766; }

    .card-title { font-size: 14px; font-weight: 800; color: #f8fafc; margin-bottom: 2px; }
    .card-sub { font-size: 11px; color: #64748b; margin-bottom: 12px; }

    .play-btn { width: 100%; background: #2563eb; color: white; border: none; padding: 9px; border-radius: 8px; font-size: 13px; font-weight: 800; cursor: pointer; transition: all 0.15s; margin-bottom: 6px; }
    .play-btn:hover { background: #3b82f6; }
    .play-btn.playing { background: #10b981 !important; transform: scale(1.02); }

    .choose-btn { width: 100%; background: #1e293b; border: 1px solid #334155; color: #94a3b8; padding: 6px; border-radius: 6px; font-size: 12px; font-weight: 700; cursor: pointer; transition: all 0.15s; }
    .choose-btn:hover { background: #334155; color: white; }
    .card.selected .choose-btn { background: #10b981; color: white; border-color: #10b981; }

    .export-panel { position: sticky; bottom: 20px; background: #1e293bee; backdrop-filter: blur(10px); border: 2px solid #10b981; border-radius: 16px; padding: 14px 20px; display: flex; justify-content: space-between; align-items: center; margin-top: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
    .export-btn { background: #10b981; color: white; border: none; padding: 10px 20px; border-radius: 10px; font-size: 14px; font-weight: 800; cursor: pointer; transition: all 0.15s; }
    .export-btn:hover { background: #059669; }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <h1>🎙️ Console de Correction — Les 9 Sons du Monde 4</h1>
      <p class="subtitle">Écoutez les propositions pour chaque mot et choisissez votre version préférée</p>
    </header>
"""

    for key, word, syll, desc in WORDS_TO_FIX:
        curr_b64 = get_b64(f"assets/audio/generated/{key}.mp3")
        html += f"""
    <div class="word-section" id="section_{key}">
      <div class="word-header">
        <div class="word-title">
          <div class="word-ar">{word}</div>
          <div>
            <div class="word-syll">{syll}</div>
            <div class="word-desc">{desc}</div>
          </div>
        </div>
        <div class="word-key">{key}.mp3</div>
      </div>
      <div class="grid">
        <!-- Version Actuelle -->
        <div class="card current">
          <div class="badge badge-curr">Version Actuelle (Signalée)</div>
          <div class="card-title">Version Actuelle</div>
          <div class="card-sub">assets/audio/generated/{key}.mp3</div>
          <button class="play-btn" onclick="playAudio('data:audio/mp3;base64,{curr_b64}', this)">🔊 Écouter Actuel</button>
        </div>
        """
        for var_id, label, voice, mode, rate in VARIANTS:
            prop_file = os.path.join(PROPOSALS_DIR, f"{key}_{var_id}.mp3")
            b64 = get_b64(prop_file)
            badge_class = "badge-shakir" if "shakir" in var_id else "badge-var"
            html += f"""
        <div class="card" id="card_{key}_{var_id}" data-key="{key}" data-var="{var_id}">
          <div class="badge {badge_class}">{label}</div>
          <div class="card-title">{label}</div>
          <div class="card-sub">{voice}</div>
          <button class="play-btn" onclick="playAudio('data:audio/mp3;base64,{b64}', this)">🔊 Écouter</button>
          <button class="choose-btn" onclick="chooseVariant('{key}', '{var_id}')">👉 Choisir cette version</button>
        </div>
            """
        html += """
      </div>
    </div>
        """

    html += """
    <div class="export-panel">
      <div>
        <div style="font-weight: 800; color: #f8fafc; font-size: 15px;">Sélections effectuées : <span id="selCount" style="color: #10b981;">0 / 9</span></div>
        <div style="font-size: 12px; color: #94a3b8;">Cliquez sur "Choisir cette version" sur chaque mot puis copiez vos choix</div>
      </div>
      <button class="export-btn" onclick="copyChoices()">📋 Copier mes choix pour application immédiate</button>
    </div>
  </div>

  <script>
    let currentAudio = null;
    let currentBtn = null;
    const choices = JSON.parse(localStorage.getItem('qalamo_world4_fixes') || '{}');

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

    function chooseVariant(key, varId) {
      // Remove selected class from all cards in this word section
      const section = document.getElementById('section_' + key);
      section.querySelectorAll('.card').forEach(c => c.classList.remove('selected'));
      
      // Select new
      const card = document.getElementById('card_' + key + '_' + varId);
      if (card) card.classList.add('selected');

      choices[key] = varId;
      localStorage.setItem('qalamo_world4_fixes', JSON.stringify(choices));
      updateCount();
    }

    function loadChoices() {
      for (const key in choices) {
        const varId = choices[key];
        const card = document.getElementById('card_' + key + '_' + varId);
        if (card) card.classList.add('selected');
      }
      updateCount();
    }

    function updateCount() {
      const count = Object.keys(choices).length;
      document.getElementById('selCount').innerText = `${count} / 9`;
    }

    function copyChoices() {
      const lines = [];
      for (const key in choices) {
        lines.push(`- **${key}** : \`${choices[key]}\``);
      }
      if (lines.length === 0) {
        alert("Veuillez sélectionner au moins une version préférée.");
        return;
      }
      const text = `### Choix des 9 Sons Monde 4\\n\\n` + lines.join('\\n');
      navigator.clipboard.writeText(text).then(() => {
        alert("Choix copiés dans le presse-papier ! Vous pouvez les coller dans le chat pour que je les applique.");
      });
    }

    loadChoices();
  </script>
</body>
</html>
"""
    with open("test_fix_9_words.html", "w", encoding="utf-8") as f:
        f.write(html)
    print("test_fix_9_words.html built successfully!")

async def main():
    await generate_all()
    build_html()

if __name__ == "__main__":
    asyncio.run(main())
