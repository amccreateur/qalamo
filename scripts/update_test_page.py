import os
import base64

candidates = [
    {
        "id": "shakir_ti_clear_15",
        "title": "Shakir — Net & Articulé (-15%) ⭐ Recommandé",
        "text": "طِي",
        "desc": "Articulation nette, très audible avec résonance de la Kasrah",
        "border": "#22c55e",
        "btn_bg": "#16a34a"
    },
    {
        "id": "shakir_ti_long_25",
        "title": "Shakir — Bien Soutenu (-25%) ⭐ Posé",
        "text": "طِي",
        "desc": "Plus lent, le son emphatique Ṭ et le i durent plus longtemps",
        "border": "#3b82f6",
        "btn_bg": "#2563eb"
    },
    {
        "id": "hamed_ti_long_20",
        "title": "Hamed — Posé & Profond (-20%)",
        "text": "طِي",
        "desc": "Voix saoudienne classique, grave et posée",
        "border": "#f59e0b",
        "btn_bg": "#d97706"
    },
    {
        "id": "hamed_ti_short_15",
        "title": "Hamed — Bref & Emphatique (-15%)",
        "text": "طِ",
        "desc": "Voyelle courte standard (sans allongement de transcription)",
        "border": "#a855f7",
        "btn_bg": "#9333ea"
    },
    {
        "id": "shakir_ti_short_15",
        "title": "Shakir — Bref Standard (-15%)",
        "text": "طِ",
        "desc": "Voyelle courte naturelle égyptienne classique",
        "border": "#ec4899",
        "btn_bg": "#db2777"
    },
    {
        "id": "fahed_ti_15",
        "title": "Fahed (Golfe) — Profond (-15%)",
        "text": "طِي",
        "desc": "Voix koweïtienne avec emphase marquée",
        "border": "#06b6d4",
        "btn_bg": "#0891b2"
    },
    {
        "id": "zariyah_ti_15",
        "title": "Zariyah (Féminin) — Clair (-15%)",
        "text": "طِي",
        "desc": "Voix féminine saoudienne très claire",
        "border": "#e11d48",
        "btn_bg": "#be123c"
    }
]

ti_cards_html = []
for c in candidates:
    audio_path = f"scripts/temp_audio/{c['id']}.mp3"
    with open(audio_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode("utf-8")
    
    card = f'''        <div class="card" style="border-color:{c['border']};">
          <div class="ar-word">طِ</div>
          <div class="phonetic" style="color:#fcd34d;">{c['title']}</div>
          <p style="font-size:11px; color:#94a3b8; margin-bottom:10px;">{c['desc']}</p>
          <button class="play-btn" style="background:{c['btn_bg']};" onclick="playAudio('data:audio/mp3;base64,{b64}', this)">🔊 Écouter</button>
        </div>'''
    ti_cards_html.append(card)

ti_section = f'''    <!-- SECTION SPECIAL CHOIX DU SON TI EMPHATIQUE -->
    <div class="highlight-box" style="border-color:#22c55e; background:#064e3b22;">
      <div class="highlight-title" style="color:#4ade80;">🎯 Choix du son « Ṭi » (طِ) — Emphatique & Clair</div>
      <p class="highlight-desc">Voici les propositions pour <strong>طِ (Ṭa avec Kasrah)</strong>. Le son doit être bien gras/emphatique dans la bouche (contrairement au <strong>تِ</strong> fin), bien audible et sans coupure :</p>
      <div class="grid">
{chr(10).join(ti_cards_html)}
      </div>
    </div>
'''

with open("test_audio.html", "r", encoding="utf-8") as f:
    content = f.read()

# Replace or insert above the Dji section
target_marker = '<!-- SECTION SPECIAL CHOIX DU SON DJI -->'
if '<!-- SECTION SPECIAL CHOIX DU SON TI EMPHATIQUE -->' in content:
    # already there, let's replace it
    import re
    content = re.sub(r'<!-- SECTION SPECIAL CHOIX DU SON TI EMPHATIQUE -->.*?<!-- /SECTION TI -->', ti_section + '    <!-- /SECTION TI -->', content, flags=re.DOTALL)
else:
    content = content.replace(target_marker, ti_section + '    <!-- /SECTION TI -->\n\n    ' + target_marker)

with open("test_audio.html", "w", encoding="utf-8") as f:
    f.write(content)

print("test_audio.html successfully updated with Ti proposals!")
