import asyncio
import base64
import os
import sys
import subprocess
import edge_tts

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')

# 28 Arabic Letters with Damma
LETTERS = [
    {"id": "alif_damma", "char": "أُ", "name": "Alif Ḍammah", "text_direct": "أُ", "text_alt": "أُو", "category": "Voyelle pure", "phonetic": "’Ou"},
    {"id": "ba_damma", "char": "بُ", "name": "Bā' Ḍammah", "text_direct": "بُـ", "text_alt": "بُو", "category": "Labiale", "phonetic": "Bou"},
    {"id": "ta_damma", "char": "تُ", "name": "Tā' Ḍammah", "text_direct": "تُـ", "text_alt": "تُو", "category": "Dentale fine", "phonetic": "Tou"},
    {"id": "tha_damma", "char": "ثُ", "name": "Thā' Ḍammah", "text_direct": "ثُـ", "text_alt": "ثُو", "category": "Interdentale", "phonetic": "Thou"},
    {"id": "jeem_damma", "char": "جُ", "name": "Jeem Ḍammah", "text_direct": "جُـ", "text_alt": "جُو", "category": "Palatale", "phonetic": "Djou"},
    {"id": "hha_damma", "char": "حُ", "name": "Ḥā' Ḍammah", "text_direct": "حُـ", "text_alt": "حُو", "category": "Gorge douce", "phonetic": "Ḥou"},
    {"id": "kha_damma", "char": "خُ", "name": "Khā' Ḍammah", "text_direct": "خُـ", "text_alt": "خُو", "category": "Emphatique / Gutturale", "phonetic": "Khou"},
    {"id": "dal_damma", "char": "دُ", "name": "Dāl Ḍammah", "text_direct": "دُ", "text_alt": "دُو", "category": "Dentale fine", "phonetic": "Dou"},
    {"id": "dhal_damma", "char": "ذُ", "name": "Dhāl Ḍammah", "text_direct": "ذُ", "text_alt": "ذُو", "category": "Interdentale", "phonetic": "Dhou"},
    {"id": "ra_damma", "char": "رُ", "name": "Rā' Ḍammah", "text_direct": "رُ", "text_alt": "رُو", "category": "Roulée sonore", "phonetic": "Rou"},
    {"id": "zay_damma", "char": "زُ", "name": "Zāy Ḍammah", "text_direct": "زُ", "text_alt": "زُو", "category": "Sifflante sonore", "phonetic": "Zou"},
    {"id": "seen_damma", "char": "سُ", "name": "Sīn Ḍammah", "text_direct": "سُـ", "text_alt": "سُو", "category": "Sifflante fine", "phonetic": "Sou"},
    {"id": "sheen_damma", "char": "شُ", "name": "Shīn Ḍammah", "text_direct": "شُـ", "text_alt": "شُو", "category": "Chuintante", "phonetic": "Chou"},
    {"id": "sad_damma", "char": "صُ", "name": "Ṣād Ḍammah", "text_direct": "صُـ", "text_alt": "صُو", "category": "Emphatique", "phonetic": "Ṣou"},
    {"id": "dad_damma", "char": "ضُ", "name": "Ḍād Ḍammah", "text_direct": "ضُـ", "text_alt": "ضُو", "category": "Emphatique", "phonetic": "Ḍou"},
    {"id": "ttaa_damma", "char": "طُ", "name": "Ṭā' Ḍammah", "text_direct": "طُـ", "text_alt": "طُو", "category": "Emphatique", "phonetic": "Ṭou"},
    {"id": "zha_damma", "char": "ظُ", "name": "Ẓā' Ḍammah", "text_direct": "ظُـ", "text_alt": "ظُو", "category": "Emphatique", "phonetic": "Ẓou"},
    {"id": "ayn_damma", "char": "عُ", "name": "ʿAyn Ḍammah", "text_direct": "عُـ", "text_alt": "عُو", "category": "Gorge profonde", "phonetic": "ʿOu"},
    {"id": "ghayn_damma", "char": "غُ", "name": "Ghayn Ḍammah", "text_direct": "غُـ", "text_alt": "غُو", "category": "Emphatique", "phonetic": "Ghou"},
    {"id": "fa_damma", "char": "فُ", "name": "Fā' Ḍammah", "text_direct": "فُـ", "text_alt": "فُو", "category": "Labio-dentale", "phonetic": "Fou"},
    {"id": "qaf_damma", "char": "قُ", "name": "Qāf Ḍammah", "text_direct": "قُـ", "text_alt": "قُو", "category": "Uvulaire profonde", "phonetic": "Qou"},
    {"id": "kaf_damma", "char": "كُ", "name": "Kāf Ḍammah", "text_direct": "كُـ", "text_alt": "كُو", "category": "Palatale fine", "phonetic": "Kou"},
    {"id": "lam_damma", "char": "لُ", "name": "Lām Ḍammah", "text_direct": "لُـ", "text_alt": "لُو", "category": "Liquide", "phonetic": "Lou"},
    {"id": "meem_damma", "char": "مُ", "name": "Mīm Ḍammah", "text_direct": "مُـ", "text_alt": "مُو", "category": "Nasale labiale", "phonetic": "Mou"},
    {"id": "noon_damma", "char": "نُ", "name": "Nūn Ḍammah", "text_direct": "نُـ", "text_alt": "نُو", "category": "Nasale dentale", "phonetic": "Nou"},
    {"id": "haa_damma", "char": "هُ", "name": "Hā' Ḍammah", "text_direct": "هُـ", "text_alt": "هُو", "category": "Laryngale douce", "phonetic": "Hou"},
    {"id": "waw_damma", "char": "وُ", "name": "Wāw Ḍammah", "text_direct": "وُ", "text_alt": "وُو", "category": "Semi-voyelle", "phonetic": "Wou"},
    {"id": "yaa_damma", "char": "يُ", "name": "Yā' Ḍammah", "text_direct": "يُـ", "text_alt": "يُو", "category": "Semi-voyelle", "phonetic": "You"},
]

