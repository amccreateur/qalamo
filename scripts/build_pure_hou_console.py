import asyncio
import base64
import os
import sys
import subprocess
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

TEMP = 'scripts/temp_audio/pure_hou'
os.makedirs(TEMP, exist_ok=True)

PROPOSALS = [
    {
        "id": "hou_sukun_hedi",
        "title": "Option 1 — Hedi (هُوْ — Vraie voyelle Damma 'Hou')",
        "voice": "ar-TN-HediNeural",
        "text": "هُوْ",
        "rate": "-15%",
        "badge": "Hedi Recommandé ⭐",
        "desc": "Prononciation 'Hou' naturelle exactement comme Bou, Tou, Dou",
        "color": "#10B981"
    },
    {
        "id": "hou_sukun_moaz",
        "title": "Option 2 — Moaz (هُوْ — Vraie voyelle Damma 'Hou')",
        "voice": "ar-QA-MoazNeural",
        "text": "هُوْ",
        "rate": "-15%",
        "badge": "Moaz Recommandé ⭐",
        "desc": "Prononciation 'Hou' douce et posée comme les autres lettres de Moaz",
        "color": "#F59E0B"
    },
    {
        "id": "hou_sukun_hamed",
        "title": "Option 3 — Hamed (هُوْ — Vraie voyelle Damma 'Hou')",
        "voice": "ar-SA-HamedNeural",
        "text": "هُوْ",
        "rate": "-15%",
        "badge": "Hamed ⭐",
        "desc": "Prononciation 'Hou' saoudienne claire",
        "color": "#3B82F6"
    },
    {
        "id": "hou_sukun_shakir",
        "title": "Option 4 — Shakir (هُوْ — Vraie voyelle Damma 'Hou')",
        "voice": "ar-EG-ShakirNeural",
        "text": "هُوْ",
        "rate": "-15%",
        "badge": "Shakir",
        "desc": "Prononciation 'Hou' classique",
        "color": "#8B5CF6"
    },
    {
        "id": "hou_tatweel_hedi",
        "title": "Option 5 — Hedi (هـُو — Avec prolongement)",
        "voice": "ar-TN-HediNeural",
        "text": "هـُو",
        "rate": "-20%",
        "badge": "Hedi",
        "desc": "Format prolongé doux",
        "color": "#10B981"
    },
    {
        "id": "hou_tatweel_moaz",
        "title": "Option 6 — Moaz (هـُو — Avec prolongement)",
        "voice": "ar-QA-MoazNeural",
        "text": "هـُو",
        "rate": "-20%",
        "badge": "Moaz",
        "desc": "Format prolongé posé",
        "color": "#F59E0B"
    },
    {
        "id": "hou_direct_hedi",
        "title": "Option 7 — Hedi (هُـ — Court direct)",
        "voice": "ar-TN-HediNeural",
        "text": "هُـ",
        "rate": "-15%",
        "badge": "Court",
        "desc": "Format direct court",
        "color": "#EC4899"
    },
    {
        "id": "hou_direct_moaz",
        "title": "Option 8 — Moaz (هُـ — Court direct)",
        "voice": "ar-QA-MoazNeural",
        "text": "هُـ",
        "rate": "-15%",
        "badge": "Court",
        "desc": "Format direct court",
        "color": "#06B6D4"
    },
]

async def generate():
    results = []
    for p in PROPOSALS:
        raw = f"{TEMP}/{p['id']}_raw.mp3"
        clean = f"{TEMP}/{p['id']}.mp3"
        
        try:
            comm = edge_tts.Communicate(p['text'], p['voice'], rate=p['rate'])
            await comm.save(raw)
            cmd = [
                "ffmpeg", "-y", "-i", raw,
                "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-50dB,volume=6dB,alimiter=limit=0.95",
                clean
            ]
            subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            
            b64 = ""
            if os.path.exists(clean) and os.path.getsize(clean) > 0:
                with open(clean, "rb") as f:
                    b64 = base64.b64encode(f.read()).decode("utf-8")
                    
            results.append({**p, "b64": b64})
            print(f"[OK] {p['title']}")
        except Exception as e:
            print(f"[FAIL] {p['title']}: {e}")
            
    return results

def build_html(results):
    cards_html = []
    for r in results:
        cards_html.append(f"""
        <div class="card" style="--accent: {r['color']}">
            <div class="card-top">
                <span class="badge">{r['badge']}</span>
                <span class="phonetic">« Hou » (Damma)</span>
            </div>
            <div class="char">هُ</div>
            <div class="card-title">{r['title']}</div>
            <div class="card-desc">{r['desc']}</div>
            <button class="play-btn" onclick="playAudio('{r['id']}', this)">
                <span>▶</span> Écouter « Hou »
            </button>
            <label class="select-label">
                <input type="radio" name="hou_choice" value="{r['id']}" onchange="selectChoice('{r['id']}', '{r['title']}')">
                <span>Choisir cette version</span>
            </label>
            <audio id="{r['id']}" src="data:audio/mp3;base64,{r['b64']}"></audio>
        </div>
        """)

    html = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qalamo — Hā' Ḍammah (هُ — « Hou » Pur)</title>
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
            <h1>🎯 Résolution Spéciale : Hā' Ḍammah (هُ — « Hou » Pur)</h1>
            <p class="subtitle">
                Voici la véritable prononciation de la lettre <strong>Hā' avec Ḍammah (هُ — « Hou »)</strong>, exactement sur le même modèle que <em>« Bou » (بُ), « Tou » (تُ), « Dou » (دُ)</em>.
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
        
    print("\n[SUCCESS] Page mise à jour : test_haa_damma_special.html")

if __name__ == "__main__":
    res = asyncio.run(generate())
    build_html(res)
