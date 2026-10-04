import os
import base64

TEMP = 'scripts/temp_audio/hou_pure_slices'

candidates = [
    {
        "id": "hou_hudhud_hedi_24",
        "title": "Proposition 1 — Hedi (Extrait 'Hud-hud' 0.24s)",
        "file": f"{TEMP}/hudhud_hedi_cut_0.24.mp3",
        "badge": "Top Recommandé ⭐",
        "desc": "Son 'Hou' 100% pur extrait de 'Hud-hud', garanti sans 'wa'",
        "color": "#10B981"
    },
    {
        "id": "hou_hudhud_moaz_24",
        "title": "Proposition 2 — Moaz (Extrait 'Hud-hud' 0.24s)",
        "file": f"{TEMP}/hudhud_moaz_cut_0.24.mp3",
        "badge": "Moaz ⭐",
        "desc": "Voix douce de Moaz, première syllabe 'Hou' pure",
        "color": "#F59E0B"
    },
    {
        "id": "hou_hudhud_hamed_24",
        "title": "Proposition 3 — Hamed (Extrait 'Hud-hud' 0.24s)",
        "file": f"{TEMP}/hudhud_hamed_cut_0.24.mp3",
        "badge": "Hamed",
        "desc": "Voix saoudienne claire, extrait de 'Hud-hud'",
        "color": "#3B82F6"
    },
    {
        "id": "hou_hudhud_shakir_24",
        "title": "Proposition 4 — Shakir (Extrait 'Hud-hud' 0.24s)",
        "file": f"{TEMP}/hudhud_shakir_cut_0.24.mp3",
        "badge": "Shakir",
        "desc": "Voix classique posée, extrait de 'Hud-hud'",
        "color": "#8B5CF6"
    },
    {
        "id": "hou_hubut_hedi_24",
        "title": "Proposition 5 — Hedi (Extrait 'Houb-out' 0.24s)",
        "file": f"{TEMP}/hubut_hedi_cut_0.24.mp3",
        "badge": "Hedi",
        "desc": "Attaque 'Hou' très articulée et distincte",
        "color": "#10B981"
    },
    {
        "id": "hou_hubut_moaz_24",
        "title": "Proposition 6 — Moaz (Extrait 'Houb-out' 0.24s)",
        "file": f"{TEMP}/hubut_moaz_cut_0.24.mp3",
        "badge": "Moaz",
        "desc": "Attaque douce 'Hou' sans le moindre parasite",
        "color": "#F59E0B"
    },
    {
        "id": "hou_hum_hedi_24",
        "title": "Proposition 7 — Hedi (Extrait 'Hou-m' 0.24s)",
        "file": f"{TEMP}/hum_hedi_cut_0.24.mp3",
        "badge": "Hedi",
        "desc": "Syllabe 'Hou' pure issue de 'Houm'",
        "color": "#10B981"
    },
    {
        "id": "hou_hum_moaz_24",
        "title": "Proposition 8 — Moaz (Extrait 'Hou-m' 0.24s)",
        "file": f"{TEMP}/hum_moaz_cut_0.24.mp3",
        "badge": "Moaz",
        "desc": "Syllabe 'Hou' pure issue de 'Houm'",
        "color": "#F59E0B"
    },
    {
        "id": "hou_hudhud_hedi_20",
        "title": "Proposition 9 — Hedi (Version Courte 0.20s)",
        "file": f"{TEMP}/hudhud_hedi_cut_0.20.mp3",
        "badge": "Court",
        "desc": "Son 'Hou' très court et percutant",
        "color": "#EC4899"
    },
    {
        "id": "hou_hudhud_moaz_20",
        "title": "Proposition 10 — Moaz (Version Courte 0.20s)",
        "file": f"{TEMP}/hudhud_moaz_cut_0.20.mp3",
        "badge": "Court",
        "desc": "Son 'Hou' très court et percutant",
        "color": "#06B6D4"
    },
]

cards_html = []
for c in candidates:
    b64 = ""
    if os.path.exists(c["file"]):
        with open(c["file"], "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")
            
    cards_html.append(f"""
    <div class="card" style="--accent: {c['color']}">
        <div class="card-top">
            <span class="badge">{c['badge']}</span>
            <span class="phonetic">« Hou »</span>
        </div>
        <div class="char">هُ</div>
        <div class="card-title">{c['title']}</div>
        <div class="card-desc">{c['desc']}</div>
        <button class="play-btn" onclick="playAudio('{c['id']}', this)">
            <span>▶</span> Écouter
        </button>
        <label class="select-label">
            <input type="radio" name="hou_choice" value="{c['id']}" onchange="selectChoice('{c['id']}', '{c['title']}')">
            <span>Choisir cette version</span>
        </label>
        <audio id="{c['id']}" src="data:audio/mp3;base64,{b64}"></audio>
    </div>
    """)