VOICES = [
    {"key": "shakir", "name": "Shakir", "voice": "ar-EG-ShakirNeural", "badge": "Shakir", "color": "#3B82F6", "rate": "-22%"},
    {"key": "hamed", "name": "Hamed", "voice": "ar-SA-HamedNeural", "badge": "Hamed", "color": "#10B981", "rate": "-22%"},
    {"key": "moaz", "name": "Moaz", "voice": "ar-QA-MoazNeural", "badge": "Moaz", "color": "#F59E0B", "rate": "-22%"},
    {"key": "hedi", "name": "Hedi", "voice": "ar-TN-HediNeural", "badge": "Hedi", "color": "#8B5CF6", "rate": "-22%"},
]

CACHE_DIR = "scripts/temp_audio/damma_proposals"
os.makedirs(CACHE_DIR, exist_ok=True)

async def generate_proposal(text_direct: str, text_alt: str, voice: str, rate: str, out_path: str):
    raw_path = out_path.replace(".mp3", "_raw.mp3")
    
    # Prioritize sustained text_alt (e.g. بُو, تُو) with slower rate for clear, prolonged vowel duration
    for t in [text_alt, text_direct, text_direct.replace("ـ", "")]:
        try:
            communicate = edge_tts.Communicate(t, voice, rate=rate)
            await communicate.save(raw_path)
            if os.path.exists(raw_path) and os.path.getsize(raw_path) > 300:
                cmd = [
                    "ffmpeg", "-y", "-i", raw_path,
                    "-af", "silenceremove=start_periods=1:start_duration=0.01:start_threshold=-55dB,volume=6dB,alimiter=limit=0.95",
                    out_path
                ]
                subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                if os.path.exists(raw_path):
                    os.remove(raw_path)
                return
        except Exception:
            continue

def get_b64(path: str) -> str:
    if os.path.exists(path) and os.path.getsize(path) > 0:
        with open(path, "rb") as f:
            return base64.b64encode(f.read()).decode("utf-8")
    return ""

