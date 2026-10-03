import os
import base64

emphatic_letters = [
    {
        "char": "طِ",
        "name": "Ṭi (طِ — Ṭaa)",
        "file": "ttaa_kasra.mp3",
        "desc": "Emphatique pur, bien rond en bouche"
    },
    {
        "char": "صِ",
        "name": "Ṣi (صِ — Ṣaad)",
        "file": "sad_kasra.mp3",
        "desc": "Sifflement sourd et plein d'air"
    },
    {
        "char": "ضِ",
        "name": "Ḍi (ضِ — Ḍaad)",
        "file": "dad_kasra.mp3",
        "desc": "Impact latéral de la langue, grave"
    },
    {
        "char": "ظِ",
        "name": "Ẓi (ظِ — Ẓaa)",
        "file": "zha_kasra.mp3",
        "desc": "Interdentale sonore emphatique"
    },
    {
        "char": "قِ",
        "name": "Qi (قِ — Qāf)",
        "file": "qaf_kasra.mp3",
        "desc": "Claquement uvulaire net et profond"
    },
    {
        "char": "خِ",
        "name": "Khi (خِ — Khā')",
        "file": "kha_kasra.mp3",
        "desc": "Frottement guttural raclé sans sifflement"
    },
    {
        "char": "غِ",
        "name": "Ghi (غِ — Ghayn)",
        "file": "ghayn_kasra.mp3",
        "desc": "Vibration gutturale postérieure douce"
    }
]

AUDIO_DIR = "assets/audio/generated"

cards_html = []
for item in emphatic_letters:
    filepath = os.path.join(AUDIO_DIR, item["file"])
    with open(filepath, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    card = f'''        <div class="card" style="border-color:#22c55e;">
          <div class="ar-word">{item["char"]}</div>
          <div class="phonetic" style="color:#fcd34d;">{item["name"]}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{item["desc"]}</p>
          <button class="play-btn" style="background:#16a34a;" onclick="playAudio('data:audio/mp3;base64,{b64}', this)">🔊 Écouter</button>
        </div>'''
    cards_html.append(card)

section_html = f'''    <!-- SECTION SPECIAL LETTRES EMPHATIQUES KASRA -->
    <div class="highlight-box" style="border-color:#22c55e; background:#064e3b22;">
      <div class="highlight-title" style="color:#4ade80;">✨ Les 7 Lettres Emphatiques avec Kasrah (Shakir -15% — Net & Articulé)</div>
      <p class="highlight-desc">Toutes les lettres d'emphase (حروف الاستعلاء) avec Kasrah ont été mises à jour avec le modèle validé pour une distinction acoustique parfaite :</p>
      <div class="grid">
{chr(10).join(cards_html)}
      </div>
    </div>
    <!-- /SECTION EMPHATIQUES -->'''

# Update test_audio.html
with open("test_audio.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace previous Ti section or insert at top
if '<!-- SECTION SPECIAL LETTRES EMPHATIQUES KASRA -->' in content:
    import re
    content = re.sub(r'<!-- SECTION SPECIAL LETTRES EMPHATIQUES KASRA -->.*?<!-- /SECTION EMPHATIQUES -->', section_html, content, flags=re.DOTALL)
elif '<!-- SECTION SPECIAL CHOIX DU SON TI EMPHATIQUE -->' in content:
    import re
    content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON TI EMPHATIQUE -->.*?<!-- /SECTION TI -->', section_html, content, flags=re.DOTALL)
else:
    target = '<!-- SECTION SPECIAL CHOIX DU SON DJI -->'
    content = content.replace(target, section_html + '\n\n    ' + target)

with open("test_audio.html", "w", encoding="utf-8") as f:
    f.write(content)

print("test_audio.html updated with all 7 emphatic Kasrah letters!")