html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qalamo — Résolution Spéciale : Hā' Ḍammah (هُ — « Hou » Pur)</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        * {{ box-sizing: border-box; margin: 0; padding: 0; font-family: 'Plus Jakarta Sans', sans-serif; }}
        body {{
            background: #0B0F19;
            color: #F8FAFC;
            padding: 30px 16px 120px;
            display: flex;
            justify-content: center;
        }}
        .container {{ width: 100%; max-width: 950px; }}
        header {{
            text-align: center;
            margin-bottom: 28px;
            background: linear-gradient(135deg, #1E293B, #0F172A);
            border: 1px solid #2A364F;
            padding: 28px 20px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        h1 {{
            font-size: 26px;
            font-weight: 800;
            background: linear-gradient(135deg, #FBBF24, #F59E0B, #EF4444);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}
        p.subtitle {{
            color: #94A3B8;
            font-size: 15px;
            line-height: 1.6;
            max-width: 750px;
            margin: 0 auto;
        }}
        .grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 16px;
        }}
        .card {{
            background: #151C2C;
            border: 1.5px solid #2A364F;
            border-radius: 18px;
            padding: 20px;
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            gap: 12px;
            transition: all 0.2s;
        }}
        .card:hover {{
            transform: translateY(-3px);
            border-color: var(--accent, #F59E0B);
            box-shadow: 0 10px 25px rgba(0,0,0,0.3);
        }}
        .card-top {{
            width: 100%;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}
        .badge {{
            background: rgba(245, 158, 11, 0.15);
            color: var(--accent, #FBBF24);
            font-size: 11px;
            font-weight: 800;
            padding: 3px 10px;
            border-radius: 6px;
        }}
        .phonetic {{
            color: #94A3B8;
            font-size: 13px;
            font-weight: 700;
        }}
        .char {{
            font-family: 'Amiri', serif;
            font-size: 54px;
            font-weight: 700;
            color: var(--accent, #FBBF24);
            line-height: 1;
        }}
        .card-title {{
            font-size: 15px;
            font-weight: 800;
            color: #FFFFFF;
        }}
        .card-desc {{
            font-size: 12px;
            color: #94A3B8;
            line-height: 1.4;
            min-height: 34px;
        }}
        .play-btn {{
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.08);
            border: 1.5px solid var(--accent, #F59E0B);
            color: white;
            padding: 10px 16px;
            border-radius: 12px;
            font-weight: 800;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .play-btn:hover {{
            background: var(--accent, #F59E0B);
            color: #0F172A;
            transform: scale(1.02);
        }}
        .play-btn.playing {{
            background: var(--accent, #F59E0B) !important;
            color: #0F172A !important;
            box-shadow: 0 0 15px var(--accent, #F59E0B);
        }}
        .select-label {{
            display: flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            font-weight: 700;
            color: #E2E8F0;
            cursor: pointer;
            padding-top: 4px;
        }}
        .select-label input {{
            accent-color: #F59E0B;
            cursor: pointer;
        }}

        .bottom-bar {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(12px);
            border-top: 1px solid #2A364F;
            padding: 16px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 950px;
            margin: 0 auto;
            z-index: 1000;
        }}
        .selected-txt {{
            font-size: 14px;
            font-weight: 700;
            color: #E2E8F0;
        }}
        .btn-action {{
            background: linear-gradient(135deg, #F59E0B, #D97706);
            color: #0F172A;
            border: none;
            padding: 12px 24px;
            border-radius: 12px;
            font-weight: 800;
            font-size: 14px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .btn-action:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(245, 158, 11, 0.6);
        }}
        .toast {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: #10B981;
            color: white;
            padding: 14px 28px;
            border-radius: 12px;
            font-weight: 800;
            display: none;
            z-index: 2000;
        }}
    </style>
</head>
<body>
    <div class="toast" id="toast">✅ Choix copié dans le presse-papier !</div>

    <div class="container">
        <header>
            <h1>🎯 Résolution Spéciale : Hā' Ḍammah (هُ — « Hou » 100% Pur)</h1>
            <p class="subtitle">
                Toutes ces propositions ont été découpées depuis des mots comme <strong>« Hud-hud » (هُدْهُدْ)</strong> et <strong>« Houb-out » (هُبُوط)</strong> pour garantir qu'il n'y ait <strong>strictement aucun son « wa »</strong>.
            </p>
        </header>

        <div class="grid">
            {''.join(cards_html)}
        </div>
    </div>

    <div class="bottom-bar">
        <div class="selected-txt" id="selected_display">Aucune proposition sélectionnée</div>
        <button class="btn-action" onclick="copyChoice()">📋 Copier mon choix</button>
    </div>

    <script>
        let currentChoice = null;
        let currentChoiceTitle = "";

        function playAudio(id, btn) {{
            document.querySelectorAll('audio').forEach(a => {{ a.pause(); a.currentTime = 0; }});
            document.querySelectorAll('.play-btn').forEach(b => b.classList.remove('playing'));
            
            const audio = document.getElementById(id);
            if (audio) {{
                audio.play();
                if (btn) {{
                    btn.classList.add('playing');
                    audio.onended = () => btn.classList.remove('playing');
                }}
            }}
        }}

        function selectChoice(id, title) {{
            currentChoice = id;
            currentChoiceTitle = title;
            document.getElementById('selected_display').innerHTML = 'Choix : <strong style="color: #FBBF24">' + title + '</strong>';
        }}

        function copyChoice() {{
            if (!currentChoice) {{
                alert("Veuillez d'abord sélectionner une proposition en cochant la case.");
                return;
            }}
            const text = "Mon choix pour Hā' Ḍammah (هُ) est : " + currentChoiceTitle + " (ID: " + currentChoice + ")";
            navigator.clipboard.writeText(text).then(() => {{
                const toast = document.getElementById('toast');
                toast.style.display = 'block';
                setTimeout(() => {{ toast.style.display = 'none'; }}, 3000);
            }}).catch(() => {{
                alert(text);
            }});
        }}
    </script>
</body>
</html>
"""

with open("test_haa_damma_special.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Page mise à jour avec succès: test_haa_damma_special.html")