async def main():
    print("Génération des propositions audio pour les 28 lettres avec Ḍammah (ـُ)...")
    
    for item in LETTERS:
        for v in VOICES:
            out_file = f"{CACHE_DIR}/{item['id']}_{v['key']}.mp3"
            await generate_proposal(item["text_direct"], item["text_alt"], v["voice"], v["rate"], out_file)
            print(f"  [OK] {item['name']} ({v['key']})")

    print("\nAssemblage de la page HTML interactive Damma...")
    
    cards_html = []
    
    for idx, item in enumerate(LETTERS, 1):
        # Current app audio
        current_path = f"assets/audio/generated/{item['id']}.mp3"
        current_b64 = get_b64(current_path)
        
        proposals_b64 = {}
        for v in VOICES:
            v_path = f"{CACHE_DIR}/{item['id']}_{v['key']}.mp3"
            proposals_b64[v['key']] = get_b64(v_path)
        
        btn_current = f"""
        <button class="audio-btn btn-current" onclick="playAudio('{item['id']}_current', this)">
            <span class="btn-icon">▶</span>
            <span class="btn-label">Actuel</span>
        </button>
        <audio id="{item['id']}_current" src="data:audio/mp3;base64,{current_b64}"></audio>
        """ if current_b64 else ""

        btns_proposals = []
        for v in VOICES:
            b64 = proposals_b64[v['key']]
            if b64:
                btns_proposals.append(f"""
                <div class="voice-opt">
                    <button class="audio-btn" style="--btn-color: {v['color']}" onclick="playAudio('{item['id']}_{v['key']}', this)">
                        <span class="btn-icon">▶</span>
                        <span class="btn-label">{v['badge']}</span>
                    </button>
                    <label class="radio-label">
                        <input type="radio" name="choice_{item['id']}" value="{v['key']}" onchange="recordChoice('{item['id']}', '{v['badge']}', '{item['name']}')">
                        <span>Choisir</span>
                    </label>
                    <audio id="{item['id']}_{v['key']}" src="data:audio/mp3;base64,{b64}"></audio>
                </div>
                """)
        
        card = f"""
        <div class="letter-card" data-category="{item['category']}">
            <div class="letter-header">
                <div class="letter-badge">#{idx}</div>
                <div class="letter-char">{item['char']}</div>
                <div class="letter-info">
                    <div class="letter-title">{item['name']}</div>
                    <div class="letter-meta">
                        <span class="pill-category">{item['category']}</span>
                        <span class="pill-phonetic">{item['phonetic']}</span>
                    </div>
                </div>
            </div>

            <div class="audio-grid">
                <div class="voice-opt current-opt">
                    {btn_current}
                    <label class="radio-label">
                        <input type="radio" name="choice_{item['id']}" value="current" checked onchange="recordChoice('{item['id']}', 'Actuel', '{item['name']}')">
                        <span>Garder actuel</span>
                    </label>
                </div>
                {''.join(btns_proposals)}
            </div>
            
            <div class="choice-indicator" id="choice_badge_{item['id']}">
                Sélection : <strong>Actuel</strong>
            </div>
        </div>
        """
        cards_html.append(card)

    html_content = f"""<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Qalamo — Les 28 Lettres avec Ḍammah (ـُ) : Console de Choix Audio</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Amiri:wght@700&family=Plus+Jakarta+Sans:wght@500;700;800&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg-main: #0B0F19;
            --bg-card: #151C2C;
            --bg-card-hover: #1A2338;
            --border-card: #2A364F;
            --primary: #F59E0B;
            --primary-dark: #D97706;
            --success: #10B981;
            --blue: #3B82F6;
            --purple: #8B5CF6;
            --text-main: #F8FAFC;
            --text-muted: #94A3B8;
        }}
        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
            font-family: 'Plus Jakarta Sans', -apple-system, BlinkMacSystemFont, sans-serif;
        }}
        body {{
            background: var(--bg-main);
            color: var(--text-main);
            padding: 30px 16px 130px;
            display: flex;
            justify-content: center;
        }}
        .container {{
            width: 100%;
            max-width: 1200px;
        }}
        header {{
            text-align: center;
            margin-bottom: 28px;
            background: linear-gradient(135deg, #1E293B, #0F172A);
            border: 1px solid var(--border-card);
            padding: 28px 20px;
            border-radius: 20px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        }}
        h1 {{
            font-size: 28px;
            font-weight: 800;
            background: linear-gradient(135deg, #FBBF24, #F59E0B, #EF4444);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 10px;
        }}
        p.subtitle {{
            color: var(--text-muted);
            font-size: 15px;
            line-height: 1.6;
            max-width: 800px;
            margin: 0 auto;
        }}
        .summary-bar {{
            margin-top: 18px;
            display: flex;
            gap: 12px;
            justify-content: center;
            flex-wrap: wrap;
        }}
        .stat-pill {{
            background: rgba(255, 255, 255, 0.06);
            border: 1px solid rgba(255, 255, 255, 0.1);
            padding: 6px 16px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 700;
            color: #E2E8F0;
        }}
        
        .filter-tabs {{
            display: flex;
            gap: 8px;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 24px;
        }}
        .filter-btn {{
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            color: var(--text-muted);
            padding: 8px 18px;
            border-radius: 12px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .filter-btn.active, .filter-btn:hover {{
            background: var(--primary);
            color: #0F172A;
            border-color: var(--primary);
        }}

        .letters-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(350px, 1fr));
            gap: 16px;
        }}
        .letter-card {{
            background: var(--bg-card);
            border: 1px solid var(--border-card);
            border-radius: 18px;
            padding: 18px;
            display: flex;
            flex-direction: column;
            gap: 14px;
            transition: transform 0.2s, border-color 0.2s;
        }}
        .letter-card:hover {{
            transform: translateY(-2px);
            border-color: var(--primary);
            background: var(--bg-card-hover);
        }}
        .letter-header {{
            display: flex;
            align-items: center;
            gap: 14px;
        }}
        .letter-badge {{
            font-size: 12px;
            font-weight: 800;
            color: var(--text-muted);
            background: rgba(255, 255, 255, 0.05);
            padding: 4px 8px;
            border-radius: 8px;
        }}
        .letter-char {{
            font-family: 'Amiri', serif;
            font-size: 48px;
            font-weight: 700;
            color: #FBBF24;
            line-height: 1;
            min-width: 54px;
            text-align: center;
        }}
        .letter-info {{
            flex: 1;
        }}
        .letter-title {{
            font-size: 17px;
            font-weight: 800;
            color: #FFFFFF;
            margin-bottom: 4px;
        }}
        .letter-meta {{
            display: flex;
            gap: 6px;
            flex-wrap: wrap;
        }}
        .pill-category {{
            background: rgba(245, 158, 11, 0.15);
            color: #FDE68A;
            font-size: 11px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
        }}
        .pill-phonetic {{
            background: rgba(16, 185, 129, 0.15);
            color: #6EE7B7;
            font-size: 11px;
            font-weight: 700;
            padding: 2px 8px;
            border-radius: 6px;
        }}

        .audio-grid {{
            display: grid;
            grid-template-columns: repeat(2, 1fr);
            gap: 10px;
            background: rgba(0, 0, 0, 0.25);
            padding: 12px;
            border-radius: 14px;
        }}
        .voice-opt {{
            display: flex;
            flex-direction: column;
            gap: 6px;
            align-items: center;
        }}
        .current-opt {{
            grid-column: span 2;
            flex-direction: row;
            justify-content: space-between;
            padding-bottom: 8px;
            border-bottom: 1px dashed var(--border-card);
            margin-bottom: 4px;
        }}
        .audio-btn {{
            width: 100%;
            display: flex;
            align-items: center;
            justify-content: center;
            gap: 8px;
            background: rgba(255, 255, 255, 0.07);
            border: 1.5px solid var(--btn-color, var(--border-card));
            color: #FFFFFF;
            padding: 8px 12px;
            border-radius: 10px;
            font-weight: 700;
            font-size: 13px;
            cursor: pointer;
            transition: all 0.15s;
        }}
        .audio-btn:hover {{
            background: var(--btn-color, var(--primary));
            color: #FFFFFF;
            transform: scale(1.02);
        }}
        .audio-btn.playing {{
            background: var(--btn-color, var(--primary)) !important;
            box-shadow: 0 0 12px var(--btn-color, var(--primary));
        }}
        .btn-current {{
            --btn-color: #64748B;
            width: auto;
            padding: 6px 14px;
        }}
        .btn-icon {{
            font-size: 11px;
        }}
        .radio-label {{
            display: flex;
            align-items: center;
            gap: 5px;
            font-size: 11px;
            font-weight: 700;
            color: var(--text-muted);
            cursor: pointer;
        }}
        .radio-label input {{
            cursor: pointer;
            accent-color: var(--primary);
        }}
        .choice-indicator {{
            font-size: 12px;
            color: var(--text-muted);
            text-align: right;
            padding-top: 4px;
        }}
        .choice-indicator strong {{
            color: #FBBF24;
        }}

        /* Floating bottom bar */
        .bottom-bar {{
            position: fixed;
            bottom: 0;
            left: 0;
            right: 0;
            background: rgba(15, 23, 42, 0.95);
            backdrop-filter: blur(12px);
            border-top: 1px solid var(--border-card);
            padding: 16px 20px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            max-width: 1200px;
            margin: 0 auto;
            z-index: 1000;
            box-shadow: 0 -10px 30px rgba(0,0,0,0.5);
        }}
        .bottom-summary {{
            font-size: 14px;
            font-weight: 700;
            color: #E2E8F0;
        }}
        .action-btns {{
            display: flex;
            gap: 12px;
        }}
        .btn-action {{
            background: linear-gradient(135deg, var(--primary), var(--primary-dark));
            color: #0F172A;
            border: none;
            padding: 12px 24px;
            border-radius: 12px;
            font-weight: 800;
            font-size: 14px;
            cursor: pointer;
            box-shadow: 0 4px 12px rgba(245, 158, 11, 0.4);
            transition: all 0.2s;
        }}
        .btn-action:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 18px rgba(245, 158, 11, 0.6);
        }}
        .copied-toast {{
            position: fixed;
            top: 20px;
            right: 20px;
            background: var(--success);
            color: white;
            padding: 14px 28px;
            border-radius: 12px;
            font-weight: 800;
            box-shadow: 0 10px 25px rgba(16, 185, 129, 0.4);
            display: none;
            z-index: 2000;
        }}
    </style>
</head>
<body>
    <div class="copied-toast" id="toast">✅ Vos choix ont été copiés ! Vous pouvez les coller directement dans le chat.</div>

    <div class="container">
        <header>
            <h1>Console d'Écoute : Les 28 Lettres avec Ḍammah (ـُ)</h1>
            <p class="subtitle">
                Écoutez et comparez les différentes voix pour chaque lettre de l'alphabet avec la voyelle <strong>Ḍammah (ou)</strong> :
                comparez la version <strong>Actuelle</strong> avec <strong>Shakir</strong> (Saoudien classique), <strong>Hamed</strong> (Saoudien clair), <strong>Moaz</strong> (Posé) et <strong>Hedi</strong> (Tunisien articulé).
            </p>
            <div class="summary-bar">
                <div class="stat-pill">📚 28 Lettres Complètes</div>
                <div class="stat-pill">🎙️ 5 Écoutes par Lettre (140 Audios)</div>
                <div class="stat-pill">🔊 Studio HD Pure Syllable</div>
            </div>
        </header>

        <div class="filter-tabs">
            <button class="filter-btn active" onclick="filterCategory('all', this)">Toutes (28)</button>
            <button class="filter-btn" onclick="filterCategory('Emphatique', this)">Emphatiques (صُ, ضُ, طُ, ظُ, غُ, خُ, قُ)</button>
            <button class="filter-btn" onclick="filterCategory('Gorge', this)">Gorge (حُ, عُ, هُ)</button>
            <button class="filter-btn" onclick="filterCategory('Sifflante', this)">Sifflantes (سُ, زُ, شُ)</button>
            <button class="filter-btn" onclick="filterCategory('Dentale', this)">Dentales (تُ, دُ, ثُ, ذُ)</button>
        </div>

        <div class="letters-grid">
            {''.join(cards_html)}
        </div>
    </div>

    <div class="bottom-bar">
        <div class="bottom-summary" id="bottom_counter">
            28 / 28 lettres disponibles (Toutes sur "Actuel" par défaut)
        </div>
        <div class="action-btns">
            <button class="btn-action" onclick="copyChoices()">📋 Copier mes choix pour l'assistant</button>
        </div>
    </div>

    <script>
        let userChoices = {{}};

        function playAudio(id, btn) {{
            document.querySelectorAll('audio').forEach(a => {{
                a.pause();
                a.currentTime = 0;
            }});
            document.querySelectorAll('.audio-btn').forEach(b => b.classList.remove('playing'));
            
            const audio = document.getElementById(id);
            if (audio) {{
                audio.play();
                if (btn) {{
                    btn.classList.add('playing');
                    audio.onended = () => btn.classList.remove('playing');
                }}
            }}
        }}

        function recordChoice(letterId, voiceName, letterName) {{
            userChoices[letterId] = {{ voice: voiceName, name: letterName }};
            const badge = document.getElementById('choice_badge_' + letterId);
            if (badge) {{
                badge.innerHTML = 'Sélection : <strong style="color: #FBBF24">' + voiceName + '</strong>';
            }}
            updateBottomCounter();
        }}

        function updateBottomCounter() {{
            const changed = Object.values(userChoices).filter(c => c.voice !== 'Actuel').length;
            document.getElementById('bottom_counter').innerText = 
                changed > 0 ? (changed + ' modification(s) sélectionnée(s) sur 28 lettres') : '28 lettres (Toutes sur "Actuel" par défaut)';
        }}

        function filterCategory(cat, btn) {{
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            document.querySelectorAll('.letter-card').forEach(card => {{
                if (cat === 'all') {{
                    card.style.display = 'flex';
                }} else {{
                    const cardCat = card.getAttribute('data-category') || '';
                    if (cardCat.includes(cat)) {{
                        card.style.display = 'flex';
                    }} else {{
                        card.style.display = 'none';
                    }}
                }}
            }});
        }}

        function copyChoices() {{
            let text = "Voici mes préférences pour les lettres avec Dammah :\\n\\n";
            let changedCount = 0;
            
            document.querySelectorAll('.letter-card').forEach(card => {{
                const input = card.querySelector('input[type="radio"]:checked');
                const title = card.querySelector('.letter-title').innerText;
                const char = card.querySelector('.letter-char').innerText;
                const val = input ? input.value : 'current';
                
                let voiceName = 'Actuel';
                if (val === 'shakir') voiceName = 'Shakir';
                if (val === 'hamed') voiceName = 'Hamed';
                if (val === 'moaz') voiceName = 'Moaz';
                if (val === 'hedi') voiceName = 'Hedi';
                
                text += "- " + char + " (" + title + ") : " + voiceName + "\\n";
                if (val !== 'current') changedCount++;
            }});

            navigator.clipboard.writeText(text).then(() => {{
                const toast = document.getElementById('toast');
                toast.style.display = 'block';
                setTimeout(() => {{ toast.style.display = 'none'; }}, 3500);
            }}).catch(() => {{
                alert(text);
            }});
        }}
    </script>
</body>
</html>
    """

    out_html = "test_all_damma_proposals.html"
    with open(out_html, "w", encoding="utf-8") as f:
        f.write(html_content)
    
    print(f"\n[SUCCESS] Console Damma créée: {out_html}")

if __name__ == "__main__":
    asyncio.run(main())

